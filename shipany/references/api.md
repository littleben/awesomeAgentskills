# Shipany - Api

**Pages:** 18

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/ai-integrations/text-generation

**Contents:**
- 文本生成
- 使用 OpenAI 的模型
- 使用 OpenAI API 兼容的模型
- 使用 OpenRouter 上的聚合模型
- API 调用参考代码
- 参考

ShipAny 支持市面上流行的 AI 文本生成模型。

先在 OpenAI 平台注册账号，生成 API Key

市面上大部分的 AI 文本模型，都兼容 OpenAI API 的接口。只需要更换一下 API 前缀和 API Key，就可以按照 OpenAI 接口约定的参数进行调用。

以 智谱 AI 为例，使用 OpenAI API 兼容的模型生成文本：

先在 OpenRouter 平台注册账号，绑定银行卡购买 credits，生成 API Key

在配置文件设置 OpenRouter 的 API Key

**Examples:**

Example 1 (unknown):
```unknown
OPENAI_API_KEY = "sk-xxx";
```

Example 2 (unknown):
```unknown
OPENAI_API_KEY = "sk-xxx";
```

Example 3 (python):
```python
import { generateText } from "ai";
import { openai } from "@ai-sdk/openai";
 
const prompt = "who are you?";
const model = "gpt-4o";
 
const textModel = openai(model);
 
const { text, warnings } = await generateText({
  model: textModel,
  prompt: prompt,
});
 
if (warnings && warnings.length > 0) {
  throw new Error("gen text failed");
}
 
console.log("gen text ok:", text);
```

Example 4 (python):
```python
import { generateText } from "ai";
import { openai } from "@ai-sdk/openai";
 
const prompt = "who are you?";
const model = "gpt-4o";
 
const textModel = openai(model);
 
const { text, warnings } = await generateText({
  model: textModel,
  prompt: prompt,
});
 
if (warnings && warnings.length > 0) {
  throw new Error("gen text failed");
}
 
console.log("gen text ok:", text);
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/ai-integrations/image-generation#参考

**Contents:**
- 图片生成
- 使用 OpenAI 的图片模型
- 使用 Replicate 上的图片模型
- 使用 Kling AI 的图片模型
- 保存图片到本地文件
- 参考

ShipAny 使用 ai-sdk 作为基础库，结合自定义的 Provider，支持了市面上主流的图片生成模型。

使用 OpenAI 的 dall-e-3 模型生成图片：

需要先在 OpenAI Platform 充值，并创建 API Key。

providerOptions.openai 支持的参数，参考 OpenAI Image Generation 接口文档

需要先在 Replicate 上绑定信用卡，并创建 API Token。

在 Replicate 模型广场 选择一个图片生成模型，复制模型名称。

providerOptions.replicate 支持的参数，参考选择模型的 API 文档

需要先在 Kling AI 充值 Image Generation API，并 创建 API Key。

注意，这里使用的是 ShipAny 自定义的 Provider：import { kling } from "@/aisdk/kling";，跟 @ai-sdk 下的 Provider 导入路径有差异。

providerOptions.kling 支持的参数，参考 Kling Image Generation API 文档

通过 generateImage 生成的图片，是 base64 编码的字符串数组。

你可以参考下面的代码，将图片内容保存到本地文件。

**Examples:**

Example 1 (unknown):
```unknown
OPENAI_BASE_URL = "https://api.openai.com/v1"
OPENAI_API_KEY = "sk-xxx"
```

Example 2 (unknown):
```unknown
OPENAI_BASE_URL = "https://api.openai.com/v1"
OPENAI_API_KEY = "sk-xxx"
```

Example 3 (python):
```python
import { experimental_generateImage as generateImage } from "ai";
import { openai } from "@ai-sdk/openai";
 
const prompt = "a beautiful girl running with 2 cats";
const model = "dall-e-3";
 
const imageModel = openai.image(model);
const providerOptions = {
  openai: {
    quality: "hd",
    style: "natural",
  },
};
 
const { images, warnings } = await generateImage({
  model: imageModel,
  prompt: prompt,
  n: 1,
  providerOptions,
});
```

Example 4 (python):
```python
import { experimental_generateImage as generateImage } from "ai";
import { openai } from "@ai-sdk/openai";
 
const prompt = "a beautiful girl running with 2 cats";
const model = "dall-e-3";
 
const imageModel = openai.image(model);
const providerOptions = {
  openai: {
    quality: "hd",
    style: "natural",
  },
};
 
const { images, warnings } = await generateImage({
  model: imageModel,
  prompt: prompt,
  n: 1,
  providerOptions,
});
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/ai-integrations/chat-completions#api-调用参考代码

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

**URL:** https://docs.shipany.ai/zh/tutorials/api-call#创建-api

**Contents:**
- API 调用
- 创建 API
- 调试 API
- 参考资料

在 ShipAny 中创建新接口，跟 NextJS 框架创建新接口的规则一致。

在 app/api 目录下创建一个接口文件夹，新建 route.ts 文件

**Examples:**

Example 1 (python):
```python
import { respData, respErr } from "@/lib/resp";
 
export async function POST(req: Request) {
  try {
    const { message } = await req.json();
    if (!message) {
      return respErr("invalid params");
    }
 
    return respData({
      pong: `received message: ${message}`,
    });
  } catch (e) {
    console.log("test failed:", e);
    return respErr("test failed");
  }
}
```

Example 2 (python):
```python
import { respData, respErr } from "@/lib/resp";
 
export async function POST(req: Request) {
  try {
    const { message } = await req.json();
    if (!message) {
      return respErr("invalid params");
    }
 
    return respData({
      pong: `received message: ${message}`,
    });
  } catch (e) {
    console.log("test failed:", e);
    return respErr("test failed");
  }
}
```

Example 3 (unknown):
```unknown
curl -X POST -H "Content-Type: application/json" \
    -d '{"message": "hello"}' \
    http://localhost:3000/api/ping
```

Example 4 (unknown):
```unknown
curl -X POST -H "Content-Type: application/json" \
    -d '{"message": "hello"}' \
    http://localhost:3000/api/ping
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/ai-integrations/image-generation

**Contents:**
- 图片生成
- 使用 OpenAI 的图片模型
- 使用 Replicate 上的图片模型
- 使用 Kling AI 的图片模型
- 保存图片到本地文件
- 参考

ShipAny 使用 ai-sdk 作为基础库，结合自定义的 Provider，支持了市面上主流的图片生成模型。

使用 OpenAI 的 dall-e-3 模型生成图片：

需要先在 OpenAI Platform 充值，并创建 API Key。

providerOptions.openai 支持的参数，参考 OpenAI Image Generation 接口文档

需要先在 Replicate 上绑定信用卡，并创建 API Token。

在 Replicate 模型广场 选择一个图片生成模型，复制模型名称。

providerOptions.replicate 支持的参数，参考选择模型的 API 文档

需要先在 Kling AI 充值 Image Generation API，并 创建 API Key。

注意，这里使用的是 ShipAny 自定义的 Provider：import { kling } from "@/aisdk/kling";，跟 @ai-sdk 下的 Provider 导入路径有差异。

providerOptions.kling 支持的参数，参考 Kling Image Generation API 文档

通过 generateImage 生成的图片，是 base64 编码的字符串数组。

你可以参考下面的代码，将图片内容保存到本地文件。

**Examples:**

Example 1 (unknown):
```unknown
OPENAI_BASE_URL = "https://api.openai.com/v1"
OPENAI_API_KEY = "sk-xxx"
```

Example 2 (unknown):
```unknown
OPENAI_BASE_URL = "https://api.openai.com/v1"
OPENAI_API_KEY = "sk-xxx"
```

Example 3 (python):
```python
import { experimental_generateImage as generateImage } from "ai";
import { openai } from "@ai-sdk/openai";
 
const prompt = "a beautiful girl running with 2 cats";
const model = "dall-e-3";
 
const imageModel = openai.image(model);
const providerOptions = {
  openai: {
    quality: "hd",
    style: "natural",
  },
};
 
const { images, warnings } = await generateImage({
  model: imageModel,
  prompt: prompt,
  n: 1,
  providerOptions,
});
```

Example 4 (python):
```python
import { experimental_generateImage as generateImage } from "ai";
import { openai } from "@ai-sdk/openai";
 
const prompt = "a beautiful girl running with 2 cats";
const model = "dall-e-3";
 
const imageModel = openai.image(model);
const providerOptions = {
  openai: {
    quality: "hd",
    style: "natural",
  },
};
 
const { images, warnings } = await generateImage({
  model: imageModel,
  prompt: prompt,
  n: 1,
  providerOptions,
});
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/user-console/api-keys

**Contents:**
- API 密钥管理

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/ai-integrations/image-generation#使用-openai-的图片模型

**Contents:**
- 图片生成
- 使用 OpenAI 的图片模型
- 使用 Replicate 上的图片模型
- 使用 Kling AI 的图片模型
- 保存图片到本地文件
- 参考

ShipAny 使用 ai-sdk 作为基础库，结合自定义的 Provider，支持了市面上主流的图片生成模型。

使用 OpenAI 的 dall-e-3 模型生成图片：

需要先在 OpenAI Platform 充值，并创建 API Key。

providerOptions.openai 支持的参数，参考 OpenAI Image Generation 接口文档

需要先在 Replicate 上绑定信用卡，并创建 API Token。

在 Replicate 模型广场 选择一个图片生成模型，复制模型名称。

providerOptions.replicate 支持的参数，参考选择模型的 API 文档

需要先在 Kling AI 充值 Image Generation API，并 创建 API Key。

注意，这里使用的是 ShipAny 自定义的 Provider：import { kling } from "@/aisdk/kling";，跟 @ai-sdk 下的 Provider 导入路径有差异。

providerOptions.kling 支持的参数，参考 Kling Image Generation API 文档

通过 generateImage 生成的图片，是 base64 编码的字符串数组。

你可以参考下面的代码，将图片内容保存到本地文件。

**Examples:**

Example 1 (unknown):
```unknown
OPENAI_BASE_URL = "https://api.openai.com/v1"
OPENAI_API_KEY = "sk-xxx"
```

Example 2 (unknown):
```unknown
OPENAI_BASE_URL = "https://api.openai.com/v1"
OPENAI_API_KEY = "sk-xxx"
```

Example 3 (python):
```python
import { experimental_generateImage as generateImage } from "ai";
import { openai } from "@ai-sdk/openai";
 
const prompt = "a beautiful girl running with 2 cats";
const model = "dall-e-3";
 
const imageModel = openai.image(model);
const providerOptions = {
  openai: {
    quality: "hd",
    style: "natural",
  },
};
 
const { images, warnings } = await generateImage({
  model: imageModel,
  prompt: prompt,
  n: 1,
  providerOptions,
});
```

Example 4 (python):
```python
import { experimental_generateImage as generateImage } from "ai";
import { openai } from "@ai-sdk/openai";
 
const prompt = "a beautiful girl running with 2 cats";
const model = "dall-e-3";
 
const imageModel = openai.image(model);
const providerOptions = {
  openai: {
    quality: "hd",
    style: "natural",
  },
};
 
const { images, warnings } = await generateImage({
  model: imageModel,
  prompt: prompt,
  n: 1,
  providerOptions,
});
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/ai-integrations/text-generation#api-调用参考代码

**Contents:**
- 文本生成
- 使用 OpenAI 的模型
- 使用 OpenAI API 兼容的模型
- 使用 OpenRouter 上的聚合模型
- API 调用参考代码
- 参考

ShipAny 支持市面上流行的 AI 文本生成模型。

先在 OpenAI 平台注册账号，生成 API Key

市面上大部分的 AI 文本模型，都兼容 OpenAI API 的接口。只需要更换一下 API 前缀和 API Key，就可以按照 OpenAI 接口约定的参数进行调用。

以 智谱 AI 为例，使用 OpenAI API 兼容的模型生成文本：

先在 OpenRouter 平台注册账号，绑定银行卡购买 credits，生成 API Key

在配置文件设置 OpenRouter 的 API Key

**Examples:**

Example 1 (unknown):
```unknown
OPENAI_API_KEY = "sk-xxx";
```

Example 2 (unknown):
```unknown
OPENAI_API_KEY = "sk-xxx";
```

Example 3 (python):
```python
import { generateText } from "ai";
import { openai } from "@ai-sdk/openai";
 
const prompt = "who are you?";
const model = "gpt-4o";
 
const textModel = openai(model);
 
const { text, warnings } = await generateText({
  model: textModel,
  prompt: prompt,
});
 
if (warnings && warnings.length > 0) {
  throw new Error("gen text failed");
}
 
console.log("gen text ok:", text);
```

Example 4 (python):
```python
import { generateText } from "ai";
import { openai } from "@ai-sdk/openai";
 
const prompt = "who are you?";
const model = "gpt-4o";
 
const textModel = openai(model);
 
const { text, warnings } = await generateText({
  model: textModel,
  prompt: prompt,
});
 
if (warnings && warnings.length > 0) {
  throw new Error("gen text failed");
}
 
console.log("gen text ok:", text);
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/tutorials/api-call#调试-api

**Contents:**
- API 调用
- 创建 API
- 调试 API
- 参考资料

在 ShipAny 中创建新接口，跟 NextJS 框架创建新接口的规则一致。

在 app/api 目录下创建一个接口文件夹，新建 route.ts 文件

**Examples:**

Example 1 (python):
```python
import { respData, respErr } from "@/lib/resp";
 
export async function POST(req: Request) {
  try {
    const { message } = await req.json();
    if (!message) {
      return respErr("invalid params");
    }
 
    return respData({
      pong: `received message: ${message}`,
    });
  } catch (e) {
    console.log("test failed:", e);
    return respErr("test failed");
  }
}
```

Example 2 (python):
```python
import { respData, respErr } from "@/lib/resp";
 
export async function POST(req: Request) {
  try {
    const { message } = await req.json();
    if (!message) {
      return respErr("invalid params");
    }
 
    return respData({
      pong: `received message: ${message}`,
    });
  } catch (e) {
    console.log("test failed:", e);
    return respErr("test failed");
  }
}
```

Example 3 (unknown):
```unknown
curl -X POST -H "Content-Type: application/json" \
    -d '{"message": "hello"}' \
    http://localhost:3000/api/ping
```

Example 4 (unknown):
```unknown
curl -X POST -H "Content-Type: application/json" \
    -d '{"message": "hello"}' \
    http://localhost:3000/api/ping
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/ai-integrations/text-generation#使用-openai-api-兼容的模型

**Contents:**
- 文本生成
- 使用 OpenAI 的模型
- 使用 OpenAI API 兼容的模型
- 使用 OpenRouter 上的聚合模型
- API 调用参考代码
- 参考

ShipAny 支持市面上流行的 AI 文本生成模型。

先在 OpenAI 平台注册账号，生成 API Key

市面上大部分的 AI 文本模型，都兼容 OpenAI API 的接口。只需要更换一下 API 前缀和 API Key，就可以按照 OpenAI 接口约定的参数进行调用。

以 智谱 AI 为例，使用 OpenAI API 兼容的模型生成文本：

先在 OpenRouter 平台注册账号，绑定银行卡购买 credits，生成 API Key

在配置文件设置 OpenRouter 的 API Key

**Examples:**

Example 1 (unknown):
```unknown
OPENAI_API_KEY = "sk-xxx";
```

Example 2 (unknown):
```unknown
OPENAI_API_KEY = "sk-xxx";
```

Example 3 (python):
```python
import { generateText } from "ai";
import { openai } from "@ai-sdk/openai";
 
const prompt = "who are you?";
const model = "gpt-4o";
 
const textModel = openai(model);
 
const { text, warnings } = await generateText({
  model: textModel,
  prompt: prompt,
});
 
if (warnings && warnings.length > 0) {
  throw new Error("gen text failed");
}
 
console.log("gen text ok:", text);
```

Example 4 (python):
```python
import { generateText } from "ai";
import { openai } from "@ai-sdk/openai";
 
const prompt = "who are you?";
const model = "gpt-4o";
 
const textModel = openai(model);
 
const { text, warnings } = await generateText({
  model: textModel,
  prompt: prompt,
});
 
if (warnings && warnings.length > 0) {
  throw new Error("gen text failed");
}
 
console.log("gen text ok:", text);
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/ai-integrations/text-generation#使用-openai-的模型

**Contents:**
- 文本生成
- 使用 OpenAI 的模型
- 使用 OpenAI API 兼容的模型
- 使用 OpenRouter 上的聚合模型
- API 调用参考代码
- 参考

ShipAny 支持市面上流行的 AI 文本生成模型。

先在 OpenAI 平台注册账号，生成 API Key

市面上大部分的 AI 文本模型，都兼容 OpenAI API 的接口。只需要更换一下 API 前缀和 API Key，就可以按照 OpenAI 接口约定的参数进行调用。

以 智谱 AI 为例，使用 OpenAI API 兼容的模型生成文本：

先在 OpenRouter 平台注册账号，绑定银行卡购买 credits，生成 API Key

在配置文件设置 OpenRouter 的 API Key

**Examples:**

Example 1 (unknown):
```unknown
OPENAI_API_KEY = "sk-xxx";
```

Example 2 (unknown):
```unknown
OPENAI_API_KEY = "sk-xxx";
```

Example 3 (python):
```python
import { generateText } from "ai";
import { openai } from "@ai-sdk/openai";
 
const prompt = "who are you?";
const model = "gpt-4o";
 
const textModel = openai(model);
 
const { text, warnings } = await generateText({
  model: textModel,
  prompt: prompt,
});
 
if (warnings && warnings.length > 0) {
  throw new Error("gen text failed");
}
 
console.log("gen text ok:", text);
```

Example 4 (python):
```python
import { generateText } from "ai";
import { openai } from "@ai-sdk/openai";
 
const prompt = "who are you?";
const model = "gpt-4o";
 
const textModel = openai(model);
 
const { text, warnings } = await generateText({
  model: textModel,
  prompt: prompt,
});
 
if (warnings && warnings.length > 0) {
  throw new Error("gen text failed");
}
 
console.log("gen text ok:", text);
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/tutorials/api-call#参考资料

**Contents:**
- API 调用
- 创建 API
- 调试 API
- 参考资料

在 ShipAny 中创建新接口，跟 NextJS 框架创建新接口的规则一致。

在 app/api 目录下创建一个接口文件夹，新建 route.ts 文件

**Examples:**

Example 1 (python):
```python
import { respData, respErr } from "@/lib/resp";
 
export async function POST(req: Request) {
  try {
    const { message } = await req.json();
    if (!message) {
      return respErr("invalid params");
    }
 
    return respData({
      pong: `received message: ${message}`,
    });
  } catch (e) {
    console.log("test failed:", e);
    return respErr("test failed");
  }
}
```

Example 2 (python):
```python
import { respData, respErr } from "@/lib/resp";
 
export async function POST(req: Request) {
  try {
    const { message } = await req.json();
    if (!message) {
      return respErr("invalid params");
    }
 
    return respData({
      pong: `received message: ${message}`,
    });
  } catch (e) {
    console.log("test failed:", e);
    return respErr("test failed");
  }
}
```

Example 3 (unknown):
```unknown
curl -X POST -H "Content-Type: application/json" \
    -d '{"message": "hello"}' \
    http://localhost:3000/api/ping
```

Example 4 (unknown):
```unknown
curl -X POST -H "Content-Type: application/json" \
    -d '{"message": "hello"}' \
    http://localhost:3000/api/ping
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/ai-integrations/image-generation#保存图片到本地文件

**Contents:**
- 图片生成
- 使用 OpenAI 的图片模型
- 使用 Replicate 上的图片模型
- 使用 Kling AI 的图片模型
- 保存图片到本地文件
- 参考

ShipAny 使用 ai-sdk 作为基础库，结合自定义的 Provider，支持了市面上主流的图片生成模型。

使用 OpenAI 的 dall-e-3 模型生成图片：

需要先在 OpenAI Platform 充值，并创建 API Key。

providerOptions.openai 支持的参数，参考 OpenAI Image Generation 接口文档

需要先在 Replicate 上绑定信用卡，并创建 API Token。

在 Replicate 模型广场 选择一个图片生成模型，复制模型名称。

providerOptions.replicate 支持的参数，参考选择模型的 API 文档

需要先在 Kling AI 充值 Image Generation API，并 创建 API Key。

注意，这里使用的是 ShipAny 自定义的 Provider：import { kling } from "@/aisdk/kling";，跟 @ai-sdk 下的 Provider 导入路径有差异。

providerOptions.kling 支持的参数，参考 Kling Image Generation API 文档

通过 generateImage 生成的图片，是 base64 编码的字符串数组。

你可以参考下面的代码，将图片内容保存到本地文件。

**Examples:**

Example 1 (unknown):
```unknown
OPENAI_BASE_URL = "https://api.openai.com/v1"
OPENAI_API_KEY = "sk-xxx"
```

Example 2 (unknown):
```unknown
OPENAI_BASE_URL = "https://api.openai.com/v1"
OPENAI_API_KEY = "sk-xxx"
```

Example 3 (python):
```python
import { experimental_generateImage as generateImage } from "ai";
import { openai } from "@ai-sdk/openai";
 
const prompt = "a beautiful girl running with 2 cats";
const model = "dall-e-3";
 
const imageModel = openai.image(model);
const providerOptions = {
  openai: {
    quality: "hd",
    style: "natural",
  },
};
 
const { images, warnings } = await generateImage({
  model: imageModel,
  prompt: prompt,
  n: 1,
  providerOptions,
});
```

Example 4 (python):
```python
import { experimental_generateImage as generateImage } from "ai";
import { openai } from "@ai-sdk/openai";
 
const prompt = "a beautiful girl running with 2 cats";
const model = "dall-e-3";
 
const imageModel = openai.image(model);
const providerOptions = {
  openai: {
    quality: "hd",
    style: "natural",
  },
};
 
const { images, warnings } = await generateImage({
  model: imageModel,
  prompt: prompt,
  n: 1,
  providerOptions,
});
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/ai-integrations/text-generation#使用-openrouter-上的聚合模型

**Contents:**
- 文本生成
- 使用 OpenAI 的模型
- 使用 OpenAI API 兼容的模型
- 使用 OpenRouter 上的聚合模型
- API 调用参考代码
- 参考

ShipAny 支持市面上流行的 AI 文本生成模型。

先在 OpenAI 平台注册账号，生成 API Key

市面上大部分的 AI 文本模型，都兼容 OpenAI API 的接口。只需要更换一下 API 前缀和 API Key，就可以按照 OpenAI 接口约定的参数进行调用。

以 智谱 AI 为例，使用 OpenAI API 兼容的模型生成文本：

先在 OpenRouter 平台注册账号，绑定银行卡购买 credits，生成 API Key

在配置文件设置 OpenRouter 的 API Key

**Examples:**

Example 1 (unknown):
```unknown
OPENAI_API_KEY = "sk-xxx";
```

Example 2 (unknown):
```unknown
OPENAI_API_KEY = "sk-xxx";
```

Example 3 (python):
```python
import { generateText } from "ai";
import { openai } from "@ai-sdk/openai";
 
const prompt = "who are you?";
const model = "gpt-4o";
 
const textModel = openai(model);
 
const { text, warnings } = await generateText({
  model: textModel,
  prompt: prompt,
});
 
if (warnings && warnings.length > 0) {
  throw new Error("gen text failed");
}
 
console.log("gen text ok:", text);
```

Example 4 (python):
```python
import { generateText } from "ai";
import { openai } from "@ai-sdk/openai";
 
const prompt = "who are you?";
const model = "gpt-4o";
 
const textModel = openai(model);
 
const { text, warnings } = await generateText({
  model: textModel,
  prompt: prompt,
});
 
if (warnings && warnings.length > 0) {
  throw new Error("gen text failed");
}
 
console.log("gen text ok:", text);
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/ai-integrations/image-generation#使用-kling-ai-的图片模型

**Contents:**
- 图片生成
- 使用 OpenAI 的图片模型
- 使用 Replicate 上的图片模型
- 使用 Kling AI 的图片模型
- 保存图片到本地文件
- 参考

ShipAny 使用 ai-sdk 作为基础库，结合自定义的 Provider，支持了市面上主流的图片生成模型。

使用 OpenAI 的 dall-e-3 模型生成图片：

需要先在 OpenAI Platform 充值，并创建 API Key。

providerOptions.openai 支持的参数，参考 OpenAI Image Generation 接口文档

需要先在 Replicate 上绑定信用卡，并创建 API Token。

在 Replicate 模型广场 选择一个图片生成模型，复制模型名称。

providerOptions.replicate 支持的参数，参考选择模型的 API 文档

需要先在 Kling AI 充值 Image Generation API，并 创建 API Key。

注意，这里使用的是 ShipAny 自定义的 Provider：import { kling } from "@/aisdk/kling";，跟 @ai-sdk 下的 Provider 导入路径有差异。

providerOptions.kling 支持的参数，参考 Kling Image Generation API 文档

通过 generateImage 生成的图片，是 base64 编码的字符串数组。

你可以参考下面的代码，将图片内容保存到本地文件。

**Examples:**

Example 1 (unknown):
```unknown
OPENAI_BASE_URL = "https://api.openai.com/v1"
OPENAI_API_KEY = "sk-xxx"
```

Example 2 (unknown):
```unknown
OPENAI_BASE_URL = "https://api.openai.com/v1"
OPENAI_API_KEY = "sk-xxx"
```

Example 3 (python):
```python
import { experimental_generateImage as generateImage } from "ai";
import { openai } from "@ai-sdk/openai";
 
const prompt = "a beautiful girl running with 2 cats";
const model = "dall-e-3";
 
const imageModel = openai.image(model);
const providerOptions = {
  openai: {
    quality: "hd",
    style: "natural",
  },
};
 
const { images, warnings } = await generateImage({
  model: imageModel,
  prompt: prompt,
  n: 1,
  providerOptions,
});
```

Example 4 (python):
```python
import { experimental_generateImage as generateImage } from "ai";
import { openai } from "@ai-sdk/openai";
 
const prompt = "a beautiful girl running with 2 cats";
const model = "dall-e-3";
 
const imageModel = openai.image(model);
const providerOptions = {
  openai: {
    quality: "hd",
    style: "natural",
  },
};
 
const { images, warnings } = await generateImage({
  model: imageModel,
  prompt: prompt,
  n: 1,
  providerOptions,
});
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/ai-integrations/text-generation#参考

**Contents:**
- 文本生成
- 使用 OpenAI 的模型
- 使用 OpenAI API 兼容的模型
- 使用 OpenRouter 上的聚合模型
- API 调用参考代码
- 参考

ShipAny 支持市面上流行的 AI 文本生成模型。

先在 OpenAI 平台注册账号，生成 API Key

市面上大部分的 AI 文本模型，都兼容 OpenAI API 的接口。只需要更换一下 API 前缀和 API Key，就可以按照 OpenAI 接口约定的参数进行调用。

以 智谱 AI 为例，使用 OpenAI API 兼容的模型生成文本：

先在 OpenRouter 平台注册账号，绑定银行卡购买 credits，生成 API Key

在配置文件设置 OpenRouter 的 API Key

**Examples:**

Example 1 (unknown):
```unknown
OPENAI_API_KEY = "sk-xxx";
```

Example 2 (unknown):
```unknown
OPENAI_API_KEY = "sk-xxx";
```

Example 3 (python):
```python
import { generateText } from "ai";
import { openai } from "@ai-sdk/openai";
 
const prompt = "who are you?";
const model = "gpt-4o";
 
const textModel = openai(model);
 
const { text, warnings } = await generateText({
  model: textModel,
  prompt: prompt,
});
 
if (warnings && warnings.length > 0) {
  throw new Error("gen text failed");
}
 
console.log("gen text ok:", text);
```

Example 4 (python):
```python
import { generateText } from "ai";
import { openai } from "@ai-sdk/openai";
 
const prompt = "who are you?";
const model = "gpt-4o";
 
const textModel = openai(model);
 
const { text, warnings } = await generateText({
  model: textModel,
  prompt: prompt,
});
 
if (warnings && warnings.length > 0) {
  throw new Error("gen text failed");
}
 
console.log("gen text ok:", text);
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/ai-integrations/image-generation#使用-replicate-上的图片模型

**Contents:**
- 图片生成
- 使用 OpenAI 的图片模型
- 使用 Replicate 上的图片模型
- 使用 Kling AI 的图片模型
- 保存图片到本地文件
- 参考

ShipAny 使用 ai-sdk 作为基础库，结合自定义的 Provider，支持了市面上主流的图片生成模型。

使用 OpenAI 的 dall-e-3 模型生成图片：

需要先在 OpenAI Platform 充值，并创建 API Key。

providerOptions.openai 支持的参数，参考 OpenAI Image Generation 接口文档

需要先在 Replicate 上绑定信用卡，并创建 API Token。

在 Replicate 模型广场 选择一个图片生成模型，复制模型名称。

providerOptions.replicate 支持的参数，参考选择模型的 API 文档

需要先在 Kling AI 充值 Image Generation API，并 创建 API Key。

注意，这里使用的是 ShipAny 自定义的 Provider：import { kling } from "@/aisdk/kling";，跟 @ai-sdk 下的 Provider 导入路径有差异。

providerOptions.kling 支持的参数，参考 Kling Image Generation API 文档

通过 generateImage 生成的图片，是 base64 编码的字符串数组。

你可以参考下面的代码，将图片内容保存到本地文件。

**Examples:**

Example 1 (unknown):
```unknown
OPENAI_BASE_URL = "https://api.openai.com/v1"
OPENAI_API_KEY = "sk-xxx"
```

Example 2 (unknown):
```unknown
OPENAI_BASE_URL = "https://api.openai.com/v1"
OPENAI_API_KEY = "sk-xxx"
```

Example 3 (python):
```python
import { experimental_generateImage as generateImage } from "ai";
import { openai } from "@ai-sdk/openai";
 
const prompt = "a beautiful girl running with 2 cats";
const model = "dall-e-3";
 
const imageModel = openai.image(model);
const providerOptions = {
  openai: {
    quality: "hd",
    style: "natural",
  },
};
 
const { images, warnings } = await generateImage({
  model: imageModel,
  prompt: prompt,
  n: 1,
  providerOptions,
});
```

Example 4 (python):
```python
import { experimental_generateImage as generateImage } from "ai";
import { openai } from "@ai-sdk/openai";
 
const prompt = "a beautiful girl running with 2 cats";
const model = "dall-e-3";
 
const imageModel = openai.image(model);
const providerOptions = {
  openai: {
    quality: "hd",
    style: "natural",
  },
};
 
const { images, warnings } = await generateImage({
  model: imageModel,
  prompt: prompt,
  n: 1,
  providerOptions,
});
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/tutorials/api-call

**Contents:**
- API 调用
- 创建 API
- 调试 API
- 参考资料

在 ShipAny 中创建新接口，跟 NextJS 框架创建新接口的规则一致。

在 app/api 目录下创建一个接口文件夹，新建 route.ts 文件

**Examples:**

Example 1 (python):
```python
import { respData, respErr } from "@/lib/resp";
 
export async function POST(req: Request) {
  try {
    const { message } = await req.json();
    if (!message) {
      return respErr("invalid params");
    }
 
    return respData({
      pong: `received message: ${message}`,
    });
  } catch (e) {
    console.log("test failed:", e);
    return respErr("test failed");
  }
}
```

Example 2 (python):
```python
import { respData, respErr } from "@/lib/resp";
 
export async function POST(req: Request) {
  try {
    const { message } = await req.json();
    if (!message) {
      return respErr("invalid params");
    }
 
    return respData({
      pong: `received message: ${message}`,
    });
  } catch (e) {
    console.log("test failed:", e);
    return respErr("test failed");
  }
}
```

Example 3 (unknown):
```unknown
curl -X POST -H "Content-Type: application/json" \
    -d '{"message": "hello"}' \
    http://localhost:3000/api/ping
```

Example 4 (unknown):
```unknown
curl -X POST -H "Content-Type: application/json" \
    -d '{"message": "hello"}' \
    http://localhost:3000/api/ping
```

---
