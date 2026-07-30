#!/bin/bash

# 文档同步工具测试脚本
# 用于验证工具的各项功能

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TEST_DIR="$(mktemp -d "${TMPDIR:-/tmp}/doc-sync-test.XXXXXX")"

cleanup() {
    find "$TEST_DIR" -depth -delete
}

trap cleanup EXIT

run_sync() {
    (
        cd "$TEST_DIR"
        node "$SCRIPT_DIR/sync.js" > /dev/null
    )
}

file_mtime() {
    node -e 'console.log(require("fs").statSync(process.argv[1]).mtimeMs)' "$1"
}

echo "🧪 开始测试文档同步工具..."
echo ""

echo "📁 创建测试目录: $TEST_DIR"
mkdir -p "$TEST_DIR/project1"
mkdir -p "$TEST_DIR/project2/subdir"
mkdir -p "$TEST_DIR/project3"

echo ""
echo "✅ 测试 1: 从单个文件创建其他文件"
echo "# Project 1 Config" > "$TEST_DIR/project1/CLAUDE.md"
echo "这是 CLAUDE.md 的内容" >> "$TEST_DIR/project1/CLAUDE.md"

run_sync

if [ -f "$TEST_DIR/project1/AGENTS.md" ] && [ -f "$TEST_DIR/project1/GEMINI.md" ]; then
    echo "   ✓ 成功创建 AGENTS.md 和 GEMINI.md"
else
    echo "   ✗ 失败: 文件未创建"
    exit 1
fi

if cmp -s "$TEST_DIR/project1/CLAUDE.md" "$TEST_DIR/project1/AGENTS.md"; then
    echo "   ✓ 文件内容一致"
else
    echo "   ✗ 失败: 文件内容不一致"
    exit 1
fi

echo ""
echo "✅ 测试 2: 嵌套目录文件同步"
echo "# Subdir Config" > "$TEST_DIR/project2/subdir/GEMINI.md"

run_sync

if [ -f "$TEST_DIR/project2/subdir/AGENTS.md" ] \
    && [ -f "$TEST_DIR/project2/subdir/CLAUDE.md" ]; then
    echo "   ✓ 嵌套目录同步成功"
else
    echo "   ✗ 失败: 嵌套目录同步失败"
    exit 1
fi

echo ""
echo "✅ 测试 3: 多个文件时选择最新内容"
echo "# Old Content" > "$TEST_DIR/project3/AGENTS.md"
node -e 'require("fs").utimesSync(process.argv[1], new Date(0), new Date(0))' \
    "$TEST_DIR/project3/AGENTS.md"
echo "# New Content" > "$TEST_DIR/project3/CLAUDE.md"

run_sync

if grep -q "# New Content" "$TEST_DIR/project3/AGENTS.md"; then
    echo "   ✓ 成功选择最新文件内容"
else
    echo "   ✗ 失败: 未选择最新文件"
    exit 1
fi

echo ""
echo "✅ 测试 4: 内容相同时跳过更新"
BEFORE_MTIME="$(file_mtime "$TEST_DIR/project1/AGENTS.md")"
run_sync
AFTER_MTIME="$(file_mtime "$TEST_DIR/project1/AGENTS.md")"

if [ "$BEFORE_MTIME" = "$AFTER_MTIME" ]; then
    echo "   ✓ 成功跳过相同内容"
else
    echo "   ✗ 失败: 不必要的文件更新"
    exit 1
fi

echo ""
echo "============================================================"
echo "🎉 所有测试通过！"
echo "============================================================"
echo ""
echo "📋 测试摘要:"
echo "   ✓ 单个文件创建"
echo "   ✓ 嵌套目录同步"
echo "   ✓ 最新文件选择"
echo "   ✓ 相同内容跳过"
echo ""
echo "✅ 文档同步工具运行正常，可以安全使用！"
