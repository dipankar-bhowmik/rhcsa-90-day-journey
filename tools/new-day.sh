#!/usr/bin/env bash
# Usage: tools/new-day.sh 12   -> creates days/day-012.md with the right date
set -euo pipefail
cd "$(dirname "$0")/.."
n="${1:?day number}"
start="$(cat START_DATE)"
date_str="$(date -d "$start +$((n-1)) days" +%F)"
f="days/day-$(printf '%03d' "$n").md"
[ -e "$f" ] && { echo "$f exists"; exit 1; }
sed -e "s/{{DAY}}/$n/g" -e "s/{{DATE}}/$date_str/g" templates/day.md > "$f"
echo "created $f"
