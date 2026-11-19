---
name: text-tools
description: Summarize text, extract keywords, check readability, and remove duplicate lines, offline, with Python. Use when the user or agent wants to shorten, measure, or clean up a text file.
---

# Text Tools

Work with plain text without a cloud AI. Get an extractive summary,
find the most frequent keywords, measure reading difficulty, or remove
duplicate lines. No cloud, no upload. Files stay local.

## When to use

- "Summarize this article in 3 sentences"
- "What are the keywords in this text?"
- "Is this easy to read?"
- "Remove the duplicate lines from this file"

## Workflow

1. Check the file is plain text. If it is not, say so and stop.
2. Summarize — picks the most representative sentences, in original order:
   ```sh
   python tools/texttool.py summarize article.txt --sentences 3
   ```
3. Find keywords — most frequent words, stopwords removed:
   ```sh
   python tools/texttool.py keywords article.txt --top 10
   ```
4. Check readability — Flesch reading ease score and level:
   ```sh
   python tools/texttool.py readability article.txt
   ```
5. Remove duplicate lines — keeps the first occurrence:
   ```sh
   python tools/texttool.py dedupe notes.txt clean.txt
   ```
6. Report the result. For summaries, quote the chosen sentences exactly — do not rewrite them.

## Examples

**A 3-sentence summary of an article**
```sh
python tools/texttool.py summarize article.txt --sentences 3
# Summary (3 of 24 sentences):
# - Good writing is clear writing.
```

**What is this text about?**
```sh
python tools/texttool.py keywords article.txt --top 5
# Top 5 keywords:
#   writing: 9 (4.2%)
```

**Clean up a messy notes file**
```sh
python tools/texttool.py dedupe notes.txt clean.txt
# Deduped: removed 6 duplicate line(s). Saved: clean.txt
```

## Rules

- Never overwrite the input file. Always write to a new output file.
- Summaries are extractive: they quote sentences from the text, they do not write new ones. Say so if the user expects a rewritten summary.
- Keywords are frequency-based, not semantic — a rare but important word will not appear.
- Readability is an estimate (Flesch score). Report the number and the level, not a verdict on the writing.
- Dedupe is case-insensitive by default; use `--case-sensitive` when case matters.
