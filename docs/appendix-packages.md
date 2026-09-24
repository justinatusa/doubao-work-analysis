# 附录：软件包与 `/opt` 体积

观测日 **2026-09-24**，`IMAGE_VERSION=1.14.10`。  
本附录承接主文「预装软件概览」；数字与清单均来自当次软件清单贴回或更早的 `sandbox_get_context` 摘要。

## 规模一览

| 类别 | 数量 | 说明 |
|------|------|------|
| deb 系统包 | 约 1275（摘要） | 当次只导出字母序到 `libuv1` 的前半 **953** 条；**后半（≥ libva）未导出** |
| pip（Python 3.12，`/opt/python3.12`） | **282** | 下方完整表 |
| pip（系统 3.10） | ≈154 | 未逐项入库 |
| pip（`/opt/python3.11`） | ≈37 | 未逐项入库 |
| npm 全局（用户态） | 0 | `npm ls -g --depth=0` 为空 |

## `/opt` 目录与体积

| 路径 | 体积 | 备注 |
|------|------|------|
| `/opt/vm` | 1.8G | 平台 VM 侧组件（修改时间当次偏新） |
| `/opt/python3.12` | 1.7G | 默认 `python3` |
| `/opt/fnm` | 1.4G | Node 版本管理 |
| `/opt/python3.11` | 368M | |
| `/opt/browser` | 356M | Chromium；实际二进制 `/opt/browser/chrome` |
| `/opt/go` | 268M | go1.23.0 |
| `/opt/runtime` | 187M | 运行时 |
| `/opt/tiger` | 187M | 含 ByteFaaS 相关注入痕迹 |
| `/opt/repl-servers` | 73M | |
| `/opt/novnc` | 2.8M | 桌面前端 |
| `/opt/gem` | 560K | 平台运行时前缀（配置/脚本侧） |
| `/opt/skills` | 124K | 磁盘 skill 树；不等于已挂进 MCP |
| `/opt/aio` | 48K | AIO 相关 |
| `/opt/secure-browser-ui` | 476K | |
| `/opt/browser-ui` / `terminal` / `application` / `jupyter` / `nodejs` | 很小 | 多为入口或薄封装 |

## deb 前半截（不完整）说明

- 导出命令形态：`dpkg-query -W -f='${Package}=${Version}\n'`，按包名排序后在对话里折叠输出。  
- 当次输出在 **`libva-drm2` 处截断**；已入库的前半以 `libuv1` 结尾，约 **953** 包。  
- 前半里可见的大类样本（仅作规模感，不是完整分类）：`fonts-*` ≈137、`fcitx*` ≈12、`nginx*` =6、名称含 libreoffice / libuno ≈35。  
- **不要把 953 当成全量**；全量摘要仍以约 1275 为准，后半未导出。

完整前半原始折叠文本保存在本仓库维护者侧的 raw 落盘，不逐字贴进 GitHub（体量大、且不完整）。需要时可再补导出后半并更新本附录。

## pip 完整清单（Python 3.12，282）

来源：`/opt/python3.12` 的 `pip freeze`（2026-09-24）。本地 wheel 只保留文件名，不展开 sha256。

| 包名 | 版本 |
|------|------|
| `aiohappyeyeballs` | `2.7.1` |
| `aiohttp` | `3.11.13` |
| `aiosignal` | `1.4.0` |
| `aiosqlite` | `0.22.1` |
| `annotated-doc` | `0.0.5` |
| `annotated-types` | `0.8.0` |
| `anyio` | `4.15.1` |
| `argon2-cffi` | `25.1.0` |
| `argon2-cffi-bindings` | `26.1.0` |
| `arrow` | `1.4.0` |
| `asttokens` | `3.0.2` |
| `async-lru` | `2.3.0` |
| `asyncinotify` | `4.4.4` |
| `attrs` | `26.1.0` |
| `Authlib` | `1.8.0` |
| `azure-ai-documentintelligence` | `1.0.2` |
| `azure-core` | `1.41.0` |
| `azure-identity` | `1.25.3` |
| `babel` | `2.18.0` |
| `bashlex` | `0.18` |
| `beartype` | `0.22.9` |
| `beautifulsoup4` | `4.15.0` |
| `binaryornot` | `0.4.4` |
| `bleach` | `6.4.0` |
| `blessed` | `1.49.0` |
| `browser-sdk` | `local wheel: browser_sdk-0.1.0-py3-none-any.whl` |
| `burner-redis` | `0.1.7` |
| `cachelib` | `0.17.0` |
| `cachetools` | `5.5.2` |
| `camelot-py` | `1.0.9` |
| `certifi` | `2026.7.22` |
| `cffi` | `2.1.1` |
| `cfgv` | `3.5.0` |
| `chardet` | `7.6.0` |
| `charset-normalizer` | `3.5.1` |
| `click` | `8.2.1` |
| `cloudpickle` | `3.1.2` |
| `cobble` | `0.1.4` |
| `comm` | `0.2.3` |
| `contourpy` | `1.3.3` |
| `cronsim` | `2.7` |
| `cryptography` | `50.0.1` |
| `cycler` | `0.12.1` |
| `cyclopts` | `4.25.1` |
| `debugpy` | `1.8.21` |
| `defusedxml` | `0.7.1` |
| `Deprecated` | `1.3.1` |
| `diskcache` | `5.6.3` |
| `distlib` | `0.4.3` |
| `distro` | `1.9.0` |
| `dnspython` | `2.8.0` |
| `docstring_parser` | `0.18.0` |
| `email_validator` | `2.2.0` |
| `ephem` | `4.2.1` |
| `et_xmlfile` | `2.0.0` |
| `exceptiongroup` | `1.3.1` |
| `executing` | `2.2.1` |
| `factor_analyzer` | `0.5.0` |
| `fakeredis` | `2.34.1` |
| `fastapi` | `0.116.0` |
| `fastjsonschema` | `2.22.2` |
| `fastmcp` | `2.14.7` |
| `filelock` | `3.32.5` |
| `flake8` | `7.3.0` |
| `flatbuffers` | `25.12.19` |
| `fonttools` | `4.64.0` |
| `fqdn` | `1.5.1` |
| `frozenlist` | `1.8.0` |
| `gitdb` | `4.0.12` |
| `GitPython` | `3.1.62` |
| `greenlet` | `3.5.5` |
| `grep-ast` | `0.9.0` |
| `h11` | `0.16.0` |
| `httpcore` | `1.0.9` |
| `httptools` | `0.8.0` |
| `httpx` | `0.28.1` |
| `httpx-sse` | `0.4.3` |
| `identify` | `2.6.19` |
| `idna` | `3.19` |
| `ipykernel` | `7.3.0` |
| `ipython` | `9.17.1` |
| `ipython_pygments_lexers` | `1.1.1` |
| `isodate` | `0.7.2` |
| `isoduration` | `20.11.0` |
| `jaraco.classes` | `3.4.0` |
| `jaraco.context` | `6.1.2` |
| `jaraco.functools` | `4.6.0` |
| `jedi` | `0.20.0` |
| `jeepney` | `0.9.0` |
| `Jinja2` | `3.1.6` |
| `jinxed` | `2.1.0` |
| `joblib` | `1.6.0` |
| `joserfc` | `1.7.5` |
| `json5` | `0.15.0` |
| `jsonpointer` | `3.1.1` |
| `jsonref` | `1.1.0` |
| `jsonschema` | `4.26.0` |
| `jsonschema-path` | `0.5.0` |
| `jsonschema-specifications` | `2025.9.1` |
| `jupyter-events` | `0.12.1` |
| `jupyter-lsp` | `2.3.1` |
| `jupyter_client` | `8.10.0` |
| `jupyter_core` | `5.9.1` |
| `jupyter_server` | `2.21.0` |
| `jupyter_server_terminals` | `0.5.4` |
| `jupyterlab` | `4.4.5` |
| `jupyterlab_pygments` | `0.3.0` |
| `jupyterlab_server` | `2.28.0` |
| `keyring` | `25.7.0` |
| `kiwisolver` | `1.5.1` |
| `lark` | `1.3.1` |
| `latex2mathml` | `3.79.0` |
| `libcst` | `1.5.0` |
| `libtmux` | `0.62.0` |
| `lunar_python` | `1.4.4` |
| `LunarCalendar` | `0.0.9` |
| `lunardate` | `0.2.2` |
| `lupa` | `2.8` |
| `lxml` | `6.1.3` |
| `magika` | `0.6.3` |
| `mammoth` | `1.11.0` |
| `Markdown` | `3.5.2` |
| `markdown-it-py` | `4.2.0` |
| `markdownify` | `1.2.2` |
| `markitdown` | `0.1.5` |
| `MarkupSafe` | `3.0.3` |
| `matplotlib` | `3.11.0` |
| `matplotlib-inline` | `0.2.2` |
| `mccabe` | `0.7.0` |
| `mcp` | `1.30.0` |
| `mdurl` | `0.1.2` |
| `mistune` | `3.3.4` |
| `more-itertools` | `11.1.0` |
| `MouseInfo` | `0.1.3` |
| `msal` | `1.38.0` |
| `msal-extensions` | `1.3.1` |
| `multidict` | `6.7.1` |
| `nbclient` | `0.11.0` |
| `nbconvert` | `7.17.1` |
| `nbformat` | `5.11.1` |
| `nest-asyncio2` | `1.7.2` |
| `networkx` | `3.6.1` |
| `nodeenv` | `1.10.0` |
| `notebook_shim` | `0.2.4` |
| `numpy` | `1.26.4` |
| `odfpy` | `1.4.1` |
| `olefile` | `0.47` |
| `onnxruntime` | `1.29.0` |
| `openapi-pydantic` | `0.5.1` |
| `opencv-python-headless` | `4.11.0.86` |
| `openhands-aci` | `0.3.3` |
| `openpyxl` | `3.1.5` |
| `opentelemetry-api` | `1.44.0` |
| `packaging` | `26.3` |
| `pandas` | `2.2.3` |
| `pandocfilters` | `1.5.1` |
| `parso` | `0.8.7` |
| `pathable` | `0.6.0` |
| `pathspec` | `1.1.1` |
| `pathvalidate` | `3.3.1` |
| `patsy` | `1.0.3` |
| `pdf2image` | `1.17.0` |
| `pdfminer.six` | `20251230` |
| `pdfplumber` | `0.11.9` |
| `pexpect` | `4.9.0` |
| `pikepdf` | `10.5.1` |
| `pillow` | `10.4.0` |
| `platformdirs` | `4.11.7` |
| `playwright` | `1.62.0` |
| `pre_commit` | `4.6.2` |
| `prometheus_client` | `0.26.0` |
| `prompt_toolkit` | `3.0.53` |
| `propcache` | `0.5.2` |
| `protobuf` | `7.36.1` |
| `psutil` | `7.2.2` |
| `ptyprocess` | `0.7.0` |
| `pure_eval` | `0.2.3` |
| `puremagic` | `2.2.0` |
| `py-key-value-aio` | `0.3.0` |
| `py-key-value-shared` | `0.3.0` |
| `PyAutoGUI` | `0.9.54` |
| `pycodestyle` | `2.14.0` |
| `pycparser` | `3.0` |
| `pycryptodome` | `3.20.0` |
| `pycryptodomex` | `3.20.0` |
| `pydantic` | `2.11.7` |
| `pydantic-settings` | `2.10.1` |
| `pydantic_core` | `2.33.2` |
| `pydocket` | `0.25.0` |
| `pydub` | `0.25.1` |
| `pyee` | `13.0.1` |
| `pyflakes` | `3.4.0` |
| `PyGetWindow` | `0.0.9` |
| `Pygments` | `2.21.0` |
| `PyJWT` | `2.13.0` |
| `PyMsgBox` | `2.0.1` |
| `pyparsing` | `3.3.2` |
| `pypdf` | `5.9.0` |
| `pypdfium2` | `5.6.0` |
| `pyperclip` | `1.1.10` |
| `PyRect` | `0.2.0` |
| `PyScreeze` | `1.0.1` |
| `python-dateutil` | `2.9.0.post0` |
| `python-discovery` | `1.6.0` |
| `python-docx` | `1.2.0` |
| `python-dotenv` | `1.2.3` |
| `python-json-logger` | `4.2.0` |
| `python-multipart` | `0.0.20` |
| `python-pptx` | `1.0.2` |
| `python-server` | `local wheel: python_server-0.1.0-py3-none-any.whl` |
| `python3-xlib` | `0.15` |
| `pytweening` | `1.2.0` |
| `pytz` | `2026.3.post1` |
| `PyYAML` | `6.0.3` |
| `pyzmq` | `27.2.0` |
| `RapidFuzz` | `3.14.6` |
| `redis` | `8.1.0` |
| `referencing` | `0.37.0` |
| `reportlab` | `4.4.1` |
| `requests` | `2.34.2` |
| `rfc3339-validator` | `0.1.4` |
| `rfc3986-validator` | `0.1.1` |
| `rfc3987-syntax` | `1.1.0` |
| `rich` | `15.0.0` |
| `rich-rst` | `2.1.0` |
| `rpds-py` | `2026.6.3` |
| `scikit-learn` | `1.4.0` |
| `scipy` | `1.17.1` |
| `seaborn` | `0.13.2` |
| `SecretStorage` | `3.5.0` |
| `seed-browser-use` | `local wheel: seed_browser_use-0.2.0-py3-none-any.whl` |
| `Send2Trash` | `2.1.0` |
| `setuptools` | `84.0.0` |
| `shellingham` | `1.5.4` |
| `six` | `1.17.0` |
| `smmap` | `5.0.3` |
| `socksio` | `1.0.0` |
| `sortedcontainers` | `2.4.0` |
| `soupsieve` | `2.9.2` |
| `SpeechRecognition` | `3.17.0` |
| `sse-starlette` | `3.0.3` |
| `stack-data` | `0.6.3` |
| `starlette` | `0.46.2` |
| `statsmodels` | `0.14.1` |
| `tabulate` | `0.10.0` |
| `termcolor` | `3.3.0` |
| `terminado` | `0.18.1` |
| `threadpoolctl` | `3.6.0` |
| `tinycss2` | `1.5.1` |
| `tornado` | `6.5.8` |
| `traitlets` | `5.16.1` |
| `tree-sitter` | `0.24.0` |
| `tree-sitter-c-sharp` | `0.23.5` |
| `tree-sitter-embedded-template` | `0.25.0` |
| `tree-sitter-language-pack` | `0.7.3` |
| `tree-sitter-yaml` | `0.7.2` |
| `typer` | `0.27.2` |
| `typing-inspection` | `0.4.4` |
| `typing_extensions` | `4.16.0` |
| `tzdata` | `2026.2` |
| `uncalled-for` | `0.4.0` |
| `unoserver` | `3.6` |
| `uri-template` | `1.3.0` |
| `urllib3` | `2.7.0` |
| `uvicorn` | `0.40.0` |
| `uvloop` | `0.22.1` |
| `virtualenv` | `21.7.8` |
| `Wand` | `0.7.0` |
| `watchdog` | `6.0.0` |
| `watchfiles` | `1.2.0` |
| `wcwidth` | `0.8.3` |
| `webcolors` | `25.10.0` |
| `webencodings` | `0.5.1` |
| `websocket-client` | `1.9.0` |
| `websockets` | `17.1` |
| `whatthepatch` | `1.0.7` |
| `wrapt` | `2.4.0` |
| `xlrd` | `2.0.2` |
| `xlsxwriter` | `3.2.9` |
| `yarl` | `1.24.5` |
| `youtube-transcript-api` | `1.0.3` |
| `zhdate` | `0.1` |

## 值得单独点名的 pip 包（分析向）

| 包 | 版本 | 为何点名 |
|----|------|----------|
| `fastmcp` | 2.14.7 | 与内置 Sandbox MCP 工具面版本号一致 |
| `mcp` | 1.30.0 | MCP SDK |
| `playwright` | 1.62.0 | 预装；主路径实测走自研 CDP bridge，非 Playwright |
| `openhands-aci` | 0.3.3 | Agent 计算机接口类依赖 |
| `PyAutoGUI` | 0.9.54 | GUI 自动化旁证 |
| `browser-sdk` / `python-server` / `seed-browser-use` | local wheel | 平台自研 wheel，装自 `/tmp/wheels` 或 `/tmp` |
| `opentelemetry-api` | 1.44.0 | 可观测 SDK 在场；导出端点当次为空 |
| `markitdown` | 0.1.5 | 对应 `sandbox_convert_to_markdown` 一类能力 |
| `jupyterlab` | 4.4.5 | 笔记本环境 |
| `unoserver` | 3.6 | LibreOffice 无头转换服务 |
