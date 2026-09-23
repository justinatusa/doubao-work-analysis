# 网络与出口

> **范围说明：** 下列域名结果为当次抽样，不是完整 allow/deny 清单；出口 IP 会轮换，勿当成固定基础设施。

## 拓扑一句话（实测）

沙箱 **算力在火山 VPC**；公网可见身份是 **VortexIP 代理落地 IP**（可落在阿里云 ASN）。「火山 vs 阿里」不是矛盾，是计算层与出口层分离。

## 容器内网络（实测）

- 网卡：例如 eth0 为火山 VPC 内网段（9.x）；默认网关走 eth1（`169.254.112.1`，Kata CNI 常见形态）。
- 本机代理组件：tinyproxy `:8118`、gost、`lark_hijack_proxy`；浏览器也走本地 8118。
- GitHub 等可被透明代理到内网镜像 `192.168.255.x`。

## 出口链（实测）

```text
容器内进程 (curl / Chrome)
  → 本地 tinyproxy / gost / hijack
  → VortexIP（vortexip.cn-beijing2.volces.com）
  → 公网落地 IP（当次见 39.96.211.203 等，AS37963）
```

- **NAT**：沙箱无公网地址；多沙箱共享少数出口 IP → 外部限流（如 GitHub API）会「连坐」。
- 不同目标可能走出不同落地 IP（当次另见 `101.47.168.70`）。

## 管控三道闸（实测）

1. **DNS / 路由**：YouTube、Wikipedia、BBC 等解析到黑洞或超时；Google 类不可用。
2. **白名单代理**：GitHub、arxiv、dev.to、Cloudflare 等技术站放行；国内站直连快。
3. **云元数据封禁**：火山 `100.96.0.96`、阿里 `100.100.100.200`、链路本地 `169.254.169.254` 返回 403（防 SSRF 偷凭证的常见加固）。

出网带宽硬上限：**测不到**（应在网关侧）。

## 包管理源（实测）

| 工具 | 显式默认 | 实际路径 |
|------|----------|----------|
| npm | `https://registry.npmmirror.com`（阿里公开镜像） | 经网关到该镜像 |
| pip | `/etc/pip.conf` 指向 `https://pypi.org/simple` | 经 `192.168.255.x` 透明网关 |
| npm 官方域名（手动切回） | `registry.npmjs.org` | 透明代理到 `192.168.255.164` 等 |

响应头显示真实 Cloudflare / Fastly / S3 → **带缓存的透明转发**，不是伪造包内容的假镜像。`no_proxy` / 白名单对包仓库域名友好。

## 证据路径（当次）

出口 IP 查询、DNS 解析对比、`curl -w %{remote_ip}`、代理相关环境变量与进程、npm/pip 配置与响应头。
