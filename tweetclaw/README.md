# TweetClaw Skill

Use this Skill for approved X/Twitter workflows through OpenClaw and Xquik.

Install TweetClaw from Xquik's verified ClawHub publisher:

```bash
openclaw plugins install clawhub:@xquik/tweetclaw
```

Enable the optional live-action tool:

```bash
openclaw config set tools.alsoAllow '["explore", "tweetclaw"]'
```

Verify the installed runtime:

```bash
openclaw plugins inspect tweetclaw --runtime --json
openclaw skills info tweetclaw
```

Read `SKILL.md` before making live calls.

Xquik is an independent third-party service. Not affiliated with X Corp. "Twitter" and "X" are trademarks of X Corp.
