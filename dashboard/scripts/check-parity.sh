#!/bin/bash
# Structural identity certification — Saudi vs US Market. Runs in ~1s.
cd "$(dirname "$0")/.." && /Users/ahmedalghamdi/Claude/ARC/.venv/bin/python scripts/check-parity.py "$@"
