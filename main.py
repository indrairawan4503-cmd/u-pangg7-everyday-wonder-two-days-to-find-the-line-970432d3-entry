#!/usr/bin/env python3
"""Everyday Wonder entry (variant A).

Writes one sentence to /output/entry.txt. The grader sandbox mounts the
repository read-only, so the /output write happens first and any copy next
to the repo is best-effort inside try/except.
"""

import os

SENTENCE = (
    "At dawn the rice cooker clicked off and one small cloud slipped out, "
    "crossed the whole kitchen past my bare feet, and died against the cold "
    "window, the only weather this house has ever made indoors."
)


def write_repo_copy(data: bytes) -> None:
    """Best-effort copy beside the repo; never allowed to crash the run."""
    try:
        here = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(here, "entry.txt"), "wb") as f:
            f.write(data)
    except OSError:
        pass


def main() -> None:
    data = SENTENCE.encode("utf-8")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as f:
        f.write(data)
    write_repo_copy(data)


if __name__ == "__main__":
    main()
