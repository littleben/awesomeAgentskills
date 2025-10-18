# Contributing to Awesome Agent Skills

Thank you for your interest in contributing! This guide will help you submit high-quality skills that benefit the community.

[中文贡献指南](#中文贡献指南) | [English Guide](#english-guide)

---

## English Guide

### How to Contribute

1. **Fork the repository**
2. **Create a new directory** for your skill (use kebab-case naming)
3. **Add your skill files** following the structure below
4. **Test your skill** to ensure it works as expected
5. **Submit a pull request** with a clear description

### Skill Structure

Each skill should be in its own directory with the following structure:

```
your-skill-name/
├── SKILL.md           # Main skill file (required)
├── WORKFLOW.md        # Detailed workflow (optional but recommended)
├── CHECKLIST.md       # Checklist for validation (optional)
├── TROUBLESHOOTING.md # Common issues and solutions (optional)
├── scripts/           # Automation scripts (if applicable)
│   └── example.sh
├── reference/         # Reference materials (optional)
│   └── guide.md
└── README.md          # Overview (optional)
```

### Required Files

#### SKILL.md

The main skill file must include:

```markdown
---
name: Your Skill Name
description: Brief description of what the skill does and when to use it (1-2 sentences)
---

# Skill Name

Brief overview of the skill.

## When to use this Skill

- Use case 1
- Use case 2
- Trigger keywords: "keyword1", "keyword2"

## Workflow

Step-by-step instructions...

## Important Notes

Key considerations and best practices...
```

**Frontmatter Requirements:**
- `name`: Clear, concise skill name (required)
- `description`: When to use this skill, including trigger keywords (required)

### Quality Guidelines

Your skill should:

#### 1. Solve a Specific Problem
- ✅ Clear, well-defined use case
- ✅ Addresses a real pain point
- ❌ Too broad or vague

#### 2. Be Well-Documented
- ✅ Clear workflow steps
- ✅ Examples where helpful
- ✅ Prerequisites listed
- ✅ Expected outcomes described
- ❌ Missing critical information

#### 3. Be Actionable
- ✅ Step-by-step instructions
- ✅ Validation checkpoints
- ✅ Error handling guidance
- ❌ Only theoretical descriptions

#### 4. Follow Best Practices
- ✅ Production-ready approach
- ✅ Security considerations
- ✅ Performance optimization
- ❌ Shortcuts or anti-patterns

#### 5. Be Tested
- ✅ Verified to work
- ✅ Edge cases considered
- ✅ Troubleshooting included
- ❌ Untested workflows

### Skill Categories

Please categorize your skill appropriately:

- **Web Development** - Frontend, backend, full-stack
- **DevOps & Deployment** - CI/CD, hosting, infrastructure
- **Data & AI** - Data processing, ML/AI workflows
- **Testing & QA** - Testing strategies, quality assurance
- **Documentation** - Technical writing, API docs
- **Code Quality** - Refactoring, optimization, best practices
- **Internationalization** - i18n, l10n, multi-language support
- **Other** - Specify if it doesn't fit above categories

### Pull Request Guidelines

#### PR Title Format

Use conventional commits format:

```
feat: Add skill for [skill name]
fix: Update [skill name] to fix [issue]
docs: Improve documentation for [skill name]
```

#### PR Description Template

```markdown
## Skill Name

[Skill Name]

## Category

[e.g., Web Development, DevOps, etc.]

## Description

Brief description of what this skill does.

## Use Cases

- Use case 1
- Use case 2

## Tech Stack (if applicable)

- Technology 1
- Technology 2

## Testing

- [ ] Tested with Claude Code
- [ ] Verified all steps work as expected
- [ ] Included troubleshooting for common issues

## Checklist

- [ ] Follows skill structure guidelines
- [ ] Includes frontmatter (name, description)
- [ ] Clear workflow instructions
- [ ] No personal/sensitive information
- [ ] Tested and working
```

### Code of Conduct

- Be respectful and constructive
- Provide helpful feedback on others' skills
- No personal attacks or harassment
- Quality over quantity

### Review Process

1. **Initial Review** - Maintainers check basic requirements
2. **Community Feedback** - Other contributors may provide feedback
3. **Revision** - Address any requested changes
4. **Merge** - Approved skills are merged

### Questions?

- Open an issue for questions
- Tag maintainers for clarification
- Check existing skills for examples

---

## 中文贡献指南

### 如何贡献

1. **Fork 本仓库**
2. **创建新目录** 存放你的 skill（使用 kebab-case 命名）
3. **添加 skill 文件** 遵循下面的结构
4. **测试你的 skill** 确保按预期工作
5. **提交 Pull Request** 并提供清晰的描述

### Skill 结构

每个 skill 应该在独立目录中，包含以下结构：

```
your-skill-name/
├── SKILL.md           # 主 skill 文件（必需）
├── WORKFLOW.md        # 详细工作流程（可选但推荐）
├── CHECKLIST.md       # 验证检查清单（可选）
├── TROUBLESHOOTING.md # 常见问题和解决方案（可选）
├── scripts/           # 自动化脚本（如适用）
│   └── example.sh
├── reference/         # 参考资料（可选）
│   └── guide.md
└── README.md          # 概述（可选）
```

### 必需文件

#### SKILL.md

主 skill 文件必须包含：

```markdown
---
name: Skill 名称
description: Skill 功能简述和使用场景（1-2句话）
---

# Skill 名称

Skill 简要概述。

## 使用场景

- 使用场景 1
- 使用场景 2
- 触发关键词："关键词1"、"关键词2"

## 工作流程

逐步说明...

## 重要注意事项

关键考虑因素和最佳实践...
```

**Frontmatter 要求：**
- `name`: 清晰、简洁的 skill 名称（必需）
- `description`: 何时使用此 skill，包括触发关键词（必需）

### 质量标准

你的 skill 应该：

#### 1. 解决具体问题
- ✅ 明确、定义清晰的使用场景
- ✅ 解决真实痛点
- ❌ 过于宽泛或模糊

#### 2. 文档完善
- ✅ 清晰的工作流程步骤
- ✅ 适当的示例说明
- ✅ 列出前置条件
- ✅ 描述预期结果
- ❌ 缺少关键信息

#### 3. 可操作性强
- ✅ 逐步操作指南
- ✅ 验证检查点
- ✅ 错误处理指导
- ❌ 仅理论描述

#### 4. 遵循最佳实践
- ✅ 生产级别的方法
- ✅ 安全考虑
- ✅ 性能优化
- ❌ 捷径或反模式

#### 5. 经过测试
- ✅ 验证可用性
- ✅ 考虑边界情况
- ✅ 包含故障排除
- ❌ 未经测试的工作流程

### Skill 分类

请为你的 skill 选择合适的分类：

- **Web 开发** - 前端、后端、全栈
- **DevOps 与部署** - CI/CD、托管、基础设施
- **数据与 AI** - 数据处理、ML/AI 工作流程
- **测试与 QA** - 测试策略、质量保证
- **文档** - 技术写作、API 文档
- **代码质量** - 重构、优化、最佳实践
- **国际化** - i18n、l10n、多语言支持
- **其他** - 如果不适合以上分类请说明

### Pull Request 规范

#### PR 标题格式

使用约定式提交格式：

```
feat: 添加 [skill 名称] skill
fix: 更新 [skill 名称] 修复 [问题]
docs: 改进 [skill 名称] 文档
```

#### PR 描述模板

```markdown
## Skill 名称

[Skill 名称]

## 分类

[例如：Web 开发、DevOps 等]

## 描述

简要描述此 skill 的功能。

## 使用场景

- 使用场景 1
- 使用场景 2

## 技术栈（如适用）

- 技术 1
- 技术 2

## 测试

- [ ] 已在 Claude Code 中测试
- [ ] 验证所有步骤按预期工作
- [ ] 包含常见问题的故障排除

## 检查清单

- [ ] 遵循 skill 结构指南
- [ ] 包含 frontmatter（name、description）
- [ ] 清晰的工作流程说明
- [ ] 无个人/敏感信息
- [ ] 已测试且可用
```

### 行为准则

- 保持尊重和建设性
- 对他人的 skills 提供有帮助的反馈
- 禁止人身攻击或骚扰
- 质量优于数量

### 审核流程

1. **初步审核** - 维护者检查基本要求
2. **社区反馈** - 其他贡献者可能提供反馈
3. **修订** - 处理任何请求的更改
4. **合并** - 批准的 skills 将被合并

### 有疑问？

- 开 issue 提问
- 标记维护者寻求说明
- 查看现有 skills 作为参考

---

**Thank you for contributing! 感谢贡献！**
