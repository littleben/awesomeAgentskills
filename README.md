# Awesome Agent Skills

A curated collection of skills for Claude Code and other AI agents. Skills are reusable workflows that help agents perform complex tasks more effectively.

[中文说明](./README_CN.md) | English

## What are Skills?

Skills are specialized prompts and workflows that extend AI agents' capabilities. They provide:
- **Structured workflows** for complex tasks
- **Best practices** codified into reusable patterns
- **Domain expertise** in specific areas
- **Consistency** across similar tasks

## Quick Links

- 📚 [**Claude Official Skills**](./official-skills/README.md) - Creative, Development, Enterprise & Meta Skills
- 🌟 [**Community Skills**](#community-skills) - Framework Docs, Web Performance, i18n & Deployment
- 🎓 [**How to Use**](#how-to-use-skills) - Installation and usage guide
- 🤝 [**Contributing**](#contributing) - Submit your own skills

## Claude Official Skills

Official skills provided by Anthropic for Claude Code. Includes Creative & Design, Development & Technical, Enterprise & Communication, Document Skills, Meta Skills, and Notion Skills.

**[📚 View All Official Skills →](./official-skills/README.md)**

### Highlights

- 🎨 **Creative**: Algorithmic Art, Canvas Design, Slack GIF Creator
- 💻 **Development**: Artifacts Builder, MCP Builder, Webapp Testing
- 🏢 **Enterprise**: Brand Guidelines, Internal Comms, Theme Factory
- 📄 **Documents**: DOCX, PDF, PPTX, XLSX manipulation
- 🔧 **Meta**: Skill Creator, Template Skill
- 📝 **Notion**: Meeting Intelligence, Research & Documentation, Knowledge Capture, Spec to Implementation

## Community Skills

### Framework Documentation

Skills providing comprehensive documentation for popular frameworks and tools.

#### [Shipany Docs](./shipany)

Complete documentation reference for Shipany AI-powered SaaS boilerplate framework.

**Use when:**
- Building SaaS applications with Shipany template
- Configuring Next.js 15 + Drizzle ORM + NextAuth
- Integrating payment systems (Stripe/Creem)
- Setting up multi-language SaaS applications
- Implementing AI features in SaaS products

**Features:**
- 228 pages of comprehensive documentation
- Database configuration with Drizzle ORM
- Authentication system (Google/GitHub)
- Payment integration (Stripe/Creem)
- Email service (Resend)
- AI integrations (OpenAI, Replicate, Kling AI)
- Internationalization (next-intl)
- SEO optimization
- Cloud storage configuration
- User management & admin dashboard
- Blog system with CMS

**Coverage:**
- 📚 11 categorized topics (572KB total)
- 🚀 Getting Started & Configuration
- 💾 Database & ORM
- 🔐 Authentication & Authorization
- 💳 Payment Processing
- 📧 Email Services
- 🤖 AI Integration (Image/Video/Text Generation)
- 🌍 Internationalization
- 🔍 SEO & Analytics
- 📦 Cloud Storage
- 👥 User Console & Admin System
- 📝 Blog & CMS

**Tech Stack:** Next.js 15, TypeScript, Drizzle ORM, NextAuth, Stripe, Resend

[View Skill →](./shipany)

---

### Web Performance & SEO

Skills for optimizing website performance, accessibility, and search engine rankings.

#### [Web Accessibility - Contrast Audit Fix](./web-performance-seo)

Diagnoses and fixes PageSpeed Insights accessibility "!" errors caused by color-contrast audit failures.

**Use when:**
- PageSpeed Insights shows "!" instead of Accessibility score
- color-contrast audit reports errors or incomplete
- Need to fix `getImageData` canvas errors
- Improving WCAG 2.1 compliance

**Features:**
- 5-step systematic fix workflow
- Quick 5-minute emergency fix
- Comprehensive diagnostic commands
- OKLCH → HSL color space conversion
- CSS filter removal guidelines
- Opacity threshold optimization
- WCAG 2.1 contrast standards
- Pre/post deployment verification

**Impact:**
- ✅ Accessibility score: "!" → 85-100
- ✅ Improved SEO rankings
- ✅ Better user experience
- ✅ Legal compliance (ADA, WCAG 2.1)

**Tech Stack:** Next.js, React, Tailwind CSS, Lighthouse, axe-core

[View Skill →](./web-performance-seo)

---

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
