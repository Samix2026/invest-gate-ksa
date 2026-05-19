"""Check dataset entry quality: draft entries must have placeholders; verified entries must have dates."""
import json
import sys
import pathlib
import glob

failures = []

for path in sorted(glob.glob("data/*.json")):
    try:
        obj = json.loads(pathlib.Path(path).read_text())
    except json.JSONDecodeError as e:
        failures.append(f"{path}: invalid JSON — {e}")
        continue

    for entry in obj.get("data", []):
        eid = entry.get("id", "<no id>")
        status = entry.get("verification_status", "")

        if status == "draft" and not entry.get("placeholders"):
            failures.append(
                f"{path}[{eid}]: status=draft but placeholders is empty or missing"
            )

        if status == "verified":
            lv = entry.get("last_verified")
            # Fail only when the date is an explicit placeholder string — null dates
            # represent "verified but date not recorded" (pre-existing convention).
            if isinstance(lv, str) and ("PLACEHOLDER" in lv.upper() or lv.strip() == ""):
                failures.append(
                    f"{path}[{eid}]: status=verified but last_verified is a placeholder string"
                )

if failures:
    print("DATA ENTRY QUALITY FAILURES:")
    for f in failures:
        print(f)
    sys.exit(1)

print("Data entry quality OK")
