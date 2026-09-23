# 沙箱出厂预装（当次观测）

## 背景先说清楚

下面写的是 **2026-09-24** 那次取证里，Agent 用 `sandbox_get_context`、包装管理命令等查到的结果。

环境变量里的 **`IMAGE_VERSION=1.14.10`**，是平台给这台沙箱镜像打的 **构建号**。  
它和 `sandbox_get_context` 回报里的版本一致。  
**它不是 Ubuntu 版本，也不是豆包客户端 / App 的对外版本。** 换一天或换函数修订，预装列表可能变。

证据摘要：[evidence/2026-09-24/01-get-context-redacted.md](../evidence/2026-09-24/01-get-context-redacted.md)。

## 一句话

镜像里预装了语言运行时、桌面、浏览器自动化，以及一批开发与网络工具，方便 Agent 开箱就能干活。  
这台环境更接近「小 Linux 工作站」，而不是空容器。

## 你怎么自己核对

在沙箱里可以让 Agent 调用：

- `sandbox_get_context`：环境与版本摘要  
- `sandbox_get_packages`：已装 Python / Node 包列表  

## 当次规模

| 类别 | 数量级 |
|------|--------|
| deb 系统包 | 约 1275 个 |
| Python pip 包 | 约 285 个 |
| 操作系统 | Ubuntu 22.04 |
| 镜像构建号 | `IMAGE_VERSION=1.14.10` |

## 按用途看自带什么

### 语言与运行时

- Python 3.10、3.11、3.12  
- Node：可见 20 / 22 / 24（经 fnm 管理），日常以 22 为主  
- 另有 Go 相关痕迹（未当主线深挖）

### 桌面与浏览器

- Xvnc、Openbox、fcitx5（拼音）  
- Chrome 146，User-Agent 含 `DoubaoWorkVM`  
- noVNC，便于从浏览器进入桌面

### Agent 与自动化

- FastMCP / MCP；内置 Sandbox 工具（见 [agent-surface.md](agent-surface.md)）  
- PyAutoGUI、Playwright、openhands-aci、opencv-headless、Pillow  
- Jupyter 相关组件  
- 名称里带文档智能的依赖包（包名级观测）

### 开发与系统工具

- git、gh、uv、tmux  
- ffmpeg、ImageMagick  
- rsync、lsyncd  
- nmap、netcat 等

### 网络与平台组件

- nginx、gost、tinyproxy、`lark_hijack_proxy`  
- ByteFaaS / gem 运行时里的 supervisord、browser-supervisor 等（平台注入，不完全是「给你用的应用」，但是镜像的一部分）

### Skills 目录（重要限制）

磁盘上能看到 `/runtime/skills`、`/opt/skills` 等预装 skill 树。  
但当次未设置 `AIO_SKILLS_PATH` 时，`sandbox_load_skill` 回报的 skills 数量是 **0**。  
**镜像里有 skill 文件，不等于当前会话已经挂给模型用。**

## 还没有逐项列清的

- 完整 deb / pip 包名表  
- npm 全局包完整列表  
- `/opt/skills` 里每一个 skill 的名称与用途  

若需要可检索的全量表，要再导出打码后的包列表入库。对本仓拆解目标，大类摘要通常已经够用。
