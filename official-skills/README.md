# Claude Official Skills

Official skills provided by Anthropic for Claude Code. All skills are from the [official repository](https://github.com/anthropics/skills).

[← Back to Main](../README.md)

## Table of Contents

- [Creative & Design](#creative--design)
- [Development & Technical](#development--technical)
- [Enterprise & Communication](#enterprise--communication)
- [Meta Skills](#meta-skills)
- [Document Skills](#document-skills)
- [Notion Skills](#notion-skills)

---

## Creative & Design

### [Algorithmic Art](https://github.com/anthropics/skills/tree/main/algorithmic-art)

Generates artistic visuals using p5.js with randomization, flow fields, and particle effects.

**Use when:** Creating procedural art, generative designs, or visual experiments.

**Tech Stack:** p5.js, JavaScript

---

### [Canvas Design](https://github.com/anthropics/skills/tree/main/canvas-design)

Produces professional visual artwork in PNG and PDF formats leveraging design principles.

**Use when:** Creating marketing materials, social media graphics, or visual content.

**Tech Stack:** HTML5 Canvas, PDF.js

---

### [Slack GIF Creator](https://github.com/anthropics/skills/tree/main/slack-gif-creator)

Produces animated GIFs optimized for Slack's size requirements.

**Use when:** Creating animations for team communication or social media.

**Tech Stack:** GIF encoding libraries

---

## Development & Technical

### [Artifacts Builder](https://github.com/anthropics/skills/tree/main/artifacts-builder)

Constructs complex interactive interfaces using React, Tailwind CSS, and shadcn/ui.

**Use when:** Building rich web interfaces, dashboards, or interactive components within Claude.ai.

**Tech Stack:** React, Tailwind CSS, shadcn/ui

---

### [MCP Builder](https://github.com/anthropics/skills/tree/main/mcp-builder)

Provides guidance for creating high-quality MCP (Model Context Protocol) servers to connect external APIs.

**Use when:** Integrating third-party services, building custom API connectors, or extending Claude's capabilities.

**Tech Stack:** MCP Protocol, Node.js/Python

---

### [Webapp Testing](https://github.com/anthropics/skills/tree/main/webapp-testing)

Tests local web applications using Playwright for UI verification and quality assurance.

**Use when:** Automating web application testing, validating UI behavior, or running QA checks.

**Tech Stack:** Playwright, Node.js

---

## Enterprise & Communication

### [Brand Guidelines](https://github.com/anthropics/skills/tree/main/brand-guidelines)

Applies Anthropic's official design system to artifacts for brand consistency.

**Use when:** Creating branded materials, ensuring design consistency, or following corporate style guides.

**Features:**
- Anthropic color palette and typography
- Logo usage guidelines
- Component design patterns
- Brand voice and tone

---

### [Internal Comms](https://github.com/anthropics/skills/tree/main/internal-comms)

Drafts organizational communications like reports, newsletters, and announcements.

**Use when:** Writing internal documentation, team updates, or company-wide communications.

**Features:**
- Professional tone and structure
- Clear information hierarchy
- Actionable formatting
- Audience-appropriate language

---

### [Theme Factory](https://github.com/anthropics/skills/tree/main/theme-factory)

Applies professional themes to artifacts or generates custom design systems.

**Use when:** Styling applications, creating design systems, or maintaining visual consistency.

**Features:**
- Multiple pre-built themes
- Custom theme generation
- Design token management
- Accessibility-first approach

---

## Meta Skills

### [Skill Creator](https://github.com/anthropics/skills/tree/main/skill-creator)

Teaches best practices for developing effective skills for Claude.

**Use when:** Building new skills, learning skill development patterns, or improving existing skills.

**Features:**
- Skill structure templates
- Best practice guidelines
- Common patterns and anti-patterns
- Testing and validation methods

---

### [Template Skill](https://github.com/anthropics/skills/tree/main/template-skill)

Provides a starter template for new skill creation with proper structure.

**Use when:** Starting a new skill from scratch or learning the skill format.

**Features:**
- Complete file structure
- Markdown documentation templates
- Example implementations
- Configuration examples

---

## Document Skills

### [Document Skills Suite](https://github.com/anthropics/skills/tree/main/document-skills)

A collection of skills for manipulating various document formats (source-available reference implementations).

#### [DOCX Skill](https://github.com/anthropics/skills/tree/main/document-skills/docx)

Create and edit Word documents programmatically.

**Features:**
- Document creation and editing
- Paragraph and text formatting
- Tables and lists
- Headers, footers, and page numbers
- Style management

**Tech Stack:** docx.js, Node.js

---

#### [PDF Skill](https://github.com/anthropics/skills/tree/main/document-skills/pdf)

Manipulate PDF files including creation, editing, and extraction.

**Features:**
- PDF generation from scratch
- Text and image extraction
- Page manipulation
- Form filling
- Annotation support

**Tech Stack:** pdf-lib, pdfkit, Node.js

---

#### [PPTX Skill](https://github.com/anthropics/skills/tree/main/document-skills/pptx)

Create and edit PowerPoint presentations.

**Features:**
- Slide creation and layout
- Text and image insertion
- Charts and tables
- Transitions and animations
- Master slide templates

**Tech Stack:** pptxgenjs, Node.js

---

#### [XLSX Skill](https://github.com/anthropics/skills/tree/main/document-skills/xlsx)

Handle Excel spreadsheets including reading, writing, and data manipulation.

**Features:**
- Workbook and sheet management
- Cell formatting and formulas
- Charts and pivot tables
- Data validation
- Conditional formatting

**Tech Stack:** xlsx, exceljs, Node.js

---

**Use these skills when:**
- Working with Office documents
- Automating document generation
- Processing and extracting data from files
- Creating reports and presentations

**Note:** These are reference implementations showcasing complex production skills. They demonstrate how to build comprehensive, production-ready skills for Claude Code.

---

## Notion Skills

Official Notion Skills that help Claude complete workflows in Notion - structuring pages, updating databases, and following your team's patterns.

### [Notion Skills for Claude](https://www.notion.so/notiondevs/Notion-Skills-for-Claude-28da4445d27180c7af1df7d8615723d0)

Step-by-step guides that teach Claude how to do real work in Notion. Instead of just answering questions, Skills help Claude complete entire workflows.

#### Available Skills

##### Meeting Intelligence 🧠

Prepares meeting materials by gathering context from Notion, enriching with Claude research, and creating both an internal pre-read and external agenda saved to Notion.

**Features:**
- Context gathering from Notion pages
- AI-powered research and enrichment
- Internal pre-read generation
- External agenda creation
- Automatic save to Notion

**Use when:** Preparing for important meetings, client calls, or team discussions.

---

##### Research & Documentation 🔎

Searches across your Notion workspace, synthesizes findings from multiple pages, and creates comprehensive research documentation saved as new Notion pages.

**Features:**
- Cross-workspace search
- Multi-source synthesis
- Structured report generation
- Proper citations and references
- Actionable insights extraction

**Use when:** Conducting research projects, creating knowledge base articles, or consolidating information.

---

##### Knowledge Capture 📚

Turns discussions into durable knowledge in Notion. Captures insights and decisions from chat, formats them clearly, and files them to the right wiki or database with smart linking.

**Features:**
- Conversation insight extraction
- Clear formatting and structure
- Smart database routing
- Automatic linking to related pages
- Metadata tagging

**Use when:** Documenting decisions, capturing meeting insights, or building knowledge repositories.

---

##### Spec to Implementation 🚀

Turns product or tech specs into concrete Notion tasks that Claude Code can implement. Breaks down spec pages into detailed implementation plans with clear tasks, acceptance criteria, and progress tracking.

**Features:**
- Spec parsing and analysis
- Task breakdown and creation
- Acceptance criteria definition
- Progress tracking setup
- Notion database integration

**Use when:** Converting product specs to development tasks, planning implementations, or managing development workflows.

---

### Installation Guide

1. **Download Skills**
   Visit the [official Notion Skills page](https://www.notion.so/notiondevs/Notion-Skills-for-Claude-28da4445d27180c7af1df7d8615723d0) and download the .zip files for each skill.

2. **Open Claude Settings**
   Navigate to Settings > Capabilities in Claude Code or Claude.ai.

3. **Upload Skills**
   - Go to the Skills section
   - Click the upload button
   - Select each Notion Skill .zip file
   - Wait for the upload to complete

4. **Try in Chat**
   - Click the "..." menu next to each skill
   - Select "Try in chat" to test the skill
   - Follow the prompts to use the skill

5. **Configure Notion Integration**
   - Ensure you have Notion MCP server installed
   - Grant necessary permissions to your Notion workspace
   - Test the connection with a simple query

---

### Prerequisites

To use Notion Skills, you need:

- ✅ Claude Code or Claude.ai account
- ✅ Notion workspace with appropriate permissions
- ✅ Notion MCP server configured (for Claude Code)
- ✅ Skills uploaded to your Claude account

---

### Resources

- 📚 [Official Notion Skills Documentation](https://www.notion.so/notiondevs/Notion-Skills-for-Claude-28da4445d27180c7af1df7d8615723d0)
- 🔧 [Notion API Documentation](https://developers.notion.com/)
- 💬 [Community Support](https://github.com/anthropics/skills/discussions)

---

[← Back to Main](../README.md)
