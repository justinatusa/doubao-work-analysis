# sandbox_get_context（重构摘要）

对应：[docs/agent-surface.md](../../docs/agent-surface.md)、[docs/compute.md](../../docs/compute.md)

```text
IMAGE_VERSION: 1.14.10
OS: Ubuntu 22.04.x
Python: 3.10 / 3.11 / 3.12（多解释器）
Node: 22（另有 fnm 管理的 20/24 痕迹）
Notable tools (examples): yt-dlp, nmap, lsyncd, …
Listening ports: (see session; includes 8080/8091/9222 patterns)
```

调用方式（会话内）：经 `POST 127.0.0.1:8091/mcp` JSON-RPC `tools/call` → `sandbox_get_context`。
