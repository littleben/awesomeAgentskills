# Shipany - Deployment

**Pages:** 7

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/deploy/deploy-to-cloudflare

**Contents:**
- 部署到 Cloudflare
- 使用 cloudflare 分支
- 部署流程
- 参考资料

ShipAny 使用 OpenNext 框架，支持一键部署到 Cloudflare。

使用 ShipAny 开发新项目时，如果希望部署到 Cloudflare Workers，建议拉取 cloudflare 分支，无需额外修改，支持一键部署。

按需修改 .env.production 文件中的配置：项目域名、数据库、登录授权等配置。

把上一步在 .env.production 文件中配置好的生产环境变量，复制到 wrangler.toml 文件中的 [vars] 下面，并且修改 wrangler.toml 文件中的项目名称 name

按照提示，输入要部署的项目名称和分支名称(main)，连接上你的 Cloudflare 账号，然后等待部署完成。

使用默认生成的域名可访问项目，绑定自定义域名可正式上线。

**Examples:**

Example 1 (unknown):
```unknown
git clone -b cloudflare [email protected]:shipanyai/shipany-template-one.git my-shipany-project
```

Example 2 (unknown):
```unknown
git clone -b cloudflare [email protected]:shipanyai/shipany-template-one.git my-shipany-project
```

Example 3 (unknown):
```unknown
cp .env.example .env.production
```

Example 4 (unknown):
```unknown
cp .env.example .env.production
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/deploy/deploy-to-vercel#部署流程

**Contents:**
- 部署到 Vercel
- 部署流程
- 参考资料

先在本地开发好你自己的项目，代码提交到 Github 私有仓库。

在 Vercel 控制台创建新项目，导入代码仓库，一键部署

你也可以在 Vercel 控制台，添加自定义域名

先在本地编辑好 .env.production 的内容，填写生产环境配置，再复制粘贴到 Vercel 的环境变量中。

下一次推送代码，自动重新部署，应用新的环境变量

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/deploy/deploy-to-vercel

**Contents:**
- 部署到 Vercel
- 部署流程
- 参考资料

先在本地开发好你自己的项目，代码提交到 Github 私有仓库。

在 Vercel 控制台创建新项目，导入代码仓库，一键部署

你也可以在 Vercel 控制台，添加自定义域名

先在本地编辑好 .env.production 的内容，填写生产环境配置，再复制粘贴到 Vercel 的环境变量中。

下一次推送代码，自动重新部署，应用新的环境变量

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/deploy/deploy-to-vercel#参考资料

**Contents:**
- 部署到 Vercel
- 部署流程
- 参考资料

先在本地开发好你自己的项目，代码提交到 Github 私有仓库。

在 Vercel 控制台创建新项目，导入代码仓库，一键部署

你也可以在 Vercel 控制台，添加自定义域名

先在本地编辑好 .env.production 的内容，填写生产环境配置，再复制粘贴到 Vercel 的环境变量中。

下一次推送代码，自动重新部署，应用新的环境变量

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/deploy/deploy-to-cloudflare#部署流程

**Contents:**
- 部署到 Cloudflare
- 使用 cloudflare 分支
- 部署流程
- 参考资料

ShipAny 使用 OpenNext 框架，支持一键部署到 Cloudflare。

使用 ShipAny 开发新项目时，如果希望部署到 Cloudflare Workers，建议拉取 cloudflare 分支，无需额外修改，支持一键部署。

按需修改 .env.production 文件中的配置：项目域名、数据库、登录授权等配置。

把上一步在 .env.production 文件中配置好的生产环境变量，复制到 wrangler.toml 文件中的 [vars] 下面，并且修改 wrangler.toml 文件中的项目名称 name

按照提示，输入要部署的项目名称和分支名称(main)，连接上你的 Cloudflare 账号，然后等待部署完成。

使用默认生成的域名可访问项目，绑定自定义域名可正式上线。

**Examples:**

Example 1 (unknown):
```unknown
git clone -b cloudflare [email protected]:shipanyai/shipany-template-one.git my-shipany-project
```

Example 2 (unknown):
```unknown
git clone -b cloudflare [email protected]:shipanyai/shipany-template-one.git my-shipany-project
```

Example 3 (unknown):
```unknown
cp .env.example .env.production
```

Example 4 (unknown):
```unknown
cp .env.example .env.production
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/deploy/deploy-to-cloudflare#使用-cloudflare-分支

**Contents:**
- 部署到 Cloudflare
- 使用 cloudflare 分支
- 部署流程
- 参考资料

ShipAny 使用 OpenNext 框架，支持一键部署到 Cloudflare。

使用 ShipAny 开发新项目时，如果希望部署到 Cloudflare Workers，建议拉取 cloudflare 分支，无需额外修改，支持一键部署。

按需修改 .env.production 文件中的配置：项目域名、数据库、登录授权等配置。

把上一步在 .env.production 文件中配置好的生产环境变量，复制到 wrangler.toml 文件中的 [vars] 下面，并且修改 wrangler.toml 文件中的项目名称 name

按照提示，输入要部署的项目名称和分支名称(main)，连接上你的 Cloudflare 账号，然后等待部署完成。

使用默认生成的域名可访问项目，绑定自定义域名可正式上线。

**Examples:**

Example 1 (unknown):
```unknown
git clone -b cloudflare [email protected]:shipanyai/shipany-template-one.git my-shipany-project
```

Example 2 (unknown):
```unknown
git clone -b cloudflare [email protected]:shipanyai/shipany-template-one.git my-shipany-project
```

Example 3 (unknown):
```unknown
cp .env.example .env.production
```

Example 4 (unknown):
```unknown
cp .env.example .env.production
```

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/deploy/deploy-to-cloudflare#参考资料

**Contents:**
- 部署到 Cloudflare
- 使用 cloudflare 分支
- 部署流程
- 参考资料

ShipAny 使用 OpenNext 框架，支持一键部署到 Cloudflare。

使用 ShipAny 开发新项目时，如果希望部署到 Cloudflare Workers，建议拉取 cloudflare 分支，无需额外修改，支持一键部署。

按需修改 .env.production 文件中的配置：项目域名、数据库、登录授权等配置。

把上一步在 .env.production 文件中配置好的生产环境变量，复制到 wrangler.toml 文件中的 [vars] 下面，并且修改 wrangler.toml 文件中的项目名称 name

按照提示，输入要部署的项目名称和分支名称(main)，连接上你的 Cloudflare 账号，然后等待部署完成。

使用默认生成的域名可访问项目，绑定自定义域名可正式上线。

**Examples:**

Example 1 (unknown):
```unknown
git clone -b cloudflare [email protected]:shipanyai/shipany-template-one.git my-shipany-project
```

Example 2 (unknown):
```unknown
git clone -b cloudflare [email protected]:shipanyai/shipany-template-one.git my-shipany-project
```

Example 3 (unknown):
```unknown
cp .env.example .env.production
```

Example 4 (unknown):
```unknown
cp .env.example .env.production
```

---
