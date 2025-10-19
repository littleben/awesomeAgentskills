# Shipany - Other

**Pages:** 17

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/ai-integrations/text-to-speech

**Contents:**
- 文本转语音

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/admin-system/layout#添加管理后台布局

**Contents:**
- 管理后台布局
- 添加管理后台布局

你可以根据自己的需求，开发自己的管理后台系统。

你可以在任何路径下实现一个新的管理后台布局，只需要 import 内置的 DashboardLayout 组件。传递侧边栏 sidebar 数据即可。

参考系统内置的 admin 系统布局逻辑：

**Examples:**

Example 1 (python):
```python
import DashboardLayout from "@/components/dashboard/layout";
import { ReactNode } from "react";
import { Sidebar } from "@/types/blocks/sidebar";
import { getUserInfo } from "@/services/user";
import { redirect } from "next/navigation";
 
export default async function AdminLayout({
  children,
}: {
  children: ReactNode;
}) {
  const userInfo = await getUserInfo();
  if (!userInfo || !userInfo.email) {
    redirect("/auth/signin");
  }
 
  const adminEmails = process.env.ADMIN_EMAILS?.split(",");
  if (!adminEmails?.includes(userInfo?.email)) {
    return (
      <div className="w-screen h-scr
...
```

Example 2 (python):
```python
import DashboardLayout from "@/components/dashboard/layout";
import { ReactNode } from "react";
import { Sidebar } from "@/types/blocks/sidebar";
import { getUserInfo } from "@/services/user";
import { redirect } from "next/navigation";
 
export default async function AdminLayout({
  children,
}: {
  children: ReactNode;
}) {
  const userInfo = await getUserInfo();
  if (!userInfo || !userInfo.email) {
    redirect("/auth/signin");
  }
 
  const adminEmails = process.env.ADMIN_EMAILS?.split(",");
  if (!adminEmails?.includes(userInfo?.email)) {
    return (
      <div className="w-screen h-scr
...
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/admin-system/layout

**Contents:**
- 管理后台布局
- 添加管理后台布局

你可以根据自己的需求，开发自己的管理后台系统。

你可以在任何路径下实现一个新的管理后台布局，只需要 import 内置的 DashboardLayout 组件。传递侧边栏 sidebar 数据即可。

参考系统内置的 admin 系统布局逻辑：

**Examples:**

Example 1 (python):
```python
import DashboardLayout from "@/components/dashboard/layout";
import { ReactNode } from "react";
import { Sidebar } from "@/types/blocks/sidebar";
import { getUserInfo } from "@/services/user";
import { redirect } from "next/navigation";
 
export default async function AdminLayout({
  children,
}: {
  children: ReactNode;
}) {
  const userInfo = await getUserInfo();
  if (!userInfo || !userInfo.email) {
    redirect("/auth/signin");
  }
 
  const adminEmails = process.env.ADMIN_EMAILS?.split(",");
  if (!adminEmails?.includes(userInfo?.email)) {
    return (
      <div className="w-screen h-scr
...
```

Example 2 (python):
```python
import DashboardLayout from "@/components/dashboard/layout";
import { ReactNode } from "react";
import { Sidebar } from "@/types/blocks/sidebar";
import { getUserInfo } from "@/services/user";
import { redirect } from "next/navigation";
 
export default async function AdminLayout({
  children,
}: {
  children: ReactNode;
}) {
  const userInfo = await getUserInfo();
  if (!userInfo || !userInfo.email) {
    redirect("/auth/signin");
  }
 
  const adminEmails = process.env.ADMIN_EMAILS?.split(",");
  if (!adminEmails?.includes(userInfo?.email)) {
    return (
      <div className="w-screen h-scr
...
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/ai-integrations/video-generation#参考

**Contents:**
- 视频生成
- 使用 Kling AI 的视频模型
- 保存视频到本地文件
- 参考

ShipAny 使用 ai-sdk 作为基础库，结合自定义的 Provider，支持了市面上主流的视频生成模型。

需要先在 Kling AI 充值 Video Generation API，并 创建 API Key。

注意，这里使用的是 ShipAny 自定义 generateVideo 方法，和自定义的 Provider：import { kling } from "@/aisdk/kling";，跟 @ai-sdk 下的 Provider 导入路径有差异。

providerOptions.kling 支持的参数，参考 Kling Text to Video API 文档

kling-v1-6 模型生成 5s 的视频，大概需要 4 分钟。kling-v1 会更久一点。

generateVideo 方法默认同步生成视频，你需要等待视频生成完成，才能断开与服务端的连接。

Your browser does not support the video tag.

通过 generateVideo 生成的视频，是 base64 编码的字符串数组。

你可以参考下面的代码，将视频内容保存到本地文件。

**Examples:**

Example 1 (unknown):
```unknown
KLING_ACCESS_KEY = "xxx"
KLING_SECRET_KEY = "xxx"
```

Example 2 (unknown):
```unknown
KLING_ACCESS_KEY = "xxx"
KLING_SECRET_KEY = "xxx"
```

Example 3 (python):
```python
import { generateVideo } from "@/aisdk";
import { kling } from "@/aisdk/kling";
 
const prompt = "a beautiful girl running with 2 cats";
const model = "kling-v1-6";
 
const videoModel = kling.video(model);
const providerOptions = {
  kling: {
    mode: "std",
    duration: 5,
  },
};
 
const { videos, warnings } = await generateVideo({
  model: videoModel,
  prompt: prompt,
  n: 1,
  providerOptions,
});
```

Example 4 (python):
```python
import { generateVideo } from "@/aisdk";
import { kling } from "@/aisdk/kling";
 
const prompt = "a beautiful girl running with 2 cats";
const model = "kling-v1-6";
 
const videoModel = kling.video(model);
const providerOptions = {
  kling: {
    mode: "std",
    duration: 5,
  },
};
 
const { videos, warnings } = await generateVideo({
  model: videoModel,
  prompt: prompt,
  n: 1,
  providerOptions,
});
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/ai-integrations/video-generation

**Contents:**
- 视频生成
- 使用 Kling AI 的视频模型
- 保存视频到本地文件
- 参考

ShipAny 使用 ai-sdk 作为基础库，结合自定义的 Provider，支持了市面上主流的视频生成模型。

需要先在 Kling AI 充值 Video Generation API，并 创建 API Key。

注意，这里使用的是 ShipAny 自定义 generateVideo 方法，和自定义的 Provider：import { kling } from "@/aisdk/kling";，跟 @ai-sdk 下的 Provider 导入路径有差异。

providerOptions.kling 支持的参数，参考 Kling Text to Video API 文档

kling-v1-6 模型生成 5s 的视频，大概需要 4 分钟。kling-v1 会更久一点。

generateVideo 方法默认同步生成视频，你需要等待视频生成完成，才能断开与服务端的连接。

Your browser does not support the video tag.

通过 generateVideo 生成的视频，是 base64 编码的字符串数组。

你可以参考下面的代码，将视频内容保存到本地文件。

**Examples:**

Example 1 (unknown):
```unknown
KLING_ACCESS_KEY = "xxx"
KLING_SECRET_KEY = "xxx"
```

Example 2 (unknown):
```unknown
KLING_ACCESS_KEY = "xxx"
KLING_SECRET_KEY = "xxx"
```

Example 3 (python):
```python
import { generateVideo } from "@/aisdk";
import { kling } from "@/aisdk/kling";
 
const prompt = "a beautiful girl running with 2 cats";
const model = "kling-v1-6";
 
const videoModel = kling.video(model);
const providerOptions = {
  kling: {
    mode: "std",
    duration: 5,
  },
};
 
const { videos, warnings } = await generateVideo({
  model: videoModel,
  prompt: prompt,
  n: 1,
  providerOptions,
});
```

Example 4 (python):
```python
import { generateVideo } from "@/aisdk";
import { kling } from "@/aisdk/kling";
 
const prompt = "a beautiful girl running with 2 cats";
const model = "kling-v1-6";
 
const videoModel = kling.video(model);
const providerOptions = {
  kling: {
    mode: "std",
    duration: 5,
  },
};
 
const { videos, warnings } = await generateVideo({
  model: videoModel,
  prompt: prompt,
  n: 1,
  providerOptions,
});
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/tutorials/edit-agreement

**Contents:**
- 更新网站协议
- 更新隐私政策
- 更新服务条款
- 修改路由配置

在网站正式上线之前，请根据你网站提供的服务，更新 app/(legal) 目录下的网站协议。

在 Cursor 中，通过提示词生成新的隐私政策内容。

替换 app/(legal)/privacy-policy/page.mdx 文件中的内容，更新隐私政策。

在 Cursor 中，通过提示词生成新的服务条款内容。

替换 app/(legal)/terms-of-service/page.mdx 文件中的内容，更新服务条款。

网站的隐私协议和服务条款，默认放置在 app/(legal) 目录下，不支持多语言。 通过 /privacy-policy 和 /terms-of-service 根路径访问。 如果你希望支持多语言，可以把 app/(legal) 文件下的内容移动到 app/[locale] 目录下。 就能通过 /zh/privacy-policy 和 /zh/terms-of-service 访问对应语言的隐私协议和服务条款。

需要修改 app/middleware.ts 文件的路由配置：

**Examples:**

Example 1 (unknown):
```unknown
update privacy-policy according to landing page content @en.json
with brand name "ShipAny", domain "shipany.ai", contact email is "[email protected]"
```

Example 2 (unknown):
```unknown
update privacy-policy according to landing page content @en.json
with brand name "ShipAny", domain "shipany.ai", contact email is "[email protected]"
```

Example 3 (unknown):
```unknown
update terms-of-service according to landing page content @en.json
with brand name "ShipAny", domain "shipany.ai", contact email is "[email protected]"
```

Example 4 (unknown):
```unknown
update terms-of-service according to landing page content @en.json
with brand name "ShipAny", domain "shipany.ai", contact email is "[email protected]"
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/admin-system/admin

**Contents:**
- 配置管理后台
- 管理员配置

ShipAny 内置了一套后台管理系统，实现基本的数据管理功能。

管理后台默认需要配置管理员邮箱，才有访问权限。

**Examples:**

Example 1 (unknown):
```unknown
ADMIN_EMAILS = "[email protected],[email protected]";
```

Example 2 (unknown):
```unknown
ADMIN_EMAILS = "[email protected],[email protected]";
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/ai-integrations/chat-completions

**Contents:**
- 文本流式生成
- API 调用参考代码
- 参考

ShipAny 支持市面上大部分的 AI 文本模型流式生成内容。

首先参考 文本生成 章节，配置对应的模型。

然后实现一个流式生成 API，用非阻塞的方式返回文本流。

**Examples:**

Example 1 (python):
```python
import { LanguageModelV1, streamText } from "ai";
 
import { createOpenAICompatible } from "@ai-sdk/openai-compatible";
import { createOpenRouter } from "@openrouter/ai-sdk-provider";
import { openai } from "@ai-sdk/openai";
import { respErr } from "@/lib/resp";
 
export async function POST(req: Request) {
  try {
    const { prompt, provider, model } = await req.json();
    if (!prompt || !provider || !model) {
      return respErr("invalid params");
    }
 
    let textModel: LanguageModelV1;
 
    switch (provider) {
      case "openai":
        textModel = openai(model);
        break;
   
...
```

Example 2 (python):
```python
import { LanguageModelV1, streamText } from "ai";
 
import { createOpenAICompatible } from "@ai-sdk/openai-compatible";
import { createOpenRouter } from "@openrouter/ai-sdk-provider";
import { openai } from "@ai-sdk/openai";
import { respErr } from "@/lib/resp";
 
export async function POST(req: Request) {
  try {
    const { prompt, provider, model } = await req.json();
    if (!prompt || !provider || !model) {
      return respErr("invalid params");
    }
 
    let textModel: LanguageModelV1;
 
    switch (provider) {
      case "openai":
        textModel = openai(model);
        break;
   
...
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/tutorials/new-page

**Contents:**
- 创建新页面
- 创建流程
- 参考

在 ShipAny 中创建新页面，跟 NextJS 框架创建新页面的规则一致。

新页面会复用在 app/[locale]/(default)/layout.tsx 文件中定义的布局，默认显示 Header 和 Footer。

如果你希望新页面有不一样的布局，需要创建新的 Layout 文件。具体步骤参考 NextJS Layout 文档

**Examples:**

Example 1 (unknown):
```unknown
export default function NewPage() {
  return (
    <div className="container py-36 flex items-center justify-center">
      New Page
    </div>
  );
}
```

Example 2 (unknown):
```unknown
export default function NewPage() {
  return (
    <div className="container py-36 flex items-center justify-center">
      New Page
    </div>
  );
}
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/user-console/credits

**Contents:**
- 积分管理
- 配置积分管理系统

ShipAny 内置了一套积分管理系统，可以帮助开发者实现用户充值获取积分 / 使用服务扣除积分等逻辑。

并且给到用户一个积分管理页面，可以查看积分余额，积分消费记录。

请确保你已经 配置数据库，复制以下 SQL 语句，创建积分表。

你可以按需修改以下逻辑，给新增用户赠送积分：

修改价格表配置，添加字段，即可实现充值购买积分，并为积分设置了有效期。

你可以按需实现自己的积分扣除逻辑。比如在用户生成一张图片时，扣除 2 个积分，生成一个视频，扣除 3 个积分等。

扣除积分前，先判断用户的积分余额。如果余额不足，则提示用户去充值。

**Examples:**

Example 1 (unknown):
```unknown
CREATE TABLE credits (
    id SERIAL PRIMARY KEY,
    trans_no VARCHAR(255) UNIQUE NOT NULL,
    created_at timestamptz,
    user_uuid VARCHAR(255) NOT NULL,
    trans_type VARCHAR(50) NOT NULL,
    credits INT NOT NULL,
    order_no VARCHAR(255),
    expired_at timestamptz
);
```

Example 2 (unknown):
```unknown
CREATE TABLE credits (
    id SERIAL PRIMARY KEY,
    trans_no VARCHAR(255) UNIQUE NOT NULL,
    created_at timestamptz,
    user_uuid VARCHAR(255) NOT NULL,
    trans_type VARCHAR(50) NOT NULL,
    credits INT NOT NULL,
    order_no VARCHAR(255),
    expired_at timestamptz
);
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/ai-integrations/chat-completions#参考

**Contents:**
- 文本流式生成
- API 调用参考代码
- 参考

ShipAny 支持市面上大部分的 AI 文本模型流式生成内容。

首先参考 文本生成 章节，配置对应的模型。

然后实现一个流式生成 API，用非阻塞的方式返回文本流。

**Examples:**

Example 1 (python):
```python
import { LanguageModelV1, streamText } from "ai";
 
import { createOpenAICompatible } from "@ai-sdk/openai-compatible";
import { createOpenRouter } from "@openrouter/ai-sdk-provider";
import { openai } from "@ai-sdk/openai";
import { respErr } from "@/lib/resp";
 
export async function POST(req: Request) {
  try {
    const { prompt, provider, model } = await req.json();
    if (!prompt || !provider || !model) {
      return respErr("invalid params");
    }
 
    let textModel: LanguageModelV1;
 
    switch (provider) {
      case "openai":
        textModel = openai(model);
        break;
   
...
```

Example 2 (python):
```python
import { LanguageModelV1, streamText } from "ai";
 
import { createOpenAICompatible } from "@ai-sdk/openai-compatible";
import { createOpenRouter } from "@openrouter/ai-sdk-provider";
import { openai } from "@ai-sdk/openai";
import { respErr } from "@/lib/resp";
 
export async function POST(req: Request) {
  try {
    const { prompt, provider, model } = await req.json();
    if (!prompt || !provider || !model) {
      return respErr("invalid params");
    }
 
    let textModel: LanguageModelV1;
 
    switch (provider) {
      case "openai":
        textModel = openai(model);
        break;
   
...
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/tutorials/new-page#创建流程

**Contents:**
- 创建新页面
- 创建流程
- 参考

在 ShipAny 中创建新页面，跟 NextJS 框架创建新页面的规则一致。

新页面会复用在 app/[locale]/(default)/layout.tsx 文件中定义的布局，默认显示 Header 和 Footer。

如果你希望新页面有不一样的布局，需要创建新的 Layout 文件。具体步骤参考 NextJS Layout 文档

**Examples:**

Example 1 (unknown):
```unknown
export default function NewPage() {
  return (
    <div className="container py-36 flex items-center justify-center">
      New Page
    </div>
  );
}
```

Example 2 (unknown):
```unknown
export default function NewPage() {
  return (
    <div className="container py-36 flex items-center justify-center">
      New Page
    </div>
  );
}
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/ai-integrations/video-generation#使用-kling-ai-的视频模型

**Contents:**
- 视频生成
- 使用 Kling AI 的视频模型
- 保存视频到本地文件
- 参考

ShipAny 使用 ai-sdk 作为基础库，结合自定义的 Provider，支持了市面上主流的视频生成模型。

需要先在 Kling AI 充值 Video Generation API，并 创建 API Key。

注意，这里使用的是 ShipAny 自定义 generateVideo 方法，和自定义的 Provider：import { kling } from "@/aisdk/kling";，跟 @ai-sdk 下的 Provider 导入路径有差异。

providerOptions.kling 支持的参数，参考 Kling Text to Video API 文档

kling-v1-6 模型生成 5s 的视频，大概需要 4 分钟。kling-v1 会更久一点。

generateVideo 方法默认同步生成视频，你需要等待视频生成完成，才能断开与服务端的连接。

Your browser does not support the video tag.

通过 generateVideo 生成的视频，是 base64 编码的字符串数组。

你可以参考下面的代码，将视频内容保存到本地文件。

**Examples:**

Example 1 (unknown):
```unknown
KLING_ACCESS_KEY = "xxx"
KLING_SECRET_KEY = "xxx"
```

Example 2 (unknown):
```unknown
KLING_ACCESS_KEY = "xxx"
KLING_SECRET_KEY = "xxx"
```

Example 3 (python):
```python
import { generateVideo } from "@/aisdk";
import { kling } from "@/aisdk/kling";
 
const prompt = "a beautiful girl running with 2 cats";
const model = "kling-v1-6";
 
const videoModel = kling.video(model);
const providerOptions = {
  kling: {
    mode: "std",
    duration: 5,
  },
};
 
const { videos, warnings } = await generateVideo({
  model: videoModel,
  prompt: prompt,
  n: 1,
  providerOptions,
});
```

Example 4 (python):
```python
import { generateVideo } from "@/aisdk";
import { kling } from "@/aisdk/kling";
 
const prompt = "a beautiful girl running with 2 cats";
const model = "kling-v1-6";
 
const videoModel = kling.video(model);
const providerOptions = {
  kling: {
    mode: "std",
    duration: 5,
  },
};
 
const { videos, warnings } = await generateVideo({
  model: videoModel,
  prompt: prompt,
  n: 1,
  providerOptions,
});
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/ai-integrations/video-generation#保存视频到本地文件

**Contents:**
- 视频生成
- 使用 Kling AI 的视频模型
- 保存视频到本地文件
- 参考

ShipAny 使用 ai-sdk 作为基础库，结合自定义的 Provider，支持了市面上主流的视频生成模型。

需要先在 Kling AI 充值 Video Generation API，并 创建 API Key。

注意，这里使用的是 ShipAny 自定义 generateVideo 方法，和自定义的 Provider：import { kling } from "@/aisdk/kling";，跟 @ai-sdk 下的 Provider 导入路径有差异。

providerOptions.kling 支持的参数，参考 Kling Text to Video API 文档

kling-v1-6 模型生成 5s 的视频，大概需要 4 分钟。kling-v1 会更久一点。

generateVideo 方法默认同步生成视频，你需要等待视频生成完成，才能断开与服务端的连接。

Your browser does not support the video tag.

通过 generateVideo 生成的视频，是 base64 编码的字符串数组。

你可以参考下面的代码，将视频内容保存到本地文件。

**Examples:**

Example 1 (unknown):
```unknown
KLING_ACCESS_KEY = "xxx"
KLING_SECRET_KEY = "xxx"
```

Example 2 (unknown):
```unknown
KLING_ACCESS_KEY = "xxx"
KLING_SECRET_KEY = "xxx"
```

Example 3 (python):
```python
import { generateVideo } from "@/aisdk";
import { kling } from "@/aisdk/kling";
 
const prompt = "a beautiful girl running with 2 cats";
const model = "kling-v1-6";
 
const videoModel = kling.video(model);
const providerOptions = {
  kling: {
    mode: "std",
    duration: 5,
  },
};
 
const { videos, warnings } = await generateVideo({
  model: videoModel,
  prompt: prompt,
  n: 1,
  providerOptions,
});
```

Example 4 (python):
```python
import { generateVideo } from "@/aisdk";
import { kling } from "@/aisdk/kling";
 
const prompt = "a beautiful girl running with 2 cats";
const model = "kling-v1-6";
 
const videoModel = kling.video(model);
const providerOptions = {
  kling: {
    mode: "std",
    duration: 5,
  },
};
 
const { videos, warnings } = await generateVideo({
  model: videoModel,
  prompt: prompt,
  n: 1,
  providerOptions,
});
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/tutorials/edit-agreement#更新服务条款

**Contents:**
- 更新网站协议
- 更新隐私政策
- 更新服务条款
- 修改路由配置

在网站正式上线之前，请根据你网站提供的服务，更新 app/(legal) 目录下的网站协议。

在 Cursor 中，通过提示词生成新的隐私政策内容。

替换 app/(legal)/privacy-policy/page.mdx 文件中的内容，更新隐私政策。

在 Cursor 中，通过提示词生成新的服务条款内容。

替换 app/(legal)/terms-of-service/page.mdx 文件中的内容，更新服务条款。

网站的隐私协议和服务条款，默认放置在 app/(legal) 目录下，不支持多语言。 通过 /privacy-policy 和 /terms-of-service 根路径访问。 如果你希望支持多语言，可以把 app/(legal) 文件下的内容移动到 app/[locale] 目录下。 就能通过 /zh/privacy-policy 和 /zh/terms-of-service 访问对应语言的隐私协议和服务条款。

需要修改 app/middleware.ts 文件的路由配置：

**Examples:**

Example 1 (unknown):
```unknown
update privacy-policy according to landing page content @en.json
with brand name "ShipAny", domain "shipany.ai", contact email is "[email protected]"
```

Example 2 (unknown):
```unknown
update privacy-policy according to landing page content @en.json
with brand name "ShipAny", domain "shipany.ai", contact email is "[email protected]"
```

Example 3 (unknown):
```unknown
update terms-of-service according to landing page content @en.json
with brand name "ShipAny", domain "shipany.ai", contact email is "[email protected]"
```

Example 4 (unknown):
```unknown
update terms-of-service according to landing page content @en.json
with brand name "ShipAny", domain "shipany.ai", contact email is "[email protected]"
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/tutorials/edit-agreement#更新隐私政策

**Contents:**
- 更新网站协议
- 更新隐私政策
- 更新服务条款
- 修改路由配置

在网站正式上线之前，请根据你网站提供的服务，更新 app/(legal) 目录下的网站协议。

在 Cursor 中，通过提示词生成新的隐私政策内容。

替换 app/(legal)/privacy-policy/page.mdx 文件中的内容，更新隐私政策。

在 Cursor 中，通过提示词生成新的服务条款内容。

替换 app/(legal)/terms-of-service/page.mdx 文件中的内容，更新服务条款。

网站的隐私协议和服务条款，默认放置在 app/(legal) 目录下，不支持多语言。 通过 /privacy-policy 和 /terms-of-service 根路径访问。 如果你希望支持多语言，可以把 app/(legal) 文件下的内容移动到 app/[locale] 目录下。 就能通过 /zh/privacy-policy 和 /zh/terms-of-service 访问对应语言的隐私协议和服务条款。

需要修改 app/middleware.ts 文件的路由配置：

**Examples:**

Example 1 (unknown):
```unknown
update privacy-policy according to landing page content @en.json
with brand name "ShipAny", domain "shipany.ai", contact email is "[email protected]"
```

Example 2 (unknown):
```unknown
update privacy-policy according to landing page content @en.json
with brand name "ShipAny", domain "shipany.ai", contact email is "[email protected]"
```

Example 3 (unknown):
```unknown
update terms-of-service according to landing page content @en.json
with brand name "ShipAny", domain "shipany.ai", contact email is "[email protected]"
```

Example 4 (unknown):
```unknown
update terms-of-service according to landing page content @en.json
with brand name "ShipAny", domain "shipany.ai", contact email is "[email protected]"
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/tutorials/new-page#参考

**Contents:**
- 创建新页面
- 创建流程
- 参考

在 ShipAny 中创建新页面，跟 NextJS 框架创建新页面的规则一致。

新页面会复用在 app/[locale]/(default)/layout.tsx 文件中定义的布局，默认显示 Header 和 Footer。

如果你希望新页面有不一样的布局，需要创建新的 Layout 文件。具体步骤参考 NextJS Layout 文档

**Examples:**

Example 1 (unknown):
```unknown
export default function NewPage() {
  return (
    <div className="container py-36 flex items-center justify-center">
      New Page
    </div>
  );
}
```

Example 2 (unknown):
```unknown
export default function NewPage() {
  return (
    <div className="container py-36 flex items-center justify-center">
      New Page
    </div>
  );
}
```

---
