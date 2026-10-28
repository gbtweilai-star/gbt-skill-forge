#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
PYTHONPATH=src python -m gbt_skill_forge info
PYTHONPATH=src python -m gbt_skill_forge check --payload '{}'
PYTHONPATH=src python -m gbt_skill_forge run   --payload '{}'
