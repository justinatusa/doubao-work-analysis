# 架构总图

> 基于 2026-09-24 观测拼接；细节见各主题文。

```text
用户浏览器
    │  (外层网关鉴权 / JWT，沙箱内不可见)
    ▼
nginx :8080  ──信任内网──┐
    ├─ /vnc|/ws|/websockify → websocat:6080 → Xvnc:5900
    ├─ /terminal /browser-ui …
    ├─ /json|/devtools → Chrome CDP:9222
    ├─ /mcp → python-server:8091 (MCP hub)
    └─ /v3|/cc|/vm/exec → mcp_vm_server:10000 / hook:10080
                              │
              ┌───────────────┴───────────────┐
              │  Kata microVM + Nydus          │
              │  ByteFaaS / veFaaS 临时实例     │
              │  supervisord (/opt/gem)        │
              └───────────────┬───────────────┘
                              │
         本地代理 tinyproxy/gost/hijack
                              ▼
                    VortexIP 出口网关
                              ▼
                      公网（共享 NAT）
```

## 主组件（索引）

| 层 | 要点 | 详见 |
|----|------|------|
| 计算 | Kata、Nydus、cgroup 2vCPU/4G、hpvs home | [compute.md](compute.md) |
| 网络 | VortexIP、白名单、包源缓存 | [network.md](network.md) |
| Agent | browser MCP + 内置 Sandbox tools、trajectory | [agent-surface.md](agent-surface.md) |
| 暴露 | noVNC、CDP、信任内网 nginx | [desktop-expose.md](desktop-expose.md) |
| 持久化 | standby/cold、upload/download API | [persistence-io.md](persistence-io.md) |
| 产品指纹 | 创作画布 CLI、Go 模块 | [product-fingerprint.md](product-fingerprint.md) |
