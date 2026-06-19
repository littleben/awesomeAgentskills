---
name: NotFair Marketing Skills
description: Open-source Claude Code skills for SEO, GEO, Google Ads, and Meta Ads. Use when auditing a website's SEO, managing Google Ads campaigns, optimizing Meta Ads, researching keywords, writing content, or connecting live marketing data through MCP integrations.
---

# NotFair Marketing Skills

A collection of Claude Code skills covering SEO, GEO (generative engine optimization), Google Ads, and Meta Ads — backed by live data through MCP integrations.

**Repository**: [nowork-studio/NotFair](https://github.com/nowork-studio/NotFair) (~2.9k stars, MIT license)

## When to use this Skill

- Auditing a website for SEO issues (technical SEO, keyword gaps, meta tags, schema markup)
- Optimizing for AI search and GEO (generative engine optimization)
- Researching keywords and planning content
- Auditing Google Ads campaigns for wasted spend, search-term cleanup, bid management
- Analyzing Meta Ads (Facebook + Instagram) for ROAS, creative fatigue, audience overlap
- Working with live marketing data via Google Ads MCP, Meta Ads MCP, Google Search Console MCP, and Google Analytics (GA4) MCP

## Skill Areas

### [SEO](https://github.com/nowork-studio/NotFair/tree/main/seo)

- Site analysis and technical SEO audit
- Keyword research
- Meta tags optimization
- Schema markup generation
- GEO optimization (AI search visibility)
- Content writing and planning
- Broken link detection

### [Google Ads](https://github.com/nowork-studio/NotFair/tree/main/google-ads)

- Campaign audits and wasted-spend detection
- Search-term analysis and cleanup
- Keyword and bid management
- Ad copy optimization

### [Meta Ads](https://github.com/nowork-studio/NotFair/tree/main/meta-ads)

- ROAS and performance analysis
- Creative fatigue detection
- Audience overlap identification

## MCP Integrations

NotFair connects to live data through:

- **Google Ads MCP** — query campaign performance, search terms, keywords, and bids
- **Meta Ads MCP** — pull Meta (Facebook + Instagram) ad account insights
- **Google Search Console MCP** — access organic search data and click/impression reports
- **Google Analytics (GA4) MCP** — fetch site traffic and conversion metrics

## Installation

Install all skills from the NotFair repository into your Claude Code project:

```bash
# Clone or copy the skill files into your project
git clone https://github.com/nowork-studio/NotFair.git
```

Then reference any skill by name in Claude Code (e.g., "run the SEO audit skill" or "use the Google Ads audit skill").

See the [NotFair README](https://github.com/nowork-studio/NotFair#readme) for full setup instructions, including MCP configuration.

## Important Notes

- Each skill area (seo/, google-ads/, meta-ads/) can be used independently
- Live-data skills require the corresponding MCP to be configured; static-analysis skills (meta tags, schema markup, content) work without MCP
- Trigger keywords: "SEO audit", "Google Ads audit", "Meta Ads", "GEO optimization", "keyword research", "wasted spend", "ROAS"
