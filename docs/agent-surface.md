# Agent 能力面

## 会话双目录（实测）

| 路径 | 角色 |
|------|------|
| `/home/user/Doubao/chats/<chat_id>/` | 用户产物；典型为 `.tmp-tool-results/`（工具大输出，权限常 600） |
| `.doubao/agent_mode/workspace/.sessions/<id>/` | Agent 运行区：`board.md`、`agents/<id>/system/assignment.md`、`trajectory.jsonl` |

两套目录 **id 数字相同、一一对应**。`assignment.md` 按 UTC 追加 `## [RFC3339] 需求`；`trajectory.jsonl` 为 `{"role","content"}` 行协议。

## 三条控制通道（实测，H/I）

| 通道 | 入口 | 技术路径 | 粒度 | 谁可调 |
|------|------|----------|------|--------|
| **browser MCP** | `:8100` → mcp-hub | 自研 `mcp-server-browser` → CDP `:9222` | 页面/DOM：导航、点选、填表、markdown | **模型直调** |
| **CC 面** | `:10000` `/cc/` | `CC*` handlers | Bash/Read/Write/Edit/Glob/Grep/Notebook/Task | 平台签名 |
| **ComputerUse / GUI** | `:10000` 经 nginx `/vm/exec/api/cc` | `ComputerUseExecute` + `ExecGui*` | 桌面键鼠（整桌 X11，不限于浏览器） | 平台签名 |

动作别名见：`MOUSE_DOWN/UP`、`LEFT_DOUBLE`、`RIGHT_CLICK`、`DRAG_TO` 等。  
底层旁证：PyAutoGUI、opencv-headless、Pillow；`mcp_vm_server` 含 Playwright 协议串与 X11 符号。  
**谁在何种产品场景选用哪条通道：容器内未测到调度规则**（推断在平台侧）。

## 浏览器运行时（实测）

- Chrome 146；UA 含 `DoubaoWorkVM`；CDP 9222 **按需**连接。
- 时区默认 `Asia/Singapore`（`/opt/gem/gem_env.sh`）。
- 控制桥：字节自研 `mcp-server-browser`（Apache-2.0 / webpack / `@langchain/core`），直说 CDP；Playwright / puppeteer 预装作备用。
- `browser-supervisor.py`：trusted-stage Chromium 托管与崩溃退避。

## 内置 Sandbox MCP（实测，H）

FastMCP「Sandbox MCP Tools」**v2.14.7**（`app/mcp/`）。经 `POST :8091/mcp` JSON-RPC 实测可调。

| 工具 | 关键参数 | 用途 |
|------|----------|------|
| `sandbox_execute_code` | `code`, `language`(python/javascript), `timeout` | 跑代码 |
| `sandbox_file_operations` | `action`, `path`, … | 统一文件 IO；`/tmp` 与 `/home/$USER` 可读写 |
| `sandbox_str_replace_editor` | 兼容 Anthropic str_replace_editor | 基于 openhands-aci |
| `sandbox_get_context` | 无 | 环境单（镜像版本、端口、工具） |
| `sandbox_get_packages` | `language` | 已装包列表 |
| `sandbox_execute_bash` | `cmd`, `cwd`, `timeout=30`, … | Shell，会话托管 |
| `sandbox_load_skill` | `name`（省略=列清单） | 加载 skill |
| `browser_get_info` | 无 | CDP url / viewport 等 |
| `browser_gui_screenshot` | 无 | **整屏**截图（vs 当前 tab 的 browser_screenshot） |
| `sandbox_convert_to_markdown` | `uri` | 资源转 markdown |

### Hub 与过滤

- 外部 hub 仍主要挂 **browser**（8100，按需，`AUTOSTART_MCP_BROWSER=false`）。
- `--filter-mcp-servers sandbox` 为 **黑名单**；hub 无同名 server → 当前不排除任何 hub 项。
- `/opt/gem/mcp.disabled`：空文件。

### Skills

- `AIO_SKILLS_PATH` 未设时，`sandbox_load_skill` 返回 **Skills Count: 0**。
- 磁盘另有 `/runtime/skills`、`/opt/skills`（大量预装）——**另一套体系，未挂进该 MCP 服务**。

### `sandbox_get_context` 摘要（当次）

镜像 **v1.14.10**、Ubuntu 22.04、多 Python + Node 22、占用端口清单；工具面可见 yt-dlp / nmap / lsyncd 等。

## Security review（实测阴性）

审查文案仅见于会话产物；容器内无策略落点；无法稳定复现拦截 → **未测到容器内策略落点**；拦截位置与判定方式属推断（更可能在容器外执行通道）。
