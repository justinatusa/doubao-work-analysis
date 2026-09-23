# nginx location 摘要（重构）

对应：[docs/desktop-expose.md](../../docs/desktop-expose.md)

```text
listen PUBLIC_PORT=8080
# no auth_request / jwt / secure_link in-sandbox (trust internal)

/ws, /websockify  -> websocat :6080 -> Xvnc :5900
/vnc/             -> /opt/novnc
/terminal         -> /opt/terminal
/browser-ui, /secure-browser-ui
/json, /devtools, /cdp/devtools/ -> 127.0.0.1:9222
/mcp, /v1/mcp     -> 127.0.0.1:8091
/vm/exec/api/runtime -> :10080
/v3, /cc          -> :10000
```

外层网关 JWT / 一次性 URL：**容器内未测到**。
