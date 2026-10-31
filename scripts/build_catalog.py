#!/usr/bin/env python3
"""Build the public catalog, plugin READMEs, marketplace and Markdown index.

The catalog file is the single source of truth for the 28 published plugins.
All generated files are deterministic so CI can verify a clean rebuild.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
CATALOG_PATH = ROOT / "catalog" / "plugins.json"
MARKETPLACE_PATH = ROOT / ".codebuddy-plugin" / "marketplace.json"
DOCS = ROOT / "docs"
REPO_URL = "https://github.com/Vane1981-2011/codebuddy-plugins"
PAGES_URL = "https://vane1981-2011.github.io/codebuddy-plugins/"

CATEGORY_MAP = {
    "meta": "developer-tools",
    "business": "business",
    "knowledge": "productivity",
    "engineering": "developer-tools",
    "content": "content-creation",
    "office": "productivity",
    "industry": "productivity",
}


def load_catalog() -> dict:
    data = json.loads(CATALOG_PATH.read_text(encoding="utf-8"))
    plugins = data["plugins"]
    domains = data["domains"]
    assert len(plugins) == 28, f"expected 28 plugins, got {len(plugins)}"
    assert len(domains) == 7, f"expected 7 domains, got {len(domains)}"
    assert len({p["name"] for p in plugins}) == len(plugins), "duplicate plugin names"
    domain_ids = {d["id"] for d in domains}
    assert {p["domain"] for p in plugins} <= domain_ids
    counts = {d["id"]: 0 for d in domains}
    for plugin in plugins:
        counts[plugin["domain"]] += 1
        for key in ("title", "tagline", "summary", "problem", "input", "output", "example"):
            assert plugin.get(key), f"{plugin['name']} missing {key}"
        assert len(plugin.get("workflow", [])) >= 3, f"{plugin['name']} workflow too short"
    for domain in domains:
        assert counts[domain["id"]] == domain["count"], (
            f"{domain['id']} count mismatch: {counts[domain['id']]} != {domain['count']}"
        )
    return data


def version_key(value: str) -> tuple[int, ...]:
    return tuple(int(x) for x in re.findall(r"\d+", str(value or "0"))[:3])


def skill_path(plugin_name: str) -> Path:
    return ROOT / "plugins" / plugin_name / "skills" / plugin_name / "SKILL.md"


def split_frontmatter(text: str) -> tuple[str, str, str]:
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n?(.*)$", text, re.S)
    if not match:
        raise ValueError("SKILL.md has no YAML frontmatter")
    return match.group(1), match.group(2), text


def read_skill(plugin_name: str) -> tuple[Path, dict, str]:
    path = skill_path(plugin_name)
    text = path.read_text(encoding="utf-8")
    front, body, _ = split_frontmatter(text)
    data = yaml.safe_load(front)
    if not isinstance(data, dict):
        raise ValueError(f"{path} frontmatter is not a mapping")
    return path, data, body


def enable_skill(plugin_name: str) -> None:
    """Make every published skill loadable by the host on first install."""
    path = skill_path(plugin_name)
    text = path.read_text(encoding="utf-8")
    front, body, _ = split_frontmatter(text)
    if re.search(r"^disable:\s*true\s*$", front, re.M):
        front = re.sub(r"^disable:\s*true\s*$", "disable: false", front, flags=re.M)
    elif not re.search(r"^disable:\s*", front, re.M):
        front = front.rstrip() + "\ndisable: false"
    path.write_text(f"---\n{front}\n---\n{body}", encoding="utf-8")


def plugin_metadata(data: dict) -> dict[str, dict]:
    metadata: dict[str, dict] = {}
    for plugin in data["plugins"]:
        name = plugin["name"]
        plugin_json_path = ROOT / "plugins" / name / ".codebuddy-plugin" / "plugin.json"
        current = json.loads(plugin_json_path.read_text(encoding="utf-8"))
        _, skill_front, _ = read_skill(name)
        versions = [
            str(current.get("version", "0.0.0")),
            str(skill_front.get("version", "0.0.0")),
        ]
        version = max(versions, key=version_key)
        plugin_url = f"{REPO_URL}/tree/main/plugins/{name}"
        page_url = f"{PAGES_URL}plugins/{name}.html"
        current.update(
            {
                "name": name,
                "displayName": plugin["title"],
                "description": plugin["summary"],
                "description_zh": plugin["tagline"],
                "version": version,
                "author": {"name": "Vane1981", "url": "https://github.com/Vane1981-2011"},
                "homepage": page_url,
                "repository": plugin_url,
                "license": plugin["license"],
                "category": CATEGORY_MAP[plugin["domain"]],
                "keywords": plugin["tags"],
                "skills": [f"./skills/{name}"],
            }
        )
        plugin_json_path.write_text(
            json.dumps(current, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
        metadata[name] = current
    return metadata


def build_marketplace(data: dict, metadata: dict[str, dict]) -> None:
    marketplace = json.loads(MARKETPLACE_PATH.read_text(encoding="utf-8"))
    marketplace.update(
        {
            "name": "codebuddy-skills",
            "description": "28 个可安装的 AI Agent 技能：财务 BP、税务风控、合同审查、知识蒸馏、内容生产与工程护栏。",
            "owner": {"name": "Vane1981", "url": "https://github.com/Vane1981-2011"},
            "homepage": PAGES_URL,
            "repository": REPO_URL,
            "license": "MIT",
        }
    )
    entries = []
    for plugin in data["plugins"]:
        meta = metadata[plugin["name"]]
        entries.append(
            {
                "name": plugin["name"],
                "displayName": plugin["title"],
                "description": plugin["summary"],
                "description_zh": plugin["tagline"],
                "source": f"./plugins/{plugin['name']}",
                "version": meta["version"],
                "category": CATEGORY_MAP[plugin["domain"]],
                "tags_zh": plugin["tags"],
                "author": {"name": "Vane1981", "url": "https://github.com/Vane1981-2011"},
                "homepage": meta["homepage"],
                "repository": meta["repository"],
                "license": plugin["license"],
                "skills": [f"./plugins/{plugin['name']}/skills/{plugin['name']}"],
            }
        )
    marketplace["plugins"] = entries
    MARKETPLACE_PATH.write_text(
        json.dumps(marketplace, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


def build_plugin_readmes(data: dict, metadata: dict[str, dict]) -> None:
    domain_by_id = {d["id"]: d for d in data["domains"]}
    for plugin in data["plugins"]:
        name = plugin["name"]
        domain = domain_by_id[plugin["domain"]]
        meta = metadata[name]
        workflow = "\n".join(
            f"{index}. **{step.split('；')[0].strip()}**" for index, step in enumerate(plugin["workflow"], 1)
        )
        tags = " ".join(f"`{tag}`" for tag in plugin["tags"])
        license_line = (
            "Apache-2.0；本插件目录内的许可证优先"
            if plugin["license"] == "Apache-2.0"
            else "MIT"
        )
        body = f"""# {plugin['title']}

> {plugin['tagline']}

[![License](https://img.shields.io/badge/license-{plugin['license'].replace('-', '--')}-blue.svg)](../../LICENSE)
[![Domain](https://img.shields.io/badge/domain-{domain['name_en'].replace(' ', '%20')}-7c9cff.svg)](../../docs/SKILL-CATALOG.md#{domain['id']})
[![Version](https://img.shields.io/badge/version-{meta['version']}-brightgreen.svg)](../../CHANGELOG.md)
[![Agent Skill](https://img.shields.io/badge/Agent-Skill-67d6c4.svg)](../../docs/ARCHITECTURE.md)

{plugin['summary']}

## 什么时候用它

{plugin['problem']}

**适合**：需要把这类判断从“凭经验”变成“有输入、有步骤、有交付物”的工作。  

## 不适用

{plugin['not_for']}

## 30 秒安装

```text
/plugin marketplace add Vane1981-2011/codebuddy-plugins
/plugin install {name}
```

安装后直接描述任务，或显式调用 `/{name}`。

## 输入与输出

| 项目 | 内容 |
|---|---|
| 最小输入 | {plugin['input']} |
| 主要输出 | {plugin['output']} |
| 交付形态 | 结构化结论、执行记录与可复用模板 |

## 执行流程

{workflow}

## 使用示例

```text
{plugin['example']}
```

## 它会交付什么

- 一份可以直接进入下一步工作的结构化结果，而不是泛泛建议。
- 关键假设、证据来源和未决问题会被显式记录。
- 涉及专业判断时，输出会标注适用边界，需由具备资质的人复核。

## 文件结构

```text
plugins/{name}/
├── README.md
├── .codebuddy-plugin/plugin.json
└── skills/{name}/SKILL.md
```

## 质量与边界

- 执行前确认目标、约束与最小输入，信息不足时先补关键事实。
- 关键结论保留来源、假设和验收记录，避免“看起来合理”的黑箱输出。
- 涉及法律、税务、投资、安全等专业判断时，本技能只作为辅助材料，不替代持证专业人士的意见。

标签：{tags}

许可：{license_line}。运行说明见 [`SKILL.md`](skills/{name}/SKILL.md)。

---

[返回技能目录](../../docs/SKILL-CATALOG.md) · [在线详情]({PAGES_URL}plugins/{name}.html) · [提交问题]({REPO_URL}/issues)
"""
        (ROOT / "plugins" / name / "README.md").write_text(body, encoding="utf-8")


def build_catalog_markdown(data: dict, metadata: dict[str, dict]) -> None:
    domain_by_id = {d["id"]: d for d in data["domains"]}
    lines = [
        "# 28 个技能 · 完整目录",
        "",
        "> 按 7 大领域组织。每个插件都是独立可安装单元，包含 `SKILL.md`、插件清单和独立 README。",
        "",
        f"在线版本：<{PAGES_URL}>",
        "",
        "## 领域概览",
        "",
        "| 领域 | 插件数 | 解决的问题 |",
        "|---|---:|---|",
    ]
    for domain in data["domains"]:
        lines.append(
            f"| [{domain['name']}](#{domain['id']}) | {domain['count']} | {domain['description']} |"
        )
    lines += ["", "## 快速选择", ""]
    for plugin in data["plugins"]:
        domain = domain_by_id[plugin["domain"]]
        lines.append(
            f"- **{plugin['title']}**（`{plugin['name']}`，{domain['name']}）— {plugin['tagline']}。{plugin['summary']}"
        )
    for domain in data["domains"]:
        lines += [
            "",
            f'<a id="{domain["id"]}"></a>',
            f"## {domain['icon']} {domain['name']} · {domain['name_en']}",
            "",
            f"{domain['description']}。共 {domain['count']} 个插件。",
            "",
        ]
        for plugin in data["plugins"]:
            if plugin["domain"] != domain["id"]:
                continue
            meta = metadata[plugin["name"]]
            lines += [
                f"### {plugin['title']}",
                "",
                f"> {plugin['tagline']}",
                "",
                plugin["summary"],
                "",
                "| 项目 | 内容 |",
                "|---|---|",
                f"| 插件名 | `{plugin['name']}` |",
                f"| 版本 | `{meta['version']}` |",
                f"| 许可 | {plugin['license']} |",
                f"| 最小输入 | {plugin['input']} |",
                f"| 主要输出 | {plugin['output']} |",
                f"| 安装 | `/plugin install {plugin['name']}` |",
                "",
                f"示例：`{plugin['example']}`",
                "",
                f"[插件说明]({REPO_URL}/tree/main/plugins/{plugin['name']}) · [在线详情]({PAGES_URL}plugins/{plugin['name']}.html)",
                "",
            ]
    lines += [
        "---",
        "",
        f"返回 [仓库首页]({REPO_URL}) · 查看 [安装指南]({REPO_URL}/blob/main/docs/INSTALL.md) · "
        f"了解 [架构设计]({REPO_URL}/blob/main/docs/ARCHITECTURE.md)",
        "",
    ]
    (DOCS / "SKILL-CATALOG.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    data = load_catalog()
    DOCS.mkdir(parents=True, exist_ok=True)
    for plugin in data["plugins"]:
        enable_skill(plugin["name"])
    metadata = plugin_metadata(data)
    build_marketplace(data, metadata)
    build_plugin_readmes(data, metadata)
    build_catalog_markdown(data, metadata)
    print(f"built catalog: {len(data['plugins'])} plugins / {len(data['domains'])} domains")


if __name__ == "__main__":
    main()
