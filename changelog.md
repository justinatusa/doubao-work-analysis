# Changelog（观测日志）

按时间追加；详细结论写在 `docs/`，这里只记「哪天补了什么」。

## 2026-09-24

- 初建仓库；方法定为沙箱内现场取证（问运行中的 Agent 勘察）。
- 坐实计算层：ByteFaaS/veFaaS、Kata+Nydus、约 2vCPU/4GiB、hpvs 持久 home。
- 坐实网络层：VortexIP 出口、共享 NAT、DNS/白名单分流、包源透明缓存。
- 坐实 Agent/桌面：自研 CDP browser MCP、noVNC 链路、飞书 hijack MITM。
- R5：双会话目录、standby/cold、内置 Sandbox MCP、创作画布 CLI 方案名、Go 模块指纹。
- SoT 目录改为 Obsidian 式：`docs/` + `changelog.md` + `publish/` 占位。
