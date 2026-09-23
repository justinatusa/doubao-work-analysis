# 持久化与文件进出

## 热池 / 同步（实测）

- `MCP_VM_STANDBY=1` → `STARTUP_MODE=standby`（不恢复持久卷、不设下载目录）；否则 `cold`。
- 当次：`MCP_VM_STANDBY=0`（cold），`VM_GENERATION=v2`，`MCP_VM_PROFILE=all`。
- `runtime_init/persistent_sync.sh`：模式含 restore/push/pull/run/async_restore_run/post_hook；配置经 `MCP_VM_PERSISTENT_SYNC_CONFIG_B64`；inotify、4 并发、最小 pull 间隔 10s；允许根 `/home/user`。冷启动后台 restore。

## 下载 / 上传 API（实测）

- 下载目录：`BROWSER_DOWNLOAD_DIR_EFFECTIVE=/home/user/Downloads`（持久卷上）。
- FastAPI（`application/python_server.py`）要点：
  - `POST /request-download-attachments`（平台按 URL 拉附件）
  - `GET /file`（≤500MB）、`GET /file/zip`
  - `POST /file/upload_local`、`/file/upload_to_s3`（presigned）、`/zip-and-upload`
- 源码快照曾写旧路径 `/home/ubuntu/upload` → **以实际 app 包为准**。
- 本会话无附件 → 对话框→路径的实测映射仍缺。

## Office 版（实测）

- `DOUBAO_OFFICE_EDITION=public`
- 与 `internal` 的可证差异主要在 hijack **后缀级清单**；预装软件 / MCP 未见 edition 分支。
