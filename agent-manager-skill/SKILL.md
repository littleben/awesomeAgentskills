---
name: Agent Manager Skill
description: Manage multiple local CLI agents via tmux sessions (start/stop/monitor/assign) with cron-friendly scheduling. Use when you need to orchestrate multiple agents, monitor progress, or automate recurring agent tasks.
---

# Agent Manager Skill

Manage multiple local CLI agents via `tmux` sessions.

## When to use this Skill

- Running multiple local agents in parallel
- Starting/stopping agents and monitoring their output
- Assigning tasks to agents and watching progress
- Scheduling recurring agent work (cron)
- User mentions: "tmux", "agent manager", "multiple agents", "monitor", "assign", "schedule", "cron"

## Prerequisites

- `python3`
- `tmux`

Install:

```bash
git clone https://github.com/fractalmind-ai/agent-manager-skill.git
```

## Workflow

### 1) Verify environment

```bash
python3 agent-manager/scripts/main.py doctor
```

### 2) List agents

```bash
python3 agent-manager/scripts/main.py list
```

### 3) Start an agent

```bash
python3 agent-manager/scripts/main.py start EMP_0001
```

### 4) Assign a task

```bash
python3 agent-manager/scripts/main.py assign EMP_0001 <<'EOF'
Follow teams/fractalmind-ai-maintenance.md Workflow
EOF
```

### 5) Monitor output

```bash
python3 agent-manager/scripts/main.py monitor EMP_0001 --follow
```

## Notes

- If you run agents from another repo, set `REPO_ROOT` so paths resolve correctly.
