---
name: expert-sync
description: WorkBuddy
  专家市场自动同步——检测新增/更新的内置专家与技能，自动匹配用户领域并安装。触发词：专家同步、检查专家更新、sync
  experts、更新技能库、市场新技能。
version: 2.1.0
agent_created: true
disable: true
---

# Expert Sync v2.1 — 专家市场自动同步器

自动监控 WorkBuddy 内置专家市场（experts + cb_teams + official）变化，
发现新增/迭代的专家及其技能，匹配用户专业领域后自动安装或推荐。

**v2.1 升级**：experts 市场无 `.marketplace-version` 文件，改用 plugin.json 联合指纹检测。

## 用户画像

默笙夏夏的核心领域（优先匹配）：
1. **财税/金融** — 建安企业财税咨询、税务合规、审计
2. **金融投资** — A股/港股/美股、基金诊断
3. **项目管理** — 全行业项目管理自动化
4. **数据分析** — 经营分析、合规监控、可视化
5. **知识管理** — Obsidian、腾讯乐享、知识卡片
6. **内容创作** — PPT制作、公众号运营、视频生成
7. **投资研究** — 尽调、估值、投行建模

## 市场目录

| 市场 | 路径 | 版本检测方式 |
|------|------|-------------|
| Experts | `~/.workbuddy/plugins/marketplaces/experts/plugins/` | plugin.json 联合 MD5 指纹 |
| cb_teams | `~/.workbuddy/plugins/marketplaces/cb_teams_marketplace/plugins/` | `.marketplace-version` UUID |
| Official | `~/.workbuddy/plugins/marketplaces/codebuddy-plugins-official/plugins/` | `.marketplace-version` UUID |

## 基线文件

`~/.workbuddy/skills/expert-sync/baseline.json` — 存储上次同步状态

结构：
```json
{
  "last_sync": "2026-07-25T08:54:00+08:00",
  "marketplace_versions": {
    "experts": "6a7c9161",
    "cb_teams": "c15d8162",
    "official": "f0557bdc"
  },
  "known_experts": { ... },
  "installed_skills": [...],
  "pre_sync_snapshot": { ... }
}
```

## 执行流程

### Phase 0: 同步前快照
1. 扫描 `~/.workbuddy/skills/` 下所有技能目录
2. 计算每个技能的 SHA256 哈希和文件数
3. 写入 baseline 的 `pre_sync_snapshot` 字段

### Phase 1: 版本检测
1. 对 cb_teams 和 official：读取 `.marketplace-version` UUID，与 baseline 对比
2. 对 experts：执行 `find plugins -name "plugin.json" -exec md5 -q {} \; | sort | md5 -q` 计算联合指纹
3. 全部相同 → 报告「无变化」，跳过后续
4. 有变化 → 进入 Phase 2

### Phase 2: 全量扫描
1. 遍历所有市场每个插件的 `.codebuddy-plugin/plugin.json`
2. 提取：name, version, description, skills（从 skills/*/SKILL.md 目录枚举）, agents 数量
3. 汇总生成当前市场状态快照

### Phase 3: 基线对比
1. 与 baseline 中的 `known_experts` 逐插件对比
2. 识别：新增插件、版本更新、新增技能
3. 去重：已在 baseline 中的不标记为新增

### Phase 4: 过滤与领域匹配
过滤规则（按优先级）：
1. **系统内置**：以下技能由插件直接内置到 available_skills，无需安装到本地：
   - `neodata-financial-search`, `westock-data`, `westock-tool`, `wb-finance-skill`
   - `tencent-docs`, `tencent-docs-routing`, `tencent-pptx`, `tencent-saas-docs`
   - `geography-map-compliance-guard`, `cloudstudio-deploy`
   - `expert-manager`, `marketplace-skill-installer`, `skill-creator`
   - `cnb-api`, `lexiang-knowledge-base`, `3D模型与视频特效`
   - `agent-browser`, `playwright-cli`, `find-skills`
   - `xlsx`, `docx`, `pptx`, `pdf`, `pdfkit-py`（document-skills 已纳入，但本地也有 hardened）
   - `weixinpay-feedback`, `weixinpay-pay`, `weixinpay-register`
2. **Hardened 版本跳过**：已在本地有修改版的技能不覆盖
3. **已安装跳过**：已在 `installed_skills` 列表中的不重复

领域匹配完成后，按相关度分三类：
- **高相关（score ≥ 3）** → 自动安装到 `~/.workbuddy/skills/`
- **中相关（1 ≤ score < 3）** → 列入推荐清单
- **低相关（score = 0）** → 忽略

### Phase 5: 安装执行
1. 高相关技能 → 从市场对应 skills 目录复制到 `~/.workbuddy/skills/`
2. 中相关技能 → 生成推荐清单
3. 更新 baseline 的 `installed_skills` 列表

### Phase 6: 报告输出
生成 Markdown 报告，保存到 `.workbuddy/outputs/expert-sync-report-{date}.md`

### Phase 7: 审计留痕
追加审计记录到 `~/.workbuddy/skills/expert-sync/audit/sync-audit.jsonl`

## 关键规则

1. **增量优先**：无版本变化则跳过全量扫描
2. **去重**：已在 `~/.workbuddy/skills/` 中的技能不重复安装
3. **Hardened 优先**：本地已有 hardened 版本的跳过市场版本
4. **记录决策**：每次安装/跳过决策更新 baseline
5. **审计完整**：每次同步写入 sync-audit.jsonl
6. **experts 指纹**：使用 `find plugins -name "plugin.json" -exec md5 -q {} \; | sort | md5 -q` 检测变更

## 自动化调度

- 由 automation-1780452996917 每日 09:00 CST 触发
- 执行记录写入 `.workbuddy/automations/automation-1780452996917/memory.md`
- 输出报告保存在 `.workbuddy/outputs/`
