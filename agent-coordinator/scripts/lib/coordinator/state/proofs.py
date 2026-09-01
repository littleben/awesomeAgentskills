"""Bounded shell execution for durable node proof commands."""

from __future__ import annotations

import os
import signal
import subprocess
import threading
from dataclasses import dataclass


PROOF_COMMAND_TIMEOUT_SECONDS = 300
PROOF_OUTPUT_MAX_BYTES = 32 * 1024


class ProofExecutionError(RuntimeError):
    """A proof command could not produce a bounded, trustworthy result."""


@dataclass(frozen=True)
class ProofCommandResult:
    exit_code: int
    output: str


def _stop_process(process: subprocess.Popen[bytes]) -> None:
    if process.poll() is not None:
        return
    try:
        if os.name != "nt":
            os.killpg(process.pid, signal.SIGKILL)
        else:
            subprocess.run(
                ["taskkill", "/F", "/T", "/PID", str(process.pid)],
                check=False,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                timeout=5,
            )
    except OSError:
        pass
    except subprocess.TimeoutExpired:
        pass
    try:
        process.kill()
    except OSError:
        pass


def run_proof_command(
    command: str,
    *,
    repository: str,
    timeout: int = PROOF_COMMAND_TIMEOUT_SECONDS,
    output_limit: int = PROOF_OUTPUT_MAX_BYTES,
) -> ProofCommandResult:
    """Run one shell command while draining and bounding merged output."""
    try:
        process = subprocess.Popen(
            command,
            cwd=repository,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            start_new_session=os.name != "nt",
        )
    except (OSError, ValueError) as exc:
        raise ProofExecutionError("unable to start proof command") from exc

    assert process.stdout is not None
    output = bytearray()
    overflow = threading.Event()
    read_error: list[Exception] = []

    def drain() -> None:
        try:
            while chunk := process.stdout.read(8192):
                remaining = output_limit + 1 - len(output)
                if remaining > 0:
                    output.extend(chunk[:remaining])
                if len(output) > output_limit or len(chunk) > remaining:
                    overflow.set()
                    _stop_process(process)
        except (OSError, ValueError) as exc:
            read_error.append(exc)

    reader = threading.Thread(
        target=drain, name="coordinator-proof-output", daemon=True
    )
    reader.start()
    try:
        process.wait(timeout=timeout)
    except subprocess.TimeoutExpired as exc:
        _stop_process(process)
        process.wait()
        reader.join(timeout=1)
        process.stdout.close()
        raise ProofExecutionError(
            f"proof command exceeded the {timeout}-second timeout"
        ) from exc
    reader.join(timeout=1)
    process.stdout.close()
    if reader.is_alive() or read_error:
        raise ProofExecutionError("unable to capture proof command output")
    if overflow.is_set():
        raise ProofExecutionError(f"proof command output exceeds {output_limit} bytes")
    try:
        decoded = bytes(output).decode("utf-8")
    except UnicodeDecodeError as exc:
        raise ProofExecutionError("proof command output is not valid UTF-8") from exc
    return ProofCommandResult(exit_code=process.returncode, output=decoded)
