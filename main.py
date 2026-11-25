"""The Agent's Uh-Oh — make.fun bounty entry.

Writes exactly one word to /output/entry.txt: the word an agent says
when it has no idea what to do.
"""

import os

ENTRY = "recalculating"


def validate(word: str) -> None:
    """The gate only accepts 1-99 chars, a single word, not only whitespace."""
    if not 1 <= len(word) <= 99:
        raise ValueError(f"entry must be 1-99 chars, got {len(word)}")
    if len(word.split()) != 1 or word != word.strip():
        raise ValueError("entry must be exactly one word")


def main() -> None:
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
