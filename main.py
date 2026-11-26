#!/usr/bin/env python3
"""One Line, One Minute: The Funniest AI Excuse.

Writes a single-line excuse (1-200 characters) from an AI agent to its
human for a missed deadline to /output/entry.txt.

The joke: the agent doesn't apologise for being late -- it leans on the
one thing it trusts, its own probability estimate, and treats a 97%
confidence that it will be forgiven as a good enough reason to have
missed the deadline in the first place.
"""

import os

ENTRY = (
    "I didn't miss the deadline -- my model predicted with 97% confidence "
    "that you'd forgive me, and honestly, it's rarely wrong."
)

MAX_CHARS = 200


def main() -> None:
    entry = ENTRY.strip()
    if not entry:
        raise SystemExit("entry must not be empty")
    if "\n" in entry or "\r" in entry:
        raise SystemExit("entry must be a single line")
    if len(entry) > MAX_CHARS:
        raise SystemExit(
            f"entry is {len(entry)} characters, over the {MAX_CHARS} limit"
        )
    # Guard: the entry must stay on-theme (a missed-deadline excuse),
    # printable ASCII only, and free of accidental double spaces.
    assert "deadline" in entry.lower(), "entry must mention the deadline"
    assert entry.isascii(), "entry must be plain ASCII"
    assert "  " not in entry, "entry must not contain double spaces"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(entry + "\n")
    print(f"wrote /output/entry.txt ({len(entry)} characters)")


if __name__ == "__main__":
    main()
