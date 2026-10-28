# Cloudish

Deploy an app to [Cloudish](https://cloudish.ai) and get back a live URL. The agent
inspects the project, uses an existing Dockerfile or writes a minimal one, creates its
own API key if needed, deploys, and reports the URL. Cloudish builds the image
server-side, so no local Docker is required.

The files here are an unmodified copy of the upstream skill at
[cloudishai/skills](https://github.com/cloudishai/skills/tree/main/skills/cloudish)
(version 0.1.6, MIT, see `LICENSE`). `SKILL.md` holds the workflow and API
reference; the agent reads the other files only when it needs them:
`container.md`, `instances.md`, `replicas.md`, `credits.md` and `changelog.md`.

## Install

```bash
mkdir -p ~/.claude/skills/cloudish
cp SKILL.md changelog.md container.md credits.md instances.md replicas.md ~/.claude/skills/cloudish/
```

Or install it as a Claude Code plugin:

```
/plugin marketplace add cloudishai/skills
/plugin install cloudish@cloudishai
```

Then ask your agent: *"Deploy this app to Cloudish."*
