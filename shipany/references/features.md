# Shipany - Features

**Pages:** 84

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/features/email/resend#发送邮件

**Contents:**
- Resend
- Resend 设置
- ShipAny 配置
- 发送邮件
  - 发送文本邮件
  - 发送 HTML 邮件
  - 发送模板邮件
  - 使用 React Email
- 参考

ShipAny 支持使用 Resend 发送邮件，可用于发送邮件验证码、发送支付通知、发送营销邮件等场景。

在 Resend 后台 添加域名，设置 DNS 记录，验证域名

在 Resend 后台 创建 API 密钥，并复制 API 密钥

在 ShipAny 项目配置文件中，填写 Resend 相关的配置信息。

比如在 Resend 后台配置的邮件域名是 mail.shipany.ai，则发件人邮箱可以配置为 [email protected] / [email protected] / [email protected] 等。

在需要发邮件的地方，根据具体场景，选择合适的发送方式。

React Email 内置大量邮件组件，可以让你更轻松创建邮件模板。

比如在 @/components/email-templates/react-email.tsx 中写入内容：

除了自己实现邮件模板，你也可以在 React Email 模板市场 选择一个模板，修改后直接使用。

**Examples:**

Example 1 (unknown):
```unknown
RESEND_API_KEY = "re_xxx"
RESEND_SENDER_EMAIL = "[email protected]"
```

Example 2 (unknown):
```unknown
RESEND_API_KEY = "re_xxx"
RESEND_SENDER_EMAIL = "[email protected]"
```

Example 3 (python):
```python
import { Resend } from "resend";
 
const resend = new Resend(process.env.RESEND_API_KEY!);
 
const result = await resend.emails.send({
  from: process.env.RESEND_SENDER_EMAIL!,
  to: ["[email protected]"],
  subject: "Hello from ShipAny with Resend",
  text: "Hello World.",
});
 
console.log("send email result", result);
```

Example 4 (python):
```python
import { Resend } from "resend";
 
const resend = new Resend(process.env.RESEND_API_KEY!);
 
const result = await resend.emails.send({
  from: process.env.RESEND_SENDER_EMAIL!,
  to: ["[email protected]"],
  subject: "Hello from ShipAny with Resend",
  text: "Hello World.",
});
 
console.log("send email result", result);
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/features/payment/creem

**Contents:**
- Creem
- Creem 设置
- ShipAny 配置
- 价格表支付
  - 配置价格表内容
  - 修改价格表组件
  - 修改价格表下单逻辑
  - 修改支付回调逻辑
  - 修改支付通知逻辑
- 本地测试

ShipAny 支持使用 Creem 进行支付，可用于产品付款、会员订阅、购买积分等场景。

在 ShipAny 项目配置文件中，填写 Creem 相关的配置信息。

页面路径可以填相对路径，也可以填绝对路径。如果填的是相对路径，跳转时会自动拼接 NEXT_PUBLIC_WEB_URL 配置的网站地址，并带上多语言参数。

比如按照以上配置，在中文页面支付成功后的跳转路径是：http://localhost:3000/zh/my-orders

比如在 ShipAny 项目中设置的价格表有三个支付方案，对应的 product_id 分别是 starter、standard、premium，你需要在 Creem 后台为这三个方案 创建对应的产品，复制每个产品的 Product ID，与价格表中的 product_id 对应关系填写到 CREEM_PRODUCTS 中。

ShipAny 模板内置了一个价格表和对应的支付逻辑，你可以根据自己的需求，简单修改即可快速实现支付功能。

ShipAny 模板内置的价格表配置文件位于：src/i18n/pages/pricing 目录下，支持多语言，默认包含 en.json 和 zh.json 两个价格表配置文件。

你可以根据自己的需求，修改价格表配置文件中的内容。

默认的价格表组件位于：src/components/blocks/pricing/index.tsx

你可以根据自己的需求，修改价格表的展示形式。

默认的价格表下单逻辑位于：src/app/api/checkout/route.ts

你可以根据自己的需求，修改价格表的下单逻辑。

在价格表下单逻辑中，默认配置的支付回调地址是：/api/pay/callback/creem

用户支付后，会在浏览器跳转到这个地址，并带上包含支付信息的参数。

默认的支付回调处理逻辑位于：src/app/api/pay/callback/creem/route.ts

你可以根据自己的需求，修改处理支付回调的逻辑，比如更新订单状态、给用户发送邮件通知、给用户赠送积分等。

支付回调是同步逻辑，依赖浏览器跳转到回调地址，才能处理支付结果。这种方式不太可靠，可能出现跳转过程中用户关闭了浏览器等情况，导致支付结果没有被正常处理。 更可靠的方式是通过 Webhook，配置支付结果异步通知。

比如把 Webhook 地址配置为：https://your-domain.com/api/pay/notify/creem

用户支付后，Creem 会把支付信息推送到这个地址。

默认的支付通知逻辑位于：src/app/api/pay/notify/creem/route.ts

你可以根据自己的需求，修改处理支付通知的逻辑，比如更新订单状态、给用户发送邮件通知、给用户赠送积分等。

在 Creem 后台进入店铺，点击右上角的 Test mode，开启测试模式。

在测试模式下，进入开发者中心，设置 测试 API 密钥。

注册 ngrok 账号，按指示安装 ngrok 命令行工具。

启动 ngrok 服务，监听本地端口，并生成一个临时的域名。

在 Creem 后台测试模式中，配置 Webhook 地址为 ngrok 生成的域名

Endpoint 填写支付通知地址，比如 https://xxx.ngrok-free.app/api/pay/notify/creem。

添加 Webhook 地址后，在 Webhook 管理页面，复制 Signing secret，

跟支付密钥一起填入 .env.development 文件中。

在本地启动项目，访问 /pricing 页面，点击下单按钮，下单成功后跳转到支付页面。

使用 Stripe 测试卡 支付，支付成功后浏览器跳转到支付回调地址，监听的地址收到支付通知。

**Examples:**

Example 1 (unknown):
```unknown
NEXT_PUBLIC_WEB_URL = "http://localhost:3000"

NEXT_PUBLIC_PAY_SUCCESS_URL = "/my-orders"
NEXT_PUBLIC_PAY_FAIL_URL = "/pricing"
NEXT_PUBLIC_PAY_CANCEL_URL = "/pricing"

PAY_PROVIDER = "creem"

CREEM_ENV = "test"
CREEM_API_KEY = "creem_test_xxx"
CREEM_WEBHOOK_SECRET = "whsec_xxx"
CREEM_PRODUCTS = '{"starter": "prod_xxx", "standard": "prod_xxx", "premium": "prod_xxx"}'
```

Example 2 (unknown):
```unknown
NEXT_PUBLIC_WEB_URL = "http://localhost:3000"

NEXT_PUBLIC_PAY_SUCCESS_URL = "/my-orders"
NEXT_PUBLIC_PAY_FAIL_URL = "/pricing"
NEXT_PUBLIC_PAY_CANCEL_URL = "/pricing"

PAY_PROVIDER = "creem"

CREEM_ENV = "test"
CREEM_API_KEY = "creem_test_xxx"
CREEM_WEBHOOK_SECRET = "whsec_xxx"
CREEM_PRODUCTS = '{"starter": "prod_xxx", "standard": "prod_xxx", "premium": "prod_xxx"}'
```

Example 3 (unknown):
```unknown
{
  "pricing": {
    "name": "pricing",
    "label": "Pricing",
    "title": "Pricing",
    "description": "Get all features of ShipAny, Ship your AI SaaS startups fast.",
    "groups": [],
    "items": [
      {
        "title": "Starter",
        "description": "Get started with your first SaaS startup.",
        "features_title": "Includes",
        "features": [
          "100 credits, valid for 1 month",
          "NextJS boilerplate",
          "SEO-friendly structure",
          "Payment with Stripe",
          "Data storage with Supabase",
          "Google Oauth & One-Tap Login",
    
...
```

Example 4 (unknown):
```unknown
{
  "pricing": {
    "name": "pricing",
    "label": "Pricing",
    "title": "Pricing",
    "description": "Get all features of ShipAny, Ship your AI SaaS startups fast.",
    "groups": [],
    "items": [
      {
        "title": "Starter",
        "description": "Get started with your first SaaS startup.",
        "features_title": "Includes",
        "features": [
          "100 credits, valid for 1 month",
          "NextJS boilerplate",
          "SEO-friendly structure",
          "Payment with Stripe",
          "Data storage with Supabase",
          "Google Oauth & One-Tap Login",
    
...
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/features/payment/creem#本地测试

**Contents:**
- Creem
- Creem 设置
- ShipAny 配置
- 价格表支付
  - 配置价格表内容
  - 修改价格表组件
  - 修改价格表下单逻辑
  - 修改支付回调逻辑
  - 修改支付通知逻辑
- 本地测试

ShipAny 支持使用 Creem 进行支付，可用于产品付款、会员订阅、购买积分等场景。

在 ShipAny 项目配置文件中，填写 Creem 相关的配置信息。

页面路径可以填相对路径，也可以填绝对路径。如果填的是相对路径，跳转时会自动拼接 NEXT_PUBLIC_WEB_URL 配置的网站地址，并带上多语言参数。

比如按照以上配置，在中文页面支付成功后的跳转路径是：http://localhost:3000/zh/my-orders

比如在 ShipAny 项目中设置的价格表有三个支付方案，对应的 product_id 分别是 starter、standard、premium，你需要在 Creem 后台为这三个方案 创建对应的产品，复制每个产品的 Product ID，与价格表中的 product_id 对应关系填写到 CREEM_PRODUCTS 中。

ShipAny 模板内置了一个价格表和对应的支付逻辑，你可以根据自己的需求，简单修改即可快速实现支付功能。

ShipAny 模板内置的价格表配置文件位于：src/i18n/pages/pricing 目录下，支持多语言，默认包含 en.json 和 zh.json 两个价格表配置文件。

你可以根据自己的需求，修改价格表配置文件中的内容。

默认的价格表组件位于：src/components/blocks/pricing/index.tsx

你可以根据自己的需求，修改价格表的展示形式。

默认的价格表下单逻辑位于：src/app/api/checkout/route.ts

你可以根据自己的需求，修改价格表的下单逻辑。

在价格表下单逻辑中，默认配置的支付回调地址是：/api/pay/callback/creem

用户支付后，会在浏览器跳转到这个地址，并带上包含支付信息的参数。

默认的支付回调处理逻辑位于：src/app/api/pay/callback/creem/route.ts

你可以根据自己的需求，修改处理支付回调的逻辑，比如更新订单状态、给用户发送邮件通知、给用户赠送积分等。

支付回调是同步逻辑，依赖浏览器跳转到回调地址，才能处理支付结果。这种方式不太可靠，可能出现跳转过程中用户关闭了浏览器等情况，导致支付结果没有被正常处理。 更可靠的方式是通过 Webhook，配置支付结果异步通知。

比如把 Webhook 地址配置为：https://your-domain.com/api/pay/notify/creem

用户支付后，Creem 会把支付信息推送到这个地址。

默认的支付通知逻辑位于：src/app/api/pay/notify/creem/route.ts

你可以根据自己的需求，修改处理支付通知的逻辑，比如更新订单状态、给用户发送邮件通知、给用户赠送积分等。

在 Creem 后台进入店铺，点击右上角的 Test mode，开启测试模式。

在测试模式下，进入开发者中心，设置 测试 API 密钥。

注册 ngrok 账号，按指示安装 ngrok 命令行工具。

启动 ngrok 服务，监听本地端口，并生成一个临时的域名。

在 Creem 后台测试模式中，配置 Webhook 地址为 ngrok 生成的域名

Endpoint 填写支付通知地址，比如 https://xxx.ngrok-free.app/api/pay/notify/creem。

添加 Webhook 地址后，在 Webhook 管理页面，复制 Signing secret，

跟支付密钥一起填入 .env.development 文件中。

在本地启动项目，访问 /pricing 页面，点击下单按钮，下单成功后跳转到支付页面。

使用 Stripe 测试卡 支付，支付成功后浏览器跳转到支付回调地址，监听的地址收到支付通知。

**Examples:**

Example 1 (unknown):
```unknown
NEXT_PUBLIC_WEB_URL = "http://localhost:3000"

NEXT_PUBLIC_PAY_SUCCESS_URL = "/my-orders"
NEXT_PUBLIC_PAY_FAIL_URL = "/pricing"
NEXT_PUBLIC_PAY_CANCEL_URL = "/pricing"

PAY_PROVIDER = "creem"

CREEM_ENV = "test"
CREEM_API_KEY = "creem_test_xxx"
CREEM_WEBHOOK_SECRET = "whsec_xxx"
CREEM_PRODUCTS = '{"starter": "prod_xxx", "standard": "prod_xxx", "premium": "prod_xxx"}'
```

Example 2 (unknown):
```unknown
NEXT_PUBLIC_WEB_URL = "http://localhost:3000"

NEXT_PUBLIC_PAY_SUCCESS_URL = "/my-orders"
NEXT_PUBLIC_PAY_FAIL_URL = "/pricing"
NEXT_PUBLIC_PAY_CANCEL_URL = "/pricing"

PAY_PROVIDER = "creem"

CREEM_ENV = "test"
CREEM_API_KEY = "creem_test_xxx"
CREEM_WEBHOOK_SECRET = "whsec_xxx"
CREEM_PRODUCTS = '{"starter": "prod_xxx", "standard": "prod_xxx", "premium": "prod_xxx"}'
```

Example 3 (unknown):
```unknown
{
  "pricing": {
    "name": "pricing",
    "label": "Pricing",
    "title": "Pricing",
    "description": "Get all features of ShipAny, Ship your AI SaaS startups fast.",
    "groups": [],
    "items": [
      {
        "title": "Starter",
        "description": "Get started with your first SaaS startup.",
        "features_title": "Includes",
        "features": [
          "100 credits, valid for 1 month",
          "NextJS boilerplate",
          "SEO-friendly structure",
          "Payment with Stripe",
          "Data storage with Supabase",
          "Google Oauth & One-Tap Login",
    
...
```

Example 4 (unknown):
```unknown
{
  "pricing": {
    "name": "pricing",
    "label": "Pricing",
    "title": "Pricing",
    "description": "Get all features of ShipAny, Ship your AI SaaS startups fast.",
    "groups": [],
    "items": [
      {
        "title": "Starter",
        "description": "Get started with your first SaaS startup.",
        "features_title": "Includes",
        "features": [
          "100 credits, valid for 1 month",
          "NextJS boilerplate",
          "SEO-friendly structure",
          "Payment with Stripe",
          "Data storage with Supabase",
          "Google Oauth & One-Tap Login",
    
...
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/features/database#初始化数据库

**Contents:**
- 数据库
- 配置数据库
- 初始化数据库
- 更新数据库
- 管理数据库
- 操作数据库
- 使用其他类型数据库
- 参考

ShipAny 使用 drizzle-orm 支持多种类型数据库。

以 Supabase 数据库为例，在 ShipAny 配置数据库的流程为：

登录 Supabase 控制台，创建数据库

在 Supabase 控制台，进入你创建的数据库，点击上方的 Connect

在弹出来的框中复制数据库连接信息，类似这样的字符串：

[YOUR-PASSWORD] 需要替换成你在创建数据库时设置的密码。

修改项目配置文件：.env.development 和 .env.production

在配置好 DATABASE_URL 后，在项目根目录下运行以下命令，初始化数据库：

这个命令会执行 src/db/migrations 目录下的所有迁移文件，创建数据库表。

如果你通过 DATABASE_URL 配置的不是一个新创建的数据库，或者数据库之前已经存在 ShipAny 的库表信息，请不要执行以上命令。而是比较 src/db/migrations 目录下所有迁移文件的 sql 内容，手动执行 sql 语句，更新数据库表。

如果在项目创建之处，你使用的是一个新的数据库，且是通过 pnpm db:migrate 命令初始化的数据库，如果后续你拉取了最新的代码，可以继续执行以下命令，更新数据库表：

这个命令会根据 src/db/migrations 目录下所有迁移文件的 sql 内容，增量更新数据库表。

在项目根目录下执行命令：pnpm db:studio

这个命令会打开一个数据库管理界面，你可以在这里查看、编辑、删除数据库表。

在 src/models 目录下，写数据库操作文件，实现对数据表的增删改查。可参考以下操作 posts 表的示例：

数据表操作语法可参考 drizzle-orm 文档。

如果你使用自建的 Postgres 数据库，或者使用其他兼容 postgres 的云数据库，比如：Neon。配置和连接数据库的步骤跟使用 Supabase 一致，你只需要填写数据库的 DATABASE_URL 即可。

如果你需要使用 MySQL 或者 SQLite 等数据库，可参考以下步骤自定义：

修改 src/db/schema.ts 文件，使用新的数据库 Schema。

Schema 中数据表的字段定义，可以参考 drizzle-orm 文档。

修改 src/db/config.ts 文件，使用新的数据库连接配置。

默认是 Postgres 数据库连接配置，你可以参考 drizzle-orm 文档按需修改。

根据你使用的数据库类型，修改数据库连接实例。

如果你希望后续通过迁移文件更新数据库表。你可以在完成以上三步之后，在项目根目录下执行以下命令生成数据库迁移文件。

在 ShipAny 中配置不同类型的数据库非常简单，只需要完成以上四个步骤的自定义即可。src/model 下操作数据库的逻辑无需修改。

**Examples:**

Example 1 (unknown):
```unknown
postgresql://postgres.defqvdpquwyqqjlmurkg:[YOUR-PASSWORD]@aws-0-ap-southeast-1.pooler.supabase.com:6543/postgres
```

Example 2 (unknown):
```unknown
postgresql://postgres.defqvdpquwyqqjlmurkg:[YOUR-PASSWORD]@aws-0-ap-southeast-1.pooler.supabase.com:6543/postgres
```

Example 3 (unknown):
```unknown
DATABASE_URL="postgresql://postgres.defqvdpquwyqqjlmurkg:******@aws-0-ap-southeast-1.pooler.supabase.com:6543/postgres"
```

Example 4 (unknown):
```unknown
DATABASE_URL="postgresql://postgres.defqvdpquwyqqjlmurkg:******@aws-0-ap-southeast-1.pooler.supabase.com:6543/postgres"
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/features/storage

**Contents:**
- 文件存储
- 配置云存储
- 上传 AI 图片到云存储
- 读取本地文件上传到云存储
- 下载远程图片上传到云存储
- 参考

ShipAny 支持上传文件到 AWS S3 兼容的文件存储系统，例如 AWS S3 / Cloudflare R2 / 腾讯云 COS 等。

选择你的云存储平台，创建存储桶，设置访问密钥和访问域名。

把 aisdk 生成的图片（返回的 base64 数据），上传到云存储。

uploadFile 接收的 body 参数是 Buffer 类型。你可以传递从 URL 下载的文件 Buffer 或者从本地文件读取的 Buffer。

注意：path 和 readFile 在 edge runtime 中无法使用，所以在 cloudflare 部署时，不能读取本地文件。

给定一个远程的图片地址，下载图片并上传到云存储。

**Examples:**

Example 1 (unknown):
```unknown
STORAGE_ENDPOINT = ""
STORAGE_REGION = ""
STORAGE_ACCESS_KEY = ""
STORAGE_SECRET_KEY = ""
STORAGE_BUCKET = ""
STORAGE_DOMAIN = ""
```

Example 2 (unknown):
```unknown
STORAGE_ENDPOINT = ""
STORAGE_REGION = ""
STORAGE_ACCESS_KEY = ""
STORAGE_SECRET_KEY = ""
STORAGE_BUCKET = ""
STORAGE_DOMAIN = ""
```

Example 3 (python):
```python
import { newStorage } from "@/lib/storage";
 
const storage = new Storage();
 
const filename = `image_${new Date().getTime()}.png`;
const key = `shipany/${filename}`;
const body = Buffer.from(image.base64, "base64");
 
try {
  const res = await storage.uploadFile({
    body,
    key,
    contentType: "image/png",
    disposition: "inline",
  });
 
  console.log("upload file success:", res);
} catch (err) {
  console.log("upload file failed:", err);
}
```

Example 4 (python):
```python
import { newStorage } from "@/lib/storage";
 
const storage = new Storage();
 
const filename = `image_${new Date().getTime()}.png`;
const key = `shipany/${filename}`;
const body = Buffer.from(image.base64, "base64");
 
try {
  const res = await storage.uploadFile({
    body,
    key,
    contentType: "image/png",
    disposition: "inline",
  });
 
  console.log("upload file success:", res);
} catch (err) {
  console.log("upload file failed:", err);
}
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/features/payment/stripe#使用折扣码

**Contents:**
- Stripe
- Stripe 设置
- ShipAny 配置
- 价格表支付
  - 配置价格表内容
  - 修改价格表组件
  - 修改价格表下单逻辑
  - 修改支付回调逻辑
  - 修改支付通知逻辑
- 自定义支付

ShipAny 支持使用 Stripe 进行支付，可用于产品付款、会员订阅、购买积分等场景。

在 ShipAny 项目配置文件中，填写 Stripe 相关的配置信息。

页面路径可以填相对路径，也可以填绝对路径。如果填的是相对路径，跳转时会自动拼接 NEXT_PUBLIC_WEB_URL 配置的网站地址，并带上多语言参数。

比如按照以上配置，在中文页面支付成功后的跳转路径是：http://localhost:3000/zh/my-orders

ShipAny 模板内置了一个价格表和对应的支付逻辑，你可以根据自己的需求，简单修改即可快速实现支付功能。

ShipAny 模板内置的价格表配置文件位于：src/i18n/pages/pricing 目录下，支持多语言，默认包含 en.json 和 zh.json 两个价格表配置文件。

你可以根据自己的需求，修改价格表配置文件中的内容。

默认的价格表组件位于：src/components/blocks/pricing/index.tsx

你可以根据自己的需求，修改价格表的展示形式。

默认的价格表下单逻辑位于：src/app/api/checkout/route.ts

你可以根据自己的需求，修改价格表的下单逻辑。

在价格表下单逻辑中，默认配置的支付回调地址是：/api/pay/callback/stripe

用户支付后，会在浏览器跳转到这个地址，并带上包含支付信息的参数。

默认的支付回调处理逻辑位于：src/app/api/pay/callback/stripe/route.ts

你可以根据自己的需求，修改处理支付回调的逻辑，比如更新订单状态、给用户发送邮件通知、给用户赠送积分等。

支付回调是同步逻辑，依赖浏览器跳转到回调地址，才能处理支付结果。这种方式不太可靠，可能出现跳转过程中用户关闭了浏览器等情况，导致支付结果没有被正常处理。 更可靠的方式是通过 Webhook，配置支付结果异步通知。

比如把 Webhook 地址配置为：https://your-domain.com/api/pay/notify/stripe

用户支付后，Stripe 会把支付信息推送到这个地址。

默认的支付通知逻辑位于：src/app/api/pay/notify/stripe/route.ts

你可以根据自己的需求，修改处理支付通知的逻辑，比如更新订单状态、给用户发送邮件通知、给用户赠送积分等。

修改价格表配置文件，添加 groups 数据，配置多个价格分组。并在 pricing.items 下为每一个价格方案，设置一个 group 名称。

配置完成后，点击价格分组，将根据 group 字段，切换显示不同的价格方案。

ShipAny 模板使用 Stripe 支付时，默认支持三种支付方案

你只需要修改价格表配置，把每个价格方案的 interval 字段，设置成上述三个值之一。

同时，按需修改价格(amount) / 积分(credits) / 有效期(valid_months) 等字段。

举例：按月订阅扣费，月付 $99，购买后得到 30 个积分，有效期 1 个月，则核心的价格表配置信息为：

修改 src/app/api/checkout/route.ts 文件，设置 Stripe 下单的 options 参数。

在 Stripe 后台 设置支付方式，开通支付宝和微信支付。

修改价格表配置文件，在每个价格方案下添加一个 cn_amount 字段，即可支持人民币支付。

比如，产品售价，$99，人民币支付价格为 699 元，核心配置信息为：

配置完成后，在价格表下单按钮上方，将会显示一个人民币支付图标。

在 Stripe 后台点击左上角的店铺打开下拉菜单，依次点击 Switch to sandbox -> Test mode，开启测试模式。

在测试模式下，进入开发者中心，设置 测试支付密钥，包括 Publishable key 和 Secret key。

注册 ngrok 账号，按指示安装 ngrok 命令行工具。

启动 ngrok 服务，监听本地端口，并生成一个临时的域名。

在 Stripe 后台测试模式中，配置 Webhook 地址为 ngrok 生成的域名，并监听以下两个事件：

Endpoint 填写支付通知地址，比如 https://xxx.ngrok-free.app/api/pay/notify/stripe。

添加 Webhook 地址后，在 Webhook 管理页面，复制 Signing secret，

跟支付密钥一起填入 .env.development 文件中。

在本地启动项目，访问 /pricing 页面，点击下单按钮，下单成功后跳转到支付页面。

使用 Stripe 测试卡 支付，支付成功后浏览器跳转到支付回调地址，监听的地址收到支付通知。

**Examples:**

Example 1 (unknown):
```unknown
NEXT_PUBLIC_WEB_URL = "http://localhost:3000"

NEXT_PUBLIC_PAY_SUCCESS_URL = "/my-orders"
NEXT_PUBLIC_PAY_FAIL_URL = "/pricing"
NEXT_PUBLIC_PAY_CANCEL_URL = "/pricing"

PAY_PROVIDER = "stripe"

STRIPE_PUBLIC_KEY = "pk_test_xxx"
STRIPE_PRIVATE_KEY = "sk_test_xxx"
STRIPE_WEBHOOK_SECRET = "whsec_cexxx"
```

Example 2 (unknown):
```unknown
NEXT_PUBLIC_WEB_URL = "http://localhost:3000"

NEXT_PUBLIC_PAY_SUCCESS_URL = "/my-orders"
NEXT_PUBLIC_PAY_FAIL_URL = "/pricing"
NEXT_PUBLIC_PAY_CANCEL_URL = "/pricing"

PAY_PROVIDER = "stripe"

STRIPE_PUBLIC_KEY = "pk_test_xxx"
STRIPE_PRIVATE_KEY = "sk_test_xxx"
STRIPE_WEBHOOK_SECRET = "whsec_cexxx"
```

Example 3 (unknown):
```unknown
{
  "pricing": {
    "name": "pricing",
    "label": "Pricing",
    "title": "Pricing",
    "description": "Get all features of ShipAny, Ship your AI SaaS startups fast.",
    "groups": [],
    "items": [
      {
        "title": "Starter",
        "description": "Get started with your first SaaS startup.",
        "features_title": "Includes",
        "features": [
          "100 credits, valid for 1 month",
          "NextJS boilerplate",
          "SEO-friendly structure",
          "Payment with Stripe",
          "Data storage with Supabase",
          "Google Oauth & One-Tap Login",
    
...
```

Example 4 (unknown):
```unknown
{
  "pricing": {
    "name": "pricing",
    "label": "Pricing",
    "title": "Pricing",
    "description": "Get all features of ShipAny, Ship your AI SaaS startups fast.",
    "groups": [],
    "items": [
      {
        "title": "Starter",
        "description": "Get started with your first SaaS startup.",
        "features_title": "Includes",
        "features": [
          "100 credits, valid for 1 month",
          "NextJS boilerplate",
          "SEO-friendly structure",
          "Payment with Stripe",
          "Data storage with Supabase",
          "Google Oauth & One-Tap Login",
    
...
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/features/seo#设置站点地图

**Contents:**
- SEO
- 设置多语言文案
- 设置站点地图
- 网页 SEO 走查
- Metadata 配置
- 接入 GSC

ShipAny 做了很多 SEO 优化，可以让你的项目在搜索引擎中获得更好的排名。

在 i18n/messages 目录下，通过 [locale].json 文件配置页面内容，默认支持中文和英文，在 i18n/messages/ 目录下，可以看到 en.json 和 zh.json 两个文件，在项目发布之前，修改成跟你项目相符合的文案即可。

修改 public/sitemap.xml 文件，配置成你自己的站点信息

按需修改 public/robots.txt 内容

检查网站首页的 title / description / Canonical 是否合理

用 AI 辅助修改 i18n/pages/landing 下 json 文件对应的网页内容，调整网站主打的关键词密度。(3% 左右比较合理)

ShipAny 对默认的 landing page 做了内容结构优化。如果你有自定义页面组件，需要检查页面的结构是否合理。

在 AITDK 插件的 Issues 面板开启 SSR Check，检测网页是否是服务端渲染。

如果你有创建新的页面路由 (page.tsx)，可以配置一下新页面的 Metadata 信息。

为子页面设置独立的 title / description / canonical 信息，有利于 SEO。

网站上站后，在 Google Search Console 中添加你的站点，可以查看网站的搜索流量和排名情况。

**Examples:**

Example 1 (unknown):
```unknown
update content of this file, for my new project "Flux AI", which is an AI Image Generator, with keywords "flux ai, ai image generator"
```

Example 2 (unknown):
```unknown
update content of this file, for my new project "Flux AI", which is an AI Image Generator, with keywords "flux ai, ai image generator"
```

Example 3 (unknown):
```unknown
<?xml version='1.0' encoding='utf-8' standalone='yes'?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://shipany.ai/</loc>
    <lastmod>2024-12-24T10:00:00+00:00</lastmod>
  </url>
</urlset>
```

Example 4 (unknown):
```unknown
<?xml version='1.0' encoding='utf-8' standalone='yes'?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://shipany.ai/</loc>
    <lastmod>2024-12-24T10:00:00+00:00</lastmod>
  </url>
</urlset>
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/features/affiliate#如何使用

**Contents:**
- 邀请返佣
- 如何使用
- 如何自定义奖励金额和比例

ShipAny 实现了一套邀请返佣系统。你可以在你的产品中使用这套系统来激励用户邀请新用户。

用户进入：http://localhost:3000/my-invites 页面，可以生成自己的邀请链接。

http://localhost:3000/i/idoubi

新用户通过分享者的邀请链接进入系统，会自动关联到分享者。

分享者可以在 /my-invites 页面查看邀请记录和邀请奖励

暂不支持在线自动提现，需要管理员人工联系用户发放奖励。

你可以修改此接口的逻辑，更改新用户注册场景下的奖励规则。

默认的 AffiliateRewardPercent.Invited 和 AffiliateRewardAmount.Invited 都是 0.

你可以修改此方法内的逻辑，修改被邀请人支付的订单，给到邀请人的奖励

默认的 AffiliateRewardPercent.Paied 值是 20，代表返佣比例是 20%

默认的 AffiliateRewardAmount.Paied 值是 50，代表返佣金额是 $50

**Examples:**

Example 1 (unknown):
```unknown
await insertAffiliate({
  user_uuid: user_uuid,
  invited_by: inviteUser.uuid,
  created_at: getIsoTimestr(),
  status: AffiliateStatus.Pending,
  paid_order_no: "",
  paid_amount: 0,
  reward_percent: AffiliateRewardPercent.Invited,
  reward_amount: AffiliateRewardAmount.Invited,
});
```

Example 2 (unknown):
```unknown
await insertAffiliate({
  user_uuid: user_uuid,
  invited_by: inviteUser.uuid,
  created_at: getIsoTimestr(),
  status: AffiliateStatus.Pending,
  paid_order_no: "",
  paid_amount: 0,
  reward_percent: AffiliateRewardPercent.Invited,
  reward_amount: AffiliateRewardAmount.Invited,
});
```

Example 3 (python):
```python
import { findAffiliateByOrderNo, insertAffiliate } from "@/models/affiliate";
 
import { AffiliateRewardAmount } from "./constant";
import { AffiliateRewardPercent } from "./constant";
import { AffiliateStatus } from "./constant";
import { Order } from "@/types/order";
import { findUserByUuid } from "@/models/user";
import { getIsoTimestr } from "@/lib/time";
 
export async function updateAffiliateForOrder(order: Order) {
  try {
    const user = await findUserByUuid(order.user_uuid);
    if (user && user.uuid && user.invited_by && user.invited_by !== user.uuid) {
      const affiliate = await
...
```

Example 4 (python):
```python
import { findAffiliateByOrderNo, insertAffiliate } from "@/models/affiliate";
 
import { AffiliateRewardAmount } from "./constant";
import { AffiliateRewardPercent } from "./constant";
import { AffiliateStatus } from "./constant";
import { Order } from "@/types/order";
import { findUserByUuid } from "@/models/user";
import { getIsoTimestr } from "@/lib/time";
 
export async function updateAffiliateForOrder(order: Order) {
  try {
    const user = await findUserByUuid(order.user_uuid);
    if (user && user.uuid && user.invited_by && user.invited_by !== user.uuid) {
      const affiliate = await
...
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/features/payment/stripe#本地测试

**Contents:**
- Stripe
- Stripe 设置
- ShipAny 配置
- 价格表支付
  - 配置价格表内容
  - 修改价格表组件
  - 修改价格表下单逻辑
  - 修改支付回调逻辑
  - 修改支付通知逻辑
- 自定义支付

ShipAny 支持使用 Stripe 进行支付，可用于产品付款、会员订阅、购买积分等场景。

在 ShipAny 项目配置文件中，填写 Stripe 相关的配置信息。

页面路径可以填相对路径，也可以填绝对路径。如果填的是相对路径，跳转时会自动拼接 NEXT_PUBLIC_WEB_URL 配置的网站地址，并带上多语言参数。

比如按照以上配置，在中文页面支付成功后的跳转路径是：http://localhost:3000/zh/my-orders

ShipAny 模板内置了一个价格表和对应的支付逻辑，你可以根据自己的需求，简单修改即可快速实现支付功能。

ShipAny 模板内置的价格表配置文件位于：src/i18n/pages/pricing 目录下，支持多语言，默认包含 en.json 和 zh.json 两个价格表配置文件。

你可以根据自己的需求，修改价格表配置文件中的内容。

默认的价格表组件位于：src/components/blocks/pricing/index.tsx

你可以根据自己的需求，修改价格表的展示形式。

默认的价格表下单逻辑位于：src/app/api/checkout/route.ts

你可以根据自己的需求，修改价格表的下单逻辑。

在价格表下单逻辑中，默认配置的支付回调地址是：/api/pay/callback/stripe

用户支付后，会在浏览器跳转到这个地址，并带上包含支付信息的参数。

默认的支付回调处理逻辑位于：src/app/api/pay/callback/stripe/route.ts

你可以根据自己的需求，修改处理支付回调的逻辑，比如更新订单状态、给用户发送邮件通知、给用户赠送积分等。

支付回调是同步逻辑，依赖浏览器跳转到回调地址，才能处理支付结果。这种方式不太可靠，可能出现跳转过程中用户关闭了浏览器等情况，导致支付结果没有被正常处理。 更可靠的方式是通过 Webhook，配置支付结果异步通知。

比如把 Webhook 地址配置为：https://your-domain.com/api/pay/notify/stripe

用户支付后，Stripe 会把支付信息推送到这个地址。

默认的支付通知逻辑位于：src/app/api/pay/notify/stripe/route.ts

你可以根据自己的需求，修改处理支付通知的逻辑，比如更新订单状态、给用户发送邮件通知、给用户赠送积分等。

修改价格表配置文件，添加 groups 数据，配置多个价格分组。并在 pricing.items 下为每一个价格方案，设置一个 group 名称。

配置完成后，点击价格分组，将根据 group 字段，切换显示不同的价格方案。

ShipAny 模板使用 Stripe 支付时，默认支持三种支付方案

你只需要修改价格表配置，把每个价格方案的 interval 字段，设置成上述三个值之一。

同时，按需修改价格(amount) / 积分(credits) / 有效期(valid_months) 等字段。

举例：按月订阅扣费，月付 $99，购买后得到 30 个积分，有效期 1 个月，则核心的价格表配置信息为：

修改 src/app/api/checkout/route.ts 文件，设置 Stripe 下单的 options 参数。

在 Stripe 后台 设置支付方式，开通支付宝和微信支付。

修改价格表配置文件，在每个价格方案下添加一个 cn_amount 字段，即可支持人民币支付。

比如，产品售价，$99，人民币支付价格为 699 元，核心配置信息为：

配置完成后，在价格表下单按钮上方，将会显示一个人民币支付图标。

在 Stripe 后台点击左上角的店铺打开下拉菜单，依次点击 Switch to sandbox -> Test mode，开启测试模式。

在测试模式下，进入开发者中心，设置 测试支付密钥，包括 Publishable key 和 Secret key。

注册 ngrok 账号，按指示安装 ngrok 命令行工具。

启动 ngrok 服务，监听本地端口，并生成一个临时的域名。

在 Stripe 后台测试模式中，配置 Webhook 地址为 ngrok 生成的域名，并监听以下两个事件：

Endpoint 填写支付通知地址，比如 https://xxx.ngrok-free.app/api/pay/notify/stripe。

添加 Webhook 地址后，在 Webhook 管理页面，复制 Signing secret，

跟支付密钥一起填入 .env.development 文件中。

在本地启动项目，访问 /pricing 页面，点击下单按钮，下单成功后跳转到支付页面。

使用 Stripe 测试卡 支付，支付成功后浏览器跳转到支付回调地址，监听的地址收到支付通知。

**Examples:**

Example 1 (unknown):
```unknown
NEXT_PUBLIC_WEB_URL = "http://localhost:3000"

NEXT_PUBLIC_PAY_SUCCESS_URL = "/my-orders"
NEXT_PUBLIC_PAY_FAIL_URL = "/pricing"
NEXT_PUBLIC_PAY_CANCEL_URL = "/pricing"

PAY_PROVIDER = "stripe"

STRIPE_PUBLIC_KEY = "pk_test_xxx"
STRIPE_PRIVATE_KEY = "sk_test_xxx"
STRIPE_WEBHOOK_SECRET = "whsec_cexxx"
```

Example 2 (unknown):
```unknown
NEXT_PUBLIC_WEB_URL = "http://localhost:3000"

NEXT_PUBLIC_PAY_SUCCESS_URL = "/my-orders"
NEXT_PUBLIC_PAY_FAIL_URL = "/pricing"
NEXT_PUBLIC_PAY_CANCEL_URL = "/pricing"

PAY_PROVIDER = "stripe"

STRIPE_PUBLIC_KEY = "pk_test_xxx"
STRIPE_PRIVATE_KEY = "sk_test_xxx"
STRIPE_WEBHOOK_SECRET = "whsec_cexxx"
```

Example 3 (unknown):
```unknown
{
  "pricing": {
    "name": "pricing",
    "label": "Pricing",
    "title": "Pricing",
    "description": "Get all features of ShipAny, Ship your AI SaaS startups fast.",
    "groups": [],
    "items": [
      {
        "title": "Starter",
        "description": "Get started with your first SaaS startup.",
        "features_title": "Includes",
        "features": [
          "100 credits, valid for 1 month",
          "NextJS boilerplate",
          "SEO-friendly structure",
          "Payment with Stripe",
          "Data storage with Supabase",
          "Google Oauth & One-Tap Login",
    
...
```

Example 4 (unknown):
```unknown
{
  "pricing": {
    "name": "pricing",
    "label": "Pricing",
    "title": "Pricing",
    "description": "Get all features of ShipAny, Ship your AI SaaS startups fast.",
    "groups": [],
    "items": [
      {
        "title": "Starter",
        "description": "Get started with your first SaaS startup.",
        "features_title": "Includes",
        "features": [
          "100 credits, valid for 1 month",
          "NextJS boilerplate",
          "SEO-friendly structure",
          "Payment with Stripe",
          "Data storage with Supabase",
          "Google Oauth & One-Tap Login",
    
...
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/features/payment/creem#修改价格表组件

**Contents:**
- Creem
- Creem 设置
- ShipAny 配置
- 价格表支付
  - 配置价格表内容
  - 修改价格表组件
  - 修改价格表下单逻辑
  - 修改支付回调逻辑
  - 修改支付通知逻辑
- 本地测试

ShipAny 支持使用 Creem 进行支付，可用于产品付款、会员订阅、购买积分等场景。

在 ShipAny 项目配置文件中，填写 Creem 相关的配置信息。

页面路径可以填相对路径，也可以填绝对路径。如果填的是相对路径，跳转时会自动拼接 NEXT_PUBLIC_WEB_URL 配置的网站地址，并带上多语言参数。

比如按照以上配置，在中文页面支付成功后的跳转路径是：http://localhost:3000/zh/my-orders

比如在 ShipAny 项目中设置的价格表有三个支付方案，对应的 product_id 分别是 starter、standard、premium，你需要在 Creem 后台为这三个方案 创建对应的产品，复制每个产品的 Product ID，与价格表中的 product_id 对应关系填写到 CREEM_PRODUCTS 中。

ShipAny 模板内置了一个价格表和对应的支付逻辑，你可以根据自己的需求，简单修改即可快速实现支付功能。

ShipAny 模板内置的价格表配置文件位于：src/i18n/pages/pricing 目录下，支持多语言，默认包含 en.json 和 zh.json 两个价格表配置文件。

你可以根据自己的需求，修改价格表配置文件中的内容。

默认的价格表组件位于：src/components/blocks/pricing/index.tsx

你可以根据自己的需求，修改价格表的展示形式。

默认的价格表下单逻辑位于：src/app/api/checkout/route.ts

你可以根据自己的需求，修改价格表的下单逻辑。

在价格表下单逻辑中，默认配置的支付回调地址是：/api/pay/callback/creem

用户支付后，会在浏览器跳转到这个地址，并带上包含支付信息的参数。

默认的支付回调处理逻辑位于：src/app/api/pay/callback/creem/route.ts

你可以根据自己的需求，修改处理支付回调的逻辑，比如更新订单状态、给用户发送邮件通知、给用户赠送积分等。

支付回调是同步逻辑，依赖浏览器跳转到回调地址，才能处理支付结果。这种方式不太可靠，可能出现跳转过程中用户关闭了浏览器等情况，导致支付结果没有被正常处理。 更可靠的方式是通过 Webhook，配置支付结果异步通知。

比如把 Webhook 地址配置为：https://your-domain.com/api/pay/notify/creem

用户支付后，Creem 会把支付信息推送到这个地址。

默认的支付通知逻辑位于：src/app/api/pay/notify/creem/route.ts

你可以根据自己的需求，修改处理支付通知的逻辑，比如更新订单状态、给用户发送邮件通知、给用户赠送积分等。

在 Creem 后台进入店铺，点击右上角的 Test mode，开启测试模式。

在测试模式下，进入开发者中心，设置 测试 API 密钥。

注册 ngrok 账号，按指示安装 ngrok 命令行工具。

启动 ngrok 服务，监听本地端口，并生成一个临时的域名。

在 Creem 后台测试模式中，配置 Webhook 地址为 ngrok 生成的域名

Endpoint 填写支付通知地址，比如 https://xxx.ngrok-free.app/api/pay/notify/creem。

添加 Webhook 地址后，在 Webhook 管理页面，复制 Signing secret，

跟支付密钥一起填入 .env.development 文件中。

在本地启动项目，访问 /pricing 页面，点击下单按钮，下单成功后跳转到支付页面。

使用 Stripe 测试卡 支付，支付成功后浏览器跳转到支付回调地址，监听的地址收到支付通知。

**Examples:**

Example 1 (unknown):
```unknown
NEXT_PUBLIC_WEB_URL = "http://localhost:3000"

NEXT_PUBLIC_PAY_SUCCESS_URL = "/my-orders"
NEXT_PUBLIC_PAY_FAIL_URL = "/pricing"
NEXT_PUBLIC_PAY_CANCEL_URL = "/pricing"

PAY_PROVIDER = "creem"

CREEM_ENV = "test"
CREEM_API_KEY = "creem_test_xxx"
CREEM_WEBHOOK_SECRET = "whsec_xxx"
CREEM_PRODUCTS = '{"starter": "prod_xxx", "standard": "prod_xxx", "premium": "prod_xxx"}'
```

Example 2 (unknown):
```unknown
NEXT_PUBLIC_WEB_URL = "http://localhost:3000"

NEXT_PUBLIC_PAY_SUCCESS_URL = "/my-orders"
NEXT_PUBLIC_PAY_FAIL_URL = "/pricing"
NEXT_PUBLIC_PAY_CANCEL_URL = "/pricing"

PAY_PROVIDER = "creem"

CREEM_ENV = "test"
CREEM_API_KEY = "creem_test_xxx"
CREEM_WEBHOOK_SECRET = "whsec_xxx"
CREEM_PRODUCTS = '{"starter": "prod_xxx", "standard": "prod_xxx", "premium": "prod_xxx"}'
```

Example 3 (unknown):
```unknown
{
  "pricing": {
    "name": "pricing",
    "label": "Pricing",
    "title": "Pricing",
    "description": "Get all features of ShipAny, Ship your AI SaaS startups fast.",
    "groups": [],
    "items": [
      {
        "title": "Starter",
        "description": "Get started with your first SaaS startup.",
        "features_title": "Includes",
        "features": [
          "100 credits, valid for 1 month",
          "NextJS boilerplate",
          "SEO-friendly structure",
          "Payment with Stripe",
          "Data storage with Supabase",
          "Google Oauth & One-Tap Login",
    
...
```

Example 4 (unknown):
```unknown
{
  "pricing": {
    "name": "pricing",
    "label": "Pricing",
    "title": "Pricing",
    "description": "Get all features of ShipAny, Ship your AI SaaS startups fast.",
    "groups": [],
    "items": [
      {
        "title": "Starter",
        "description": "Get started with your first SaaS startup.",
        "features_title": "Includes",
        "features": [
          "100 credits, valid for 1 month",
          "NextJS boilerplate",
          "SEO-friendly structure",
          "Payment with Stripe",
          "Data storage with Supabase",
          "Google Oauth & One-Tap Login",
    
...
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/features/seo#网页-seo-走查

**Contents:**
- SEO
- 设置多语言文案
- 设置站点地图
- 网页 SEO 走查
- Metadata 配置
- 接入 GSC

ShipAny 做了很多 SEO 优化，可以让你的项目在搜索引擎中获得更好的排名。

在 i18n/messages 目录下，通过 [locale].json 文件配置页面内容，默认支持中文和英文，在 i18n/messages/ 目录下，可以看到 en.json 和 zh.json 两个文件，在项目发布之前，修改成跟你项目相符合的文案即可。

修改 public/sitemap.xml 文件，配置成你自己的站点信息

按需修改 public/robots.txt 内容

检查网站首页的 title / description / Canonical 是否合理

用 AI 辅助修改 i18n/pages/landing 下 json 文件对应的网页内容，调整网站主打的关键词密度。(3% 左右比较合理)

ShipAny 对默认的 landing page 做了内容结构优化。如果你有自定义页面组件，需要检查页面的结构是否合理。

在 AITDK 插件的 Issues 面板开启 SSR Check，检测网页是否是服务端渲染。

如果你有创建新的页面路由 (page.tsx)，可以配置一下新页面的 Metadata 信息。

为子页面设置独立的 title / description / canonical 信息，有利于 SEO。

网站上站后，在 Google Search Console 中添加你的站点，可以查看网站的搜索流量和排名情况。

**Examples:**

Example 1 (unknown):
```unknown
update content of this file, for my new project "Flux AI", which is an AI Image Generator, with keywords "flux ai, ai image generator"
```

Example 2 (unknown):
```unknown
update content of this file, for my new project "Flux AI", which is an AI Image Generator, with keywords "flux ai, ai image generator"
```

Example 3 (unknown):
```unknown
<?xml version='1.0' encoding='utf-8' standalone='yes'?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://shipany.ai/</loc>
    <lastmod>2024-12-24T10:00:00+00:00</lastmod>
  </url>
</urlset>
```

Example 4 (unknown):
```unknown
<?xml version='1.0' encoding='utf-8' standalone='yes'?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://shipany.ai/</loc>
    <lastmod>2024-12-24T10:00:00+00:00</lastmod>
  </url>
</urlset>
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/features/database#操作数据库

**Contents:**
- 数据库
- 配置数据库
- 初始化数据库
- 更新数据库
- 管理数据库
- 操作数据库
- 使用其他类型数据库
- 参考

ShipAny 使用 drizzle-orm 支持多种类型数据库。

以 Supabase 数据库为例，在 ShipAny 配置数据库的流程为：

登录 Supabase 控制台，创建数据库

在 Supabase 控制台，进入你创建的数据库，点击上方的 Connect

在弹出来的框中复制数据库连接信息，类似这样的字符串：

[YOUR-PASSWORD] 需要替换成你在创建数据库时设置的密码。

修改项目配置文件：.env.development 和 .env.production

在配置好 DATABASE_URL 后，在项目根目录下运行以下命令，初始化数据库：

这个命令会执行 src/db/migrations 目录下的所有迁移文件，创建数据库表。

如果你通过 DATABASE_URL 配置的不是一个新创建的数据库，或者数据库之前已经存在 ShipAny 的库表信息，请不要执行以上命令。而是比较 src/db/migrations 目录下所有迁移文件的 sql 内容，手动执行 sql 语句，更新数据库表。

如果在项目创建之处，你使用的是一个新的数据库，且是通过 pnpm db:migrate 命令初始化的数据库，如果后续你拉取了最新的代码，可以继续执行以下命令，更新数据库表：

这个命令会根据 src/db/migrations 目录下所有迁移文件的 sql 内容，增量更新数据库表。

在项目根目录下执行命令：pnpm db:studio

这个命令会打开一个数据库管理界面，你可以在这里查看、编辑、删除数据库表。

在 src/models 目录下，写数据库操作文件，实现对数据表的增删改查。可参考以下操作 posts 表的示例：

数据表操作语法可参考 drizzle-orm 文档。

如果你使用自建的 Postgres 数据库，或者使用其他兼容 postgres 的云数据库，比如：Neon。配置和连接数据库的步骤跟使用 Supabase 一致，你只需要填写数据库的 DATABASE_URL 即可。

如果你需要使用 MySQL 或者 SQLite 等数据库，可参考以下步骤自定义：

修改 src/db/schema.ts 文件，使用新的数据库 Schema。

Schema 中数据表的字段定义，可以参考 drizzle-orm 文档。

修改 src/db/config.ts 文件，使用新的数据库连接配置。

默认是 Postgres 数据库连接配置，你可以参考 drizzle-orm 文档按需修改。

根据你使用的数据库类型，修改数据库连接实例。

如果你希望后续通过迁移文件更新数据库表。你可以在完成以上三步之后，在项目根目录下执行以下命令生成数据库迁移文件。

在 ShipAny 中配置不同类型的数据库非常简单，只需要完成以上四个步骤的自定义即可。src/model 下操作数据库的逻辑无需修改。

**Examples:**

Example 1 (unknown):
```unknown
postgresql://postgres.defqvdpquwyqqjlmurkg:[YOUR-PASSWORD]@aws-0-ap-southeast-1.pooler.supabase.com:6543/postgres
```

Example 2 (unknown):
```unknown
postgresql://postgres.defqvdpquwyqqjlmurkg:[YOUR-PASSWORD]@aws-0-ap-southeast-1.pooler.supabase.com:6543/postgres
```

Example 3 (unknown):
```unknown
DATABASE_URL="postgresql://postgres.defqvdpquwyqqjlmurkg:******@aws-0-ap-southeast-1.pooler.supabase.com:6543/postgres"
```

Example 4 (unknown):
```unknown
DATABASE_URL="postgresql://postgres.defqvdpquwyqqjlmurkg:******@aws-0-ap-southeast-1.pooler.supabase.com:6543/postgres"
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/features/payment/stripe#修改支付回调逻辑

**Contents:**
- Stripe
- Stripe 设置
- ShipAny 配置
- 价格表支付
  - 配置价格表内容
  - 修改价格表组件
  - 修改价格表下单逻辑
  - 修改支付回调逻辑
  - 修改支付通知逻辑
- 自定义支付

ShipAny 支持使用 Stripe 进行支付，可用于产品付款、会员订阅、购买积分等场景。

在 ShipAny 项目配置文件中，填写 Stripe 相关的配置信息。

页面路径可以填相对路径，也可以填绝对路径。如果填的是相对路径，跳转时会自动拼接 NEXT_PUBLIC_WEB_URL 配置的网站地址，并带上多语言参数。

比如按照以上配置，在中文页面支付成功后的跳转路径是：http://localhost:3000/zh/my-orders

ShipAny 模板内置了一个价格表和对应的支付逻辑，你可以根据自己的需求，简单修改即可快速实现支付功能。

ShipAny 模板内置的价格表配置文件位于：src/i18n/pages/pricing 目录下，支持多语言，默认包含 en.json 和 zh.json 两个价格表配置文件。

你可以根据自己的需求，修改价格表配置文件中的内容。

默认的价格表组件位于：src/components/blocks/pricing/index.tsx

你可以根据自己的需求，修改价格表的展示形式。

默认的价格表下单逻辑位于：src/app/api/checkout/route.ts

你可以根据自己的需求，修改价格表的下单逻辑。

在价格表下单逻辑中，默认配置的支付回调地址是：/api/pay/callback/stripe

用户支付后，会在浏览器跳转到这个地址，并带上包含支付信息的参数。

默认的支付回调处理逻辑位于：src/app/api/pay/callback/stripe/route.ts

你可以根据自己的需求，修改处理支付回调的逻辑，比如更新订单状态、给用户发送邮件通知、给用户赠送积分等。

支付回调是同步逻辑，依赖浏览器跳转到回调地址，才能处理支付结果。这种方式不太可靠，可能出现跳转过程中用户关闭了浏览器等情况，导致支付结果没有被正常处理。 更可靠的方式是通过 Webhook，配置支付结果异步通知。

比如把 Webhook 地址配置为：https://your-domain.com/api/pay/notify/stripe

用户支付后，Stripe 会把支付信息推送到这个地址。

默认的支付通知逻辑位于：src/app/api/pay/notify/stripe/route.ts

你可以根据自己的需求，修改处理支付通知的逻辑，比如更新订单状态、给用户发送邮件通知、给用户赠送积分等。

修改价格表配置文件，添加 groups 数据，配置多个价格分组。并在 pricing.items 下为每一个价格方案，设置一个 group 名称。

配置完成后，点击价格分组，将根据 group 字段，切换显示不同的价格方案。

ShipAny 模板使用 Stripe 支付时，默认支持三种支付方案

你只需要修改价格表配置，把每个价格方案的 interval 字段，设置成上述三个值之一。

同时，按需修改价格(amount) / 积分(credits) / 有效期(valid_months) 等字段。

举例：按月订阅扣费，月付 $99，购买后得到 30 个积分，有效期 1 个月，则核心的价格表配置信息为：

修改 src/app/api/checkout/route.ts 文件，设置 Stripe 下单的 options 参数。

在 Stripe 后台 设置支付方式，开通支付宝和微信支付。

修改价格表配置文件，在每个价格方案下添加一个 cn_amount 字段，即可支持人民币支付。

比如，产品售价，$99，人民币支付价格为 699 元，核心配置信息为：

配置完成后，在价格表下单按钮上方，将会显示一个人民币支付图标。

在 Stripe 后台点击左上角的店铺打开下拉菜单，依次点击 Switch to sandbox -> Test mode，开启测试模式。

在测试模式下，进入开发者中心，设置 测试支付密钥，包括 Publishable key 和 Secret key。

注册 ngrok 账号，按指示安装 ngrok 命令行工具。

启动 ngrok 服务，监听本地端口，并生成一个临时的域名。

在 Stripe 后台测试模式中，配置 Webhook 地址为 ngrok 生成的域名，并监听以下两个事件：

Endpoint 填写支付通知地址，比如 https://xxx.ngrok-free.app/api/pay/notify/stripe。

添加 Webhook 地址后，在 Webhook 管理页面，复制 Signing secret，

跟支付密钥一起填入 .env.development 文件中。

在本地启动项目，访问 /pricing 页面，点击下单按钮，下单成功后跳转到支付页面。

使用 Stripe 测试卡 支付，支付成功后浏览器跳转到支付回调地址，监听的地址收到支付通知。

**Examples:**

Example 1 (unknown):
```unknown
NEXT_PUBLIC_WEB_URL = "http://localhost:3000"

NEXT_PUBLIC_PAY_SUCCESS_URL = "/my-orders"
NEXT_PUBLIC_PAY_FAIL_URL = "/pricing"
NEXT_PUBLIC_PAY_CANCEL_URL = "/pricing"

PAY_PROVIDER = "stripe"

STRIPE_PUBLIC_KEY = "pk_test_xxx"
STRIPE_PRIVATE_KEY = "sk_test_xxx"
STRIPE_WEBHOOK_SECRET = "whsec_cexxx"
```

Example 2 (unknown):
```unknown
NEXT_PUBLIC_WEB_URL = "http://localhost:3000"

NEXT_PUBLIC_PAY_SUCCESS_URL = "/my-orders"
NEXT_PUBLIC_PAY_FAIL_URL = "/pricing"
NEXT_PUBLIC_PAY_CANCEL_URL = "/pricing"

PAY_PROVIDER = "stripe"

STRIPE_PUBLIC_KEY = "pk_test_xxx"
STRIPE_PRIVATE_KEY = "sk_test_xxx"
STRIPE_WEBHOOK_SECRET = "whsec_cexxx"
```

Example 3 (unknown):
```unknown
{
  "pricing": {
    "name": "pricing",
    "label": "Pricing",
    "title": "Pricing",
    "description": "Get all features of ShipAny, Ship your AI SaaS startups fast.",
    "groups": [],
    "items": [
      {
        "title": "Starter",
        "description": "Get started with your first SaaS startup.",
        "features_title": "Includes",
        "features": [
          "100 credits, valid for 1 month",
          "NextJS boilerplate",
          "SEO-friendly structure",
          "Payment with Stripe",
          "Data storage with Supabase",
          "Google Oauth & One-Tap Login",
    
...
```

Example 4 (unknown):
```unknown
{
  "pricing": {
    "name": "pricing",
    "label": "Pricing",
    "title": "Pricing",
    "description": "Get all features of ShipAny, Ship your AI SaaS startups fast.",
    "groups": [],
    "items": [
      {
        "title": "Starter",
        "description": "Get started with your first SaaS startup.",
        "features_title": "Includes",
        "features": [
          "100 credits, valid for 1 month",
          "NextJS boilerplate",
          "SEO-friendly structure",
          "Payment with Stripe",
          "Data storage with Supabase",
          "Google Oauth & One-Tap Login",
    
...
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/features/payment/creem#价格表支付

**Contents:**
- Creem
- Creem 设置
- ShipAny 配置
- 价格表支付
  - 配置价格表内容
  - 修改价格表组件
  - 修改价格表下单逻辑
  - 修改支付回调逻辑
  - 修改支付通知逻辑
- 本地测试

ShipAny 支持使用 Creem 进行支付，可用于产品付款、会员订阅、购买积分等场景。

在 ShipAny 项目配置文件中，填写 Creem 相关的配置信息。

页面路径可以填相对路径，也可以填绝对路径。如果填的是相对路径，跳转时会自动拼接 NEXT_PUBLIC_WEB_URL 配置的网站地址，并带上多语言参数。

比如按照以上配置，在中文页面支付成功后的跳转路径是：http://localhost:3000/zh/my-orders

比如在 ShipAny 项目中设置的价格表有三个支付方案，对应的 product_id 分别是 starter、standard、premium，你需要在 Creem 后台为这三个方案 创建对应的产品，复制每个产品的 Product ID，与价格表中的 product_id 对应关系填写到 CREEM_PRODUCTS 中。

ShipAny 模板内置了一个价格表和对应的支付逻辑，你可以根据自己的需求，简单修改即可快速实现支付功能。

ShipAny 模板内置的价格表配置文件位于：src/i18n/pages/pricing 目录下，支持多语言，默认包含 en.json 和 zh.json 两个价格表配置文件。

你可以根据自己的需求，修改价格表配置文件中的内容。

默认的价格表组件位于：src/components/blocks/pricing/index.tsx

你可以根据自己的需求，修改价格表的展示形式。

默认的价格表下单逻辑位于：src/app/api/checkout/route.ts

你可以根据自己的需求，修改价格表的下单逻辑。

在价格表下单逻辑中，默认配置的支付回调地址是：/api/pay/callback/creem

用户支付后，会在浏览器跳转到这个地址，并带上包含支付信息的参数。

默认的支付回调处理逻辑位于：src/app/api/pay/callback/creem/route.ts

你可以根据自己的需求，修改处理支付回调的逻辑，比如更新订单状态、给用户发送邮件通知、给用户赠送积分等。

支付回调是同步逻辑，依赖浏览器跳转到回调地址，才能处理支付结果。这种方式不太可靠，可能出现跳转过程中用户关闭了浏览器等情况，导致支付结果没有被正常处理。 更可靠的方式是通过 Webhook，配置支付结果异步通知。

比如把 Webhook 地址配置为：https://your-domain.com/api/pay/notify/creem

用户支付后，Creem 会把支付信息推送到这个地址。

默认的支付通知逻辑位于：src/app/api/pay/notify/creem/route.ts

你可以根据自己的需求，修改处理支付通知的逻辑，比如更新订单状态、给用户发送邮件通知、给用户赠送积分等。

在 Creem 后台进入店铺，点击右上角的 Test mode，开启测试模式。

在测试模式下，进入开发者中心，设置 测试 API 密钥。

注册 ngrok 账号，按指示安装 ngrok 命令行工具。

启动 ngrok 服务，监听本地端口，并生成一个临时的域名。

在 Creem 后台测试模式中，配置 Webhook 地址为 ngrok 生成的域名

Endpoint 填写支付通知地址，比如 https://xxx.ngrok-free.app/api/pay/notify/creem。

添加 Webhook 地址后，在 Webhook 管理页面，复制 Signing secret，

跟支付密钥一起填入 .env.development 文件中。

在本地启动项目，访问 /pricing 页面，点击下单按钮，下单成功后跳转到支付页面。

使用 Stripe 测试卡 支付，支付成功后浏览器跳转到支付回调地址，监听的地址收到支付通知。

**Examples:**

Example 1 (unknown):
```unknown
NEXT_PUBLIC_WEB_URL = "http://localhost:3000"

NEXT_PUBLIC_PAY_SUCCESS_URL = "/my-orders"
NEXT_PUBLIC_PAY_FAIL_URL = "/pricing"
NEXT_PUBLIC_PAY_CANCEL_URL = "/pricing"

PAY_PROVIDER = "creem"

CREEM_ENV = "test"
CREEM_API_KEY = "creem_test_xxx"
CREEM_WEBHOOK_SECRET = "whsec_xxx"
CREEM_PRODUCTS = '{"starter": "prod_xxx", "standard": "prod_xxx", "premium": "prod_xxx"}'
```

Example 2 (unknown):
```unknown
NEXT_PUBLIC_WEB_URL = "http://localhost:3000"

NEXT_PUBLIC_PAY_SUCCESS_URL = "/my-orders"
NEXT_PUBLIC_PAY_FAIL_URL = "/pricing"
NEXT_PUBLIC_PAY_CANCEL_URL = "/pricing"

PAY_PROVIDER = "creem"

CREEM_ENV = "test"
CREEM_API_KEY = "creem_test_xxx"
CREEM_WEBHOOK_SECRET = "whsec_xxx"
CREEM_PRODUCTS = '{"starter": "prod_xxx", "standard": "prod_xxx", "premium": "prod_xxx"}'
```

Example 3 (unknown):
```unknown
{
  "pricing": {
    "name": "pricing",
    "label": "Pricing",
    "title": "Pricing",
    "description": "Get all features of ShipAny, Ship your AI SaaS startups fast.",
    "groups": [],
    "items": [
      {
        "title": "Starter",
        "description": "Get started with your first SaaS startup.",
        "features_title": "Includes",
        "features": [
          "100 credits, valid for 1 month",
          "NextJS boilerplate",
          "SEO-friendly structure",
          "Payment with Stripe",
          "Data storage with Supabase",
          "Google Oauth & One-Tap Login",
    
...
```

Example 4 (unknown):
```unknown
{
  "pricing": {
    "name": "pricing",
    "label": "Pricing",
    "title": "Pricing",
    "description": "Get all features of ShipAny, Ship your AI SaaS startups fast.",
    "groups": [],
    "items": [
      {
        "title": "Starter",
        "description": "Get started with your first SaaS startup.",
        "features_title": "Includes",
        "features": [
          "100 credits, valid for 1 month",
          "NextJS boilerplate",
          "SEO-friendly structure",
          "Payment with Stripe",
          "Data storage with Supabase",
          "Google Oauth & One-Tap Login",
    
...
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/features/oauth#参考

**Contents:**
- 登录鉴权
- 生成 Auth Secret
- 谷歌登录
- 谷歌一键登录
- Github 登录
- 登录预览
- 参考

ShipAny 目前支持 谷歌登录 / 谷歌一键登录 / Github 登录三种登录方式。

其他登录方式逐步集成，也可以参考 next-auth 文档自行接入。

生成一个 32 字节的随机字符串，作为 Auth Secret

修改环境变量中的 AUTH_SECRET 值

创建一个新项目，进入新项目的 Credentials 管理页面，创建 Oauth Client ID

创建 Oauth Client ID 后，得到 Client ID 和 Client Secret

首先按照谷歌登录的步骤，拿到 AUTH_GOOGLE_ID 和 AUTH_GOOGLE_SECRET

修改配置文件中的 NEXT_PUBLIC_AUTH_GOOGLE_ONE_TAP_ENABLED 和 NEXT_PUBLIC_AUTH_GOOGLE_ID

谷歌一键登录使用到的 NEXT_PUBLIC_AUTH_GOOGLE_ID 跟谷歌登录配置的 AUTH_GOOGLE_ID 保持一致。

开发环境和生产环境，需要创建两个不同的 OAuth app，分别配置不同的回调地址。

进入 OAuth app，复制 Client ID 和 Client Secret

修改配置文件中的 AUTH_GITHUB_ID 和 AUTH_GITHUB_SECRET

**Examples:**

Example 1 (unknown):
```unknown
openssl rand -base64 32
```

Example 2 (unknown):
```unknown
openssl rand -base64 32
```

Example 3 (unknown):
```unknown
AUTH_SECRET = "xxx"
```

Example 4 (unknown):
```unknown
AUTH_SECRET = "xxx"
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/guide/good-to-know#shipany-框架包含哪些功能

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

**URL:** https://docs.shipany.ai/zh/guide/course#第二集对接-ai-接口实现壁纸生成完成业务功能开发

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

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/features/blog#配置博客路由

**Contents:**
- 博客
- 配置 CMS
- 管理博客内容
- 配置博客路由

ShipAny 内置一套 CMS 系统，用于博客内容管理，支持多语言。

为了能可视化管理博客内容，你需要 配置管理后台。

博客的标题和访问路由(slug)必填，默认支持多语言，需要选择对应的语言。

访问博客列表前台路由，可以看到在后台添加的博客内容。

默认的博客路由是 /posts，按照上述步骤添加博客内容后，你可以在 i18n/pages/landing 的 json 文件中添加导航项，显示博客列表的入口。

你需要添加自定义的文件夹，并参考 app/[locale]/(default)/posts 文件夹组织自定义的代码。

**Examples:**

Example 1 (unknown):
```unknown
CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    uuid VARCHAR(255) UNIQUE NOT NULL,
    slug VARCHAR(255),
    title VARCHAR(255),
    description TEXT,
    content TEXT,
    created_at timestamptz,
    updated_at timestamptz,
    status VARCHAR(50),
    cover_url VARCHAR(255),
    author_name VARCHAR(255),
    author_avatar_url VARCHAR(255),
    locale VARCHAR(50)
);
```

Example 2 (unknown):
```unknown
CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    uuid VARCHAR(255) UNIQUE NOT NULL,
    slug VARCHAR(255),
    title VARCHAR(255),
    description TEXT,
    content TEXT,
    created_at timestamptz,
    updated_at timestamptz,
    status VARCHAR(50),
    cover_url VARCHAR(255),
    author_name VARCHAR(255),
    author_avatar_url VARCHAR(255),
    locale VARCHAR(50)
);
```

Example 3 (unknown):
```unknown
https://{your-domain}/admin/posts
```

Example 4 (unknown):
```unknown
https://{your-domain}/admin/posts
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/features/storage#参考

**Contents:**
- 文件存储
- 配置云存储
- 上传 AI 图片到云存储
- 读取本地文件上传到云存储
- 下载远程图片上传到云存储
- 参考

ShipAny 支持上传文件到 AWS S3 兼容的文件存储系统，例如 AWS S3 / Cloudflare R2 / 腾讯云 COS 等。

选择你的云存储平台，创建存储桶，设置访问密钥和访问域名。

把 aisdk 生成的图片（返回的 base64 数据），上传到云存储。

uploadFile 接收的 body 参数是 Buffer 类型。你可以传递从 URL 下载的文件 Buffer 或者从本地文件读取的 Buffer。

注意：path 和 readFile 在 edge runtime 中无法使用，所以在 cloudflare 部署时，不能读取本地文件。

给定一个远程的图片地址，下载图片并上传到云存储。

**Examples:**

Example 1 (unknown):
```unknown
STORAGE_ENDPOINT = ""
STORAGE_REGION = ""
STORAGE_ACCESS_KEY = ""
STORAGE_SECRET_KEY = ""
STORAGE_BUCKET = ""
STORAGE_DOMAIN = ""
```

Example 2 (unknown):
```unknown
STORAGE_ENDPOINT = ""
STORAGE_REGION = ""
STORAGE_ACCESS_KEY = ""
STORAGE_SECRET_KEY = ""
STORAGE_BUCKET = ""
STORAGE_DOMAIN = ""
```

Example 3 (python):
```python
import { newStorage } from "@/lib/storage";
 
const storage = new Storage();
 
const filename = `image_${new Date().getTime()}.png`;
const key = `shipany/${filename}`;
const body = Buffer.from(image.base64, "base64");
 
try {
  const res = await storage.uploadFile({
    body,
    key,
    contentType: "image/png",
    disposition: "inline",
  });
 
  console.log("upload file success:", res);
} catch (err) {
  console.log("upload file failed:", err);
}
```

Example 4 (python):
```python
import { newStorage } from "@/lib/storage";
 
const storage = new Storage();
 
const filename = `image_${new Date().getTime()}.png`;
const key = `shipany/${filename}`;
const body = Buffer.from(image.base64, "base64");
 
try {
  const res = await storage.uploadFile({
    body,
    key,
    contentType: "image/png",
    disposition: "inline",
  });
 
  console.log("upload file success:", res);
} catch (err) {
  console.log("upload file failed:", err);
}
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/features/payment/creem#参考

**Contents:**
- Creem
- Creem 设置
- ShipAny 配置
- 价格表支付
  - 配置价格表内容
  - 修改价格表组件
  - 修改价格表下单逻辑
  - 修改支付回调逻辑
  - 修改支付通知逻辑
- 本地测试

ShipAny 支持使用 Creem 进行支付，可用于产品付款、会员订阅、购买积分等场景。

在 ShipAny 项目配置文件中，填写 Creem 相关的配置信息。

页面路径可以填相对路径，也可以填绝对路径。如果填的是相对路径，跳转时会自动拼接 NEXT_PUBLIC_WEB_URL 配置的网站地址，并带上多语言参数。

比如按照以上配置，在中文页面支付成功后的跳转路径是：http://localhost:3000/zh/my-orders

比如在 ShipAny 项目中设置的价格表有三个支付方案，对应的 product_id 分别是 starter、standard、premium，你需要在 Creem 后台为这三个方案 创建对应的产品，复制每个产品的 Product ID，与价格表中的 product_id 对应关系填写到 CREEM_PRODUCTS 中。

ShipAny 模板内置了一个价格表和对应的支付逻辑，你可以根据自己的需求，简单修改即可快速实现支付功能。

ShipAny 模板内置的价格表配置文件位于：src/i18n/pages/pricing 目录下，支持多语言，默认包含 en.json 和 zh.json 两个价格表配置文件。

你可以根据自己的需求，修改价格表配置文件中的内容。

默认的价格表组件位于：src/components/blocks/pricing/index.tsx

你可以根据自己的需求，修改价格表的展示形式。

默认的价格表下单逻辑位于：src/app/api/checkout/route.ts

你可以根据自己的需求，修改价格表的下单逻辑。

在价格表下单逻辑中，默认配置的支付回调地址是：/api/pay/callback/creem

用户支付后，会在浏览器跳转到这个地址，并带上包含支付信息的参数。

默认的支付回调处理逻辑位于：src/app/api/pay/callback/creem/route.ts

你可以根据自己的需求，修改处理支付回调的逻辑，比如更新订单状态、给用户发送邮件通知、给用户赠送积分等。

支付回调是同步逻辑，依赖浏览器跳转到回调地址，才能处理支付结果。这种方式不太可靠，可能出现跳转过程中用户关闭了浏览器等情况，导致支付结果没有被正常处理。 更可靠的方式是通过 Webhook，配置支付结果异步通知。

比如把 Webhook 地址配置为：https://your-domain.com/api/pay/notify/creem

用户支付后，Creem 会把支付信息推送到这个地址。

默认的支付通知逻辑位于：src/app/api/pay/notify/creem/route.ts

你可以根据自己的需求，修改处理支付通知的逻辑，比如更新订单状态、给用户发送邮件通知、给用户赠送积分等。

在 Creem 后台进入店铺，点击右上角的 Test mode，开启测试模式。

在测试模式下，进入开发者中心，设置 测试 API 密钥。

注册 ngrok 账号，按指示安装 ngrok 命令行工具。

启动 ngrok 服务，监听本地端口，并生成一个临时的域名。

在 Creem 后台测试模式中，配置 Webhook 地址为 ngrok 生成的域名

Endpoint 填写支付通知地址，比如 https://xxx.ngrok-free.app/api/pay/notify/creem。

添加 Webhook 地址后，在 Webhook 管理页面，复制 Signing secret，

跟支付密钥一起填入 .env.development 文件中。

在本地启动项目，访问 /pricing 页面，点击下单按钮，下单成功后跳转到支付页面。

使用 Stripe 测试卡 支付，支付成功后浏览器跳转到支付回调地址，监听的地址收到支付通知。

**Examples:**

Example 1 (unknown):
```unknown
NEXT_PUBLIC_WEB_URL = "http://localhost:3000"

NEXT_PUBLIC_PAY_SUCCESS_URL = "/my-orders"
NEXT_PUBLIC_PAY_FAIL_URL = "/pricing"
NEXT_PUBLIC_PAY_CANCEL_URL = "/pricing"

PAY_PROVIDER = "creem"

CREEM_ENV = "test"
CREEM_API_KEY = "creem_test_xxx"
CREEM_WEBHOOK_SECRET = "whsec_xxx"
CREEM_PRODUCTS = '{"starter": "prod_xxx", "standard": "prod_xxx", "premium": "prod_xxx"}'
```

Example 2 (unknown):
```unknown
NEXT_PUBLIC_WEB_URL = "http://localhost:3000"

NEXT_PUBLIC_PAY_SUCCESS_URL = "/my-orders"
NEXT_PUBLIC_PAY_FAIL_URL = "/pricing"
NEXT_PUBLIC_PAY_CANCEL_URL = "/pricing"

PAY_PROVIDER = "creem"

CREEM_ENV = "test"
CREEM_API_KEY = "creem_test_xxx"
CREEM_WEBHOOK_SECRET = "whsec_xxx"
CREEM_PRODUCTS = '{"starter": "prod_xxx", "standard": "prod_xxx", "premium": "prod_xxx"}'
```

Example 3 (unknown):
```unknown
{
  "pricing": {
    "name": "pricing",
    "label": "Pricing",
    "title": "Pricing",
    "description": "Get all features of ShipAny, Ship your AI SaaS startups fast.",
    "groups": [],
    "items": [
      {
        "title": "Starter",
        "description": "Get started with your first SaaS startup.",
        "features_title": "Includes",
        "features": [
          "100 credits, valid for 1 month",
          "NextJS boilerplate",
          "SEO-friendly structure",
          "Payment with Stripe",
          "Data storage with Supabase",
          "Google Oauth & One-Tap Login",
    
...
```

Example 4 (unknown):
```unknown
{
  "pricing": {
    "name": "pricing",
    "label": "Pricing",
    "title": "Pricing",
    "description": "Get all features of ShipAny, Ship your AI SaaS startups fast.",
    "groups": [],
    "items": [
      {
        "title": "Starter",
        "description": "Get started with your first SaaS startup.",
        "features_title": "Includes",
        "features": [
          "100 credits, valid for 1 month",
          "NextJS boilerplate",
          "SEO-friendly structure",
          "Payment with Stripe",
          "Data storage with Supabase",
          "Google Oauth & One-Tap Login",
    
...
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/features/oauth#生成-auth-secret

**Contents:**
- 登录鉴权
- 生成 Auth Secret
- 谷歌登录
- 谷歌一键登录
- Github 登录
- 登录预览
- 参考

ShipAny 目前支持 谷歌登录 / 谷歌一键登录 / Github 登录三种登录方式。

其他登录方式逐步集成，也可以参考 next-auth 文档自行接入。

生成一个 32 字节的随机字符串，作为 Auth Secret

修改环境变量中的 AUTH_SECRET 值

创建一个新项目，进入新项目的 Credentials 管理页面，创建 Oauth Client ID

创建 Oauth Client ID 后，得到 Client ID 和 Client Secret

首先按照谷歌登录的步骤，拿到 AUTH_GOOGLE_ID 和 AUTH_GOOGLE_SECRET

修改配置文件中的 NEXT_PUBLIC_AUTH_GOOGLE_ONE_TAP_ENABLED 和 NEXT_PUBLIC_AUTH_GOOGLE_ID

谷歌一键登录使用到的 NEXT_PUBLIC_AUTH_GOOGLE_ID 跟谷歌登录配置的 AUTH_GOOGLE_ID 保持一致。

开发环境和生产环境，需要创建两个不同的 OAuth app，分别配置不同的回调地址。

进入 OAuth app，复制 Client ID 和 Client Secret

修改配置文件中的 AUTH_GITHUB_ID 和 AUTH_GITHUB_SECRET

**Examples:**

Example 1 (unknown):
```unknown
openssl rand -base64 32
```

Example 2 (unknown):
```unknown
openssl rand -base64 32
```

Example 3 (unknown):
```unknown
AUTH_SECRET = "xxx"
```

Example 4 (unknown):
```unknown
AUTH_SECRET = "xxx"
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/features/analytics#谷歌数据统计

**Contents:**
- 数据统计
- 谷歌数据统计
- OpenPanel 统计
- 参考

目前数据统计仅支持 Google Analytics 和 OpenPanel。后续会逐步支持 Plausible 和 Umami 等统计工具。

注册 OpenPanel 账号，参考官网文档，创建统计实例

在实例的管理后台，创建一个统计客户端，得到 Client ID

**Examples:**

Example 1 (unknown):
```unknown
NEXT_PUBLIC_GOOGLE_ANALYTICS_ID = "G-1TPQYZXS53"
```

Example 2 (unknown):
```unknown
NEXT_PUBLIC_GOOGLE_ANALYTICS_ID = "G-1TPQYZXS53"
```

Example 3 (unknown):
```unknown
NEXT_PUBLIC_OPENPANEL_CLIENT_ID = "xxx-xxx-xxx-xxx"
```

Example 4 (unknown):
```unknown
NEXT_PUBLIC_OPENPANEL_CLIENT_ID = "xxx-xxx-xxx-xxx"
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/features/payment/stripe#价格表支付

**Contents:**
- Stripe
- Stripe 设置
- ShipAny 配置
- 价格表支付
  - 配置价格表内容
  - 修改价格表组件
  - 修改价格表下单逻辑
  - 修改支付回调逻辑
  - 修改支付通知逻辑
- 自定义支付

ShipAny 支持使用 Stripe 进行支付，可用于产品付款、会员订阅、购买积分等场景。

在 ShipAny 项目配置文件中，填写 Stripe 相关的配置信息。

页面路径可以填相对路径，也可以填绝对路径。如果填的是相对路径，跳转时会自动拼接 NEXT_PUBLIC_WEB_URL 配置的网站地址，并带上多语言参数。

比如按照以上配置，在中文页面支付成功后的跳转路径是：http://localhost:3000/zh/my-orders

ShipAny 模板内置了一个价格表和对应的支付逻辑，你可以根据自己的需求，简单修改即可快速实现支付功能。

ShipAny 模板内置的价格表配置文件位于：src/i18n/pages/pricing 目录下，支持多语言，默认包含 en.json 和 zh.json 两个价格表配置文件。

你可以根据自己的需求，修改价格表配置文件中的内容。

默认的价格表组件位于：src/components/blocks/pricing/index.tsx

你可以根据自己的需求，修改价格表的展示形式。

默认的价格表下单逻辑位于：src/app/api/checkout/route.ts

你可以根据自己的需求，修改价格表的下单逻辑。

在价格表下单逻辑中，默认配置的支付回调地址是：/api/pay/callback/stripe

用户支付后，会在浏览器跳转到这个地址，并带上包含支付信息的参数。

默认的支付回调处理逻辑位于：src/app/api/pay/callback/stripe/route.ts

你可以根据自己的需求，修改处理支付回调的逻辑，比如更新订单状态、给用户发送邮件通知、给用户赠送积分等。

支付回调是同步逻辑，依赖浏览器跳转到回调地址，才能处理支付结果。这种方式不太可靠，可能出现跳转过程中用户关闭了浏览器等情况，导致支付结果没有被正常处理。 更可靠的方式是通过 Webhook，配置支付结果异步通知。

比如把 Webhook 地址配置为：https://your-domain.com/api/pay/notify/stripe

用户支付后，Stripe 会把支付信息推送到这个地址。

默认的支付通知逻辑位于：src/app/api/pay/notify/stripe/route.ts

你可以根据自己的需求，修改处理支付通知的逻辑，比如更新订单状态、给用户发送邮件通知、给用户赠送积分等。

修改价格表配置文件，添加 groups 数据，配置多个价格分组。并在 pricing.items 下为每一个价格方案，设置一个 group 名称。

配置完成后，点击价格分组，将根据 group 字段，切换显示不同的价格方案。

ShipAny 模板使用 Stripe 支付时，默认支持三种支付方案

你只需要修改价格表配置，把每个价格方案的 interval 字段，设置成上述三个值之一。

同时，按需修改价格(amount) / 积分(credits) / 有效期(valid_months) 等字段。

举例：按月订阅扣费，月付 $99，购买后得到 30 个积分，有效期 1 个月，则核心的价格表配置信息为：

修改 src/app/api/checkout/route.ts 文件，设置 Stripe 下单的 options 参数。

在 Stripe 后台 设置支付方式，开通支付宝和微信支付。

修改价格表配置文件，在每个价格方案下添加一个 cn_amount 字段，即可支持人民币支付。

比如，产品售价，$99，人民币支付价格为 699 元，核心配置信息为：

配置完成后，在价格表下单按钮上方，将会显示一个人民币支付图标。

在 Stripe 后台点击左上角的店铺打开下拉菜单，依次点击 Switch to sandbox -> Test mode，开启测试模式。

在测试模式下，进入开发者中心，设置 测试支付密钥，包括 Publishable key 和 Secret key。

注册 ngrok 账号，按指示安装 ngrok 命令行工具。

启动 ngrok 服务，监听本地端口，并生成一个临时的域名。

在 Stripe 后台测试模式中，配置 Webhook 地址为 ngrok 生成的域名，并监听以下两个事件：

Endpoint 填写支付通知地址，比如 https://xxx.ngrok-free.app/api/pay/notify/stripe。

添加 Webhook 地址后，在 Webhook 管理页面，复制 Signing secret，

跟支付密钥一起填入 .env.development 文件中。

在本地启动项目，访问 /pricing 页面，点击下单按钮，下单成功后跳转到支付页面。

使用 Stripe 测试卡 支付，支付成功后浏览器跳转到支付回调地址，监听的地址收到支付通知。

**Examples:**

Example 1 (unknown):
```unknown
NEXT_PUBLIC_WEB_URL = "http://localhost:3000"

NEXT_PUBLIC_PAY_SUCCESS_URL = "/my-orders"
NEXT_PUBLIC_PAY_FAIL_URL = "/pricing"
NEXT_PUBLIC_PAY_CANCEL_URL = "/pricing"

PAY_PROVIDER = "stripe"

STRIPE_PUBLIC_KEY = "pk_test_xxx"
STRIPE_PRIVATE_KEY = "sk_test_xxx"
STRIPE_WEBHOOK_SECRET = "whsec_cexxx"
```

Example 2 (unknown):
```unknown
NEXT_PUBLIC_WEB_URL = "http://localhost:3000"

NEXT_PUBLIC_PAY_SUCCESS_URL = "/my-orders"
NEXT_PUBLIC_PAY_FAIL_URL = "/pricing"
NEXT_PUBLIC_PAY_CANCEL_URL = "/pricing"

PAY_PROVIDER = "stripe"

STRIPE_PUBLIC_KEY = "pk_test_xxx"
STRIPE_PRIVATE_KEY = "sk_test_xxx"
STRIPE_WEBHOOK_SECRET = "whsec_cexxx"
```

Example 3 (unknown):
```unknown
{
  "pricing": {
    "name": "pricing",
    "label": "Pricing",
    "title": "Pricing",
    "description": "Get all features of ShipAny, Ship your AI SaaS startups fast.",
    "groups": [],
    "items": [
      {
        "title": "Starter",
        "description": "Get started with your first SaaS startup.",
        "features_title": "Includes",
        "features": [
          "100 credits, valid for 1 month",
          "NextJS boilerplate",
          "SEO-friendly structure",
          "Payment with Stripe",
          "Data storage with Supabase",
          "Google Oauth & One-Tap Login",
    
...
```

Example 4 (unknown):
```unknown
{
  "pricing": {
    "name": "pricing",
    "label": "Pricing",
    "title": "Pricing",
    "description": "Get all features of ShipAny, Ship your AI SaaS startups fast.",
    "groups": [],
    "items": [
      {
        "title": "Starter",
        "description": "Get started with your first SaaS startup.",
        "features_title": "Includes",
        "features": [
          "100 credits, valid for 1 month",
          "NextJS boilerplate",
          "SEO-friendly structure",
          "Payment with Stripe",
          "Data storage with Supabase",
          "Google Oauth & One-Tap Login",
    
...
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/features/feedback#用户反馈组件

**Contents:**
- 用户反馈
- 用户反馈组件
- 如何使用

ShipAny 提供用户反馈组件，用于收集用户反馈。

用户反馈组件位于页面右下角，点击后会弹窗收集用户反馈。

**Examples:**

Example 1 (unknown):
```unknown
CREATE TABLE feedbacks (
    id SERIAL PRIMARY KEY,
    created_at timestamptz,
    status VARCHAR(50),
    user_uuid VARCHAR(255),
    content TEXT,
    rating INT
);
```

Example 2 (unknown):
```unknown
CREATE TABLE feedbacks (
    id SERIAL PRIMARY KEY,
    created_at timestamptz,
    status VARCHAR(50),
    user_uuid VARCHAR(255),
    content TEXT,
    rating INT
);
```

Example 3 (python):
```python
import Footer from "@/components/blocks/footer";
import Header from "@/components/blocks/header";
import { ReactNode } from "react";
import { getLandingPage } from "@/services/page";
import Feedback from "@/components/feedback";
 
export default async function DefaultLayout({
  children,
  params,
}: {
  children: ReactNode;
  params: Promise<{ locale: string }>;
}) {
  const { locale } = await params;
  const page = await getLandingPage(locale);
 
  return (
    <>
      {page.header && <Header header={page.header} />}
      <main className="overflow-x-hidden">{children}</main>
      {page.fo
...
```

Example 4 (python):
```python
import Footer from "@/components/blocks/footer";
import Header from "@/components/blocks/header";
import { ReactNode } from "react";
import { getLandingPage } from "@/services/page";
import Feedback from "@/components/feedback";
 
export default async function DefaultLayout({
  children,
  params,
}: {
  children: ReactNode;
  params: Promise<{ locale: string }>;
}) {
  const { locale } = await params;
  const page = await getLandingPage(locale);
 
  return (
    <>
      {page.header && <Header header={page.header} />}
      <main className="overflow-x-hidden">{children}</main>
      {page.fo
...
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/features/oauth#登录预览

**Contents:**
- 登录鉴权
- 生成 Auth Secret
- 谷歌登录
- 谷歌一键登录
- Github 登录
- 登录预览
- 参考

ShipAny 目前支持 谷歌登录 / 谷歌一键登录 / Github 登录三种登录方式。

其他登录方式逐步集成，也可以参考 next-auth 文档自行接入。

生成一个 32 字节的随机字符串，作为 Auth Secret

修改环境变量中的 AUTH_SECRET 值

创建一个新项目，进入新项目的 Credentials 管理页面，创建 Oauth Client ID

创建 Oauth Client ID 后，得到 Client ID 和 Client Secret

首先按照谷歌登录的步骤，拿到 AUTH_GOOGLE_ID 和 AUTH_GOOGLE_SECRET

修改配置文件中的 NEXT_PUBLIC_AUTH_GOOGLE_ONE_TAP_ENABLED 和 NEXT_PUBLIC_AUTH_GOOGLE_ID

谷歌一键登录使用到的 NEXT_PUBLIC_AUTH_GOOGLE_ID 跟谷歌登录配置的 AUTH_GOOGLE_ID 保持一致。

开发环境和生产环境，需要创建两个不同的 OAuth app，分别配置不同的回调地址。

进入 OAuth app，复制 Client ID 和 Client Secret

修改配置文件中的 AUTH_GITHUB_ID 和 AUTH_GITHUB_SECRET

**Examples:**

Example 1 (unknown):
```unknown
openssl rand -base64 32
```

Example 2 (unknown):
```unknown
openssl rand -base64 32
```

Example 3 (unknown):
```unknown
AUTH_SECRET = "xxx"
```

Example 4 (unknown):
```unknown
AUTH_SECRET = "xxx"
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/features/payment/stripe#配置价格表内容

**Contents:**
- Stripe
- Stripe 设置
- ShipAny 配置
- 价格表支付
  - 配置价格表内容
  - 修改价格表组件
  - 修改价格表下单逻辑
  - 修改支付回调逻辑
  - 修改支付通知逻辑
- 自定义支付

ShipAny 支持使用 Stripe 进行支付，可用于产品付款、会员订阅、购买积分等场景。

在 ShipAny 项目配置文件中，填写 Stripe 相关的配置信息。

页面路径可以填相对路径，也可以填绝对路径。如果填的是相对路径，跳转时会自动拼接 NEXT_PUBLIC_WEB_URL 配置的网站地址，并带上多语言参数。

比如按照以上配置，在中文页面支付成功后的跳转路径是：http://localhost:3000/zh/my-orders

ShipAny 模板内置了一个价格表和对应的支付逻辑，你可以根据自己的需求，简单修改即可快速实现支付功能。

ShipAny 模板内置的价格表配置文件位于：src/i18n/pages/pricing 目录下，支持多语言，默认包含 en.json 和 zh.json 两个价格表配置文件。

你可以根据自己的需求，修改价格表配置文件中的内容。

默认的价格表组件位于：src/components/blocks/pricing/index.tsx

你可以根据自己的需求，修改价格表的展示形式。

默认的价格表下单逻辑位于：src/app/api/checkout/route.ts

你可以根据自己的需求，修改价格表的下单逻辑。

在价格表下单逻辑中，默认配置的支付回调地址是：/api/pay/callback/stripe

用户支付后，会在浏览器跳转到这个地址，并带上包含支付信息的参数。

默认的支付回调处理逻辑位于：src/app/api/pay/callback/stripe/route.ts

你可以根据自己的需求，修改处理支付回调的逻辑，比如更新订单状态、给用户发送邮件通知、给用户赠送积分等。

支付回调是同步逻辑，依赖浏览器跳转到回调地址，才能处理支付结果。这种方式不太可靠，可能出现跳转过程中用户关闭了浏览器等情况，导致支付结果没有被正常处理。 更可靠的方式是通过 Webhook，配置支付结果异步通知。

比如把 Webhook 地址配置为：https://your-domain.com/api/pay/notify/stripe

用户支付后，Stripe 会把支付信息推送到这个地址。

默认的支付通知逻辑位于：src/app/api/pay/notify/stripe/route.ts

你可以根据自己的需求，修改处理支付通知的逻辑，比如更新订单状态、给用户发送邮件通知、给用户赠送积分等。

修改价格表配置文件，添加 groups 数据，配置多个价格分组。并在 pricing.items 下为每一个价格方案，设置一个 group 名称。

配置完成后，点击价格分组，将根据 group 字段，切换显示不同的价格方案。

ShipAny 模板使用 Stripe 支付时，默认支持三种支付方案

你只需要修改价格表配置，把每个价格方案的 interval 字段，设置成上述三个值之一。

同时，按需修改价格(amount) / 积分(credits) / 有效期(valid_months) 等字段。

举例：按月订阅扣费，月付 $99，购买后得到 30 个积分，有效期 1 个月，则核心的价格表配置信息为：

修改 src/app/api/checkout/route.ts 文件，设置 Stripe 下单的 options 参数。

在 Stripe 后台 设置支付方式，开通支付宝和微信支付。

修改价格表配置文件，在每个价格方案下添加一个 cn_amount 字段，即可支持人民币支付。

比如，产品售价，$99，人民币支付价格为 699 元，核心配置信息为：

配置完成后，在价格表下单按钮上方，将会显示一个人民币支付图标。

在 Stripe 后台点击左上角的店铺打开下拉菜单，依次点击 Switch to sandbox -> Test mode，开启测试模式。

在测试模式下，进入开发者中心，设置 测试支付密钥，包括 Publishable key 和 Secret key。

注册 ngrok 账号，按指示安装 ngrok 命令行工具。

启动 ngrok 服务，监听本地端口，并生成一个临时的域名。

在 Stripe 后台测试模式中，配置 Webhook 地址为 ngrok 生成的域名，并监听以下两个事件：

Endpoint 填写支付通知地址，比如 https://xxx.ngrok-free.app/api/pay/notify/stripe。

添加 Webhook 地址后，在 Webhook 管理页面，复制 Signing secret，

跟支付密钥一起填入 .env.development 文件中。

在本地启动项目，访问 /pricing 页面，点击下单按钮，下单成功后跳转到支付页面。

使用 Stripe 测试卡 支付，支付成功后浏览器跳转到支付回调地址，监听的地址收到支付通知。

**Examples:**

Example 1 (unknown):
```unknown
NEXT_PUBLIC_WEB_URL = "http://localhost:3000"

NEXT_PUBLIC_PAY_SUCCESS_URL = "/my-orders"
NEXT_PUBLIC_PAY_FAIL_URL = "/pricing"
NEXT_PUBLIC_PAY_CANCEL_URL = "/pricing"

PAY_PROVIDER = "stripe"

STRIPE_PUBLIC_KEY = "pk_test_xxx"
STRIPE_PRIVATE_KEY = "sk_test_xxx"
STRIPE_WEBHOOK_SECRET = "whsec_cexxx"
```

Example 2 (unknown):
```unknown
NEXT_PUBLIC_WEB_URL = "http://localhost:3000"

NEXT_PUBLIC_PAY_SUCCESS_URL = "/my-orders"
NEXT_PUBLIC_PAY_FAIL_URL = "/pricing"
NEXT_PUBLIC_PAY_CANCEL_URL = "/pricing"

PAY_PROVIDER = "stripe"

STRIPE_PUBLIC_KEY = "pk_test_xxx"
STRIPE_PRIVATE_KEY = "sk_test_xxx"
STRIPE_WEBHOOK_SECRET = "whsec_cexxx"
```

Example 3 (unknown):
```unknown
{
  "pricing": {
    "name": "pricing",
    "label": "Pricing",
    "title": "Pricing",
    "description": "Get all features of ShipAny, Ship your AI SaaS startups fast.",
    "groups": [],
    "items": [
      {
        "title": "Starter",
        "description": "Get started with your first SaaS startup.",
        "features_title": "Includes",
        "features": [
          "100 credits, valid for 1 month",
          "NextJS boilerplate",
          "SEO-friendly structure",
          "Payment with Stripe",
          "Data storage with Supabase",
          "Google Oauth & One-Tap Login",
    
...
```

Example 4 (unknown):
```unknown
{
  "pricing": {
    "name": "pricing",
    "label": "Pricing",
    "title": "Pricing",
    "description": "Get all features of ShipAny, Ship your AI SaaS startups fast.",
    "groups": [],
    "items": [
      {
        "title": "Starter",
        "description": "Get started with your first SaaS startup.",
        "features_title": "Includes",
        "features": [
          "100 credits, valid for 1 month",
          "NextJS boilerplate",
          "SEO-friendly structure",
          "Payment with Stripe",
          "Data storage with Supabase",
          "Google Oauth & One-Tap Login",
    
...
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/features/oauth

**Contents:**
- 登录鉴权
- 生成 Auth Secret
- 谷歌登录
- 谷歌一键登录
- Github 登录
- 登录预览
- 参考

ShipAny 目前支持 谷歌登录 / 谷歌一键登录 / Github 登录三种登录方式。

其他登录方式逐步集成，也可以参考 next-auth 文档自行接入。

生成一个 32 字节的随机字符串，作为 Auth Secret

修改环境变量中的 AUTH_SECRET 值

创建一个新项目，进入新项目的 Credentials 管理页面，创建 Oauth Client ID

创建 Oauth Client ID 后，得到 Client ID 和 Client Secret

首先按照谷歌登录的步骤，拿到 AUTH_GOOGLE_ID 和 AUTH_GOOGLE_SECRET

修改配置文件中的 NEXT_PUBLIC_AUTH_GOOGLE_ONE_TAP_ENABLED 和 NEXT_PUBLIC_AUTH_GOOGLE_ID

谷歌一键登录使用到的 NEXT_PUBLIC_AUTH_GOOGLE_ID 跟谷歌登录配置的 AUTH_GOOGLE_ID 保持一致。

开发环境和生产环境，需要创建两个不同的 OAuth app，分别配置不同的回调地址。

进入 OAuth app，复制 Client ID 和 Client Secret

修改配置文件中的 AUTH_GITHUB_ID 和 AUTH_GITHUB_SECRET

**Examples:**

Example 1 (unknown):
```unknown
openssl rand -base64 32
```

Example 2 (unknown):
```unknown
openssl rand -base64 32
```

Example 3 (unknown):
```unknown
AUTH_SECRET = "xxx"
```

Example 4 (unknown):
```unknown
AUTH_SECRET = "xxx"
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/features/payment/creem#修改价格表下单逻辑

**Contents:**
- Creem
- Creem 设置
- ShipAny 配置
- 价格表支付
  - 配置价格表内容
  - 修改价格表组件
  - 修改价格表下单逻辑
  - 修改支付回调逻辑
  - 修改支付通知逻辑
- 本地测试

ShipAny 支持使用 Creem 进行支付，可用于产品付款、会员订阅、购买积分等场景。

在 ShipAny 项目配置文件中，填写 Creem 相关的配置信息。

页面路径可以填相对路径，也可以填绝对路径。如果填的是相对路径，跳转时会自动拼接 NEXT_PUBLIC_WEB_URL 配置的网站地址，并带上多语言参数。

比如按照以上配置，在中文页面支付成功后的跳转路径是：http://localhost:3000/zh/my-orders

比如在 ShipAny 项目中设置的价格表有三个支付方案，对应的 product_id 分别是 starter、standard、premium，你需要在 Creem 后台为这三个方案 创建对应的产品，复制每个产品的 Product ID，与价格表中的 product_id 对应关系填写到 CREEM_PRODUCTS 中。

ShipAny 模板内置了一个价格表和对应的支付逻辑，你可以根据自己的需求，简单修改即可快速实现支付功能。

ShipAny 模板内置的价格表配置文件位于：src/i18n/pages/pricing 目录下，支持多语言，默认包含 en.json 和 zh.json 两个价格表配置文件。

你可以根据自己的需求，修改价格表配置文件中的内容。

默认的价格表组件位于：src/components/blocks/pricing/index.tsx

你可以根据自己的需求，修改价格表的展示形式。

默认的价格表下单逻辑位于：src/app/api/checkout/route.ts

你可以根据自己的需求，修改价格表的下单逻辑。

在价格表下单逻辑中，默认配置的支付回调地址是：/api/pay/callback/creem

用户支付后，会在浏览器跳转到这个地址，并带上包含支付信息的参数。

默认的支付回调处理逻辑位于：src/app/api/pay/callback/creem/route.ts

你可以根据自己的需求，修改处理支付回调的逻辑，比如更新订单状态、给用户发送邮件通知、给用户赠送积分等。

支付回调是同步逻辑，依赖浏览器跳转到回调地址，才能处理支付结果。这种方式不太可靠，可能出现跳转过程中用户关闭了浏览器等情况，导致支付结果没有被正常处理。 更可靠的方式是通过 Webhook，配置支付结果异步通知。

比如把 Webhook 地址配置为：https://your-domain.com/api/pay/notify/creem

用户支付后，Creem 会把支付信息推送到这个地址。

默认的支付通知逻辑位于：src/app/api/pay/notify/creem/route.ts

你可以根据自己的需求，修改处理支付通知的逻辑，比如更新订单状态、给用户发送邮件通知、给用户赠送积分等。

在 Creem 后台进入店铺，点击右上角的 Test mode，开启测试模式。

在测试模式下，进入开发者中心，设置 测试 API 密钥。

注册 ngrok 账号，按指示安装 ngrok 命令行工具。

启动 ngrok 服务，监听本地端口，并生成一个临时的域名。

在 Creem 后台测试模式中，配置 Webhook 地址为 ngrok 生成的域名

Endpoint 填写支付通知地址，比如 https://xxx.ngrok-free.app/api/pay/notify/creem。

添加 Webhook 地址后，在 Webhook 管理页面，复制 Signing secret，

跟支付密钥一起填入 .env.development 文件中。

在本地启动项目，访问 /pricing 页面，点击下单按钮，下单成功后跳转到支付页面。

使用 Stripe 测试卡 支付，支付成功后浏览器跳转到支付回调地址，监听的地址收到支付通知。

**Examples:**

Example 1 (unknown):
```unknown
NEXT_PUBLIC_WEB_URL = "http://localhost:3000"

NEXT_PUBLIC_PAY_SUCCESS_URL = "/my-orders"
NEXT_PUBLIC_PAY_FAIL_URL = "/pricing"
NEXT_PUBLIC_PAY_CANCEL_URL = "/pricing"

PAY_PROVIDER = "creem"

CREEM_ENV = "test"
CREEM_API_KEY = "creem_test_xxx"
CREEM_WEBHOOK_SECRET = "whsec_xxx"
CREEM_PRODUCTS = '{"starter": "prod_xxx", "standard": "prod_xxx", "premium": "prod_xxx"}'
```

Example 2 (unknown):
```unknown
NEXT_PUBLIC_WEB_URL = "http://localhost:3000"

NEXT_PUBLIC_PAY_SUCCESS_URL = "/my-orders"
NEXT_PUBLIC_PAY_FAIL_URL = "/pricing"
NEXT_PUBLIC_PAY_CANCEL_URL = "/pricing"

PAY_PROVIDER = "creem"

CREEM_ENV = "test"
CREEM_API_KEY = "creem_test_xxx"
CREEM_WEBHOOK_SECRET = "whsec_xxx"
CREEM_PRODUCTS = '{"starter": "prod_xxx", "standard": "prod_xxx", "premium": "prod_xxx"}'
```

Example 3 (unknown):
```unknown
{
  "pricing": {
    "name": "pricing",
    "label": "Pricing",
    "title": "Pricing",
    "description": "Get all features of ShipAny, Ship your AI SaaS startups fast.",
    "groups": [],
    "items": [
      {
        "title": "Starter",
        "description": "Get started with your first SaaS startup.",
        "features_title": "Includes",
        "features": [
          "100 credits, valid for 1 month",
          "NextJS boilerplate",
          "SEO-friendly structure",
          "Payment with Stripe",
          "Data storage with Supabase",
          "Google Oauth & One-Tap Login",
    
...
```

Example 4 (unknown):
```unknown
{
  "pricing": {
    "name": "pricing",
    "label": "Pricing",
    "title": "Pricing",
    "description": "Get all features of ShipAny, Ship your AI SaaS startups fast.",
    "groups": [],
    "items": [
      {
        "title": "Starter",
        "description": "Get started with your first SaaS startup.",
        "features_title": "Includes",
        "features": [
          "100 credits, valid for 1 month",
          "NextJS boilerplate",
          "SEO-friendly structure",
          "Payment with Stripe",
          "Data storage with Supabase",
          "Google Oauth & One-Tap Login",
    
...
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/features/email/resend

**Contents:**
- Resend
- Resend 设置
- ShipAny 配置
- 发送邮件
  - 发送文本邮件
  - 发送 HTML 邮件
  - 发送模板邮件
  - 使用 React Email
- 参考

ShipAny 支持使用 Resend 发送邮件，可用于发送邮件验证码、发送支付通知、发送营销邮件等场景。

在 Resend 后台 添加域名，设置 DNS 记录，验证域名

在 Resend 后台 创建 API 密钥，并复制 API 密钥

在 ShipAny 项目配置文件中，填写 Resend 相关的配置信息。

比如在 Resend 后台配置的邮件域名是 mail.shipany.ai，则发件人邮箱可以配置为 [email protected] / [email protected] / [email protected] 等。

在需要发邮件的地方，根据具体场景，选择合适的发送方式。

React Email 内置大量邮件组件，可以让你更轻松创建邮件模板。

比如在 @/components/email-templates/react-email.tsx 中写入内容：

除了自己实现邮件模板，你也可以在 React Email 模板市场 选择一个模板，修改后直接使用。

**Examples:**

Example 1 (unknown):
```unknown
RESEND_API_KEY = "re_xxx"
RESEND_SENDER_EMAIL = "[email protected]"
```

Example 2 (unknown):
```unknown
RESEND_API_KEY = "re_xxx"
RESEND_SENDER_EMAIL = "[email protected]"
```

Example 3 (python):
```python
import { Resend } from "resend";
 
const resend = new Resend(process.env.RESEND_API_KEY!);
 
const result = await resend.emails.send({
  from: process.env.RESEND_SENDER_EMAIL!,
  to: ["[email protected]"],
  subject: "Hello from ShipAny with Resend",
  text: "Hello World.",
});
 
console.log("send email result", result);
```

Example 4 (python):
```python
import { Resend } from "resend";
 
const resend = new Resend(process.env.RESEND_API_KEY!);
 
const result = await resend.emails.send({
  from: process.env.RESEND_SENDER_EMAIL!,
  to: ["[email protected]"],
  subject: "Hello from ShipAny with Resend",
  text: "Hello World.",
});
 
console.log("send email result", result);
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/features/email/resend#使用-react-email

**Contents:**
- Resend
- Resend 设置
- ShipAny 配置
- 发送邮件
  - 发送文本邮件
  - 发送 HTML 邮件
  - 发送模板邮件
  - 使用 React Email
- 参考

ShipAny 支持使用 Resend 发送邮件，可用于发送邮件验证码、发送支付通知、发送营销邮件等场景。

在 Resend 后台 添加域名，设置 DNS 记录，验证域名

在 Resend 后台 创建 API 密钥，并复制 API 密钥

在 ShipAny 项目配置文件中，填写 Resend 相关的配置信息。

比如在 Resend 后台配置的邮件域名是 mail.shipany.ai，则发件人邮箱可以配置为 [email protected] / [email protected] / [email protected] 等。

在需要发邮件的地方，根据具体场景，选择合适的发送方式。

React Email 内置大量邮件组件，可以让你更轻松创建邮件模板。

比如在 @/components/email-templates/react-email.tsx 中写入内容：

除了自己实现邮件模板，你也可以在 React Email 模板市场 选择一个模板，修改后直接使用。

**Examples:**

Example 1 (unknown):
```unknown
RESEND_API_KEY = "re_xxx"
RESEND_SENDER_EMAIL = "[email protected]"
```

Example 2 (unknown):
```unknown
RESEND_API_KEY = "re_xxx"
RESEND_SENDER_EMAIL = "[email protected]"
```

Example 3 (python):
```python
import { Resend } from "resend";
 
const resend = new Resend(process.env.RESEND_API_KEY!);
 
const result = await resend.emails.send({
  from: process.env.RESEND_SENDER_EMAIL!,
  to: ["[email protected]"],
  subject: "Hello from ShipAny with Resend",
  text: "Hello World.",
});
 
console.log("send email result", result);
```

Example 4 (python):
```python
import { Resend } from "resend";
 
const resend = new Resend(process.env.RESEND_API_KEY!);
 
const result = await resend.emails.send({
  from: process.env.RESEND_SENDER_EMAIL!,
  to: ["[email protected]"],
  subject: "Hello from ShipAny with Resend",
  text: "Hello World.",
});
 
console.log("send email result", result);
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/features/payment/creem#修改支付通知逻辑

**Contents:**
- Creem
- Creem 设置
- ShipAny 配置
- 价格表支付
  - 配置价格表内容
  - 修改价格表组件
  - 修改价格表下单逻辑
  - 修改支付回调逻辑
  - 修改支付通知逻辑
- 本地测试

ShipAny 支持使用 Creem 进行支付，可用于产品付款、会员订阅、购买积分等场景。

在 ShipAny 项目配置文件中，填写 Creem 相关的配置信息。

页面路径可以填相对路径，也可以填绝对路径。如果填的是相对路径，跳转时会自动拼接 NEXT_PUBLIC_WEB_URL 配置的网站地址，并带上多语言参数。

比如按照以上配置，在中文页面支付成功后的跳转路径是：http://localhost:3000/zh/my-orders

比如在 ShipAny 项目中设置的价格表有三个支付方案，对应的 product_id 分别是 starter、standard、premium，你需要在 Creem 后台为这三个方案 创建对应的产品，复制每个产品的 Product ID，与价格表中的 product_id 对应关系填写到 CREEM_PRODUCTS 中。

ShipAny 模板内置了一个价格表和对应的支付逻辑，你可以根据自己的需求，简单修改即可快速实现支付功能。

ShipAny 模板内置的价格表配置文件位于：src/i18n/pages/pricing 目录下，支持多语言，默认包含 en.json 和 zh.json 两个价格表配置文件。

你可以根据自己的需求，修改价格表配置文件中的内容。

默认的价格表组件位于：src/components/blocks/pricing/index.tsx

你可以根据自己的需求，修改价格表的展示形式。

默认的价格表下单逻辑位于：src/app/api/checkout/route.ts

你可以根据自己的需求，修改价格表的下单逻辑。

在价格表下单逻辑中，默认配置的支付回调地址是：/api/pay/callback/creem

用户支付后，会在浏览器跳转到这个地址，并带上包含支付信息的参数。

默认的支付回调处理逻辑位于：src/app/api/pay/callback/creem/route.ts

你可以根据自己的需求，修改处理支付回调的逻辑，比如更新订单状态、给用户发送邮件通知、给用户赠送积分等。

支付回调是同步逻辑，依赖浏览器跳转到回调地址，才能处理支付结果。这种方式不太可靠，可能出现跳转过程中用户关闭了浏览器等情况，导致支付结果没有被正常处理。 更可靠的方式是通过 Webhook，配置支付结果异步通知。

比如把 Webhook 地址配置为：https://your-domain.com/api/pay/notify/creem

用户支付后，Creem 会把支付信息推送到这个地址。

默认的支付通知逻辑位于：src/app/api/pay/notify/creem/route.ts

你可以根据自己的需求，修改处理支付通知的逻辑，比如更新订单状态、给用户发送邮件通知、给用户赠送积分等。

在 Creem 后台进入店铺，点击右上角的 Test mode，开启测试模式。

在测试模式下，进入开发者中心，设置 测试 API 密钥。

注册 ngrok 账号，按指示安装 ngrok 命令行工具。

启动 ngrok 服务，监听本地端口，并生成一个临时的域名。

在 Creem 后台测试模式中，配置 Webhook 地址为 ngrok 生成的域名

Endpoint 填写支付通知地址，比如 https://xxx.ngrok-free.app/api/pay/notify/creem。

添加 Webhook 地址后，在 Webhook 管理页面，复制 Signing secret，

跟支付密钥一起填入 .env.development 文件中。

在本地启动项目，访问 /pricing 页面，点击下单按钮，下单成功后跳转到支付页面。

使用 Stripe 测试卡 支付，支付成功后浏览器跳转到支付回调地址，监听的地址收到支付通知。

**Examples:**

Example 1 (unknown):
```unknown
NEXT_PUBLIC_WEB_URL = "http://localhost:3000"

NEXT_PUBLIC_PAY_SUCCESS_URL = "/my-orders"
NEXT_PUBLIC_PAY_FAIL_URL = "/pricing"
NEXT_PUBLIC_PAY_CANCEL_URL = "/pricing"

PAY_PROVIDER = "creem"

CREEM_ENV = "test"
CREEM_API_KEY = "creem_test_xxx"
CREEM_WEBHOOK_SECRET = "whsec_xxx"
CREEM_PRODUCTS = '{"starter": "prod_xxx", "standard": "prod_xxx", "premium": "prod_xxx"}'
```

Example 2 (unknown):
```unknown
NEXT_PUBLIC_WEB_URL = "http://localhost:3000"

NEXT_PUBLIC_PAY_SUCCESS_URL = "/my-orders"
NEXT_PUBLIC_PAY_FAIL_URL = "/pricing"
NEXT_PUBLIC_PAY_CANCEL_URL = "/pricing"

PAY_PROVIDER = "creem"

CREEM_ENV = "test"
CREEM_API_KEY = "creem_test_xxx"
CREEM_WEBHOOK_SECRET = "whsec_xxx"
CREEM_PRODUCTS = '{"starter": "prod_xxx", "standard": "prod_xxx", "premium": "prod_xxx"}'
```

Example 3 (unknown):
```unknown
{
  "pricing": {
    "name": "pricing",
    "label": "Pricing",
    "title": "Pricing",
    "description": "Get all features of ShipAny, Ship your AI SaaS startups fast.",
    "groups": [],
    "items": [
      {
        "title": "Starter",
        "description": "Get started with your first SaaS startup.",
        "features_title": "Includes",
        "features": [
          "100 credits, valid for 1 month",
          "NextJS boilerplate",
          "SEO-friendly structure",
          "Payment with Stripe",
          "Data storage with Supabase",
          "Google Oauth & One-Tap Login",
    
...
```

Example 4 (unknown):
```unknown
{
  "pricing": {
    "name": "pricing",
    "label": "Pricing",
    "title": "Pricing",
    "description": "Get all features of ShipAny, Ship your AI SaaS startups fast.",
    "groups": [],
    "items": [
      {
        "title": "Starter",
        "description": "Get started with your first SaaS startup.",
        "features_title": "Includes",
        "features": [
          "100 credits, valid for 1 month",
          "NextJS boilerplate",
          "SEO-friendly structure",
          "Payment with Stripe",
          "Data storage with Supabase",
          "Google Oauth & One-Tap Login",
    
...
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/features/analytics

**Contents:**
- 数据统计
- 谷歌数据统计
- OpenPanel 统计
- 参考

目前数据统计仅支持 Google Analytics 和 OpenPanel。后续会逐步支持 Plausible 和 Umami 等统计工具。

注册 OpenPanel 账号，参考官网文档，创建统计实例

在实例的管理后台，创建一个统计客户端，得到 Client ID

**Examples:**

Example 1 (unknown):
```unknown
NEXT_PUBLIC_GOOGLE_ANALYTICS_ID = "G-1TPQYZXS53"
```

Example 2 (unknown):
```unknown
NEXT_PUBLIC_GOOGLE_ANALYTICS_ID = "G-1TPQYZXS53"
```

Example 3 (unknown):
```unknown
NEXT_PUBLIC_OPENPANEL_CLIENT_ID = "xxx-xxx-xxx-xxx"
```

Example 4 (unknown):
```unknown
NEXT_PUBLIC_OPENPANEL_CLIENT_ID = "xxx-xxx-xxx-xxx"
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/features/payment/creem#配置价格表内容

**Contents:**
- Creem
- Creem 设置
- ShipAny 配置
- 价格表支付
  - 配置价格表内容
  - 修改价格表组件
  - 修改价格表下单逻辑
  - 修改支付回调逻辑
  - 修改支付通知逻辑
- 本地测试

ShipAny 支持使用 Creem 进行支付，可用于产品付款、会员订阅、购买积分等场景。

在 ShipAny 项目配置文件中，填写 Creem 相关的配置信息。

页面路径可以填相对路径，也可以填绝对路径。如果填的是相对路径，跳转时会自动拼接 NEXT_PUBLIC_WEB_URL 配置的网站地址，并带上多语言参数。

比如按照以上配置，在中文页面支付成功后的跳转路径是：http://localhost:3000/zh/my-orders

比如在 ShipAny 项目中设置的价格表有三个支付方案，对应的 product_id 分别是 starter、standard、premium，你需要在 Creem 后台为这三个方案 创建对应的产品，复制每个产品的 Product ID，与价格表中的 product_id 对应关系填写到 CREEM_PRODUCTS 中。

ShipAny 模板内置了一个价格表和对应的支付逻辑，你可以根据自己的需求，简单修改即可快速实现支付功能。

ShipAny 模板内置的价格表配置文件位于：src/i18n/pages/pricing 目录下，支持多语言，默认包含 en.json 和 zh.json 两个价格表配置文件。

你可以根据自己的需求，修改价格表配置文件中的内容。

默认的价格表组件位于：src/components/blocks/pricing/index.tsx

你可以根据自己的需求，修改价格表的展示形式。

默认的价格表下单逻辑位于：src/app/api/checkout/route.ts

你可以根据自己的需求，修改价格表的下单逻辑。

在价格表下单逻辑中，默认配置的支付回调地址是：/api/pay/callback/creem

用户支付后，会在浏览器跳转到这个地址，并带上包含支付信息的参数。

默认的支付回调处理逻辑位于：src/app/api/pay/callback/creem/route.ts

你可以根据自己的需求，修改处理支付回调的逻辑，比如更新订单状态、给用户发送邮件通知、给用户赠送积分等。

支付回调是同步逻辑，依赖浏览器跳转到回调地址，才能处理支付结果。这种方式不太可靠，可能出现跳转过程中用户关闭了浏览器等情况，导致支付结果没有被正常处理。 更可靠的方式是通过 Webhook，配置支付结果异步通知。

比如把 Webhook 地址配置为：https://your-domain.com/api/pay/notify/creem

用户支付后，Creem 会把支付信息推送到这个地址。

默认的支付通知逻辑位于：src/app/api/pay/notify/creem/route.ts

你可以根据自己的需求，修改处理支付通知的逻辑，比如更新订单状态、给用户发送邮件通知、给用户赠送积分等。

在 Creem 后台进入店铺，点击右上角的 Test mode，开启测试模式。

在测试模式下，进入开发者中心，设置 测试 API 密钥。

注册 ngrok 账号，按指示安装 ngrok 命令行工具。

启动 ngrok 服务，监听本地端口，并生成一个临时的域名。

在 Creem 后台测试模式中，配置 Webhook 地址为 ngrok 生成的域名

Endpoint 填写支付通知地址，比如 https://xxx.ngrok-free.app/api/pay/notify/creem。

添加 Webhook 地址后，在 Webhook 管理页面，复制 Signing secret，

跟支付密钥一起填入 .env.development 文件中。

在本地启动项目，访问 /pricing 页面，点击下单按钮，下单成功后跳转到支付页面。

使用 Stripe 测试卡 支付，支付成功后浏览器跳转到支付回调地址，监听的地址收到支付通知。

**Examples:**

Example 1 (unknown):
```unknown
NEXT_PUBLIC_WEB_URL = "http://localhost:3000"

NEXT_PUBLIC_PAY_SUCCESS_URL = "/my-orders"
NEXT_PUBLIC_PAY_FAIL_URL = "/pricing"
NEXT_PUBLIC_PAY_CANCEL_URL = "/pricing"

PAY_PROVIDER = "creem"

CREEM_ENV = "test"
CREEM_API_KEY = "creem_test_xxx"
CREEM_WEBHOOK_SECRET = "whsec_xxx"
CREEM_PRODUCTS = '{"starter": "prod_xxx", "standard": "prod_xxx", "premium": "prod_xxx"}'
```

Example 2 (unknown):
```unknown
NEXT_PUBLIC_WEB_URL = "http://localhost:3000"

NEXT_PUBLIC_PAY_SUCCESS_URL = "/my-orders"
NEXT_PUBLIC_PAY_FAIL_URL = "/pricing"
NEXT_PUBLIC_PAY_CANCEL_URL = "/pricing"

PAY_PROVIDER = "creem"

CREEM_ENV = "test"
CREEM_API_KEY = "creem_test_xxx"
CREEM_WEBHOOK_SECRET = "whsec_xxx"
CREEM_PRODUCTS = '{"starter": "prod_xxx", "standard": "prod_xxx", "premium": "prod_xxx"}'
```

Example 3 (unknown):
```unknown
{
  "pricing": {
    "name": "pricing",
    "label": "Pricing",
    "title": "Pricing",
    "description": "Get all features of ShipAny, Ship your AI SaaS startups fast.",
    "groups": [],
    "items": [
      {
        "title": "Starter",
        "description": "Get started with your first SaaS startup.",
        "features_title": "Includes",
        "features": [
          "100 credits, valid for 1 month",
          "NextJS boilerplate",
          "SEO-friendly structure",
          "Payment with Stripe",
          "Data storage with Supabase",
          "Google Oauth & One-Tap Login",
    
...
```

Example 4 (unknown):
```unknown
{
  "pricing": {
    "name": "pricing",
    "label": "Pricing",
    "title": "Pricing",
    "description": "Get all features of ShipAny, Ship your AI SaaS startups fast.",
    "groups": [],
    "items": [
      {
        "title": "Starter",
        "description": "Get started with your first SaaS startup.",
        "features_title": "Includes",
        "features": [
          "100 credits, valid for 1 month",
          "NextJS boilerplate",
          "SEO-friendly structure",
          "Payment with Stripe",
          "Data storage with Supabase",
          "Google Oauth & One-Tap Login",
    
...
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/features/seo

**Contents:**
- SEO
- 设置多语言文案
- 设置站点地图
- 网页 SEO 走查
- Metadata 配置
- 接入 GSC

ShipAny 做了很多 SEO 优化，可以让你的项目在搜索引擎中获得更好的排名。

在 i18n/messages 目录下，通过 [locale].json 文件配置页面内容，默认支持中文和英文，在 i18n/messages/ 目录下，可以看到 en.json 和 zh.json 两个文件，在项目发布之前，修改成跟你项目相符合的文案即可。

修改 public/sitemap.xml 文件，配置成你自己的站点信息

按需修改 public/robots.txt 内容

检查网站首页的 title / description / Canonical 是否合理

用 AI 辅助修改 i18n/pages/landing 下 json 文件对应的网页内容，调整网站主打的关键词密度。(3% 左右比较合理)

ShipAny 对默认的 landing page 做了内容结构优化。如果你有自定义页面组件，需要检查页面的结构是否合理。

在 AITDK 插件的 Issues 面板开启 SSR Check，检测网页是否是服务端渲染。

如果你有创建新的页面路由 (page.tsx)，可以配置一下新页面的 Metadata 信息。

为子页面设置独立的 title / description / canonical 信息，有利于 SEO。

网站上站后，在 Google Search Console 中添加你的站点，可以查看网站的搜索流量和排名情况。

**Examples:**

Example 1 (unknown):
```unknown
update content of this file, for my new project "Flux AI", which is an AI Image Generator, with keywords "flux ai, ai image generator"
```

Example 2 (unknown):
```unknown
update content of this file, for my new project "Flux AI", which is an AI Image Generator, with keywords "flux ai, ai image generator"
```

Example 3 (unknown):
```unknown
<?xml version='1.0' encoding='utf-8' standalone='yes'?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://shipany.ai/</loc>
    <lastmod>2024-12-24T10:00:00+00:00</lastmod>
  </url>
</urlset>
```

Example 4 (unknown):
```unknown
<?xml version='1.0' encoding='utf-8' standalone='yes'?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://shipany.ai/</loc>
    <lastmod>2024-12-24T10:00:00+00:00</lastmod>
  </url>
</urlset>
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/features/blog

**Contents:**
- 博客
- 配置 CMS
- 管理博客内容
- 配置博客路由

ShipAny 内置一套 CMS 系统，用于博客内容管理，支持多语言。

为了能可视化管理博客内容，你需要 配置管理后台。

博客的标题和访问路由(slug)必填，默认支持多语言，需要选择对应的语言。

访问博客列表前台路由，可以看到在后台添加的博客内容。

默认的博客路由是 /posts，按照上述步骤添加博客内容后，你可以在 i18n/pages/landing 的 json 文件中添加导航项，显示博客列表的入口。

你需要添加自定义的文件夹，并参考 app/[locale]/(default)/posts 文件夹组织自定义的代码。

**Examples:**

Example 1 (unknown):
```unknown
CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    uuid VARCHAR(255) UNIQUE NOT NULL,
    slug VARCHAR(255),
    title VARCHAR(255),
    description TEXT,
    content TEXT,
    created_at timestamptz,
    updated_at timestamptz,
    status VARCHAR(50),
    cover_url VARCHAR(255),
    author_name VARCHAR(255),
    author_avatar_url VARCHAR(255),
    locale VARCHAR(50)
);
```

Example 2 (unknown):
```unknown
CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    uuid VARCHAR(255) UNIQUE NOT NULL,
    slug VARCHAR(255),
    title VARCHAR(255),
    description TEXT,
    content TEXT,
    created_at timestamptz,
    updated_at timestamptz,
    status VARCHAR(50),
    cover_url VARCHAR(255),
    author_name VARCHAR(255),
    author_avatar_url VARCHAR(255),
    locale VARCHAR(50)
);
```

Example 3 (unknown):
```unknown
https://{your-domain}/admin/posts
```

Example 4 (unknown):
```unknown
https://{your-domain}/admin/posts
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/features/email/resend#resend-设置

**Contents:**
- Resend
- Resend 设置
- ShipAny 配置
- 发送邮件
  - 发送文本邮件
  - 发送 HTML 邮件
  - 发送模板邮件
  - 使用 React Email
- 参考

ShipAny 支持使用 Resend 发送邮件，可用于发送邮件验证码、发送支付通知、发送营销邮件等场景。

在 Resend 后台 添加域名，设置 DNS 记录，验证域名

在 Resend 后台 创建 API 密钥，并复制 API 密钥

在 ShipAny 项目配置文件中，填写 Resend 相关的配置信息。

比如在 Resend 后台配置的邮件域名是 mail.shipany.ai，则发件人邮箱可以配置为 [email protected] / [email protected] / [email protected] 等。

在需要发邮件的地方，根据具体场景，选择合适的发送方式。

React Email 内置大量邮件组件，可以让你更轻松创建邮件模板。

比如在 @/components/email-templates/react-email.tsx 中写入内容：

除了自己实现邮件模板，你也可以在 React Email 模板市场 选择一个模板，修改后直接使用。

**Examples:**

Example 1 (unknown):
```unknown
RESEND_API_KEY = "re_xxx"
RESEND_SENDER_EMAIL = "[email protected]"
```

Example 2 (unknown):
```unknown
RESEND_API_KEY = "re_xxx"
RESEND_SENDER_EMAIL = "[email protected]"
```

Example 3 (python):
```python
import { Resend } from "resend";
 
const resend = new Resend(process.env.RESEND_API_KEY!);
 
const result = await resend.emails.send({
  from: process.env.RESEND_SENDER_EMAIL!,
  to: ["[email protected]"],
  subject: "Hello from ShipAny with Resend",
  text: "Hello World.",
});
 
console.log("send email result", result);
```

Example 4 (python):
```python
import { Resend } from "resend";
 
const resend = new Resend(process.env.RESEND_API_KEY!);
 
const result = await resend.emails.send({
  from: process.env.RESEND_SENDER_EMAIL!,
  to: ["[email protected]"],
  subject: "Hello from ShipAny with Resend",
  text: "Hello World.",
});
 
console.log("send email result", result);
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/features/affiliate#如何自定义奖励金额和比例

**Contents:**
- 邀请返佣
- 如何使用
- 如何自定义奖励金额和比例

ShipAny 实现了一套邀请返佣系统。你可以在你的产品中使用这套系统来激励用户邀请新用户。

用户进入：http://localhost:3000/my-invites 页面，可以生成自己的邀请链接。

http://localhost:3000/i/idoubi

新用户通过分享者的邀请链接进入系统，会自动关联到分享者。

分享者可以在 /my-invites 页面查看邀请记录和邀请奖励

暂不支持在线自动提现，需要管理员人工联系用户发放奖励。

你可以修改此接口的逻辑，更改新用户注册场景下的奖励规则。

默认的 AffiliateRewardPercent.Invited 和 AffiliateRewardAmount.Invited 都是 0.

你可以修改此方法内的逻辑，修改被邀请人支付的订单，给到邀请人的奖励

默认的 AffiliateRewardPercent.Paied 值是 20，代表返佣比例是 20%

默认的 AffiliateRewardAmount.Paied 值是 50，代表返佣金额是 $50

**Examples:**

Example 1 (unknown):
```unknown
await insertAffiliate({
  user_uuid: user_uuid,
  invited_by: inviteUser.uuid,
  created_at: getIsoTimestr(),
  status: AffiliateStatus.Pending,
  paid_order_no: "",
  paid_amount: 0,
  reward_percent: AffiliateRewardPercent.Invited,
  reward_amount: AffiliateRewardAmount.Invited,
});
```

Example 2 (unknown):
```unknown
await insertAffiliate({
  user_uuid: user_uuid,
  invited_by: inviteUser.uuid,
  created_at: getIsoTimestr(),
  status: AffiliateStatus.Pending,
  paid_order_no: "",
  paid_amount: 0,
  reward_percent: AffiliateRewardPercent.Invited,
  reward_amount: AffiliateRewardAmount.Invited,
});
```

Example 3 (python):
```python
import { findAffiliateByOrderNo, insertAffiliate } from "@/models/affiliate";
 
import { AffiliateRewardAmount } from "./constant";
import { AffiliateRewardPercent } from "./constant";
import { AffiliateStatus } from "./constant";
import { Order } from "@/types/order";
import { findUserByUuid } from "@/models/user";
import { getIsoTimestr } from "@/lib/time";
 
export async function updateAffiliateForOrder(order: Order) {
  try {
    const user = await findUserByUuid(order.user_uuid);
    if (user && user.uuid && user.invited_by && user.invited_by !== user.uuid) {
      const affiliate = await
...
```

Example 4 (python):
```python
import { findAffiliateByOrderNo, insertAffiliate } from "@/models/affiliate";
 
import { AffiliateRewardAmount } from "./constant";
import { AffiliateRewardPercent } from "./constant";
import { AffiliateStatus } from "./constant";
import { Order } from "@/types/order";
import { findUserByUuid } from "@/models/user";
import { getIsoTimestr } from "@/lib/time";
 
export async function updateAffiliateForOrder(order: Order) {
  try {
    const user = await findUserByUuid(order.user_uuid);
    if (user && user.uuid && user.invited_by && user.invited_by !== user.uuid) {
      const affiliate = await
...
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/features/feedback

**Contents:**
- 用户反馈
- 用户反馈组件
- 如何使用

ShipAny 提供用户反馈组件，用于收集用户反馈。

用户反馈组件位于页面右下角，点击后会弹窗收集用户反馈。

**Examples:**

Example 1 (unknown):
```unknown
CREATE TABLE feedbacks (
    id SERIAL PRIMARY KEY,
    created_at timestamptz,
    status VARCHAR(50),
    user_uuid VARCHAR(255),
    content TEXT,
    rating INT
);
```

Example 2 (unknown):
```unknown
CREATE TABLE feedbacks (
    id SERIAL PRIMARY KEY,
    created_at timestamptz,
    status VARCHAR(50),
    user_uuid VARCHAR(255),
    content TEXT,
    rating INT
);
```

Example 3 (python):
```python
import Footer from "@/components/blocks/footer";
import Header from "@/components/blocks/header";
import { ReactNode } from "react";
import { getLandingPage } from "@/services/page";
import Feedback from "@/components/feedback";
 
export default async function DefaultLayout({
  children,
  params,
}: {
  children: ReactNode;
  params: Promise<{ locale: string }>;
}) {
  const { locale } = await params;
  const page = await getLandingPage(locale);
 
  return (
    <>
      {page.header && <Header header={page.header} />}
      <main className="overflow-x-hidden">{children}</main>
      {page.fo
...
```

Example 4 (python):
```python
import Footer from "@/components/blocks/footer";
import Header from "@/components/blocks/header";
import { ReactNode } from "react";
import { getLandingPage } from "@/services/page";
import Feedback from "@/components/feedback";
 
export default async function DefaultLayout({
  children,
  params,
}: {
  children: ReactNode;
  params: Promise<{ locale: string }>;
}) {
  const { locale } = await params;
  const page = await getLandingPage(locale);
 
  return (
    <>
      {page.header && <Header header={page.header} />}
      <main className="overflow-x-hidden">{children}</main>
      {page.fo
...
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/features/email/resend#参考

**Contents:**
- Resend
- Resend 设置
- ShipAny 配置
- 发送邮件
  - 发送文本邮件
  - 发送 HTML 邮件
  - 发送模板邮件
  - 使用 React Email
- 参考

ShipAny 支持使用 Resend 发送邮件，可用于发送邮件验证码、发送支付通知、发送营销邮件等场景。

在 Resend 后台 添加域名，设置 DNS 记录，验证域名

在 Resend 后台 创建 API 密钥，并复制 API 密钥

在 ShipAny 项目配置文件中，填写 Resend 相关的配置信息。

比如在 Resend 后台配置的邮件域名是 mail.shipany.ai，则发件人邮箱可以配置为 [email protected] / [email protected] / [email protected] 等。

在需要发邮件的地方，根据具体场景，选择合适的发送方式。

React Email 内置大量邮件组件，可以让你更轻松创建邮件模板。

比如在 @/components/email-templates/react-email.tsx 中写入内容：

除了自己实现邮件模板，你也可以在 React Email 模板市场 选择一个模板，修改后直接使用。

**Examples:**

Example 1 (unknown):
```unknown
RESEND_API_KEY = "re_xxx"
RESEND_SENDER_EMAIL = "[email protected]"
```

Example 2 (unknown):
```unknown
RESEND_API_KEY = "re_xxx"
RESEND_SENDER_EMAIL = "[email protected]"
```

Example 3 (python):
```python
import { Resend } from "resend";
 
const resend = new Resend(process.env.RESEND_API_KEY!);
 
const result = await resend.emails.send({
  from: process.env.RESEND_SENDER_EMAIL!,
  to: ["[email protected]"],
  subject: "Hello from ShipAny with Resend",
  text: "Hello World.",
});
 
console.log("send email result", result);
```

Example 4 (python):
```python
import { Resend } from "resend";
 
const resend = new Resend(process.env.RESEND_API_KEY!);
 
const result = await resend.emails.send({
  from: process.env.RESEND_SENDER_EMAIL!,
  to: ["[email protected]"],
  subject: "Hello from ShipAny with Resend",
  text: "Hello World.",
});
 
console.log("send email result", result);
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/features/oauth#谷歌一键登录

**Contents:**
- 登录鉴权
- 生成 Auth Secret
- 谷歌登录
- 谷歌一键登录
- Github 登录
- 登录预览
- 参考

ShipAny 目前支持 谷歌登录 / 谷歌一键登录 / Github 登录三种登录方式。

其他登录方式逐步集成，也可以参考 next-auth 文档自行接入。

生成一个 32 字节的随机字符串，作为 Auth Secret

修改环境变量中的 AUTH_SECRET 值

创建一个新项目，进入新项目的 Credentials 管理页面，创建 Oauth Client ID

创建 Oauth Client ID 后，得到 Client ID 和 Client Secret

首先按照谷歌登录的步骤，拿到 AUTH_GOOGLE_ID 和 AUTH_GOOGLE_SECRET

修改配置文件中的 NEXT_PUBLIC_AUTH_GOOGLE_ONE_TAP_ENABLED 和 NEXT_PUBLIC_AUTH_GOOGLE_ID

谷歌一键登录使用到的 NEXT_PUBLIC_AUTH_GOOGLE_ID 跟谷歌登录配置的 AUTH_GOOGLE_ID 保持一致。

开发环境和生产环境，需要创建两个不同的 OAuth app，分别配置不同的回调地址。

进入 OAuth app，复制 Client ID 和 Client Secret

修改配置文件中的 AUTH_GITHUB_ID 和 AUTH_GITHUB_SECRET

**Examples:**

Example 1 (unknown):
```unknown
openssl rand -base64 32
```

Example 2 (unknown):
```unknown
openssl rand -base64 32
```

Example 3 (unknown):
```unknown
AUTH_SECRET = "xxx"
```

Example 4 (unknown):
```unknown
AUTH_SECRET = "xxx"
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/features/database#使用其他类型数据库

**Contents:**
- 数据库
- 配置数据库
- 初始化数据库
- 更新数据库
- 管理数据库
- 操作数据库
- 使用其他类型数据库
- 参考

ShipAny 使用 drizzle-orm 支持多种类型数据库。

以 Supabase 数据库为例，在 ShipAny 配置数据库的流程为：

登录 Supabase 控制台，创建数据库

在 Supabase 控制台，进入你创建的数据库，点击上方的 Connect

在弹出来的框中复制数据库连接信息，类似这样的字符串：

[YOUR-PASSWORD] 需要替换成你在创建数据库时设置的密码。

修改项目配置文件：.env.development 和 .env.production

在配置好 DATABASE_URL 后，在项目根目录下运行以下命令，初始化数据库：

这个命令会执行 src/db/migrations 目录下的所有迁移文件，创建数据库表。

如果你通过 DATABASE_URL 配置的不是一个新创建的数据库，或者数据库之前已经存在 ShipAny 的库表信息，请不要执行以上命令。而是比较 src/db/migrations 目录下所有迁移文件的 sql 内容，手动执行 sql 语句，更新数据库表。

如果在项目创建之处，你使用的是一个新的数据库，且是通过 pnpm db:migrate 命令初始化的数据库，如果后续你拉取了最新的代码，可以继续执行以下命令，更新数据库表：

这个命令会根据 src/db/migrations 目录下所有迁移文件的 sql 内容，增量更新数据库表。

在项目根目录下执行命令：pnpm db:studio

这个命令会打开一个数据库管理界面，你可以在这里查看、编辑、删除数据库表。

在 src/models 目录下，写数据库操作文件，实现对数据表的增删改查。可参考以下操作 posts 表的示例：

数据表操作语法可参考 drizzle-orm 文档。

如果你使用自建的 Postgres 数据库，或者使用其他兼容 postgres 的云数据库，比如：Neon。配置和连接数据库的步骤跟使用 Supabase 一致，你只需要填写数据库的 DATABASE_URL 即可。

如果你需要使用 MySQL 或者 SQLite 等数据库，可参考以下步骤自定义：

修改 src/db/schema.ts 文件，使用新的数据库 Schema。

Schema 中数据表的字段定义，可以参考 drizzle-orm 文档。

修改 src/db/config.ts 文件，使用新的数据库连接配置。

默认是 Postgres 数据库连接配置，你可以参考 drizzle-orm 文档按需修改。

根据你使用的数据库类型，修改数据库连接实例。

如果你希望后续通过迁移文件更新数据库表。你可以在完成以上三步之后，在项目根目录下执行以下命令生成数据库迁移文件。

在 ShipAny 中配置不同类型的数据库非常简单，只需要完成以上四个步骤的自定义即可。src/model 下操作数据库的逻辑无需修改。

**Examples:**

Example 1 (unknown):
```unknown
postgresql://postgres.defqvdpquwyqqjlmurkg:[YOUR-PASSWORD]@aws-0-ap-southeast-1.pooler.supabase.com:6543/postgres
```

Example 2 (unknown):
```unknown
postgresql://postgres.defqvdpquwyqqjlmurkg:[YOUR-PASSWORD]@aws-0-ap-southeast-1.pooler.supabase.com:6543/postgres
```

Example 3 (unknown):
```unknown
DATABASE_URL="postgresql://postgres.defqvdpquwyqqjlmurkg:******@aws-0-ap-southeast-1.pooler.supabase.com:6543/postgres"
```

Example 4 (unknown):
```unknown
DATABASE_URL="postgresql://postgres.defqvdpquwyqqjlmurkg:******@aws-0-ap-southeast-1.pooler.supabase.com:6543/postgres"
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/features/seo#metadata-配置

**Contents:**
- SEO
- 设置多语言文案
- 设置站点地图
- 网页 SEO 走查
- Metadata 配置
- 接入 GSC

ShipAny 做了很多 SEO 优化，可以让你的项目在搜索引擎中获得更好的排名。

在 i18n/messages 目录下，通过 [locale].json 文件配置页面内容，默认支持中文和英文，在 i18n/messages/ 目录下，可以看到 en.json 和 zh.json 两个文件，在项目发布之前，修改成跟你项目相符合的文案即可。

修改 public/sitemap.xml 文件，配置成你自己的站点信息

按需修改 public/robots.txt 内容

检查网站首页的 title / description / Canonical 是否合理

用 AI 辅助修改 i18n/pages/landing 下 json 文件对应的网页内容，调整网站主打的关键词密度。(3% 左右比较合理)

ShipAny 对默认的 landing page 做了内容结构优化。如果你有自定义页面组件，需要检查页面的结构是否合理。

在 AITDK 插件的 Issues 面板开启 SSR Check，检测网页是否是服务端渲染。

如果你有创建新的页面路由 (page.tsx)，可以配置一下新页面的 Metadata 信息。

为子页面设置独立的 title / description / canonical 信息，有利于 SEO。

网站上站后，在 Google Search Console 中添加你的站点，可以查看网站的搜索流量和排名情况。

**Examples:**

Example 1 (unknown):
```unknown
update content of this file, for my new project "Flux AI", which is an AI Image Generator, with keywords "flux ai, ai image generator"
```

Example 2 (unknown):
```unknown
update content of this file, for my new project "Flux AI", which is an AI Image Generator, with keywords "flux ai, ai image generator"
```

Example 3 (unknown):
```unknown
<?xml version='1.0' encoding='utf-8' standalone='yes'?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://shipany.ai/</loc>
    <lastmod>2024-12-24T10:00:00+00:00</lastmod>
  </url>
</urlset>
```

Example 4 (unknown):
```unknown
<?xml version='1.0' encoding='utf-8' standalone='yes'?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://shipany.ai/</loc>
    <lastmod>2024-12-24T10:00:00+00:00</lastmod>
  </url>
</urlset>
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/features/payment/stripe#自定义支付

**Contents:**
- Stripe
- Stripe 设置
- ShipAny 配置
- 价格表支付
  - 配置价格表内容
  - 修改价格表组件
  - 修改价格表下单逻辑
  - 修改支付回调逻辑
  - 修改支付通知逻辑
- 自定义支付

ShipAny 支持使用 Stripe 进行支付，可用于产品付款、会员订阅、购买积分等场景。

在 ShipAny 项目配置文件中，填写 Stripe 相关的配置信息。

页面路径可以填相对路径，也可以填绝对路径。如果填的是相对路径，跳转时会自动拼接 NEXT_PUBLIC_WEB_URL 配置的网站地址，并带上多语言参数。

比如按照以上配置，在中文页面支付成功后的跳转路径是：http://localhost:3000/zh/my-orders

ShipAny 模板内置了一个价格表和对应的支付逻辑，你可以根据自己的需求，简单修改即可快速实现支付功能。

ShipAny 模板内置的价格表配置文件位于：src/i18n/pages/pricing 目录下，支持多语言，默认包含 en.json 和 zh.json 两个价格表配置文件。

你可以根据自己的需求，修改价格表配置文件中的内容。

默认的价格表组件位于：src/components/blocks/pricing/index.tsx

你可以根据自己的需求，修改价格表的展示形式。

默认的价格表下单逻辑位于：src/app/api/checkout/route.ts

你可以根据自己的需求，修改价格表的下单逻辑。

在价格表下单逻辑中，默认配置的支付回调地址是：/api/pay/callback/stripe

用户支付后，会在浏览器跳转到这个地址，并带上包含支付信息的参数。

默认的支付回调处理逻辑位于：src/app/api/pay/callback/stripe/route.ts

你可以根据自己的需求，修改处理支付回调的逻辑，比如更新订单状态、给用户发送邮件通知、给用户赠送积分等。

支付回调是同步逻辑，依赖浏览器跳转到回调地址，才能处理支付结果。这种方式不太可靠，可能出现跳转过程中用户关闭了浏览器等情况，导致支付结果没有被正常处理。 更可靠的方式是通过 Webhook，配置支付结果异步通知。

比如把 Webhook 地址配置为：https://your-domain.com/api/pay/notify/stripe

用户支付后，Stripe 会把支付信息推送到这个地址。

默认的支付通知逻辑位于：src/app/api/pay/notify/stripe/route.ts

你可以根据自己的需求，修改处理支付通知的逻辑，比如更新订单状态、给用户发送邮件通知、给用户赠送积分等。

修改价格表配置文件，添加 groups 数据，配置多个价格分组。并在 pricing.items 下为每一个价格方案，设置一个 group 名称。

配置完成后，点击价格分组，将根据 group 字段，切换显示不同的价格方案。

ShipAny 模板使用 Stripe 支付时，默认支持三种支付方案

你只需要修改价格表配置，把每个价格方案的 interval 字段，设置成上述三个值之一。

同时，按需修改价格(amount) / 积分(credits) / 有效期(valid_months) 等字段。

举例：按月订阅扣费，月付 $99，购买后得到 30 个积分，有效期 1 个月，则核心的价格表配置信息为：

修改 src/app/api/checkout/route.ts 文件，设置 Stripe 下单的 options 参数。

在 Stripe 后台 设置支付方式，开通支付宝和微信支付。

修改价格表配置文件，在每个价格方案下添加一个 cn_amount 字段，即可支持人民币支付。

比如，产品售价，$99，人民币支付价格为 699 元，核心配置信息为：

配置完成后，在价格表下单按钮上方，将会显示一个人民币支付图标。

在 Stripe 后台点击左上角的店铺打开下拉菜单，依次点击 Switch to sandbox -> Test mode，开启测试模式。

在测试模式下，进入开发者中心，设置 测试支付密钥，包括 Publishable key 和 Secret key。

注册 ngrok 账号，按指示安装 ngrok 命令行工具。

启动 ngrok 服务，监听本地端口，并生成一个临时的域名。

在 Stripe 后台测试模式中，配置 Webhook 地址为 ngrok 生成的域名，并监听以下两个事件：

Endpoint 填写支付通知地址，比如 https://xxx.ngrok-free.app/api/pay/notify/stripe。

添加 Webhook 地址后，在 Webhook 管理页面，复制 Signing secret，

跟支付密钥一起填入 .env.development 文件中。

在本地启动项目，访问 /pricing 页面，点击下单按钮，下单成功后跳转到支付页面。

使用 Stripe 测试卡 支付，支付成功后浏览器跳转到支付回调地址，监听的地址收到支付通知。

**Examples:**

Example 1 (unknown):
```unknown
NEXT_PUBLIC_WEB_URL = "http://localhost:3000"

NEXT_PUBLIC_PAY_SUCCESS_URL = "/my-orders"
NEXT_PUBLIC_PAY_FAIL_URL = "/pricing"
NEXT_PUBLIC_PAY_CANCEL_URL = "/pricing"

PAY_PROVIDER = "stripe"

STRIPE_PUBLIC_KEY = "pk_test_xxx"
STRIPE_PRIVATE_KEY = "sk_test_xxx"
STRIPE_WEBHOOK_SECRET = "whsec_cexxx"
```

Example 2 (unknown):
```unknown
NEXT_PUBLIC_WEB_URL = "http://localhost:3000"

NEXT_PUBLIC_PAY_SUCCESS_URL = "/my-orders"
NEXT_PUBLIC_PAY_FAIL_URL = "/pricing"
NEXT_PUBLIC_PAY_CANCEL_URL = "/pricing"

PAY_PROVIDER = "stripe"

STRIPE_PUBLIC_KEY = "pk_test_xxx"
STRIPE_PRIVATE_KEY = "sk_test_xxx"
STRIPE_WEBHOOK_SECRET = "whsec_cexxx"
```

Example 3 (unknown):
```unknown
{
  "pricing": {
    "name": "pricing",
    "label": "Pricing",
    "title": "Pricing",
    "description": "Get all features of ShipAny, Ship your AI SaaS startups fast.",
    "groups": [],
    "items": [
      {
        "title": "Starter",
        "description": "Get started with your first SaaS startup.",
        "features_title": "Includes",
        "features": [
          "100 credits, valid for 1 month",
          "NextJS boilerplate",
          "SEO-friendly structure",
          "Payment with Stripe",
          "Data storage with Supabase",
          "Google Oauth & One-Tap Login",
    
...
```

Example 4 (unknown):
```unknown
{
  "pricing": {
    "name": "pricing",
    "label": "Pricing",
    "title": "Pricing",
    "description": "Get all features of ShipAny, Ship your AI SaaS startups fast.",
    "groups": [],
    "items": [
      {
        "title": "Starter",
        "description": "Get started with your first SaaS startup.",
        "features_title": "Includes",
        "features": [
          "100 credits, valid for 1 month",
          "NextJS boilerplate",
          "SEO-friendly structure",
          "Payment with Stripe",
          "Data storage with Supabase",
          "Google Oauth & One-Tap Login",
    
...
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/features/database#管理数据库

**Contents:**
- 数据库
- 配置数据库
- 初始化数据库
- 更新数据库
- 管理数据库
- 操作数据库
- 使用其他类型数据库
- 参考

ShipAny 使用 drizzle-orm 支持多种类型数据库。

以 Supabase 数据库为例，在 ShipAny 配置数据库的流程为：

登录 Supabase 控制台，创建数据库

在 Supabase 控制台，进入你创建的数据库，点击上方的 Connect

在弹出来的框中复制数据库连接信息，类似这样的字符串：

[YOUR-PASSWORD] 需要替换成你在创建数据库时设置的密码。

修改项目配置文件：.env.development 和 .env.production

在配置好 DATABASE_URL 后，在项目根目录下运行以下命令，初始化数据库：

这个命令会执行 src/db/migrations 目录下的所有迁移文件，创建数据库表。

如果你通过 DATABASE_URL 配置的不是一个新创建的数据库，或者数据库之前已经存在 ShipAny 的库表信息，请不要执行以上命令。而是比较 src/db/migrations 目录下所有迁移文件的 sql 内容，手动执行 sql 语句，更新数据库表。

如果在项目创建之处，你使用的是一个新的数据库，且是通过 pnpm db:migrate 命令初始化的数据库，如果后续你拉取了最新的代码，可以继续执行以下命令，更新数据库表：

这个命令会根据 src/db/migrations 目录下所有迁移文件的 sql 内容，增量更新数据库表。

在项目根目录下执行命令：pnpm db:studio

这个命令会打开一个数据库管理界面，你可以在这里查看、编辑、删除数据库表。

在 src/models 目录下，写数据库操作文件，实现对数据表的增删改查。可参考以下操作 posts 表的示例：

数据表操作语法可参考 drizzle-orm 文档。

如果你使用自建的 Postgres 数据库，或者使用其他兼容 postgres 的云数据库，比如：Neon。配置和连接数据库的步骤跟使用 Supabase 一致，你只需要填写数据库的 DATABASE_URL 即可。

如果你需要使用 MySQL 或者 SQLite 等数据库，可参考以下步骤自定义：

修改 src/db/schema.ts 文件，使用新的数据库 Schema。

Schema 中数据表的字段定义，可以参考 drizzle-orm 文档。

修改 src/db/config.ts 文件，使用新的数据库连接配置。

默认是 Postgres 数据库连接配置，你可以参考 drizzle-orm 文档按需修改。

根据你使用的数据库类型，修改数据库连接实例。

如果你希望后续通过迁移文件更新数据库表。你可以在完成以上三步之后，在项目根目录下执行以下命令生成数据库迁移文件。

在 ShipAny 中配置不同类型的数据库非常简单，只需要完成以上四个步骤的自定义即可。src/model 下操作数据库的逻辑无需修改。

**Examples:**

Example 1 (unknown):
```unknown
postgresql://postgres.defqvdpquwyqqjlmurkg:[YOUR-PASSWORD]@aws-0-ap-southeast-1.pooler.supabase.com:6543/postgres
```

Example 2 (unknown):
```unknown
postgresql://postgres.defqvdpquwyqqjlmurkg:[YOUR-PASSWORD]@aws-0-ap-southeast-1.pooler.supabase.com:6543/postgres
```

Example 3 (unknown):
```unknown
DATABASE_URL="postgresql://postgres.defqvdpquwyqqjlmurkg:******@aws-0-ap-southeast-1.pooler.supabase.com:6543/postgres"
```

Example 4 (unknown):
```unknown
DATABASE_URL="postgresql://postgres.defqvdpquwyqqjlmurkg:******@aws-0-ap-southeast-1.pooler.supabase.com:6543/postgres"
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/features/database#更新数据库

**Contents:**
- 数据库
- 配置数据库
- 初始化数据库
- 更新数据库
- 管理数据库
- 操作数据库
- 使用其他类型数据库
- 参考

ShipAny 使用 drizzle-orm 支持多种类型数据库。

以 Supabase 数据库为例，在 ShipAny 配置数据库的流程为：

登录 Supabase 控制台，创建数据库

在 Supabase 控制台，进入你创建的数据库，点击上方的 Connect

在弹出来的框中复制数据库连接信息，类似这样的字符串：

[YOUR-PASSWORD] 需要替换成你在创建数据库时设置的密码。

修改项目配置文件：.env.development 和 .env.production

在配置好 DATABASE_URL 后，在项目根目录下运行以下命令，初始化数据库：

这个命令会执行 src/db/migrations 目录下的所有迁移文件，创建数据库表。

如果你通过 DATABASE_URL 配置的不是一个新创建的数据库，或者数据库之前已经存在 ShipAny 的库表信息，请不要执行以上命令。而是比较 src/db/migrations 目录下所有迁移文件的 sql 内容，手动执行 sql 语句，更新数据库表。

如果在项目创建之处，你使用的是一个新的数据库，且是通过 pnpm db:migrate 命令初始化的数据库，如果后续你拉取了最新的代码，可以继续执行以下命令，更新数据库表：

这个命令会根据 src/db/migrations 目录下所有迁移文件的 sql 内容，增量更新数据库表。

在项目根目录下执行命令：pnpm db:studio

这个命令会打开一个数据库管理界面，你可以在这里查看、编辑、删除数据库表。

在 src/models 目录下，写数据库操作文件，实现对数据表的增删改查。可参考以下操作 posts 表的示例：

数据表操作语法可参考 drizzle-orm 文档。

如果你使用自建的 Postgres 数据库，或者使用其他兼容 postgres 的云数据库，比如：Neon。配置和连接数据库的步骤跟使用 Supabase 一致，你只需要填写数据库的 DATABASE_URL 即可。

如果你需要使用 MySQL 或者 SQLite 等数据库，可参考以下步骤自定义：

修改 src/db/schema.ts 文件，使用新的数据库 Schema。

Schema 中数据表的字段定义，可以参考 drizzle-orm 文档。

修改 src/db/config.ts 文件，使用新的数据库连接配置。

默认是 Postgres 数据库连接配置，你可以参考 drizzle-orm 文档按需修改。

根据你使用的数据库类型，修改数据库连接实例。

如果你希望后续通过迁移文件更新数据库表。你可以在完成以上三步之后，在项目根目录下执行以下命令生成数据库迁移文件。

在 ShipAny 中配置不同类型的数据库非常简单，只需要完成以上四个步骤的自定义即可。src/model 下操作数据库的逻辑无需修改。

**Examples:**

Example 1 (unknown):
```unknown
postgresql://postgres.defqvdpquwyqqjlmurkg:[YOUR-PASSWORD]@aws-0-ap-southeast-1.pooler.supabase.com:6543/postgres
```

Example 2 (unknown):
```unknown
postgresql://postgres.defqvdpquwyqqjlmurkg:[YOUR-PASSWORD]@aws-0-ap-southeast-1.pooler.supabase.com:6543/postgres
```

Example 3 (unknown):
```unknown
DATABASE_URL="postgresql://postgres.defqvdpquwyqqjlmurkg:******@aws-0-ap-southeast-1.pooler.supabase.com:6543/postgres"
```

Example 4 (unknown):
```unknown
DATABASE_URL="postgresql://postgres.defqvdpquwyqqjlmurkg:******@aws-0-ap-southeast-1.pooler.supabase.com:6543/postgres"
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/features/blog#配置-cms

**Contents:**
- 博客
- 配置 CMS
- 管理博客内容
- 配置博客路由

ShipAny 内置一套 CMS 系统，用于博客内容管理，支持多语言。

为了能可视化管理博客内容，你需要 配置管理后台。

博客的标题和访问路由(slug)必填，默认支持多语言，需要选择对应的语言。

访问博客列表前台路由，可以看到在后台添加的博客内容。

默认的博客路由是 /posts，按照上述步骤添加博客内容后，你可以在 i18n/pages/landing 的 json 文件中添加导航项，显示博客列表的入口。

你需要添加自定义的文件夹，并参考 app/[locale]/(default)/posts 文件夹组织自定义的代码。

**Examples:**

Example 1 (unknown):
```unknown
CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    uuid VARCHAR(255) UNIQUE NOT NULL,
    slug VARCHAR(255),
    title VARCHAR(255),
    description TEXT,
    content TEXT,
    created_at timestamptz,
    updated_at timestamptz,
    status VARCHAR(50),
    cover_url VARCHAR(255),
    author_name VARCHAR(255),
    author_avatar_url VARCHAR(255),
    locale VARCHAR(50)
);
```

Example 2 (unknown):
```unknown
CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    uuid VARCHAR(255) UNIQUE NOT NULL,
    slug VARCHAR(255),
    title VARCHAR(255),
    description TEXT,
    content TEXT,
    created_at timestamptz,
    updated_at timestamptz,
    status VARCHAR(50),
    cover_url VARCHAR(255),
    author_name VARCHAR(255),
    author_avatar_url VARCHAR(255),
    locale VARCHAR(50)
);
```

Example 3 (unknown):
```unknown
https://{your-domain}/admin/posts
```

Example 4 (unknown):
```unknown
https://{your-domain}/admin/posts
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/features/payment/stripe#修改价格表下单逻辑

**Contents:**
- Stripe
- Stripe 设置
- ShipAny 配置
- 价格表支付
  - 配置价格表内容
  - 修改价格表组件
  - 修改价格表下单逻辑
  - 修改支付回调逻辑
  - 修改支付通知逻辑
- 自定义支付

ShipAny 支持使用 Stripe 进行支付，可用于产品付款、会员订阅、购买积分等场景。

在 ShipAny 项目配置文件中，填写 Stripe 相关的配置信息。

页面路径可以填相对路径，也可以填绝对路径。如果填的是相对路径，跳转时会自动拼接 NEXT_PUBLIC_WEB_URL 配置的网站地址，并带上多语言参数。

比如按照以上配置，在中文页面支付成功后的跳转路径是：http://localhost:3000/zh/my-orders

ShipAny 模板内置了一个价格表和对应的支付逻辑，你可以根据自己的需求，简单修改即可快速实现支付功能。

ShipAny 模板内置的价格表配置文件位于：src/i18n/pages/pricing 目录下，支持多语言，默认包含 en.json 和 zh.json 两个价格表配置文件。

你可以根据自己的需求，修改价格表配置文件中的内容。

默认的价格表组件位于：src/components/blocks/pricing/index.tsx

你可以根据自己的需求，修改价格表的展示形式。

默认的价格表下单逻辑位于：src/app/api/checkout/route.ts

你可以根据自己的需求，修改价格表的下单逻辑。

在价格表下单逻辑中，默认配置的支付回调地址是：/api/pay/callback/stripe

用户支付后，会在浏览器跳转到这个地址，并带上包含支付信息的参数。

默认的支付回调处理逻辑位于：src/app/api/pay/callback/stripe/route.ts

你可以根据自己的需求，修改处理支付回调的逻辑，比如更新订单状态、给用户发送邮件通知、给用户赠送积分等。

支付回调是同步逻辑，依赖浏览器跳转到回调地址，才能处理支付结果。这种方式不太可靠，可能出现跳转过程中用户关闭了浏览器等情况，导致支付结果没有被正常处理。 更可靠的方式是通过 Webhook，配置支付结果异步通知。

比如把 Webhook 地址配置为：https://your-domain.com/api/pay/notify/stripe

用户支付后，Stripe 会把支付信息推送到这个地址。

默认的支付通知逻辑位于：src/app/api/pay/notify/stripe/route.ts

你可以根据自己的需求，修改处理支付通知的逻辑，比如更新订单状态、给用户发送邮件通知、给用户赠送积分等。

修改价格表配置文件，添加 groups 数据，配置多个价格分组。并在 pricing.items 下为每一个价格方案，设置一个 group 名称。

配置完成后，点击价格分组，将根据 group 字段，切换显示不同的价格方案。

ShipAny 模板使用 Stripe 支付时，默认支持三种支付方案

你只需要修改价格表配置，把每个价格方案的 interval 字段，设置成上述三个值之一。

同时，按需修改价格(amount) / 积分(credits) / 有效期(valid_months) 等字段。

举例：按月订阅扣费，月付 $99，购买后得到 30 个积分，有效期 1 个月，则核心的价格表配置信息为：

修改 src/app/api/checkout/route.ts 文件，设置 Stripe 下单的 options 参数。

在 Stripe 后台 设置支付方式，开通支付宝和微信支付。

修改价格表配置文件，在每个价格方案下添加一个 cn_amount 字段，即可支持人民币支付。

比如，产品售价，$99，人民币支付价格为 699 元，核心配置信息为：

配置完成后，在价格表下单按钮上方，将会显示一个人民币支付图标。

在 Stripe 后台点击左上角的店铺打开下拉菜单，依次点击 Switch to sandbox -> Test mode，开启测试模式。

在测试模式下，进入开发者中心，设置 测试支付密钥，包括 Publishable key 和 Secret key。

注册 ngrok 账号，按指示安装 ngrok 命令行工具。

启动 ngrok 服务，监听本地端口，并生成一个临时的域名。

在 Stripe 后台测试模式中，配置 Webhook 地址为 ngrok 生成的域名，并监听以下两个事件：

Endpoint 填写支付通知地址，比如 https://xxx.ngrok-free.app/api/pay/notify/stripe。

添加 Webhook 地址后，在 Webhook 管理页面，复制 Signing secret，

跟支付密钥一起填入 .env.development 文件中。

在本地启动项目，访问 /pricing 页面，点击下单按钮，下单成功后跳转到支付页面。

使用 Stripe 测试卡 支付，支付成功后浏览器跳转到支付回调地址，监听的地址收到支付通知。

**Examples:**

Example 1 (unknown):
```unknown
NEXT_PUBLIC_WEB_URL = "http://localhost:3000"

NEXT_PUBLIC_PAY_SUCCESS_URL = "/my-orders"
NEXT_PUBLIC_PAY_FAIL_URL = "/pricing"
NEXT_PUBLIC_PAY_CANCEL_URL = "/pricing"

PAY_PROVIDER = "stripe"

STRIPE_PUBLIC_KEY = "pk_test_xxx"
STRIPE_PRIVATE_KEY = "sk_test_xxx"
STRIPE_WEBHOOK_SECRET = "whsec_cexxx"
```

Example 2 (unknown):
```unknown
NEXT_PUBLIC_WEB_URL = "http://localhost:3000"

NEXT_PUBLIC_PAY_SUCCESS_URL = "/my-orders"
NEXT_PUBLIC_PAY_FAIL_URL = "/pricing"
NEXT_PUBLIC_PAY_CANCEL_URL = "/pricing"

PAY_PROVIDER = "stripe"

STRIPE_PUBLIC_KEY = "pk_test_xxx"
STRIPE_PRIVATE_KEY = "sk_test_xxx"
STRIPE_WEBHOOK_SECRET = "whsec_cexxx"
```

Example 3 (unknown):
```unknown
{
  "pricing": {
    "name": "pricing",
    "label": "Pricing",
    "title": "Pricing",
    "description": "Get all features of ShipAny, Ship your AI SaaS startups fast.",
    "groups": [],
    "items": [
      {
        "title": "Starter",
        "description": "Get started with your first SaaS startup.",
        "features_title": "Includes",
        "features": [
          "100 credits, valid for 1 month",
          "NextJS boilerplate",
          "SEO-friendly structure",
          "Payment with Stripe",
          "Data storage with Supabase",
          "Google Oauth & One-Tap Login",
    
...
```

Example 4 (unknown):
```unknown
{
  "pricing": {
    "name": "pricing",
    "label": "Pricing",
    "title": "Pricing",
    "description": "Get all features of ShipAny, Ship your AI SaaS startups fast.",
    "groups": [],
    "items": [
      {
        "title": "Starter",
        "description": "Get started with your first SaaS startup.",
        "features_title": "Includes",
        "features": [
          "100 credits, valid for 1 month",
          "NextJS boilerplate",
          "SEO-friendly structure",
          "Payment with Stripe",
          "Data storage with Supabase",
          "Google Oauth & One-Tap Login",
    
...
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/features/email/resend#发送文本邮件

**Contents:**
- Resend
- Resend 设置
- ShipAny 配置
- 发送邮件
  - 发送文本邮件
  - 发送 HTML 邮件
  - 发送模板邮件
  - 使用 React Email
- 参考

ShipAny 支持使用 Resend 发送邮件，可用于发送邮件验证码、发送支付通知、发送营销邮件等场景。

在 Resend 后台 添加域名，设置 DNS 记录，验证域名

在 Resend 后台 创建 API 密钥，并复制 API 密钥

在 ShipAny 项目配置文件中，填写 Resend 相关的配置信息。

比如在 Resend 后台配置的邮件域名是 mail.shipany.ai，则发件人邮箱可以配置为 [email protected] / [email protected] / [email protected] 等。

在需要发邮件的地方，根据具体场景，选择合适的发送方式。

React Email 内置大量邮件组件，可以让你更轻松创建邮件模板。

比如在 @/components/email-templates/react-email.tsx 中写入内容：

除了自己实现邮件模板，你也可以在 React Email 模板市场 选择一个模板，修改后直接使用。

**Examples:**

Example 1 (unknown):
```unknown
RESEND_API_KEY = "re_xxx"
RESEND_SENDER_EMAIL = "[email protected]"
```

Example 2 (unknown):
```unknown
RESEND_API_KEY = "re_xxx"
RESEND_SENDER_EMAIL = "[email protected]"
```

Example 3 (python):
```python
import { Resend } from "resend";
 
const resend = new Resend(process.env.RESEND_API_KEY!);
 
const result = await resend.emails.send({
  from: process.env.RESEND_SENDER_EMAIL!,
  to: ["[email protected]"],
  subject: "Hello from ShipAny with Resend",
  text: "Hello World.",
});
 
console.log("send email result", result);
```

Example 4 (python):
```python
import { Resend } from "resend";
 
const resend = new Resend(process.env.RESEND_API_KEY!);
 
const result = await resend.emails.send({
  from: process.env.RESEND_SENDER_EMAIL!,
  to: ["[email protected]"],
  subject: "Hello from ShipAny with Resend",
  text: "Hello World.",
});
 
console.log("send email result", result);
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/features/analytics#参考

**Contents:**
- 数据统计
- 谷歌数据统计
- OpenPanel 统计
- 参考

目前数据统计仅支持 Google Analytics 和 OpenPanel。后续会逐步支持 Plausible 和 Umami 等统计工具。

注册 OpenPanel 账号，参考官网文档，创建统计实例

在实例的管理后台，创建一个统计客户端，得到 Client ID

**Examples:**

Example 1 (unknown):
```unknown
NEXT_PUBLIC_GOOGLE_ANALYTICS_ID = "G-1TPQYZXS53"
```

Example 2 (unknown):
```unknown
NEXT_PUBLIC_GOOGLE_ANALYTICS_ID = "G-1TPQYZXS53"
```

Example 3 (unknown):
```unknown
NEXT_PUBLIC_OPENPANEL_CLIENT_ID = "xxx-xxx-xxx-xxx"
```

Example 4 (unknown):
```unknown
NEXT_PUBLIC_OPENPANEL_CLIENT_ID = "xxx-xxx-xxx-xxx"
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/features/seo#设置多语言文案

**Contents:**
- SEO
- 设置多语言文案
- 设置站点地图
- 网页 SEO 走查
- Metadata 配置
- 接入 GSC

ShipAny 做了很多 SEO 优化，可以让你的项目在搜索引擎中获得更好的排名。

在 i18n/messages 目录下，通过 [locale].json 文件配置页面内容，默认支持中文和英文，在 i18n/messages/ 目录下，可以看到 en.json 和 zh.json 两个文件，在项目发布之前，修改成跟你项目相符合的文案即可。

修改 public/sitemap.xml 文件，配置成你自己的站点信息

按需修改 public/robots.txt 内容

检查网站首页的 title / description / Canonical 是否合理

用 AI 辅助修改 i18n/pages/landing 下 json 文件对应的网页内容，调整网站主打的关键词密度。(3% 左右比较合理)

ShipAny 对默认的 landing page 做了内容结构优化。如果你有自定义页面组件，需要检查页面的结构是否合理。

在 AITDK 插件的 Issues 面板开启 SSR Check，检测网页是否是服务端渲染。

如果你有创建新的页面路由 (page.tsx)，可以配置一下新页面的 Metadata 信息。

为子页面设置独立的 title / description / canonical 信息，有利于 SEO。

网站上站后，在 Google Search Console 中添加你的站点，可以查看网站的搜索流量和排名情况。

**Examples:**

Example 1 (unknown):
```unknown
update content of this file, for my new project "Flux AI", which is an AI Image Generator, with keywords "flux ai, ai image generator"
```

Example 2 (unknown):
```unknown
update content of this file, for my new project "Flux AI", which is an AI Image Generator, with keywords "flux ai, ai image generator"
```

Example 3 (unknown):
```unknown
<?xml version='1.0' encoding='utf-8' standalone='yes'?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://shipany.ai/</loc>
    <lastmod>2024-12-24T10:00:00+00:00</lastmod>
  </url>
</urlset>
```

Example 4 (unknown):
```unknown
<?xml version='1.0' encoding='utf-8' standalone='yes'?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://shipany.ai/</loc>
    <lastmod>2024-12-24T10:00:00+00:00</lastmod>
  </url>
</urlset>
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/features/i18n#支持更多语言

**Contents:**
- 国际化
- 项目国际化
- 落地页国际化
- 支持更多语言
- 参考

ShipAny 使用 next-intl 默认支持国际化。只需要简单的配置，即可开启。

项目国际化，包括 ShipAny 项目启动后看到的页面 title，SEO 信息，登陆框文案等。

在 i18n/messages 目录下，通过 [locale].json 文件配置页面内容，默认支持中文和英文，在 i18n/messages/ 目录下，可以看到 en.json 和 zh.json 两个文件，在项目发布之前，修改成跟你项目相符合的文案即可。

落地页的内容，在 i18n/pages/landing 目录下，通过 [locale].json 文件进行配置。

默认支持 en.json 和 zh.json 两个文件，在项目发布之前，修改成跟你项目相符合的文案即可。

除了默认的 en 和 zh 外，如果你还需要支持更多的语言，比如日语：ja，韩语：ko，法语：fr等，你可以按照以下步骤进行多语言配置：

在 i18n/messages 目录和 i18n/pages/landing 目录下，添加对应的语言文件，比如 ja.json 和 ko.json， fr.json 等。

修改 i18n/locale.ts 文件，添加更多语言支持

**Examples:**

Example 1 (unknown):
```unknown
update content of this file, for my new project "Flux AI", which is an AI Image Generator, with keywords "flux ai, ai image generator"
```

Example 2 (unknown):
```unknown
update content of this file, for my new project "Flux AI", which is an AI Image Generator, with keywords "flux ai, ai image generator"
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

**URL:** https://docs.shipany.ai/zh/features/payment/stripe#shipany-配置

**Contents:**
- Stripe
- Stripe 设置
- ShipAny 配置
- 价格表支付
  - 配置价格表内容
  - 修改价格表组件
  - 修改价格表下单逻辑
  - 修改支付回调逻辑
  - 修改支付通知逻辑
- 自定义支付

ShipAny 支持使用 Stripe 进行支付，可用于产品付款、会员订阅、购买积分等场景。

在 ShipAny 项目配置文件中，填写 Stripe 相关的配置信息。

页面路径可以填相对路径，也可以填绝对路径。如果填的是相对路径，跳转时会自动拼接 NEXT_PUBLIC_WEB_URL 配置的网站地址，并带上多语言参数。

比如按照以上配置，在中文页面支付成功后的跳转路径是：http://localhost:3000/zh/my-orders

ShipAny 模板内置了一个价格表和对应的支付逻辑，你可以根据自己的需求，简单修改即可快速实现支付功能。

ShipAny 模板内置的价格表配置文件位于：src/i18n/pages/pricing 目录下，支持多语言，默认包含 en.json 和 zh.json 两个价格表配置文件。

你可以根据自己的需求，修改价格表配置文件中的内容。

默认的价格表组件位于：src/components/blocks/pricing/index.tsx

你可以根据自己的需求，修改价格表的展示形式。

默认的价格表下单逻辑位于：src/app/api/checkout/route.ts

你可以根据自己的需求，修改价格表的下单逻辑。

在价格表下单逻辑中，默认配置的支付回调地址是：/api/pay/callback/stripe

用户支付后，会在浏览器跳转到这个地址，并带上包含支付信息的参数。

默认的支付回调处理逻辑位于：src/app/api/pay/callback/stripe/route.ts

你可以根据自己的需求，修改处理支付回调的逻辑，比如更新订单状态、给用户发送邮件通知、给用户赠送积分等。

支付回调是同步逻辑，依赖浏览器跳转到回调地址，才能处理支付结果。这种方式不太可靠，可能出现跳转过程中用户关闭了浏览器等情况，导致支付结果没有被正常处理。 更可靠的方式是通过 Webhook，配置支付结果异步通知。

比如把 Webhook 地址配置为：https://your-domain.com/api/pay/notify/stripe

用户支付后，Stripe 会把支付信息推送到这个地址。

默认的支付通知逻辑位于：src/app/api/pay/notify/stripe/route.ts

你可以根据自己的需求，修改处理支付通知的逻辑，比如更新订单状态、给用户发送邮件通知、给用户赠送积分等。

修改价格表配置文件，添加 groups 数据，配置多个价格分组。并在 pricing.items 下为每一个价格方案，设置一个 group 名称。

配置完成后，点击价格分组，将根据 group 字段，切换显示不同的价格方案。

ShipAny 模板使用 Stripe 支付时，默认支持三种支付方案

你只需要修改价格表配置，把每个价格方案的 interval 字段，设置成上述三个值之一。

同时，按需修改价格(amount) / 积分(credits) / 有效期(valid_months) 等字段。

举例：按月订阅扣费，月付 $99，购买后得到 30 个积分，有效期 1 个月，则核心的价格表配置信息为：

修改 src/app/api/checkout/route.ts 文件，设置 Stripe 下单的 options 参数。

在 Stripe 后台 设置支付方式，开通支付宝和微信支付。

修改价格表配置文件，在每个价格方案下添加一个 cn_amount 字段，即可支持人民币支付。

比如，产品售价，$99，人民币支付价格为 699 元，核心配置信息为：

配置完成后，在价格表下单按钮上方，将会显示一个人民币支付图标。

在 Stripe 后台点击左上角的店铺打开下拉菜单，依次点击 Switch to sandbox -> Test mode，开启测试模式。

在测试模式下，进入开发者中心，设置 测试支付密钥，包括 Publishable key 和 Secret key。

注册 ngrok 账号，按指示安装 ngrok 命令行工具。

启动 ngrok 服务，监听本地端口，并生成一个临时的域名。

在 Stripe 后台测试模式中，配置 Webhook 地址为 ngrok 生成的域名，并监听以下两个事件：

Endpoint 填写支付通知地址，比如 https://xxx.ngrok-free.app/api/pay/notify/stripe。

添加 Webhook 地址后，在 Webhook 管理页面，复制 Signing secret，

跟支付密钥一起填入 .env.development 文件中。

在本地启动项目，访问 /pricing 页面，点击下单按钮，下单成功后跳转到支付页面。

使用 Stripe 测试卡 支付，支付成功后浏览器跳转到支付回调地址，监听的地址收到支付通知。

**Examples:**

Example 1 (unknown):
```unknown
NEXT_PUBLIC_WEB_URL = "http://localhost:3000"

NEXT_PUBLIC_PAY_SUCCESS_URL = "/my-orders"
NEXT_PUBLIC_PAY_FAIL_URL = "/pricing"
NEXT_PUBLIC_PAY_CANCEL_URL = "/pricing"

PAY_PROVIDER = "stripe"

STRIPE_PUBLIC_KEY = "pk_test_xxx"
STRIPE_PRIVATE_KEY = "sk_test_xxx"
STRIPE_WEBHOOK_SECRET = "whsec_cexxx"
```

Example 2 (unknown):
```unknown
NEXT_PUBLIC_WEB_URL = "http://localhost:3000"

NEXT_PUBLIC_PAY_SUCCESS_URL = "/my-orders"
NEXT_PUBLIC_PAY_FAIL_URL = "/pricing"
NEXT_PUBLIC_PAY_CANCEL_URL = "/pricing"

PAY_PROVIDER = "stripe"

STRIPE_PUBLIC_KEY = "pk_test_xxx"
STRIPE_PRIVATE_KEY = "sk_test_xxx"
STRIPE_WEBHOOK_SECRET = "whsec_cexxx"
```

Example 3 (unknown):
```unknown
{
  "pricing": {
    "name": "pricing",
    "label": "Pricing",
    "title": "Pricing",
    "description": "Get all features of ShipAny, Ship your AI SaaS startups fast.",
    "groups": [],
    "items": [
      {
        "title": "Starter",
        "description": "Get started with your first SaaS startup.",
        "features_title": "Includes",
        "features": [
          "100 credits, valid for 1 month",
          "NextJS boilerplate",
          "SEO-friendly structure",
          "Payment with Stripe",
          "Data storage with Supabase",
          "Google Oauth & One-Tap Login",
    
...
```

Example 4 (unknown):
```unknown
{
  "pricing": {
    "name": "pricing",
    "label": "Pricing",
    "title": "Pricing",
    "description": "Get all features of ShipAny, Ship your AI SaaS startups fast.",
    "groups": [],
    "items": [
      {
        "title": "Starter",
        "description": "Get started with your first SaaS startup.",
        "features_title": "Includes",
        "features": [
          "100 credits, valid for 1 month",
          "NextJS boilerplate",
          "SEO-friendly structure",
          "Payment with Stripe",
          "Data storage with Supabase",
          "Google Oauth & One-Tap Login",
    
...
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/features/payment/stripe#修改支付通知逻辑

**Contents:**
- Stripe
- Stripe 设置
- ShipAny 配置
- 价格表支付
  - 配置价格表内容
  - 修改价格表组件
  - 修改价格表下单逻辑
  - 修改支付回调逻辑
  - 修改支付通知逻辑
- 自定义支付

ShipAny 支持使用 Stripe 进行支付，可用于产品付款、会员订阅、购买积分等场景。

在 ShipAny 项目配置文件中，填写 Stripe 相关的配置信息。

页面路径可以填相对路径，也可以填绝对路径。如果填的是相对路径，跳转时会自动拼接 NEXT_PUBLIC_WEB_URL 配置的网站地址，并带上多语言参数。

比如按照以上配置，在中文页面支付成功后的跳转路径是：http://localhost:3000/zh/my-orders

ShipAny 模板内置了一个价格表和对应的支付逻辑，你可以根据自己的需求，简单修改即可快速实现支付功能。

ShipAny 模板内置的价格表配置文件位于：src/i18n/pages/pricing 目录下，支持多语言，默认包含 en.json 和 zh.json 两个价格表配置文件。

你可以根据自己的需求，修改价格表配置文件中的内容。

默认的价格表组件位于：src/components/blocks/pricing/index.tsx

你可以根据自己的需求，修改价格表的展示形式。

默认的价格表下单逻辑位于：src/app/api/checkout/route.ts

你可以根据自己的需求，修改价格表的下单逻辑。

在价格表下单逻辑中，默认配置的支付回调地址是：/api/pay/callback/stripe

用户支付后，会在浏览器跳转到这个地址，并带上包含支付信息的参数。

默认的支付回调处理逻辑位于：src/app/api/pay/callback/stripe/route.ts

你可以根据自己的需求，修改处理支付回调的逻辑，比如更新订单状态、给用户发送邮件通知、给用户赠送积分等。

支付回调是同步逻辑，依赖浏览器跳转到回调地址，才能处理支付结果。这种方式不太可靠，可能出现跳转过程中用户关闭了浏览器等情况，导致支付结果没有被正常处理。 更可靠的方式是通过 Webhook，配置支付结果异步通知。

比如把 Webhook 地址配置为：https://your-domain.com/api/pay/notify/stripe

用户支付后，Stripe 会把支付信息推送到这个地址。

默认的支付通知逻辑位于：src/app/api/pay/notify/stripe/route.ts

你可以根据自己的需求，修改处理支付通知的逻辑，比如更新订单状态、给用户发送邮件通知、给用户赠送积分等。

修改价格表配置文件，添加 groups 数据，配置多个价格分组。并在 pricing.items 下为每一个价格方案，设置一个 group 名称。

配置完成后，点击价格分组，将根据 group 字段，切换显示不同的价格方案。

ShipAny 模板使用 Stripe 支付时，默认支持三种支付方案

你只需要修改价格表配置，把每个价格方案的 interval 字段，设置成上述三个值之一。

同时，按需修改价格(amount) / 积分(credits) / 有效期(valid_months) 等字段。

举例：按月订阅扣费，月付 $99，购买后得到 30 个积分，有效期 1 个月，则核心的价格表配置信息为：

修改 src/app/api/checkout/route.ts 文件，设置 Stripe 下单的 options 参数。

在 Stripe 后台 设置支付方式，开通支付宝和微信支付。

修改价格表配置文件，在每个价格方案下添加一个 cn_amount 字段，即可支持人民币支付。

比如，产品售价，$99，人民币支付价格为 699 元，核心配置信息为：

配置完成后，在价格表下单按钮上方，将会显示一个人民币支付图标。

在 Stripe 后台点击左上角的店铺打开下拉菜单，依次点击 Switch to sandbox -> Test mode，开启测试模式。

在测试模式下，进入开发者中心，设置 测试支付密钥，包括 Publishable key 和 Secret key。

注册 ngrok 账号，按指示安装 ngrok 命令行工具。

启动 ngrok 服务，监听本地端口，并生成一个临时的域名。

在 Stripe 后台测试模式中，配置 Webhook 地址为 ngrok 生成的域名，并监听以下两个事件：

Endpoint 填写支付通知地址，比如 https://xxx.ngrok-free.app/api/pay/notify/stripe。

添加 Webhook 地址后，在 Webhook 管理页面，复制 Signing secret，

跟支付密钥一起填入 .env.development 文件中。

在本地启动项目，访问 /pricing 页面，点击下单按钮，下单成功后跳转到支付页面。

使用 Stripe 测试卡 支付，支付成功后浏览器跳转到支付回调地址，监听的地址收到支付通知。

**Examples:**

Example 1 (unknown):
```unknown
NEXT_PUBLIC_WEB_URL = "http://localhost:3000"

NEXT_PUBLIC_PAY_SUCCESS_URL = "/my-orders"
NEXT_PUBLIC_PAY_FAIL_URL = "/pricing"
NEXT_PUBLIC_PAY_CANCEL_URL = "/pricing"

PAY_PROVIDER = "stripe"

STRIPE_PUBLIC_KEY = "pk_test_xxx"
STRIPE_PRIVATE_KEY = "sk_test_xxx"
STRIPE_WEBHOOK_SECRET = "whsec_cexxx"
```

Example 2 (unknown):
```unknown
NEXT_PUBLIC_WEB_URL = "http://localhost:3000"

NEXT_PUBLIC_PAY_SUCCESS_URL = "/my-orders"
NEXT_PUBLIC_PAY_FAIL_URL = "/pricing"
NEXT_PUBLIC_PAY_CANCEL_URL = "/pricing"

PAY_PROVIDER = "stripe"

STRIPE_PUBLIC_KEY = "pk_test_xxx"
STRIPE_PRIVATE_KEY = "sk_test_xxx"
STRIPE_WEBHOOK_SECRET = "whsec_cexxx"
```

Example 3 (unknown):
```unknown
{
  "pricing": {
    "name": "pricing",
    "label": "Pricing",
    "title": "Pricing",
    "description": "Get all features of ShipAny, Ship your AI SaaS startups fast.",
    "groups": [],
    "items": [
      {
        "title": "Starter",
        "description": "Get started with your first SaaS startup.",
        "features_title": "Includes",
        "features": [
          "100 credits, valid for 1 month",
          "NextJS boilerplate",
          "SEO-friendly structure",
          "Payment with Stripe",
          "Data storage with Supabase",
          "Google Oauth & One-Tap Login",
    
...
```

Example 4 (unknown):
```unknown
{
  "pricing": {
    "name": "pricing",
    "label": "Pricing",
    "title": "Pricing",
    "description": "Get all features of ShipAny, Ship your AI SaaS startups fast.",
    "groups": [],
    "items": [
      {
        "title": "Starter",
        "description": "Get started with your first SaaS startup.",
        "features_title": "Includes",
        "features": [
          "100 credits, valid for 1 month",
          "NextJS boilerplate",
          "SEO-friendly structure",
          "Payment with Stripe",
          "Data storage with Supabase",
          "Google Oauth & One-Tap Login",
    
...
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/features/email/resend#发送模板邮件

**Contents:**
- Resend
- Resend 设置
- ShipAny 配置
- 发送邮件
  - 发送文本邮件
  - 发送 HTML 邮件
  - 发送模板邮件
  - 使用 React Email
- 参考

ShipAny 支持使用 Resend 发送邮件，可用于发送邮件验证码、发送支付通知、发送营销邮件等场景。

在 Resend 后台 添加域名，设置 DNS 记录，验证域名

在 Resend 后台 创建 API 密钥，并复制 API 密钥

在 ShipAny 项目配置文件中，填写 Resend 相关的配置信息。

比如在 Resend 后台配置的邮件域名是 mail.shipany.ai，则发件人邮箱可以配置为 [email protected] / [email protected] / [email protected] 等。

在需要发邮件的地方，根据具体场景，选择合适的发送方式。

React Email 内置大量邮件组件，可以让你更轻松创建邮件模板。

比如在 @/components/email-templates/react-email.tsx 中写入内容：

除了自己实现邮件模板，你也可以在 React Email 模板市场 选择一个模板，修改后直接使用。

**Examples:**

Example 1 (unknown):
```unknown
RESEND_API_KEY = "re_xxx"
RESEND_SENDER_EMAIL = "[email protected]"
```

Example 2 (unknown):
```unknown
RESEND_API_KEY = "re_xxx"
RESEND_SENDER_EMAIL = "[email protected]"
```

Example 3 (python):
```python
import { Resend } from "resend";
 
const resend = new Resend(process.env.RESEND_API_KEY!);
 
const result = await resend.emails.send({
  from: process.env.RESEND_SENDER_EMAIL!,
  to: ["[email protected]"],
  subject: "Hello from ShipAny with Resend",
  text: "Hello World.",
});
 
console.log("send email result", result);
```

Example 4 (python):
```python
import { Resend } from "resend";
 
const resend = new Resend(process.env.RESEND_API_KEY!);
 
const result = await resend.emails.send({
  from: process.env.RESEND_SENDER_EMAIL!,
  to: ["[email protected]"],
  subject: "Hello from ShipAny with Resend",
  text: "Hello World.",
});
 
console.log("send email result", result);
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/features/i18n#项目国际化

**Contents:**
- 国际化
- 项目国际化
- 落地页国际化
- 支持更多语言
- 参考

ShipAny 使用 next-intl 默认支持国际化。只需要简单的配置，即可开启。

项目国际化，包括 ShipAny 项目启动后看到的页面 title，SEO 信息，登陆框文案等。

在 i18n/messages 目录下，通过 [locale].json 文件配置页面内容，默认支持中文和英文，在 i18n/messages/ 目录下，可以看到 en.json 和 zh.json 两个文件，在项目发布之前，修改成跟你项目相符合的文案即可。

落地页的内容，在 i18n/pages/landing 目录下，通过 [locale].json 文件进行配置。

默认支持 en.json 和 zh.json 两个文件，在项目发布之前，修改成跟你项目相符合的文案即可。

除了默认的 en 和 zh 外，如果你还需要支持更多的语言，比如日语：ja，韩语：ko，法语：fr等，你可以按照以下步骤进行多语言配置：

在 i18n/messages 目录和 i18n/pages/landing 目录下，添加对应的语言文件，比如 ja.json 和 ko.json， fr.json 等。

修改 i18n/locale.ts 文件，添加更多语言支持

**Examples:**

Example 1 (unknown):
```unknown
update content of this file, for my new project "Flux AI", which is an AI Image Generator, with keywords "flux ai, ai image generator"
```

Example 2 (unknown):
```unknown
update content of this file, for my new project "Flux AI", which is an AI Image Generator, with keywords "flux ai, ai image generator"
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

**URL:** https://docs.shipany.ai/zh/features/oauth#github-登录

**Contents:**
- 登录鉴权
- 生成 Auth Secret
- 谷歌登录
- 谷歌一键登录
- Github 登录
- 登录预览
- 参考

ShipAny 目前支持 谷歌登录 / 谷歌一键登录 / Github 登录三种登录方式。

其他登录方式逐步集成，也可以参考 next-auth 文档自行接入。

生成一个 32 字节的随机字符串，作为 Auth Secret

修改环境变量中的 AUTH_SECRET 值

创建一个新项目，进入新项目的 Credentials 管理页面，创建 Oauth Client ID

创建 Oauth Client ID 后，得到 Client ID 和 Client Secret

首先按照谷歌登录的步骤，拿到 AUTH_GOOGLE_ID 和 AUTH_GOOGLE_SECRET

修改配置文件中的 NEXT_PUBLIC_AUTH_GOOGLE_ONE_TAP_ENABLED 和 NEXT_PUBLIC_AUTH_GOOGLE_ID

谷歌一键登录使用到的 NEXT_PUBLIC_AUTH_GOOGLE_ID 跟谷歌登录配置的 AUTH_GOOGLE_ID 保持一致。

开发环境和生产环境，需要创建两个不同的 OAuth app，分别配置不同的回调地址。

进入 OAuth app，复制 Client ID 和 Client Secret

修改配置文件中的 AUTH_GITHUB_ID 和 AUTH_GITHUB_SECRET

**Examples:**

Example 1 (unknown):
```unknown
openssl rand -base64 32
```

Example 2 (unknown):
```unknown
openssl rand -base64 32
```

Example 3 (unknown):
```unknown
AUTH_SECRET = "xxx"
```

Example 4 (unknown):
```unknown
AUTH_SECRET = "xxx"
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/features/storage#配置云存储

**Contents:**
- 文件存储
- 配置云存储
- 上传 AI 图片到云存储
- 读取本地文件上传到云存储
- 下载远程图片上传到云存储
- 参考

ShipAny 支持上传文件到 AWS S3 兼容的文件存储系统，例如 AWS S3 / Cloudflare R2 / 腾讯云 COS 等。

选择你的云存储平台，创建存储桶，设置访问密钥和访问域名。

把 aisdk 生成的图片（返回的 base64 数据），上传到云存储。

uploadFile 接收的 body 参数是 Buffer 类型。你可以传递从 URL 下载的文件 Buffer 或者从本地文件读取的 Buffer。

注意：path 和 readFile 在 edge runtime 中无法使用，所以在 cloudflare 部署时，不能读取本地文件。

给定一个远程的图片地址，下载图片并上传到云存储。

**Examples:**

Example 1 (unknown):
```unknown
STORAGE_ENDPOINT = ""
STORAGE_REGION = ""
STORAGE_ACCESS_KEY = ""
STORAGE_SECRET_KEY = ""
STORAGE_BUCKET = ""
STORAGE_DOMAIN = ""
```

Example 2 (unknown):
```unknown
STORAGE_ENDPOINT = ""
STORAGE_REGION = ""
STORAGE_ACCESS_KEY = ""
STORAGE_SECRET_KEY = ""
STORAGE_BUCKET = ""
STORAGE_DOMAIN = ""
```

Example 3 (python):
```python
import { newStorage } from "@/lib/storage";
 
const storage = new Storage();
 
const filename = `image_${new Date().getTime()}.png`;
const key = `shipany/${filename}`;
const body = Buffer.from(image.base64, "base64");
 
try {
  const res = await storage.uploadFile({
    body,
    key,
    contentType: "image/png",
    disposition: "inline",
  });
 
  console.log("upload file success:", res);
} catch (err) {
  console.log("upload file failed:", err);
}
```

Example 4 (python):
```python
import { newStorage } from "@/lib/storage";
 
const storage = new Storage();
 
const filename = `image_${new Date().getTime()}.png`;
const key = `shipany/${filename}`;
const body = Buffer.from(image.base64, "base64");
 
try {
  const res = await storage.uploadFile({
    body,
    key,
    contentType: "image/png",
    disposition: "inline",
  });
 
  console.log("upload file success:", res);
} catch (err) {
  console.log("upload file failed:", err);
}
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/features/affiliate

**Contents:**
- 邀请返佣
- 如何使用
- 如何自定义奖励金额和比例

ShipAny 实现了一套邀请返佣系统。你可以在你的产品中使用这套系统来激励用户邀请新用户。

用户进入：http://localhost:3000/my-invites 页面，可以生成自己的邀请链接。

http://localhost:3000/i/idoubi

新用户通过分享者的邀请链接进入系统，会自动关联到分享者。

分享者可以在 /my-invites 页面查看邀请记录和邀请奖励

暂不支持在线自动提现，需要管理员人工联系用户发放奖励。

你可以修改此接口的逻辑，更改新用户注册场景下的奖励规则。

默认的 AffiliateRewardPercent.Invited 和 AffiliateRewardAmount.Invited 都是 0.

你可以修改此方法内的逻辑，修改被邀请人支付的订单，给到邀请人的奖励

默认的 AffiliateRewardPercent.Paied 值是 20，代表返佣比例是 20%

默认的 AffiliateRewardAmount.Paied 值是 50，代表返佣金额是 $50

**Examples:**

Example 1 (unknown):
```unknown
await insertAffiliate({
  user_uuid: user_uuid,
  invited_by: inviteUser.uuid,
  created_at: getIsoTimestr(),
  status: AffiliateStatus.Pending,
  paid_order_no: "",
  paid_amount: 0,
  reward_percent: AffiliateRewardPercent.Invited,
  reward_amount: AffiliateRewardAmount.Invited,
});
```

Example 2 (unknown):
```unknown
await insertAffiliate({
  user_uuid: user_uuid,
  invited_by: inviteUser.uuid,
  created_at: getIsoTimestr(),
  status: AffiliateStatus.Pending,
  paid_order_no: "",
  paid_amount: 0,
  reward_percent: AffiliateRewardPercent.Invited,
  reward_amount: AffiliateRewardAmount.Invited,
});
```

Example 3 (python):
```python
import { findAffiliateByOrderNo, insertAffiliate } from "@/models/affiliate";
 
import { AffiliateRewardAmount } from "./constant";
import { AffiliateRewardPercent } from "./constant";
import { AffiliateStatus } from "./constant";
import { Order } from "@/types/order";
import { findUserByUuid } from "@/models/user";
import { getIsoTimestr } from "@/lib/time";
 
export async function updateAffiliateForOrder(order: Order) {
  try {
    const user = await findUserByUuid(order.user_uuid);
    if (user && user.uuid && user.invited_by && user.invited_by !== user.uuid) {
      const affiliate = await
...
```

Example 4 (python):
```python
import { findAffiliateByOrderNo, insertAffiliate } from "@/models/affiliate";
 
import { AffiliateRewardAmount } from "./constant";
import { AffiliateRewardPercent } from "./constant";
import { AffiliateStatus } from "./constant";
import { Order } from "@/types/order";
import { findUserByUuid } from "@/models/user";
import { getIsoTimestr } from "@/lib/time";
 
export async function updateAffiliateForOrder(order: Order) {
  try {
    const user = await findUserByUuid(order.user_uuid);
    if (user && user.uuid && user.invited_by && user.invited_by !== user.uuid) {
      const affiliate = await
...
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/features/payment/creem#修改支付回调逻辑

**Contents:**
- Creem
- Creem 设置
- ShipAny 配置
- 价格表支付
  - 配置价格表内容
  - 修改价格表组件
  - 修改价格表下单逻辑
  - 修改支付回调逻辑
  - 修改支付通知逻辑
- 本地测试

ShipAny 支持使用 Creem 进行支付，可用于产品付款、会员订阅、购买积分等场景。

在 ShipAny 项目配置文件中，填写 Creem 相关的配置信息。

页面路径可以填相对路径，也可以填绝对路径。如果填的是相对路径，跳转时会自动拼接 NEXT_PUBLIC_WEB_URL 配置的网站地址，并带上多语言参数。

比如按照以上配置，在中文页面支付成功后的跳转路径是：http://localhost:3000/zh/my-orders

比如在 ShipAny 项目中设置的价格表有三个支付方案，对应的 product_id 分别是 starter、standard、premium，你需要在 Creem 后台为这三个方案 创建对应的产品，复制每个产品的 Product ID，与价格表中的 product_id 对应关系填写到 CREEM_PRODUCTS 中。

ShipAny 模板内置了一个价格表和对应的支付逻辑，你可以根据自己的需求，简单修改即可快速实现支付功能。

ShipAny 模板内置的价格表配置文件位于：src/i18n/pages/pricing 目录下，支持多语言，默认包含 en.json 和 zh.json 两个价格表配置文件。

你可以根据自己的需求，修改价格表配置文件中的内容。

默认的价格表组件位于：src/components/blocks/pricing/index.tsx

你可以根据自己的需求，修改价格表的展示形式。

默认的价格表下单逻辑位于：src/app/api/checkout/route.ts

你可以根据自己的需求，修改价格表的下单逻辑。

在价格表下单逻辑中，默认配置的支付回调地址是：/api/pay/callback/creem

用户支付后，会在浏览器跳转到这个地址，并带上包含支付信息的参数。

默认的支付回调处理逻辑位于：src/app/api/pay/callback/creem/route.ts

你可以根据自己的需求，修改处理支付回调的逻辑，比如更新订单状态、给用户发送邮件通知、给用户赠送积分等。

支付回调是同步逻辑，依赖浏览器跳转到回调地址，才能处理支付结果。这种方式不太可靠，可能出现跳转过程中用户关闭了浏览器等情况，导致支付结果没有被正常处理。 更可靠的方式是通过 Webhook，配置支付结果异步通知。

比如把 Webhook 地址配置为：https://your-domain.com/api/pay/notify/creem

用户支付后，Creem 会把支付信息推送到这个地址。

默认的支付通知逻辑位于：src/app/api/pay/notify/creem/route.ts

你可以根据自己的需求，修改处理支付通知的逻辑，比如更新订单状态、给用户发送邮件通知、给用户赠送积分等。

在 Creem 后台进入店铺，点击右上角的 Test mode，开启测试模式。

在测试模式下，进入开发者中心，设置 测试 API 密钥。

注册 ngrok 账号，按指示安装 ngrok 命令行工具。

启动 ngrok 服务，监听本地端口，并生成一个临时的域名。

在 Creem 后台测试模式中，配置 Webhook 地址为 ngrok 生成的域名

Endpoint 填写支付通知地址，比如 https://xxx.ngrok-free.app/api/pay/notify/creem。

添加 Webhook 地址后，在 Webhook 管理页面，复制 Signing secret，

跟支付密钥一起填入 .env.development 文件中。

在本地启动项目，访问 /pricing 页面，点击下单按钮，下单成功后跳转到支付页面。

使用 Stripe 测试卡 支付，支付成功后浏览器跳转到支付回调地址，监听的地址收到支付通知。

**Examples:**

Example 1 (unknown):
```unknown
NEXT_PUBLIC_WEB_URL = "http://localhost:3000"

NEXT_PUBLIC_PAY_SUCCESS_URL = "/my-orders"
NEXT_PUBLIC_PAY_FAIL_URL = "/pricing"
NEXT_PUBLIC_PAY_CANCEL_URL = "/pricing"

PAY_PROVIDER = "creem"

CREEM_ENV = "test"
CREEM_API_KEY = "creem_test_xxx"
CREEM_WEBHOOK_SECRET = "whsec_xxx"
CREEM_PRODUCTS = '{"starter": "prod_xxx", "standard": "prod_xxx", "premium": "prod_xxx"}'
```

Example 2 (unknown):
```unknown
NEXT_PUBLIC_WEB_URL = "http://localhost:3000"

NEXT_PUBLIC_PAY_SUCCESS_URL = "/my-orders"
NEXT_PUBLIC_PAY_FAIL_URL = "/pricing"
NEXT_PUBLIC_PAY_CANCEL_URL = "/pricing"

PAY_PROVIDER = "creem"

CREEM_ENV = "test"
CREEM_API_KEY = "creem_test_xxx"
CREEM_WEBHOOK_SECRET = "whsec_xxx"
CREEM_PRODUCTS = '{"starter": "prod_xxx", "standard": "prod_xxx", "premium": "prod_xxx"}'
```

Example 3 (unknown):
```unknown
{
  "pricing": {
    "name": "pricing",
    "label": "Pricing",
    "title": "Pricing",
    "description": "Get all features of ShipAny, Ship your AI SaaS startups fast.",
    "groups": [],
    "items": [
      {
        "title": "Starter",
        "description": "Get started with your first SaaS startup.",
        "features_title": "Includes",
        "features": [
          "100 credits, valid for 1 month",
          "NextJS boilerplate",
          "SEO-friendly structure",
          "Payment with Stripe",
          "Data storage with Supabase",
          "Google Oauth & One-Tap Login",
    
...
```

Example 4 (unknown):
```unknown
{
  "pricing": {
    "name": "pricing",
    "label": "Pricing",
    "title": "Pricing",
    "description": "Get all features of ShipAny, Ship your AI SaaS startups fast.",
    "groups": [],
    "items": [
      {
        "title": "Starter",
        "description": "Get started with your first SaaS startup.",
        "features_title": "Includes",
        "features": [
          "100 credits, valid for 1 month",
          "NextJS boilerplate",
          "SEO-friendly structure",
          "Payment with Stripe",
          "Data storage with Supabase",
          "Google Oauth & One-Tap Login",
    
...
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/features/database#参考

**Contents:**
- 数据库
- 配置数据库
- 初始化数据库
- 更新数据库
- 管理数据库
- 操作数据库
- 使用其他类型数据库
- 参考

ShipAny 使用 drizzle-orm 支持多种类型数据库。

以 Supabase 数据库为例，在 ShipAny 配置数据库的流程为：

登录 Supabase 控制台，创建数据库

在 Supabase 控制台，进入你创建的数据库，点击上方的 Connect

在弹出来的框中复制数据库连接信息，类似这样的字符串：

[YOUR-PASSWORD] 需要替换成你在创建数据库时设置的密码。

修改项目配置文件：.env.development 和 .env.production

在配置好 DATABASE_URL 后，在项目根目录下运行以下命令，初始化数据库：

这个命令会执行 src/db/migrations 目录下的所有迁移文件，创建数据库表。

如果你通过 DATABASE_URL 配置的不是一个新创建的数据库，或者数据库之前已经存在 ShipAny 的库表信息，请不要执行以上命令。而是比较 src/db/migrations 目录下所有迁移文件的 sql 内容，手动执行 sql 语句，更新数据库表。

如果在项目创建之处，你使用的是一个新的数据库，且是通过 pnpm db:migrate 命令初始化的数据库，如果后续你拉取了最新的代码，可以继续执行以下命令，更新数据库表：

这个命令会根据 src/db/migrations 目录下所有迁移文件的 sql 内容，增量更新数据库表。

在项目根目录下执行命令：pnpm db:studio

这个命令会打开一个数据库管理界面，你可以在这里查看、编辑、删除数据库表。

在 src/models 目录下，写数据库操作文件，实现对数据表的增删改查。可参考以下操作 posts 表的示例：

数据表操作语法可参考 drizzle-orm 文档。

如果你使用自建的 Postgres 数据库，或者使用其他兼容 postgres 的云数据库，比如：Neon。配置和连接数据库的步骤跟使用 Supabase 一致，你只需要填写数据库的 DATABASE_URL 即可。

如果你需要使用 MySQL 或者 SQLite 等数据库，可参考以下步骤自定义：

修改 src/db/schema.ts 文件，使用新的数据库 Schema。

Schema 中数据表的字段定义，可以参考 drizzle-orm 文档。

修改 src/db/config.ts 文件，使用新的数据库连接配置。

默认是 Postgres 数据库连接配置，你可以参考 drizzle-orm 文档按需修改。

根据你使用的数据库类型，修改数据库连接实例。

如果你希望后续通过迁移文件更新数据库表。你可以在完成以上三步之后，在项目根目录下执行以下命令生成数据库迁移文件。

在 ShipAny 中配置不同类型的数据库非常简单，只需要完成以上四个步骤的自定义即可。src/model 下操作数据库的逻辑无需修改。

**Examples:**

Example 1 (unknown):
```unknown
postgresql://postgres.defqvdpquwyqqjlmurkg:[YOUR-PASSWORD]@aws-0-ap-southeast-1.pooler.supabase.com:6543/postgres
```

Example 2 (unknown):
```unknown
postgresql://postgres.defqvdpquwyqqjlmurkg:[YOUR-PASSWORD]@aws-0-ap-southeast-1.pooler.supabase.com:6543/postgres
```

Example 3 (unknown):
```unknown
DATABASE_URL="postgresql://postgres.defqvdpquwyqqjlmurkg:******@aws-0-ap-southeast-1.pooler.supabase.com:6543/postgres"
```

Example 4 (unknown):
```unknown
DATABASE_URL="postgresql://postgres.defqvdpquwyqqjlmurkg:******@aws-0-ap-southeast-1.pooler.supabase.com:6543/postgres"
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/features/i18n#落地页国际化

**Contents:**
- 国际化
- 项目国际化
- 落地页国际化
- 支持更多语言
- 参考

ShipAny 使用 next-intl 默认支持国际化。只需要简单的配置，即可开启。

项目国际化，包括 ShipAny 项目启动后看到的页面 title，SEO 信息，登陆框文案等。

在 i18n/messages 目录下，通过 [locale].json 文件配置页面内容，默认支持中文和英文，在 i18n/messages/ 目录下，可以看到 en.json 和 zh.json 两个文件，在项目发布之前，修改成跟你项目相符合的文案即可。

落地页的内容，在 i18n/pages/landing 目录下，通过 [locale].json 文件进行配置。

默认支持 en.json 和 zh.json 两个文件，在项目发布之前，修改成跟你项目相符合的文案即可。

除了默认的 en 和 zh 外，如果你还需要支持更多的语言，比如日语：ja，韩语：ko，法语：fr等，你可以按照以下步骤进行多语言配置：

在 i18n/messages 目录和 i18n/pages/landing 目录下，添加对应的语言文件，比如 ja.json 和 ko.json， fr.json 等。

修改 i18n/locale.ts 文件，添加更多语言支持

**Examples:**

Example 1 (unknown):
```unknown
update content of this file, for my new project "Flux AI", which is an AI Image Generator, with keywords "flux ai, ai image generator"
```

Example 2 (unknown):
```unknown
update content of this file, for my new project "Flux AI", which is an AI Image Generator, with keywords "flux ai, ai image generator"
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

**URL:** https://docs.shipany.ai/zh/features/payment/stripe#人民币支付

**Contents:**
- Stripe
- Stripe 设置
- ShipAny 配置
- 价格表支付
  - 配置价格表内容
  - 修改价格表组件
  - 修改价格表下单逻辑
  - 修改支付回调逻辑
  - 修改支付通知逻辑
- 自定义支付

ShipAny 支持使用 Stripe 进行支付，可用于产品付款、会员订阅、购买积分等场景。

在 ShipAny 项目配置文件中，填写 Stripe 相关的配置信息。

页面路径可以填相对路径，也可以填绝对路径。如果填的是相对路径，跳转时会自动拼接 NEXT_PUBLIC_WEB_URL 配置的网站地址，并带上多语言参数。

比如按照以上配置，在中文页面支付成功后的跳转路径是：http://localhost:3000/zh/my-orders

ShipAny 模板内置了一个价格表和对应的支付逻辑，你可以根据自己的需求，简单修改即可快速实现支付功能。

ShipAny 模板内置的价格表配置文件位于：src/i18n/pages/pricing 目录下，支持多语言，默认包含 en.json 和 zh.json 两个价格表配置文件。

你可以根据自己的需求，修改价格表配置文件中的内容。

默认的价格表组件位于：src/components/blocks/pricing/index.tsx

你可以根据自己的需求，修改价格表的展示形式。

默认的价格表下单逻辑位于：src/app/api/checkout/route.ts

你可以根据自己的需求，修改价格表的下单逻辑。

在价格表下单逻辑中，默认配置的支付回调地址是：/api/pay/callback/stripe

用户支付后，会在浏览器跳转到这个地址，并带上包含支付信息的参数。

默认的支付回调处理逻辑位于：src/app/api/pay/callback/stripe/route.ts

你可以根据自己的需求，修改处理支付回调的逻辑，比如更新订单状态、给用户发送邮件通知、给用户赠送积分等。

支付回调是同步逻辑，依赖浏览器跳转到回调地址，才能处理支付结果。这种方式不太可靠，可能出现跳转过程中用户关闭了浏览器等情况，导致支付结果没有被正常处理。 更可靠的方式是通过 Webhook，配置支付结果异步通知。

比如把 Webhook 地址配置为：https://your-domain.com/api/pay/notify/stripe

用户支付后，Stripe 会把支付信息推送到这个地址。

默认的支付通知逻辑位于：src/app/api/pay/notify/stripe/route.ts

你可以根据自己的需求，修改处理支付通知的逻辑，比如更新订单状态、给用户发送邮件通知、给用户赠送积分等。

修改价格表配置文件，添加 groups 数据，配置多个价格分组。并在 pricing.items 下为每一个价格方案，设置一个 group 名称。

配置完成后，点击价格分组，将根据 group 字段，切换显示不同的价格方案。

ShipAny 模板使用 Stripe 支付时，默认支持三种支付方案

你只需要修改价格表配置，把每个价格方案的 interval 字段，设置成上述三个值之一。

同时，按需修改价格(amount) / 积分(credits) / 有效期(valid_months) 等字段。

举例：按月订阅扣费，月付 $99，购买后得到 30 个积分，有效期 1 个月，则核心的价格表配置信息为：

修改 src/app/api/checkout/route.ts 文件，设置 Stripe 下单的 options 参数。

在 Stripe 后台 设置支付方式，开通支付宝和微信支付。

修改价格表配置文件，在每个价格方案下添加一个 cn_amount 字段，即可支持人民币支付。

比如，产品售价，$99，人民币支付价格为 699 元，核心配置信息为：

配置完成后，在价格表下单按钮上方，将会显示一个人民币支付图标。

在 Stripe 后台点击左上角的店铺打开下拉菜单，依次点击 Switch to sandbox -> Test mode，开启测试模式。

在测试模式下，进入开发者中心，设置 测试支付密钥，包括 Publishable key 和 Secret key。

注册 ngrok 账号，按指示安装 ngrok 命令行工具。

启动 ngrok 服务，监听本地端口，并生成一个临时的域名。

在 Stripe 后台测试模式中，配置 Webhook 地址为 ngrok 生成的域名，并监听以下两个事件：

Endpoint 填写支付通知地址，比如 https://xxx.ngrok-free.app/api/pay/notify/stripe。

添加 Webhook 地址后，在 Webhook 管理页面，复制 Signing secret，

跟支付密钥一起填入 .env.development 文件中。

在本地启动项目，访问 /pricing 页面，点击下单按钮，下单成功后跳转到支付页面。

使用 Stripe 测试卡 支付，支付成功后浏览器跳转到支付回调地址，监听的地址收到支付通知。

**Examples:**

Example 1 (unknown):
```unknown
NEXT_PUBLIC_WEB_URL = "http://localhost:3000"

NEXT_PUBLIC_PAY_SUCCESS_URL = "/my-orders"
NEXT_PUBLIC_PAY_FAIL_URL = "/pricing"
NEXT_PUBLIC_PAY_CANCEL_URL = "/pricing"

PAY_PROVIDER = "stripe"

STRIPE_PUBLIC_KEY = "pk_test_xxx"
STRIPE_PRIVATE_KEY = "sk_test_xxx"
STRIPE_WEBHOOK_SECRET = "whsec_cexxx"
```

Example 2 (unknown):
```unknown
NEXT_PUBLIC_WEB_URL = "http://localhost:3000"

NEXT_PUBLIC_PAY_SUCCESS_URL = "/my-orders"
NEXT_PUBLIC_PAY_FAIL_URL = "/pricing"
NEXT_PUBLIC_PAY_CANCEL_URL = "/pricing"

PAY_PROVIDER = "stripe"

STRIPE_PUBLIC_KEY = "pk_test_xxx"
STRIPE_PRIVATE_KEY = "sk_test_xxx"
STRIPE_WEBHOOK_SECRET = "whsec_cexxx"
```

Example 3 (unknown):
```unknown
{
  "pricing": {
    "name": "pricing",
    "label": "Pricing",
    "title": "Pricing",
    "description": "Get all features of ShipAny, Ship your AI SaaS startups fast.",
    "groups": [],
    "items": [
      {
        "title": "Starter",
        "description": "Get started with your first SaaS startup.",
        "features_title": "Includes",
        "features": [
          "100 credits, valid for 1 month",
          "NextJS boilerplate",
          "SEO-friendly structure",
          "Payment with Stripe",
          "Data storage with Supabase",
          "Google Oauth & One-Tap Login",
    
...
```

Example 4 (unknown):
```unknown
{
  "pricing": {
    "name": "pricing",
    "label": "Pricing",
    "title": "Pricing",
    "description": "Get all features of ShipAny, Ship your AI SaaS startups fast.",
    "groups": [],
    "items": [
      {
        "title": "Starter",
        "description": "Get started with your first SaaS startup.",
        "features_title": "Includes",
        "features": [
          "100 credits, valid for 1 month",
          "NextJS boilerplate",
          "SEO-friendly structure",
          "Payment with Stripe",
          "Data storage with Supabase",
          "Google Oauth & One-Tap Login",
    
...
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/features/email/resend#shipany-配置

**Contents:**
- Resend
- Resend 设置
- ShipAny 配置
- 发送邮件
  - 发送文本邮件
  - 发送 HTML 邮件
  - 发送模板邮件
  - 使用 React Email
- 参考

ShipAny 支持使用 Resend 发送邮件，可用于发送邮件验证码、发送支付通知、发送营销邮件等场景。

在 Resend 后台 添加域名，设置 DNS 记录，验证域名

在 Resend 后台 创建 API 密钥，并复制 API 密钥

在 ShipAny 项目配置文件中，填写 Resend 相关的配置信息。

比如在 Resend 后台配置的邮件域名是 mail.shipany.ai，则发件人邮箱可以配置为 [email protected] / [email protected] / [email protected] 等。

在需要发邮件的地方，根据具体场景，选择合适的发送方式。

React Email 内置大量邮件组件，可以让你更轻松创建邮件模板。

比如在 @/components/email-templates/react-email.tsx 中写入内容：

除了自己实现邮件模板，你也可以在 React Email 模板市场 选择一个模板，修改后直接使用。

**Examples:**

Example 1 (unknown):
```unknown
RESEND_API_KEY = "re_xxx"
RESEND_SENDER_EMAIL = "[email protected]"
```

Example 2 (unknown):
```unknown
RESEND_API_KEY = "re_xxx"
RESEND_SENDER_EMAIL = "[email protected]"
```

Example 3 (python):
```python
import { Resend } from "resend";
 
const resend = new Resend(process.env.RESEND_API_KEY!);
 
const result = await resend.emails.send({
  from: process.env.RESEND_SENDER_EMAIL!,
  to: ["[email protected]"],
  subject: "Hello from ShipAny with Resend",
  text: "Hello World.",
});
 
console.log("send email result", result);
```

Example 4 (python):
```python
import { Resend } from "resend";
 
const resend = new Resend(process.env.RESEND_API_KEY!);
 
const result = await resend.emails.send({
  from: process.env.RESEND_SENDER_EMAIL!,
  to: ["[email protected]"],
  subject: "Hello from ShipAny with Resend",
  text: "Hello World.",
});
 
console.log("send email result", result);
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/features/payment/stripe#分组价格表

**Contents:**
- Stripe
- Stripe 设置
- ShipAny 配置
- 价格表支付
  - 配置价格表内容
  - 修改价格表组件
  - 修改价格表下单逻辑
  - 修改支付回调逻辑
  - 修改支付通知逻辑
- 自定义支付

ShipAny 支持使用 Stripe 进行支付，可用于产品付款、会员订阅、购买积分等场景。

在 ShipAny 项目配置文件中，填写 Stripe 相关的配置信息。

页面路径可以填相对路径，也可以填绝对路径。如果填的是相对路径，跳转时会自动拼接 NEXT_PUBLIC_WEB_URL 配置的网站地址，并带上多语言参数。

比如按照以上配置，在中文页面支付成功后的跳转路径是：http://localhost:3000/zh/my-orders

ShipAny 模板内置了一个价格表和对应的支付逻辑，你可以根据自己的需求，简单修改即可快速实现支付功能。

ShipAny 模板内置的价格表配置文件位于：src/i18n/pages/pricing 目录下，支持多语言，默认包含 en.json 和 zh.json 两个价格表配置文件。

你可以根据自己的需求，修改价格表配置文件中的内容。

默认的价格表组件位于：src/components/blocks/pricing/index.tsx

你可以根据自己的需求，修改价格表的展示形式。

默认的价格表下单逻辑位于：src/app/api/checkout/route.ts

你可以根据自己的需求，修改价格表的下单逻辑。

在价格表下单逻辑中，默认配置的支付回调地址是：/api/pay/callback/stripe

用户支付后，会在浏览器跳转到这个地址，并带上包含支付信息的参数。

默认的支付回调处理逻辑位于：src/app/api/pay/callback/stripe/route.ts

你可以根据自己的需求，修改处理支付回调的逻辑，比如更新订单状态、给用户发送邮件通知、给用户赠送积分等。

支付回调是同步逻辑，依赖浏览器跳转到回调地址，才能处理支付结果。这种方式不太可靠，可能出现跳转过程中用户关闭了浏览器等情况，导致支付结果没有被正常处理。 更可靠的方式是通过 Webhook，配置支付结果异步通知。

比如把 Webhook 地址配置为：https://your-domain.com/api/pay/notify/stripe

用户支付后，Stripe 会把支付信息推送到这个地址。

默认的支付通知逻辑位于：src/app/api/pay/notify/stripe/route.ts

你可以根据自己的需求，修改处理支付通知的逻辑，比如更新订单状态、给用户发送邮件通知、给用户赠送积分等。

修改价格表配置文件，添加 groups 数据，配置多个价格分组。并在 pricing.items 下为每一个价格方案，设置一个 group 名称。

配置完成后，点击价格分组，将根据 group 字段，切换显示不同的价格方案。

ShipAny 模板使用 Stripe 支付时，默认支持三种支付方案

你只需要修改价格表配置，把每个价格方案的 interval 字段，设置成上述三个值之一。

同时，按需修改价格(amount) / 积分(credits) / 有效期(valid_months) 等字段。

举例：按月订阅扣费，月付 $99，购买后得到 30 个积分，有效期 1 个月，则核心的价格表配置信息为：

修改 src/app/api/checkout/route.ts 文件，设置 Stripe 下单的 options 参数。

在 Stripe 后台 设置支付方式，开通支付宝和微信支付。

修改价格表配置文件，在每个价格方案下添加一个 cn_amount 字段，即可支持人民币支付。

比如，产品售价，$99，人民币支付价格为 699 元，核心配置信息为：

配置完成后，在价格表下单按钮上方，将会显示一个人民币支付图标。

在 Stripe 后台点击左上角的店铺打开下拉菜单，依次点击 Switch to sandbox -> Test mode，开启测试模式。

在测试模式下，进入开发者中心，设置 测试支付密钥，包括 Publishable key 和 Secret key。

注册 ngrok 账号，按指示安装 ngrok 命令行工具。

启动 ngrok 服务，监听本地端口，并生成一个临时的域名。

在 Stripe 后台测试模式中，配置 Webhook 地址为 ngrok 生成的域名，并监听以下两个事件：

Endpoint 填写支付通知地址，比如 https://xxx.ngrok-free.app/api/pay/notify/stripe。

添加 Webhook 地址后，在 Webhook 管理页面，复制 Signing secret，

跟支付密钥一起填入 .env.development 文件中。

在本地启动项目，访问 /pricing 页面，点击下单按钮，下单成功后跳转到支付页面。

使用 Stripe 测试卡 支付，支付成功后浏览器跳转到支付回调地址，监听的地址收到支付通知。

**Examples:**

Example 1 (unknown):
```unknown
NEXT_PUBLIC_WEB_URL = "http://localhost:3000"

NEXT_PUBLIC_PAY_SUCCESS_URL = "/my-orders"
NEXT_PUBLIC_PAY_FAIL_URL = "/pricing"
NEXT_PUBLIC_PAY_CANCEL_URL = "/pricing"

PAY_PROVIDER = "stripe"

STRIPE_PUBLIC_KEY = "pk_test_xxx"
STRIPE_PRIVATE_KEY = "sk_test_xxx"
STRIPE_WEBHOOK_SECRET = "whsec_cexxx"
```

Example 2 (unknown):
```unknown
NEXT_PUBLIC_WEB_URL = "http://localhost:3000"

NEXT_PUBLIC_PAY_SUCCESS_URL = "/my-orders"
NEXT_PUBLIC_PAY_FAIL_URL = "/pricing"
NEXT_PUBLIC_PAY_CANCEL_URL = "/pricing"

PAY_PROVIDER = "stripe"

STRIPE_PUBLIC_KEY = "pk_test_xxx"
STRIPE_PRIVATE_KEY = "sk_test_xxx"
STRIPE_WEBHOOK_SECRET = "whsec_cexxx"
```

Example 3 (unknown):
```unknown
{
  "pricing": {
    "name": "pricing",
    "label": "Pricing",
    "title": "Pricing",
    "description": "Get all features of ShipAny, Ship your AI SaaS startups fast.",
    "groups": [],
    "items": [
      {
        "title": "Starter",
        "description": "Get started with your first SaaS startup.",
        "features_title": "Includes",
        "features": [
          "100 credits, valid for 1 month",
          "NextJS boilerplate",
          "SEO-friendly structure",
          "Payment with Stripe",
          "Data storage with Supabase",
          "Google Oauth & One-Tap Login",
    
...
```

Example 4 (unknown):
```unknown
{
  "pricing": {
    "name": "pricing",
    "label": "Pricing",
    "title": "Pricing",
    "description": "Get all features of ShipAny, Ship your AI SaaS startups fast.",
    "groups": [],
    "items": [
      {
        "title": "Starter",
        "description": "Get started with your first SaaS startup.",
        "features_title": "Includes",
        "features": [
          "100 credits, valid for 1 month",
          "NextJS boilerplate",
          "SEO-friendly structure",
          "Payment with Stripe",
          "Data storage with Supabase",
          "Google Oauth & One-Tap Login",
    
...
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/features/i18n#参考

**Contents:**
- 国际化
- 项目国际化
- 落地页国际化
- 支持更多语言
- 参考

ShipAny 使用 next-intl 默认支持国际化。只需要简单的配置，即可开启。

项目国际化，包括 ShipAny 项目启动后看到的页面 title，SEO 信息，登陆框文案等。

在 i18n/messages 目录下，通过 [locale].json 文件配置页面内容，默认支持中文和英文，在 i18n/messages/ 目录下，可以看到 en.json 和 zh.json 两个文件，在项目发布之前，修改成跟你项目相符合的文案即可。

落地页的内容，在 i18n/pages/landing 目录下，通过 [locale].json 文件进行配置。

默认支持 en.json 和 zh.json 两个文件，在项目发布之前，修改成跟你项目相符合的文案即可。

除了默认的 en 和 zh 外，如果你还需要支持更多的语言，比如日语：ja，韩语：ko，法语：fr等，你可以按照以下步骤进行多语言配置：

在 i18n/messages 目录和 i18n/pages/landing 目录下，添加对应的语言文件，比如 ja.json 和 ko.json， fr.json 等。

修改 i18n/locale.ts 文件，添加更多语言支持

**Examples:**

Example 1 (unknown):
```unknown
update content of this file, for my new project "Flux AI", which is an AI Image Generator, with keywords "flux ai, ai image generator"
```

Example 2 (unknown):
```unknown
update content of this file, for my new project "Flux AI", which is an AI Image Generator, with keywords "flux ai, ai image generator"
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

**URL:** https://docs.shipany.ai/zh/features/seo#接入-gsc

**Contents:**
- SEO
- 设置多语言文案
- 设置站点地图
- 网页 SEO 走查
- Metadata 配置
- 接入 GSC

ShipAny 做了很多 SEO 优化，可以让你的项目在搜索引擎中获得更好的排名。

在 i18n/messages 目录下，通过 [locale].json 文件配置页面内容，默认支持中文和英文，在 i18n/messages/ 目录下，可以看到 en.json 和 zh.json 两个文件，在项目发布之前，修改成跟你项目相符合的文案即可。

修改 public/sitemap.xml 文件，配置成你自己的站点信息

按需修改 public/robots.txt 内容

检查网站首页的 title / description / Canonical 是否合理

用 AI 辅助修改 i18n/pages/landing 下 json 文件对应的网页内容，调整网站主打的关键词密度。(3% 左右比较合理)

ShipAny 对默认的 landing page 做了内容结构优化。如果你有自定义页面组件，需要检查页面的结构是否合理。

在 AITDK 插件的 Issues 面板开启 SSR Check，检测网页是否是服务端渲染。

如果你有创建新的页面路由 (page.tsx)，可以配置一下新页面的 Metadata 信息。

为子页面设置独立的 title / description / canonical 信息，有利于 SEO。

网站上站后，在 Google Search Console 中添加你的站点，可以查看网站的搜索流量和排名情况。

**Examples:**

Example 1 (unknown):
```unknown
update content of this file, for my new project "Flux AI", which is an AI Image Generator, with keywords "flux ai, ai image generator"
```

Example 2 (unknown):
```unknown
update content of this file, for my new project "Flux AI", which is an AI Image Generator, with keywords "flux ai, ai image generator"
```

Example 3 (unknown):
```unknown
<?xml version='1.0' encoding='utf-8' standalone='yes'?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://shipany.ai/</loc>
    <lastmod>2024-12-24T10:00:00+00:00</lastmod>
  </url>
</urlset>
```

Example 4 (unknown):
```unknown
<?xml version='1.0' encoding='utf-8' standalone='yes'?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://shipany.ai/</loc>
    <lastmod>2024-12-24T10:00:00+00:00</lastmod>
  </url>
</urlset>
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/features/feedback#如何使用

**Contents:**
- 用户反馈
- 用户反馈组件
- 如何使用

ShipAny 提供用户反馈组件，用于收集用户反馈。

用户反馈组件位于页面右下角，点击后会弹窗收集用户反馈。

**Examples:**

Example 1 (unknown):
```unknown
CREATE TABLE feedbacks (
    id SERIAL PRIMARY KEY,
    created_at timestamptz,
    status VARCHAR(50),
    user_uuid VARCHAR(255),
    content TEXT,
    rating INT
);
```

Example 2 (unknown):
```unknown
CREATE TABLE feedbacks (
    id SERIAL PRIMARY KEY,
    created_at timestamptz,
    status VARCHAR(50),
    user_uuid VARCHAR(255),
    content TEXT,
    rating INT
);
```

Example 3 (python):
```python
import Footer from "@/components/blocks/footer";
import Header from "@/components/blocks/header";
import { ReactNode } from "react";
import { getLandingPage } from "@/services/page";
import Feedback from "@/components/feedback";
 
export default async function DefaultLayout({
  children,
  params,
}: {
  children: ReactNode;
  params: Promise<{ locale: string }>;
}) {
  const { locale } = await params;
  const page = await getLandingPage(locale);
 
  return (
    <>
      {page.header && <Header header={page.header} />}
      <main className="overflow-x-hidden">{children}</main>
      {page.fo
...
```

Example 4 (python):
```python
import Footer from "@/components/blocks/footer";
import Header from "@/components/blocks/header";
import { ReactNode } from "react";
import { getLandingPage } from "@/services/page";
import Feedback from "@/components/feedback";
 
export default async function DefaultLayout({
  children,
  params,
}: {
  children: ReactNode;
  params: Promise<{ locale: string }>;
}) {
  const { locale } = await params;
  const page = await getLandingPage(locale);
 
  return (
    <>
      {page.header && <Header header={page.header} />}
      <main className="overflow-x-hidden">{children}</main>
      {page.fo
...
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/features/database#配置数据库

**Contents:**
- 数据库
- 配置数据库
- 初始化数据库
- 更新数据库
- 管理数据库
- 操作数据库
- 使用其他类型数据库
- 参考

ShipAny 使用 drizzle-orm 支持多种类型数据库。

以 Supabase 数据库为例，在 ShipAny 配置数据库的流程为：

登录 Supabase 控制台，创建数据库

在 Supabase 控制台，进入你创建的数据库，点击上方的 Connect

在弹出来的框中复制数据库连接信息，类似这样的字符串：

[YOUR-PASSWORD] 需要替换成你在创建数据库时设置的密码。

修改项目配置文件：.env.development 和 .env.production

在配置好 DATABASE_URL 后，在项目根目录下运行以下命令，初始化数据库：

这个命令会执行 src/db/migrations 目录下的所有迁移文件，创建数据库表。

如果你通过 DATABASE_URL 配置的不是一个新创建的数据库，或者数据库之前已经存在 ShipAny 的库表信息，请不要执行以上命令。而是比较 src/db/migrations 目录下所有迁移文件的 sql 内容，手动执行 sql 语句，更新数据库表。

如果在项目创建之处，你使用的是一个新的数据库，且是通过 pnpm db:migrate 命令初始化的数据库，如果后续你拉取了最新的代码，可以继续执行以下命令，更新数据库表：

这个命令会根据 src/db/migrations 目录下所有迁移文件的 sql 内容，增量更新数据库表。

在项目根目录下执行命令：pnpm db:studio

这个命令会打开一个数据库管理界面，你可以在这里查看、编辑、删除数据库表。

在 src/models 目录下，写数据库操作文件，实现对数据表的增删改查。可参考以下操作 posts 表的示例：

数据表操作语法可参考 drizzle-orm 文档。

如果你使用自建的 Postgres 数据库，或者使用其他兼容 postgres 的云数据库，比如：Neon。配置和连接数据库的步骤跟使用 Supabase 一致，你只需要填写数据库的 DATABASE_URL 即可。

如果你需要使用 MySQL 或者 SQLite 等数据库，可参考以下步骤自定义：

修改 src/db/schema.ts 文件，使用新的数据库 Schema。

Schema 中数据表的字段定义，可以参考 drizzle-orm 文档。

修改 src/db/config.ts 文件，使用新的数据库连接配置。

默认是 Postgres 数据库连接配置，你可以参考 drizzle-orm 文档按需修改。

根据你使用的数据库类型，修改数据库连接实例。

如果你希望后续通过迁移文件更新数据库表。你可以在完成以上三步之后，在项目根目录下执行以下命令生成数据库迁移文件。

在 ShipAny 中配置不同类型的数据库非常简单，只需要完成以上四个步骤的自定义即可。src/model 下操作数据库的逻辑无需修改。

**Examples:**

Example 1 (unknown):
```unknown
postgresql://postgres.defqvdpquwyqqjlmurkg:[YOUR-PASSWORD]@aws-0-ap-southeast-1.pooler.supabase.com:6543/postgres
```

Example 2 (unknown):
```unknown
postgresql://postgres.defqvdpquwyqqjlmurkg:[YOUR-PASSWORD]@aws-0-ap-southeast-1.pooler.supabase.com:6543/postgres
```

Example 3 (unknown):
```unknown
DATABASE_URL="postgresql://postgres.defqvdpquwyqqjlmurkg:******@aws-0-ap-southeast-1.pooler.supabase.com:6543/postgres"
```

Example 4 (unknown):
```unknown
DATABASE_URL="postgresql://postgres.defqvdpquwyqqjlmurkg:******@aws-0-ap-southeast-1.pooler.supabase.com:6543/postgres"
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/features/payment/stripe

**Contents:**
- Stripe
- Stripe 设置
- ShipAny 配置
- 价格表支付
  - 配置价格表内容
  - 修改价格表组件
  - 修改价格表下单逻辑
  - 修改支付回调逻辑
  - 修改支付通知逻辑
- 自定义支付

ShipAny 支持使用 Stripe 进行支付，可用于产品付款、会员订阅、购买积分等场景。

在 ShipAny 项目配置文件中，填写 Stripe 相关的配置信息。

页面路径可以填相对路径，也可以填绝对路径。如果填的是相对路径，跳转时会自动拼接 NEXT_PUBLIC_WEB_URL 配置的网站地址，并带上多语言参数。

比如按照以上配置，在中文页面支付成功后的跳转路径是：http://localhost:3000/zh/my-orders

ShipAny 模板内置了一个价格表和对应的支付逻辑，你可以根据自己的需求，简单修改即可快速实现支付功能。

ShipAny 模板内置的价格表配置文件位于：src/i18n/pages/pricing 目录下，支持多语言，默认包含 en.json 和 zh.json 两个价格表配置文件。

你可以根据自己的需求，修改价格表配置文件中的内容。

默认的价格表组件位于：src/components/blocks/pricing/index.tsx

你可以根据自己的需求，修改价格表的展示形式。

默认的价格表下单逻辑位于：src/app/api/checkout/route.ts

你可以根据自己的需求，修改价格表的下单逻辑。

在价格表下单逻辑中，默认配置的支付回调地址是：/api/pay/callback/stripe

用户支付后，会在浏览器跳转到这个地址，并带上包含支付信息的参数。

默认的支付回调处理逻辑位于：src/app/api/pay/callback/stripe/route.ts

你可以根据自己的需求，修改处理支付回调的逻辑，比如更新订单状态、给用户发送邮件通知、给用户赠送积分等。

支付回调是同步逻辑，依赖浏览器跳转到回调地址，才能处理支付结果。这种方式不太可靠，可能出现跳转过程中用户关闭了浏览器等情况，导致支付结果没有被正常处理。 更可靠的方式是通过 Webhook，配置支付结果异步通知。

比如把 Webhook 地址配置为：https://your-domain.com/api/pay/notify/stripe

用户支付后，Stripe 会把支付信息推送到这个地址。

默认的支付通知逻辑位于：src/app/api/pay/notify/stripe/route.ts

你可以根据自己的需求，修改处理支付通知的逻辑，比如更新订单状态、给用户发送邮件通知、给用户赠送积分等。

修改价格表配置文件，添加 groups 数据，配置多个价格分组。并在 pricing.items 下为每一个价格方案，设置一个 group 名称。

配置完成后，点击价格分组，将根据 group 字段，切换显示不同的价格方案。

ShipAny 模板使用 Stripe 支付时，默认支持三种支付方案

你只需要修改价格表配置，把每个价格方案的 interval 字段，设置成上述三个值之一。

同时，按需修改价格(amount) / 积分(credits) / 有效期(valid_months) 等字段。

举例：按月订阅扣费，月付 $99，购买后得到 30 个积分，有效期 1 个月，则核心的价格表配置信息为：

修改 src/app/api/checkout/route.ts 文件，设置 Stripe 下单的 options 参数。

在 Stripe 后台 设置支付方式，开通支付宝和微信支付。

修改价格表配置文件，在每个价格方案下添加一个 cn_amount 字段，即可支持人民币支付。

比如，产品售价，$99，人民币支付价格为 699 元，核心配置信息为：

配置完成后，在价格表下单按钮上方，将会显示一个人民币支付图标。

在 Stripe 后台点击左上角的店铺打开下拉菜单，依次点击 Switch to sandbox -> Test mode，开启测试模式。

在测试模式下，进入开发者中心，设置 测试支付密钥，包括 Publishable key 和 Secret key。

注册 ngrok 账号，按指示安装 ngrok 命令行工具。

启动 ngrok 服务，监听本地端口，并生成一个临时的域名。

在 Stripe 后台测试模式中，配置 Webhook 地址为 ngrok 生成的域名，并监听以下两个事件：

Endpoint 填写支付通知地址，比如 https://xxx.ngrok-free.app/api/pay/notify/stripe。

添加 Webhook 地址后，在 Webhook 管理页面，复制 Signing secret，

跟支付密钥一起填入 .env.development 文件中。

在本地启动项目，访问 /pricing 页面，点击下单按钮，下单成功后跳转到支付页面。

使用 Stripe 测试卡 支付，支付成功后浏览器跳转到支付回调地址，监听的地址收到支付通知。

**Examples:**

Example 1 (unknown):
```unknown
NEXT_PUBLIC_WEB_URL = "http://localhost:3000"

NEXT_PUBLIC_PAY_SUCCESS_URL = "/my-orders"
NEXT_PUBLIC_PAY_FAIL_URL = "/pricing"
NEXT_PUBLIC_PAY_CANCEL_URL = "/pricing"

PAY_PROVIDER = "stripe"

STRIPE_PUBLIC_KEY = "pk_test_xxx"
STRIPE_PRIVATE_KEY = "sk_test_xxx"
STRIPE_WEBHOOK_SECRET = "whsec_cexxx"
```

Example 2 (unknown):
```unknown
NEXT_PUBLIC_WEB_URL = "http://localhost:3000"

NEXT_PUBLIC_PAY_SUCCESS_URL = "/my-orders"
NEXT_PUBLIC_PAY_FAIL_URL = "/pricing"
NEXT_PUBLIC_PAY_CANCEL_URL = "/pricing"

PAY_PROVIDER = "stripe"

STRIPE_PUBLIC_KEY = "pk_test_xxx"
STRIPE_PRIVATE_KEY = "sk_test_xxx"
STRIPE_WEBHOOK_SECRET = "whsec_cexxx"
```

Example 3 (unknown):
```unknown
{
  "pricing": {
    "name": "pricing",
    "label": "Pricing",
    "title": "Pricing",
    "description": "Get all features of ShipAny, Ship your AI SaaS startups fast.",
    "groups": [],
    "items": [
      {
        "title": "Starter",
        "description": "Get started with your first SaaS startup.",
        "features_title": "Includes",
        "features": [
          "100 credits, valid for 1 month",
          "NextJS boilerplate",
          "SEO-friendly structure",
          "Payment with Stripe",
          "Data storage with Supabase",
          "Google Oauth & One-Tap Login",
    
...
```

Example 4 (unknown):
```unknown
{
  "pricing": {
    "name": "pricing",
    "label": "Pricing",
    "title": "Pricing",
    "description": "Get all features of ShipAny, Ship your AI SaaS startups fast.",
    "groups": [],
    "items": [
      {
        "title": "Starter",
        "description": "Get started with your first SaaS startup.",
        "features_title": "Includes",
        "features": [
          "100 credits, valid for 1 month",
          "NextJS boilerplate",
          "SEO-friendly structure",
          "Payment with Stripe",
          "Data storage with Supabase",
          "Google Oauth & One-Tap Login",
    
...
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/features/payment/stripe#stripe-设置

**Contents:**
- Stripe
- Stripe 设置
- ShipAny 配置
- 价格表支付
  - 配置价格表内容
  - 修改价格表组件
  - 修改价格表下单逻辑
  - 修改支付回调逻辑
  - 修改支付通知逻辑
- 自定义支付

ShipAny 支持使用 Stripe 进行支付，可用于产品付款、会员订阅、购买积分等场景。

在 ShipAny 项目配置文件中，填写 Stripe 相关的配置信息。

页面路径可以填相对路径，也可以填绝对路径。如果填的是相对路径，跳转时会自动拼接 NEXT_PUBLIC_WEB_URL 配置的网站地址，并带上多语言参数。

比如按照以上配置，在中文页面支付成功后的跳转路径是：http://localhost:3000/zh/my-orders

ShipAny 模板内置了一个价格表和对应的支付逻辑，你可以根据自己的需求，简单修改即可快速实现支付功能。

ShipAny 模板内置的价格表配置文件位于：src/i18n/pages/pricing 目录下，支持多语言，默认包含 en.json 和 zh.json 两个价格表配置文件。

你可以根据自己的需求，修改价格表配置文件中的内容。

默认的价格表组件位于：src/components/blocks/pricing/index.tsx

你可以根据自己的需求，修改价格表的展示形式。

默认的价格表下单逻辑位于：src/app/api/checkout/route.ts

你可以根据自己的需求，修改价格表的下单逻辑。

在价格表下单逻辑中，默认配置的支付回调地址是：/api/pay/callback/stripe

用户支付后，会在浏览器跳转到这个地址，并带上包含支付信息的参数。

默认的支付回调处理逻辑位于：src/app/api/pay/callback/stripe/route.ts

你可以根据自己的需求，修改处理支付回调的逻辑，比如更新订单状态、给用户发送邮件通知、给用户赠送积分等。

支付回调是同步逻辑，依赖浏览器跳转到回调地址，才能处理支付结果。这种方式不太可靠，可能出现跳转过程中用户关闭了浏览器等情况，导致支付结果没有被正常处理。 更可靠的方式是通过 Webhook，配置支付结果异步通知。

比如把 Webhook 地址配置为：https://your-domain.com/api/pay/notify/stripe

用户支付后，Stripe 会把支付信息推送到这个地址。

默认的支付通知逻辑位于：src/app/api/pay/notify/stripe/route.ts

你可以根据自己的需求，修改处理支付通知的逻辑，比如更新订单状态、给用户发送邮件通知、给用户赠送积分等。

修改价格表配置文件，添加 groups 数据，配置多个价格分组。并在 pricing.items 下为每一个价格方案，设置一个 group 名称。

配置完成后，点击价格分组，将根据 group 字段，切换显示不同的价格方案。

ShipAny 模板使用 Stripe 支付时，默认支持三种支付方案

你只需要修改价格表配置，把每个价格方案的 interval 字段，设置成上述三个值之一。

同时，按需修改价格(amount) / 积分(credits) / 有效期(valid_months) 等字段。

举例：按月订阅扣费，月付 $99，购买后得到 30 个积分，有效期 1 个月，则核心的价格表配置信息为：

修改 src/app/api/checkout/route.ts 文件，设置 Stripe 下单的 options 参数。

在 Stripe 后台 设置支付方式，开通支付宝和微信支付。

修改价格表配置文件，在每个价格方案下添加一个 cn_amount 字段，即可支持人民币支付。

比如，产品售价，$99，人民币支付价格为 699 元，核心配置信息为：

配置完成后，在价格表下单按钮上方，将会显示一个人民币支付图标。

在 Stripe 后台点击左上角的店铺打开下拉菜单，依次点击 Switch to sandbox -> Test mode，开启测试模式。

在测试模式下，进入开发者中心，设置 测试支付密钥，包括 Publishable key 和 Secret key。

注册 ngrok 账号，按指示安装 ngrok 命令行工具。

启动 ngrok 服务，监听本地端口，并生成一个临时的域名。

在 Stripe 后台测试模式中，配置 Webhook 地址为 ngrok 生成的域名，并监听以下两个事件：

Endpoint 填写支付通知地址，比如 https://xxx.ngrok-free.app/api/pay/notify/stripe。

添加 Webhook 地址后，在 Webhook 管理页面，复制 Signing secret，

跟支付密钥一起填入 .env.development 文件中。

在本地启动项目，访问 /pricing 页面，点击下单按钮，下单成功后跳转到支付页面。

使用 Stripe 测试卡 支付，支付成功后浏览器跳转到支付回调地址，监听的地址收到支付通知。

**Examples:**

Example 1 (unknown):
```unknown
NEXT_PUBLIC_WEB_URL = "http://localhost:3000"

NEXT_PUBLIC_PAY_SUCCESS_URL = "/my-orders"
NEXT_PUBLIC_PAY_FAIL_URL = "/pricing"
NEXT_PUBLIC_PAY_CANCEL_URL = "/pricing"

PAY_PROVIDER = "stripe"

STRIPE_PUBLIC_KEY = "pk_test_xxx"
STRIPE_PRIVATE_KEY = "sk_test_xxx"
STRIPE_WEBHOOK_SECRET = "whsec_cexxx"
```

Example 2 (unknown):
```unknown
NEXT_PUBLIC_WEB_URL = "http://localhost:3000"

NEXT_PUBLIC_PAY_SUCCESS_URL = "/my-orders"
NEXT_PUBLIC_PAY_FAIL_URL = "/pricing"
NEXT_PUBLIC_PAY_CANCEL_URL = "/pricing"

PAY_PROVIDER = "stripe"

STRIPE_PUBLIC_KEY = "pk_test_xxx"
STRIPE_PRIVATE_KEY = "sk_test_xxx"
STRIPE_WEBHOOK_SECRET = "whsec_cexxx"
```

Example 3 (unknown):
```unknown
{
  "pricing": {
    "name": "pricing",
    "label": "Pricing",
    "title": "Pricing",
    "description": "Get all features of ShipAny, Ship your AI SaaS startups fast.",
    "groups": [],
    "items": [
      {
        "title": "Starter",
        "description": "Get started with your first SaaS startup.",
        "features_title": "Includes",
        "features": [
          "100 credits, valid for 1 month",
          "NextJS boilerplate",
          "SEO-friendly structure",
          "Payment with Stripe",
          "Data storage with Supabase",
          "Google Oauth & One-Tap Login",
    
...
```

Example 4 (unknown):
```unknown
{
  "pricing": {
    "name": "pricing",
    "label": "Pricing",
    "title": "Pricing",
    "description": "Get all features of ShipAny, Ship your AI SaaS startups fast.",
    "groups": [],
    "items": [
      {
        "title": "Starter",
        "description": "Get started with your first SaaS startup.",
        "features_title": "Includes",
        "features": [
          "100 credits, valid for 1 month",
          "NextJS boilerplate",
          "SEO-friendly structure",
          "Payment with Stripe",
          "Data storage with Supabase",
          "Google Oauth & One-Tap Login",
    
...
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/features/payment/stripe#修改价格表组件

**Contents:**
- Stripe
- Stripe 设置
- ShipAny 配置
- 价格表支付
  - 配置价格表内容
  - 修改价格表组件
  - 修改价格表下单逻辑
  - 修改支付回调逻辑
  - 修改支付通知逻辑
- 自定义支付

ShipAny 支持使用 Stripe 进行支付，可用于产品付款、会员订阅、购买积分等场景。

在 ShipAny 项目配置文件中，填写 Stripe 相关的配置信息。

页面路径可以填相对路径，也可以填绝对路径。如果填的是相对路径，跳转时会自动拼接 NEXT_PUBLIC_WEB_URL 配置的网站地址，并带上多语言参数。

比如按照以上配置，在中文页面支付成功后的跳转路径是：http://localhost:3000/zh/my-orders

ShipAny 模板内置了一个价格表和对应的支付逻辑，你可以根据自己的需求，简单修改即可快速实现支付功能。

ShipAny 模板内置的价格表配置文件位于：src/i18n/pages/pricing 目录下，支持多语言，默认包含 en.json 和 zh.json 两个价格表配置文件。

你可以根据自己的需求，修改价格表配置文件中的内容。

默认的价格表组件位于：src/components/blocks/pricing/index.tsx

你可以根据自己的需求，修改价格表的展示形式。

默认的价格表下单逻辑位于：src/app/api/checkout/route.ts

你可以根据自己的需求，修改价格表的下单逻辑。

在价格表下单逻辑中，默认配置的支付回调地址是：/api/pay/callback/stripe

用户支付后，会在浏览器跳转到这个地址，并带上包含支付信息的参数。

默认的支付回调处理逻辑位于：src/app/api/pay/callback/stripe/route.ts

你可以根据自己的需求，修改处理支付回调的逻辑，比如更新订单状态、给用户发送邮件通知、给用户赠送积分等。

支付回调是同步逻辑，依赖浏览器跳转到回调地址，才能处理支付结果。这种方式不太可靠，可能出现跳转过程中用户关闭了浏览器等情况，导致支付结果没有被正常处理。 更可靠的方式是通过 Webhook，配置支付结果异步通知。

比如把 Webhook 地址配置为：https://your-domain.com/api/pay/notify/stripe

用户支付后，Stripe 会把支付信息推送到这个地址。

默认的支付通知逻辑位于：src/app/api/pay/notify/stripe/route.ts

你可以根据自己的需求，修改处理支付通知的逻辑，比如更新订单状态、给用户发送邮件通知、给用户赠送积分等。

修改价格表配置文件，添加 groups 数据，配置多个价格分组。并在 pricing.items 下为每一个价格方案，设置一个 group 名称。

配置完成后，点击价格分组，将根据 group 字段，切换显示不同的价格方案。

ShipAny 模板使用 Stripe 支付时，默认支持三种支付方案

你只需要修改价格表配置，把每个价格方案的 interval 字段，设置成上述三个值之一。

同时，按需修改价格(amount) / 积分(credits) / 有效期(valid_months) 等字段。

举例：按月订阅扣费，月付 $99，购买后得到 30 个积分，有效期 1 个月，则核心的价格表配置信息为：

修改 src/app/api/checkout/route.ts 文件，设置 Stripe 下单的 options 参数。

在 Stripe 后台 设置支付方式，开通支付宝和微信支付。

修改价格表配置文件，在每个价格方案下添加一个 cn_amount 字段，即可支持人民币支付。

比如，产品售价，$99，人民币支付价格为 699 元，核心配置信息为：

配置完成后，在价格表下单按钮上方，将会显示一个人民币支付图标。

在 Stripe 后台点击左上角的店铺打开下拉菜单，依次点击 Switch to sandbox -> Test mode，开启测试模式。

在测试模式下，进入开发者中心，设置 测试支付密钥，包括 Publishable key 和 Secret key。

注册 ngrok 账号，按指示安装 ngrok 命令行工具。

启动 ngrok 服务，监听本地端口，并生成一个临时的域名。

在 Stripe 后台测试模式中，配置 Webhook 地址为 ngrok 生成的域名，并监听以下两个事件：

Endpoint 填写支付通知地址，比如 https://xxx.ngrok-free.app/api/pay/notify/stripe。

添加 Webhook 地址后，在 Webhook 管理页面，复制 Signing secret，

跟支付密钥一起填入 .env.development 文件中。

在本地启动项目，访问 /pricing 页面，点击下单按钮，下单成功后跳转到支付页面。

使用 Stripe 测试卡 支付，支付成功后浏览器跳转到支付回调地址，监听的地址收到支付通知。

**Examples:**

Example 1 (unknown):
```unknown
NEXT_PUBLIC_WEB_URL = "http://localhost:3000"

NEXT_PUBLIC_PAY_SUCCESS_URL = "/my-orders"
NEXT_PUBLIC_PAY_FAIL_URL = "/pricing"
NEXT_PUBLIC_PAY_CANCEL_URL = "/pricing"

PAY_PROVIDER = "stripe"

STRIPE_PUBLIC_KEY = "pk_test_xxx"
STRIPE_PRIVATE_KEY = "sk_test_xxx"
STRIPE_WEBHOOK_SECRET = "whsec_cexxx"
```

Example 2 (unknown):
```unknown
NEXT_PUBLIC_WEB_URL = "http://localhost:3000"

NEXT_PUBLIC_PAY_SUCCESS_URL = "/my-orders"
NEXT_PUBLIC_PAY_FAIL_URL = "/pricing"
NEXT_PUBLIC_PAY_CANCEL_URL = "/pricing"

PAY_PROVIDER = "stripe"

STRIPE_PUBLIC_KEY = "pk_test_xxx"
STRIPE_PRIVATE_KEY = "sk_test_xxx"
STRIPE_WEBHOOK_SECRET = "whsec_cexxx"
```

Example 3 (unknown):
```unknown
{
  "pricing": {
    "name": "pricing",
    "label": "Pricing",
    "title": "Pricing",
    "description": "Get all features of ShipAny, Ship your AI SaaS startups fast.",
    "groups": [],
    "items": [
      {
        "title": "Starter",
        "description": "Get started with your first SaaS startup.",
        "features_title": "Includes",
        "features": [
          "100 credits, valid for 1 month",
          "NextJS boilerplate",
          "SEO-friendly structure",
          "Payment with Stripe",
          "Data storage with Supabase",
          "Google Oauth & One-Tap Login",
    
...
```

Example 4 (unknown):
```unknown
{
  "pricing": {
    "name": "pricing",
    "label": "Pricing",
    "title": "Pricing",
    "description": "Get all features of ShipAny, Ship your AI SaaS startups fast.",
    "groups": [],
    "items": [
      {
        "title": "Starter",
        "description": "Get started with your first SaaS startup.",
        "features_title": "Includes",
        "features": [
          "100 credits, valid for 1 month",
          "NextJS boilerplate",
          "SEO-friendly structure",
          "Payment with Stripe",
          "Data storage with Supabase",
          "Google Oauth & One-Tap Login",
    
...
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/features/storage#下载远程图片上传到云存储

**Contents:**
- 文件存储
- 配置云存储
- 上传 AI 图片到云存储
- 读取本地文件上传到云存储
- 下载远程图片上传到云存储
- 参考

ShipAny 支持上传文件到 AWS S3 兼容的文件存储系统，例如 AWS S3 / Cloudflare R2 / 腾讯云 COS 等。

选择你的云存储平台，创建存储桶，设置访问密钥和访问域名。

把 aisdk 生成的图片（返回的 base64 数据），上传到云存储。

uploadFile 接收的 body 参数是 Buffer 类型。你可以传递从 URL 下载的文件 Buffer 或者从本地文件读取的 Buffer。

注意：path 和 readFile 在 edge runtime 中无法使用，所以在 cloudflare 部署时，不能读取本地文件。

给定一个远程的图片地址，下载图片并上传到云存储。

**Examples:**

Example 1 (unknown):
```unknown
STORAGE_ENDPOINT = ""
STORAGE_REGION = ""
STORAGE_ACCESS_KEY = ""
STORAGE_SECRET_KEY = ""
STORAGE_BUCKET = ""
STORAGE_DOMAIN = ""
```

Example 2 (unknown):
```unknown
STORAGE_ENDPOINT = ""
STORAGE_REGION = ""
STORAGE_ACCESS_KEY = ""
STORAGE_SECRET_KEY = ""
STORAGE_BUCKET = ""
STORAGE_DOMAIN = ""
```

Example 3 (python):
```python
import { newStorage } from "@/lib/storage";
 
const storage = new Storage();
 
const filename = `image_${new Date().getTime()}.png`;
const key = `shipany/${filename}`;
const body = Buffer.from(image.base64, "base64");
 
try {
  const res = await storage.uploadFile({
    body,
    key,
    contentType: "image/png",
    disposition: "inline",
  });
 
  console.log("upload file success:", res);
} catch (err) {
  console.log("upload file failed:", err);
}
```

Example 4 (python):
```python
import { newStorage } from "@/lib/storage";
 
const storage = new Storage();
 
const filename = `image_${new Date().getTime()}.png`;
const key = `shipany/${filename}`;
const body = Buffer.from(image.base64, "base64");
 
try {
  const res = await storage.uploadFile({
    body,
    key,
    contentType: "image/png",
    disposition: "inline",
  });
 
  console.log("upload file success:", res);
} catch (err) {
  console.log("upload file failed:", err);
}
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/features/storage#上传-ai-图片到云存储

**Contents:**
- 文件存储
- 配置云存储
- 上传 AI 图片到云存储
- 读取本地文件上传到云存储
- 下载远程图片上传到云存储
- 参考

ShipAny 支持上传文件到 AWS S3 兼容的文件存储系统，例如 AWS S3 / Cloudflare R2 / 腾讯云 COS 等。

选择你的云存储平台，创建存储桶，设置访问密钥和访问域名。

把 aisdk 生成的图片（返回的 base64 数据），上传到云存储。

uploadFile 接收的 body 参数是 Buffer 类型。你可以传递从 URL 下载的文件 Buffer 或者从本地文件读取的 Buffer。

注意：path 和 readFile 在 edge runtime 中无法使用，所以在 cloudflare 部署时，不能读取本地文件。

给定一个远程的图片地址，下载图片并上传到云存储。

**Examples:**

Example 1 (unknown):
```unknown
STORAGE_ENDPOINT = ""
STORAGE_REGION = ""
STORAGE_ACCESS_KEY = ""
STORAGE_SECRET_KEY = ""
STORAGE_BUCKET = ""
STORAGE_DOMAIN = ""
```

Example 2 (unknown):
```unknown
STORAGE_ENDPOINT = ""
STORAGE_REGION = ""
STORAGE_ACCESS_KEY = ""
STORAGE_SECRET_KEY = ""
STORAGE_BUCKET = ""
STORAGE_DOMAIN = ""
```

Example 3 (python):
```python
import { newStorage } from "@/lib/storage";
 
const storage = new Storage();
 
const filename = `image_${new Date().getTime()}.png`;
const key = `shipany/${filename}`;
const body = Buffer.from(image.base64, "base64");
 
try {
  const res = await storage.uploadFile({
    body,
    key,
    contentType: "image/png",
    disposition: "inline",
  });
 
  console.log("upload file success:", res);
} catch (err) {
  console.log("upload file failed:", err);
}
```

Example 4 (python):
```python
import { newStorage } from "@/lib/storage";
 
const storage = new Storage();
 
const filename = `image_${new Date().getTime()}.png`;
const key = `shipany/${filename}`;
const body = Buffer.from(image.base64, "base64");
 
try {
  const res = await storage.uploadFile({
    body,
    key,
    contentType: "image/png",
    disposition: "inline",
  });
 
  console.log("upload file success:", res);
} catch (err) {
  console.log("upload file failed:", err);
}
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/features/storage#读取本地文件上传到云存储

**Contents:**
- 文件存储
- 配置云存储
- 上传 AI 图片到云存储
- 读取本地文件上传到云存储
- 下载远程图片上传到云存储
- 参考

ShipAny 支持上传文件到 AWS S3 兼容的文件存储系统，例如 AWS S3 / Cloudflare R2 / 腾讯云 COS 等。

选择你的云存储平台，创建存储桶，设置访问密钥和访问域名。

把 aisdk 生成的图片（返回的 base64 数据），上传到云存储。

uploadFile 接收的 body 参数是 Buffer 类型。你可以传递从 URL 下载的文件 Buffer 或者从本地文件读取的 Buffer。

注意：path 和 readFile 在 edge runtime 中无法使用，所以在 cloudflare 部署时，不能读取本地文件。

给定一个远程的图片地址，下载图片并上传到云存储。

**Examples:**

Example 1 (unknown):
```unknown
STORAGE_ENDPOINT = ""
STORAGE_REGION = ""
STORAGE_ACCESS_KEY = ""
STORAGE_SECRET_KEY = ""
STORAGE_BUCKET = ""
STORAGE_DOMAIN = ""
```

Example 2 (unknown):
```unknown
STORAGE_ENDPOINT = ""
STORAGE_REGION = ""
STORAGE_ACCESS_KEY = ""
STORAGE_SECRET_KEY = ""
STORAGE_BUCKET = ""
STORAGE_DOMAIN = ""
```

Example 3 (python):
```python
import { newStorage } from "@/lib/storage";
 
const storage = new Storage();
 
const filename = `image_${new Date().getTime()}.png`;
const key = `shipany/${filename}`;
const body = Buffer.from(image.base64, "base64");
 
try {
  const res = await storage.uploadFile({
    body,
    key,
    contentType: "image/png",
    disposition: "inline",
  });
 
  console.log("upload file success:", res);
} catch (err) {
  console.log("upload file failed:", err);
}
```

Example 4 (python):
```python
import { newStorage } from "@/lib/storage";
 
const storage = new Storage();
 
const filename = `image_${new Date().getTime()}.png`;
const key = `shipany/${filename}`;
const body = Buffer.from(image.base64, "base64");
 
try {
  const res = await storage.uploadFile({
    body,
    key,
    contentType: "image/png",
    disposition: "inline",
  });
 
  console.log("upload file success:", res);
} catch (err) {
  console.log("upload file failed:", err);
}
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/features/email/resend#发送-html-邮件

**Contents:**
- Resend
- Resend 设置
- ShipAny 配置
- 发送邮件
  - 发送文本邮件
  - 发送 HTML 邮件
  - 发送模板邮件
  - 使用 React Email
- 参考

ShipAny 支持使用 Resend 发送邮件，可用于发送邮件验证码、发送支付通知、发送营销邮件等场景。

在 Resend 后台 添加域名，设置 DNS 记录，验证域名

在 Resend 后台 创建 API 密钥，并复制 API 密钥

在 ShipAny 项目配置文件中，填写 Resend 相关的配置信息。

比如在 Resend 后台配置的邮件域名是 mail.shipany.ai，则发件人邮箱可以配置为 [email protected] / [email protected] / [email protected] 等。

在需要发邮件的地方，根据具体场景，选择合适的发送方式。

React Email 内置大量邮件组件，可以让你更轻松创建邮件模板。

比如在 @/components/email-templates/react-email.tsx 中写入内容：

除了自己实现邮件模板，你也可以在 React Email 模板市场 选择一个模板，修改后直接使用。

**Examples:**

Example 1 (unknown):
```unknown
RESEND_API_KEY = "re_xxx"
RESEND_SENDER_EMAIL = "[email protected]"
```

Example 2 (unknown):
```unknown
RESEND_API_KEY = "re_xxx"
RESEND_SENDER_EMAIL = "[email protected]"
```

Example 3 (python):
```python
import { Resend } from "resend";
 
const resend = new Resend(process.env.RESEND_API_KEY!);
 
const result = await resend.emails.send({
  from: process.env.RESEND_SENDER_EMAIL!,
  to: ["[email protected]"],
  subject: "Hello from ShipAny with Resend",
  text: "Hello World.",
});
 
console.log("send email result", result);
```

Example 4 (python):
```python
import { Resend } from "resend";
 
const resend = new Resend(process.env.RESEND_API_KEY!);
 
const result = await resend.emails.send({
  from: process.env.RESEND_SENDER_EMAIL!,
  to: ["[email protected]"],
  subject: "Hello from ShipAny with Resend",
  text: "Hello World.",
});
 
console.log("send email result", result);
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/features/analytics#openpanel-统计

**Contents:**
- 数据统计
- 谷歌数据统计
- OpenPanel 统计
- 参考

目前数据统计仅支持 Google Analytics 和 OpenPanel。后续会逐步支持 Plausible 和 Umami 等统计工具。

注册 OpenPanel 账号，参考官网文档，创建统计实例

在实例的管理后台，创建一个统计客户端，得到 Client ID

**Examples:**

Example 1 (unknown):
```unknown
NEXT_PUBLIC_GOOGLE_ANALYTICS_ID = "G-1TPQYZXS53"
```

Example 2 (unknown):
```unknown
NEXT_PUBLIC_GOOGLE_ANALYTICS_ID = "G-1TPQYZXS53"
```

Example 3 (unknown):
```unknown
NEXT_PUBLIC_OPENPANEL_CLIENT_ID = "xxx-xxx-xxx-xxx"
```

Example 4 (unknown):
```unknown
NEXT_PUBLIC_OPENPANEL_CLIENT_ID = "xxx-xxx-xxx-xxx"
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/features/payment/stripe#参考

**Contents:**
- Stripe
- Stripe 设置
- ShipAny 配置
- 价格表支付
  - 配置价格表内容
  - 修改价格表组件
  - 修改价格表下单逻辑
  - 修改支付回调逻辑
  - 修改支付通知逻辑
- 自定义支付

ShipAny 支持使用 Stripe 进行支付，可用于产品付款、会员订阅、购买积分等场景。

在 ShipAny 项目配置文件中，填写 Stripe 相关的配置信息。

页面路径可以填相对路径，也可以填绝对路径。如果填的是相对路径，跳转时会自动拼接 NEXT_PUBLIC_WEB_URL 配置的网站地址，并带上多语言参数。

比如按照以上配置，在中文页面支付成功后的跳转路径是：http://localhost:3000/zh/my-orders

ShipAny 模板内置了一个价格表和对应的支付逻辑，你可以根据自己的需求，简单修改即可快速实现支付功能。

ShipAny 模板内置的价格表配置文件位于：src/i18n/pages/pricing 目录下，支持多语言，默认包含 en.json 和 zh.json 两个价格表配置文件。

你可以根据自己的需求，修改价格表配置文件中的内容。

默认的价格表组件位于：src/components/blocks/pricing/index.tsx

你可以根据自己的需求，修改价格表的展示形式。

默认的价格表下单逻辑位于：src/app/api/checkout/route.ts

你可以根据自己的需求，修改价格表的下单逻辑。

在价格表下单逻辑中，默认配置的支付回调地址是：/api/pay/callback/stripe

用户支付后，会在浏览器跳转到这个地址，并带上包含支付信息的参数。

默认的支付回调处理逻辑位于：src/app/api/pay/callback/stripe/route.ts

你可以根据自己的需求，修改处理支付回调的逻辑，比如更新订单状态、给用户发送邮件通知、给用户赠送积分等。

支付回调是同步逻辑，依赖浏览器跳转到回调地址，才能处理支付结果。这种方式不太可靠，可能出现跳转过程中用户关闭了浏览器等情况，导致支付结果没有被正常处理。 更可靠的方式是通过 Webhook，配置支付结果异步通知。

比如把 Webhook 地址配置为：https://your-domain.com/api/pay/notify/stripe

用户支付后，Stripe 会把支付信息推送到这个地址。

默认的支付通知逻辑位于：src/app/api/pay/notify/stripe/route.ts

你可以根据自己的需求，修改处理支付通知的逻辑，比如更新订单状态、给用户发送邮件通知、给用户赠送积分等。

修改价格表配置文件，添加 groups 数据，配置多个价格分组。并在 pricing.items 下为每一个价格方案，设置一个 group 名称。

配置完成后，点击价格分组，将根据 group 字段，切换显示不同的价格方案。

ShipAny 模板使用 Stripe 支付时，默认支持三种支付方案

你只需要修改价格表配置，把每个价格方案的 interval 字段，设置成上述三个值之一。

同时，按需修改价格(amount) / 积分(credits) / 有效期(valid_months) 等字段。

举例：按月订阅扣费，月付 $99，购买后得到 30 个积分，有效期 1 个月，则核心的价格表配置信息为：

修改 src/app/api/checkout/route.ts 文件，设置 Stripe 下单的 options 参数。

在 Stripe 后台 设置支付方式，开通支付宝和微信支付。

修改价格表配置文件，在每个价格方案下添加一个 cn_amount 字段，即可支持人民币支付。

比如，产品售价，$99，人民币支付价格为 699 元，核心配置信息为：

配置完成后，在价格表下单按钮上方，将会显示一个人民币支付图标。

在 Stripe 后台点击左上角的店铺打开下拉菜单，依次点击 Switch to sandbox -> Test mode，开启测试模式。

在测试模式下，进入开发者中心，设置 测试支付密钥，包括 Publishable key 和 Secret key。

注册 ngrok 账号，按指示安装 ngrok 命令行工具。

启动 ngrok 服务，监听本地端口，并生成一个临时的域名。

在 Stripe 后台测试模式中，配置 Webhook 地址为 ngrok 生成的域名，并监听以下两个事件：

Endpoint 填写支付通知地址，比如 https://xxx.ngrok-free.app/api/pay/notify/stripe。

添加 Webhook 地址后，在 Webhook 管理页面，复制 Signing secret，

跟支付密钥一起填入 .env.development 文件中。

在本地启动项目，访问 /pricing 页面，点击下单按钮，下单成功后跳转到支付页面。

使用 Stripe 测试卡 支付，支付成功后浏览器跳转到支付回调地址，监听的地址收到支付通知。

**Examples:**

Example 1 (unknown):
```unknown
NEXT_PUBLIC_WEB_URL = "http://localhost:3000"

NEXT_PUBLIC_PAY_SUCCESS_URL = "/my-orders"
NEXT_PUBLIC_PAY_FAIL_URL = "/pricing"
NEXT_PUBLIC_PAY_CANCEL_URL = "/pricing"

PAY_PROVIDER = "stripe"

STRIPE_PUBLIC_KEY = "pk_test_xxx"
STRIPE_PRIVATE_KEY = "sk_test_xxx"
STRIPE_WEBHOOK_SECRET = "whsec_cexxx"
```

Example 2 (unknown):
```unknown
NEXT_PUBLIC_WEB_URL = "http://localhost:3000"

NEXT_PUBLIC_PAY_SUCCESS_URL = "/my-orders"
NEXT_PUBLIC_PAY_FAIL_URL = "/pricing"
NEXT_PUBLIC_PAY_CANCEL_URL = "/pricing"

PAY_PROVIDER = "stripe"

STRIPE_PUBLIC_KEY = "pk_test_xxx"
STRIPE_PRIVATE_KEY = "sk_test_xxx"
STRIPE_WEBHOOK_SECRET = "whsec_cexxx"
```

Example 3 (unknown):
```unknown
{
  "pricing": {
    "name": "pricing",
    "label": "Pricing",
    "title": "Pricing",
    "description": "Get all features of ShipAny, Ship your AI SaaS startups fast.",
    "groups": [],
    "items": [
      {
        "title": "Starter",
        "description": "Get started with your first SaaS startup.",
        "features_title": "Includes",
        "features": [
          "100 credits, valid for 1 month",
          "NextJS boilerplate",
          "SEO-friendly structure",
          "Payment with Stripe",
          "Data storage with Supabase",
          "Google Oauth & One-Tap Login",
    
...
```

Example 4 (unknown):
```unknown
{
  "pricing": {
    "name": "pricing",
    "label": "Pricing",
    "title": "Pricing",
    "description": "Get all features of ShipAny, Ship your AI SaaS startups fast.",
    "groups": [],
    "items": [
      {
        "title": "Starter",
        "description": "Get started with your first SaaS startup.",
        "features_title": "Includes",
        "features": [
          "100 credits, valid for 1 month",
          "NextJS boilerplate",
          "SEO-friendly structure",
          "Payment with Stripe",
          "Data storage with Supabase",
          "Google Oauth & One-Tap Login",
    
...
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/features/i18n

**Contents:**
- 国际化
- 项目国际化
- 落地页国际化
- 支持更多语言
- 参考

ShipAny 使用 next-intl 默认支持国际化。只需要简单的配置，即可开启。

项目国际化，包括 ShipAny 项目启动后看到的页面 title，SEO 信息，登陆框文案等。

在 i18n/messages 目录下，通过 [locale].json 文件配置页面内容，默认支持中文和英文，在 i18n/messages/ 目录下，可以看到 en.json 和 zh.json 两个文件，在项目发布之前，修改成跟你项目相符合的文案即可。

落地页的内容，在 i18n/pages/landing 目录下，通过 [locale].json 文件进行配置。

默认支持 en.json 和 zh.json 两个文件，在项目发布之前，修改成跟你项目相符合的文案即可。

除了默认的 en 和 zh 外，如果你还需要支持更多的语言，比如日语：ja，韩语：ko，法语：fr等，你可以按照以下步骤进行多语言配置：

在 i18n/messages 目录和 i18n/pages/landing 目录下，添加对应的语言文件，比如 ja.json 和 ko.json， fr.json 等。

修改 i18n/locale.ts 文件，添加更多语言支持

**Examples:**

Example 1 (unknown):
```unknown
update content of this file, for my new project "Flux AI", which is an AI Image Generator, with keywords "flux ai, ai image generator"
```

Example 2 (unknown):
```unknown
update content of this file, for my new project "Flux AI", which is an AI Image Generator, with keywords "flux ai, ai image generator"
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

**URL:** https://docs.shipany.ai/zh/features/database

**Contents:**
- 数据库
- 配置数据库
- 初始化数据库
- 更新数据库
- 管理数据库
- 操作数据库
- 使用其他类型数据库
- 参考

ShipAny 使用 drizzle-orm 支持多种类型数据库。

以 Supabase 数据库为例，在 ShipAny 配置数据库的流程为：

登录 Supabase 控制台，创建数据库

在 Supabase 控制台，进入你创建的数据库，点击上方的 Connect

在弹出来的框中复制数据库连接信息，类似这样的字符串：

[YOUR-PASSWORD] 需要替换成你在创建数据库时设置的密码。

修改项目配置文件：.env.development 和 .env.production

在配置好 DATABASE_URL 后，在项目根目录下运行以下命令，初始化数据库：

这个命令会执行 src/db/migrations 目录下的所有迁移文件，创建数据库表。

如果你通过 DATABASE_URL 配置的不是一个新创建的数据库，或者数据库之前已经存在 ShipAny 的库表信息，请不要执行以上命令。而是比较 src/db/migrations 目录下所有迁移文件的 sql 内容，手动执行 sql 语句，更新数据库表。

如果在项目创建之处，你使用的是一个新的数据库，且是通过 pnpm db:migrate 命令初始化的数据库，如果后续你拉取了最新的代码，可以继续执行以下命令，更新数据库表：

这个命令会根据 src/db/migrations 目录下所有迁移文件的 sql 内容，增量更新数据库表。

在项目根目录下执行命令：pnpm db:studio

这个命令会打开一个数据库管理界面，你可以在这里查看、编辑、删除数据库表。

在 src/models 目录下，写数据库操作文件，实现对数据表的增删改查。可参考以下操作 posts 表的示例：

数据表操作语法可参考 drizzle-orm 文档。

如果你使用自建的 Postgres 数据库，或者使用其他兼容 postgres 的云数据库，比如：Neon。配置和连接数据库的步骤跟使用 Supabase 一致，你只需要填写数据库的 DATABASE_URL 即可。

如果你需要使用 MySQL 或者 SQLite 等数据库，可参考以下步骤自定义：

修改 src/db/schema.ts 文件，使用新的数据库 Schema。

Schema 中数据表的字段定义，可以参考 drizzle-orm 文档。

修改 src/db/config.ts 文件，使用新的数据库连接配置。

默认是 Postgres 数据库连接配置，你可以参考 drizzle-orm 文档按需修改。

根据你使用的数据库类型，修改数据库连接实例。

如果你希望后续通过迁移文件更新数据库表。你可以在完成以上三步之后，在项目根目录下执行以下命令生成数据库迁移文件。

在 ShipAny 中配置不同类型的数据库非常简单，只需要完成以上四个步骤的自定义即可。src/model 下操作数据库的逻辑无需修改。

**Examples:**

Example 1 (unknown):
```unknown
postgresql://postgres.defqvdpquwyqqjlmurkg:[YOUR-PASSWORD]@aws-0-ap-southeast-1.pooler.supabase.com:6543/postgres
```

Example 2 (unknown):
```unknown
postgresql://postgres.defqvdpquwyqqjlmurkg:[YOUR-PASSWORD]@aws-0-ap-southeast-1.pooler.supabase.com:6543/postgres
```

Example 3 (unknown):
```unknown
DATABASE_URL="postgresql://postgres.defqvdpquwyqqjlmurkg:******@aws-0-ap-southeast-1.pooler.supabase.com:6543/postgres"
```

Example 4 (unknown):
```unknown
DATABASE_URL="postgresql://postgres.defqvdpquwyqqjlmurkg:******@aws-0-ap-southeast-1.pooler.supabase.com:6543/postgres"
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/features/payment/creem#shipany-配置

**Contents:**
- Creem
- Creem 设置
- ShipAny 配置
- 价格表支付
  - 配置价格表内容
  - 修改价格表组件
  - 修改价格表下单逻辑
  - 修改支付回调逻辑
  - 修改支付通知逻辑
- 本地测试

ShipAny 支持使用 Creem 进行支付，可用于产品付款、会员订阅、购买积分等场景。

在 ShipAny 项目配置文件中，填写 Creem 相关的配置信息。

页面路径可以填相对路径，也可以填绝对路径。如果填的是相对路径，跳转时会自动拼接 NEXT_PUBLIC_WEB_URL 配置的网站地址，并带上多语言参数。

比如按照以上配置，在中文页面支付成功后的跳转路径是：http://localhost:3000/zh/my-orders

比如在 ShipAny 项目中设置的价格表有三个支付方案，对应的 product_id 分别是 starter、standard、premium，你需要在 Creem 后台为这三个方案 创建对应的产品，复制每个产品的 Product ID，与价格表中的 product_id 对应关系填写到 CREEM_PRODUCTS 中。

ShipAny 模板内置了一个价格表和对应的支付逻辑，你可以根据自己的需求，简单修改即可快速实现支付功能。

ShipAny 模板内置的价格表配置文件位于：src/i18n/pages/pricing 目录下，支持多语言，默认包含 en.json 和 zh.json 两个价格表配置文件。

你可以根据自己的需求，修改价格表配置文件中的内容。

默认的价格表组件位于：src/components/blocks/pricing/index.tsx

你可以根据自己的需求，修改价格表的展示形式。

默认的价格表下单逻辑位于：src/app/api/checkout/route.ts

你可以根据自己的需求，修改价格表的下单逻辑。

在价格表下单逻辑中，默认配置的支付回调地址是：/api/pay/callback/creem

用户支付后，会在浏览器跳转到这个地址，并带上包含支付信息的参数。

默认的支付回调处理逻辑位于：src/app/api/pay/callback/creem/route.ts

你可以根据自己的需求，修改处理支付回调的逻辑，比如更新订单状态、给用户发送邮件通知、给用户赠送积分等。

支付回调是同步逻辑，依赖浏览器跳转到回调地址，才能处理支付结果。这种方式不太可靠，可能出现跳转过程中用户关闭了浏览器等情况，导致支付结果没有被正常处理。 更可靠的方式是通过 Webhook，配置支付结果异步通知。

比如把 Webhook 地址配置为：https://your-domain.com/api/pay/notify/creem

用户支付后，Creem 会把支付信息推送到这个地址。

默认的支付通知逻辑位于：src/app/api/pay/notify/creem/route.ts

你可以根据自己的需求，修改处理支付通知的逻辑，比如更新订单状态、给用户发送邮件通知、给用户赠送积分等。

在 Creem 后台进入店铺，点击右上角的 Test mode，开启测试模式。

在测试模式下，进入开发者中心，设置 测试 API 密钥。

注册 ngrok 账号，按指示安装 ngrok 命令行工具。

启动 ngrok 服务，监听本地端口，并生成一个临时的域名。

在 Creem 后台测试模式中，配置 Webhook 地址为 ngrok 生成的域名

Endpoint 填写支付通知地址，比如 https://xxx.ngrok-free.app/api/pay/notify/creem。

添加 Webhook 地址后，在 Webhook 管理页面，复制 Signing secret，

跟支付密钥一起填入 .env.development 文件中。

在本地启动项目，访问 /pricing 页面，点击下单按钮，下单成功后跳转到支付页面。

使用 Stripe 测试卡 支付，支付成功后浏览器跳转到支付回调地址，监听的地址收到支付通知。

**Examples:**

Example 1 (unknown):
```unknown
NEXT_PUBLIC_WEB_URL = "http://localhost:3000"

NEXT_PUBLIC_PAY_SUCCESS_URL = "/my-orders"
NEXT_PUBLIC_PAY_FAIL_URL = "/pricing"
NEXT_PUBLIC_PAY_CANCEL_URL = "/pricing"

PAY_PROVIDER = "creem"

CREEM_ENV = "test"
CREEM_API_KEY = "creem_test_xxx"
CREEM_WEBHOOK_SECRET = "whsec_xxx"
CREEM_PRODUCTS = '{"starter": "prod_xxx", "standard": "prod_xxx", "premium": "prod_xxx"}'
```

Example 2 (unknown):
```unknown
NEXT_PUBLIC_WEB_URL = "http://localhost:3000"

NEXT_PUBLIC_PAY_SUCCESS_URL = "/my-orders"
NEXT_PUBLIC_PAY_FAIL_URL = "/pricing"
NEXT_PUBLIC_PAY_CANCEL_URL = "/pricing"

PAY_PROVIDER = "creem"

CREEM_ENV = "test"
CREEM_API_KEY = "creem_test_xxx"
CREEM_WEBHOOK_SECRET = "whsec_xxx"
CREEM_PRODUCTS = '{"starter": "prod_xxx", "standard": "prod_xxx", "premium": "prod_xxx"}'
```

Example 3 (unknown):
```unknown
{
  "pricing": {
    "name": "pricing",
    "label": "Pricing",
    "title": "Pricing",
    "description": "Get all features of ShipAny, Ship your AI SaaS startups fast.",
    "groups": [],
    "items": [
      {
        "title": "Starter",
        "description": "Get started with your first SaaS startup.",
        "features_title": "Includes",
        "features": [
          "100 credits, valid for 1 month",
          "NextJS boilerplate",
          "SEO-friendly structure",
          "Payment with Stripe",
          "Data storage with Supabase",
          "Google Oauth & One-Tap Login",
    
...
```

Example 4 (unknown):
```unknown
{
  "pricing": {
    "name": "pricing",
    "label": "Pricing",
    "title": "Pricing",
    "description": "Get all features of ShipAny, Ship your AI SaaS startups fast.",
    "groups": [],
    "items": [
      {
        "title": "Starter",
        "description": "Get started with your first SaaS startup.",
        "features_title": "Includes",
        "features": [
          "100 credits, valid for 1 month",
          "NextJS boilerplate",
          "SEO-friendly structure",
          "Payment with Stripe",
          "Data storage with Supabase",
          "Google Oauth & One-Tap Login",
    
...
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/features/payment/stripe#订阅支付

**Contents:**
- Stripe
- Stripe 设置
- ShipAny 配置
- 价格表支付
  - 配置价格表内容
  - 修改价格表组件
  - 修改价格表下单逻辑
  - 修改支付回调逻辑
  - 修改支付通知逻辑
- 自定义支付

ShipAny 支持使用 Stripe 进行支付，可用于产品付款、会员订阅、购买积分等场景。

在 ShipAny 项目配置文件中，填写 Stripe 相关的配置信息。

页面路径可以填相对路径，也可以填绝对路径。如果填的是相对路径，跳转时会自动拼接 NEXT_PUBLIC_WEB_URL 配置的网站地址，并带上多语言参数。

比如按照以上配置，在中文页面支付成功后的跳转路径是：http://localhost:3000/zh/my-orders

ShipAny 模板内置了一个价格表和对应的支付逻辑，你可以根据自己的需求，简单修改即可快速实现支付功能。

ShipAny 模板内置的价格表配置文件位于：src/i18n/pages/pricing 目录下，支持多语言，默认包含 en.json 和 zh.json 两个价格表配置文件。

你可以根据自己的需求，修改价格表配置文件中的内容。

默认的价格表组件位于：src/components/blocks/pricing/index.tsx

你可以根据自己的需求，修改价格表的展示形式。

默认的价格表下单逻辑位于：src/app/api/checkout/route.ts

你可以根据自己的需求，修改价格表的下单逻辑。

在价格表下单逻辑中，默认配置的支付回调地址是：/api/pay/callback/stripe

用户支付后，会在浏览器跳转到这个地址，并带上包含支付信息的参数。

默认的支付回调处理逻辑位于：src/app/api/pay/callback/stripe/route.ts

你可以根据自己的需求，修改处理支付回调的逻辑，比如更新订单状态、给用户发送邮件通知、给用户赠送积分等。

支付回调是同步逻辑，依赖浏览器跳转到回调地址，才能处理支付结果。这种方式不太可靠，可能出现跳转过程中用户关闭了浏览器等情况，导致支付结果没有被正常处理。 更可靠的方式是通过 Webhook，配置支付结果异步通知。

比如把 Webhook 地址配置为：https://your-domain.com/api/pay/notify/stripe

用户支付后，Stripe 会把支付信息推送到这个地址。

默认的支付通知逻辑位于：src/app/api/pay/notify/stripe/route.ts

你可以根据自己的需求，修改处理支付通知的逻辑，比如更新订单状态、给用户发送邮件通知、给用户赠送积分等。

修改价格表配置文件，添加 groups 数据，配置多个价格分组。并在 pricing.items 下为每一个价格方案，设置一个 group 名称。

配置完成后，点击价格分组，将根据 group 字段，切换显示不同的价格方案。

ShipAny 模板使用 Stripe 支付时，默认支持三种支付方案

你只需要修改价格表配置，把每个价格方案的 interval 字段，设置成上述三个值之一。

同时，按需修改价格(amount) / 积分(credits) / 有效期(valid_months) 等字段。

举例：按月订阅扣费，月付 $99，购买后得到 30 个积分，有效期 1 个月，则核心的价格表配置信息为：

修改 src/app/api/checkout/route.ts 文件，设置 Stripe 下单的 options 参数。

在 Stripe 后台 设置支付方式，开通支付宝和微信支付。

修改价格表配置文件，在每个价格方案下添加一个 cn_amount 字段，即可支持人民币支付。

比如，产品售价，$99，人民币支付价格为 699 元，核心配置信息为：

配置完成后，在价格表下单按钮上方，将会显示一个人民币支付图标。

在 Stripe 后台点击左上角的店铺打开下拉菜单，依次点击 Switch to sandbox -> Test mode，开启测试模式。

在测试模式下，进入开发者中心，设置 测试支付密钥，包括 Publishable key 和 Secret key。

注册 ngrok 账号，按指示安装 ngrok 命令行工具。

启动 ngrok 服务，监听本地端口，并生成一个临时的域名。

在 Stripe 后台测试模式中，配置 Webhook 地址为 ngrok 生成的域名，并监听以下两个事件：

Endpoint 填写支付通知地址，比如 https://xxx.ngrok-free.app/api/pay/notify/stripe。

添加 Webhook 地址后，在 Webhook 管理页面，复制 Signing secret，

跟支付密钥一起填入 .env.development 文件中。

在本地启动项目，访问 /pricing 页面，点击下单按钮，下单成功后跳转到支付页面。

使用 Stripe 测试卡 支付，支付成功后浏览器跳转到支付回调地址，监听的地址收到支付通知。

**Examples:**

Example 1 (unknown):
```unknown
NEXT_PUBLIC_WEB_URL = "http://localhost:3000"

NEXT_PUBLIC_PAY_SUCCESS_URL = "/my-orders"
NEXT_PUBLIC_PAY_FAIL_URL = "/pricing"
NEXT_PUBLIC_PAY_CANCEL_URL = "/pricing"

PAY_PROVIDER = "stripe"

STRIPE_PUBLIC_KEY = "pk_test_xxx"
STRIPE_PRIVATE_KEY = "sk_test_xxx"
STRIPE_WEBHOOK_SECRET = "whsec_cexxx"
```

Example 2 (unknown):
```unknown
NEXT_PUBLIC_WEB_URL = "http://localhost:3000"

NEXT_PUBLIC_PAY_SUCCESS_URL = "/my-orders"
NEXT_PUBLIC_PAY_FAIL_URL = "/pricing"
NEXT_PUBLIC_PAY_CANCEL_URL = "/pricing"

PAY_PROVIDER = "stripe"

STRIPE_PUBLIC_KEY = "pk_test_xxx"
STRIPE_PRIVATE_KEY = "sk_test_xxx"
STRIPE_WEBHOOK_SECRET = "whsec_cexxx"
```

Example 3 (unknown):
```unknown
{
  "pricing": {
    "name": "pricing",
    "label": "Pricing",
    "title": "Pricing",
    "description": "Get all features of ShipAny, Ship your AI SaaS startups fast.",
    "groups": [],
    "items": [
      {
        "title": "Starter",
        "description": "Get started with your first SaaS startup.",
        "features_title": "Includes",
        "features": [
          "100 credits, valid for 1 month",
          "NextJS boilerplate",
          "SEO-friendly structure",
          "Payment with Stripe",
          "Data storage with Supabase",
          "Google Oauth & One-Tap Login",
    
...
```

Example 4 (unknown):
```unknown
{
  "pricing": {
    "name": "pricing",
    "label": "Pricing",
    "title": "Pricing",
    "description": "Get all features of ShipAny, Ship your AI SaaS startups fast.",
    "groups": [],
    "items": [
      {
        "title": "Starter",
        "description": "Get started with your first SaaS startup.",
        "features_title": "Includes",
        "features": [
          "100 credits, valid for 1 month",
          "NextJS boilerplate",
          "SEO-friendly structure",
          "Payment with Stripe",
          "Data storage with Supabase",
          "Google Oauth & One-Tap Login",
    
...
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/features/oauth#谷歌登录

**Contents:**
- 登录鉴权
- 生成 Auth Secret
- 谷歌登录
- 谷歌一键登录
- Github 登录
- 登录预览
- 参考

ShipAny 目前支持 谷歌登录 / 谷歌一键登录 / Github 登录三种登录方式。

其他登录方式逐步集成，也可以参考 next-auth 文档自行接入。

生成一个 32 字节的随机字符串，作为 Auth Secret

修改环境变量中的 AUTH_SECRET 值

创建一个新项目，进入新项目的 Credentials 管理页面，创建 Oauth Client ID

创建 Oauth Client ID 后，得到 Client ID 和 Client Secret

首先按照谷歌登录的步骤，拿到 AUTH_GOOGLE_ID 和 AUTH_GOOGLE_SECRET

修改配置文件中的 NEXT_PUBLIC_AUTH_GOOGLE_ONE_TAP_ENABLED 和 NEXT_PUBLIC_AUTH_GOOGLE_ID

谷歌一键登录使用到的 NEXT_PUBLIC_AUTH_GOOGLE_ID 跟谷歌登录配置的 AUTH_GOOGLE_ID 保持一致。

开发环境和生产环境，需要创建两个不同的 OAuth app，分别配置不同的回调地址。

进入 OAuth app，复制 Client ID 和 Client Secret

修改配置文件中的 AUTH_GITHUB_ID 和 AUTH_GITHUB_SECRET

**Examples:**

Example 1 (unknown):
```unknown
openssl rand -base64 32
```

Example 2 (unknown):
```unknown
openssl rand -base64 32
```

Example 3 (unknown):
```unknown
AUTH_SECRET = "xxx"
```

Example 4 (unknown):
```unknown
AUTH_SECRET = "xxx"
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/features/payment/creem#creem-设置

**Contents:**
- Creem
- Creem 设置
- ShipAny 配置
- 价格表支付
  - 配置价格表内容
  - 修改价格表组件
  - 修改价格表下单逻辑
  - 修改支付回调逻辑
  - 修改支付通知逻辑
- 本地测试

ShipAny 支持使用 Creem 进行支付，可用于产品付款、会员订阅、购买积分等场景。

在 ShipAny 项目配置文件中，填写 Creem 相关的配置信息。

页面路径可以填相对路径，也可以填绝对路径。如果填的是相对路径，跳转时会自动拼接 NEXT_PUBLIC_WEB_URL 配置的网站地址，并带上多语言参数。

比如按照以上配置，在中文页面支付成功后的跳转路径是：http://localhost:3000/zh/my-orders

比如在 ShipAny 项目中设置的价格表有三个支付方案，对应的 product_id 分别是 starter、standard、premium，你需要在 Creem 后台为这三个方案 创建对应的产品，复制每个产品的 Product ID，与价格表中的 product_id 对应关系填写到 CREEM_PRODUCTS 中。

ShipAny 模板内置了一个价格表和对应的支付逻辑，你可以根据自己的需求，简单修改即可快速实现支付功能。

ShipAny 模板内置的价格表配置文件位于：src/i18n/pages/pricing 目录下，支持多语言，默认包含 en.json 和 zh.json 两个价格表配置文件。

你可以根据自己的需求，修改价格表配置文件中的内容。

默认的价格表组件位于：src/components/blocks/pricing/index.tsx

你可以根据自己的需求，修改价格表的展示形式。

默认的价格表下单逻辑位于：src/app/api/checkout/route.ts

你可以根据自己的需求，修改价格表的下单逻辑。

在价格表下单逻辑中，默认配置的支付回调地址是：/api/pay/callback/creem

用户支付后，会在浏览器跳转到这个地址，并带上包含支付信息的参数。

默认的支付回调处理逻辑位于：src/app/api/pay/callback/creem/route.ts

你可以根据自己的需求，修改处理支付回调的逻辑，比如更新订单状态、给用户发送邮件通知、给用户赠送积分等。

支付回调是同步逻辑，依赖浏览器跳转到回调地址，才能处理支付结果。这种方式不太可靠，可能出现跳转过程中用户关闭了浏览器等情况，导致支付结果没有被正常处理。 更可靠的方式是通过 Webhook，配置支付结果异步通知。

比如把 Webhook 地址配置为：https://your-domain.com/api/pay/notify/creem

用户支付后，Creem 会把支付信息推送到这个地址。

默认的支付通知逻辑位于：src/app/api/pay/notify/creem/route.ts

你可以根据自己的需求，修改处理支付通知的逻辑，比如更新订单状态、给用户发送邮件通知、给用户赠送积分等。

在 Creem 后台进入店铺，点击右上角的 Test mode，开启测试模式。

在测试模式下，进入开发者中心，设置 测试 API 密钥。

注册 ngrok 账号，按指示安装 ngrok 命令行工具。

启动 ngrok 服务，监听本地端口，并生成一个临时的域名。

在 Creem 后台测试模式中，配置 Webhook 地址为 ngrok 生成的域名

Endpoint 填写支付通知地址，比如 https://xxx.ngrok-free.app/api/pay/notify/creem。

添加 Webhook 地址后，在 Webhook 管理页面，复制 Signing secret，

跟支付密钥一起填入 .env.development 文件中。

在本地启动项目，访问 /pricing 页面，点击下单按钮，下单成功后跳转到支付页面。

使用 Stripe 测试卡 支付，支付成功后浏览器跳转到支付回调地址，监听的地址收到支付通知。

**Examples:**

Example 1 (unknown):
```unknown
NEXT_PUBLIC_WEB_URL = "http://localhost:3000"

NEXT_PUBLIC_PAY_SUCCESS_URL = "/my-orders"
NEXT_PUBLIC_PAY_FAIL_URL = "/pricing"
NEXT_PUBLIC_PAY_CANCEL_URL = "/pricing"

PAY_PROVIDER = "creem"

CREEM_ENV = "test"
CREEM_API_KEY = "creem_test_xxx"
CREEM_WEBHOOK_SECRET = "whsec_xxx"
CREEM_PRODUCTS = '{"starter": "prod_xxx", "standard": "prod_xxx", "premium": "prod_xxx"}'
```

Example 2 (unknown):
```unknown
NEXT_PUBLIC_WEB_URL = "http://localhost:3000"

NEXT_PUBLIC_PAY_SUCCESS_URL = "/my-orders"
NEXT_PUBLIC_PAY_FAIL_URL = "/pricing"
NEXT_PUBLIC_PAY_CANCEL_URL = "/pricing"

PAY_PROVIDER = "creem"

CREEM_ENV = "test"
CREEM_API_KEY = "creem_test_xxx"
CREEM_WEBHOOK_SECRET = "whsec_xxx"
CREEM_PRODUCTS = '{"starter": "prod_xxx", "standard": "prod_xxx", "premium": "prod_xxx"}'
```

Example 3 (unknown):
```unknown
{
  "pricing": {
    "name": "pricing",
    "label": "Pricing",
    "title": "Pricing",
    "description": "Get all features of ShipAny, Ship your AI SaaS startups fast.",
    "groups": [],
    "items": [
      {
        "title": "Starter",
        "description": "Get started with your first SaaS startup.",
        "features_title": "Includes",
        "features": [
          "100 credits, valid for 1 month",
          "NextJS boilerplate",
          "SEO-friendly structure",
          "Payment with Stripe",
          "Data storage with Supabase",
          "Google Oauth & One-Tap Login",
    
...
```

Example 4 (unknown):
```unknown
{
  "pricing": {
    "name": "pricing",
    "label": "Pricing",
    "title": "Pricing",
    "description": "Get all features of ShipAny, Ship your AI SaaS startups fast.",
    "groups": [],
    "items": [
      {
        "title": "Starter",
        "description": "Get started with your first SaaS startup.",
        "features_title": "Includes",
        "features": [
          "100 credits, valid for 1 month",
          "NextJS boilerplate",
          "SEO-friendly structure",
          "Payment with Stripe",
          "Data storage with Supabase",
          "Google Oauth & One-Tap Login",
    
...
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/features/blog#管理博客内容

**Contents:**
- 博客
- 配置 CMS
- 管理博客内容
- 配置博客路由

ShipAny 内置一套 CMS 系统，用于博客内容管理，支持多语言。

为了能可视化管理博客内容，你需要 配置管理后台。

博客的标题和访问路由(slug)必填，默认支持多语言，需要选择对应的语言。

访问博客列表前台路由，可以看到在后台添加的博客内容。

默认的博客路由是 /posts，按照上述步骤添加博客内容后，你可以在 i18n/pages/landing 的 json 文件中添加导航项，显示博客列表的入口。

你需要添加自定义的文件夹，并参考 app/[locale]/(default)/posts 文件夹组织自定义的代码。

**Examples:**

Example 1 (unknown):
```unknown
CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    uuid VARCHAR(255) UNIQUE NOT NULL,
    slug VARCHAR(255),
    title VARCHAR(255),
    description TEXT,
    content TEXT,
    created_at timestamptz,
    updated_at timestamptz,
    status VARCHAR(50),
    cover_url VARCHAR(255),
    author_name VARCHAR(255),
    author_avatar_url VARCHAR(255),
    locale VARCHAR(50)
);
```

Example 2 (unknown):
```unknown
CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    uuid VARCHAR(255) UNIQUE NOT NULL,
    slug VARCHAR(255),
    title VARCHAR(255),
    description TEXT,
    content TEXT,
    created_at timestamptz,
    updated_at timestamptz,
    status VARCHAR(50),
    cover_url VARCHAR(255),
    author_name VARCHAR(255),
    author_avatar_url VARCHAR(255),
    locale VARCHAR(50)
);
```

Example 3 (unknown):
```unknown
https://{your-domain}/admin/posts
```

Example 4 (unknown):
```unknown
https://{your-domain}/admin/posts
```

---
