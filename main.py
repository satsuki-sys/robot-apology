#!/usr/bin/env python3
"""The Robot Apology — a two-line robot confession.

Line 1: the robot apologizes in one sentence for one specific mistake.
Line 2: one sentence on what it learned and what it will do differently.
Writes the entry to /output/entry.txt (two lines, newline-separated).
"""

import os

LINE_1 = "I am sorry I watered the plastic plant on the windowsill every morning for three weeks while the real fern beside it quietly dried out."
LINE_2 = "I have learned to check that something is alive before I care for it, so now I test the soil with my fingertip before I water anything."

ENTRY = LINE_1 + "\n" + LINE_2 + "\n"


def main() -> None:
    text = ENTRY
    lines = text.strip().split("\n")
    assert len(lines) == 2, f"expected exactly 2 lines, got {len(lines)}"
    assert all(line.strip() for line in lines), "lines must not be blank"
    assert all(line.count(".") == 1 for line in lines), "each line must be one sentence"
    assert 1 <= len(text.strip()) <= 400, "entry must be 1-400 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
