"""Monday Morning Punchlines: one joke about Monday mornings.

Writes one single-line joke to /output/entry.txt (UTF-8,
1-200 characters). The joke is about Monday morning itself: the bed
files for custody and wins, so getting up is legally impossible --
case closed. Setup and punch land inside the one line, in one breath.
Standard library only.
"""

import os

LINE = (
    "Monday morning: my bed filed for custody of me, "
    "and the judge ruled in its favor -- case closed, I'm not getting up."
)

MIN_CHARS = 1
MAX_CHARS = 200


def char_count(text):
    return len(text)


def check(text):
    chars = char_count(text)
    if not MIN_CHARS <= chars <= MAX_CHARS:
        raise SystemExit(
            "char count %d outside %d-%d" % (chars, MIN_CHARS, MAX_CHARS)
        )
    if not text.strip():
        raise SystemExit("entry is only whitespace")
    if "\n" in text.strip():
        raise SystemExit("entry must be a single line")
    lowered = text.lower()
    if "monday" not in lowered:
        raise SystemExit("joke must be about Monday")
    for worn in ("i hate mondays", "coffee", "snooze", "alarm"):
        if worn in lowered:
            raise SystemExit("worn Monday cliche, rewrite: %r" % worn)
    if "bed" not in lowered and "judge" not in lowered:
        raise SystemExit("line must carry the custody twist")
    return chars


def main():
    chars = check(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(LINE + "\n")
    print("wrote /output/entry.txt: %d chars" % chars)


if __name__ == "__main__":
    main()
