#!/bin/bash

# Vercel 自动部署脚本
# 使用方法: bash deploy-to-vercel.sh <project-name>

set -e  # 遇到错误立即退出

PROJECT_NAME=$1

if [ -z "$PROJECT_NAME" ]; then
  echo "❌ 错误: 请提供项目名称"
  echo "使用方法: bash deploy-to-vercel.sh <project-name>"
  exit 1
fi

PROJECT_DIR="/Volumes/Time/go to wild/websites/${PROJECT_NAME}"

# 检查项目目录是否存在
if [ ! -d "$PROJECT_DIR" ]; then
  echo "❌ 错误: 项目目录不存在: $PROJECT_DIR"
  exit 1
fi

echo "📁 切换到项目目录: $PROJECT_DIR"
cd "$PROJECT_DIR"

# 检查是否安装了Vercel CLI
if ! command -v vercel &> /dev/null; then
  echo "❌ 错误: Vercel CLI 未安装"
  echo "请先安装: npm install -g vercel"
  exit 1
fi

echo "🔧 链接Vercel项目..."
vercel link --yes

echo "🚀 部署到Vercel (生产环境)..."
vercel --prod --yes

if [ $? -eq 0 ]; then
  echo ""
  echo "✅ Vercel部署成功!"
  echo "📱 查看部署: vercel ls ${PROJECT_NAME}"
  echo ""

  # 获取部署URL
  DEPLOY_URL=$(vercel ls ${PROJECT_NAME} --limit=1 | grep -o 'https://[^ ]*' | head -1)
  if [ ! -z "$DEPLOY_URL" ]; then
    echo "🌐 部署URL: $DEPLOY_URL"
  fi
else
  echo "❌ 部署失败"
  exit 1
fi
