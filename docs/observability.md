# 可观测与审计

## 日志（实测，K）

- `LOG_DIR=/var/log/gem/`：nginx-access、python-server、gost、browser-supervisor、tigervnc 等。
- 落在本实例可写层 → **实例销毁即没**。

## OpenTelemetry（实测，K）

- `OTEL_SDK_DISABLED=false`；Python 自动埋点（`OTEL_PYTHON_DISABLED_INSTRUMENTATIONS=redis`）。
- OTLP 导出端点环境变量 **为空**；`/otel-auto-instrumentation-python` **不存在** → 导出目标 **测不到**。
- 无 otel/jaeger/fluent/prom **独立 sidecar** 进程。

## 审计（实测）

- `vm_runtime_hook audit-skill-permissions`（entrypoint 中 best-effort 后台）。

## trajectory 出沙箱（未测到）

容器内脚本未见上传 `trajectory.jsonl` 的逻辑 → **回收应在平台侧**。
