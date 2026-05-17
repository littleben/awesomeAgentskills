# X Social Media Manager

[![skills.sh](https://img.shields.io/badge/npx%20skills-add%20rabden%2FX--twitter--social--manager--skill-black?style=flat-square&logo=npm)](https://github.com/rabden/X-twitter-social-manager-skill)

A self-evolving AI skill that turns any AI coding agent into a personalized X (Twitter) social media manager. Works with any niche, any goal, any follower count.

## What It Does

On first run, the agent interviews you about your identity, niche, goals, and voice — then researches your X account automatically and populates all strategy files. From that point on, it:

- **Crafts posts** with proven hook frameworks, character validation, and strategic research
- **Writes replies** in your authentic voice (not AI-sounding generic praise)
- **Runs engagement sessions** with Reply Cards for your approval before posting
- **Plans content** with a 60/40 engagement-to-showcase ratio
- **Tracks performance** and self-updates its own strategy files based on what's working
- **Manages DM outreach** for client acquisition, job hunting, or networking
- **Operates the CLI** — can post, reply, search, and analyze directly via `twitter-cli`

## Requirements

- An AI agent that supports skills/instructions (see Installation below)
- `twitter-cli` — installed automatically on first run via `uv tool install twitter-cli`
- An active X (Twitter) session in your browser (for cookie-based auth)

## Installation

The easiest way to install this skill is using **Vercel's `skills` CLI**, which automatically detects and configures all major coding agents (OpenCode, Claude Code, Cursor, Windsurf, Codex, Gemini CLI, etc.).

### Automatic Installation (Recommended)

Run this single command in your terminal:

```bash
npx skills add rabden/X-twitter-social-manager-skill
```

*The CLI will automatically prompt you to choose:*
1. **Scope:** Install globally (available in all workspaces at `~/`) or project-scoped (restricted to the current workspace).
2. **Agents:** Choose which of your installed coding agents (OpenCode, Claude Code, Cursor, etc.) you want to enable the skill for.
3. **Method:** Install via **Symlink** (recommended — allows instant git updates) or **Copy**.

### Manual Installation (Fallback)

If you prefer to install manually, copy the `SKILL.md` and `references/` directory into your agent's config folder:

*   **OpenCode:** Global (`~/.config/opencode/skills/x-social-manager/`) or Project (`.agents/skills/x-social-manager/`)
*   **Claude Code:** Global (`~/.claude/skills/x-social-manager/`) or Project (`.claude/skills/x-social-manager/`)
*   **Cursor / Windsurf / Codex:** Project (`.agents/skills/x-social-manager/`) or Global

Place the `SKILL.md` and `references/` directory in your agent's custom instructions path. The skill is self-contained — it only needs the agent to be able to read/write files, run bash commands, and search the web.

### Standalone Usage

If your agent supports reading markdown files as instructions directly:

1. Clone this repository into your workspace:
   ```bash
   git clone https://github.com/rabden/X-twitter-social-manager-skill.git
   ```
2. Tell your agent: `"Read SKILL.md and follow the instructions to set up X Social Media Manager."`
3. The onboarding flow will handle the rest.

## File Structure

```
x-social-manager/
  SKILL.md                              # Main orchestration — onboarding, workflows, rules
  references/
    user-profile.md                     # Your identity, niche, goals, voice (filled during onboarding)
    memory.md                           # Living document — performance data, voice patterns, lessons
    voice-anti-patterns.md              # Banned AI phrases, verification checklist
    real-replies-archive.md             # Your actual replies word-for-word (auto-populated)
    content-strategy.md                 # Content pillars, target accounts, DM templates
    hook-library.md                     # 10 proven hook frameworks, ranked by performance
    algorithm-playbook.md               # X Phoenix algorithm mechanics, timing, growth phases
    growth-strategy.md                  # 90-day tactical playbook (generated during onboarding)
    branding-strategy.md                # Positioning analysis, competitive gaps, lead funnel
    content-planner.md                  # Post queue, scheduling logic
    cli-reference.md                    # twitter-cli commands, flags, safety rules
    subagent-definitions.md             # System prompts for 4 specialized sub-agents
    media/                              # Downloaded images for analysis (gitignored)
```

## How Onboarding Works

When the skill detects `onboarding_complete: false` in `user-profile.md`, it runs a 3-phase setup:

1. **Interview** — Asks about your handle, niche, expertise, goals, voice, constraints
2. **Research** — Fetches your X profile, recent posts, real replies, and scans your niche landscape
3. **File Generation** — Populates ALL reference files with your personalized data:
   - Generates 4 content pillars for your niche
   - Writes a 90-day growth playbook for your specific situation
   - Extracts your voice patterns and reply archetypes from real data
   - Identifies Tier 1/2/3 accounts to engage with
   - Drafts starter posts and a content calendar

After onboarding, the skill works identically to a hand-customized version.

## Core Workflows

| # | Workflow | What It Does |
|---|----------|-------------|
| 1 | **Craft a Post** | Research -> 2-3 variations with hooks -> post on approval |
| 2 | **Craft a Reply** | Voice-matched reply with image analysis -> approval -> post |
| 3 | **Write a Thread** | 3-7 tweet thread with per-tweet char counts |
| 4 | **Engagement Session** | Feed scan -> Reply Cards -> post approved replies |
| 5 | **Content Planner** | Feed scan + competitor analysis -> draft 3-5 posts -> schedule |
| 6 | **Visual Post Analysis** | Download + analyze images from any post |
| 7 | **Strategy Chat** | Data-grounded advice from your performance history |
| 8 | **DM Outreach** | Research target -> warm DM draft |
| 9 | **Intelligence Update** | Performance analysis -> auto-update strategy files |

## Sub-Agents

The skill spawns 4 specialized sub-agents (if the host IDE supports them):

| Agent | Purpose |
|-------|---------|
| `x-reply-crafter` | Drafts voice-matched replies |
| `x-feed-researcher` | Runs research, produces Research Summaries |
| `x-post-composer` | Crafts post text from research |
| `x-intel-updater` | Analyzes performance, updates strategy files |

If sub-agents aren't supported, the main agent handles everything directly — nothing breaks.

## Key Design Principles

- **Voice authenticity** — Replies are matched against your real writing patterns, not generic AI output. A banned-phrases list and verification checklist prevent AI-sounding text.
- **Research-first** — Every post requires a mandatory Research Summary before drafting. No shooting from the hip.
- **Approval-gated** — The agent never posts without explicit user approval.
- **Self-evolving** — The Intelligence Update workflow re-ranks hooks, updates strategy, and profiles your audience based on real performance data.
- **Algorithm-aware** — All strategies are built on the X Phoenix algorithm's actual ranking signals (Author-Engaged Reply > Bookmark > Like).

## License

MIT
