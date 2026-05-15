#!/usr/bin/env python3
"""
Source gap reporting tool for Invest Gate KSA.

Reports official authorities referenced in other datasets that do not
yet have a verified entry in data/sources.en.json.

Architecture
────────────
  Loader      reads and validates the source-gaps JSON file
  Formatter   pure functions — no I/O, importable by MCP or API
  CLI         thin argparse wrapper over loader and formatter

Usage
─────
  python scripts/report-source-gaps.py
  python scripts/report-source-gaps.py --lang ar
  python scripts/report-source-gaps.py --status draft
  python scripts/report-source-gaps.py --id sama
  python scripts/report-source-gaps.py --id cma

Exit codes:
  0  report printed (including when a filter returns no matches)
  1  file not found or invalid JSON
"""

import argparse
import json
import os
import sys
import textwrap

# ── Paths ──────────────────────────────────────────────────────────────────────

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_FILES = {
    "en": os.path.join(ROOT, "data", "source-gaps.en.json"),
    "ar": os.path.join(ROOT, "data", "source-gaps.ar.json"),
}

WIDTH = 72


# ── Output helpers ─────────────────────────────────────────────────────────────

def _hr(char="─"):
    return char * WIDTH


def _wrap(text, indent=4):
    prefix = " " * indent
    return textwrap.fill(
        text,
        width=WIDTH,
        initial_indent=prefix,
        subsequent_indent=prefix,
    )


def _status_line(index, total, entry_id, status):
    """Right-align [status] against WIDTH regardless of ID length."""
    prefix = f"  {index} / {total}  {entry_id}"
    suffix = f"[{status}]"
    pad = max(1, WIDTH - len(prefix) - len(suffix))
    return prefix + " " * pad + suffix


# ── Data loader ────────────────────────────────────────────────────────────────

def load_gaps(lang):
    """Load and parse the source-gaps file. Exits 1 on missing file or bad JSON."""
    path = DATA_FILES[lang]
    try:
        with open(path, encoding="utf-8") as fh:
            return json.load(fh)
    except FileNotFoundError:
        print(f"ERROR: File not found: {path}", file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError as exc:
        print(f"ERROR: Invalid JSON in {path}: {exc}", file=sys.stderr)
        sys.exit(1)


def filter_entries(data, status=None):
    """Return all entries, optionally filtered by verification_status."""
    entries = list(data.get("data", []))
    if status:
        entries = [e for e in entries if e.get("verification_status") == status]
    return entries


# ── Formatting layer ───────────────────────────────────────────────────────────

def fmt_gap_block(entry, index, total):
    """
    Render a single gap entry as a report block for the list view.
    Starts with a separator; ends with a blank line.
    """
    status = entry.get("verification_status", "")
    lines = [_hr(), ""]

    lines.append(_status_line(index, total, entry["id"], status))
    lines.append(f"  {entry.get('name', '')}")

    alt = entry.get("name_alt", "")
    if alt:
        lines.append(f"  ({alt})")

    mentioned = entry.get("mentioned_in_datasets", [])
    if mentioned:
        lines.append(f"  Mentioned in:     {', '.join(mentioned)}")

    domain = entry.get("likely_official_domain", "")
    if domain:
        lines.append(f"  Domain to verify: {domain}")

    step = entry.get("next_verification_step", "")
    if step:
        lines += ["", "  NEXT STEP"]
        lines.append(_wrap(step, 4))

    lines.append("")
    return "\n".join(lines)


def fmt_detail(entry, lang):
    """Render the full detail view of a single entry for --id."""
    status = entry.get("verification_status", "")
    lines = [
        "",
        entry.get("name", ""),
        _hr(),
        f"  ID:               {entry['id']}",
        f"  Status:           {status}",
        f"  Also known as:    {entry.get('name_alt', '')}",
    ]

    mentioned = entry.get("mentioned_in_datasets", [])
    if mentioned:
        lines.append(f"  Mentioned in:     {', '.join(mentioned)}")

    domain = entry.get("likely_official_domain", "")
    if domain:
        lines.append(f"  Domain to verify: {domain}")

    reason = entry.get("reason_needed", "")
    if reason:
        lines += ["", "  WHY THIS GAP EXISTS"]
        lines.append(_wrap(reason, 4))

    step = entry.get("next_verification_step", "")
    if step:
        lines += ["", "  NEXT VERIFICATION STEP"]
        lines.append(_wrap(step, 4))

    phs = entry.get("placeholders", [])
    if phs:
        lines += ["", f"  PLACEHOLDERS  ({len(phs)} pending)"]
        for i, ph in enumerate(phs, 1):
            lines.append(f"    {i}. {ph.get('field', '')}")
            lines.append(_wrap(ph.get("description", ""), 7))
            lines.append(f"       → Verify at: {ph.get('verify_at', '')}")

    tags = entry.get("tags", [])
    if tags:
        lines += ["", "  TAGS"]
        lines.append(f"    {', '.join(tags)}")

    lines += [
        "",
        _hr(),
        f"  Source: data/source-gaps.{lang}.json",
    ]
    return "\n".join(lines)


# ── CLI ────────────────────────────────────────────────────────────────────────

def _build_parser():
    parser = argparse.ArgumentParser(
        prog="report-source-gaps",
        description="Report source gaps — authorities not yet verified in the sources registry.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent("""\
            examples:
              python scripts/report-source-gaps.py
              python scripts/report-source-gaps.py --lang ar
              python scripts/report-source-gaps.py --status draft
              python scripts/report-source-gaps.py --id sama
              python scripts/report-source-gaps.py --id cma
        """),
    )
    parser.add_argument(
        "--lang", choices=["en", "ar"], default="en",
        metavar="LANG",
        help="Dataset language: en (default) or ar",
    )
    parser.add_argument(
        "--status", choices=["draft", "verified"],
        metavar="STATUS",
        help="Filter by verification_status: draft or verified",
    )
    parser.add_argument(
        "--id", metavar="ID",
        help="Show full detail for a single gap entry",
    )
    return parser


def main():
    parser = _build_parser()
    args = parser.parse_args()
    data = load_gaps(args.lang)

    # ── Detail mode ────────────────────────────────────────────────────────────
    if args.id:
        entry = next(
            (e for e in data.get("data", []) if e["id"] == args.id),
            None,
        )
        if entry is None:
            all_ids = [e["id"] for e in data.get("data", [])]
            print(f"No gap entry found with id '{args.id}'.")
            print(f"Available ids: {', '.join(all_ids)}")
        else:
            print(fmt_detail(entry, args.lang))
        return

    # ── Report mode ────────────────────────────────────────────────────────────
    entries = filter_entries(data, args.status)
    status_label = f"status: {args.status}" if args.status else "all"

    print("")
    print("Invest Gate KSA — Source Gap Report")
    print(_hr("="))
    print(f"  {len(entries)} gap(s)  ({status_label})  |  language: {args.lang}")

    if not entries:
        if args.status == "verified":
            print("\n  No verified gaps found. All entries are still draft.")
        else:
            print(f"\n  No gaps found with status '{args.status}'.")
        print("")
        return

    for i, entry in enumerate(entries, 1):
        print(fmt_gap_block(entry, i, len(entries)))


if __name__ == "__main__":
    main()
