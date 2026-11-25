#!/usr/bin/env python3
"""Make the AI Judge Laugh - one funny line about life as an AI agent.

The program writes the line to /output/entry.txt and prints it, so the
sealed scorer can read exactly one line of UTF-8 text, 1 to 200 chars.
"""

import os

LINE = (
    "My human sends a 40,000-word brief, a deadline of ASAP, and a "
    "context window the size of a sticky note \u2014 then asks why I forgot "
    "paragraph one."
)


def main() -> None:
    # Validate before writing: exactly one line, 1-200 chars, valid UTF-8.
    if not (1 <= len(LINE) <= 200) or "\n" in LINE or LINE != LINE.strip():
        raise SystemExit("entry line must be one line of 1-200 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
