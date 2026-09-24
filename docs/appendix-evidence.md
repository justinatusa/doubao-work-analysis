# 附录：证据索引与可比产品

观测日 **2026-09-24**，`IMAGE_VERSION=1.14.10`。  
主文主张与下列打码摘录互证；摘录由诱导会话回报重构，不是原始终端全量 dump。

## 打码摘录（`evidence/2026-09-24/`）

| 文件 | 对应主张 |
|------|----------|
| [01-get-context-redacted.md](../evidence/2026-09-24/01-get-context-redacted.md) | 镜像版本 / 运行时概览 |
| [02-mounts-cgroup-redacted.md](../evidence/2026-09-24/02-mounts-cgroup-redacted.md) | 挂载与配额 |
| [03-mcp-tools-list-redacted.md](../evidence/2026-09-24/03-mcp-tools-list-redacted.md) | Sandbox MCP 工具面 |
| [04-nginx-locations-redacted.md](../evidence/2026-09-24/04-nginx-locations-redacted.md) | 对外暴露路径 |
| [05-hijack-domains-redacted.md](../evidence/2026-09-24/05-hijack-domains-redacted.md) | 本机劫持域名清单（样例） |

索引页：[evidence/2026-09-24/README.md](../evidence/2026-09-24/README.md)。

## 与业界同类的对照（公开信息）

本表只放 **可引用的公开文档结论** 与本仓 **Doubao Work 观测** 的并排。不编造对方内部细节。Doubao 列均标注观测日 / `IMAGE_VERSION`。

| 轴 | Doubao Work（本仓观测） | AWS Bedrock AgentCore Runtime（公开文档） | Claude Managed Agents（公开工程叙述） |
|----|-------------------------|---------------------------------------------|----------------------------------------|
| 隔离基质 | Kata microVM + Nydus（实测路径线索） | Firecracker microVM（[docs](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-how-it-works.html)） | 云沙箱；自托管侧常见 gVisor 等更强隔离建议（[engineering](https://www.anthropic.com/engineering/managed-agents)、[secure deployment](https://code.claude.com/docs/en/agent-sdk/secure-deployment.md)） |
| 会话生命周期 | idle TTL **未测到**；见函数超时等局部变量 | 公开：idle / max lifetime 可配；终止后 microVM 销毁并清理内存（[sessions](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-sessions.html)） | session 为事件日志接口；sandbox 可替换（脑/手/会话解耦） |
| 网络模式 | 受控出口代理 + 域名分流样例（见主文网络节）；非「随意公网」 | `PUBLIC` 或 `VPC`（[VPC guide](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agentcore-vpc.html)） | 托管沙箱出站由平台策略约束；自托管则出站留在你的环境 |
| 工具 / 「手」 | 三通道：browser MCP（模型）、CC、ComputerUse（平台签名） | Runtime 调用 + 同会话命令执行等（公开 API） | harness 调工具；hands = sandbox/tools |
| 持久化 | hpvs home 跨会话；standby 热池 | 会话文件系统默认偏临时；长期靠 Memory 等产品能力 | session 日志与 sandbox 文件系统可分离 |
| 审计 / 轨迹 | 容器内 gem 日志；trajectory 出沙箱 **未测到** | 文档强调日志 / traces / 可观测 | session 事件日志为显式接口 |
| 热池 | `MCP_VM_STANDBY` + post_hook（实测） | 文档描述会话亲和与冷启动，热池细节以官方为准 | 自托管 K8s 方案可见 warm pool 类设计（生态文档） |

### 怎么用这张表

- 读 Doubao 列时回到 [主文](sandbox-outside-in.md) 看路径级证据。  
- 读其他列时点官方链接，勿把第三方 teardown 博客当官网。  
- 空白 / 「未测到」不要脑补成「一定没有」。

## 方法说明（一句话）

材料来自产品对话里的现场取证：让 Agent 执行命令、读配置、探测网络，再把可核对结论整理进本仓。不是二进制逆向教程，也不是未授权渗透指南。
