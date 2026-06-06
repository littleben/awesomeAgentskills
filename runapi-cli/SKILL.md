---
name: RunAPI CLI
description: Use when an AI agent needs to generate images, videos, music, or audio through RunAPI, pass JSON request bodies, poll async model jobs, inspect auth, or script RunAPI from a terminal, server, or CI job.
---

# RunAPI CLI

Use the `runapi` CLI when an agent needs to run RunAPI model jobs from a shell. It is useful for AI image, video, music/audio, and other model API workflows where requests are easier to express as JSON and results may complete asynchronously.

## When to Use This Skill

- Generate AI images, videos, music, or audio through RunAPI services.
- Submit one-off model jobs from an agent workflow.
- Pass JSON request bodies from files, stdin, or inline input.
- Start async tasks, wait for completion, and fetch task results.
- Check RunAPI auth and account status before making calls.
- Script RunAPI from a terminal, server, or CI job.

## Install

```bash
brew install runapi-ai/tap/runapi
```

For headless Linux or CI environments, use the public installer:

```bash
curl -fsSL https://runapi.ai/cli/install.sh | sh
```

## Authentication

Check the current auth state first:

```bash
runapi auth status
```

For agent and CI workflows, prefer `RUNAPI_API_KEY` in the environment. If a saved config is needed, import the token from stdin so it is not exposed in the process list:

```bash
printf '%s' "$RUNAPI_API_KEY" | runapi auth import-token --token -
```

Use interactive browser login only when the user explicitly wants it:

```bash
runapi login
```

## Discover Commands

Run help before composing a request instead of guessing service names or fields:

```bash
runapi --help
runapi suno --help
runapi suno text-to-music --help
```

## Run a Model Job

Pass a JSON request body with `--input-file`. The default flow submits the task and polls until it finishes.

```bash
runapi suno text-to-music --input-file request.json
```

For long-running jobs, submit asynchronously and wait separately:

```bash
runapi suno text-to-music --async --input-file request.json
runapi wait <task-id> --service suno --action text-to-music
runapi get <task-id> --service suno --action text-to-music
```

JSON responses go to stdout; progress and polling messages go to stderr.

## Agent Runtime Install

The CLI can install this skill into common agent runtimes:

```bash
runapi agent install-skill --target claude
runapi agent install-skill --target codex
runapi agent install-skill --target gemini
runapi agent install-skill --target openclaw
runapi agent install-skill --target-dir <path>
```

## Safety Rules

- Never paste API keys into prompts, examples, logs, PRs, issues, or shell history.
- Prefer `RUNAPI_API_KEY` or stdin token import for non-interactive agents.
- Check command exit codes before assuming a model job succeeded.
- Prefer async submit plus `runapi wait` for long-running generation jobs.
- Do not invent request fields. Inspect command help or the RunAPI model catalog first.

## References

- RunAPI CLI repository: https://github.com/runapi-ai/cli
- RunAPI CLI skill: https://github.com/runapi-ai/cli-skill
- RunAPI model catalog: https://runapi.ai/models.md
