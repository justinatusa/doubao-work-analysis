from xml.sax.saxutils import escape
FONT = "'PingFang SC','Hiragino Sans GB','Microsoft YaHei','Noto Sans CJK SC','Noto Serif CJK SC',sans-serif"

def box(x,y,w,h,title,sub=None,fill="#eef4ff",stroke="#4a6fb5",rx=8,tsize=15,bold=True):
    s=f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="1.5"/>'
    cy = y+h/2 + (0 if sub is None else -8)
    s+=f'<text x="{x+w/2}" y="{cy+5}" text-anchor="middle" font-size="{tsize}" font-weight="{"600" if bold else "400"}" fill="#1d2b4a">{escape(title)}</text>'
    if sub:
        for i,line in enumerate(sub.split("\n")):
            s+=f'<text x="{x+w/2}" y="{cy+24+i*16}" text-anchor="middle" font-size="12" fill="#4b5563">{escape(line)}</text>'
    return s

def arrow(x1,y1,x2,y2,label=None,dash=False):
    d=' stroke-dasharray="5,4"' if dash else ''
    s=f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#6b7280" stroke-width="1.6" marker-end="url(#ah)"{d}/>'
    if label:
        s+=f'<text x="{(x1+x2)/2+6}" y="{(y1+y2)/2+4}" font-size="12" fill="#6b7280">{escape(label)}</text>'
    return s

def svg(w,h,body,title):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" font-family="{FONT}">
<title>{escape(title)}</title>
<defs><marker id="ah" markerWidth="10" markerHeight="8" refX="9" refY="4" orient="auto"><path d="M0,0 L10,4 L0,8 z" fill="#6b7280"/></marker></defs>
<rect width="100%" height="100%" fill="#ffffff"/>
{body}
</svg>'''

# ---------- detailed architecture ----------
W=1000; b=""
b+=f'<text x="{W/2}" y="30" text-anchor="middle" font-size="19" font-weight="700" fill="#111827">豆包工作 Agent 沙箱 · 架构总图</text>'
b+=f'<text x="{W/2}" y="52" text-anchor="middle" font-size="12" fill="#6b7280">观测日 2026-09-24 · 镜像构建号 IMAGE_VERSION=1.14.10 · 非官方观察笔记</text>'
b+=box(400,70,200,44,"用户浏览器",fill="#f3f4f6",stroke="#9ca3af")
b+=arrow(500,114,500,140)
b+=box(360,140,280,50,"外层网关","在这里验证用户身份（JWT）",fill="#fff7e6",stroke="#d97706")
b+=arrow(500,190,500,236)
# sandbox container
b+=f'<rect x="40" y="215" width="920" height="420" rx="14" fill="#fafbff" stroke="#4a6fb5" stroke-width="2" stroke-dasharray="8,5"/>'
b+=f'<text x="60" y="240" font-size="14" font-weight="600" fill="#4a6fb5">临时云沙箱 · Kata 微虚拟机 + Nydus 按需镜像 · 跑在火山 ByteFaaS / veFaaS 函数算力上 · 约 2 核 / 4 GiB</text>'
b+=box(360,250,280,54,"nginx :8080","沙箱入口；信任内网，不再验票",fill="#e8f5e9",stroke="#2e7d32")
xs=[60,240,420,600,780]; wd=160
items=[("桌面","noVNC / Xvnc"),("Chrome","CDP 调试口 :9222"),("MCP hub :8091","工具总线"),("平台 VM API :10000","CC 文件/命令\nComputerUse 键鼠"),("运行时钩子","vm_runtime_hook\n:10080")]
for x,(t,s) in zip(xs,items):
    b+=arrow(500,304,x+wd/2,350)
    b+=box(x,350,wd,70,t,s)
# browser mcp under hub
b+=box(420,450,160,56,"browser MCP :8100","模型可直接调用",fill="#e0f2fe",stroke="#0284c7")
b+=arrow(500,420,500,450)
b+=arrow(420,478,320,420,"CDP 协议")
b+=f'<text x="700" y="440" font-size="11" fill="#b45309">需平台签名</text>'
b+=box(60,450,300,56,"supervisord（/opt/gem）","托管 nginx、Chrome、MCP、VNC 等进程",fill="#f5f3ff",stroke="#7c3aed")
b+=box(620,450,320,56,"出网代理","tinyproxy / gost / 飞书域名本地劫持",fill="#fff1f2",stroke="#e11d48")
# storage row
b+=box(60,540,420,70,"/home/user · hpvs 持久卷","关掉对话后文件往往还在（含 Doubao/chats）",fill="#ecfdf5",stroke="#059669")
b+=box(520,540,420,70,"/ 与 /tmp/user · 本实例本地盘","实例回收即消失（日志 /var/log/gem 也在这里）",fill="#f9fafb",stroke="#9ca3af")
# egress
b+=arrow(780,506,780,540+0) if False else ""
b+=f'<line x1="940" y1="478" x2="975" y2="478" stroke="#6b7280" stroke-width="1.6"/><line x1="975" y1="478" x2="975" y2="668" stroke="#6b7280" stroke-width="1.6"/>'
b+=arrow(975,668,760,668)
b+=box(420,648,340,44,"VortexIP 平台出口代理",fill="#fff1f2",stroke="#e11d48")
b+=arrow(420,670,330,670)
b+=box(100,648,230,44,"公网（共享 NAT 出口 IP）",fill="#f3f4f6",stroke="#9ca3af")
b+=f'<text x="{W/2}" y="722" text-anchor="middle" font-size="11" fill="#9ca3af">端口与路径均为当次实测；平台侧调度、网关签名细节不在容器内，未测到。</text>'
open('docs/assets/architecture.svg','w').write(svg(W,740,b,"豆包工作 Agent 沙箱架构总图"))

# ---------- README overview ----------
W=900; b=""
b+=f'<text x="{W/2}" y="28" text-anchor="middle" font-size="17" font-weight="700" fill="#111827">架构速览（2026-09-24 · IMAGE_VERSION=1.14.10）</text>'
b+=box(60,60,150,46,"用户",fill="#f3f4f6",stroke="#9ca3af")
b+=arrow(210,83,250,83)
b+=box(250,60,170,46,"外层网关","验证身份",fill="#fff7e6",stroke="#d97706")
b+=arrow(420,83,460,83)
b+=f'<rect x="460" y="45" width="410" height="275" rx="12" fill="#fafbff" stroke="#4a6fb5" stroke-width="2" stroke-dasharray="8,5"/>'
b+=f'<text x="475" y="66" font-size="12" font-weight="600" fill="#4a6fb5">临时云沙箱（Kata 微虚拟机）</text>'
b+=box(560,76,210,40,"nginx 入口",fill="#e8f5e9",stroke="#2e7d32")
rows=[("桌面（noVNC）",126),("浏览器（Chrome / CDP）",170),("MCP 工具（模型可调）",214),("平台 VM API（需签名）",258)]
for t,y in rows:
    b+=box(560,y+10,210,34,t,fill="#eef4ff",stroke="#4a6fb5",tsize=13,bold=False)
b+=f'<line x1="545" y1="96" x2="545" y2="285" stroke="#6b7280" stroke-width="1.6"/><line x1="560" y1="96" x2="545" y2="96" stroke="#6b7280" stroke-width="1.6"/>'
for t,y in rows:
    b+=arrow(545,y+27,560,y+27)
b+=box(60,200,360,46,"出网：本地代理 → VortexIP → 公网",fill="#fff1f2",stroke="#e11d48",tsize=13)
b+=arrow(460,223,420,223)
b+=box(60,268,360,46,"家目录 hpvs 持久卷：跨会话保留",fill="#ecfdf5",stroke="#059669",tsize=13)
open('docs/assets/overview.svg','w').write(svg(W,340,b,"架构速览"))
print("ok")
