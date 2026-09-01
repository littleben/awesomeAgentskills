"""Stable CLI outcomes shared by Coordinator command adapters."""

from __future__ import annotations

import argparse
import json
import sys
from typing import Any, Sequence


class InvocationError(ValueError):
    pass


class OutcomeArgumentParser(argparse.ArgumentParser):
    """Argument parser whose public boundary can emit the stable outcome schema."""

    def add_subparsers(self, **kwargs: Any) -> argparse._SubParsersAction[Any]:
        kwargs.setdefault("parser_class", type(self))
        return super().add_subparsers(**kwargs)

    def error(self, _message: str) -> None:
        raise InvocationError("invalid command line")


def emit(
    command: str,
    *,
    code: str,
    data: Any = None,
    warnings: list[str] | None = None,
    exit_code: int = 0,
    as_json: bool = False,
) -> int:
    payload = {
        "command": command,
        "status": "ok" if exit_code == 0 else "negative" if exit_code == 1 else "error",
        "code": code,
        "data": data if data is not None else {},
        "warnings": warnings or [],
    }
    if as_json:
        print(json.dumps(payload, indent=2, sort_keys=True))
    elif exit_code in (0, 1):
        print(f"{command}: {code.replace('_', ' ')}")
        if isinstance(data, dict):
            for key, value in data.items():
                if value is not None:
                    print(f"{key}={value}")
        for warning in warnings or []:
            print(f"warning: {warning}", file=sys.stderr)
    else:
        message = data.get("message", code) if isinstance(data, dict) else code
        print(f"{command}: {message}", file=sys.stderr)
    return exit_code


def parse_invocation(
    parser: argparse.ArgumentParser,
    argv: Sequence[str] | None,
) -> tuple[argparse.Namespace | None, int]:
    arguments = list(sys.argv[1:] if argv is None else argv)
    try:
        return parser.parse_args(arguments), 0
    except InvocationError as exc:
        command = next((item for item in arguments if item and not item.startswith("-")), "unknown")
        return None, emit(
            command,
            code="invalid_invocation",
            data={"message": str(exc)},
            exit_code=2,
            as_json="--json" in arguments,
        )
