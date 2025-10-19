# Shipany - Internationalization

**Pages:** 5

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/tutorials/customize-landing-page#修改-landing-page-内容

**Contents:**
- 自定义 Landing Page
- 修改 Landing Page 内容
  - 使用 AI 编辑器生成新的 Landing Page 内容
  - 使用 AI 对话产品，生成新的 Landing Page 内容
- 修改 Landing Page 页面结构

Landing Page 是 ShipAny 的特色功能之一，你可以通过简单的配置，自定义 Landing Page 的样式和内容。

ShipAny 内置一个 Landing Page 页面，通过 JSON 文件定义了页面上的全部内容。

默认支持多语言，英文 Landing Page 文件位于 i18n/pages/landing/en.json 文件中。

中文 Landing Page 文件位于 i18n/pages/landing/zh.json 文件中。

你可以在 i18n/pages/landing 目录下，添加其他语言的 Landing Page 文件。

Landing Page 文件包括以下几部分内容，你可以根据自己的需求，修改成对应的内容。

你可以在 AI 编辑器 Cursor 中，输入你的新网站主题，通过 AI 对话，指定参考资料，生成新网站的 Landing Page 内容。

你可以复制默认的 Landing Page 内容，使用 AI 对话产品，比如：ThinkAny / v0 / Claude / ChatGPT / Kimi 等， 生成新的 Landing Page 内容。

默认的 Landing Page 布局文件位于 app/[locale]/(default)/layout.tsx 文件中。

首页的内容结构位于 app/[locale]/(default)/page.tsx 文件中。

你可以根据新网站的需求，自行修改。比如删除部分组件，或者添加一些新组件。

每个组件支持传递的参数，请在组件文档部分查看。

**Examples:**

Example 1 (unknown):
```unknown
{
  "template": "shipany-template-one",
  "theme": "light",
  "header": {},
  "hero": {},
  "branding": {},
  "introduce": {},
  "benefit": {},
  "usage": {},
  "feature": {},
  "showcase": {},
  "stats": {},
  "pricing": {},
  "testimonial": {},
  "faq": {},
  "cta": {},
  "footer": {}
}
```

Example 2 (unknown):
```unknown
{
  "template": "shipany-template-one",
  "theme": "light",
  "header": {},
  "hero": {},
  "branding": {},
  "introduce": {},
  "benefit": {},
  "usage": {},
  "feature": {},
  "showcase": {},
  "stats": {},
  "pricing": {},
  "testimonial": {},
  "faq": {},
  "cta": {},
  "footer": {}
}
```

Example 3 (unknown):
```unknown
I want to build a landing page for my product named "Flux AI Image Generator", please update the landing page json file, content reference @Web @https://www.flux.ai/
```

Example 4 (unknown):
```unknown
I want to build a landing page for my product named "Flux AI Image Generator", please update the landing page json file, content reference @Web @https://www.flux.ai/
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/tutorials/customize-landing-page#使用-ai-对话产品生成新的-landing-page-内容

**Contents:**
- 自定义 Landing Page
- 修改 Landing Page 内容
  - 使用 AI 编辑器生成新的 Landing Page 内容
  - 使用 AI 对话产品，生成新的 Landing Page 内容
- 修改 Landing Page 页面结构

Landing Page 是 ShipAny 的特色功能之一，你可以通过简单的配置，自定义 Landing Page 的样式和内容。

ShipAny 内置一个 Landing Page 页面，通过 JSON 文件定义了页面上的全部内容。

默认支持多语言，英文 Landing Page 文件位于 i18n/pages/landing/en.json 文件中。

中文 Landing Page 文件位于 i18n/pages/landing/zh.json 文件中。

你可以在 i18n/pages/landing 目录下，添加其他语言的 Landing Page 文件。

Landing Page 文件包括以下几部分内容，你可以根据自己的需求，修改成对应的内容。

你可以在 AI 编辑器 Cursor 中，输入你的新网站主题，通过 AI 对话，指定参考资料，生成新网站的 Landing Page 内容。

你可以复制默认的 Landing Page 内容，使用 AI 对话产品，比如：ThinkAny / v0 / Claude / ChatGPT / Kimi 等， 生成新的 Landing Page 内容。

默认的 Landing Page 布局文件位于 app/[locale]/(default)/layout.tsx 文件中。

首页的内容结构位于 app/[locale]/(default)/page.tsx 文件中。

你可以根据新网站的需求，自行修改。比如删除部分组件，或者添加一些新组件。

每个组件支持传递的参数，请在组件文档部分查看。

**Examples:**

Example 1 (unknown):
```unknown
{
  "template": "shipany-template-one",
  "theme": "light",
  "header": {},
  "hero": {},
  "branding": {},
  "introduce": {},
  "benefit": {},
  "usage": {},
  "feature": {},
  "showcase": {},
  "stats": {},
  "pricing": {},
  "testimonial": {},
  "faq": {},
  "cta": {},
  "footer": {}
}
```

Example 2 (unknown):
```unknown
{
  "template": "shipany-template-one",
  "theme": "light",
  "header": {},
  "hero": {},
  "branding": {},
  "introduce": {},
  "benefit": {},
  "usage": {},
  "feature": {},
  "showcase": {},
  "stats": {},
  "pricing": {},
  "testimonial": {},
  "faq": {},
  "cta": {},
  "footer": {}
}
```

Example 3 (unknown):
```unknown
I want to build a landing page for my product named "Flux AI Image Generator", please update the landing page json file, content reference @Web @https://www.flux.ai/
```

Example 4 (unknown):
```unknown
I want to build a landing page for my product named "Flux AI Image Generator", please update the landing page json file, content reference @Web @https://www.flux.ai/
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/tutorials/customize-landing-page#修改-landing-page-页面结构

**Contents:**
- 自定义 Landing Page
- 修改 Landing Page 内容
  - 使用 AI 编辑器生成新的 Landing Page 内容
  - 使用 AI 对话产品，生成新的 Landing Page 内容
- 修改 Landing Page 页面结构

Landing Page 是 ShipAny 的特色功能之一，你可以通过简单的配置，自定义 Landing Page 的样式和内容。

ShipAny 内置一个 Landing Page 页面，通过 JSON 文件定义了页面上的全部内容。

默认支持多语言，英文 Landing Page 文件位于 i18n/pages/landing/en.json 文件中。

中文 Landing Page 文件位于 i18n/pages/landing/zh.json 文件中。

你可以在 i18n/pages/landing 目录下，添加其他语言的 Landing Page 文件。

Landing Page 文件包括以下几部分内容，你可以根据自己的需求，修改成对应的内容。

你可以在 AI 编辑器 Cursor 中，输入你的新网站主题，通过 AI 对话，指定参考资料，生成新网站的 Landing Page 内容。

你可以复制默认的 Landing Page 内容，使用 AI 对话产品，比如：ThinkAny / v0 / Claude / ChatGPT / Kimi 等， 生成新的 Landing Page 内容。

默认的 Landing Page 布局文件位于 app/[locale]/(default)/layout.tsx 文件中。

首页的内容结构位于 app/[locale]/(default)/page.tsx 文件中。

你可以根据新网站的需求，自行修改。比如删除部分组件，或者添加一些新组件。

每个组件支持传递的参数，请在组件文档部分查看。

**Examples:**

Example 1 (unknown):
```unknown
{
  "template": "shipany-template-one",
  "theme": "light",
  "header": {},
  "hero": {},
  "branding": {},
  "introduce": {},
  "benefit": {},
  "usage": {},
  "feature": {},
  "showcase": {},
  "stats": {},
  "pricing": {},
  "testimonial": {},
  "faq": {},
  "cta": {},
  "footer": {}
}
```

Example 2 (unknown):
```unknown
{
  "template": "shipany-template-one",
  "theme": "light",
  "header": {},
  "hero": {},
  "branding": {},
  "introduce": {},
  "benefit": {},
  "usage": {},
  "feature": {},
  "showcase": {},
  "stats": {},
  "pricing": {},
  "testimonial": {},
  "faq": {},
  "cta": {},
  "footer": {}
}
```

Example 3 (unknown):
```unknown
I want to build a landing page for my product named "Flux AI Image Generator", please update the landing page json file, content reference @Web @https://www.flux.ai/
```

Example 4 (unknown):
```unknown
I want to build a landing page for my product named "Flux AI Image Generator", please update the landing page json file, content reference @Web @https://www.flux.ai/
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/tutorials/customize-landing-page

**Contents:**
- 自定义 Landing Page
- 修改 Landing Page 内容
  - 使用 AI 编辑器生成新的 Landing Page 内容
  - 使用 AI 对话产品，生成新的 Landing Page 内容
- 修改 Landing Page 页面结构

Landing Page 是 ShipAny 的特色功能之一，你可以通过简单的配置，自定义 Landing Page 的样式和内容。

ShipAny 内置一个 Landing Page 页面，通过 JSON 文件定义了页面上的全部内容。

默认支持多语言，英文 Landing Page 文件位于 i18n/pages/landing/en.json 文件中。

中文 Landing Page 文件位于 i18n/pages/landing/zh.json 文件中。

你可以在 i18n/pages/landing 目录下，添加其他语言的 Landing Page 文件。

Landing Page 文件包括以下几部分内容，你可以根据自己的需求，修改成对应的内容。

你可以在 AI 编辑器 Cursor 中，输入你的新网站主题，通过 AI 对话，指定参考资料，生成新网站的 Landing Page 内容。

你可以复制默认的 Landing Page 内容，使用 AI 对话产品，比如：ThinkAny / v0 / Claude / ChatGPT / Kimi 等， 生成新的 Landing Page 内容。

默认的 Landing Page 布局文件位于 app/[locale]/(default)/layout.tsx 文件中。

首页的内容结构位于 app/[locale]/(default)/page.tsx 文件中。

你可以根据新网站的需求，自行修改。比如删除部分组件，或者添加一些新组件。

每个组件支持传递的参数，请在组件文档部分查看。

**Examples:**

Example 1 (unknown):
```unknown
{
  "template": "shipany-template-one",
  "theme": "light",
  "header": {},
  "hero": {},
  "branding": {},
  "introduce": {},
  "benefit": {},
  "usage": {},
  "feature": {},
  "showcase": {},
  "stats": {},
  "pricing": {},
  "testimonial": {},
  "faq": {},
  "cta": {},
  "footer": {}
}
```

Example 2 (unknown):
```unknown
{
  "template": "shipany-template-one",
  "theme": "light",
  "header": {},
  "hero": {},
  "branding": {},
  "introduce": {},
  "benefit": {},
  "usage": {},
  "feature": {},
  "showcase": {},
  "stats": {},
  "pricing": {},
  "testimonial": {},
  "faq": {},
  "cta": {},
  "footer": {}
}
```

Example 3 (unknown):
```unknown
I want to build a landing page for my product named "Flux AI Image Generator", please update the landing page json file, content reference @Web @https://www.flux.ai/
```

Example 4 (unknown):
```unknown
I want to build a landing page for my product named "Flux AI Image Generator", please update the landing page json file, content reference @Web @https://www.flux.ai/
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/tutorials/customize-landing-page#使用-ai-编辑器生成新的-landing-page-内容

**Contents:**
- 自定义 Landing Page
- 修改 Landing Page 内容
  - 使用 AI 编辑器生成新的 Landing Page 内容
  - 使用 AI 对话产品，生成新的 Landing Page 内容
- 修改 Landing Page 页面结构

Landing Page 是 ShipAny 的特色功能之一，你可以通过简单的配置，自定义 Landing Page 的样式和内容。

ShipAny 内置一个 Landing Page 页面，通过 JSON 文件定义了页面上的全部内容。

默认支持多语言，英文 Landing Page 文件位于 i18n/pages/landing/en.json 文件中。

中文 Landing Page 文件位于 i18n/pages/landing/zh.json 文件中。

你可以在 i18n/pages/landing 目录下，添加其他语言的 Landing Page 文件。

Landing Page 文件包括以下几部分内容，你可以根据自己的需求，修改成对应的内容。

你可以在 AI 编辑器 Cursor 中，输入你的新网站主题，通过 AI 对话，指定参考资料，生成新网站的 Landing Page 内容。

你可以复制默认的 Landing Page 内容，使用 AI 对话产品，比如：ThinkAny / v0 / Claude / ChatGPT / Kimi 等， 生成新的 Landing Page 内容。

默认的 Landing Page 布局文件位于 app/[locale]/(default)/layout.tsx 文件中。

首页的内容结构位于 app/[locale]/(default)/page.tsx 文件中。

你可以根据新网站的需求，自行修改。比如删除部分组件，或者添加一些新组件。

每个组件支持传递的参数，请在组件文档部分查看。

**Examples:**

Example 1 (unknown):
```unknown
{
  "template": "shipany-template-one",
  "theme": "light",
  "header": {},
  "hero": {},
  "branding": {},
  "introduce": {},
  "benefit": {},
  "usage": {},
  "feature": {},
  "showcase": {},
  "stats": {},
  "pricing": {},
  "testimonial": {},
  "faq": {},
  "cta": {},
  "footer": {}
}
```

Example 2 (unknown):
```unknown
{
  "template": "shipany-template-one",
  "theme": "light",
  "header": {},
  "hero": {},
  "branding": {},
  "introduce": {},
  "benefit": {},
  "usage": {},
  "feature": {},
  "showcase": {},
  "stats": {},
  "pricing": {},
  "testimonial": {},
  "faq": {},
  "cta": {},
  "footer": {}
}
```

Example 3 (unknown):
```unknown
I want to build a landing page for my product named "Flux AI Image Generator", please update the landing page json file, content reference @Web @https://www.flux.ai/
```

Example 4 (unknown):
```unknown
I want to build a landing page for my product named "Flux AI Image Generator", please update the landing page json file, content reference @Web @https://www.flux.ai/
```

---
