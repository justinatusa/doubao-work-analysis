# mount / cgroup（重构摘要）

对应：[docs/compute.md](../../docs/compute.md)、[docs/persistence-io.md](../../docs/persistence-io.md)

```text
# mounts (selected)
/          overlay on vda ~10G
/tmp/user  ext4 on vdb ~10G
/home/user hpvs_fs          # cross-session
/sandboxdata/...  virtiofs
.../browser/.../customCookie  virtiofs
/opt/tiger/bytefaas/binary    virtiofs ro

# cgroup v2 (selected)
cpu.max:    200000 100000     # 2 vCPU
memory.max: 4294967296        # 4 GiB
swap:       none observed

# env (selected, redacted)
_FAAS_INSTANCE_VCPU=2000
_FAAS_INSTANCE_MEMORY=4096
_FAAS_FUNC_NAME=super-25-general-agent-efs
_FAAS_FUNC_TIMEOUT=315
MCP_VM_STANDBY=0
VM_GENERATION=v2
MCP_VM_PROFILE=all
```
