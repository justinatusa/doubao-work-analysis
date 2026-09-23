# 可观测与审计

## 日志（实测）

日志目录是 `/var/log/gem/`。nginx、python-server、gost、browser-supervisor、VNC 等组件各有日志文件。  
这些日志写在当前实例本地可写盘上。**实例回收后，容器里的这份日志就没了。**

## OpenTelemetry（实测）

SDK 没有被关掉，Python 侧也有自动埋点相关配置。  
但是：指向哪里导出的端点变量当次是空的，自动埋点目录在容器里也不存在。  
因此 **日志和指标最终送到哪：未测到**。  
进程列表里也没有看到独立的 otel / jaeger / fluent / prometheus 采集边车。

## 审计（实测）

启动流程里会 best-effort 跑技能权限审计一类钩子。

## 对话轨迹会不会被送出沙箱（未测到）

在容器脚本里没有搜到上传 `trajectory.jsonl` 的逻辑。更可能由平台侧回收，但本仓没有直接证据。
