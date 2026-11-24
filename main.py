#!/usr/bin/env python3
"""One-Line Roast: The Gadget You Use Every Day - make.fun entry.

Reads the roast line from line.txt (shipped beside this file) and writes it
verbatim to the program output: $MAKEFUN_OUTPUT_DIR/entry.txt when that
environment variable is set, else /output/entry.txt.

Standard library only; deterministic - the same input always produces the
same output bytes.
"""

import os
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
LINE_FILE = HERE / "line.txt"
MAX_CHARS = 200


def load_line() -> str:
    raw = LINE_FILE.read_bytes()
    text = raw.decode("utf-8")  # strict: invalid UTF-8 raises
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"line must be 1..{MAX_CHARS} characters, got {len(text)}")
    if not text.strip():
        raise ValueError("line must not be only whitespace")
    return text


def write_entry(out_dir: Path, data: bytes) -> None:
    """Write data to out_dir/entry.txt atomically and verify the bytes."""
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    tmp = out_dir / ".entry.txt.tmp"
    tmp.write_bytes(data)
    os.replace(tmp, target)
    if target.read_bytes() != data:
        raise OSError("round-trip verification failed: entry.txt bytes differ")


def main() -> int:
    data = load_line().encode("utf-8")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    write_entry(out_dir, data)
    return 0


if __name__ == "__main__":
    sys.exit(main())
