# Awesome Agent Skills

A curated collection of skills for Claude Code and other AI agents. Skills are reusable workflows that help agents perform complex tasks more effectively.

[中文说明](./README_CN.md) | English

## What are Skills?

Skills are specialized prompts and workflows that extend AI agents' capabilities. They provide:
- **Structured workflows** for complex tasks
- **Best practices** codified into reusable patterns
- **Domain expertise** in specific areas
- **Consistency** across similar tasks

## Table of Contents

- [Claude Official Skills](#claude-official-skills)
- [Community Skills](#community-skills)
  - [Internationalization & Deployment](#internationalization--deployment)
- [How to Use Skills](#how-to-use-skills)
- [Contributing](#contributing)

## Claude Official Skills

Official skills provided by Anthropic for Claude Code.

*Coming soon - official skills will be added as they become available*

## Community Skills

### Internationalization & Deployment

Skills for adding multi-language support and deploying web applications.

#### [Internationalizing Websites](./internationalizing-websites)

Adds multi-language support to Next.js websites with proper SEO configuration.

**Use when:**
- Adding new language versions to existing website
- Setting up i18n for new website
- Configuring SEO for multiple languages
- Optimizing for international markets

**Features:**
- Automated language file generation
- SEO-optimized hreflang tags
- Localized sitemaps
- Language-specific content management
- Support for 15+ languages

**Tech Stack:** Next.js, next-intl

[View Skill →](./internationalizing-websites)

---

#### [Deploying to Production](./deploying-to-production)

Automates GitHub repository creation and Vercel deployment for Next.js websites.

**Use when:**
- Deploying new websites to production
- Setting up CI/CD pipelines
- Configuring GitHub + Vercel integration
- Going live with your application

**Features:**
- Automated GitHub repository creation
- One-command Vercel deployment
- Pre-deployment validation checklist
- Post-deployment verification
- Comprehensive troubleshooting guide

**Tech Stack:** GitHub CLI, Vercel CLI, Next.js

[View Skill →](./deploying-to-production)

---

## How to Use Skills

### In Claude Code

1. **Copy the skill** to your project's `.claude/skills/` directory
2. **Reference in prompts** by mentioning the skill name
3. Claude will **automatically expand** the skill's workflow

### As Standalone Reference

Skills can also be used as:
- **Documentation** for best practices
- **Checklists** for manual execution
- **Templates** for creating your own workflows

## Contributing

We welcome contributions! Please see [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines.

### Quick Start

1. Fork this repository
2. Add your skill in a new directory
3. Follow the [skill template structure](./CONTRIBUTING.md#skill-structure)
4. Submit a pull request

### What Makes a Good Skill?

- ✅ Solves a specific, well-defined problem
- ✅ Includes clear usage instructions
- ✅ Provides actionable workflows
- ✅ Is well-documented and tested
- ✅ Follows best practices

## License

This repository is licensed under the MIT License. See [LICENSE](./LICENSE) for details.

Individual skills may have their own licenses - please check each skill's directory.

## Acknowledgments

- Thanks to [Anthropic](https://www.anthropic.com/) for creating Claude and the skills framework
- Thanks to all contributors who share their skills with the community

---

**Star ⭐ this repo** if you find these skills useful!

**Share your skills** by submitting a PR - let's build an amazing collection together!
