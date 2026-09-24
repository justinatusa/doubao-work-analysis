# lark_hijack 域名样例（重构）

对应：[docs/network.md](../../docs/sandbox-outside-in.md)、[docs/product-fingerprint.md](../../docs/sandbox-outside-in.md)

说明：这是 **本机透明劫持 / 本地 CA** 的观测（组件 `lark_hijack_proxy`），用于说明流量如何被沙箱侧接管；**不是**教你对外实施中间人攻击。

```text
# exact hosts (examples from DEFAULT_HIJACK_DNS_HOSTS family)
open.feishu.cn / accounts.feishu.cn / applink.feishu.cn
open.larksuite.com / accounts.larksuite.com / …
meego.larkoffice.com
project.feishu.cn
api5-normal-lq.doubao.com
mediakit.cn-beijing.volces.com
# + pre / meegle variants

# MITM check (session):
# curl https://open.feishu.cn -> 127.0.0.2
# cert issuer: MCP Sandbox Root CA
# control: HIJACK_PROXY_TARGET_URL=https://mcp.doubaocdn.com/vm/hijack

# office edition: DOUBAO_OFFICE_EDITION=public
# suffix-list hijack only when internal
```
