# Agent 能力面

## 会话用两套目录（实测）

用户侧产物和 Agent 内部工作区是两套目录。两边的会话数字 ID 一致，可以一一对应。

| 路径 | 做什么用 |
|------|----------|
| `/home/user/Doubao/chats/<chat_id>/` | 用户侧产物。常见子目录是 `.tmp-tool-results/`，用来放大体积的工具输出（权限常为仅所有者可读） |
| `/home/user/.doubao/agent_mode/workspace/.sessions/<id>/` | Agent 运行区。里面有任务板 `board.md`、按时间追加的需求单 `assignment.md`，以及整段对话轨迹 `trajectory.jsonl` |

`assignment.md` 会按 UTC 时间追加「需求」小节。  
`trajectory.jsonl` 每一行大致是带 `role` 与 `content` 字段的 JSON。

## 三条控制通道（实测）

**MCP（Model Context Protocol）** 是模型调用外部工具的一种接口。本沙箱用它把浏览器等能力挂给模型；另外还有一套用 **FastMCP** 实现的「Sandbox MCP Tools」。

沙箱里至少能分清三条「动手」的路：

| 通道 | 入口 | 技术路径 | 能做什么 | 谁可以调用 |
|------|------|----------|----------|------------|
| 浏览器 MCP | 本机 8100 端口，再进 MCP hub | 字节自研的 `mcp-server-browser`，连到 Chrome 的 CDP（9222 端口） | 打开网页、点选、填表、取正文 | **模型可以直接调** |
| **CC 面** | 本机 10000 端口的 `/cc/` | 平台签名的代码/文件操控 API；容器内 handler 名称常带 `CC` 前缀 | 跑命令、读写文件、搜索文件等 | 需要平台签名 |
| ComputerUse / GUI | 同样到 10000，经 nginx 的 `/vm/exec/api/cc` | `ComputerUseExecute` 与一组 GUI 动作 | 控制整个桌面的键鼠，不限于浏览器 | 需要平台签名 |

**CC** 在这里指「平台签名的代码/文件操控通道」，不是桌面键鼠（那是 ComputerUse）。读者不必把它猜成 Claude Code 或别的产品名；本仓只按容器内看到的接口前缀记述。

旁证包括：Python 环境里有 PyAutoGUI 等库；平台二进制里能搜到 Playwright 协议字符串和 X11 相关符号。  
**哪种产品场景必须走哪一条通道：容器内没有读到调度规则（未测到；推断在平台侧）。**

## 浏览器运行时（实测）

- Chrome 大版本当次为 146；User-Agent 里带有 `DoubaoWorkVM`。  
- CDP 开在 9222 端口，空闲时不一定有客户端连着，属于按需连接。  
- 时区默认写成新加坡（`Asia/Singapore`），来自 gem 环境脚本，可被外部覆盖。  
- 主控制桥是字节自研的 `mcp-server-browser`：直接说 CDP 协议。机器上也预装了 Playwright / Puppeteer，当次没有看到它们在主路径上跑。  
- 另有 `browser-supervisor.py` 负责在容器生命周期里托管 Chrome，并处理崩溃重试。

## 内置 Sandbox MCP（实测）

除了挂给模型的 browser 服务，应用里还有一套用 **FastMCP**（MCP 的一种实现框架）挂载的工具，对外名称类似「Sandbox MCP Tools」，当次版本号为 2.14.7。  
可以通过本机 8091 端口的 MCP HTTP 接口真实调用。

| 工具名 | 主要参数 | 用途 |
|--------|----------|------|
| `sandbox_execute_code` | 代码、语言（Python/JS）、超时 | 跑代码 |
| `sandbox_file_operations` | 动作、路径、内容等 | 统一文件读写；`/tmp` 与用户家目录可写 |
| `sandbox_str_replace_editor` | 与常见 str_replace_editor 兼容 | 精细改文件 |
| `sandbox_get_context` | 无 | 返回环境摘要（含镜像版本、端口等） |
| `sandbox_get_packages` | 语言 | 列出已安装包 |
| `sandbox_execute_bash` | 命令、工作目录、超时等 | 执行 shell |
| `sandbox_load_skill` | 名称；省略则列清单 | 加载 skill |
| `browser_get_info` | 无 | 浏览器 / CDP 信息 |
| `browser_gui_screenshot` | 无 | **整屏**截图（和「只截当前标签页」不是同一个工具） |
| `sandbox_convert_to_markdown` | 资源地址 | 把网页或文件转成 markdown |

### Hub 与过滤

- 外部 hub 里主要挂的是 **browser**（8100 端口，默认不自动启动，用时再拉起）。  
- 启动参数里的 `--filter-mcp-servers sandbox` 表示黑名单。当前 hub 上并没有名叫 `sandbox` 的服务，所以这条过滤实际上没有去掉任何已挂载项。  
- `/opt/gem/mcp.disabled` 当次是空文件。

### Skills

- skill 扫描根目录由环境变量 `AIO_SKILLS_PATH` 决定。当次未设置时，调用 `sandbox_load_skill` 得到的 skills 数量是 **0**。  
- 磁盘上另外看得到 `/runtime/skills`、`/opt/skills` 等目录，里面有大量预装 skill 文件。那是另一套体系，**没有挂进当前这个 MCP 服务**。

`sandbox_get_context` 的摘要与预装大类，见 [preinstall.md](preinstall.md) 与 [evidence/2026-09-24/01-get-context-redacted.md](../evidence/2026-09-24/01-get-context-redacted.md)。

## 关于「Security review」（实测偏阴性）

对话产物里出现过类似 **security review** 的审查类提示文案（产品对某次操作给出的安全审查反馈）。  
在沙箱文件系统里搜过对应策略文件或本地策略服务，**没有找到落点**。  
用多种「历史上像会挂」的命令写法复测时，当次反而都通过了，因此无法稳定复现拦截。更稳妥的结论是：**未测到容器内的策略落点**；真正拦在哪一层、按什么规则拦，推断更可能在容器外的执行通道上。

## 证据从哪来

CDP 版本接口、端口监听、二进制文件头、Python 包列表、MCP 的 initialize / tools/list / tools/call，以及会话目录列表。
