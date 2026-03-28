#!/usr/bin/env python3
from __future__ import annotations

import sys


MESSAGE = """\
This repository no longer rewrites README catalog links automatically from this script.

Canonical links are now maintained directly in README.md and validated by:
  python3 scripts/validate_governance_artifacts.py

If bulk catalog regeneration is needed in the future, reintroduce a dedicated mapping utility in an isolated branch with the numbered path structure as the source of truth.
"""


def main() -> int:
    sys.stdout.write(MESSAGE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
