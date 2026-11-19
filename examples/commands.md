# Example commands

```sh
# Summarize the sample text in 3 sentences
python tools/texttool.py summarize examples/sample.txt --sentences 3

# Summarize in 2 sentences
python tools/texttool.py summarize examples/sample.txt --sentences 2

# Top 10 keywords
python tools/texttool.py keywords examples/sample.txt --top 10

# Top 5 keywords
python tools/texttool.py keywords examples/sample.txt --top 5

# Flesch reading ease score and level
python tools/texttool.py readability examples/sample.txt

# Remove duplicate lines (keeps the first occurrence)
python tools/texttool.py dedupe examples/sample.txt clean.txt
```
