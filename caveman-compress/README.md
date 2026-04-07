<p align="center">
  <img src="https://em-content.zobj.net/source/apple/391/rock_1faa8.png" width="80" />
</p>

<h1 align="center">caveman-compress</h1>

<p align="center">
  <strong>shrink memory file. save token every session.</strong>
</p>

---

A Claude Code skill that compresses your project memory files (`CLAUDE.md`, todos, preferences) into caveman format — so every session loads fewer tokens automatically.

Claude read `CLAUDE.md` on every session start. If file big, cost big. Caveman make file small. Cost go down forever.

## What It Do

```
/ultra-caveman-compress CLAUDE.md
```

```
CLAUDE.md          ← compressed (Claude reads this — fewer tokens every session)
CLAUDE.original.md ← human-readable backup (you edit this)
```

Original never lost. You can read and edit `.original.md`. Run skill again to re-compress after edits.

## Benchmarks

Real results on real project files:

| File | Original | Compressed | Saved |
|------|----------:|----------:|------:|
| `claude-md-preferences.md` | 706 | 285 | **59.6%** |
| `project-notes.md` | 1145 | 535 | **53.3%** |
| `claude-md-project.md` | 1122 | 687 | **38.8%** |
| `todo-list.md` | 627 | 388 | **38.1%** |
| `mixed-with-code.md` | 888 | 574 | **35.4%** |
| **Average** | **898** | **494** | **45%** |

All validations passed ✅ — headings, code blocks, URLs, file paths preserved exactly.

## Before / After

<table>
<tr>
<td width="50%">

### 📄 Original (706 tokens)

> "我强烈建议在所有新代码中启用严格模式使用 TypeScript。请不要使用 `any` 类型，除非确实没有其他办法，如果必须使用，请留下注释解释原因。我发现花时间正确设置类型可以在代码运行之前捕获许多 Bug。"

</td>
<td width="50%">

### 🪨 Caveman (285 tokens)

> "首选TypeScript严格模式。无 `any`，除非不可避免 — 若用需注释原因。正确类型早抓Bug。"

</td>
</tr>
</table>

**Same instructions. 60% fewer tokens. Every. Single. Session.**

## Install

```bash
cp -r ~/.claude/skills/ultra-caveman-compress <path-to-skill>
```

Or if you have the caveman repo:

```bash
cp -r skills/caveman-compress ~/.claude/skills/ultra-caveman-compress
```

**Requires:** Python 3.10+

## Usage

```
/ultra-caveman-compress <filepath>
```

Examples:
```
/ultra-caveman-compress CLAUDE.md
/ultra-caveman-compress docs/preferences.md
/ultra-caveman-compress todos.md
```

### What files work

| Type | Compress? |
|------|-----------|
| `.md`, `.txt`, `.rst` | ✅ Yes |
| Extensionless natural language | ✅ Yes |
| `.py`, `.js`, `.ts`, `.json`, `.yaml` | ❌ Skip (code/config) |
| `*.original.md` | ❌ Skip (backup files) |

## How It Work

```
/caveman-compress CLAUDE.md
        ↓
detect file type        (no tokens)
        ↓
Claude compresses       (tokens — one call)
        ↓
validate output         (no tokens)
  checks: headings, code blocks, URLs, file paths, bullets
        ↓
if errors: Claude fixes cherry-picked issues only   (tokens — targeted fix)
  does NOT recompress — only patches broken parts
        ↓
retry up to 2 times
        ↓
write compressed → CLAUDE.md
write original   → CLAUDE.original.md
```

Only two things use tokens: initial compression + targeted fix if validation fails. Everything else is local Python.

## What Is Preserved

Caveman compress natural language. It never touch:

- Code blocks (` ``` ` fenced or indented)
- Inline code (`` `backtick content` ``)
- URLs and links
- File paths (`/src/components/...`)
- Commands (`npm install`, `git commit`)
- Technical terms, library names, API names
- Punctuation (Only strictly required punctuation is kept, otherwise reduced to minimize tokens)
- Headings (exact text preserved)
- Tables (structure preserved, cell text compressed)
- Dates, version numbers, numeric values

## Why This Matter

`CLAUDE.md` loads on **every session start**. A 1000-token project memory file costs tokens every single time you open a project. Over 100 sessions that's 100,000 tokens of overhead — just for context you already wrote.

Caveman cut that by ~45% on average. Same instructions. Same accuracy. Less waste.

```
┌──────────────────────────────────────────┐
│  TOKEN SAVINGS PER FILE    ████████  45% │
│  SESSIONS THAT BENEFIT     ████████ 100% │
│  INFORMATION PRESERVED     ████████ 100% │
│  SETUP TIME                █         1x  │
└──────────────────────────────────────────┘
```

## Part of Caveman

This skill is part of the [caveman](https://github.com/JuliusBrussee/caveman) toolkit — making Claude use fewer tokens without losing accuracy.

- **caveman** — make Claude *speak* like caveman (cuts response tokens ~65%)
- **caveman-compress** — make Claude *read* less (cuts context tokens ~45%)
