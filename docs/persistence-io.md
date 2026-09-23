# 持久化与文件进出

## 热池与待命（实测）

平台用环境变量 `MCP_VM_STANDBY` 区分两种启动方式：

| 条件 | 行为 |
|------|------|
| 还没有会话 ID | 进入 **standby（热池待命）** |
| 已经分配了会话 ID | 进入业务态（当次看到 `MCP_VM_STANDBY=0`） |

当次实例还带有 `VM_GENERATION=v2`，以及配置档 `MCP_VM_PROFILE=all`。  
配置档合法取值包括：`all`（完整启动）、`ci`（走 CI 专用入口）；其他值会直接报错退出。

### 待命时会先跳过什么

热池待命时，下面这些初始化会先跳过，等真正借给某个会话后再由 post_hook 补跑，例如：

- 官方 npm CLI 安装  
- 持久卷恢复（restore）  
- 用户家目录初始化  
- workspace 初始化、cookie 目录权限  
- shell 代理环境、data 目录权限  
- experience / skills 的冷加载与权限审计  
- lark_cli 相关初始化  

同步脚本 `persistent_sync.sh` 支持 restore、push、pull、post_hook 等模式。配置通过 Base64 环境变量下发。机制上使用 inotify，并限制并发与最小拉取间隔。冷启动时会在后台做 restore。

另外还发现应用内有 `file_watch.py`，用 watchfiles 收集变更。**它是否已经完全替代旧的 shell 同步脚本，仍属推断。**

## 挂载回顾

`/home/user` 走可跨会话的共享存储；根目录 overlay 与 `/tmp/user` 仍随实例销毁。  
`CREATE_SANDBOX_PARAMS` 只有加密形态，**读不出明文**。

## 上传与下载（实测）

浏览器下载目录落在家目录下的 `Downloads`（在持久卷上）。当次写过探针文件：`/home/user/Downloads/probe-upload-test.txt`。

以实际在跑的应用代码为准：

- 上传接口可以显式指定路径；如果不指定，默认落到 **`/tmp/<文件名>`**，而不是旧文档里的 `/home/ubuntu/upload`。  
- 下载接口按路径流式返回；若开启「文件变更则中断」策略，文件被改动时会失败。  
- 旧的「按 URL 批量拉附件」接口，在当次应用包里已经搜不到。

对话框里用户丢进的文件，最终精确落到哪条路径：本会话没有真实附件，**只有接口机制，没有端到端实测**。

## 办公版开关（实测）

当次 `DOUBAO_OFFICE_EDITION=public`。  
和 `internal` 相比，能核实的差异主要在飞书域名劫持的「后缀级清单」是否启用；预装软件与 MCP 工具表未见因该开关而分叉。
