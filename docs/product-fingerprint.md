# 产品与代码指纹

## 命名（实测）

- 技术方案字符串：《**豆包创作画布 CLI · 云沙箱侧技术方案**》
- 函数名：`super-25-general-agent-efs`
- 路径含 `agent_mode`；内部代号 **AIO**

## AIO / 多 CLI（实测，J）

环境变量族 `AIO_*` 示例：

- `AIO_RUNTIME_DIR=/runtime/aio`
- `AIO_HOME_ISOLATION_ENABLED=true`
- `AIO_CLI_BIN_DIR`、`AIO_CLI_SKILL_ENABLED=false`
- Codex：`AIO_CODEX_CONFIG_FILE=aio-config.toml`、`model-catalog.json`、DATA_DIR
- OpenCode：`AIO_OPENCODE_DATA_DIR`
- code-server：extensions / user-data 目录

用户态目录：`/runtime/user_skills`、`~/.agents`、`~/.dws`、`~/.config`。

## 内部工程坐标（实测）

| 类型 | 值 |
|------|-----|
| Go 模块 | `code.byted.org/flow/mcp_vm_server`、`code.byted.org/flow/vm_runtime_hook` |
| Go 文件 | `biz/pkg/tcc/lark_cli_config.go`、`biz/pkg/tcc/hijack_host_cli.go` |
| TCC key | `lark_cli_bootstrap:open:v2` |
| 代码托管 | `source.byted.org` |
| 服务 | `mcp_vm_server`、`mcp_vm_tool` |
| 域 | `certs.doubaocdn.com`、`ext.volces.com`、`api5-normal-lq.doubao.com`、`mediakit.cn-beijing.volces.com`、`mcp.doubaocdn.com` |

## 镜像与预装

完整「出厂带什么」说明已单列为 [`preinstall.md`](preinstall.md)。下面保留指纹级摘要。

## 镜像供应链摘要（实测，L）

- `IMAGE_VERSION=1.14.10`（与 `sandbox_get_context` 一致）
- `BUILD_IMAGE_DIR_PREFIX=./docker_build`
- 规模当次：约 **1275** deb、**285** pip
- 大类：多 Python（3.10–3.12）、fnm Node 20/22/24、桌面栈、fastmcp/mcp、PyAutoGUI/playwright/openhands-aci、jupyter、azure-ai-documentintelligence、ffmpeg/imagemagick、git/gh/uv、nmap、nginx/gost/tinyproxy/hijack

## 推断（标清）

「创作画布 CLI」+ AIO + general-agent FaaS，更像可远程操作的创作/办公 Agent 运行时。与 **Seed** 模型的编排粘合方式仍属未决。
