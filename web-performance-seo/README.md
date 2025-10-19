# Agent Skill: Accessibility 对比度审计报错修复

**Skill Type**: Technical Debugging & Optimization
**Domain**: Web Accessibility, SEO, Frontend Performance
**Difficulty**: Intermediate
**Impact**: High (直接影响 SEO 排名和用户体验)

---

## 📋 Skill Overview

### What This Skill Solves

**Problem**: PageSpeed Insights (PSI) 的 Accessibility 分数显示 **感叹号（"!"）** 而非正常数字分数。

**Root Cause**: 不是分数低，而是 **测量失败**！
- `color-contrast` 审计在执行过程中直接报错
- Canvas `getImageData()` 调用失败
- 无法计算颜色对比度 → 无法给出分数

**Impact**:
- ❌ SEO 排名下降（Accessibility 是 Google 排名因素）
- ❌ 无法通过 Google 质量检查
- ❌ 视障用户体验受损
- ❌ 部分市场（美国、欧盟）法律合规风险

---

## 🔍 Diagnostic Process

### Step 1: Identify the Problem

**Symptom Check**:
```
PageSpeed Insights → Accessibility → "!" (exclamation mark)
Chrome DevTools → Lighthouse → Accessibility → Error
```

**Key Indicators**:
- 显示感叹号，而非分数（如 85、90 等）
- Console 可能显示 `getImageData` 相关错误
- color-contrast 审计标记为 "Error" 或 "Incomplete"

### Step 2: Root Cause Analysis

**核心触发器**（按优先级排序）:

1. **CSS Filter** ⚠️ 最常见
   - `backdrop-blur`, `filter: brightness()`, `filter: contrast()`
   - `mix-blend-mode`
   - 直接导致 canvas 像素采样失败

2. **OKLCH/OKLAB 颜色空间**
   - 新色彩模型导致 axe-core 计算偏差
   - 与 sRGB 转换不稳定

3. **超低透明度** (< 0.4)
   - 背景透明度太低（如 `/10`, `/20`, `/30`）
   - 让 canvas 采样结果不可靠

4. **复杂渐变遮罩**
   - `mask-image: linear-gradient(...)` + 低 opacity
   - 跨域图片背景 + 文字覆盖

### Step 3: Quick Diagnostic Commands

```bash
# 1. 检查颜色空间（OKLCH/OKLAB）
grep -r "oklch\|oklab" app/ components/ styles/

# 2. 检查低透明度（< 0.4）
grep -r "/10\|/20\|/30\|opacity-25\|opacity-0" components/ app/

# 3. 检查 CSS Filter（关键！）
grep -r "backdrop-blur\|filter:\|mix-blend-mode" components/ app/

# 4. 检查渐变文字
grep -r "background-clip.*text\|color.*transparent" components/ app/
```

---

## 🛠️ Fix Implementation

### Phase 1: Remove CSS Filters (Priority: Critical)

**Why**: CSS filters 是触发 `getImageData` 报错的主要原因。

**What to Fix**:
```tsx
// ❌ BEFORE: Triggers getImageData error
<div className="bg-card/50 backdrop-blur-sm">
  <h2>Content</h2>
</div>

// ✅ AFTER: Use solid background instead
<div className="bg-card/80">
  <h2>Content</h2>
</div>
```

**Affected Properties**:
- `backdrop-blur-*` → Remove completely
- `filter: brightness()` → Remove or use opacity instead
- `filter: contrast()` → Remove
- `mix-blend-mode` → Remove

**Search & Replace**:
```bash
# Find all backdrop-blur usage
grep -r "backdrop-blur" components/

# Replace pattern (manual review recommended)
# backdrop-blur-sm → (remove)
# bg-card/50 → bg-card/80
```

---

### Phase 2: Convert Color Space (Priority: High)

**Why**: OKLCH/OKLAB 颜色空间导致对比度计算偏差。

**What to Fix**:
```css
/* ❌ BEFORE: OKLCH color space */
:root {
  --background: oklch(0.99 0 0);
  --foreground: oklch(0.15 0.01 270);
  --primary: oklch(0.55 0.22 264);
}

/* ✅ AFTER: Stable HSL color space */
:root {
  --background: hsl(0, 0%, 99%);
  --foreground: hsl(270, 5%, 15%);
  --primary: hsl(250, 60%, 50%);
}
```

**Conversion Table** (OKLCH → HSL):

| OKLCH | Approximate HSL | Description |
|-------|-----------------|-------------|
| `oklch(0.99 0 0)` | `hsl(0, 0%, 99%)` | Near white |
| `oklch(0.15 0.01 270)` | `hsl(270, 5%, 15%)` | Dark gray |
| `oklch(0.55 0.22 264)` | `hsl(250, 60%, 50%)` | Primary blue |
| `oklch(0.12 0.01 270)` | `hsl(270, 5%, 12%)` | Very dark (dark mode) |
| `oklch(0.95 0.01 270)` | `hsl(270, 5%, 95%)` | Light gray (dark mode text) |

**Files to Check**:
- `app/globals.css`
- `app/theme.css`
- `tailwind.config.ts` (if using custom colors)

---

### Phase 3: Increase Opacity Thresholds (Priority: Medium)

**Why**: 透明度 < 0.4 导致 canvas 采样不稳定。

**Target**: 所有背景透明度 ≥ 0.4（推荐 ≥ 0.6）

**What to Fix**:
```tsx
// ❌ BEFORE: Too low opacity
className="bg-muted/20"           // 20%
className="from-primary/10"       // 10%
className="opacity-25"            // 25%

// ✅ AFTER: Safe opacity threshold
className="bg-muted/40"           // 40% (min safe)
className="from-primary/20"       // 20% (gradient ok)
className="opacity-40"            // 40%

// ✅ BETTER: Recommended opacity
className="bg-muted/60"           // 60%
className="from-primary/40"       // 40%
className="opacity-60"            // 60%
```

**Pattern Replacement**:
- `/10` → `/20` (gradients) or `/40` (backgrounds)
- `/20` → `/40`
- `/30` → `/60`
- `opacity-25` → `opacity-40`

---

### Phase 4: Handle Gradient Text (Priority: Low)

**Why**: `color: transparent` + `background-clip: text` 让对比度无法计算。

**Solution**: 提供纯色降级

```css
/* ❌ AVOID: Pure gradient text (no fallback) */
.gradient-text {
  background: linear-gradient(90deg, #0ea5e9, #6366f1);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;  /* ← Problem! */
}

/* ✅ SOLUTION: Solid color fallback */
.title {
  color: #0a0a0a;  /* Default: solid color (accessible) */
}

/* Apply gradient only when safe */
@media (prefers-contrast: no-preference) {
  .title.with-gradient {
    background: linear-gradient(90deg, #0ea5e9, #6366f1);
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
  }
}

/* Remove gradient in high-contrast mode */
@media (forced-colors: active) {
  .title.with-gradient {
    background: none;
    color: CanvasText;
    forced-color-adjust: auto;
  }
}
```

---

### Phase 5: Add Overlay for Image Backgrounds (Priority: Medium)

**Why**: 文字直接覆盖图片，背景无法被可靠采样。

**Solution**: 添加不透明遮罩（≥ 0.6）

```tsx
// ❌ BEFORE: Text directly on image
<div className="relative">
  <img src="/hero.jpg" alt="Hero" />
  <h1 className="absolute top-1/2 left-1/2 text-white">
    Title
  </h1>
</div>

// ✅ AFTER: Add opaque overlay
<div className="relative">
  <img src="/hero.jpg" alt="Hero" />
  {/* Semi-transparent overlay */}
  <div className="absolute inset-0 bg-black/60"></div>
  {/* Text above overlay */}
  <h1 className="relative top-1/2 left-1/2 text-white">
    Title
  </h1>
</div>
```

**Overlay Opacity Guidelines**:
- **Dark overlay + White text**: `bg-black/60` (60% opacity)
- **Light overlay + Dark text**: `bg-white/80` (80% opacity)
- **Branded overlay**: `bg-primary/70` (70% opacity)

---

## ✅ Verification Checklist

### Pre-Deployment Check

```markdown
## Color Space
- [ ] All colors use `hsl()` or `rgb()` (no `oklch` or `oklab`)
- [ ] Check `app/globals.css`, `app/theme.css`, `tailwind.config.ts`

## Opacity
- [ ] All background opacity ≥ 0.4 (prefer ≥ 0.6)
- [ ] No Tailwind classes: `/10`, `/20`, `/30` in backgrounds
- [ ] No `opacity-0`, `opacity-25` in visible elements

## CSS Filters (CRITICAL!)
- [ ] No `backdrop-blur-*` classes
- [ ] No `filter: brightness()` or `filter: contrast()`
- [ ] No `mix-blend-mode`
- [ ] No `backdrop-filter` in CSS

## Gradient Text
- [ ] Gradient text has solid color fallback
- [ ] Uses `@media (prefers-contrast)` for safe application
- [ ] Uses `@media (forced-colors)` for accessibility

## Image Backgrounds
- [ ] Text over images has opaque overlay (≥ 0.6 opacity)
- [ ] Contrast ratio ≥ 4.5:1 (small text) or ≥ 3:1 (large text)
```

### Local Testing

```bash
# 1. Build verification (must pass)
npm run build
# or
pnpm build

# 2. Chrome DevTools Lighthouse
# Open browser → F12 → Lighthouse → Accessibility
# Should show a number (85-100), NOT "!"

# 3. axe DevTools CLI (optional)
npx @axe-core/cli http://localhost:3000
```

### Post-Deployment Verification

```bash
# 1. PageSpeed Insights (wait 24-48 hours after deployment)
# https://pagespeed.web.dev/
# Input: Your production URL
# Check: Accessibility should show a number, NOT "!"

# 2. Check specific contrast issues
# Chrome DevTools → Elements → Accessibility pane
# Or: axe DevTools browser extension
```

---

## 📊 Success Metrics

### Before Fix
- ❌ Accessibility score: **"!" (error)**
- ❌ color-contrast audit: **Error/Incomplete**
- ❌ Cannot calculate contrast ratios

### After Fix
- ✅ Accessibility score: **85-100** (numeric score)
- ✅ color-contrast audit: **Pass** (or specific items listed)
- ✅ All contrast ratios calculable

---

## 🚀 Quick Fix Workflow

### 5-Minute Emergency Fix

If you need to fix this urgently:

```bash
# Step 1: Remove backdrop-blur (CRITICAL!)
# Find & replace in all components
grep -r "backdrop-blur" components/ app/
# Replace: backdrop-blur-sm → (delete)

# Step 2: Increase low opacity
# Find & replace in all components
grep -r "/10\|/20\|/30" components/
# Replace: /10 → /40, /20 → /40, /30 → /60

# Step 3: Build & verify
npm run build

# Step 4: Deploy
git add .
git commit -m "Fix accessibility contrast audit errors"
git push
```

### Comprehensive Fix (Recommended)

Follow all 5 phases:
1. Remove CSS Filters (~10 min)
2. Convert Color Space (~15 min)
3. Increase Opacity Thresholds (~10 min)
4. Handle Gradient Text (~15 min, if applicable)
5. Add Image Overlays (~10 min, if applicable)

**Total Time**: ~1 hour for thorough fix

---

## 🔧 Tools & Resources

### Diagnostic Tools

**Online**:
- [PageSpeed Insights](https://pagespeed.web.dev/)
- [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/)

**Browser Extensions**:
- [axe DevTools](https://www.deque.com/axe/devtools/) (Chrome/Firefox)
- [WAVE](https://wave.webaim.org/extension/) (Chrome/Firefox)

**CLI Tools**:
```bash
# axe-core CLI
npx @axe-core/cli https://your-site.com

# Lighthouse CLI
npm install -g lighthouse
lighthouse https://your-site.com --only-categories=accessibility
```

### Contrast Standards (WCAG 2.1)

| Text Size | Min Contrast | Example |
|-----------|--------------|---------|
| Small (< 18pt) | 4.5:1 | Body text, buttons |
| Large (≥ 18pt) | 3.0:1 | Headings, hero text |
| Large bold (≥ 14pt) | 3.0:1 | Bold headings |

### Reference Documentation

**Official Standards**:
- [WCAG 2.1 Contrast Requirements](https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum.html)
- [MDN: Canvas CORS](https://developer.mozilla.org/en-US/docs/Web/HTML/How_to/CORS_enabled_image)

**GitHub Issues** (for deep dive):
- [Lighthouse #15002](https://github.com/GoogleChrome/lighthouse/issues/15002) - getImageData errors
- [axe-core #4628](https://github.com/dequelabs/axe-core/issues/4628) - Gradient background support

---

## ⚠️ Common Mistakes to Avoid

### ❌ Mistake 1: Thinking "!" = Low Score
**Reality**: "!" means measurement failed, not score is low.
**Fix**: Address the root cause (CSS filters, color space), not try to "improve score"

### ❌ Mistake 2: Only Fixing Obvious Contrast Issues
**Reality**: Hidden CSS filters or color space issues are often the culprit.
**Fix**: Use systematic checklist, don't cherry-pick

### ❌ Mistake 3: Skipping Local Testing
**Reality**: PageSpeed Insights updates with 24-48 hour delay.
**Fix**: Test locally with Lighthouse/axe before deployment

### ❌ Mistake 4: Using OKLCH for "Better Colors"
**Reality**: OKLCH breaks axe-core contrast calculations.
**Fix**: Use HSL/RGB for production, even if OKLCH looks better

### ❌ Mistake 5: Relying on Build Success
**Reality**: `npm run build` success ≠ Accessibility compliance.
**Fix**: Always run Lighthouse after build

---

## 🎯 Prevention Strategy

### For New Projects

**1. Template Configuration**
```css
/* ✅ Use HSL from day one */
:root {
  --background: hsl(0, 0%, 100%);
  --foreground: hsl(0, 0%, 10%);
  /* No OKLCH! */
}
```

**2. Tailwind Safeguards**
```javascript
// tailwind.config.js
module.exports = {
  // Avoid low opacity utilities
  theme: {
    extend: {
      // Use named opacity values
      opacity: {
        'safe': '0.6',  // Instead of /10, /20, /30
      }
    }
  }
}
```

**3. Development Checks**
```bash
# Add to pre-commit hook or CI/CD
npm run build && lighthouse http://localhost:3000 --only-categories=accessibility
```

### For Existing Projects

**Quarterly Audit**:
- Run full Lighthouse check
- Review new components for CSS filters
- Check for new low-opacity backgrounds
- Validate color space in theme files

---

## 📈 Expected Outcomes

### Immediate Impact
- ✅ Accessibility score displays normally (85-100)
- ✅ No more getImageData errors
- ✅ All contrast ratios calculable

### Long-term Benefits
- 📈 Improved SEO rankings (Accessibility is a ranking factor)
- 👥 Better user experience for all users
- ⚖️ Legal compliance (ADA, WCAG 2.1 AA)
- 🤖 Better visibility in AI/LLM results (GEO)

---

## 🎓 Skill Mastery Checklist

You've mastered this skill when you can:

- [ ] Diagnose "!" vs numeric score in under 2 minutes
- [ ] Identify CSS filter issues without tools (code review)
- [ ] Convert OKLCH to HSL accurately
- [ ] Know when opacity is "too low" (< 0.4) at a glance
- [ ] Fix most issues in under 1 hour
- [ ] Prevent issues in new projects from day one
- [ ] Explain the root cause to non-technical stakeholders

---

## 📚 Advanced Topics

### Understanding getImageData Failure

**Why it happens**:
1. Canvas is "tainted" by cross-origin images
2. CSS filters make pixel data unreliable
3. New color spaces (OKLCH) not fully supported by axe-core
4. Low opacity makes sampling results unstable

**Technical deep dive**:
- axe-core uses canvas to sample background colors
- Calls `getImageData()` to read pixels
- If canvas is tainted or data is unreliable → Error
- Error in color-contrast audit → No accessibility score

### CI/CD Integration

```yaml
# .github/workflows/accessibility.yml
name: Accessibility Check

on: [push, pull_request]

jobs:
  lighthouse:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Run Lighthouse CI
        uses: treosh/lighthouse-ci-action@v9
        with:
          urls: |
            http://localhost:3000
          uploadArtifacts: true
          temporaryPublicStorage: true
          budgetPath: ./budget.json
```

---

**Skill Version**: 1.0
**Last Updated**: 2025-10-19
**Tested On**: Next.js 15, React 18, Tailwind CSS 4

---

## 🤝 Contributing

Found a new trigger or fix? This skill document can be updated with:
- New edge cases
- Additional diagnostic methods
- Faster fix workflows
- Tool recommendations

Keep the skill sharp and up-to-date! 🚀
