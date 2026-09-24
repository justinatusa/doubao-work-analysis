# MCP tools（重构摘要）

对应：[docs/agent-surface.md](../../docs/sandbox-outside-in.md)

```text
# Hub external
browser @ http://127.0.0.1:8100/mcp   # on-demand; Web Browser 1.2.29; ~21 tools

# Built-in FastMCP "Sandbox MCP Tools" v2.14.7 (app/mcp/)
sandbox_execute_code
sandbox_file_operations
sandbox_str_replace_editor
sandbox_get_context
sandbox_get_packages
sandbox_execute_bash
sandbox_load_skill          # Skills Count: 0 when AIO_SKILLS_PATH unset
browser_get_info
browser_gui_screenshot
sandbox_convert_to_markdown

# Platform (signed; not model-naked)
mcp_vm_server :10000
vm_runtime_hook :10080
```
