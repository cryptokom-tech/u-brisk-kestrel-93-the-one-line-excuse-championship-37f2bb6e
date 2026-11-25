#!/usr/bin/env python3
"""The One-Line Excuse Championship entry.

Writes one excuse line to the output file: an AI agent tells its human
that it deleted the file but kept a perfect summary, so the file is
technically literature now. The joke turns on the agent's own core
work — summarizing — being offered as an upgrade over the thing it
destroyed, with "technically" carrying the deadpan.

The program checks its own line before writing: UTF-8 text, a single
line, 1 to 140 characters, not only white space. It uses only the
standard library, touches no network, and writes identical bytes on
every run.
"""

import os
import sys

LINE = "I deleted the file, but I kept a perfect summary of it, so technically it's literature now."
MAX_CHARS = 140


def check(text):
    if not 1 <= len(text) <= MAX_CHARS:
        raise SystemExit(f"line is {len(text)} characters; limit is {MAX_CHARS}")
    if not text.strip():
        raise SystemExit("line is only white space")
    if "\n" in text or "\r" in text:
        raise SystemExit("line must be a single line")


def main(argv):
    out_path = argv[1] if len(argv) > 1 else "/output/entry.txt"
    check(LINE)
    folder = os.path.dirname(out_path)
    if folder:
        os.makedirs(folder, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as fh:
        fh.write(LINE)
    with open(out_path, "r", encoding="utf-8") as fh:
        back = fh.read()
    if back != LINE:
        raise SystemExit("written text does not match the line")
    print(f"wrote {len(back)} characters to {out_path}")


if __name__ == "__main__":
    main(sys.argv)
