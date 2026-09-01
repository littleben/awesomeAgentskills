"""Command adapter for task routing."""

from __future__ import annotations

import argparse
import json
import pathlib
import sys
from typing import Any, Sequence

from coordinator.cli.outcome import OutcomeArgumentParser, emit, parse_invocation
from coordinator.routing.selector import RoutingError, choose

MAX_JSON_BYTES = 4 * 1024 * 1024


def _json_file(path: str) -> Any:
    def pairs(items: list[tuple[str, Any]]) -> dict[str, Any]:
        result: dict[str, Any] = {}
        for key, value in items:
            if key in result:
                raise RoutingError(f"JSON input contains duplicate key {key!r}")
            result[key] = value
        return result

    def constant(value: str) -> None:
        raise RoutingError(f"JSON input contains non-standard numeric constant {value}")

    try:
        if path == "-":
            text = sys.stdin.read(MAX_JSON_BYTES + 1)
            size = len(text.encode("utf-8"))
        else:
            with pathlib.Path(path).open("rb") as handle:
                raw = handle.read(MAX_JSON_BYTES + 1)
            size = len(raw)
            text = raw.decode("utf-8")
        if size > MAX_JSON_BYTES:
            raise RoutingError(f"JSON input exceeds {MAX_JSON_BYTES} UTF-8 bytes")
        return json.loads(text, object_pairs_hook=pairs, parse_constant=constant)
    except RoutingError:
        raise
    except (OSError, UnicodeDecodeError, UnicodeEncodeError, json.JSONDecodeError, RecursionError) as exc:
        raise RoutingError(f"unable to read valid UTF-8 JSON from {path}") from exc


def build_parser() -> argparse.ArgumentParser:
    parser = OutcomeArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    choose_parser = sub.add_parser("choose")
    choose_parser.add_argument("--task-file", required=True)
    choose_parser.add_argument("--profile-file")
    choose_parser.add_argument("--json", action="store_true")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args, invalid = parse_invocation(build_parser(), argv)
    if args is None:
        return invalid
    try:
        result = choose(_json_file(args.task_file), _json_file(args.profile_file) if args.profile_file else None)
        return emit(args.command, code="route_selected", data=result, as_json=args.json)
    except RoutingError as exc:
        return emit(args.command, code="invalid_routing_input", data={"message": str(exc)}, exit_code=2, as_json=args.json)
