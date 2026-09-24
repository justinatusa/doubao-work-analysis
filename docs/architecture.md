# 架构总图

下面这张图，是把 **2026-09-24** 当天在沙箱里看到的组件串起来的总览。细节在各主题文。  
当时沙箱通过环境变量 `IMAGE_VERSION` 自报的镜像版本是 **1.14.10**（这是镜像构建号，不是 Ubuntu 版本，也不是豆包 App 版本）。

## 图上专有词（首次释义）

| 词 | 白话 |
|----|------|
| **Kata** | 用轻量虚拟机（microVM）做隔离，比普通容器进程隔离更硬一点 |
| **Nydus** | 镜像按需拉取/加载的一层技术，不必整包先下完 |
| **MCP** | Model Context Protocol：模型调用外部工具的一种接口/总线 |
| **CDP** | Chrome DevTools Protocol：调试与遥控 Chrome 的协议 |
| **VortexIP** | 平台侧出口代理；公网看到的来源 IP 往往是过它之后的落地地址 |
| **信任内网** | 沙箱内 nginx 假定流量已在外层网关验过用户票，本机不再验一次 |
| **gem** | 观测到的沙箱镜像内平台运行时目录前缀（如 `/opt/gem`、`/var/log/gem`），不是独立对外产品名 |
| **hpvs** | 观测到的持久卷文件系统名；对用户含义：关对话后，家目录里的文件往往还在 |

![豆包工作 Agent 沙箱架构总图](assets/architecture.svg)

### 图的文字版（从外到内）

1. 用户浏览器先到**外层网关**，在那里验证身份（JWT）。
2. 流量进入沙箱后先到监听 8080 端口的 **nginx**。nginx 按信任内网配置，不再重复验票。
3. nginx 把请求分给五类服务：桌面（noVNC / Xvnc）、Chrome 的 CDP 调试口（9222）、MCP hub（8091）、平台 VM API（10000，含 CC 文件/命令通道与 ComputerUse 键鼠通道，需要平台签名）、运行时钩子（10080）。
4. MCP hub 下挂着 **browser MCP**（8100），它用 CDP 协议遥控 Chrome，模型可以直接调用。
5. 以上进程都由 **supervisord** 托管，配置在 `/opt/gem`。
6. 沙箱出网先经过本地代理（tinyproxy、gost、飞书域名本地劫持），再经 **VortexIP** 平台出口到公网共享 NAT。
7. 存储分两类：`/home/user` 在 hpvs 持久卷上，关对话后往往还在；根目录和 `/tmp/user` 是本实例本地盘，实例回收即消失。
8. 整个沙箱是一台 Kata 微虚拟机，镜像用 Nydus 按需加载，跑在火山 ByteFaaS / veFaaS 函数算力上。

## 主组件索引

| 层 | 要点 | 详见 |
|----|------|------|
| 方法 | 实测 / 推断 / 未测到 | [method.md](method.md) |
| 预装 | 出厂软件与镜像构建号 | [preinstall.md](preinstall.md) |
| 计算 | Kata、Nydus、配额、挂载 | [compute.md](compute.md) |
| 网络 | 出口代理、DNS、包源 | [network.md](network.md) |
| Agent | 三条工具通道、MCP、会话目录 | [agent-surface.md](agent-surface.md) |
| 暴露 | noVNC、CDP、沙箱内 nginx | [desktop-expose.md](desktop-expose.md) |
| 持久化 | 热池、上传下载 | [persistence-io.md](persistence-io.md) |
| 产品指纹 | AIO、创作画布、内部模块名 | [product-fingerprint.md](product-fingerprint.md) |
| 可观测 | 日志、OpenTelemetry | [observability.md](observability.md) |
| 对照 | 与其他家沙箱并排 | [comparables.md](comparables.md) |
| 未决 | 仍缺证据的问题 | [open-questions.md](open-questions.md) |
