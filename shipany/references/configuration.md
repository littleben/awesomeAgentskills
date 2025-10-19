# Shipany - Configuration

**Pages:** 3

---

## ShipAny Docs

**URL:** https://docs.shipany.ai/zh/admin-system/admin#管理员配置

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

**URL:** https://docs.shipany.ai/zh/tutorials/edit-agreement#修改路由配置

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

**URL:** https://docs.shipany.ai/zh/user-console/credits#配置积分管理系统

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
