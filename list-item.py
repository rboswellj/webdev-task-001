#!/usr/bin/env python3

# Path to the vocabulary file (same directory as this script)
VOCAB_FILE = "vocabulary-list.txt"
VOCAB_TAGGED = "vocabulary-list-tagged.txt"

list_items = []

with open(VOCAB_FILE, "r", encoding="utf-8") as f:
    content = f.readlines()
    for line in content:
        stripped_line = line.strip()
        if stripped_line:  # Only add non-empty lines
            split_line = line.split(':')
            list_items.append(f"<li><strong>{split_line[0]}:</strong> {split_line[1].strip()}</li>\n")

with open(VOCAB_TAGGED, "w", encoding="utf-8") as f2:
    f2.writelines(list_items)