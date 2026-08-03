---
name: pixabay-bgm-search
description: |-
  智能背景音乐搜索与下载技能。从视频文案（标题/描述/字幕）中自动提取音乐关键词（情绪、风格、节奏），
  翻译为英文后搜索 Pixabay Music / Freesound，展示匹配的背景音乐列表（标题、时长、风格标签、
  预览/下载链接）。支持自定义搜索参数（时长范围、风格过滤、来源选择）以及一键下载指定音乐。
  当用户需要搜索背景音乐、为视频配BGM、搜索免费可商用音乐、或在 Pixabay/Freesound 上找音乐时，
  加载此技能。关键词：BGM、背景音乐、配乐、Pixabay、Freesound、免费音乐、视频配乐。
agent_created: true
disable: true
---

# Pixabay BGM Search — 智能背景音乐搜索与下载

自动从视频文案中提取音乐关键词，搜索 Pixabay / Freesound 匹配的背景音乐，展示结果并支持下载。

## 触发条件

当用户涉及以下任一意图时使用此技能：

- "帮我找一段背景音乐" / "给这个视频配个BGM"
- "搜索适合XX场景的音乐"
- 用户粘贴视频文案 + 描述内容风格
- "在Pixabay/Freesound上找音乐"

## 核心流程

### 阶段1：输入解析

从用户输入中提取以下维度：

| 维度 | 提取内容 | 示例 |
|------|----------|------|
| 视频文案 | 标题、描述、字幕、关键词 | "空山新雨后，煮茶听松风" |
| 情感基调 | 温馨/激昂/悲伤/紧张/平静/浪漫/神秘 | 平静、禅意 |
| 节奏快慢 | 快速/中速/舒缓/极慢 | 舒缓 |
| 场景类型 | 自然/城市/室内/科技/古典/现代 | 自然、山景、茶道 |
| 时长要求 | 目标音乐时长（秒） | 97s |

### 阶段2：关键词提取与翻译

执行 `scripts/search_music.py extract` 子命令，自动完成：

1. **中文情绪词提取**：从文案中识别情绪形容词、场景名词
2. **音乐风格映射**：情绪词 → 音乐风格标签
   - 温馨 → warm, gentle, acoustic
   - 激昂 → epic, powerful, orchestral
   - 悲伤 → sad, emotional, piano
   - 平静/禅意 → ambient, meditation, calm, nature
   - 紧张 → suspense, dramatic, tension
   - 浪漫 → romantic, soft, love
3. **英文关键词生成**：组合 2-5 个英文搜索词
4. **备选词生成**：提供同义/近义词列表，用于扩大搜索

### 阶段3：Pixabay / Freesound 音乐搜索

**重要：Pixabay 官方 REST API 不支持音乐搜索（仅 Images/Videos 端点）。**

因此技能采用双源策略：

**源A — Pixabay Music（网页搜索）**：
- 搜索 URL：`https://pixabay.com/music/search/{encoded_query}/`
- 解析 HTML 获取音乐列表
- 提取：标题、时长、风格标签、预览链接、下载链接
- 限制：依赖 HTML 结构，需定期维护解析规则

**源B — Freesound API（推荐主源）**：
- 端点：`https://freesound.org/apiv2/search/text/`
- 需要 Freesound API Key（免费注册获取）
- 支持参数：query, duration, filter, sort
- 返回：完整元数据 + 预览/下载 URL

执行 `scripts/search_music.py search` 子命令。

### 阶段4：结果展示

搜索结果以结构化列表呈现：

```
## 搜索结果 — "ambient meditation calm nature"

| # | 标题 | 时长 | 来源 | 风格标签 |
|---|------|------|------|----------|
| 1 | Mountain Silence | 2:34 | Pixabay | ambient, nature, calm |
| 2 | Zen Garden | 1:45 | Freesound | meditation, peaceful |

每条结果附带：
- 预览链接（可直接试听）
- 下载指令（`download:<ID>` 触发下载）
```

### 阶段5：下载支持

用户通过以下方式触发下载：

- 输入 `download <音乐ID>` 下载指定曲目
- 输入 `download <序号>` 下载列表中对应序号
- 输入 `download all` 下载全部搜索结果

执行 `scripts/download_music.py`，保存至用户指定目录（默认 `~/Downloads/BGM/`）。

## 自定义搜索参数

用户可通过自然语言调整搜索：

- "只找2分钟以上的" → `min_duration: 120`
- "只要舒缓的" → 强制过滤 `mood: calm`
- "多搜几个，20条" → `limit: 20`
- "优先Freesound" → `source: freesound`
- "免费可商用的" → `license: cc0` (Freesound filter)

## 工作流总结

```
用户输入文案+描述
    ↓
search_music.py extract  → 提取关键词、翻译英文
    ↓
search_music.py search   → 双源搜索 (Pixabay + Freesound)
    ↓
结构化展示结果（表格 + 试听 + 下载指令）
    ↓
用户选择 → download_music.py → 保存到本地
```

## 依赖与初始化

### Python 依赖

```bash
pip install requests beautifulsoup4 python-dotenv
```

### API 密钥配置

创建 `~/.pixabay_bgm.env`：

```
PIXABAY_API_KEY=your_pixabay_key_here    # 可选（视频/图片搜索用）
FREESOUND_API_KEY=your_freesound_key_here # 推荐（音乐搜索主源）
FREESOUND_CLIENT_ID=your_client_id_here   # Freesound OAuth2 Client ID（可选，用于下载）
```

### Freesound API Key 获取

1. 注册 https://freesound.org/apiv2/apply/
2. 获取 API Key 填入配置文件
3. 无需审核即可使用基本搜索（限制：2000次/天）

## 脚本说明

- `scripts/search_music.py` — 关键词提取 + 双源音乐搜索
- `scripts/download_music.py` — 音乐文件下载
- `references/freesound_api.md` — Freesound API 完整参考
- `references/keyword_mapping.md` — 中文情绪词 → 英文音乐标签映射表
