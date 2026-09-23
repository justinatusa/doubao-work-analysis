# 计算与沙箱

## 身份与平台（实测）

对话里的模型自称「豆包」。真正执行命令的地方，是一台临时分配的 Linux 沙箱。

主机名长得像 `vefaas-…-sandbox`。从 1 号进程往下看，最终会进入火山 **ByteFaaS / veFaaS** 的运行脚本。这说明这台「云电脑」挂在函数算力上，而不是一台长期租给你的个人 VPS。

进程树可以概括成：

```text
dumb-init（1 号进程）
  └─ runtime-agent  /opt/bytefaas/run.sh
       └─ /runtime/mcp_vm_server/entrypoint.sh
            └─ supervisord（配置在 /opt/gem/）
                 └─ nginx、Chrome、MCP、VNC 等服务
```

当次还能看到这些函数侧标识（敏感值已省略）：

- 函数名：`super-25-general-agent-efs`
- 修订号：`_FAAS_REVISION_NUMBER=4`
- 另有函数 ID，以及加密块 `CREATE_SANDBOX_PARAMS=ENCv1|…`（容器内解不开明文）

## 隔离与镜像（实测）

根文件系统的挂载信息里出现过 `kata-containers` 与 `nydus` 字样。据此可以判断：隔离形态是 **Kata Containers** 微虚拟机，镜像层用 **Nydus** 做按需加载。

根目录是大约 10GB 的 overlay 可写层。实例销毁后，这一层上的内容会一起消失。

**推断：** 相对普通 Docker 进程隔离，Kata 微虚拟机更适合多租户 Agent 沙箱。

## 规格与配额（实测）

| 资源 | 当次观测 |
|------|----------|
| CPU | 2 个虚拟核；型号线索为 Intel Xeon Platinum 8457C；cgroup 把 CPU 硬限制在 2 核 |
| 内存 | 大约 4 GiB 硬上限；没有 swap |
| 进程数 / 磁盘 IO | 未看到对应的硬限制 |
| 文件句柄等 | `nofile` 实际大约 2048 |
| 并发相关变量 | 出现过 `MAX_CONCURRENCY=1000`（这是 FaaS 侧变量，不等于浏览器可以无限开标签） |

内存超过上限会被 cgroup 直接杀掉进程；CPU 超限通常是被限流，而不是立刻杀进程。supervisor 相关注释里提到：Chrome 若陷入崩溃重试，有可能很快写满可写层。

## 挂载与持久化（实测）

| 挂载点 | 类型 | 含义 |
|--------|------|------|
| `/` | overlay，约 10GB | 本实例本地可写，销毁即没 |
| `/tmp/user` | 独立磁盘上的 ext4，约 10GB | 本实例临时盘 |
| `/home/user` | hpvs 共享存储 | **可以跨会话保留**；下面有 `Doubao/chats/` 等目录 |
| `/sandboxdata/…` | virtiofs | 持久卷（当次几乎是空的） |
| 浏览器 Cookie 相关路径 | virtiofs | Cookie 可持久 |
| `/opt/tiger/bytefaas/binary` | 只读 virtiofs | 平台注入的二进制 |

## 入口与超时（实测）

平台流量进入沙箱后，先到监听 **8080** 的 nginx。配置目录在 `/opt/gem/nginx*.conf`。  
还存在「把某个端口反代到本机」的写法。

超时相关环境变量当次见过：单次函数执行约 315 秒、等待 60 秒、关闭钩子 30 秒，以及快速关闭开关。  
**用户关掉对话之后，实例究竟闲置多久会被回收：容器内没有找到对应字段（未测到）。**

## 镜像版本（实测）

沙箱会通过环境变量 `IMAGE_VERSION` 报告自己的镜像构建号；当次是 **1.14.10**。  
另外还有 `BUILD_IMAGE_DIR_PREFIX=./docker_build` 这类构建目录线索。

引用本仓时请带上：观测日 `2026-09-24` 与 `IMAGE_VERSION=1.14.10`。  
出厂预装了哪些软件，见 [preinstall.md](preinstall.md)。

## 证据从哪来

当次使用了进程查看、`mount` / `lsblk`、cgroup 文件、`/opt/gem` 下的 supervisord 与 nginx 配置，以及相关环境变量。
