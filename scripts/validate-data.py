#!/usr/bin/env python3
"""
Validation script for Invest Gate KSA datasets.

Runs structural validation (JSON Schema) and semantic checks
(cross-file ID parity, source completeness, placeholder discipline).

Usage:
    python scripts/validate-data.py

Requirements:
    pip install jsonschema>=3.2.0
    # or:
    pip install -r scripts/requirements.txt

Exit codes:
    0  all checks passed
    1  one or more checks failed
"""

import json
import os
import sys

try:
    from jsonschema import Draft7Validator
except ImportError:
    print("ERROR: 'jsonschema' is required but not installed.")
    print("       Run: pip install jsonschema>=3.2.0")
    print("       Or:  pip install -r scripts/requirements.txt")
    sys.exit(1)


# ── Paths ─────────────────────────────────────────────────────────────────────

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SCHEMA_PATH = os.path.join(ROOT, "schemas", "business-structures.schema.json")
EN_PATH     = os.path.join(ROOT, "data", "business-structures.en.json")
AR_PATH     = os.path.join(ROOT, "data", "business-structures.ar.json")


# ── I/O helpers ───────────────────────────────────────────────────────────────

def load_json(path, label):
    """Load and parse a JSON file. Returns None and prints an error on failure."""
    try:
        with open(path, encoding="utf-8") as fh:
            return json.load(fh)
    except FileNotFoundError:
        print(f"  FAIL  {label}: file not found — {path}")
        return None
    except json.JSONDecodeError as exc:
        print(f"  FAIL  {label}: invalid JSON — {exc}")
        return None


def section(title):
    print(f"\n{title}")
    print("─" * len(title))


def result(ok, name, detail=""):
    tag = "PASS" if ok else "FAIL"
    suffix = f"  ({detail})" if detail else ""
    print(f"  {tag}  {name}{suffix}")
    return ok


# ── Per-file checks ───────────────────────────────────────────────────────────

def check_schema(data, schema, label):
    """Validate a dataset against the JSON Schema (Draft 7)."""
    validator = Draft7Validator(schema)
    errors = sorted(validator.iter_errors(data), key=lambda e: list(e.absolute_path))
    if errors:
        print(f"  FAIL  JSON Schema ({len(errors)} error(s))")
        for err in errors:
            path = " > ".join(str(p) for p in err.absolute_path) or "(root)"
            print(f"        [{path}] {err.message}")
        return False
    return result(True, "JSON Schema", f"{len(data.get('data', []))} entries validated")


def check_sources_not_empty(data):
    """Every entry must have at least one official source."""
    bad = [
        e["id"] for e in data.get("data", [])
        if not e.get("official_sources")
    ]
    if bad:
        print(f"  FAIL  official_sources not empty")
        for entry_id in bad:
            print(f"        Entry '{entry_id}': official_sources is empty")
        return False
    return result(True, "official_sources not empty")


def check_placeholders_when_draft(data):
    """Entries with verification_status 'draft' must declare at least one placeholder."""
    bad = [
        e["id"] for e in data.get("data", [])
        if e.get("verification_status") == "draft" and not e.get("placeholders")
    ]
    if bad:
        print(f"  FAIL  placeholders present when draft")
        for entry_id in bad:
            print(f"        Entry '{entry_id}': status is 'draft' but placeholders is empty")
        return False
    draft_count = sum(
        1 for e in data.get("data", [])
        if e.get("verification_status") == "draft"
    )
    return result(True, "placeholders present when draft", f"{draft_count} draft entries checked")


def run_file_checks(label, data, schema):
    """Run all per-file checks. Returns (passes, fails)."""
    checks = [
        check_schema(data, schema, label),
        check_sources_not_empty(data),
        check_placeholders_when_draft(data),
    ]
    passes = sum(1 for c in checks if c)
    fails  = sum(1 for c in checks if not c)
    return passes, fails


# ── Cross-file checks ─────────────────────────────────────────────────────────

def check_id_parity(en_data, ar_data):
    """Both files must have the same IDs in the same order."""
    en_ids = [e["id"] for e in en_data.get("data", [])]
    ar_ids = [e["id"] for e in ar_data.get("data", [])]

    if en_ids == ar_ids:
        return result(True, "ID parity", f"{len(en_ids)} IDs match in correct order")

    # Diagnose the mismatch
    en_set, ar_set = set(en_ids), set(ar_ids)
    only_en = sorted(en_set - ar_set)
    only_ar = sorted(ar_set - en_set)
    same_set_diff_order = (en_set == ar_set)

    print("  FAIL  ID parity")
    if only_en:
        print(f"        IDs only in EN: {only_en}")
    if only_ar:
        print(f"        IDs only in AR: {only_ar}")
    if same_set_diff_order:
        print(f"        IDs match but order differs")
        print(f"        EN order: {en_ids}")
        print(f"        AR order: {ar_ids}")
    return False


def run_cross_file_checks(en_data, ar_data):
    """Run all cross-file checks. Returns (passes, fails)."""
    checks = [
        check_id_parity(en_data, ar_data),
    ]
    passes = sum(1 for c in checks if c)
    fails  = sum(1 for c in checks if not c)
    return passes, fails


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    print("Invest Gate KSA — Dataset Validation")
    print("=" * 45)

    section("Loading files")
    schema  = load_json(SCHEMA_PATH, "schemas/business-structures.schema.json")
    en_data = load_json(EN_PATH,     "data/business-structures.en.json")
    ar_data = load_json(AR_PATH,     "data/business-structures.ar.json")

    if not all([schema, en_data, ar_data]):
        print("\nFATAL: One or more required files could not be loaded. Aborting.")
        sys.exit(1)

    print("  OK    All files loaded")

    total_passes = total_fails = 0

    section("data/business-structures.en.json")
    p, f = run_file_checks("EN", en_data, schema)
    total_passes += p
    total_fails  += f

    section("data/business-structures.ar.json")
    p, f = run_file_checks("AR", ar_data, schema)
    total_passes += p
    total_fails  += f

    section("Cross-file consistency")
    p, f = run_cross_file_checks(en_data, ar_data)
    total_passes += p
    total_fails  += f

    print(f"\n{'=' * 45}")
    print(f"Checks passed: {total_passes}   Checks failed: {total_fails}")
    if total_fails == 0:
        print("RESULT: All checks passed.")
        sys.exit(0)
    else:
        print(f"RESULT: {total_fails} check(s) failed. See above for details.")
        sys.exit(1)


if __name__ == "__main__":
    main()
