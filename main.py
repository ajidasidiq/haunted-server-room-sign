#!/usr/bin/env python3
"""Funniest Sign on a Haunted Server Room Door.

Writes one funny sign line to /output/entry.txt for the make.fun bounty
u-eager-stork-81-9647-funniest-sign-on-a-haunted-ab1d019a.

The sign: a deadpan facilities notice for the door of a haunted server room.
The joke lands on the collision of IT life and the supernatural -- the ghost
is not the problem, he is the only one left who knows the root password, so
exorcising him would be an operational outage, not a haunting fix.
"""

import os

SIGN = "Do not exorcise the ghost in Rack 7. He is the only one who knows the root password."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    if not 1 <= len(SIGN) <= 120:
        raise ValueError(f"sign must be 1-120 characters, got {len(SIGN)}")
    if not SIGN.strip():
        raise ValueError("sign must not be only whitespace")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(SIGN)


if __name__ == "__main__":
    main()
