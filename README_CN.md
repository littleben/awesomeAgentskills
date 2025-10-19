# Awesome Agent Skills

精选的 Claude Code 和其他 AI 智能体技能集合。Skills 是可复用的工作流程，帮助智能体更有效地执行复杂任务。

中文说明 | [English](./README.md)

## 什么是 Skills？

Skills 是专门化的提示词和工作流程，用于扩展 AI 智能体的能力。它们提供：
- **结构化工作流程** - 处理复杂任务
- **最佳实践** - 编码为可复用的模式
- **领域专业知识** - 在特定领域的专业能力
- **一致性** - 在相似任务中保持一致的质量

## 目录

- [Claude 官方 Skills](#claude-官方-skills)
- [社区贡献 Skills](#社区贡献-skills)
  - [国际化与部署](#国际化与部署)
- [如何使用 Skills](#如何使用-skills)
- [贡献指南](#贡献指南)

## Claude 官方 Skills

Anthropic 官方为 Claude Code 提供的 skills。所有 skills 来自[官方仓库](https://github.com/anthropics/skills)。

### 创意与设计

#### [算法艺术](https://github.com/anthropics/skills/tree/main/algorithmic-art)
使用 p5.js 生成艺术视觉效果，包括随机化、流场和粒子效果。

**使用场景：** 创建程序化艺术、生成式设计或视觉实验。

---

#### [画布设计](https://github.com/anthropics/skills/tree/main/canvas-design)
利用设计原则生成专业的 PNG 和 PDF 格式视觉作品。

**使用场景：** 创建营销素材、社交媒体图形或视觉内容。

---

#### [Slack GIF 创建器](https://github.com/anthropics/skills/tree/main/slack-gif-creator)
生成符合 Slack 大小要求的优化动画 GIF。

**使用场景：** 为团队沟通或社交媒体创建动画。

---

### 开发与技术

#### [Artifacts 构建器](https://github.com/anthropics/skills/tree/main/artifacts-builder)
使用 React、Tailwind CSS 和 shadcn/ui 构建复杂的交互式界面。

**使用场景：** 在 Claude.ai 中构建丰富的 Web 界面、仪表板或交互式组件。

---

#### [MCP 构建器](https://github.com/anthropics/skills/tree/main/mcp-builder)
提供创建高质量 MCP（模型上下文协议）服务器的指导，用于连接外部 API。

**使用场景：** 集成第三方服务、构建自定义 API 连接器或扩展 Claude 的能力。

---

#### [Web 应用测试](https://github.com/anthropics/skills/tree/main/webapp-testing)
使用 Playwright 测试本地 Web 应用，进行 UI 验证和质量保证。

**使用场景：** 自动化 Web 应用测试、验证 UI 行为或执行 QA 检查。

---

### 企业与沟通

#### [品牌指南](https://github.com/anthropics/skills/tree/main/brand-guidelines)
将 Anthropic 官方设计系统应用于 artifacts，确保品牌一致性。

**使用场景：** 创建品牌素材、确保设计一致性或遵循企业风格指南。

---

#### [内部沟通](https://github.com/anthropics/skills/tree/main/internal-comms)
起草组织沟通内容，如报告、新闻通讯和公告。

**使用场景：** 编写内部文档、团队更新或公司范围的沟通。

---

#### [主题工厂](https://github.com/anthropics/skills/tree/main/theme-factory)
为 artifacts 应用专业主题或生成自定义设计系统。

**使用场景：** 应用样式、创建设计系统或保持视觉一致性。

---

### 元技能

#### [Skill 创建器](https://github.com/anthropics/skills/tree/main/skill-creator)
教授为 Claude 开发有效 skills 的最佳实践。

**使用场景：** 构建新 skills、学习 skill 开发模式或改进现有 skills。

---

#### [Skill 模板](https://github.com/anthropics/skills/tree/main/template-skill)
提供具有正确结构的新 skill 创建起始模板。

**使用场景：** 从头开始创建新 skill 或学习 skill 格式。

---

### 文档技能

#### [文档技能套件](https://github.com/anthropics/skills/tree/main/document-skills)

用于操作各种文档格式的 skills 集合（源码可用的参考实现）：

- **[DOCX](https://github.com/anthropics/skills/tree/main/document-skills/docx)** - 创建和编辑 Word 文档
- **[PDF](https://github.com/anthropics/skills/tree/main/document-skills/pdf)** - 操作 PDF 文件
- **[PPTX](https://github.com/anthropics/skills/tree/main/document-skills/pptx)** - 创建和编辑 PowerPoint 演示文稿
- **[XLSX](https://github.com/anthropics/skills/tree/main/document-skills/xlsx)** - 处理 Excel 电子表格

**使用场景：** 处理 Office 文档、自动化文档生成或处理文件。

**注意：** 这些是展示复杂生产 skills 的参考实现。

## 社区贡献 Skills

### Web 性能与 SEO

用于优化网站性能、可访问性和搜索引擎排名的 skills。

#### [Web 可访问性 - 对比度审计修复](./web-performance-seo)

诊断并修复 PageSpeed Insights 可访问性 "!" 错误（由 color-contrast 审计失败导致）。

**使用场景：**
- PageSpeed Insights 显示 "!" 而非可访问性分数
- color-contrast 审计报告错误或不完整
- 需要修复 `getImageData` canvas 错误
- 提升 WCAG 2.1 合规性

**功能特性：**
- 5 步系统化修复工作流程
- 5 分钟紧急修复方案
- 完整的诊断命令集
- OKLCH → HSL 颜色空间转换
- CSS filter 移除指南
- 透明度阈值优化
- WCAG 2.1 对比度标准
- 部署前后验证流程

**效果：**
- ✅ 可访问性分数："!" → 85-100
- ✅ SEO 排名提升
- ✅ 用户体验改善
- ✅ 法律合规（ADA, WCAG 2.1）

**技术栈：** Next.js, React, Tailwind CSS, Lighthouse, axe-core

[查看 Skill →](./web-performance-seo)

---

### 国际化与部署

用于添加多语言支持和部署 Web 应用的 skills。

#### [国际化网站](./internationalizing-websites)

为 Next.js 网站添加多语言支持，并配置符合 SEO 标准的国际化设置。

**使用场景：**
- 为现有网站添加新的语言版本
- 为新网站设置国际化（i18n）
- 配置多语言 SEO 优化
- 优化国际市场

**功能特性：**
- 自动生成语言文件
- SEO 优化的 hreflang 标签
- 本地化站点地图
- 语言特定的内容管理
- 支持 15+ 种语言

**技术栈：** Next.js, next-intl

[查看 Skill →](./internationalizing-websites)

---

#### [生产环境部署](./deploying-to-production)

自动化 GitHub 仓库创建和 Vercel 部署流程。

**使用场景：**
- 部署新网站到生产环境
- 设置 CI/CD 流水线
- 配置 GitHub + Vercel 集成
- 应用上线发布

**功能特性：**
- 自动创建 GitHub 仓库
- 一键 Vercel 部署
- 部署前验证检查清单
- 部署后验证流程
- 完整的故障排除指南

**技术栈：** GitHub CLI, Vercel CLI, Next.js

[查看 Skill →](./deploying-to-production)

---

## 如何使用 Skills

### 在 Claude Code 中使用

1. **复制 skill** 到你项目的 `.claude/skills/` 目录
2. **在提示词中引用** skill 名称
3. Claude 将**自动展开** skill 的工作流程

### 作为独立参考

Skills 也可以用作：
- **最佳实践文档** - 参考学习
- **检查清单** - 手动执行任务
- **模板** - 创建自己的工作流程

## 贡献指南

我们欢迎贡献！请查看 [CONTRIBUTING.md](./CONTRIBUTING.md) 了解详细规范。

### 快速开始

1. Fork 本仓库
2. 在新目录中添加你的 skill
3. 遵循 [skill 模板结构](./CONTRIBUTING.md#skill-structure)
4. 提交 Pull Request

### 什么是好的 Skill？

- ✅ 解决一个明确定义的具体问题
- ✅ 包含清晰的使用说明
- ✅ 提供可操作的工作流程
- ✅ 有良好的文档和测试
- ✅ 遵循最佳实践

## 贡献者

感谢所有为本项目贡献 skills 的开发者！

## 许可证

本仓库采用 MIT 许可证。详见 [LICENSE](./LICENSE)。

单个 skill 可能有自己的许可证 - 请查看每个 skill 的目录。

## 致谢

- 感谢 [Anthropic](https://www.anthropic.com/) 创建了 Claude 和 skills 框架
- 感谢所有与社区分享 skills 的贡献者

---

**给个星标 ⭐** 如果你觉得这些 skills 有用！

**分享你的 skills** - 提交 PR，让我们一起打造一个优秀的 skills 集合！
