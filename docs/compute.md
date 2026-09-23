# 计算与沙箱

## 身份与平台（实测）

- 产品对话侧自称「豆包」；执行环境为临时 Linux 沙箱。
- 主机名形态：`vefaas-…-sandbox`；PID1 链路最终进 ByteFaaS 运行时。
- 进程树（归纳）：

```text
dumb-init (PID1)
  └─ runtime-agent /opt/bytefaas/run.sh
       └─ /runtime/mcp_vm_server/entrypoint.sh
            └─ supervisord (/opt/gem/supervisord.conf → include /opt/gem/supervisord/*.conf)
                 └─ nginx / Chrome / MCP / VNC …
```

- 对外品牌对应：**火山引擎 veFaaS / ByteFaaS**。
- 函数侧标识（当次）：`_FAAS_FUNC_NAME=super-25-general-agent-efs`，`_FAAS_REVISION_NUMBER=4`，另有 `_FAAS_FUNC_ID`、加密块 `CREATE_SANDBOX_PARAMS=ENCv1|…`。

## 隔离与镜像（实测）

- 根挂载线索：`lowerdir=/run/kata-containers/sandbox/nydus/…` → **Kata Containers** microVM + **Nydus** 按需加载。
- 根文件系统：overlay（约 10G 可写层，实例销毁即没）。
- **推断**：相对普通 Docker 进程隔离，Kata microVM 是为多租户 Agent 沙箱加强边界。

## 规格与配额（实测）

| 资源 | 观测 |
|------|------|
| CPU | 2 vCPU；型号 Intel Xeon Platinum 8457C；cgroup v2 `cpu.max = 200000 100000`；`_FAAS_INSTANCE_VCPU=2000` |
| 内存 | ~3.9–4 GiB；`memory.max = 4294967296`；无 swap；`_FAAS_INSTANCE_MEMORY=4096` |
| 进程 / IO | `pids.max` / `io.max` 未见硬限 |
| ulimit | nofile 实际约 2048（脚本曾试图抬到 20480）；stack 8MB；core 0 |
| 并发相关 | `MAX_CONCURRENCY=1000`（FaaS 侧变量；不等于单沙箱无限开浏览器） |

超内存会被 cgroup OOM killer；CPU 过量是 throttle。supervisor 注释提到 Chrome crash-loop 可能高速写爆可写层。

## 挂载与持久化（实测）

| 挂载点 | 类型 | 性质 |
|--------|------|------|
| `/` | overlay on vda ~10G | 实例本地可写，销毁即没 |
| `/tmp/user` | ext4 on vdb ~10G | 本实例临时盘 |
| `/home/user` | hpvs_fs（共享池，后端量级曾显示约 10P） | **跨会话持久**；见 `Doubao/chats/` 跨日期目录 |
| `/sandboxdata/workspace`、`/sandboxdata/data` | virtiofs | 持久卷（当次几乎为空） |
| browser `…/Default/customCookie` | virtiofs | Cookie 持久化 |
| `/opt/tiger/bytefaas/binary` | virtiofs ro | 平台二进制只读注入 |

## 入口与超时（实测）

- 平台流量入口：nginx **8080**（`_BYTEFAAS_RUNTIME_PORT=8080`），配置在 `/opt/gem/nginx*.conf`；支持 `<port>-<host>` 反代到本机端口。
- 超时类变量：`_FAAS_FUNC_TIMEOUT=315`、`WAIT_TIMEOUT=60`、`SANDBOX_SHUTDOWN_HOOKS_TIMEOUT=30`、`_BYTEFAAS_FAST_SHUTDOWN=True`。
- **关对话后的 idle 回收 TTL：测不到**（环境变量无对应字段）。

## 证据路径（当次）

`ps`、`mount`、`lsblk`、cgroup 文件、`/opt/gem/supervisord*.conf`、`/opt/gem/nginx*.conf`、相关环境变量。
