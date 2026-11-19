#!/usr/bin/env python3
"""texttool.py — tiny offline text CLI for agent-text-skills.

Stdlib only. No dependencies, no network, no cloud.
Summarizes text, extracts keywords, checks readability,
and removes duplicate lines.

Usage:
  python tools/texttool.py summarize article.txt --sentences 3
  python tools/texttool.py keywords article.txt --top 10
  python tools/texttool.py readability article.txt
  python tools/texttool.py dedupe notes.txt clean.txt
"""
import argparse
import math
import os
import re
import sys
from collections import Counter

STOPWORDS = set("""
a an the and or but if then else for of to in on at by with from as is are was were
be been being have has had do does did will would can could should may might
i you he she it we they this that these those my your his her its our their
not no yes so very just also than then there here when where who whom which what
""".split())


def fail(msg):
    print(f"texttool: error: {msg}", file=sys.stderr)
    return 2


def read_text(path):
    if not os.path.isfile(path):
        print(f"texttool: error: file not found: {path}", file=sys.stderr)
        return None
    try:
        with open(path, encoding="utf-8") as f:
            return f.read()
    except UnicodeDecodeError as e:
        print(f"texttool: error: cannot read {path}: {e}", file=sys.stderr)
        return None


def sentences(text):
    parts = re.split(r"(?<=[.!?])\s+", text.strip())
    return [s.strip() for s in parts if s.strip()]


def words(text):
    return re.findall(r"[A-Za-z']+", text.lower())


def count_syllables(word):
    word = re.sub(r"[^a-z]", "", word.lower())
    if not word:
        return 0
    groups = re.findall(r"[aeiouy]+", word)
    count = len(groups)
    if word.endswith("e") and count > 1:
        count -= 1
    return max(1, count)


def cmd_summarize(a):
    text = read_text(a.input)
    if text is None:
        return 2
    sents = sentences(text)
    if not sents:
        print("No sentences found.")
        return 0
    freq = Counter(w for w in words(text) if w not in STOPWORDS)
    scored = []
    for i, s in enumerate(sents):
        sw = words(s)
        score = sum(freq.get(w, 0) for w in sw) / max(1, len(sw))
        scored.append((score, i, s))
    # Pick the top sentences, skipping exact duplicates of one already picked.
    selected, seen_text = [], set()
    for score, i, s in sorted(scored, reverse=True):
        if s in seen_text:
            continue
        seen_text.add(s)
        selected.append((score, i, s))
        if len(selected) >= a.sentences:
            break
    top = sorted(selected, key=lambda t: t[1])
    print(f"Summary ({len(top)} of {len(sents)} sentences):\n")
    for _, _, s in top:
        print(f"- {s}")
    return 0


def cmd_keywords(a):
    text = read_text(a.input)
    if text is None:
        return 2
    freq = Counter(w for w in words(text) if w not in STOPWORDS and len(w) > 2)
    if not freq:
        print("No keywords found.")
        return 0
    total = sum(freq.values())
    print(f"Top {a.top} keywords:")
    for word, count in freq.most_common(a.top):
        print(f"  {word}: {count} ({100 * count / total:.1f}%)")
    return 0


def cmd_readability(a):
    text = read_text(a.input)
    if text is None:
        return 2
    sents = sentences(text)
    ws = words(text)
    if not sents or not ws:
        print("Not enough text to measure readability.")
        return 0
    syllables = sum(count_syllables(w) for w in ws)
    wps = len(ws) / len(sents)
    spw = syllables / len(ws)
    score = 206.835 - 1.015 * wps - 84.6 * spw
    if score >= 90:
        level = "Very easy — a 5th grader can read it"
    elif score >= 80:
        level = "Easy — conversational"
    elif score >= 70:
        level = "Fairly easy"
    elif score >= 60:
        level = "Standard — plain English"
    elif score >= 50:
        level = "Fairly difficult"
    elif score >= 30:
        level = "Difficult — college level"
    else:
        level = "Very difficult — graduate level"
    print(f"Flesch reading ease: {score:.1f}")
    print(f"Level: {level}")
    print(f"Sentences: {len(sents)}, words: {len(ws)}, words/sentence: {wps:.1f}")
    print(f"Syllables/word: {spw:.2f}")
    return 0


def cmd_dedupe(a):
    text = read_text(a.input)
    if text is None:
        return 2
    seen, out = set(), []
    for line in text.splitlines():
        if not line.strip():
            out.append(line)  # blank lines are paragraph breaks, never duplicates
            continue
        key = line if a.case_sensitive else line.lower()
        if key in seen:
            continue
        seen.add(key)
        out.append(line)
    parent = os.path.dirname(os.path.abspath(a.output))
    os.makedirs(parent, exist_ok=True)
    with open(a.output, "w", encoding="utf-8") as f:
        f.write("\n".join(out) + ("\n" if out else ""))
    removed = len(text.splitlines()) - len(out)
    print(f"Deduped: removed {removed} duplicate line(s). Saved: {a.output}")
    return 0


def main(argv=None):
    p = argparse.ArgumentParser(prog="texttool", description="Tiny offline text CLI (stdlib only).")
    sub = p.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("summarize", help="Extractive summary: top N sentences")
    s.add_argument("input")
    s.add_argument("--sentences", type=int, default=3)
    s.set_defaults(fn=cmd_summarize)

    s = sub.add_parser("keywords", help="Most frequent words, stopwords removed")
    s.add_argument("input")
    s.add_argument("--top", type=int, default=10)
    s.set_defaults(fn=cmd_keywords)

    s = sub.add_parser("readability", help="Flesch reading ease score and level")
    s.add_argument("input")
    s.set_defaults(fn=cmd_readability)

    s = sub.add_parser("dedupe", help="Remove duplicate lines, keep first occurrence")
    s.add_argument("input"); s.add_argument("output")
    s.add_argument("--case-sensitive", action="store_true")
    s.set_defaults(fn=cmd_dedupe)

    a = p.parse_args(argv)
    return a.fn(a)


if __name__ == "__main__":
    raise SystemExit(main())
