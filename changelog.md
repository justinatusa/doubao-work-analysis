# Changelog（观测日志）

详细结论写在主文与附录；这里只记「哪天补了什么」。

## 2026-09-24

- 初建；方法定为沙箱内现场取证。
- 计算层：ByteFaaS/veFaaS、Kata+Nydus、~2vCPU/4GiB、hpvs home。
- 网络层：VortexIP、共享 NAT、DNS/白名单、包源透明缓存。
- Agent/桌面：自研 CDP browser MCP、noVNC、飞书 hijack。
- 补全：双会话目录、standby/cold、Sandbox MCP 工具表与真实调用、三控制通道、AIO/多 CLI、可观测空洞、上传默认 `/tmp`、PROFILE=`all|ci`。
- 补 `evidence/2026-09-24` 打码摘要；收紧部分措辞强度。
- 新增预装与 `IMAGE_VERSION` 人话说明；文风改为完整中文句；架构图改为仓内 SVG。
- **结构重排：** 原 12 篇薄主题文合并为通读主文 [`docs/sandbox-outside-in.md`](docs/sandbox-outside-in.md)；软件包与证据/对照迁入附录；README 缩短为入口；删除 `publish/` 与旧分篇空壳。R6 软件清单（versions / Python / pip-3.12 全表 / npm 空 / `/opt` 体积 / deb 前半约 953）并入附录；deb 后半未导出，正文如实标注不完整。
- 按 humanizer-zh（技术文档模式）+ qu-ai-wei（保事实结构重写）+ stop-slop/deslop 可迁移规则润色主文：加节间转接、砍起跑式铺垫与口号收尾、保留全部路径/版本/口径标注；不用人设/小红书腔。
- 吸收博客工坊去 AI 味审阅：去掉假对比/口语拔高/「R6」轮次黑话；正文口径只留实测·推断·未测到。

