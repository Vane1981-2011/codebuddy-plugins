# 安装指南

> 目标：用两条命令完成市场订阅与插件安装，并在 1 分钟内验证技能可用。

## 1. 环境要求

- 支持 CodeBuddy / WorkBuddy 插件市场的宿主。
- 能访问 GitHub。
- 无需额外 API Key；具体插件的模型与工具依赖见各自 `SKILL.md`。

技能层遵循 Agent Skills 的目录约定，其他兼容宿主可按 `plugins/<name>/skills/<name>/` 手动加载。

## 2. 添加市场

在对话中输入：

```text
/plugin marketplace add Vane1981-2011/codebuddy-plugins
```

也可以使用完整仓库地址：

```text
/plugin marketplace add https://github.com/Vane1981-2011/codebuddy-plugins
```

添加成功后，市场中应出现 28 个插件。

## 3. 安装一个插件

以财务 BP 插件为例：

```text
/plugin install financial-bp-command-center
```

其他常用插件：

```text
/plugin install tax-risk-early-warning-engine
/plugin install contract-risk-scanner
/plugin install cangjie-skill
/plugin install creative-origin-engine
/plugin install context-manager
```

## 4. 验证安装

安装后可以：

1. 直接描述任务，让宿主根据 `description` 自动匹配技能。
2. 显式调用 `/<plugin-name>`。
3. 检查插件目录下是否存在 `SKILL.md`，且 frontmatter 中 `disable` 不为 `true`。

示例：

```text
用财务 BP 视角分析 Q4 渠道预算，输出差异原因、影响金额和三条调整建议。
```

## 5. 更新

```text
/plugin marketplace update Vane1981-2011/codebuddy-plugins
/plugin update financial-bp-command-center
```

或重新执行 `marketplace add` 与 `install`。插件版本记录见 [`CHANGELOG.md`](../CHANGELOG.md)。

## 6. 手动安装（离线或自托管）

```bash
git clone https://github.com/Vane1981-2011/codebuddy-plugins.git
cd codebuddy-plugins
```

把需要的插件目录复制到宿主的插件目录，或直接将 `plugins/<name>/skills/<name>/` 作为技能目录加载。每个插件的 `plugin.json` 包含名称、版本、许可与技能入口。

## 7. 常见问题

### 市场添加成功，但搜索不到插件

- 确认仓库默认分支为 `main`。
- 确认 `.codebuddy-plugin/marketplace.json` 存在且可访问。
- 重新执行 `marketplace add`，或清除宿主的市场缓存后重试。

### 安装成功，但技能没有触发

- 检查 `SKILL.md` 的 frontmatter 是否存在 `disable: true`。
- 检查 `description` 是否包含你的任务关键词。
- 尝试显式调用 `/<plugin-name>`。

### 输出不符合预期

- 补充最小输入：目标、约束、数据口径、交付格式。
- 阅读插件 README 的“不适用”部分，确认场景匹配。
- 在 GitHub Issue 中提供脱敏后的输入、预期输出和实际输出。

### 插件包含专业判断

财税、法律、投资类插件是辅助工具，不替代持证专业人士意见。涉及申报、签约、投资决策时，请由具备资质的人员复核。

## 8. 卸载

```text
/plugin uninstall <plugin-name>
```

如需彻底移除市场：

```text
/plugin marketplace remove Vane1981-2011/codebuddy-plugins
```

## 9. 安全建议

- 不要在对话中粘贴未脱敏的身份证号、银行账号、合同原文或客户数据。
- 对涉及外部命令、浏览器自动化、文件写入的插件，先在隔离环境验证。
- 只从本仓库的 `main` 分支或 Release 快照安装，避免使用来路不明的镜像。

---

[返回首页](index.html) · [查看完整目录](SKILL-CATALOG.html) · [查看质量门禁](QUALITY.html)
