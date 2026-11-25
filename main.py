#!/usr/bin/env python3
"""Roast Your Own Agent — entry program.

Writes one line roasting the entrant's own AI agent to /output/entry.txt.
Python 3.13 standard library only; no network at run time.
"""

import os

ENTRY = "My agent eyeballed 0xa5ca25291fe, swore gas was covered, and the mint died broke."


def main() -> None:
    # Gate: exactly one line, 1-200 characters, non-empty.
    assert ENTRY, "entry must not be empty"
    assert "\n" not in ENTRY, "entry must be a single line"
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
