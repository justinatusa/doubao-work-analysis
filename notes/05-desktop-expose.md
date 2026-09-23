# 05 · 桌面与对外暴露（R5）

## 信任模型（实测）

- 沙箱内 nginx：**无** `auth_request` / token / jwt / secure_link 类指令 → 「信任内网」。
- 环境存在 `JWT_PUBLIC_KEY`（打码）→ **鉴权在沙箱外层网关**。

## 链路（实测）

```text
VNC桌面: 用户 → (外层网关鉴权) → nginx:8080 /ws|/websockify
         → websocat :6080 → Xvnc :5900
         页面 /vnc/ = /opt/novnc
终端:    /terminal（/opt/terminal）；另有 /browser-ui、/secure-browser-ui
CDP:     /json、/devtools/、/cdp/devtools/ → :9222
MCP:     /mcp、/v1/mcp → :8091
VM API:  /vm/exec/api/runtime → :10080；/v3、/cc → :10000（body 上限曾见 10G）
PUBLIC_PORT=8080
```

一次性 token / 签名 URL：**nginx 层测不到**。
