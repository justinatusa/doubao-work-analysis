# 持久化与文件进出

## 热池 / standby（实测，N）

| 条件 | 行为 |
|------|------|
| `SESSION_ID` 为空 | `MCP_VM_STANDBY=1` → **standby**（热池待命） |
| 有 `SESSION_ID`（借出） | `MCP_VM_STANDBY=0` → **cold/业务态** |

当次实例：`MCP_VM_STANDBY=0`，`VM_GENERATION=v2`，`MCP_VM_PROFILE=all`。

**PROFILE**（entrypoint）：`all`（默认完整）、`ci`（`exec entrypoint_ci.sh`）、其他值报错退出。

### standby 跳过（deferred to post-hook）

官方 npm CLI 安装、持久卷 restore、`init_user_home`、workspace-init、cookie 确权、shell http proxy、data 目录权限、experience 冷加载、skills 冷同步与权限审计、lark_cli 初始化/重建等。  
借出后由 **post_hook** 补跑（`persistent_sync.sh` 支持 `post_hook`：restore 一次、不写 runner pid）。

### 同步机制

- `runtime_init/persistent_sync.sh`：restore/push/pull/run/async_restore_run/post_hook；配置 `MCP_VM_PERSISTENT_SYNC_CONFIG_B64`；inotify、4 并发、最小 pull 10s；根允许 `/home/user`。
- 新发现 `app/services/file_watch.py`：watchfiles 批量收集变更并持久化（**疑似**新实现，推断）。

## 挂载回顾（实测）

| 点 | 类型 | 性质 |
|----|------|------|
| `/home/user` | hpvs_fs | 跨会话 |
| `/sandboxdata/*` | virtiofs | 持久 |
| `/` overlay、`/tmp/user` vdb | 本地 | 随实例销毁 |

`CREATE_SANDBOX_PARAMS=ENCv1|…`：**无明文**。

## 上传 / 下载（实测，M）

- 下载目录：`BROWSER_DOWNLOAD_DIR_EFFECTIVE=/home/user/Downloads`（持久卷）。
- 探针已写：`/home/user/Downloads/probe-upload-test.txt`。
- 实际 app 包：
  - `POST …/upload`：可显式 `path`；默认 **`/tmp/<filename>`**（不是旧 `/home/ubuntu/upload`）。
  - `GET …/download`：按 path 流式；`change_policy=abort` → 变更则 409。
  - 旧 `request-download-attachments`：**当前包中 grep 不到**（已不存在/未启用）。
- 另见（较早包描述）：`upload_local` / `upload_to_s3` / `zip-and-upload` 等——以当次 app 包路由为准。

## Office 版（实测）

`DOUBAO_OFFICE_EDITION=public`。与 `internal` 的可证差异主要在 hijack **后缀级清单**；预装 / MCP 未见 edition 分支。
