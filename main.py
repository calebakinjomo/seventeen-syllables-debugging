#!/usr/bin/env python3
"""Seventeen Syllables of Debugging — make.fun bounty entry.

Writes one haiku about debugging (5-7-5 syllables, 77 characters)
to /output/entry.txt. Python 3 standard library only.

The haiku:
    Cursor blinks at three          (5)
    the log swears nothing is wrong (7)
    yet the bug just grins          (5)
"""

import os

HAIKU = """Cursor blinks at three
the log swears nothing is wrong
yet the bug just grins"""


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(HAIKU)


if __name__ == "__main__":
    main()
