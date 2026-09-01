"""Validated, deterministic role and runtime-candidate selection."""

from __future__ import annotations

import hashlib
import json
import math
from typing import Any

STAGES = {
    "architecture": "architect",
    "design": "designer",
    "documentation": "documenter",
    "fix": "fixer",
    "implementation": "implementer",
    "integration": "implementer",
    "research": "researcher",
    "review": "reviewer",
    "validation": "validator",
}


class RoutingError(ValueError):
    pass


def _score(value: Any, field: str) -> float:
    if not isinstance(value, (int, float)) or isinstance(value, bool) or not math.isfinite(value) or not 1 <= value <= 5:
        raise RoutingError(f"{field} must be a number from 1 through 5")
    return float(value)


def _label(value: Any, field: str, *, maximum: int = 256) -> str:
    if (
        not isinstance(value, str)
        or not value.strip()
        or len(value) > maximum
        or any(0xD800 <= ord(character) <= 0xDFFF for character in value)
    ):
        raise RoutingError(f"{field} must be a non-blank bounded string")
    return value


def _non_negative(value: Any, field: str) -> float:
    if not isinstance(value, (int, float)) or isinstance(value, bool) or not math.isfinite(value) or value < 0:
        raise RoutingError(f"{field} must be a finite non-negative number")
    return float(value)


def validate_task(value: Any) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise RoutingError("task file must contain one JSON object")
    expected = {
        "summary", "stage", "complexity", "ambiguity", "criticality", "coupling", "novelty",
        "determinism",
    }
    unknown = set(value) - expected
    missing = expected - set(value)
    if unknown or missing:
        raise RoutingError(
            "task fields are invalid"
            + ("; missing " + ", ".join(sorted(missing)) if missing else "")
            + ("; unknown " + ", ".join(sorted(unknown)) if unknown else "")
        )
    result = {"summary": _label(value["summary"], "summary", maximum=32_768), "stage": value["stage"]}
    if not isinstance(value["stage"], str) or value["stage"] not in STAGES:
        raise RoutingError("stage is not supported")
    for field in ("complexity", "ambiguity", "criticality", "coupling", "novelty", "determinism"):
        result[field] = _score(value[field], field)
    return result


def validate_profile(value: Any) -> dict[str, Any]:
    if value is None:
        return {"candidates": [], "budget": "balanced"}
    if not isinstance(value, dict):
        raise RoutingError("profile file must contain one JSON object")
    expected = {"candidates", "budget"}
    if set(value) - expected:
        raise RoutingError("profile contains unknown fields: " + ", ".join(sorted(set(value) - expected)))
    raw_candidates = value.get("candidates", [])
    if not isinstance(raw_candidates, list) or len(raw_candidates) > 128:
        raise RoutingError("candidates must be a list with at most 128 entries")
    candidates = []
    identities: set[tuple[str, str | None]] = set()
    for index, raw in enumerate(raw_candidates):
        if not isinstance(raw, dict) or set(raw) != {"model", "effort", "capacity", "relative_cost"}:
            raise RoutingError(f"candidates[{index}] has invalid fields")
        model = _label(raw["model"], f"candidates[{index}].model")
        effort = raw["effort"]
        if effort is not None:
            effort = _label(effort, f"candidates[{index}].effort")
        identity = (model, effort)
        if identity in identities:
            raise RoutingError("candidates must contain unique model/effort pairs")
        identities.add(identity)
        candidates.append(
            {
                "model": model,
                "effort": effort,
                "capacity": _non_negative(raw["capacity"], f"candidates[{index}].capacity"),
                "relative_cost": _non_negative(raw["relative_cost"], f"candidates[{index}].relative_cost"),
            }
        )
    budget = value.get("budget", "balanced")
    if budget not in ("value", "balanced", "quality"):
        raise RoutingError("budget must be value, balanced, or quality")
    return {"candidates": candidates, "budget": budget}


def choose(task_value: Any, profile_value: Any = None) -> dict[str, Any]:
    task = validate_task(task_value)
    profile = validate_profile(profile_value)
    required = (
        task["complexity"] * 0.23
        + task["ambiguity"] * 0.20
        + task["criticality"] * 0.24
        + task["coupling"] * 0.14
        + task["novelty"] * 0.14
        + (6 - task["determinism"]) * 0.05
    )
    if task["stage"] in ("architecture", "review"):
        required += 0.3
    if task["stage"] in ("documentation", "validation"):
        required -= 0.2
    cost_weight = {"value": 0.35, "balanced": 0.14, "quality": 0.04}[profile["budget"]]
    alternatives = []
    for candidate in profile["candidates"]:
        margin = candidate["capacity"] - required
        score = margin - cost_weight * candidate["relative_cost"] - (
            abs(margin) * 0.08 if margin >= 0 else abs(margin) * 3.0
        )
        alternatives.append(
            {
                **candidate,
                "capacity": round(candidate["capacity"], 3),
                "required_capacity": round(required, 3),
                "margin": round(margin, 3),
                "relative_cost": round(candidate["relative_cost"], 3),
                "score": round(score, 3),
                "viable": margin >= 0,
            }
        )
    alternatives.sort(
        key=lambda item: (
            -int(item["viable"]),
            -item["score"],
            item["relative_cost"],
            item["model"],
            item["effort"] or "",
        )
    )
    canonical = json.dumps(task, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    role = STAGES[task["stage"]]
    if alternatives:
        selected = alternatives[0]
        route = {"role": role, "model": selected["model"], "effort": selected["effort"]}
        selection = (
            "highest-ranked viable runtime candidate"
            if selected["viable"]
            else "highest-ranked runtime fallback because no candidate met required capacity"
        )
        rationale = (
            f"{task['stage']} requires capacity {required:.2f}; selected the {selection} "
            f"under the {profile['budget']} profile"
        )
    else:
        route = {"role": role, "model": None, "effort": None}
        rationale = f"{task['stage']} has no runtime candidate catalog; inherit the parent model and effort"
    return {
        "task_digest": hashlib.sha256(canonical).hexdigest(),
        "route": route,
        "rationale": rationale,
        "inputs": task,
        "profile": profile,
        "alternatives": alternatives[:5],
        "caveat": "Candidate capacity and relative cost are caller-supplied planning heuristics.",
    }
