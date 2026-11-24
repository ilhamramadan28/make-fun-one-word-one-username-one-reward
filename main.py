#!/usr/bin/env python3
"""Write ilham's make.fun username to /output/entry.txt (one word, <=30 chars)."""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.txt")
DEST = "/output/entry.txt"


def main():
    with open(SRC, "r", encoding="utf-8") as f:
        text = f.read()
    assert 1 <= len(text) <= 30, "entry must be 1-30 chars"
    assert text.strip(), "entry must not be only whitespace"
    assert " " not in text and "\n" not in text, "entry must be a single word"
    os.makedirs(os.path.dirname(DEST), exist_ok=True)
    shutil.copyfile(SRC, DEST)
    os.chmod(DEST, 0o644)
    with open(SRC, "rb") as a, open(DEST, "rb") as b:
        assert a.read() == b.read(), "copy mismatch"


if __name__ == "__main__":
    main()
