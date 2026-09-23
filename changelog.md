# Changelog（观测日志）

详细结论写在 `docs/`；这里只记「哪天补了什么」。

## 2026-09-24

- 初建；方法定为沙箱内现场取证。
- 计算层：ByteFaaS/veFaaS、Kata+Nydus、~2vCPU/4GiB、hpvs home。
- 网络层：VortexIP、共享 NAT、DNS/白名单、包源透明缓存。
- Agent/桌面：自研 CDP browser MCP、noVNC、飞书 hijack MITM。
- R5（A–G）：双会话目录、standby/cold、内置 Sandbox MCP 线索、创作画布 CLI、Go 模块指纹。
- SoT 改为 Obsidian 式 `docs/` + `changelog` + `publish/`。
- **R6（H–N）**：Sandbox 工具全表与真实调用；三控制通道；AIO/多 CLI；可观测空洞；镜像 v1.14.10 与预装摘要；上传默认 `/tmp`；standby 跳过项与 PROFILE=`all|ci`。
- 按调研评审：补 `docs/comparables.md`、`evidence/2026-09-24` 打码摘要；收紧部分措辞强度。
- 新增 `docs/preinstall.md`；README 补「观测背景」，把 `IMAGE_VERSION` 说成人话。
