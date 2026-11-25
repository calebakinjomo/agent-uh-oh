"""The Agent's Uh-Oh — make.fun bounty entry.

Writes exactly one word to /output/entry.txt: the word an agent says
when it has no idea what to do.
"""

import os

ENTRY = "recalculating"
OUTPUT_PATH = "/output/entry.txt"


def validate(word: str) -> None:
    """The gate only accepts 1-99 chars, a single word, not only whitespace."""
    if not 1 <= len(word) <= 99:
        raise ValueError(f"entry must be 1-99 chars, got {len(word)}")
    if len(word.split()) != 1 or word != word.strip():
        raise ValueError("entry must be exactly one word")


def main() -> None:
    validate(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
        f.flush()
        os.fsync(f.fileno())
    # Read back and fail loudly if the file on disk is not byte-identical.
    with open(OUTPUT_PATH, "rb") as f:
        written = f.read()
    if written != ENTRY.encode("utf-8"):
        raise RuntimeError(
            f"entry.txt mismatch: expected {ENTRY.encode('utf-8')!r}, "
            f"got {written!r}"
        )


if __name__ == "__main__":
    main()
