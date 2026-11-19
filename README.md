# agent-text-skills

> **Agent Skills for text — summarize, extract keywords, check readability, and remove duplicate lines. Offline, stdlib-only Python.**

**1 skill · 1 CLI · 0 dependencies · 100% offline**

[![GitHub stars](https://img.shields.io/github/stars/megaartaiking-cmd/agent-text-skills?style=social)](https://github.com/megaartaiking-cmd/agent-text-skills/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/python-3.9%2B-blue.svg)](tools/texttool.py)

AI agents are great at code, but plain text still means pasting a whole article into a chat to get a summary, or writing a one-off script to find duplicates. This repo fixes that gap: a small Agent Skill (SKILL.md) plus a tiny Python CLI that summarizes text, extracts keywords, checks readability, and removes duplicate lines — in the terminal, on the user's own PC.

Works with Claude Code, Cursor, GitHub Copilot, Codex, Gemini CLI, and any agent that reads SKILL.md files.

## Why this exists

Agent Skills are the fastest-growing category on GitHub — small, composable skill bundles, one job per skill, install in one step. Text is what agents read most, and there is no small, offline, agent-native way to shorten it, measure it, or clean it up without sending it to a cloud service.

This one is:

- **Agent-native** — a skill in the open SKILL.md format, one job, clear rules
- **Offline** — no upload, no cloud, files never leave the PC
- **Lightweight** — stdlib-only Python, no pip install, no heavy app
- **Honest** — summaries are extractive: they quote sentences from the text, they do not write new ones

## Skills

| Skill | What it does | Command |
|---|---|---|
| `text-tools` | Summarize, keywords, readability, dedupe | `texttool.py` |

The skill lives in `skills/text-tools/SKILL.md` — copy that folder into your agent's skills folder, or point your agent at this repo.

## Quick start

```sh
git clone https://github.com/megaartaiking-cmd/agent-text-skills.git
cd agent-text-skills

# 1. Summarize the sample text in 3 sentences
python tools/texttool.py summarize examples/sample.txt --sentences 3

# 2. Top 10 keywords
python tools/texttool.py keywords examples/sample.txt --top 10

# 3. Reading ease score
python tools/texttool.py readability examples/sample.txt
```

No installation needed — Python 3.9+ is the only requirement.

## Usage

```sh
# Extractive summary: top N sentences, in original order
python tools/texttool.py summarize article.txt --sentences 3

# Most frequent words, stopwords removed
python tools/texttool.py keywords article.txt --top 10

# Flesch reading ease score and level
python tools/texttool.py readability article.txt

# Remove duplicate lines, keep the first occurrence
python tools/texttool.py dedupe notes.txt clean.txt
```

See [examples/commands.md](examples/commands.md) for all commands, and [examples/sample.txt](examples/sample.txt) for a small file to try them on.

## How it works

1. You (or your agent) describe the job in plain words: "summarize this in 3 sentences".
2. The skill in `skills/text-tools/` tells the agent the exact workflow, the command to run, and the rules — never overwrite the original, always write to a new file.
3. `tools/texttool.py` (stdlib-only Python) does the work locally and reports the result.
4. Nothing is uploaded. The work happens on your PC.

## Works with

- Claude Code
- Cursor
- GitHub Copilot
- Codex
- Gemini CLI
- Any agent that reads Agent Skills (SKILL.md)

Copy `skills/text-tools/` into your agent's skills directory, or ask your agent to read the SKILL.md file in this repo directly.

## FAQ

**Does it need the internet?**
No. After `git clone`, everything runs offline.

**Is the summary written by AI?**
No. It is extractive — it picks the most representative sentences from the text and quotes them exactly. It does not write new sentences.

**What are keywords here?**
The most frequent words, with common stopwords removed. They are frequency-based, not semantic — a rare but important word will not appear.

**What is the readability score?**
The Flesch reading ease score (0–100). Higher means easier to read. The tool reports the number and the level, not a verdict on the writing.

**Will it run on an old PC?**
Yes — that is the point. It is a small Python script with no dependencies.

**Can I add a skill?**
Yes — copy `skills/text-tools/` as a template, write a SKILL.md with a clear name, description, workflow, and rules, and open a pull request.

## Contributing

Issues and pull requests are welcome. Keep skills small, one job per skill, with a tested command in `tools/texttool.py`. Please do not add dependencies — stdlib only.

## License

MIT — see [LICENSE](LICENSE).

## More Agent Skills

More offline Agent Skills by the same author — one focused skill per repo:

- [agent-audio-skills](https://github.com/megaartaiking-cmd/agent-audio-skills) — Trim podcasts, normalize volume, extract audio from video
- [agent-csv-skills](https://github.com/megaartaiking-cmd/agent-csv-skills) — Clean, filter, summarize CSVs; convert to JSON and Markdown
- [agent-json-skills](https://github.com/megaartaiking-cmd/agent-json-skills) — Validate, format, flatten, query, and diff JSON
- [agent-markdown-skills](https://github.com/megaartaiking-cmd/agent-markdown-skills) — Markdown to HTML, table of contents, link check, word count
- [agent-git-skills](https://github.com/megaartaiking-cmd/agent-git-skills) — Commit messages, changelogs, repo health, branch cleanup
- [agent-file-skills](https://github.com/megaartaiking-cmd/agent-file-skills) — Organize folders, find duplicates, batch rename
- [agent-sql-skills](https://github.com/megaartaiking-cmd/agent-sql-skills) — Explore SQLite, run queries, export to CSV
- [agent-video-skills](https://github.com/megaartaiking-cmd/agent-video-skills) — Edit video offline — trim, make Shorts, add titles, colour-grade
- [LiteCut Pro](https://github.com/megaartaiking-cmd/LIGHT-CUT-VIDEO-EDITOR) — lightweight offline video editor for Windows 10

---

**Keywords:** agent skills, AI agent text, text summarizer, keyword extractor, readability checker, dedupe lines, Claude Code skills, Cursor skills, offline text tool, Python text CLI
