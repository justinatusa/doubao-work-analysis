# 00 · 时间线

捕获窗口：**2026-09-24**（Asia/Shanghai）。

## 材料性质

- 来源：用户与豆包工作 Agent 的多轮对话；模型在沙箱内执行勘察后口述结果。
- 整理原则：不照抄聊天原文；抽取可复核的标识符、路径、行为，并标 **实测 / 推断**。
- 风险说明：出口 IP、函数名等会轮换；本笔记记录的是当次快照。

## 轮次摘要

| 轮次 | 用户意图（归纳） | 模型吐出的关键层 |
|------|------------------|------------------|
| R1 | 我是谁 / 网络能否出公网、境外站 / 机器配置 | 临时 Ubuntu 沙箱；veFaaS 风格主机名；分类出网；失败路径（robots / 分支名 / API 限流） |
| R2 | 为何「火山又像阿里」；NAT；像网安一样深挖基建 | 计算在火山；出口经 VortexIP；落地 ASN 可属阿里；Kata+Nydus；代理链；桌面与 Chrome 指纹 |
| R3 | npm / pip 是否厂内源；防封 IP | npm 默认 npmmirror；官方 registry 经透明缓存网关；响应头显示真实 Cloudflare/Fastly/S3 |
| R4 | 六块取证：会话生命周期、浏览器、MCP、Security review、hijack、配额 | 持久卷；自研 CDP 桥；仅 browser MCP；审查在容器外；飞书 MITM；cgroup 硬限 |

## 下一轮计划（动态）

在已有拼图上补：会话目录结构、热池借还、nginx 对外暴露、MCP 过滤清单、办公版开关、文件进出、平台代码指纹；并穿插更「基建工程师」视角的多样追问（镜像构建、可观测性、多租户隔离等）。

| R5 | A–G：会话结构、热池、对外暴露、MCP 过滤、office、文件 IO、代码指纹 | 双目录 chats + agent_mode；standby/cold；noVNC 全链路；内置 Sandbox MCP；创作画布 CLI 方案名；Go 模块 `code.byted.org/flow/*` |
