# Shipany - Components

**Pages:** 38

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/components/hero

**Contents:**
- Hero
- custom hero in page
- Hero Type

**Examples:**

Example 1 (python):
```python
import Hero from "@/components/blocks/hero";
import { Hero as HeroType } from "@/types/blocks/hero";
 
export default function Page() {
  // custom hero data
  const hero: HeroType = {
    title: "Ship Any AI Startups in hours, not days",
    highlight_text: "Ship Any",
    description:
      "ShipAny is a NextJS boilerplate for building AI SaaS startups.<br/>Ship Fast with a variety of templates and components.",
    announcement: {
      title: "🎉 Happy New Year",
      url: "/#pricing",
    },
    buttons: [
      {
        title: "Get ShipAny",
        url: "/ai-podcast-generator",
      }
...
```

Example 2 (python):
```python
import Hero from "@/components/blocks/hero";
import { Hero as HeroType } from "@/types/blocks/hero";
 
export default function Page() {
  // custom hero data
  const hero: HeroType = {
    title: "Ship Any AI Startups in hours, not days",
    highlight_text: "Ship Any",
    description:
      "ShipAny is a NextJS boilerplate for building AI SaaS startups.<br/>Ship Fast with a variety of templates and components.",
    announcement: {
      title: "🎉 Happy New Year",
      url: "/#pricing",
    },
    buttons: [
      {
        title: "Get ShipAny",
        url: "/ai-podcast-generator",
      }
...
```

Example 3 (unknown):
```unknown
export interface Hero {
  disabled?: boolean;
  title?: string;
  highlight_text?: string;
  description?: string;
  buttons?: Button[];
  image?: Image;
  announcement?: Announcement;
  show_happy_users?: boolean;
}
```

Example 4 (unknown):
```unknown
export interface Hero {
  disabled?: boolean;
  title?: string;
  highlight_text?: string;
  description?: string;
  buttons?: Button[];
  image?: Image;
  announcement?: Announcement;
  show_happy_users?: boolean;
}
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/components/footer

---

## Feature | ShipAny Docs

**URL:** https://docs.shipany.ai/zh/components/feature

**Contents:**
- Feature
- custom Feature in page
- Feature Type

**Examples:**

Example 1 (python):
```python
import Feature from "@/components/blocks/feature";
import { Feature as FeatureType } from "@/types/blocks/feature";
 
export default function Page() {
  // custom Feature data
  const feature: FeatureType = {
    "title": "Key Features of ShipAny",
    "description": "Everything you need to launch your AI SaaS startup quickly and efficiently.",
    "items": [
      {
        "title": "Next.js Boilerplate",
        "description": "Production-ready Next.js templates with SEO-friendly structure and i18n support.",
        "icon": "Sparkles"
      },
      // ...other features
    ],
  };
 
  retu
...
```

Example 2 (python):
```python
import Feature from "@/components/blocks/feature";
import { Feature as FeatureType } from "@/types/blocks/feature";
 
export default function Page() {
  // custom Feature data
  const feature: FeatureType = {
    "title": "Key Features of ShipAny",
    "description": "Everything you need to launch your AI SaaS startup quickly and efficiently.",
    "items": [
      {
        "title": "Next.js Boilerplate",
        "description": "Production-ready Next.js templates with SEO-friendly structure and i18n support.",
        "icon": "Sparkles"
      },
      // ...other features
    ],
  };
 
  retu
...
```

Example 3 (python):
```python
import { Image } from "@/types/blocks/image";
 
export interface FeatureItem {
  title: string;
  description: string;
  icon?: string;
  image?: Image;
}
 
export interface Feature {
  title: string;
  description: string;
  items: FeatureItem[];
}
```

Example 4 (python):
```python
import { Image } from "@/types/blocks/image";
 
export interface FeatureItem {
  title: string;
  description: string;
  icon?: string;
  image?: Image;
}
 
export interface Feature {
  title: string;
  description: string;
  items: FeatureItem[];
}
```

---

## Header | ShipAny Docs

**URL:** https://docs.shipany.ai/zh/components/header#custom-header-in-page

**Contents:**
- Header
- custom header in page
- Header Type

**Examples:**

Example 1 (python):
```python
import Header from "@/components/blocks/header";
import { Header as HeaderType } from "@/types/blocks/header";
 
export default function Page() {
  // custom header data
  const header: HeaderType = {
    logo: {
      title: "ShipAny",
      image: {
        src: "/logo.png",
        alt: "ShipAny",
      },
    },
    nav: {
      items: [
        {
          title: "Features",
          href: "/features",
        },
        {
          title: "Pricing",
          href: "/pricing",
        },
        {
          title: "Showcases",
          children: [
            {
              title: "Sh
...
```

Example 2 (python):
```python
import Header from "@/components/blocks/header";
import { Header as HeaderType } from "@/types/blocks/header";
 
export default function Page() {
  // custom header data
  const header: HeaderType = {
    logo: {
      title: "ShipAny",
      image: {
        src: "/logo.png",
        alt: "ShipAny",
      },
    },
    nav: {
      items: [
        {
          title: "Features",
          href: "/features",
        },
        {
          title: "Pricing",
          href: "/pricing",
        },
        {
          title: "Showcases",
          children: [
            {
              title: "Sh
...
```

Example 3 (unknown):
```unknown
export interface Header {
  disabled?: boolean;
  logo?: Logo;
  nav?: Nav;
  buttons?: Button[];
  className?: string;
}
```

Example 4 (unknown):
```unknown
export interface Header {
  disabled?: boolean;
  logo?: Logo;
  nav?: Nav;
  buttons?: Button[];
  className?: string;
}
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/admin-system/new-table

**Contents:**
- 添加表格视图
- 渲染数据表格

在创建完管理后台布局之后，你可以新建一个 page.tsx 页面，用数据表的形式管理数据。

ShipAny 内置了一个表格视图组件，可以快速渲染一个数据表格，用于各类列表形式的数据展示。

你只需要 import 表格视图组件 @/components/dashboard/slots/table，定义数据表格字段，再传递一份 data 即可。

参考系统内置的后台管理系统， 用户列表页面实现逻辑：

**Examples:**

Example 1 (python):
```python
import { TableColumn } from "@/types/blocks/table";
import TableSlot from "@/components/dashboard/slots/table";
import { Table as TableSlotType } from "@/types/slots/table";
import { getUsers } from "@/models/user";
import moment from "moment";
 
export default async function () {
  const users = await getUsers(1, 50);
 
  const columns: TableColumn[] = [
    { name: "uuid", title: "UUID" },
    { name: "email", title: "Email" },
    { name: "nickname", title: "Name" },
    {
      name: "avatar_url",
      title: "Avatar",
      callback: (row) => (
        <img src={row.avatar_url} className
...
```

Example 2 (python):
```python
import { TableColumn } from "@/types/blocks/table";
import TableSlot from "@/components/dashboard/slots/table";
import { Table as TableSlotType } from "@/types/slots/table";
import { getUsers } from "@/models/user";
import moment from "moment";
 
export default async function () {
  const users = await getUsers(1, 50);
 
  const columns: TableColumn[] = [
    { name: "uuid", title: "UUID" },
    { name: "email", title: "Email" },
    { name: "nickname", title: "Name" },
    {
      name: "avatar_url",
      title: "Avatar",
      callback: (row) => (
        <img src={row.avatar_url} className
...
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/guide/good-to-know

**Contents:**
- 前置说明
- ShipAny 是什么
- ShipAny 框架包含哪些功能
- 技术依赖
- 环境依赖
- AI 辅助编程工具
- AI 编辑器插件

ShipAny 是一个基于 NextJS 的 AI SaaS 开发框架，内置丰富的组件和 AI SDK，帮助你快速完成 AI SaaS 项目开发。

其他需求可以在 Github Issues 提交，按优先级支持。

ShipAny 基于 NextJS 框架构建，用到了诸多流行的技术组件和云服务。

为确保你能充分使用 ShipAny 的完整功能，请自行熟悉以下技术/组件或云服务：

为确保你能顺利在本地运行和二次开发 ShipAny，请在你的电脑上安装必要的环境。

推荐使用以下版本的 NodeJS 和 npm：

其他操作系统，请自行搜索对应的环境配置方法。运行 ShipAny 代码之前，请确保你的电脑环境已经安装了 nodejs 和 pnpm。

为了更好的理解 ShipAny 框架，更高效的开发项目，推荐使用以下 AI 辅助编程工具：

为了更好的格式化代码，更方便的调试接口，推荐在 VS Code / Cursor / Windsurf 等编辑器中安装以下插件：

**Examples:**

Example 1 (unknown):
```unknown
$ node -v
v22.2.0
 
$ npm -v
10.7.0
```

Example 2 (unknown):
```unknown
$ node -v
v22.2.0
 
$ npm -v
10.7.0
```

Example 3 (unknown):
```unknown
$ npm install -g pnpm
```

Example 4 (unknown):
```unknown
$ npm install -g pnpm
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/guide/course

**Contents:**
- 视频课程
- 使用 shipany.ai 一小时上线 AI 壁纸生成器：
  - 第一集：使用 ShipAny 一小时上站
  - 第二集：对接 AI 接口，实现壁纸生成，完成业务功能开发
  - 第三集：对接支付系统，核销用户积分，实现壁纸管理后台

https://www.bilibili.com/video/BV1ooK7eJEag

https://www.bilibili.com/video/BV1v1KnesEbg

https://www.bilibili.com/video/BV1VUKnepEoY

---

## CTA | ShipAny Docs

**URL:** https://docs.shipany.ai/zh/components/cta

**Contents:**
- CTA (Call to Action)
- custom CTA in page
- CTA Type

**Examples:**

Example 1 (python):
```python
import CTA from "@/components/blocks/cta";
import { CTA as CTAType } from "@/types/blocks/cta";
 
export default function Page() {
  // custom CTA data
  const cta: CTAType =  {
    "title": "Ship your first AI SaaS Startup",
    "description": "Start from here, with ShipAny.",
    "buttons": [
      {
        "title": "Get ShipAny",
        "url": "/#pricing"
      }
    ]
  }
 
  return <>
      <CTA cta={cta} />
      // ...other components
    </>
  );
}
```

Example 2 (python):
```python
import CTA from "@/components/blocks/cta";
import { CTA as CTAType } from "@/types/blocks/cta";
 
export default function Page() {
  // custom CTA data
  const cta: CTAType =  {
    "title": "Ship your first AI SaaS Startup",
    "description": "Start from here, with ShipAny.",
    "buttons": [
      {
        "title": "Get ShipAny",
        "url": "/#pricing"
      }
    ]
  }
 
  return <>
      <CTA cta={cta} />
      // ...other components
    </>
  );
}
```

Example 3 (python):
```python
import { Button } from "@/types/blocks/button";
 
export interface CTA {
  disabled?: boolean;
  title?: string;
  description?: string;
  buttons?: Button[];
}
```

Example 4 (python):
```python
import { Button } from "@/types/blocks/button";
 
export interface CTA {
  disabled?: boolean;
  title?: string;
  description?: string;
  buttons?: Button[];
}
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/components/pricing

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/guide/good-to-know#ai-辅助编程工具

**Contents:**
- 前置说明
- ShipAny 是什么
- ShipAny 框架包含哪些功能
- 技术依赖
- 环境依赖
- AI 辅助编程工具
- AI 编辑器插件

ShipAny 是一个基于 NextJS 的 AI SaaS 开发框架，内置丰富的组件和 AI SDK，帮助你快速完成 AI SaaS 项目开发。

其他需求可以在 Github Issues 提交，按优先级支持。

ShipAny 基于 NextJS 框架构建，用到了诸多流行的技术组件和云服务。

为确保你能充分使用 ShipAny 的完整功能，请自行熟悉以下技术/组件或云服务：

为确保你能顺利在本地运行和二次开发 ShipAny，请在你的电脑上安装必要的环境。

推荐使用以下版本的 NodeJS 和 npm：

其他操作系统，请自行搜索对应的环境配置方法。运行 ShipAny 代码之前，请确保你的电脑环境已经安装了 nodejs 和 pnpm。

为了更好的理解 ShipAny 框架，更高效的开发项目，推荐使用以下 AI 辅助编程工具：

为了更好的格式化代码，更方便的调试接口，推荐在 VS Code / Cursor / Windsurf 等编辑器中安装以下插件：

**Examples:**

Example 1 (unknown):
```unknown
$ node -v
v22.2.0
 
$ npm -v
10.7.0
```

Example 2 (unknown):
```unknown
$ node -v
v22.2.0
 
$ npm -v
10.7.0
```

Example 3 (unknown):
```unknown
$ npm install -g pnpm
```

Example 4 (unknown):
```unknown
$ npm install -g pnpm
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/guide/good-to-know#环境依赖

**Contents:**
- 前置说明
- ShipAny 是什么
- ShipAny 框架包含哪些功能
- 技术依赖
- 环境依赖
- AI 辅助编程工具
- AI 编辑器插件

ShipAny 是一个基于 NextJS 的 AI SaaS 开发框架，内置丰富的组件和 AI SDK，帮助你快速完成 AI SaaS 项目开发。

其他需求可以在 Github Issues 提交，按优先级支持。

ShipAny 基于 NextJS 框架构建，用到了诸多流行的技术组件和云服务。

为确保你能充分使用 ShipAny 的完整功能，请自行熟悉以下技术/组件或云服务：

为确保你能顺利在本地运行和二次开发 ShipAny，请在你的电脑上安装必要的环境。

推荐使用以下版本的 NodeJS 和 npm：

其他操作系统，请自行搜索对应的环境配置方法。运行 ShipAny 代码之前，请确保你的电脑环境已经安装了 nodejs 和 pnpm。

为了更好的理解 ShipAny 框架，更高效的开发项目，推荐使用以下 AI 辅助编程工具：

为了更好的格式化代码，更方便的调试接口，推荐在 VS Code / Cursor / Windsurf 等编辑器中安装以下插件：

**Examples:**

Example 1 (unknown):
```unknown
$ node -v
v22.2.0
 
$ npm -v
10.7.0
```

Example 2 (unknown):
```unknown
$ node -v
v22.2.0
 
$ npm -v
10.7.0
```

Example 3 (unknown):
```unknown
$ npm install -g pnpm
```

Example 4 (unknown):
```unknown
$ npm install -g pnpm
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/guide/course#第一集使用-shipany-一小时上站

**Contents:**
- 视频课程
- 使用 shipany.ai 一小时上线 AI 壁纸生成器：
  - 第一集：使用 ShipAny 一小时上站
  - 第二集：对接 AI 接口，实现壁纸生成，完成业务功能开发
  - 第三集：对接支付系统，核销用户积分，实现壁纸管理后台

https://www.bilibili.com/video/BV1ooK7eJEag

https://www.bilibili.com/video/BV1v1KnesEbg

https://www.bilibili.com/video/BV1VUKnepEoY

---

## Testimonial | ShipAny Docs

**URL:** https://docs.shipany.ai/zh/components/testimonial#testimonial-type

**Contents:**
- Testimonial
- custom Testimonial in page
- Testimonial Type

**Examples:**

Example 1 (python):
```python
import Testimonial from "@/components/blocks/testimonial";
import { Testimonial as TestimonialType } from "@/types/blocks/testimonial";
 
export default function Page() {
  // custom Testimonial data
  const testimonial: TestimonialType = {
    "title": "What Users Say About ShipAny",
    "description": "Hear from developers and founders who launched their AI startups with ShipAny.",
    "items": [
      {
        "avatar": {
          "src": "/imgs/user/1.png"
        },
        "name": "David Chen",
        "title": "Founder of AIWallpaper.shop",
        "comment": "ShipAny saved us months o
...
```

Example 2 (python):
```python
import Testimonial from "@/components/blocks/testimonial";
import { Testimonial as TestimonialType } from "@/types/blocks/testimonial";
 
export default function Page() {
  // custom Testimonial data
  const testimonial: TestimonialType = {
    "title": "What Users Say About ShipAny",
    "description": "Hear from developers and founders who launched their AI startups with ShipAny.",
    "items": [
      {
        "avatar": {
          "src": "/imgs/user/1.png"
        },
        "name": "David Chen",
        "title": "Founder of AIWallpaper.shop",
        "comment": "ShipAny saved us months o
...
```

Example 3 (python):
```python
import { Image } from "@/types/blocks/image";
 
export interface TestimonialItem {
  avatar?: Image;
  name?: string;
  title?: string;
  comment?: string;
}
 
export interface Testimonial {
  disabled?: boolean;
  title?: string;
  description?: string;
  items?: TestimonialItem[];
}
```

Example 4 (python):
```python
import { Image } from "@/types/blocks/image";
 
export interface TestimonialItem {
  avatar?: Image;
  name?: string;
  title?: string;
  comment?: string;
}
 
export interface Testimonial {
  disabled?: boolean;
  title?: string;
  description?: string;
  items?: TestimonialItem[];
}
```

---

## Feature | ShipAny Docs

**URL:** https://docs.shipany.ai/zh/components/feature#feature-type

**Contents:**
- Feature
- custom Feature in page
- Feature Type

**Examples:**

Example 1 (python):
```python
import Feature from "@/components/blocks/feature";
import { Feature as FeatureType } from "@/types/blocks/feature";
 
export default function Page() {
  // custom Feature data
  const feature: FeatureType = {
    "title": "Key Features of ShipAny",
    "description": "Everything you need to launch your AI SaaS startup quickly and efficiently.",
    "items": [
      {
        "title": "Next.js Boilerplate",
        "description": "Production-ready Next.js templates with SEO-friendly structure and i18n support.",
        "icon": "Sparkles"
      },
      // ...other features
    ],
  };
 
  retu
...
```

Example 2 (python):
```python
import Feature from "@/components/blocks/feature";
import { Feature as FeatureType } from "@/types/blocks/feature";
 
export default function Page() {
  // custom Feature data
  const feature: FeatureType = {
    "title": "Key Features of ShipAny",
    "description": "Everything you need to launch your AI SaaS startup quickly and efficiently.",
    "items": [
      {
        "title": "Next.js Boilerplate",
        "description": "Production-ready Next.js templates with SEO-friendly structure and i18n support.",
        "icon": "Sparkles"
      },
      // ...other features
    ],
  };
 
  retu
...
```

Example 3 (python):
```python
import { Image } from "@/types/blocks/image";
 
export interface FeatureItem {
  title: string;
  description: string;
  icon?: string;
  image?: Image;
}
 
export interface Feature {
  title: string;
  description: string;
  items: FeatureItem[];
}
```

Example 4 (python):
```python
import { Image } from "@/types/blocks/image";
 
export interface FeatureItem {
  title: string;
  description: string;
  icon?: string;
  image?: Image;
}
 
export interface Feature {
  title: string;
  description: string;
  items: FeatureItem[];
}
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/guide/good-to-know#shipany-是什么

**Contents:**
- 前置说明
- ShipAny 是什么
- ShipAny 框架包含哪些功能
- 技术依赖
- 环境依赖
- AI 辅助编程工具
- AI 编辑器插件

ShipAny 是一个基于 NextJS 的 AI SaaS 开发框架，内置丰富的组件和 AI SDK，帮助你快速完成 AI SaaS 项目开发。

其他需求可以在 Github Issues 提交，按优先级支持。

ShipAny 基于 NextJS 框架构建，用到了诸多流行的技术组件和云服务。

为确保你能充分使用 ShipAny 的完整功能，请自行熟悉以下技术/组件或云服务：

为确保你能顺利在本地运行和二次开发 ShipAny，请在你的电脑上安装必要的环境。

推荐使用以下版本的 NodeJS 和 npm：

其他操作系统，请自行搜索对应的环境配置方法。运行 ShipAny 代码之前，请确保你的电脑环境已经安装了 nodejs 和 pnpm。

为了更好的理解 ShipAny 框架，更高效的开发项目，推荐使用以下 AI 辅助编程工具：

为了更好的格式化代码，更方便的调试接口，推荐在 VS Code / Cursor / Windsurf 等编辑器中安装以下插件：

**Examples:**

Example 1 (unknown):
```unknown
$ node -v
v22.2.0
 
$ npm -v
10.7.0
```

Example 2 (unknown):
```unknown
$ node -v
v22.2.0
 
$ npm -v
10.7.0
```

Example 3 (unknown):
```unknown
$ npm install -g pnpm
```

Example 4 (unknown):
```unknown
$ npm install -g pnpm
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/user-console/console#用户中心

**Contents:**
- 控制台
- 用户中心
- 控制台布局

用户登录后，点击头像下拉，可以进入用户中心。查看自己的订单，编辑个人信息等。

你可以根据自己的需求，在用户控制台添加更多的功能。

ShipAny 内置了一个控制台布局，位于 components/console/layout.tsx 文件。

实现一个用户中心布局，只需要引入控制台布局组件，传递一个 sidebar 即可。

**Examples:**

Example 1 (python):
```python
import ConsoleLayout from "@/components/console/layout";
import { ReactNode } from "react";
import { Sidebar } from "@/types/blocks/sidebar";
import { getTranslations } from "next-intl/server";
import { getUserInfo } from "@/services/user";
import { redirect } from "next/navigation";
 
export default async function ({ children }: { children: ReactNode }) {
  const userInfo = await getUserInfo();
  if (!userInfo || !userInfo.email) {
    redirect("/auth/signin");
  }
 
  const t = await getTranslations();
 
  const sidebar: Sidebar = {
    nav: {
      items: [
        {
          title: t("use
...
```

Example 2 (python):
```python
import ConsoleLayout from "@/components/console/layout";
import { ReactNode } from "react";
import { Sidebar } from "@/types/blocks/sidebar";
import { getTranslations } from "next-intl/server";
import { getUserInfo } from "@/services/user";
import { redirect } from "next/navigation";
 
export default async function ({ children }: { children: ReactNode }) {
  const userInfo = await getUserInfo();
  if (!userInfo || !userInfo.email) {
    redirect("/auth/signin");
  }
 
  const t = await getTranslations();
 
  const sidebar: Sidebar = {
    nav: {
      items: [
        {
          title: t("use
...
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/tutorials/new-components#参考

**Contents:**
- 创建新组件
- AI 辅助创建新组件
- 参考

在 components 目录下，创建新的组件文件 new-component/index.tsx。

在 Cursor 中，通过 截图 + 提示词，让 AI 辅助生成新的组件代码。

建议可复用的组件，放在 components/blocks 目录下，业务组件放在 components 目录下。

**Examples:**

Example 1 (unknown):
```unknown
follow this screenshot, create a react function component for me, use shadcn/ui, tailwindcss
```

Example 2 (unknown):
```unknown
follow this screenshot, create a react function component for me, use shadcn/ui, tailwindcss
```

Example 3 (python):
```python
import { LoginForm } from "@/components/new-component";
 
export const runtime = "edge";
 
export default function NewPage() {
  return (
    <div className="container py-36 flex items-center justify-center">
      <LoginForm />
    </div>
  );
}
```

Example 4 (python):
```python
import { LoginForm } from "@/components/new-component";
 
export const runtime = "edge";
 
export default function NewPage() {
  return (
    <div className="container py-36 flex items-center justify-center">
      <LoginForm />
    </div>
  );
}
```

---

## Testimonial | ShipAny Docs

**URL:** https://docs.shipany.ai/zh/components/testimonial

**Contents:**
- Testimonial
- custom Testimonial in page
- Testimonial Type

**Examples:**

Example 1 (python):
```python
import Testimonial from "@/components/blocks/testimonial";
import { Testimonial as TestimonialType } from "@/types/blocks/testimonial";
 
export default function Page() {
  // custom Testimonial data
  const testimonial: TestimonialType = {
    "title": "What Users Say About ShipAny",
    "description": "Hear from developers and founders who launched their AI startups with ShipAny.",
    "items": [
      {
        "avatar": {
          "src": "/imgs/user/1.png"
        },
        "name": "David Chen",
        "title": "Founder of AIWallpaper.shop",
        "comment": "ShipAny saved us months o
...
```

Example 2 (python):
```python
import Testimonial from "@/components/blocks/testimonial";
import { Testimonial as TestimonialType } from "@/types/blocks/testimonial";
 
export default function Page() {
  // custom Testimonial data
  const testimonial: TestimonialType = {
    "title": "What Users Say About ShipAny",
    "description": "Hear from developers and founders who launched their AI startups with ShipAny.",
    "items": [
      {
        "avatar": {
          "src": "/imgs/user/1.png"
        },
        "name": "David Chen",
        "title": "Founder of AIWallpaper.shop",
        "comment": "ShipAny saved us months o
...
```

Example 3 (python):
```python
import { Image } from "@/types/blocks/image";
 
export interface TestimonialItem {
  avatar?: Image;
  name?: string;
  title?: string;
  comment?: string;
}
 
export interface Testimonial {
  disabled?: boolean;
  title?: string;
  description?: string;
  items?: TestimonialItem[];
}
```

Example 4 (python):
```python
import { Image } from "@/types/blocks/image";
 
export interface TestimonialItem {
  avatar?: Image;
  name?: string;
  title?: string;
  comment?: string;
}
 
export interface Testimonial {
  disabled?: boolean;
  title?: string;
  description?: string;
  items?: TestimonialItem[];
}
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/user-console/console#控制台布局

**Contents:**
- 控制台
- 用户中心
- 控制台布局

用户登录后，点击头像下拉，可以进入用户中心。查看自己的订单，编辑个人信息等。

你可以根据自己的需求，在用户控制台添加更多的功能。

ShipAny 内置了一个控制台布局，位于 components/console/layout.tsx 文件。

实现一个用户中心布局，只需要引入控制台布局组件，传递一个 sidebar 即可。

**Examples:**

Example 1 (python):
```python
import ConsoleLayout from "@/components/console/layout";
import { ReactNode } from "react";
import { Sidebar } from "@/types/blocks/sidebar";
import { getTranslations } from "next-intl/server";
import { getUserInfo } from "@/services/user";
import { redirect } from "next/navigation";
 
export default async function ({ children }: { children: ReactNode }) {
  const userInfo = await getUserInfo();
  if (!userInfo || !userInfo.email) {
    redirect("/auth/signin");
  }
 
  const t = await getTranslations();
 
  const sidebar: Sidebar = {
    nav: {
      items: [
        {
          title: t("use
...
```

Example 2 (python):
```python
import ConsoleLayout from "@/components/console/layout";
import { ReactNode } from "react";
import { Sidebar } from "@/types/blocks/sidebar";
import { getTranslations } from "next-intl/server";
import { getUserInfo } from "@/services/user";
import { redirect } from "next/navigation";
 
export default async function ({ children }: { children: ReactNode }) {
  const userInfo = await getUserInfo();
  if (!userInfo || !userInfo.email) {
    redirect("/auth/signin");
  }
 
  const t = await getTranslations();
 
  const sidebar: Sidebar = {
    nav: {
      items: [
        {
          title: t("use
...
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/guide/good-to-know#ai-编辑器插件

**Contents:**
- 前置说明
- ShipAny 是什么
- ShipAny 框架包含哪些功能
- 技术依赖
- 环境依赖
- AI 辅助编程工具
- AI 编辑器插件

ShipAny 是一个基于 NextJS 的 AI SaaS 开发框架，内置丰富的组件和 AI SDK，帮助你快速完成 AI SaaS 项目开发。

其他需求可以在 Github Issues 提交，按优先级支持。

ShipAny 基于 NextJS 框架构建，用到了诸多流行的技术组件和云服务。

为确保你能充分使用 ShipAny 的完整功能，请自行熟悉以下技术/组件或云服务：

为确保你能顺利在本地运行和二次开发 ShipAny，请在你的电脑上安装必要的环境。

推荐使用以下版本的 NodeJS 和 npm：

其他操作系统，请自行搜索对应的环境配置方法。运行 ShipAny 代码之前，请确保你的电脑环境已经安装了 nodejs 和 pnpm。

为了更好的理解 ShipAny 框架，更高效的开发项目，推荐使用以下 AI 辅助编程工具：

为了更好的格式化代码，更方便的调试接口，推荐在 VS Code / Cursor / Windsurf 等编辑器中安装以下插件：

**Examples:**

Example 1 (unknown):
```unknown
$ node -v
v22.2.0
 
$ npm -v
10.7.0
```

Example 2 (unknown):
```unknown
$ node -v
v22.2.0
 
$ npm -v
10.7.0
```

Example 3 (unknown):
```unknown
$ npm install -g pnpm
```

Example 4 (unknown):
```unknown
$ npm install -g pnpm
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/components/hero#hero-type

**Contents:**
- Hero
- custom hero in page
- Hero Type

**Examples:**

Example 1 (python):
```python
import Hero from "@/components/blocks/hero";
import { Hero as HeroType } from "@/types/blocks/hero";
 
export default function Page() {
  // custom hero data
  const hero: HeroType = {
    title: "Ship Any AI Startups in hours, not days",
    highlight_text: "Ship Any",
    description:
      "ShipAny is a NextJS boilerplate for building AI SaaS startups.<br/>Ship Fast with a variety of templates and components.",
    announcement: {
      title: "🎉 Happy New Year",
      url: "/#pricing",
    },
    buttons: [
      {
        title: "Get ShipAny",
        url: "/ai-podcast-generator",
      }
...
```

Example 2 (python):
```python
import Hero from "@/components/blocks/hero";
import { Hero as HeroType } from "@/types/blocks/hero";
 
export default function Page() {
  // custom hero data
  const hero: HeroType = {
    title: "Ship Any AI Startups in hours, not days",
    highlight_text: "Ship Any",
    description:
      "ShipAny is a NextJS boilerplate for building AI SaaS startups.<br/>Ship Fast with a variety of templates and components.",
    announcement: {
      title: "🎉 Happy New Year",
      url: "/#pricing",
    },
    buttons: [
      {
        title: "Get ShipAny",
        url: "/ai-podcast-generator",
      }
...
```

Example 3 (unknown):
```unknown
export interface Hero {
  disabled?: boolean;
  title?: string;
  highlight_text?: string;
  description?: string;
  buttons?: Button[];
  image?: Image;
  announcement?: Announcement;
  show_happy_users?: boolean;
}
```

Example 4 (unknown):
```unknown
export interface Hero {
  disabled?: boolean;
  title?: string;
  highlight_text?: string;
  description?: string;
  buttons?: Button[];
  image?: Image;
  announcement?: Announcement;
  show_happy_users?: boolean;
}
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/guide/faq

**Contents:**
- 常见问题
- 如何同步 ShipAny 最新代码
- 本地调试谷歌登录报错

拉取的上游代码可能跟你本地的修改有冲突，需要人工解决冲突。

解决完冲突后，建议本地编译验证一下，确保项目能正常运行，并且无编译报错。

出现这个错误的主要原因，是你本地网络的问题，没法直接请求谷歌的 API。

需要通过配置代理，解决科学上网问题。可以从以下几个方面尝试解决：

**Examples:**

Example 1 (unknown):
```unknown
git checkout -b backup
```

Example 2 (unknown):
```unknown
git checkout -b backup
```

Example 3 (unknown):
```unknown
git checkout main
git remote add upstream [email protected]:shipanyai/shipany-template-one.git
git fetch upstream
git merge upstream/main --allow-unrelated-histories
```

Example 4 (unknown):
```unknown
git checkout main
git remote add upstream [email protected]:shipanyai/shipany-template-one.git
git fetch upstream
git merge upstream/main --allow-unrelated-histories
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/tutorials/new-components

**Contents:**
- 创建新组件
- AI 辅助创建新组件
- 参考

在 components 目录下，创建新的组件文件 new-component/index.tsx。

在 Cursor 中，通过 截图 + 提示词，让 AI 辅助生成新的组件代码。

建议可复用的组件，放在 components/blocks 目录下，业务组件放在 components 目录下。

**Examples:**

Example 1 (unknown):
```unknown
follow this screenshot, create a react function component for me, use shadcn/ui, tailwindcss
```

Example 2 (unknown):
```unknown
follow this screenshot, create a react function component for me, use shadcn/ui, tailwindcss
```

Example 3 (python):
```python
import { LoginForm } from "@/components/new-component";
 
export const runtime = "edge";
 
export default function NewPage() {
  return (
    <div className="container py-36 flex items-center justify-center">
      <LoginForm />
    </div>
  );
}
```

Example 4 (python):
```python
import { LoginForm } from "@/components/new-component";
 
export const runtime = "edge";
 
export default function NewPage() {
  return (
    <div className="container py-36 flex items-center justify-center">
      <LoginForm />
    </div>
  );
}
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/user-console/console

**Contents:**
- 控制台
- 用户中心
- 控制台布局

用户登录后，点击头像下拉，可以进入用户中心。查看自己的订单，编辑个人信息等。

你可以根据自己的需求，在用户控制台添加更多的功能。

ShipAny 内置了一个控制台布局，位于 components/console/layout.tsx 文件。

实现一个用户中心布局，只需要引入控制台布局组件，传递一个 sidebar 即可。

**Examples:**

Example 1 (python):
```python
import ConsoleLayout from "@/components/console/layout";
import { ReactNode } from "react";
import { Sidebar } from "@/types/blocks/sidebar";
import { getTranslations } from "next-intl/server";
import { getUserInfo } from "@/services/user";
import { redirect } from "next/navigation";
 
export default async function ({ children }: { children: ReactNode }) {
  const userInfo = await getUserInfo();
  if (!userInfo || !userInfo.email) {
    redirect("/auth/signin");
  }
 
  const t = await getTranslations();
 
  const sidebar: Sidebar = {
    nav: {
      items: [
        {
          title: t("use
...
```

Example 2 (python):
```python
import ConsoleLayout from "@/components/console/layout";
import { ReactNode } from "react";
import { Sidebar } from "@/types/blocks/sidebar";
import { getTranslations } from "next-intl/server";
import { getUserInfo } from "@/services/user";
import { redirect } from "next/navigation";
 
export default async function ({ children }: { children: ReactNode }) {
  const userInfo = await getUserInfo();
  if (!userInfo || !userInfo.email) {
    redirect("/auth/signin");
  }
 
  const t = await getTranslations();
 
  const sidebar: Sidebar = {
    nav: {
      items: [
        {
          title: t("use
...
```

---

## FAQ | ShipAny Docs

**URL:** https://docs.shipany.ai/zh/components/faq#faq-type

**Contents:**
- FAQ
- custom FAQ in page
- FAQ Type

**Examples:**

Example 1 (python):
```python
import FAQ from "@/components/blocks/faq";
import { FAQ as FAQType } from "@/types/blocks/faq";
 
export default function Page() {
  // custom FAQ data
  const faq: FAQType = {
    "title": "FAQ",
    "description": "Frequently Asked Questions About ShipAny",
    "items": [
      {
        "question": "What exactly is ShipAny and how does it work?",
        "answer": "ShipAny is a comprehensive NextJS boilerplate designed specifically for building AI SaaS startups. It provides ready-to-use templates, infrastructure setup, and deployment tools that help you launch your AI business in hours inst
...
```

Example 2 (python):
```python
import FAQ from "@/components/blocks/faq";
import { FAQ as FAQType } from "@/types/blocks/faq";
 
export default function Page() {
  // custom FAQ data
  const faq: FAQType = {
    "title": "FAQ",
    "description": "Frequently Asked Questions About ShipAny",
    "items": [
      {
        "question": "What exactly is ShipAny and how does it work?",
        "answer": "ShipAny is a comprehensive NextJS boilerplate designed specifically for building AI SaaS startups. It provides ready-to-use templates, infrastructure setup, and deployment tools that help you launch your AI business in hours inst
...
```

Example 3 (unknown):
```unknown
export interface FAQItem {
  question?: string;
  answer?: string;
}
 
export interface FAQ {
  disabled?: boolean;
  title?: string;
  description?: string;
  items?: FAQItem[];
}
```

Example 4 (unknown):
```unknown
export interface FAQItem {
  question?: string;
  answer?: string;
}
 
export interface FAQ {
  disabled?: boolean;
  title?: string;
  description?: string;
  items?: FAQItem[];
}
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/components/hero#custom-hero-in-page

**Contents:**
- Hero
- custom hero in page
- Hero Type

**Examples:**

Example 1 (python):
```python
import Hero from "@/components/blocks/hero";
import { Hero as HeroType } from "@/types/blocks/hero";
 
export default function Page() {
  // custom hero data
  const hero: HeroType = {
    title: "Ship Any AI Startups in hours, not days",
    highlight_text: "Ship Any",
    description:
      "ShipAny is a NextJS boilerplate for building AI SaaS startups.<br/>Ship Fast with a variety of templates and components.",
    announcement: {
      title: "🎉 Happy New Year",
      url: "/#pricing",
    },
    buttons: [
      {
        title: "Get ShipAny",
        url: "/ai-podcast-generator",
      }
...
```

Example 2 (python):
```python
import Hero from "@/components/blocks/hero";
import { Hero as HeroType } from "@/types/blocks/hero";
 
export default function Page() {
  // custom hero data
  const hero: HeroType = {
    title: "Ship Any AI Startups in hours, not days",
    highlight_text: "Ship Any",
    description:
      "ShipAny is a NextJS boilerplate for building AI SaaS startups.<br/>Ship Fast with a variety of templates and components.",
    announcement: {
      title: "🎉 Happy New Year",
      url: "/#pricing",
    },
    buttons: [
      {
        title: "Get ShipAny",
        url: "/ai-podcast-generator",
      }
...
```

Example 3 (unknown):
```unknown
export interface Hero {
  disabled?: boolean;
  title?: string;
  highlight_text?: string;
  description?: string;
  buttons?: Button[];
  image?: Image;
  announcement?: Announcement;
  show_happy_users?: boolean;
}
```

Example 4 (unknown):
```unknown
export interface Hero {
  disabled?: boolean;
  title?: string;
  highlight_text?: string;
  description?: string;
  buttons?: Button[];
  image?: Image;
  announcement?: Announcement;
  show_happy_users?: boolean;
}
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/user-console/new-table#创建新的表格视图

**Contents:**
- 添加表格视图
- 创建新的表格视图

ShipAny 内置了表格视图组件，可以很方便的渲染一个表格视图，用于展示各类数据。

比如用户列表 / 订单列表 / 积分记录等。

以下步骤演示如何快速在用户中心渲染一个表格视图，显示用户支付订单列表。

getUserUuid 方法可以从 session 中获取当前登录用户的 uuid

预览新页面，可以看到登录后的用户 uuid。

定义要显示的表头列表 columns: TableColumn[]，

引入表格视图组件: import TableSlot from "@/components/console/slots/table";

显示表头：return <TableSlot title={t("my_orders.title")} columns={columns} data={[]} />;

调用步骤 1 实现的读取数据的函数，把获取到的数据传递给表格视图组件进行显示。

**Examples:**

Example 1 (javascript):
```javascript
export async function getOrdersByUserUuid(
  user_uuid: string
): Promise<Order[] | undefined> {
  const now = new Date().toISOString();
  const supabase = getSupabaseClient();
  const { data, error } = await supabase
    .from("orders")
    .select("*")
    .eq("user_uuid", user_uuid)
    .eq("status", "paid")
    .order("created_at", { ascending: false });
 
  if (error) {
    return undefined;
  }
 
  return data;
}
```

Example 2 (javascript):
```javascript
export async function getOrdersByUserUuid(
  user_uuid: string
): Promise<Order[] | undefined> {
  const now = new Date().toISOString();
  const supabase = getSupabaseClient();
  const { data, error } = await supabase
    .from("orders")
    .select("*")
    .eq("user_uuid", user_uuid)
    .eq("status", "paid")
    .order("created_at", { ascending: false });
 
  if (error) {
    return undefined;
  }
 
  return data;
}
```

Example 3 (python):
```python
import { getUserUuid } from "@/services/user";
import { redirect } from "next/navigation";
 
export default async function MyOrdersPage() {
  const user_uuid = await getUserUuid();
 
  const callbackUrl = `${process.env.NEXT_PUBLIC_WEB_URL}/my-orders`;
  if (!user_uuid) {
    redirect(`/auth/signin?callbackUrl=${encodeURIComponent(callbackUrl)}`);
  }
 
  return <div>My Orders With User UUID: {user_uuid}</div>;
}
```

Example 4 (python):
```python
import { getUserUuid } from "@/services/user";
import { redirect } from "next/navigation";
 
export default async function MyOrdersPage() {
  const user_uuid = await getUserUuid();
 
  const callbackUrl = `${process.env.NEXT_PUBLIC_WEB_URL}/my-orders`;
  if (!user_uuid) {
    redirect(`/auth/signin?callbackUrl=${encodeURIComponent(callbackUrl)}`);
  }
 
  return <div>My Orders With User UUID: {user_uuid}</div>;
}
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/user-console/new-table

**Contents:**
- 添加表格视图
- 创建新的表格视图

ShipAny 内置了表格视图组件，可以很方便的渲染一个表格视图，用于展示各类数据。

比如用户列表 / 订单列表 / 积分记录等。

以下步骤演示如何快速在用户中心渲染一个表格视图，显示用户支付订单列表。

getUserUuid 方法可以从 session 中获取当前登录用户的 uuid

预览新页面，可以看到登录后的用户 uuid。

定义要显示的表头列表 columns: TableColumn[]，

引入表格视图组件: import TableSlot from "@/components/console/slots/table";

显示表头：return <TableSlot title={t("my_orders.title")} columns={columns} data={[]} />;

调用步骤 1 实现的读取数据的函数，把获取到的数据传递给表格视图组件进行显示。

**Examples:**

Example 1 (javascript):
```javascript
export async function getOrdersByUserUuid(
  user_uuid: string
): Promise<Order[] | undefined> {
  const now = new Date().toISOString();
  const supabase = getSupabaseClient();
  const { data, error } = await supabase
    .from("orders")
    .select("*")
    .eq("user_uuid", user_uuid)
    .eq("status", "paid")
    .order("created_at", { ascending: false });
 
  if (error) {
    return undefined;
  }
 
  return data;
}
```

Example 2 (javascript):
```javascript
export async function getOrdersByUserUuid(
  user_uuid: string
): Promise<Order[] | undefined> {
  const now = new Date().toISOString();
  const supabase = getSupabaseClient();
  const { data, error } = await supabase
    .from("orders")
    .select("*")
    .eq("user_uuid", user_uuid)
    .eq("status", "paid")
    .order("created_at", { ascending: false });
 
  if (error) {
    return undefined;
  }
 
  return data;
}
```

Example 3 (python):
```python
import { getUserUuid } from "@/services/user";
import { redirect } from "next/navigation";
 
export default async function MyOrdersPage() {
  const user_uuid = await getUserUuid();
 
  const callbackUrl = `${process.env.NEXT_PUBLIC_WEB_URL}/my-orders`;
  if (!user_uuid) {
    redirect(`/auth/signin?callbackUrl=${encodeURIComponent(callbackUrl)}`);
  }
 
  return <div>My Orders With User UUID: {user_uuid}</div>;
}
```

Example 4 (python):
```python
import { getUserUuid } from "@/services/user";
import { redirect } from "next/navigation";
 
export default async function MyOrdersPage() {
  const user_uuid = await getUserUuid();
 
  const callbackUrl = `${process.env.NEXT_PUBLIC_WEB_URL}/my-orders`;
  if (!user_uuid) {
    redirect(`/auth/signin?callbackUrl=${encodeURIComponent(callbackUrl)}`);
  }
 
  return <div>My Orders With User UUID: {user_uuid}</div>;
}
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/admin-system/new-table#渲染数据表格

**Contents:**
- 添加表格视图
- 渲染数据表格

在创建完管理后台布局之后，你可以新建一个 page.tsx 页面，用数据表的形式管理数据。

ShipAny 内置了一个表格视图组件，可以快速渲染一个数据表格，用于各类列表形式的数据展示。

你只需要 import 表格视图组件 @/components/dashboard/slots/table，定义数据表格字段，再传递一份 data 即可。

参考系统内置的后台管理系统， 用户列表页面实现逻辑：

**Examples:**

Example 1 (python):
```python
import { TableColumn } from "@/types/blocks/table";
import TableSlot from "@/components/dashboard/slots/table";
import { Table as TableSlotType } from "@/types/slots/table";
import { getUsers } from "@/models/user";
import moment from "moment";
 
export default async function () {
  const users = await getUsers(1, 50);
 
  const columns: TableColumn[] = [
    { name: "uuid", title: "UUID" },
    { name: "email", title: "Email" },
    { name: "nickname", title: "Name" },
    {
      name: "avatar_url",
      title: "Avatar",
      callback: (row) => (
        <img src={row.avatar_url} className
...
```

Example 2 (python):
```python
import { TableColumn } from "@/types/blocks/table";
import TableSlot from "@/components/dashboard/slots/table";
import { Table as TableSlotType } from "@/types/slots/table";
import { getUsers } from "@/models/user";
import moment from "moment";
 
export default async function () {
  const users = await getUsers(1, 50);
 
  const columns: TableColumn[] = [
    { name: "uuid", title: "UUID" },
    { name: "email", title: "Email" },
    { name: "nickname", title: "Name" },
    {
      name: "avatar_url",
      title: "Avatar",
      callback: (row) => (
        <img src={row.avatar_url} className
...
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/tutorials/new-components#ai-辅助创建新组件

**Contents:**
- 创建新组件
- AI 辅助创建新组件
- 参考

在 components 目录下，创建新的组件文件 new-component/index.tsx。

在 Cursor 中，通过 截图 + 提示词，让 AI 辅助生成新的组件代码。

建议可复用的组件，放在 components/blocks 目录下，业务组件放在 components 目录下。

**Examples:**

Example 1 (unknown):
```unknown
follow this screenshot, create a react function component for me, use shadcn/ui, tailwindcss
```

Example 2 (unknown):
```unknown
follow this screenshot, create a react function component for me, use shadcn/ui, tailwindcss
```

Example 3 (python):
```python
import { LoginForm } from "@/components/new-component";
 
export const runtime = "edge";
 
export default function NewPage() {
  return (
    <div className="container py-36 flex items-center justify-center">
      <LoginForm />
    </div>
  );
}
```

Example 4 (python):
```python
import { LoginForm } from "@/components/new-component";
 
export const runtime = "edge";
 
export default function NewPage() {
  return (
    <div className="container py-36 flex items-center justify-center">
      <LoginForm />
    </div>
  );
}
```

---

## Header | ShipAny Docs

**URL:** https://docs.shipany.ai/zh/components/header#header-type

**Contents:**
- Header
- custom header in page
- Header Type

**Examples:**

Example 1 (python):
```python
import Header from "@/components/blocks/header";
import { Header as HeaderType } from "@/types/blocks/header";
 
export default function Page() {
  // custom header data
  const header: HeaderType = {
    logo: {
      title: "ShipAny",
      image: {
        src: "/logo.png",
        alt: "ShipAny",
      },
    },
    nav: {
      items: [
        {
          title: "Features",
          href: "/features",
        },
        {
          title: "Pricing",
          href: "/pricing",
        },
        {
          title: "Showcases",
          children: [
            {
              title: "Sh
...
```

Example 2 (python):
```python
import Header from "@/components/blocks/header";
import { Header as HeaderType } from "@/types/blocks/header";
 
export default function Page() {
  // custom header data
  const header: HeaderType = {
    logo: {
      title: "ShipAny",
      image: {
        src: "/logo.png",
        alt: "ShipAny",
      },
    },
    nav: {
      items: [
        {
          title: "Features",
          href: "/features",
        },
        {
          title: "Pricing",
          href: "/pricing",
        },
        {
          title: "Showcases",
          children: [
            {
              title: "Sh
...
```

Example 3 (unknown):
```unknown
export interface Header {
  disabled?: boolean;
  logo?: Logo;
  nav?: Nav;
  buttons?: Button[];
  className?: string;
}
```

Example 4 (unknown):
```unknown
export interface Header {
  disabled?: boolean;
  logo?: Logo;
  nav?: Nav;
  buttons?: Button[];
  className?: string;
}
```

---

## FAQ | ShipAny Docs

**URL:** https://docs.shipany.ai/zh/components/faq

**Contents:**
- FAQ
- custom FAQ in page
- FAQ Type

**Examples:**

Example 1 (python):
```python
import FAQ from "@/components/blocks/faq";
import { FAQ as FAQType } from "@/types/blocks/faq";
 
export default function Page() {
  // custom FAQ data
  const faq: FAQType = {
    "title": "FAQ",
    "description": "Frequently Asked Questions About ShipAny",
    "items": [
      {
        "question": "What exactly is ShipAny and how does it work?",
        "answer": "ShipAny is a comprehensive NextJS boilerplate designed specifically for building AI SaaS startups. It provides ready-to-use templates, infrastructure setup, and deployment tools that help you launch your AI business in hours inst
...
```

Example 2 (python):
```python
import FAQ from "@/components/blocks/faq";
import { FAQ as FAQType } from "@/types/blocks/faq";
 
export default function Page() {
  // custom FAQ data
  const faq: FAQType = {
    "title": "FAQ",
    "description": "Frequently Asked Questions About ShipAny",
    "items": [
      {
        "question": "What exactly is ShipAny and how does it work?",
        "answer": "ShipAny is a comprehensive NextJS boilerplate designed specifically for building AI SaaS startups. It provides ready-to-use templates, infrastructure setup, and deployment tools that help you launch your AI business in hours inst
...
```

Example 3 (unknown):
```unknown
export interface FAQItem {
  question?: string;
  answer?: string;
}
 
export interface FAQ {
  disabled?: boolean;
  title?: string;
  description?: string;
  items?: FAQItem[];
}
```

Example 4 (unknown):
```unknown
export interface FAQItem {
  question?: string;
  answer?: string;
}
 
export interface FAQ {
  disabled?: boolean;
  title?: string;
  description?: string;
  items?: FAQItem[];
}
```

---

## CTA | ShipAny Docs

**URL:** https://docs.shipany.ai/zh/components/cta#cta-type

**Contents:**
- CTA (Call to Action)
- custom CTA in page
- CTA Type

**Examples:**

Example 1 (python):
```python
import CTA from "@/components/blocks/cta";
import { CTA as CTAType } from "@/types/blocks/cta";
 
export default function Page() {
  // custom CTA data
  const cta: CTAType =  {
    "title": "Ship your first AI SaaS Startup",
    "description": "Start from here, with ShipAny.",
    "buttons": [
      {
        "title": "Get ShipAny",
        "url": "/#pricing"
      }
    ]
  }
 
  return <>
      <CTA cta={cta} />
      // ...other components
    </>
  );
}
```

Example 2 (python):
```python
import CTA from "@/components/blocks/cta";
import { CTA as CTAType } from "@/types/blocks/cta";
 
export default function Page() {
  // custom CTA data
  const cta: CTAType =  {
    "title": "Ship your first AI SaaS Startup",
    "description": "Start from here, with ShipAny.",
    "buttons": [
      {
        "title": "Get ShipAny",
        "url": "/#pricing"
      }
    ]
  }
 
  return <>
      <CTA cta={cta} />
      // ...other components
    </>
  );
}
```

Example 3 (python):
```python
import { Button } from "@/types/blocks/button";
 
export interface CTA {
  disabled?: boolean;
  title?: string;
  description?: string;
  buttons?: Button[];
}
```

Example 4 (python):
```python
import { Button } from "@/types/blocks/button";
 
export interface CTA {
  disabled?: boolean;
  title?: string;
  description?: string;
  buttons?: Button[];
}
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/guide/faq#如何同步-shipany-最新代码

**Contents:**
- 常见问题
- 如何同步 ShipAny 最新代码
- 本地调试谷歌登录报错

拉取的上游代码可能跟你本地的修改有冲突，需要人工解决冲突。

解决完冲突后，建议本地编译验证一下，确保项目能正常运行，并且无编译报错。

出现这个错误的主要原因，是你本地网络的问题，没法直接请求谷歌的 API。

需要通过配置代理，解决科学上网问题。可以从以下几个方面尝试解决：

**Examples:**

Example 1 (unknown):
```unknown
git checkout -b backup
```

Example 2 (unknown):
```unknown
git checkout -b backup
```

Example 3 (unknown):
```unknown
git checkout main
git remote add upstream [email protected]:shipanyai/shipany-template-one.git
git fetch upstream
git merge upstream/main --allow-unrelated-histories
```

Example 4 (unknown):
```unknown
git checkout main
git remote add upstream [email protected]:shipanyai/shipany-template-one.git
git fetch upstream
git merge upstream/main --allow-unrelated-histories
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/guide/good-to-know#技术依赖

**Contents:**
- 前置说明
- ShipAny 是什么
- ShipAny 框架包含哪些功能
- 技术依赖
- 环境依赖
- AI 辅助编程工具
- AI 编辑器插件

ShipAny 是一个基于 NextJS 的 AI SaaS 开发框架，内置丰富的组件和 AI SDK，帮助你快速完成 AI SaaS 项目开发。

其他需求可以在 Github Issues 提交，按优先级支持。

ShipAny 基于 NextJS 框架构建，用到了诸多流行的技术组件和云服务。

为确保你能充分使用 ShipAny 的完整功能，请自行熟悉以下技术/组件或云服务：

为确保你能顺利在本地运行和二次开发 ShipAny，请在你的电脑上安装必要的环境。

推荐使用以下版本的 NodeJS 和 npm：

其他操作系统，请自行搜索对应的环境配置方法。运行 ShipAny 代码之前，请确保你的电脑环境已经安装了 nodejs 和 pnpm。

为了更好的理解 ShipAny 框架，更高效的开发项目，推荐使用以下 AI 辅助编程工具：

为了更好的格式化代码，更方便的调试接口，推荐在 VS Code / Cursor / Windsurf 等编辑器中安装以下插件：

**Examples:**

Example 1 (unknown):
```unknown
$ node -v
v22.2.0
 
$ npm -v
10.7.0
```

Example 2 (unknown):
```unknown
$ node -v
v22.2.0
 
$ npm -v
10.7.0
```

Example 3 (unknown):
```unknown
$ npm install -g pnpm
```

Example 4 (unknown):
```unknown
$ npm install -g pnpm
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/components/showcase

---

## Header | ShipAny Docs

**URL:** https://docs.shipany.ai/zh/components/header

**Contents:**
- Header
- custom header in page
- Header Type

**Examples:**

Example 1 (python):
```python
import Header from "@/components/blocks/header";
import { Header as HeaderType } from "@/types/blocks/header";
 
export default function Page() {
  // custom header data
  const header: HeaderType = {
    logo: {
      title: "ShipAny",
      image: {
        src: "/logo.png",
        alt: "ShipAny",
      },
    },
    nav: {
      items: [
        {
          title: "Features",
          href: "/features",
        },
        {
          title: "Pricing",
          href: "/pricing",
        },
        {
          title: "Showcases",
          children: [
            {
              title: "Sh
...
```

Example 2 (python):
```python
import Header from "@/components/blocks/header";
import { Header as HeaderType } from "@/types/blocks/header";
 
export default function Page() {
  // custom header data
  const header: HeaderType = {
    logo: {
      title: "ShipAny",
      image: {
        src: "/logo.png",
        alt: "ShipAny",
      },
    },
    nav: {
      items: [
        {
          title: "Features",
          href: "/features",
        },
        {
          title: "Pricing",
          href: "/pricing",
        },
        {
          title: "Showcases",
          children: [
            {
              title: "Sh
...
```

Example 3 (unknown):
```unknown
export interface Header {
  disabled?: boolean;
  logo?: Logo;
  nav?: Nav;
  buttons?: Button[];
  className?: string;
}
```

Example 4 (unknown):
```unknown
export interface Header {
  disabled?: boolean;
  logo?: Logo;
  nav?: Nav;
  buttons?: Button[];
  className?: string;
}
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/guide/course#使用-shipanyai-一小时上线-ai-壁纸生成器

**Contents:**
- 视频课程
- 使用 shipany.ai 一小时上线 AI 壁纸生成器：
  - 第一集：使用 ShipAny 一小时上站
  - 第二集：对接 AI 接口，实现壁纸生成，完成业务功能开发
  - 第三集：对接支付系统，核销用户积分，实现壁纸管理后台

https://www.bilibili.com/video/BV1ooK7eJEag

https://www.bilibili.com/video/BV1v1KnesEbg

https://www.bilibili.com/video/BV1VUKnepEoY

---
