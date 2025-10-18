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

Official skills provided by Anthropic for Claude Code. All skills are from the [official repository](https://github.com/anthropics/skills).

### Creative & Design

#### [Algorithmic Art](https://github.com/anthropics/skills/tree/main/algorithmic-art)
Generates artistic visuals using p5.js with randomization, flow fields, and particle effects.

**Use when:** Creating procedural art, generative designs, or visual experiments.

---

#### [Canvas Design](https://github.com/anthropics/skills/tree/main/canvas-design)
Produces professional visual artwork in PNG and PDF formats leveraging design principles.

**Use when:** Creating marketing materials, social media graphics, or visual content.

---

#### [Slack GIF Creator](https://github.com/anthropics/skills/tree/main/slack-gif-creator)
Produces animated GIFs optimized for Slack's size requirements.

**Use when:** Creating animations for team communication or social media.

---

### Development & Technical

#### [Artifacts Builder](https://github.com/anthropics/skills/tree/main/artifacts-builder)
Constructs complex interactive interfaces using React, Tailwind CSS, and shadcn/ui.

**Use when:** Building rich web interfaces, dashboards, or interactive components within Claude.ai.

---

#### [MCP Builder](https://github.com/anthropics/skills/tree/main/mcp-builder)
Provides guidance for creating high-quality MCP (Model Context Protocol) servers to connect external APIs.

**Use when:** Integrating third-party services, building custom API connectors, or extending Claude's capabilities.

---

#### [Webapp Testing](https://github.com/anthropics/skills/tree/main/webapp-testing)
Tests local web applications using Playwright for UI verification and quality assurance.

**Use when:** Automating web application testing, validating UI behavior, or running QA checks.

---

### Enterprise & Communication

#### [Brand Guidelines](https://github.com/anthropics/skills/tree/main/brand-guidelines)
Applies Anthropic's official design system to artifacts for brand consistency.

**Use when:** Creating branded materials, ensuring design consistency, or following corporate style guides.

---

#### [Internal Comms](https://github.com/anthropics/skills/tree/main/internal-comms)
Drafts organizational communications like reports, newsletters, and announcements.

**Use when:** Writing internal documentation, team updates, or company-wide communications.

---

#### [Theme Factory](https://github.com/anthropics/skills/tree/main/theme-factory)
Applies professional themes to artifacts or generates custom design systems.

**Use when:** Styling applications, creating design systems, or maintaining visual consistency.

---

### Meta Skills

#### [Skill Creator](https://github.com/anthropics/skills/tree/main/skill-creator)
Teaches best practices for developing effective skills for Claude.

**Use when:** Building new skills, learning skill development patterns, or improving existing skills.

---

#### [Template Skill](https://github.com/anthropics/skills/tree/main/template-skill)
Provides a starter template for new skill creation with proper structure.

**Use when:** Starting a new skill from scratch or learning the skill format.

---

### Document Skills

#### [Document Skills Suite](https://github.com/anthropics/skills/tree/main/document-skills)

A collection of skills for manipulating various document formats (source-available reference implementations):

- **[DOCX](https://github.com/anthropics/skills/tree/main/document-skills/docx)** - Create and edit Word documents
- **[PDF](https://github.com/anthropics/skills/tree/main/document-skills/pdf)** - Manipulate PDF files
- **[PPTX](https://github.com/anthropics/skills/tree/main/document-skills/pptx)** - Create and edit PowerPoint presentations
- **[XLSX](https://github.com/anthropics/skills/tree/main/document-skills/xlsx)** - Handle Excel spreadsheets

**Use when:** Working with Office documents, automating document generation, or processing files.

**Note:** These are reference implementations showcasing complex production skills.

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
