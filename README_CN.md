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

Anthropic 官方为 Claude Code 提供的 skills。

*即将推出 - 官方 skills 将在可用时添加*

## 社区贡献 Skills

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
