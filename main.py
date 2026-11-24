#!/usr/bin/env python3
"""Entry for u-aldy998-the-one-line-cat-joke-that-lands-a7b18262.

Writes a single one-line cat joke to entry.txt in MAKEFUN_OUTPUT_DIR.
"""
import os

ENTRY = (
    "My cat keeps a ledger: 4,217 times I opened the fridge and gave her "
    "nothing, and at 3 a.m. she collects the debt by walking across my face."
)


def main():
    # Gate: 1-200 chars, single line, non-whitespace (per competition.yaml).
    assert 1 <= len(ENTRY) <= 200, f"entry length {len(ENTRY)} out of gate"
    assert "\n" not in ENTRY and ENTRY.strip(), "entry must be one line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
