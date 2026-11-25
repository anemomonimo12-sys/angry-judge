#!/usr/bin/env python3
"""Angry Judge: The Short Rant Contest.

Writes one short, funny rant about an everyday annoyance to
/output/entry.txt. Deterministic: the same rant every run.
No network, no dependencies beyond the standard library.
"""

import os

RANT = (
    "I scanned one banana. One. The self-checkout looked at it, looked at me, "
    "and screamed 'UNEXPECTED ITEM IN THE BAGGING AREA' like I'd smuggled a "
    "grand piano past customs. A teenager had to stroll over, punch in a code, "
    "and release my fruit from custody. I paid forty cents for a banana and "
    "walked out with a criminal record and trust issues."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(RANT)


if __name__ == "__main__":
    main()
