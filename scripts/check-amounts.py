"""Flag numeric amount fields that exceed a plausibility ceiling (catches copy-paste errors)."""
import json
import sys
import pathlib
import glob
import re

PLAUSIBLE_MAX_SAR = 1_000_000

failures = []
fee_pattern = re.compile(r'"amount"\s*:\s*(\d+(?:\.\d+)?)')

for path in sorted(glob.glob("data/*.json")):
    text = pathlib.Path(path).read_text()
    for match in fee_pattern.finditer(text):
        val = float(match.group(1))
        if val > PLAUSIBLE_MAX_SAR:
            failures.append(
                f"{path}: amount {val} exceeds plausibility ceiling "
                f"({PLAUSIBLE_MAX_SAR} SAR) — verify this is correct"
            )

if failures:
    print("AMOUNT PLAUSIBILITY WARNINGS:")
    for f in failures:
        print(f)
    sys.exit(1)

print("Amount plausibility OK")
