#!/bin/bash

# GitHub 私有仓库自动创建脚本
# 使用方法: bash create-github-repo.sh <project-name>

set -e  # 遇到错误立即退出

PROJECT_NAME=$1

if [ -z "$PROJECT_NAME" ]; then
  echo "❌ 错误: 请提供项目名称"
  echo "使用方法: bash create-github-repo.sh <project-name>"
  exit 1
fi

REPO_NAME="${PROJECT_NAME}"
PROJECT_DIR="/Volumes/Time/go to wild/websites/${PROJECT_NAME}"

# 检查项目目录是否存在
if [ ! -d "$PROJECT_DIR" ]; then
  echo "❌ 错误: 项目目录不存在: $PROJECT_DIR"
  exit 1
fi

echo "📁 切换到项目目录: $PROJECT_DIR"
cd "$PROJECT_DIR"

# 检查是否已有Git仓库
if [ -d ".git" ]; then
  echo "✅ Git仓库已存在"
else
  echo "🔧 初始化Git仓库..."
  git init
  git add .
  git commit -m "Initial commit from Shipany template"
fi

# 检查是否安装了GitHub CLI
if ! command -v gh &> /dev/null; then
  echo "❌ 错误: GitHub CLI (gh) 未安装"
  echo "请先安装: brew install gh"
  echo "然后登录: gh auth login"
  exit 1
fi

# 检查GitHub CLI是否已登录
if ! gh auth status &> /dev/null; then
  echo "❌ 错误: GitHub CLI 未登录"
  echo "请先登录: gh auth login"
  exit 1
fi

echo "🚀 创建GitHub私有仓库: $REPO_NAME"

# 创建私有仓库
gh repo create "$REPO_NAME" \
  --private \
  --source=. \
  --remote=origin \
  --push

if [ $? -eq 0 ]; then
  echo ""
  echo "✅ GitHub仓库创建成功!"
  echo "📊 仓库URL: https://github.com/$(gh api user --jq .login)/${REPO_NAME}"
  echo ""
else
  echo "❌ 创建失败"
  exit 1
fi
