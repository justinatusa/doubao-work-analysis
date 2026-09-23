# 桌面与对外暴露

## 信任模型（实测）

- 沙箱内 nginx：**无** `auth_request` / token / jwt / secure_link → 「信任内网」。
- 环境有 `JWT_PUBLIC_KEY`（打码）→ **鉴权在沙箱外层网关**。
- `PUBLIC_PORT=8080`。

## 链路（实测）

```text
用户 → (外层网关鉴权) → nginx:8080
  ├─ /ws | /websockify → websocat:6080 → Xvnc:5900
  ├─ /vnc/            → /opt/novnc 静态
  ├─ /terminal        → /opt/terminal
  ├─ /browser-ui | /secure-browser-ui
  ├─ /json | /devtools | /cdp/devtools/ → Chrome:9222
  ├─ /mcp | /v1/mcp   → python-server:8091
  └─ /vm/exec/api/runtime → :10080
      /v3 | /cc       → :10000（client_max_body_size 曾见 10G）
```

一次性 token / 签名 URL / TTL：**nginx 层测不到**（外层网关）。

## 桌面栈（实测）

Xvnc 1920×1080 + Openbox + fcitx5（拼音）；Chrome UA `DoubaoWorkVM`。
