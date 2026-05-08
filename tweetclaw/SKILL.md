---
name: TweetClaw
description: Use TweetClaw when an agent needs to search tweets, post tweets, post tweet replies, export followers, download media, monitor tweets, run giveaway draws, or call X/Twitter automation endpoints through OpenClaw.
---

# TweetClaw

TweetClaw is an OpenClaw plugin for X/Twitter automation through Xquik. It gives agents structured tools for tweet search, tweet lookup, post tweets, post tweet replies, direct messages, follower export, media upload, media download, monitor tweets, webhooks, giveaway draws, and credit checks.

## When to Use This Skill

- Search tweets, tweet replies, quote tweets, user timelines, liked tweets, bookmarks, notifications, or trends.
- Post tweets, post tweet replies, like, retweet, follow, unfollow, remove followers, update profiles, or send direct messages after explicit user approval.
- Export followers, following, verified followers, tweet replies, retweeters, favoriters, media tweets, list members, or community members.
- Upload media, download tweet media, create gallery links, or post tweets with images and videos.
- Monitor tweets from selected accounts and send webhook notifications for new activity.
- Run giveaway draws from tweet replies or export results.

## Setup

Install the OpenClaw plugin:

```bash
openclaw plugins install @xquik/tweetclaw
```

TweetClaw can be installed before credentials are configured. The free `explore` tool works without credentials and helps agents find the right endpoint before making a live API call.

For account-backed actions, configure an Xquik API key through OpenClaw plugin config. Keep the key in an environment variable or local secret store, never in prompts, docs, issue bodies, or chat logs.

```bash
openclaw config set plugins.entries.tweetclaw.config.apiKey "$XQUIK_API_KEY"
```

For accountless pay-per-use reads, configure an MPP signing key. MPP mode is read-only and covers 31 X API endpoints. It cannot post tweets, create monitors, send direct messages, upload media, download media, or change account state.

```bash
npm i mppx viem
openclaw config set plugins.entries.tweetclaw.config.tempoSigningKey "$MPP_SIGNING_KEY"
```

If OpenClaw can see the skill but cannot call the tools, allow the catalog and invoker tools:

```bash
openclaw config set tools.alsoAllow '["explore", "tweetclaw"]'
```

## Workflow

1. Use `explore` first to find the endpoint for the user request.
2. Check whether the action is read-only, paid, private, write-like, recurring, or bulk.
3. Summarize the exact action, account, target, text, media, limit, estimated credits, and storage or notification behavior.
4. Wait for explicit user approval before posting, replying, liking, retweeting, following, sending DMs, uploading media, downloading media, creating monitors, creating webhooks, running giveaway draws, or starting extraction jobs.
5. Use `tweetclaw` with the endpoint path, method, query, and body returned by the catalog.
6. Return concise results and redact credentials, private account data, or personal data unless the user explicitly requested that specific output.

## Common Requests

- "Search tweets about AI agents from the last 24 hours."
- "Post a tweet reply to this URL with the approved text."
- "Export followers for this account as JSON."
- "Download media from this tweet."
- "Monitor tweets from these accounts and send webhook events."
- "Run a giveaway draw from replies to this tweet."
- "Check my Xquik credit balance."

## Safety Rules

- Never use TweetClaw for spam, harassment, deceptive engagement, impersonation, credential collection, platform evasion, bulk unsolicited DMs, or bulk follow/like/retweet campaigns.
- Never print API keys, signing keys, cookies, tokens, or account secrets.
- Do not add links, mentions, hashtags, claims, or media the user did not approve.
- Keep bulk exports and monitors narrow by default.
- Use MPP only for read-only endpoints. Media download is not MPP-eligible because it requires authenticated access.

## References

- TweetClaw repository: https://github.com/Xquik-dev/tweetclaw
- npm package: https://www.npmjs.com/package/@xquik/tweetclaw
- Context7 docs: https://context7.com/xquik-dev/tweetclaw
- Xquik docs: https://docs.xquik.com
