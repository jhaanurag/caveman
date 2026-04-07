<p align="center">
  <img src="https://em-content.zobj.net/source/apple/391/rock_1faa8.png" width="120" />
</p>

<h1 align="center">caveman</h1>

<p align="center">
  <strong>why use many token when few do trick</strong>
</p>

<p align="center">
  <a href="https://github.com/JuliusBrussee/caveman/stargazers"><img src="https://img.shields.io/github/stars/JuliusBrussee/caveman?style=flat&color=yellow" alt="Stars"></a>
  <a href="https://github.com/JuliusBrussee/caveman/commits/main"><img src="https://img.shields.io/github/last-commit/JuliusBrussee/caveman?style=flat" alt="Last Commit"></a>
  <a href="LICENSE"><img src="https://img.shields.io/github/license/JuliusBrussee/caveman?style=flat" alt="License"></a>
</p>

<p align="center">
  <a href="#install">Install</a> •
  <a href="#benchmarks">Benchmarks</a> •
  <a href="#before--after">Before/After</a> •
  <a href="#intensity-levels">Intensity Levels</a> •
  <a href="#caveman-compress">Compress</a> •
  <a href="#why">Why</a>
</p>

---

A [Claude Code](https://docs.anthropic.com/en/docs/claude-code) skill/plugin and Codex plugin that makes agent talk like a Chinese caveman (`caveman-zh`) — cutting **~75% of output tokens** while keeping full technical accuracy. Plus a companion tool (`caveman-compress-zh`) that compresses your memory files to cut **~45% of input tokens** every session.

Based on the viral observation that caveman-speak dramatically reduces LLM token usage without losing technical substance. So we made it a one-line install.

## Before / After

<table>
<tr>
<td width="50%">

### 🗣️ Normal Claude (69 tokens)

> "您的React组件重新渲染的原因可能是因为您在每个渲染周期都创建了一个新的对象引用。当您将内联对象作为prop传递时，React的浅比较每次都会将其视为不同的对象，从而触发重新渲染。我建议使用useMemo来记忆该对象。"

</td>
<td width="50%">

### 🪨 Caveman Claude (19 tokens)

> "每次渲染新对象引用。内联对象prop = 新引用 = 重渲染。包 `useMemo`。"

</td>
</tr>
<tr>
<td>

### 🗣️ Normal Claude

> "没问题！我很乐意帮您解决这个问题。您遇到的问题可能是因为身份验证中间件没有正确验证Token过期时间。让我看看并建议一个修复方案。"

</td>
<td>

### 🪨 Caveman Claude

> "auth中间件bug。Token过期检查用 `<` 不做 `<=`。改:"

</td>
</tr>
</table>

**Same fix. 75% less word. Brain still big.**

**Sometimes too much caveman. Sometimes not enough:**

<table>
<tr>
<td width="33%">

#### 🪶 Lite

> "你的组件重新渲染是因为你每次渲染都会创建新的对象引用。内联对象prop每次都通不过浅层比较。把它包在 `useMemo` 里。"

</td>
<td width="33%">

#### 🪨 Full

> "每次渲染新对象引用。内联对象prop = 新引用 = 重渲染。包 `useMemo`。"

</td>
<td width="33%">

#### 🔥 Ultra

> "内联对象prop → 新引用 → 重渲染。 `useMemo`。"

</td>
</tr>
</table>

**Same answer. You pick how many word.**

## Benchmarks

Real token counts from the Claude API ([reproduce it yourself](benchmarks/)):

<!-- BENCHMARK-TABLE-START -->
| Task | Normal (tokens) | Caveman (tokens) | Saved |
|------|---------------:|----------------:|------:|
| Explain React re-render bug | 1180 | 159 | 87% |
| Fix auth middleware token expiry | 704 | 121 | 83% |
| Set up PostgreSQL connection pool | 2347 | 380 | 84% |
| Explain git rebase vs merge | 702 | 292 | 58% |
| Refactor callback to async/await | 387 | 301 | 22% |
| Architecture: microservices vs monolith | 446 | 310 | 30% |
| Review PR for security issues | 678 | 398 | 41% |
| Docker multi-stage build | 1042 | 290 | 72% |
| Debug PostgreSQL race condition | 1200 | 232 | 81% |
| Implement React error boundary | 3454 | 456 | 87% |
| **Average** | **1214** | **294** | **65%** |

*Range: 22%–87% savings across prompts.*
<!-- BENCHMARK-TABLE-END -->

> [!IMPORTANT]
> Caveman only affects output tokens — thinking/reasoning tokens are untouched. Caveman no make brain smaller. Caveman make *mouth* smaller. Biggest win is **readability and speed**, cost savings are a bonus.

### Science back caveman up

A March 2026 paper ["Brevity Constraints Reverse Performance Hierarchies in Language Models"](https://arxiv.org/abs/2604.00025) found that constraining large models to brief responses **improved accuracy by 26 percentage points** on certain benchmarks and completely reversed performance hierarchies. Verbose not always better. Sometimes less word = more correct.

## Install

```bash
npx skills add JuliusBrussee/caveman
```

`npx skills` supports 40+ agents — Claude Code, GitHub Copilot, Cursor, Windsurf, Cline, and more. To install for a specific agent:

```bash
npx skills add JuliusBrussee/caveman -a cursor
npx skills add JuliusBrussee/caveman -a copilot
npx skills add JuliusBrussee/caveman -a cline
npx skills add JuliusBrussee/caveman -a windsurf
```

Or with Claude Code plugin system:

```bash
claude plugin marketplace add JuliusBrussee/caveman
claude plugin install caveman@caveman
```

Codex:

1. Clone repo
2. Open Codex in repo
3. Run `/plugins`
4. Search `Caveman`
5. Install plugin

Install once. Use in all sessions after that.

One rock. That it.

## Usage

Trigger with:
- `/caveman` or Codex `$caveman`
- "talk like caveman"
- "caveman mode"
- "less tokens please"

Stop with: "stop caveman" or "normal mode"

### Intensity Levels

Sometimes full caveman too much. Sometimes not enough. Now you pick:

| Level | Trigger | What it do |
|-------|---------|------------|
| **Lite** | `/caveman lite` or `$caveman lite` | Drop filler, keep grammar. Professional but no fluff |
| **Full** | `/caveman full` or `$caveman full` | Default caveman. Drop articles, fragments, full grunt |
| **Ultra** | `/caveman ultra` or `$caveman ultra` | Maximum compression. Telegraphic. Abbreviate everything |

Level stick until you change it or session end.

## What Caveman Do

| Thing | Caveman Do? |
|-------|------------|
| English explanation | 🪨 Caveman smash filler words |
| Code blocks | ✍️ Write normal (caveman not stupid) |
| Technical terms | 🧠 Keep exact (polymorphism stay polymorphism) |
| Error messages | 📋 Quote exact |
| Git commits & PRs | ✍️ Write normal |
| Articles (a, an, the) | 💀 Gone |
| Pleasantries | 💀 "Sure I'd be happy to" is dead |
| Hedging | 💀 "It might be worth considering" extinct |

## Why

```
┌─────────────────────────────────────┐
│  TOKENS SAVED          ████████ 75% │
│  TECHNICAL ACCURACY    ████████ 100%│
│  SPEED INCREASE        ████████ ~3x │
│  VIBES                 ████████ OOG │
└─────────────────────────────────────┘
```

- **Faster response** — less token to generate = speed go brrr
- **Easier to read** — no wall of text, just the answer
- **Same accuracy** — all technical info kept, only fluff removed ([science say so](https://arxiv.org/abs/2604.00025))
- **Save money** — ~71% less output token = less cost
- **Fun** — every code review become comedy

## How It Work

Caveman not dumb. Caveman **efficient**.

Normal LLM waste token on:
- "I'd be happy to help you with that" (8 wasted tokens)
- "The reason this is happening is because" (7 wasted tokens)
- "I would recommend that you consider" (7 wasted tokens)
- "Sure, let me take a look at that for you" (10 wasted tokens)

Caveman say what need saying. Then stop.

## Caveman Compress

Caveman makes Claude *speak* with fewer tokens. **Caveman Compress** makes Claude *read* fewer tokens.

Your `CLAUDE.md` loads on **every session start**. A 1000-token project memory file costs you tokens every single time you open a project. Caveman Compress rewrites those files into caveman-speak so Claude reads less — without you losing the human-readable original.

```
/caveman-compress CLAUDE.md
```

```
CLAUDE.md          ← compressed (Claude reads this every session — fewer tokens)
CLAUDE.original.md ← human-readable backup (you read and edit this)
```

### How it works

A Python pipeline that shells out to `claude --print` for the actual compression, then validates the result locally — no tokens wasted on checking.

```
detect file type (local)  →  compress with Claude (1 call)  →  validate (local)
                                                                    ↓
                                                              if errors: targeted fix (1 call, cherry-pick only)
                                                                    ↓
                                                              retry up to 2×, restore original on failure
```

### What's preserved exactly

Code blocks, inline code, URLs, file paths, commands, headings, table structure, dates, version numbers — anything technical passes through untouched. Only natural language prose gets compressed.

### Compress benchmarks

| File | Original | Compressed | Saved |
|------|----------:|----------:|------:|
| `claude-md-preferences.md` | 706 | 285 | **59.6%** |
| `project-notes.md` | 1145 | 535 | **53.3%** |
| `claude-md-project.md` | 1122 | 687 | **38.8%** |
| `todo-list.md` | 627 | 388 | **38.1%** |
| `mixed-with-code.md` | 888 | 574 | **35.4%** |
| **Average** | **898** | **494** | **45%** |

### Full-circle token savings

| Tool | What it cuts | Savings |
|------|-------------|---------|
| **caveman** | Output tokens (Claude's responses) | ~65% |
| **caveman-compress** | Input tokens (memory files loaded per session) | ~45% |
| **Both together** | The whole conversation | Output + input both shrunk |

See the full [caveman-compress README](caveman-compress/README.md) for install, usage, and validation details.

## Star This Repo

If caveman save you mass token, mass money — leave mass star. ⭐

[![Star History Chart](https://api.star-history.com/svg?repos=JuliusBrussee/caveman&type=Date)](https://star-history.com/#JuliusBrussee/caveman&Date)

## Also by Julius Brussee

- **[Blueprint](https://github.com/JuliusBrussee/blueprint)** — specification-driven development for Claude Code. Natural language → blueprints → parallel builds → working software.
- **[Revu](https://github.com/JuliusBrussee/revu-swift)** — local-first macOS study app with FSRS spaced repetition, decks, exams, and study guides. [revu.cards](https://revu.cards)

## License

MIT — free like mass mammoth on open plain.
