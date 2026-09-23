# 产品与代码指纹

## 命名（实测）

字符串里出现过技术方案名：《**豆包创作画布 CLI · 云沙箱侧技术方案**》。  
函数名当次为 `super-25-general-agent-efs`。  
路径与变量里反复出现 `agent_mode`，以及内部代号 **AIO**。

## AIO 与多种 CLI 痕迹（实测）

环境变量里有一整族 `AIO_*`，例如运行时目录、家目录隔离开关、CLI 相关目录，以及「CLI skill 是否启用」一类开关（当次为关闭）。  
还能看到与 Codex、OpenCode、code-server 相关的数据目录或配置文件名。  
用户态还出现过 `~/.agents`、`~/.dws` 等目录名。

这些说明：沙箱镜像并不只服务「网页聊天」，还叠了多种编程助手 / 编辑器运行时的痕迹。  
它和 Seed 模型本身如何编排，仍属 **未测到**。

## 内部工程坐标（实测）

从二进制字符串和配置注释里能抠出内部模块路径与服务名，例如：

| 类型 | 例子 |
|------|------|
| Go 模块 | `code.byted.org/flow/mcp_vm_server`、`…/vm_runtime_hook` |
| 配置相关文件名 | `lark_cli_config.go`、`hijack_host_cli.go` |
| TCC 一类 key | `lark_cli_bootstrap:open:v2` |
| 代码托管域名 | `source.byted.org` |
| 平台相关域名 | `certs.doubaocdn.com`、`mcp.doubaocdn.com`、`ext.volces.com` 等 |

## 镜像与预装

「开箱有哪些软件、`IMAGE_VERSION` 是什么意思」已经单独写在 [preinstall.md](preinstall.md)。  
本页只保留命名与内部坐标，避免和预装清单挤在一起。
