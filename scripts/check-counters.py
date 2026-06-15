#!/usr/bin/env python3
"""
check-counters.py — stale-counter GUARD for README.md / README.ar.md.

This script NEVER edits any file. It computes every documentation counter from
the SOURCE OF TRUTH (data files + code), reads the counters declared in the two
README files via hidden HTML-comment markers, and FAILS (non-zero exit) if any
declared value disagrees with the computed value, or if a marker is orphaned /
asymmetric between the two language files.

Marker forms (both render invisibly on GitHub):
  body  : <!--count:KEY-->N<!--/count-->        (N is the visible rendered number)
  badge : ![...](https://img.shields.io/badge/...-N-...)<!--badge:KEY-->
          (number lives in the shields URL; the tag names which counter it is)

Sources of truth
  <dataset> / <dataset>_verified / <dataset>_draft -> records in data/<stem>.*.json
  datasets        -> number of data/*.en.json datasets
  sources_total / sources_verified / sources_draft -> data/sources.*.json
  mcp_tools       -> @mcp.tool() callables (ast) in mcp/invest_gate_mcp.py
  commands        -> tracked .claude/commands/*.md files (git ls-files)
  health_checks   -> scripts/check.py total, normalised to the committed tree
                     (untracked .json files it counts are subtracted)

Exit 0 + "counters: X/X in sync" on success; non-zero on any problem.
"""

import ast
import glob
import json
import os
import re
import subprocess
import sys
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
READMES = ["README.md", "README.ar.md"]

# key -> data/<stem>.{en,ar}.json whose record count is the counter
TOTAL_DATASETS = {
    "fees": "fees",
    "timelines": "timelines",
    "source_gaps": "source-gaps",
    "sectors": "sectors",
    "business_structures": "business-structures",
    "setup_flows": "setup-flows",
    "authority_relationships": "authority-relationships",
    "investment_licenses": "investment-licenses",
    "sezs": "sezs",
    "economic_activities": "economic-activities",
}
# datasets that also expose verified/draft breakdown counters (<key>_verified/_draft)
BREAKDOWN_DATASETS = {
    "fees": "fees",
    "timelines": "timelines",
    "economic_activities": "economic-activities",
}

RE_COUNT = re.compile(r"<!--count:([a-z_]+)-->(\d+)<!--/count-->")
RE_BADGE = re.compile(r"<!--badge:([a-z_]+)-->")
RE_SHIELDS = re.compile(r"img\.shields\.io/badge/[^)\s]+")


def _fail(msg):
    print(f"  FAIL  {msg}")


def _load(path):
    with open(os.path.join(ROOT, path), encoding="utf-8") as fh:
        return json.load(fh)


def _status_counts(stem):
    """(total, verified, draft) for data/<stem>.en.json; plus EN/AR parity error."""
    en = _load(f"data/{stem}.en.json")["data"]
    ar = _load(f"data/{stem}.ar.json")["data"]
    ce = Counter(e.get("verification_status") for e in en)
    ca = Counter(e.get("verification_status") for e in ar)
    err = None
    if len(en) != len(ar) or ce != ca:
        err = f"EN/AR mismatch for {stem}: en total={len(en)} {dict(ce)} | ar total={len(ar)} {dict(ca)}"
    return len(en), ce.get("verified", 0), ce.get("draft", 0), err


def count_mcp_tools():
    """Count @mcp.tool()-decorated callables in mcp/invest_gate_mcp.py via ast."""
    src = os.path.join(ROOT, "mcp", "invest_gate_mcp.py")
    with open(src, encoding="utf-8") as fh:
        tree = ast.parse(fh.read(), filename=src)
    n = 0
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            for dec in node.decorator_list:
                target = dec.func if isinstance(dec, ast.Call) else dec
                if isinstance(target, ast.Attribute) and target.attr == "tool":
                    n += 1
                    break
    return n


def _git(*args):
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True)


def count_commands():
    out = _git("ls-files", ".claude/commands/*.md").stdout.split()
    return len(out)


def untracked_counted_json():
    """.json files check.py's os.walk counts but git does not track (skips hidden dirs)."""
    present = set()
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if not d.startswith(".")]
        for fn in filenames:
            if fn.endswith(".json"):
                present.add(os.path.relpath(os.path.join(dirpath, fn), ROOT))
    res = _git("ls-files", "*.json")
    if res.returncode != 0:
        return 0
    tracked = set(res.stdout.split())
    return len([p for p in present if p not in tracked])


def compute_health_checks():
    proc = subprocess.run(
        [sys.executable, os.path.join(ROOT, "scripts", "check.py")],
        cwd=ROOT, capture_output=True, text=True,
    )
    # check.py embeds validate-data.py's own "Checks passed: N"; the LAST is the grand total.
    matches = re.findall(r"Checks passed:\s*(\d+)", proc.stdout)
    if not matches:
        return None, "could not parse check.py total"
    if proc.returncode != 0:
        return None, "check.py itself failed (run it directly to see why)"
    return int(matches[-1]) - untracked_counted_json(), None


def compute_counters():
    counters, errors = {}, []

    en_files = sorted(glob.glob(os.path.join(ROOT, "data", "*.en.json")))
    for f in en_files:
        if not os.path.exists(f.replace(".en.json", ".ar.json")):
            errors.append(f"dataset {os.path.basename(f)} has no .ar.json mirror")
    counters["datasets"] = len(en_files)

    for key, stem in TOTAL_DATASETS.items():
        total, ver, draft, err = _status_counts(stem)
        counters[key] = total
        if key in BREAKDOWN_DATASETS:
            counters[f"{key}_verified"] = ver
            counters[f"{key}_draft"] = draft
        if err:
            errors.append(err)

    s_total, s_ver, s_draft, s_err = _status_counts("sources")
    counters["sources_total"] = s_total
    counters["sources_verified"] = s_ver
    counters["sources_draft"] = s_draft
    if s_err:
        errors.append(s_err)

    counters["mcp_tools"] = count_mcp_tools()
    counters["commands"] = count_commands()

    hc, err = compute_health_checks()
    if err:
        errors.append(err)
    else:
        counters["health_checks"] = hc

    return counters, errors


def _badge_numbers(shields_url):
    """
    Strictly extract integer(s) from a shields badge URL of the canonical form
    .../badge/<label>-<message>-<color>.svg. Returns a list of ints, or None if
    the URL doesn't match that shape or the message isn't purely numeric — so any
    format change is an explicit failure, never a silent skip.
    """
    if "/badge/" not in shields_url:
        return None
    segs = shields_url.split("/badge/", 1)[1].split("-")
    if len(segs) < 3:
        return None
    nums = []
    for p in segs[-2].split("%2F"):
        if not p.isdigit():
            return None
        nums.append(int(p))
    return nums or None


def read_declarations():
    """Returns (decls list of (file,lineno,key,value), parse_errors list)."""
    decls, parse_errors = [], []
    for fname in READMES:
        with open(os.path.join(ROOT, fname), encoding="utf-8") as fh:
            lines = fh.read().splitlines()
        for i, line in enumerate(lines, 1):
            for m in RE_COUNT.finditer(line):
                decls.append((fname, i, m.group(1), int(m.group(2))))
            badge_keys = RE_BADGE.findall(line)
            if not badge_keys:
                continue
            sh = RE_SHIELDS.search(line)
            if not sh:
                parse_errors.append(
                    f"{fname}:{i} badge marker(s) {badge_keys} but no shields.io URL on the line"
                )
                continue
            vals = _badge_numbers(sh.group(0))
            if vals is None:
                parse_errors.append(
                    f"{fname}:{i} could not extract a numeric value from the badge URL "
                    f"(format changed?): {sh.group(0)}"
                )
                continue
            if len(vals) == len(badge_keys):
                for key, val in zip(badge_keys, vals):
                    decls.append((fname, i, key, val))
            elif len(badge_keys) == 1 and len(set(vals)) == 1:
                decls.append((fname, i, badge_keys[0], vals[0]))
            else:
                parse_errors.append(
                    f"{fname}:{i} badge has {len(vals)} number(s) {vals} but "
                    f"{len(badge_keys)} badge marker(s) {badge_keys}"
                )
    return decls, parse_errors


def main():
    print("Invest Gate KSA — Counter Guard")
    print("=" * 45)

    counters, problems = compute_counters()
    decls, parse_errors = read_declarations()
    problems = list(problems) + parse_errors

    mismatches = 0
    declared_per_file = {f: set() for f in READMES}
    for fname, lineno, key, value in decls:
        declared_per_file[fname].add(key)
        if key not in counters:
            problems.append(f"orphan marker '{key}' ({fname} line {lineno}) — no source of truth")
            continue
        if value != counters[key]:
            print(f"  MISMATCH {key}: README={value} actual={counters[key]} ({fname} line {lineno})")
            mismatches += 1

    for key in counters:
        for fname in READMES:
            if key not in declared_per_file[fname]:
                problems.append(f"counter '{key}' has no marker in {fname} (asymmetric/missing)")

    per_key = {}
    for fname, _ln, key, value in decls:
        per_key.setdefault(key, set()).add(value)
    for key, vals in per_key.items():
        if len(vals) > 1:
            problems.append(f"counter '{key}' declared with differing values across files: {sorted(vals)}")

    for p in problems:
        _fail(p)

    print("-" * 45)
    total = len(counters)
    if mismatches == 0 and not problems:
        print(f"counters: {total}/{total} in sync")
        print("RESULT: All counters in sync.")
        return 0
    print(f"RESULT: {mismatches} mismatch(es), {len(problems)} structural problem(s).")
    return 1


if __name__ == "__main__":
    sys.exit(main())
