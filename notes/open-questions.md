# 未决问题

按优先级大致排序；补证后把条目迁到对应 notes，并在此划掉。

## 平台与生命周期

1. 用户关闭对话后，实例 **idle 回收 TTL** 是多少？（环境未下发字段）
2. 热池预热 / 借出 / 归还的完整 hook 与环境变量集
3. `CREATE_SANDBOX_PARAMS` 明文元数据是否在旁路可读
4. `super-25-general-agent-efs` 命名中 efs / hpvs 与存储产品的对应关系

## 安全与策略

5. Security review 的规则服务位置与判定特征（容器内零落点）
6. 出网带宽、并发连接硬限（网关侧）
7. 多租户之间除 Kata 外还有哪些隔离与审计

## Agent / 产品形态

8. `--filter-mcp-servers sandbox` 过滤掉了哪些 server
9. 用户上传文件 → 容器内路径的完整映射；下载回传链路
10. nginx port-proxy + VNC/websocat 对用户浏览器的完整暴露与鉴权（token / 签名 URL / TTL）
11. `DOUBAO_OFFICE_EDITION` 取值与企业版能力差异
12. **Seed** 模型与 Work 产品壳、本 FaaS 镜像的粘合方式（编排、提示、工具策略）——目前只有沙箱层，缺产品架构层

## 供应链与镜像

13. 沙箱镜像构建流水线、基线包列表、更新节奏
14. Nydus 快照 / 层缓存是否跨租户共享及失效策略

## 可观测性

15. 日志 / trace 如何离开沙箱；用户是否可见；平台侧 retention
