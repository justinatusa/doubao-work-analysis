# 桌面与对外暴露

## 信任模型（实测）

沙箱里面的 nginx **没有**配置 `auth_request`、token、jwt、secure_link 这类鉴权指令。它按「已经处在可信内网」来工作。  
环境里能看到 `JWT_PUBLIC_KEY`（内容已打码），说明 **真正验用户身份的地方在沙箱外面的网关**。  

沙箱对外服务端口是 **8080**（环境变量 `PUBLIC_PORT`）。用户浏览器通常不会直连这台 nginx，而是先经过外层网关。

## 链路（实测）

```text
用户
  →（外层网关鉴权）
  → nginx:8080
       ├─ /ws、/websockify  → websocat:6080 → Xvnc:5900
       ├─ /vnc/             → /opt/novnc 静态页面
       ├─ /terminal         → 终端前端
       ├─ /browser-ui 等
       ├─ /json、/devtools  → Chrome CDP:9222
       ├─ /mcp              → MCP hub:8091
       └─ /vm/exec、/v3、/cc → 平台 VM 接口（10000 / 10080）
```

一次性 token、签名 URL、链接多久失效：在 nginx 配置里 **没有找到**（未测到；应在外层网关）。

## 桌面软件（实测）

桌面是 Xvnc（分辨率当次为 1920×1080）加上 Openbox 窗口管理，以及 fcitx5 中文输入。  
Chrome 的 User-Agent 带有 `DoubaoWorkVM`。
