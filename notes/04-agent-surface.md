# 04 · Agent 能力面（R5 起）

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
