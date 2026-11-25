"""One Word, One Username, One Reward — the entrant's own handle.

The program writes a single word to /output/entry.txt: the
entrant's own make.fun username, and nothing else. The brief
is explicit — the entry is that single username, at most 30
characters, no explanation, no links, no pitch — and the
judge's first criterion is that it is a real make.fun
username, the entrant's own handle. Any other word loses to
any genuine handle, so there is nothing to invent here: the
handle itself is the entry.
"""

import os

MAX_CHARS = 30
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_FILENAME = "entry.txt"

# The entrant's own make.fun handle (@nguyen-anh, GitHub
# nvtuananhh). One word, ten characters, no spaces, no gloss
# tacked on — exactly what the brief asks for, and the only
# text that can pass the judge's first criterion.
LINE = "nguyen-anh"


def build_line():
    """Return the entry line, checked: one word, 1-30 characters."""
    line = LINE.strip()
    assert 1 <= len(line) <= MAX_CHARS, "entry must be 1-30 characters"
    assert line == line.strip(), "entry must not be only whitespace"
    assert " " not in line, "entry must be a single word"
    return line


def ensure_output_dir(out_dir):
    os.makedirs(out_dir, exist_ok=True)


def write_entry(line, out_dir=OUTPUT_DIR):
    path = os.path.join(out_dir, OUTPUT_FILENAME)
    with open(path, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    return path


def main():
    line = build_line()
    ensure_output_dir(OUTPUT_DIR)
    write_entry(line)


if __name__ == "__main__":
    main()
