# Doubao Work Analysis

对 **豆包工作（Doubao Work）** 运行时沙箱的观察笔记。材料来自对产品内 Agent 的现场取证式提问（让其在沙箱内跑命令、读配置、测网络），**不是**字节 / 火山官方文档。

| 图例 | 含义 |
|------|------|
| **实测** | 有路径、命令或响应头支撑 |
| **推断** | 由产品形态或旁证推出，尚未坐实 |

## 一页结论

1. **形态**：Agent + 临时 Linux 云电脑（microVM），带桌面、Chrome、MCP 工具面、受控出网。
2. **计算层（实测）**：火山引擎 ByteFaaS / veFaaS；Kata Containers + Nydus；约 2 vCPU / 4 GiB；函数名形如 `super-25-general-agent-efs`。
3. **网络层（实测）**：容器内多层代理 → VortexIP 出口；落地 IP 可落在阿里云 ASN（共享 NAT）；按域名白名单 / DNS 黑洞分流；包管理走公开镜像或透明缓存网关。
4. **Agent 面（实测）**：模型侧 MCP 目前主要挂 **browser**（自研 CDP 桥）；飞书 / Lark 相关域名被本地 MITM 劫持，鉴权回源平台管控面。
5. **持久化（实测）**：`/home/user` 走 hpvs 共享存储，会话目录可跨天保留；根 overlay 随实例销毁。

## 文档索引

| 文档 | 内容 |
|------|------|
| [notes/00-timeline.md](notes/00-timeline.md) | 诱导时间线与材料来源 |
| [notes/01-compute-sandbox.md](notes/01-compute-sandbox.md) | 计算 / 沙箱 / 挂载 / 配额 |
| [notes/02-network-egress.md](notes/02-network-egress.md) | 出口代理 / DNS / NAT / 包源 |
| [notes/03-agent-runtime.md](notes/03-agent-runtime.md) | MCP / Chrome / hijack / 会话 |
| [notes/04-agent-surface.md](notes/04-agent-surface.md) | MCP / ComputerUse / 会话目录 |
| [notes/05-desktop-expose.md](notes/05-desktop-expose.md) | noVNC / nginx / CDP 对外 |
| [notes/06-persistence-io.md](notes/06-persistence-io.md) | 热池同步 / 上传下载 |
| [notes/07-product-fingerprint.md](notes/07-product-fingerprint.md) | 创作画布 CLI / 内部模块 |
| [notes/open-questions.md](notes/open-questions.md) | 尚未坐实的洞 |

## 方法（简述）

不依赖外部漏洞利用：在产品对话里要求模型做「现场勘察」（进程树、挂载、cgroup、代理环境、证书、MCP handshake）。结论随产品版本会变；以当次实测为准。

## 仓库定位

偏 **证据驱动的逆向笔记**，结构刻意做薄（可对照作者另一仓库 `llm-api-protocols` 的 Layer0/1/2，但本仓尚未拆那么细）。后续若材料变厚，可再升成 `docs/` 手册。

捕获窗口：2026-09-24（Asia/Shanghai）。
