"""Verify that EN and AR dataset files have identical entry IDs in the same order."""
import json
import sys
import pathlib

PAIRS = [
    ("data/business-structures.en.json", "data/business-structures.ar.json"),
    ("data/investment-licenses.en.json",  "data/investment-licenses.ar.json"),
    ("data/sources.en.json",              "data/sources.ar.json"),
    ("data/sectors.en.json",              "data/sectors.ar.json"),
    ("data/authority-relationships.en.json", "data/authority-relationships.ar.json"),
    ("data/setup-flows.en.json",          "data/setup-flows.ar.json"),
    ("data/source-gaps.en.json",          "data/source-gaps.ar.json"),
]

failures = []

for en_path, ar_path in PAIRS:
    if not pathlib.Path(en_path).exists() or not pathlib.Path(ar_path).exists():
        continue
    en_ids = [e["id"] for e in json.loads(pathlib.Path(en_path).read_text())["data"]]
    ar_ids = [e["id"] for e in json.loads(pathlib.Path(ar_path).read_text())["data"]]
    if en_ids != ar_ids:
        failures.append(
            f"{en_path} / {ar_path}: ID mismatch\n  EN: {en_ids}\n  AR: {ar_ids}"
        )

if failures:
    print("BILINGUAL PARITY FAILURES:")
    for f in failures:
        print(f)
    sys.exit(1)

print(f"Bilingual parity OK ({len(PAIRS)} pairs checked)")
