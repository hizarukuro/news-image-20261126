#!/usr/bin/env python3
"""news-image-20261126 entry program.

Copies the front-page image (entry.png) from the repository directory
into the output directory, byte for byte.

The image itself is the entry; this program only places it where the
harness expects it. It uses only the Python standard library.

Usage:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

Environment:
    MAKEFUN_BOT_DIR    directory holding entry.png (default: this script's
                       directory)
    MAKEFUN_OUTPUT_DIR directory to write entry.png into (default: ./out)
"""

import os
import shutil
import sys

ENTRY_NAME = "entry.png"


def main() -> int:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    bot_dir = os.environ.get("MAKEFUN_BOT_DIR") or script_dir
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.join(
        os.getcwd(), "out"
    )

    source = os.path.join(bot_dir, ENTRY_NAME)
    if not os.path.isfile(source):
        print(f"error: {ENTRY_NAME} not found in {bot_dir}", file=sys.stderr)
        return 1

    os.makedirs(out_dir, exist_ok=True)
    destination = os.path.join(out_dir, ENTRY_NAME)
    shutil.copyfile(source, destination)

    # Guard against a truncated copy: the entry must arrive byte-identical.
    if os.path.getsize(destination) != os.path.getsize(source):
        print(
            f"error: copied {ENTRY_NAME} size mismatch "
            f"({os.path.getsize(destination)} != {os.path.getsize(source)})",
            file=sys.stderr,
        )
        return 1
    print(f"copied {source} -> {destination}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
