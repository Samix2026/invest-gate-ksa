#!/usr/bin/env python3
"""
Project health check for Invest Gate KSA.

Runs four check suites:
  1. Required files    — all key project files must exist
  2. JSON validity     — every .json file must parse cleanly
  3. Dataset checks    — delegates to validate-data.py via subprocess
  4. Markdown links    — local [text](path) links in .md files must resolve

External URLs (http/https) and anchor-only links (#...) are skipped.

Usage:
    python scripts/check.py

Requirements:
    Python 3.7+ — no additional packages needed for this script.
    validate-data.py requires: pip install jsonschema>=3.2.0

Exit codes:
    0  all checks passed
    1  one or more checks failed
"""

import json
import os
import re
import subprocess
import sys

# ── Paths ─────────────────────────────────────────────────────────────────────

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

REQUIRED_FILES = [
    "README.md",
    "README.ar.md",
    "CONTRIBUTING.md",
    "LICENSE",
    "roadmap.md",
    "docs/en/README.md",
    "docs/ar/README.md",
    "docs/en/company-setup-overview.md",
    "docs/ar/company-setup-overview.md",
    "data/README.md",
    "data/business-structures.en.json",
    "data/business-structures.ar.json",
    "schemas/business-structures.schema.json",
    "sources/index.md",
    "scripts/validate-data.py",
    "scripts/query-structures.py",
    "scripts/requirements.txt",
    "examples/query-examples.md",
]

# Markdown link targets to skip (not local paths)
_SKIP_LINK_RE = re.compile(r"^(https?://|mailto:|#)", re.IGNORECASE)

# Matches [label](target) — captures the target portion
_LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")


# ── Output helpers ─────────────────────────────────────────────────────────────

def _section(title: str) -> None:
    print(f"\n{title}")
    print("─" * len(title))


def _pass(label: str, detail: str = "") -> None:
    suffix = f"  ({detail})" if detail else ""
    print(f"  PASS  {label}{suffix}")


def _fail(label: str, detail: str = "") -> None:
    print(f"  FAIL  {label}")
    if detail:
        for line in detail.splitlines():
            print(f"        {line}")


# ── Check suites ──────────────────────────────────────────────────────────────

def run_required_files() -> tuple:
    """Check that all required project files exist."""
    _section("Required files")
    passes = fails = 0
    for rel_path in REQUIRED_FILES:
        full = os.path.join(ROOT, rel_path)
        if os.path.isfile(full):
            _pass(rel_path)
            passes += 1
        else:
            _fail(rel_path, "file not found")
            fails += 1
    return passes, fails


def run_json_validity() -> tuple:
    """Parse every .json file under ROOT and report any that are invalid."""
    _section("JSON validity")
    passes = fails = 0
    for dirpath, _dirnames, filenames in os.walk(ROOT):
        # Skip hidden directories (e.g. .git)
        _dirnames[:] = [d for d in _dirnames if not d.startswith(".")]
        for fname in sorted(filenames):
            if not fname.endswith(".json"):
                continue
            full = os.path.join(dirpath, fname)
            rel = os.path.relpath(full, ROOT)
            try:
                with open(full, encoding="utf-8") as fh:
                    json.load(fh)
                _pass(rel)
                passes += 1
            except json.JSONDecodeError as exc:
                _fail(rel, str(exc))
                fails += 1
            except OSError as exc:
                _fail(rel, str(exc))
                fails += 1
    if passes == 0 and fails == 0:
        print("  (no .json files found)")
    return passes, fails


def run_dataset_validation() -> tuple:
    """Delegate full dataset + alias validation to validate-data.py."""
    _section("Dataset and alias validation  (validate-data.py)")
    validate_script = os.path.join(ROOT, "scripts", "validate-data.py")

    if not os.path.isfile(validate_script):
        _fail("validate-data.py", "script not found — skipping")
        return 0, 1

    result = subprocess.run(
        [sys.executable, validate_script],
        capture_output=True,
        text=True,
    )

    # Indent the sub-script output so it reads as nested content
    for line in result.stdout.splitlines():
        print(f"  {line}")

    if result.returncode == 0:
        _pass("validate-data.py", "all dataset checks passed")
        return 1, 0
    else:
        _fail("validate-data.py", "one or more dataset checks failed (see above)")
        return 0, 1


def run_markdown_links() -> tuple:
    """
    Find all [text](target) links in .md files.
    Skip external URLs and anchor-only links.
    For local targets: strip any #fragment, resolve relative to the file's
    directory, and check the path exists.
    """
    _section("Markdown local links")
    passes = fails = 0

    md_files = []
    for dirpath, _dirnames, filenames in os.walk(ROOT):
        _dirnames[:] = [d for d in _dirnames if not d.startswith(".")]
        for fname in sorted(filenames):
            if fname.endswith(".md"):
                md_files.append(os.path.join(dirpath, fname))

    for md_path in sorted(md_files):
        rel_md = os.path.relpath(md_path, ROOT)
        file_passes = file_fails = 0

        try:
            with open(md_path, encoding="utf-8") as fh:
                content = fh.read()
        except OSError as exc:
            _fail(rel_md, f"could not read: {exc}")
            fails += 1
            continue

        # Strip inline code spans so example links inside backticks aren't checked
        content_no_code = re.sub(r"`[^`\n]*`", "", content)
        targets = _LINK_RE.findall(content_no_code)
        for raw_target in targets:
            # Skip external and anchor-only links
            if _SKIP_LINK_RE.match(raw_target):
                continue

            # Strip inline #fragment
            target = raw_target.split("#")[0]
            if not target:
                # Pure anchor link — skip
                continue

            # Resolve relative to the markdown file's directory
            base_dir = os.path.dirname(md_path)
            resolved = os.path.normpath(os.path.join(base_dir, target))

            if os.path.exists(resolved):
                file_passes += 1
            else:
                rel_target = os.path.relpath(resolved, ROOT)
                _fail(f"{rel_md} → {raw_target}", f"target not found: {rel_target}")
                file_fails += 1

        passes += file_passes
        fails  += file_fails

        if file_passes > 0 and file_fails == 0:
            _pass(rel_md, f"{file_passes} local link(s) OK")

    if passes == 0 and fails == 0:
        print("  (no local markdown links found)")

    return passes, fails


# ── Main ──────────────────────────────────────────────────────────────────────

def main() -> None:
    print("Invest Gate KSA — Project Health Check")
    print("=" * 45)

    total_passes = total_fails = 0

    for suite in [
        run_required_files,
        run_json_validity,
        run_dataset_validation,
        run_markdown_links,
    ]:
        p, f = suite()
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
