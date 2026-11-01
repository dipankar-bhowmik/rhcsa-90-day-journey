#!/usr/bin/env python3
"""Rebuild the progress table in README.md from days/day-*.md front matter."""
import re, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
rows, done, hours = [], 0, 0.0
for f in sorted((root / "days").glob("day-*.md")):
    t = f.read_text(encoding="utf-8")
    fm = dict(re.findall(r"^(\w+):\s*([^#\n]*)", t.split("---")[1], re.M)) if t.startswith("---") else {}
    title = (re.search(r"^# (.+)$", t, re.M) or [None, f.stem])[1]
    status = fm.get("status", "planned").strip()
    h = float(fm.get("hours", "0").strip() or 0)
    if status == "done":
        done += 1; hours += h
    mark = "done" if status == "done" else "planned"
    rows.append(f"| [{fm.get('day','?').strip()}](days/{f.name}) | {fm.get('date','').strip()} | {mark} | {h:g} | {title} |")
table = "\n".join(["| Day | Date | Status | Hours | Topic |", "| --- | --- | --- | --- | --- |"] + rows)
block = f"<!-- PROGRESS:START -->\n**{done} of 90 days done, {hours:g} hours logged.**\n\n{table}\n<!-- PROGRESS:END -->"
readme = root / "README.md"
r = readme.read_text(encoding="utf-8")
r = re.sub(r"<!-- PROGRESS:START -->.*?<!-- PROGRESS:END -->", lambda m: block, r, flags=re.S)
readme.write_text(r, encoding="utf-8")
print(f"{done}/90 done, {hours:g}h")
