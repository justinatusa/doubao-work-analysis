# 07 · 产品与代码指纹（R5）

## 命名与方案（实测）

- 技术方案名字符串：《**豆包创作画布 CLI · 云沙箱侧技术方案**》
- 函数名：`super-25-general-agent-efs`
- 运行区路径含 `agent_mode`

## 内部工程坐标（实测）

| 类型 | 值 |
|------|-----|
| Go 模块 | `code.byted.org/flow/mcp_vm_server`、`code.byted.org/flow/vm_runtime_hook` |
| Go 文件 | `biz/pkg/tcc/lark_cli_config.go`、`biz/pkg/tcc/hijack_host_cli.go` |
| TCC key | `lark_cli_bootstrap:open:v2` |
| 代码托管 | `source.byted.org` |
| 服务名 | `mcp_vm_server`、`mcp_vm_tool` |
| 相关域 | `certs.doubaocdn.com`、`ext.volces.com`、`api5-normal-lq.doubao.com`、`mediakit.cn-beijing.volces.com` |

## 推断（标清）

「创作画布 CLI」+ general-agent FaaS + MCP VM 工具链，更像 **可远程操作的创作/办公 Agent 运行时**，而不仅是聊天附件沙箱。与 **Seed** 模型的粘合方式仍属未决。
