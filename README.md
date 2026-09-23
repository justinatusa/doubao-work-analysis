# Doubao Work Analysis

Obsidian 式知识库：用 GitHub 存可版本化的 Markdown。主题是 **豆包工作 Agent 云沙箱运行时** 的观察型 teardown（非官方文档）。

## 怎么读

1. 先看本页 TL;DR  
2. 总图 → [`docs/architecture.md`](docs/architecture.md)  
3. 按兴趣进 `docs/` 各篇  
4. 未决 → [`docs/open-questions.md`](docs/open-questions.md)  
5. 观测日志 → [`changelog.md`](changelog.md)

对外长文（若有）只放在 [`publish/`](publish/)；**Source of Truth 是 `docs/`**。

## TL;DR（2026-09-24）

1. **形态**：Agent + 临时 Linux 云电脑（Kata microVM），带桌面、Chrome、MCP、受控出网。  
2. **计算**：火山 ByteFaaS/veFaaS；约 2 vCPU / 4 GiB；`/home/user` 经 hpvs 可跨会话。  
3. **网络**：VortexIP 出口 + 共享 NAT；技术站白名单，常见消费站黑洞；包源走公开镜像或透明缓存。  
4. **Agent**：模型侧 browser MCP（自研 CDP）+ 内置 Sandbox 工具；飞书域名本地 MITM，鉴权回平台。  
5. **暴露**：沙箱 nginx 信任内网；用户鉴权在外层网关。

## 目录（MOC）

| 路径 | 内容 |
|------|------|
| [docs/method.md](docs/method.md) | 方法与图例 |
| [docs/architecture.md](docs/architecture.md) | 架构总图 |
| [docs/compute.md](docs/compute.md) | 计算 / 沙箱 / 配额 |
| [docs/network.md](docs/network.md) | 出口 / DNS / 包源 |
| [docs/agent-surface.md](docs/agent-surface.md) | MCP / ComputerUse / 会话 |
| [docs/desktop-expose.md](docs/desktop-expose.md) | noVNC / nginx / CDP |
| [docs/persistence-io.md](docs/persistence-io.md) | 热池 / 上传下载 |
| [docs/product-fingerprint.md](docs/product-fingerprint.md) | 创作画布 / 内部模块 |
| [docs/open-questions.md](docs/open-questions.md) | 未决 |
| [changelog.md](changelog.md) | 观测日志 |
| [publish/](publish/) | 对外稿（占位） |
| [evidence/](evidence/) | 可选证据摘录 |

## 归类

英文标签：`agent sandbox teardown` · `runtime anatomy` · `observational reverse engineering`  
中文：豆包工作 · Agent 云沙箱运行时拆解
