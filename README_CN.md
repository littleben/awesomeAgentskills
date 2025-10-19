# Awesome Agent Skills

精选的 Claude Code 和其他 AI 智能体技能集合。Skills 是可复用的工作流程，帮助智能体更有效地执行复杂任务。

中文说明 | [English](./README.md)

## 什么是 Skills？

Skills 是专门化的提示词和工作流程，用于扩展 AI 智能体的能力。它们提供：
- **结构化工作流程** - 处理复杂任务
- **最佳实践** - 编码为可复用的模式
- **领域专业知识** - 在特定领域的专业能力
- **一致性** - 在相似任务中保持一致的质量

## 快速导航

- 📚 [**Claude 官方 Skills**](./official-skills/README.md) - 创意设计、开发工具、企业沟通与元技能
- 🌟 [**社区贡献 Skills**](#社区贡献-skills) - 框架文档、Web性能、国际化与部署
- 🎓 [**使用指南**](#如何使用-skills) - 安装和使用说明
- 🤝 [**贡献指南**](#贡献指南) - 提交你自己的 skills

## Claude 官方 Skills

Anthropic 官方为 Claude Code 提供的 skills。包含创意设计、开发工具、企业沟通、文档处理、元技能和 Notion 集成。

**[📚 查看所有官方 Skills →](./official-skills/README.md)**

### 精选推荐

- 🎨 **创意类**: 算法艺术、画布设计、Slack GIF 创建器
- 💻 **开发类**: Artifacts 构建器、MCP 构建器、Web 应用测试
- 🏢 **企业类**: 品牌指南、内部沟通、主题工厂
- 📄 **文档类**: DOCX、PDF、PPTX、XLSX 操作
- 🔧 **元技能**: Skill 创建器、Skill 模板
- 📝 **Notion**: 会议智能、研究文档、知识捕获、规格实现

## 社区贡献 Skills

### 框架文档

为流行框架和工具提供完整文档参考的 skills。

#### [Shipany Docs](./shipany)

Shipany AI 驱动的 SaaS 脚手架框架完整文档参考。

**使用场景：**
- 使用 Shipany 模板构建 SaaS 应用
- 配置 Next.js 15 + Drizzle ORM + NextAuth
- 集成支付系统（Stripe/Creem）
- 搭建多语言 SaaS 应用
- 在 SaaS 产品中实现 AI 功能

**功能特性：**
- 228 页完整文档
- Drizzle ORM 数据库配置
- 认证系统（Google/GitHub 登录）
- 支付集成（Stripe/Creem）
- 邮件服务（Resend）
- AI 集成（OpenAI、Replicate、Kling AI）
- 国际化（next-intl）
- SEO 优化
- 云存储配置
- 用户管理与管理后台
- 博客系统与 CMS

**覆盖内容：**
- 📚 11 个分类主题（总计 572KB）
- 🚀 快速开始与配置
- 💾 数据库与 ORM
- 🔐 认证与授权
- 💳 支付处理
- 📧 邮件服务
- 🤖 AI 集成（图片/视频/文本生成）
- 🌍 国际化
- 🔍 SEO 与分析
- 📦 云存储
- 👥 用户控制台与管理系统
- 📝 博客与 CMS

**技术栈：** Next.js 15, TypeScript, Drizzle ORM, NextAuth, Stripe, Resend

[查看 Skill →](./shipany)

---

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
