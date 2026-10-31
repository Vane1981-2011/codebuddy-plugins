---
name: "weread-skills"
description: >
  微信读书助手 — 搜索书籍、管理书架、查看笔记划线、浏览书评、阅读统计、发现推荐好书、 生成高质量Obsidian知识笔记、Cookie刷新管理。WeRead assistant — search, bookshelf, notes, reviews, stats, cookie.
version: "3.0.0"
agent_created: true
qualityGate: "standard"
trigger_recommended:
  - 微信读书
  - 搜索书籍
  - 我的书架
  - 读书笔记
  - 阅读统计
  - 书评
  - 热门划线
  - 发现好书
  - weread
  - WeRead
  - 同步到Obsidian
  - 生成读书笔记
  - 知识库笔记
  - 刷新微信读书 Cookie
  - 微信读书登录过期
  - Cookie过期
  - 微信读书扫码登录
trigger_exclusive:
  - 微信读书管理
  - WeRead助手
  - 微信读书Cookie刷新
  - WeRead cookie refresh
anti_triggers:
  - 股票
  - 代码
  - 设计
dependencies:
  - playwright-cli (optional, 用于 Cookie 刷新)
  - obsidian (optional)
supersedes:
  - weread-cookie-refresh
zcode:
  version: "1.0"
  τ_role: "executor"
  τ_impact:
    - {'metric': 'τ_execute', 'direction': 'reduce', 'target': '25%', 'mechanism': '批量笔记同步 + 增量更新管道'}
    - {'metric': 'τ_close', 'direction': 'reduce', 'target': '15%', 'mechanism': '自动Obsidian同步 + 知识库归档'}
  bus_compatible: true
  cross_validate_with:
disable: false
last_updated: 2026-07-02
---
# WeRead — 微信读书助手

通过 Agent API Gateway 调用微信读书接口，提供搜索、书架、笔记、书评等能力。**v3.0 新增：知识库笔记质量标准与生成规范 + Cookie刷新管理**。

## 支持的能力

| 能力 | 说明 | 用户示例 | 详细说明 |
|------|------|----------|----------|
| 搜索书籍 | 在书城搜索 | "帮我搜一下三体" | `search.md` |
| 书籍信息 | 查看书籍详情、章节目录、阅读进度 | "这本书有多少章" "我读到哪了" | `book.md` |
| 书架管理 | 查看书架 | "看看我的书架" | `shelf.md` |
| 阅读统计 | 阅读时长、天数、偏好分析、阅读统计摘要 | "我这个月读了多久" "今年读了几本书" | `readdata.md` |
| 笔记划线 | 查看个人笔记数量与内容，包括划线、想法/点评、书签数量 | "看看我在三体里的笔记" "导出我的划线" "在这本书有多少笔记" | `notes.md` |
| 章节热门划线 | 查看书籍/章节热门划线、划线热度及划线下想法 | "看看这章有什么热门划线" "这段话下面有什么想法" | `notes.md` |
| 书籍点评 | 查看书籍的公开点评 | "三体这本书有什么点评？" "看看推荐的点评" | `review.md` |
| 推荐好书 | 个性化推荐/相似推荐 | "给我推荐几本书" | `discover.md` |
| **知识笔记生成** | **基于书籍内容生成高质量 Obsidian 知识库笔记** | **"把反脆弱同步到我的知识库" "生成读书笔记"** | **`note-quality.md`（v2.0 新增）** |
| **Cookie管理** | **Cookie过期刷新、扫码登录、会话维护** | **"Cookie过期了""重新登录微信读书"** | **见下方「Cookie管理」章节（v3.0 新增）** |

根据用户意图参考对应说明文件了解接口参数、回包结构和工作流。

---

## 接口调用规范

### 统一入口

```
POST https://i.weread.qq.com/api/agent/gateway
```

### 鉴权

- Header：`Authorization: Bearer $WEREAD_API_KEY`
- `WEREAD_API_KEY` 从环境变量获取，格式 `wrk-xxxxxxxx`
- 若未设置，提示用户：`export WEREAD_API_KEY=<你的apikey>`
- API Key 绑定用户身份（vid），需要用户身份的接口会自动注入，无需手动传 vid

### 请求格式

- **Method**：POST
- **Content-Type**：application/json
- **Body**：JSON，`api_name` 指定接口，其余为接口参数，**每次请求必须带 `skill_version`**

```bash
curl -X POST "https://i.weread.qq.com/api/agent/gateway" \
  -H "Authorization: Bearer $WEREAD_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"api_name": "/store/search", "keyword": "三体", "count": 10, "skill_version": "3.0.0"}'
```

### 请求 few-shot

**正确：业务参数平铺在 body 顶层。**

```json
{"api_name":"/user/notebooks","count":100,"skill_version":"1.0.5"}
```

**正确：下一页继续平铺 `lastSort`。**

```json
{"api_name":"/user/notebooks","count":100,"lastSort":1516907353,"skill_version":"1.0.5"}
```

**错误：不要把业务参数包在 `params` 内。**

```json
{"api_name":"/user/notebooks","params":{"count":100,"lastSort":1516907353},"skill_version":"1.0.5"}
```

上面的错误写法会导致 `count`、`lastSort` 未被转发，后端按默认值返回第一页，看起来像分页失效。

### 响应格式

- JSON，回包经过字段裁剪，只返回核心字段
- `errcode` 非 0 时表示错误，给出中文提示
- 发送 `{"api_name": "/_list"}` 可查看所有可用接口及参数定义

### 通用规则

1. **版本上报**：每次请求 body 必须包含 `"skill_version": "3.0.0"`（取本文件顶部 version 字段的值），用于服务端检查版本更新。**如果回包中出现 `upgrade_info` 字段，必须立即暂停当前操作，按照 `upgrade_info.message` 中的指引完成升级，升级完成后再重新执行用户请求，不得忽略该字段**
2. **参数平铺**：业务参数必须和 `api_name`、`skill_version` 放在同一层；不要包在 `params`、`data`、`body` 等对象里。只有接口文档明确声明的数组/对象字段（如 `/book/readreviews` 的 `reviews`）才允许作为业务字段传入。
3. **能力文档预检**：调用任何接口前，必须先根据「支持的能力」表阅读对应说明文件（如阅读统计先读 `readdata.md`，书架先读 `shelf.md`），确认接口参数、字段含义、单位、计数口径和工作流；禁止仅凭字段名或经验猜测含义。
4. **字段解释优先级**：解释接口回包时，以对应说明文件中的字段说明为准；如果回包字段名和直觉含义冲突，必须服从说明文件，不得直接翻译字段名。
5. **bookId 解析**：用户输入书名时，先调 `/store/search` 获取 bookId，再执行后续操作
6. **书架数量**：使用 `/shelf/sync` 回答"书架有多少本书/多少条目"时，必须按 `books.length + albums.length + (mp 非空 ? 1 : 0)` 计算；`albums[]` 是专辑/有声书，也属于书架里的书，详细规则见 `shelf.md`
7. **结果展示**：列表用编号展示方便选择；搜索结果重点展示书名、作者、评分；展示接口回包信息时，字段**禁止**直接翻译，应该参考文件中的说明内容提供
8. **上下文衔接**：对话中记住已查询的 bookId，后续操作无需用户重复提供
9. **深度链接**：在展示划线、想法、章节等内容时，拼接对应的跳转链接方便用户直接在 App 中打开，具体格式见下方「深度链接（URL Schema）」章节
10. **数据展示规范**：
   - **时间戳**：所有 Unix 时间戳字段（如 `updateTime`、`createTime`、`finishTime`、`readUpdateTime` 等），**展示时须转为 YYYY-MM-DD 格式**（如 `1748563200` 展示为"2025-05-30"），不得直接展示原始数字
   - **阅读时长**：单位为秒，展示时转为"X小时Y分钟"格式

---

## 深度链接（URL Schema）

在展示书籍、章节、划线等内容时，如果回包字段足以构造链接，应附上对应的跳转链接，方便用户点击后直接在微信读书 App 中打开对应位置。想法/点评不一定都有划线位置，只有具备 `chapterUid` 和 `range` 时才生成划线位置链接。

### 打开书籍（跳转到上次阅读进度）

```
weread://reading?bId={bookId}
```

| 参数 | 说明 | 来源 |
|------|------|------|
| `bookId` | 书籍 ID | 各接口返回的 `bookId` |

**示例**：

```
weread://reading?bId=3300045871
```

**使用场景**：
- 展示书架列表时，每本书附上跳转链接
- 展示搜索结果时，附上「打开阅读」链接
- 展示阅读进度时，提供「继续阅读」链接

### 跳转到指定章节

```
weread://reading?bId={bookId}&chapterUid={chapterUid}
```

| 参数 | 说明 | 来源 |
|------|------|------|
| `bookId` | 书籍 ID | 各接口返回的 `bookId` |
| `chapterUid` | 章节 UID | `/book/chapterinfo` 返回的 `chapters[].chapterUid` |

**示例**：

```
weread://reading?bId=3300045871&chapterUid=107
```

**使用场景**：
- 展示章节目录时，每个章节附上跳转链接

### 跳转到划线/想法所在位置

```
weread://bestbookmark?bookId={bookId}&chapterUid={chapterUid}&rangeStart={rangeStart}&rangeEnd={rangeEnd}&userVid={userVid}
```

| 参数 | 说明 | 来源 |
|------|------|------|
| `bookId` | 书籍 ID | 各接口返回的 `bookId` |
| `chapterUid` | 章节 UID | 划线/想法所属的 `chapterUid` |
| `rangeStart` | 划线起始位置 | `range` 字段中 `-` 前面的数字 |
| `rangeEnd` | 划线结束位置 | `range` 字段中 `-` 后面的数字 |
| `userVid` | 用户 VID | API Key 鉴权后自动关联的用户 ID（从 `/shelf/sync` 等接口的上下文获取，或省略） |

> **range 解析**：划线接口返回的 `range` 格式为 `"起始-结束"`（如 `"900-2004"`），拆分后分别填入 `rangeStart` 和 `rangeEnd`。

**示例**：

```
weread://bestbookmark?bookId=3300045871&chapterUid=107&rangeStart=900&rangeEnd=2004&userVid=583802764
```

**使用场景**：
- 展示划线列表（`/book/bookmarklist`）时，每条划线附上跳转链接（`range` 字段可直接解析）
- 展示热门划线（`/book/bestbookmarks`）时，每条附上跳转链接；`/book/underlines` 只是划线热度统计，不含划线文本
- 展示想法（`/review/list/mine`、`/book/readreviews`）时，只有返回内容包含 `chapterUid` 和 `range` 时才附上跳转到对应划线位置的链接；整本书评或无法定位到划线的点评不强制生成该链接

---

## 🧠 专家思维 — 读书服务诊断

- Q1: 用户意图 → 搜索书籍？管理书架？查看笔记？阅读统计？发现推荐？**生成知识笔记？**
- Q2: 搜索精度 → 按书名/作者/关键词/分类搜索？→ 优先精准匹配
- Q3: 数据时效 → 书架实时/笔记增量/阅读统计按日更新
- **Q4 (v3.0新增): 笔记质量 → 是否涉及 Obsidian 知识库笔记生成？→ 必须先加载 `note-quality.md` 质量规范，禁止凭直觉生成**
- **Q5 (v3.0新增): Cookie状态 → 是否涉及 Cookie 过期/登录？→ 执行下方 Cookie管理 刷新流程**

## 📐 v3.0 新增：知识笔记质量标准（强制加载）

> **⚠️ 当用户请求涉及以下任一场景时，必须先加载 `note-quality.md`：**
> - "同步到Obsidian" / "生成读书笔记" / "写入知识库"
> - "帮我把这本书的笔记整理一下"
> - 任何将微信读书数据转换为知识库内容的操作
>
> **不加载 `note-quality.md` 就生成笔记 = 生产垃圾内容。已因重复空话表格导致知识库污染的教训必须牢记。**

## 📚 知识库引用

| 来源 | 内容 |
|------|------|
| 微信读书 MCP API | 书架/笔记/划线/搜索/统计 |
| 微信读书平台 | 书籍元数据/分类/评分 |
| **实战经验（v3.0）** | **反脆弱笔记改造：4文件28行100%重复表格→差异化检查清单+行业工具箱** |

## 🖨️ 多格式输出

Markdown（默认）。需 Excel 书目清单/笔记导出请告知。

**笔记质量分级（v3.0）：**
- ⭐⭐⭐ **行动导向型**：含可填写检查清单、决策打分卡、实验模板（推荐）
- ⭐⭐ **知识沉淀型**：核心观点清晰、有逻辑拆解、有延伸关联（及格）
- ⭐ **信息搬运型**：仅摘录原文无加工、或填充空话模板（不合格，必须重做）

## 🔄 持续学习

触发：微信读书API新增能力/平台分类体系调整 → 更新可用功能
触发：知识库笔记质量问题发现 → 更新 `note-quality.md` 质量规范
触发：Cookie 登录流程变更 → 更新 `## Cookie管理` 章节

### 更新日志
| 2026-07-02 | v3.0 重大升级 | 吸收 weread-cookie-refresh 全部功能；新增 Cookie管理 能力模块；完整7步Cookie刷新流程含异常处理矩阵和关键Cookie字段表；新增专家思维 Q5 Cookie状态诊断 |
| 2026-06-02 | v2.0 重新封装 | 新增笔记质量标准模块 `note-quality.md`；强化专家思维Q4质量门禁；从反脆弱改造中提取3条核心教训写入规范 |
| 2026-06-02 | v1.1升级 | 新增四能力模块 | — |

---

## 🍪 Cookie管理 — Cookie刷新与维护（v3.0 新增）

> **触发场景**：微信读书 Cookie 过期导致 MCP 请求失败、用户主动要求登录/刷新 Cookie、首次配置微信读书 MCP Server。

### 前置条件

- `playwright-cli` Skill 已安装且可用
- 用户手机上有微信可以扫码
- `~/.workbuddy/mcp.json` 中存在 `mcp-server-weread` 配置

---

### 执行流程（7步）

#### Step 1：打开微信读书网页

先加载 `playwright-cli` Skill，然后打开微信读书首页：

```bash
playwright-cli open https://weread.qq.com/ --browser=chromium
```

等待页面加载完成（约3秒）。

#### Step 2：点击登录按钮，触发扫码

```bash
# 获取页面快照，找到登录按钮的 ref
playwright-cli snapshot | head -60

# 点击登录按钮
playwright-cli click <登录按钮ref>

# 等待2秒让二维码加载
sleep 2

# 截图保存二维码
playwright-cli screenshot --filename=weread-qrcode.png
```

> 常见登录按钮 ref 值：`e31` 或 `e35`（取决于页面版本）。建议先用 snapshot 确认。

#### Step 3：展示二维码给用户

用 `Read` 工具读取截图文件，或告知用户二维码已保存到工作目录。

提示用户：**「请用微信扫描二维码登录微信读书，扫码后在此回复'已扫码'」**

#### Step 4：确认登录成功

用户回复已扫码后，等待5秒让登录状态稳定，验证是否已登录：

```bash
# 重新 snapshot，检查页面是否显示用户头像/昵称（已登录的标志）
playwright-cli snapshot | head -40
```

**判断标准**：页面中出现用户昵称、头像或书架内容，说明登录成功。

> 登录未成功的处理：
> 1. 确认用户是否已完成微信扫码
> 2. 如果已扫码但未跳转，刷新页面后重试：`playwright-cli navigate https://weread.qq.com/`
> 3. 如果二维码过期，回到 Step 2 重新获取

#### Step 5：提取 Cookie

```bash
# 提取 weread.qq.com 域下的所有 Cookie
playwright-cli cookie-list --domain=weread.qq.com
```

**输出格式**：JSON 数组，每个元素包含 `name`、`value`、`domain` 等字段。

#### Step 6：组装 Cookie 字符串并更新配置

从 Step 5 的输出中提取所有 Cookie，按 `name1=value1; name2=value2; ...` 格式组装。

**关键 Cookie 字段**：

| Cookie 名 | 说明 | 重要性 |
|-----------|------|--------|
| `wr_vid` | 用户身份标识 | 必须 |
| `wr_skey` | 会话密钥 | 必须 |
| `wr_gid` | 群组标识 | 建议 |
| `wr_fp` | 设备指纹 | 建议 |

**更新步骤**：
1. 读取 `~/.workbuddy/mcp.json`
2. 找到 `mcp-server-weread` 配置段
3. 更新 `env.WEREAD_COOKIE` 字段为组装好的 Cookie 字符串
4. 保存文件

> Cookie 组装示例：
> ```
> wr_vid=12345678; wr_skey=abcdefgh; wr_gid=87654321; wr_fp=xyz123
> ```
> 注意：不要包含换行符，不要添加引号包裹整个字符串。

#### Step 7：验证与清理

```bash
# 验证 Cookie 有效性（如果存在验证脚本）
bash ~/.workbuddy/scripts/weread-cookie-check.sh 2>/dev/null || echo "验证脚本不存在，请手动测试微信读书 MCP 功能"

# 关闭浏览器
playwright-cli close
```

**验证确认**：提示用户尝试使用微信读书 MCP 功能（如搜索书籍），确认 Cookie 生效。

---

### 异常处理矩阵

| 异常场景 | 处理方式 |
|----------|---------|
| 二维码截图失败 | 检查 playwright-cli 是否正常运行，重试 Step 2 |
| 用户扫码后页面未跳转 | 手动 navigate 到 `https://weread.qq.com/` 再检查 |
| Cookie 提取为空 | 确认已完成登录，检查 cookie-list 命令的 domain 参数 |
| mcp.json 中无 weread 配置 | 提示用户先安装 mcp-server-weread MCP Server |
| 更新后 Cookie 仍无效 | Cookie 字符串可能有特殊字符需要 URL 编码，检查 `wr_skey` 值 |

---

### 关键注意事项

1. **Cookie 有效期**：微信读书 Cookie 通常有效期约30天，过期后需重新刷新
2. **安全性**：Cookie 存储在本地 mcp.json 中，不会上传到外部
3. **浏览器进程**：如果之前有残留的 playwright-cli 进程，Step 1 的 `open` 会自动关闭旧窗口
4. **域名限制**：只提取 `weread.qq.com` 域下的 Cookie，避免混入其他域
5. **MCP 自动检测**：当 MCP Server 返回认证相关错误（如 401/403）时，应主动提示用户 Cookie 可能已过期，引导执行 Cookie 刷新流程

---

## 🛡️ 硬化增强层（由 skill-hardener v1.0.0 自动注入）

> **注入时间**: 2026-06-03 09:09:45
> **硬化等级**: L2
> **硬化评分**: 60/100

### 执行铁律

1. **重试法则**：所有外部调用（API/MCP/文件/网络）使用 `scripts/retry_wrapper.py` 包装，最大 3 次退避重试（2s → 4s → 8s）
2. **验证法则**：执行前运行 `scripts/preflight_check.py`，交付前运行 `scripts/postflight_check.py`
3. **降级法则**：主路径失败后自动走 Fallback 路径（见下方降级路径表）
4. **记录法则**：每次失败自动调用 `scripts/error_capture.py capture` 记录完整错误上下文
5. **自愈法则**：同类型错误出现 1 次即，自动提炼经验注入本文件「踩坑经验」区域

### 踩坑经验（自动积累）

<!-- ERROR_LOG_START -->
（暂无——将在实际执行中由 error_capture.py 自动填充）
<!-- ERROR_LOG_END -->

### 降级路径

| 主路径 | 失败条件 | 降级方案 |
|--------|---------|---------|
| 主 API 调用 | 网络/限流/认证失败 | 本地模拟数据 + 手动操作指南 |
| MCP 工具调用 | 连接断开/超时 | WebSearch + 用户手动确认 |

### 硬化组件清单

| 组件 | 路径 | 用途 |
|------|------|------|
| 重试包装器 | `scripts/retry_wrapper.py` | 所有外部调用的指数退避重试 |
| 前置验证 | `scripts/preflight_check.py` | 执行前环境/依赖/输入校验 |
| 后置校验 | `scripts/postflight_check.py` | 交付前产出完整性校验 |
| 错误捕获 | `scripts/error_capture.py` | 错误上下文记录与模式分析 |
| 踩坑经验 | `references/lessons_learned.md` | 自动积累的错误经验库 |
| 降级路由 | `references/fallback_routes.md` | 主备路径决策表 |

### 快速命令

```bash
# 健康检查
python3 scripts/diagnose_skill.py .

# 查看踩坑经验
cat references/lessons_learned.md

# 分析错误模式
python3 scripts/error_capture.py analyze --skill-path .
```

## Zcode 集成

### τ 角色与贡献

本技能在 Zcode 体系中承担 **executor** 角色，遵循 `skills/shared/zcode/zcode-embedding-standard.md` 标准。

| 指标 | 方向 | 机制 | 目标压缩 |
|------|------|------|---------|
| τ_execute | reduce | 批量笔记同步 + 增量更新管道 | 25% |
| τ_close | reduce | 自动Obsidian同步 + 知识库归档 | 15% |

### 质量门禁

- **等级**: standard
- **依据**: `skills/shared/skill-quality-gate.md`
- **执行前**: 输入校验 + 反模式预检（`skills/shared/feedback/anti-patterns.yaml`）
- **执行后**: 输出校验 + 交付判定（三阶段门禁）

### 交叉验证

- **协同技能**: 无
- **校验协议**: `skills/shared/zcode/zcode-embedding-standard.md` 第 4 节

### 反馈闭环

- **输出触发**: Memory 写入 + τ 快照更新 + 反模式比对（如适用）
- **遵循协议**: `skills/shared/feedback/feedback-loop-protocol.md`

---
*Zcode 嵌入版本: 1.0 | © 版权所有：默笙夏夏の知書房 - 2026-07-09*
