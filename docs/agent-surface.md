# Agent 能力面

> 合并自原 notes/03（运行时浏览器/MCP）与 notes/04（会话目录与内置工具）。

## 会话双目录（实测）

| 路径 | 角色 |
|------|------|
| `/home/user/Doubao/chats/<chat_id>/` | 用户产物；典型只有 `.tmp-tool-results/`（工具大输出，权限常 600） |
| `.doubao/agent_mode/workspace/.sessions/<id>/` | Agent 运行区：`board.md`（任务公告板）、`agents/<id>/system/assignment.md`（按 UTC 追加需求）、`trajectory.jsonl`（role/content 轨迹） |

两套目录 **id 数字相同、一一对应**。

## 内置 MCP（实测，相对「只挂 browser」的修正）

- Hub 外部 server：仍主要是 **browser**（8100，按需）。
- `--filter-mcp-servers sandbox` → `MCP_FILTER_SERVERS=sandbox`，源码注释为 **黑名单**；hub 无名为 `sandbox` 的 server → **当前不排除任何 hub server**。
- `/opt/gem/mcp.disabled`：空文件。
- 另有内置 FastMCP「Sandbox MCP Tools」（`app/mcp/`）：
  - tags=`official`：`sandbox_execute_code`、`sandbox_file_operations`、`sandbox_str_replace_editor`、`sandbox_get_context`、`sandbox_get_packages`、`sandbox_execute_bash`、`sandbox_load_skill`
  - tags=`browser`：`browser_get_info`、`browser_gui_screenshot`

工具完整签名与 skill 清单 → 见后续 H 轮。

## 平台 handler 指纹（实测，strings）

`mcp_vm_server` 能力名（摘录）：`CCListTools` / `CCToolExecute` / `CCHealth`、`CIExec`、`ComputerUseExecute`、`ExecGui*`（Click/Drag/Hotkey/Type/Scroll/FullScreenshot/Wait/WaitDownload）、`FileUpload` / `Download` / `Zip`、`TextEditor(V)`。

→ 存在 **GUI 键鼠 ComputerUse 面**，与浏览器 CDP MCP 可能并列（分流细节待 I）。

---

## 浏览器与 MCP 运行时（补充）

## 桌面与浏览器（实测）

- 桌面：Xvnc（1920×1080）+ Openbox + fcitx5；可通过 websocat 把 VNC 转到 WebSocket（具体对外 URL 形态见后续补证）。
- Chrome 146；UA 含 **`DoubaoWorkVM`**；CDP **9222**；空闲时无客户端常驻连接（按需连）。
- 时区默认：`/opt/gem/gem_env.sh` 中 `TZ="${TZ:-Asia/Singapore}"`（可被外部覆盖）。
- 扩展目录：当次不存在（无扩展）。
- `browser-supervisor.py`：注释称 Minimal trusted-stage Chromium supervisor；崩溃指数退避；提及可写层写爆与 seccomp / `--no-sandbox` 条件。

## 控制桥（实测）

- 主路径：**字节自研** `/usr/local/bin/mcp-server-browser`（链到 Node 22），文件头 Copyright 2025 Bytedance，Apache-2.0，webpack 打包（含 `@langchain/core`）。
- 启动显式：`--cdp-endpoint http://127.0.0.1:9222/json/version` → 直接说 CDP，**不是**当前在用的 Puppeteer/Playwright 驱动。
- 机器另预装 Playwright 1.62（Python）与 puppeteer（`/opt/runtime/nodejs`）作备用，当次无进程占用。

## MCP 能力面（实测）

- Hub 配置：`/opt/gem/mcp-hub.json` → 仅挂 **browser**；streamable-http `http://127.0.0.1:8100/mcp`。
- 默认 `AUTOSTART_MCP_BROWSER=false`（平台按需拉起）。ServerInfo：Web Browser **1.2.29**；工具约 **21** 个（导航/标签、点击前先取可点元素、填表、markdown/text、evaluate、截图、下载列表等）。
- 平台侧：`mcp_vm_server:10000`、`vm_runtime_hook:10080` 对裸 MCP 握手返回 **401 Missing signature headers**。
- `python-server`（8091）为 hub 宿主，带 `--filter-mcp-servers sandbox` → **可能还有未挂给模型的 server**（待补证）。

## Security review（实测结论偏「阴性」）

- 容器内全文检索审查文案：**无落点**；仅出现在会话产物（如 `trajectory.jsonl`、`assignment.md`）。
- 复现实验：多种历史上「挂过」的命令形态当次均过 → **拦截更像在容器外执行通道**；非稳定字符串黑名单。具体策略 **测不到**。

## 飞书 / Lark Hijack（实测）

- 组件：`/hijack_proxy/lark_hijack_proxy` + `config/hijack_domains.conf` + 本地 CA（`CN=MCP Sandbox Root CA`）。
- 精确劫持主机含：feishu / larksuite 的 open、accounts、applink；`meego.larkoffice.com`；`project.feishu.cn`；部分 volces mediakit；`api5-normal-lq.doubao.com`；预发域；`meegle.com` 等。
- `DOUBAO_OFFICE_EDITION=internal` 时另有后缀级劫持清单。
- MITM 成立：`https://open.feishu.cn` 落地 `127.0.0.2`，证书为沙箱 CA；对照百度仍为公网 CA。
- 回源：`HIJACK_PROXY_TARGET_URL=https://mcp.doubaocdn.com/vm/hijack` → **平台代持鉴权**，沙箱不直连真实账号体系。
- 注释提到与平台 Go 配置同步（如 `mcp_vm_tool … lark_cli_config.go` 中 `defaultDomesticHijackDNSHosts`）及热池预签证书以省借出延迟。

## 会话与任务产物（实测线索）

- `/home/user/Doubao/chats/` 下存在跨日期目录 → home 持久化与产品会话有关。
- 任务轨迹类文件名曾出现：`trajectory.jsonl`、`assignment.md`（细节待下一轮列目录取证）。

## 证据路径（当次）

CDP `/json/version`、`ss`、二进制头、`pip list`、MCP JSON-RPC `initialize`/`tools/list`、hijack 配置与 `openssl`、supervisor 状态。
