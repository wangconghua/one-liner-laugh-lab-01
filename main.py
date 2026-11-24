#!/usr/bin/env python3
"""One-Liner Laugh Lab: the excuse a robot vacuum gives after eating a sock."""

import os

LINE = "The sock filed a complaint. I filed it under 'delicious.'"

OUT_PATH = "/output/entry.txt"


def main():
    # The gate wants UTF-8 text of 1 to 200 characters, not only whitespace,
    # a single line. The line is 57 characters, one line, deadpan and tight.
    # Also reject a trailing newline so the file holds exactly the line.
    if not (1 <= len(LINE) <= 200) or LINE.isspace() or "\n" in LINE or LINE != LINE.strip():
        raise ValueError("entry must be one line of 1 to 200 characters")
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
