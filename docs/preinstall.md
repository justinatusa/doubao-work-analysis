# 沙箱出厂预装（当次观测）

## 先说清楚背景

下面写的是 **2026-09-24** 那次诱导里，Agent 在沙箱内用 `sandbox_get_context`、`dpkg`/`pip` 等查到的结果。  
环境变量里有一项 **`IMAGE_VERSION=1.14.10`**：这是平台给这台沙箱镜像打的版本号，和 `sandbox_get_context` 回报里的 v1.14.10 一致。  
**它不是 Ubuntu 版本，也不是豆包 App 的对外版本号**；只表示「当次拉起的沙箱镜像构建号」。换一天、换函数 revision，列表可能变。

对应证据摘录：[evidence/2026-09-24/01-get-context-redacted.md](../evidence/2026-09-24/01-get-context-redacted.md)。

## 一句话

这台沙箱出厂就接近一台「能写代码、能开桌面浏览器、能装包」的小 Linux 工作站，而不是空容器。

## 规模（当次抽样）

| 类别 | 当次数量级 |
|------|------------|
| deb 系统包 | 约 1275 个 |
| Python pip 包 | 约 285 个 |
| 操作系统 | Ubuntu 22.04 |
| 镜像构建号 | `IMAGE_VERSION=1.14.10` |

## 按用途看「自带什么」

### 语言与运行时

- Python 3.10、3.11、3.12（多解释器并存）
- Node：fnm 管理，可见 20 / 22 / 24；日常以 22 为主
- 另有 Go 相关源码树痕迹（未当主工作流深挖）

### 桌面与浏览器

- Xvnc + Openbox + fcitx5（拼音）
- Chrome / Chromium 146，UA 含 `DoubaoWorkVM`
- noVNC 静态页，方便从浏览器进桌面

### Agent / 自动化相关

- FastMCP / MCP 栈；内置 Sandbox MCP 工具（见 [agent-surface.md](agent-surface.md)）
- PyAutoGUI、Playwright、openhands-aci、opencv-headless、Pillow
- Jupyter 相关组件
- `azure-ai-documentintelligence` 等文档智能依赖（包名级观测）

### 开发与系统工具

- git、gh、uv、tmux
- ffmpeg、ImageMagick
- rsync、lsyncd
- nmap、netcat 等网络探测工具（上下文里曾点名）

### 网络与平台组件

- nginx、gost、tinyproxy、`lark_hijack_proxy`
- ByteFaaS / gem 运行时目录下的 supervisord、browser-supervisor 等（平台注入，不算「给你用的应用软件」，但是镜像的一部分）

### Skills 目录（重要限制）

磁盘上能看到 `/runtime/skills`、`/opt/skills` 等预装 skill 树，但当次 `AIO_SKILLS_PATH` 未设置时，MCP 的 `sandbox_load_skill` 回报 **Skills Count: 0**。  
也就是说：**镜像里可能有 skill 文件，不等于当前会话已经挂给模型用。**

## 还没逐项列清的

- 完整 deb/pip 清单（只有数量级与大类，没有全量表）
- npm 全局包完整列表
- `/opt/skills` 里每一个 skill 的名字与用途

若你需要「可检索的全量包名表」，要再开一轮诱导，让 Agent 导出打码后的 `dpkg -l` / `pip freeze` 摘要入库。对本仓 teardown 目标，大类摘要通常够用。
