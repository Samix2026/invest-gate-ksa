#!/usr/bin/env python3
"""
Query script for Invest Gate KSA business structures dataset.

Architecture
────────────
  DataLoader   loads and caches dataset files from disk
  Query layer  pure functions — no I/O, importable by an MCP server or API
  Formatter    renders query results to terminal
  CLI          thin argparse wrapper over the query and formatter layers

MCP usage
─────────
  Import the query layer directly — no CLI needed:

    from scripts.query_structures import DataLoader, get_by_id, get_by_tag, list_all

  Example MCP tool handler:

    def handle_get_structure(tool_input):
        data = DataLoader.load(tool_input.get("lang", "en"))
        entry = get_by_id(data, tool_input["id"])
        return entry or {"error": "not_found", "id": tool_input["id"]}

Usage
─────
  python scripts/query-structures.py --list
  python scripts/query-structures.py --lang ar --list
  python scripts/query-structures.py --id llc
  python scripts/query-structures.py --lang ar --id llc
  python scripts/query-structures.py --tag foreign_investment
  python scripts/query-structures.py --lang ar --tag non_commercial
"""

import argparse
import json
import os
import sys
import textwrap
from typing import Dict, List, Optional

# ── Paths ─────────────────────────────────────────────────────────────────────

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_FILES = {
    "en": os.path.join(ROOT, "data", "business-structures.en.json"),
    "ar": os.path.join(ROOT, "data", "business-structures.ar.json"),
}

# ── Layout constants ──────────────────────────────────────────────────────────

WIDTH    = 72   # terminal line width
COL_ID   = 24   # "representative_office" = 21 + 3 padding
COL_NAME = 30   # "Branch of a Foreign Company" = 27 + 3 padding
COL_COMM = 5    # "Yes" / "No " + 2 padding

# ── Data loader ───────────────────────────────────────────────────────────────

class DataLoader:
    """
    Loads and caches datasets from disk.

    MCP note: instantiate once at server start; call .load(lang) per request.
    The base_path parameter lets callers override ROOT for deployment environments
    where the repository is not at the script's parent directory.
    """

    _cache: Dict[str, dict] = {}

    @classmethod
    def load(cls, lang: str, base_path: str = ROOT) -> dict:
        """Return the parsed dataset for the given language."""
        if lang not in DATA_FILES:
            _die(f"Unknown language '{lang}'. Valid options: en, ar")
        cache_key = f"{lang}:{base_path}"
        if cache_key not in cls._cache:
            path = os.path.join(base_path, "data", f"business-structures.{lang}.json")
            try:
                with open(path, encoding="utf-8") as fh:
                    cls._cache[cache_key] = json.load(fh)
            except FileNotFoundError:
                _die(f"Dataset not found: {path}")
            except json.JSONDecodeError as exc:
                _die(f"Invalid JSON in {path}: {exc}")
        return cls._cache[cache_key]


def _die(msg: str) -> None:
    print(f"ERROR: {msg}", file=sys.stderr)
    sys.exit(1)


# ── Query layer ───────────────────────────────────────────────────────────────
# Pure functions — no I/O, no side effects.
# Return plain Python objects (list, dict, None) so callers can serialise
# to JSON, Markdown, or any format without modifying this layer.

def list_all(data: dict) -> List[dict]:
    """Return all structure entries in dataset order."""
    return list(data.get("data", []))


def get_by_id(data: dict, structure_id: str) -> Optional[dict]:
    """Return the entry matching structure_id, or None if not found."""
    for entry in data.get("data", []):
        if entry["id"] == structure_id:
            return entry
    return None


def get_by_tag(data: dict, tag: str) -> List[dict]:
    """Return all entries that carry the given tag."""
    return [e for e in data.get("data", []) if tag in e.get("tags", [])]


def all_ids(data: dict) -> List[str]:
    """Return every entry ID in dataset order."""
    return [e["id"] for e in data.get("data", [])]


def all_tags(data: dict) -> List[str]:
    """Return sorted list of every unique tag across all entries."""
    tags: set = set()
    for entry in data.get("data", []):
        tags.update(entry.get("tags", []))
    return sorted(tags)


# ── Formatting layer ──────────────────────────────────────────────────────────

def _hr() -> str:
    return "─" * WIDTH


def _ybool(value) -> str:
    """Render a boolean or the string 'sector_dependent' for display."""
    if isinstance(value, bool):
        return "Yes" if value else "No"
    return str(value)


def _wrap(text: str, indent: int = 4) -> str:
    """Word-wrap text to WIDTH with a fixed left indent."""
    prefix = " " * indent
    return textwrap.fill(
        text, width=WIDTH,
        initial_indent=prefix,
        subsequent_indent=prefix,
    )


def _trunc(text: str, max_len: int) -> str:
    """Truncate text to max_len, adding '…' if cut."""
    return text if len(text) <= max_len else text[: max_len - 1] + "…"


def fmt_list_table(entries: List[dict], title: str) -> str:
    """Render a compact table of structures for --list and --tag."""
    lines = [
        "",
        title,
        _hr(),
        f"  {'ID':<{COL_ID}}{'NAME':<{COL_NAME}}{'COMM':<{COL_COMM}}STATUS",
        _hr(),
    ]
    for e in entries:
        comm = _ybool(e.get("commercial_activities_permitted"))
        name = _trunc(e.get("name", ""), COL_NAME - 1)
        lines.append(
            f"  {e['id']:<{COL_ID}}{name:<{COL_NAME}}{comm:<{COL_COMM}}"
            f"{e.get('verification_status', '')}"
        )
    lines += [_hr(), f"  {len(entries)} structure(s)"]
    return "\n".join(lines)


def fmt_detail(entry: dict, lang: str) -> str:
    """Render the full detail view of a single structure for --id."""
    lines = []
    abbr = f" ({entry['abbreviation']})" if entry.get("abbreviation") else ""
    lines += [
        "",
        f"{entry['name']}{abbr}",
        _hr(),
        f"  ID:         {entry['id']}",
        f"  Status:     {entry.get('verification_status', '')}",
        f"  Also known: {entry.get('name_alt', '')}",
    ]

    lines += ["", "  DESCRIPTION"]
    lines.append(_wrap(entry.get("short_description", ""), 4))

    ot = entry.get("ownership_type", {})
    lines += [
        "",
        "  OWNERSHIP",
        f"    Full foreign ownership:  {_ybool(ot.get('allows_full_foreign_ownership'))}",
        f"    Local ownership:         {_ybool(ot.get('allows_local_ownership'))}",
        f"    Mixed ownership:         {_ybool(ot.get('allows_mixed_ownership'))}",
    ]
    if ot.get("notes"):
        lines.append(_wrap(ot["notes"], 4))

    le = entry.get("legal_entity_status", {})
    lines += [
        "",
        "  LEGAL ENTITY",
        f"    Separate legal entity:   {_ybool(le.get('is_separate_legal_entity'))}",
        f"    Liability model:         {le.get('liability_model', '')}",
        f"    Commercial activities:   {_ybool(entry.get('commercial_activities_permitted'))}",
    ]

    uses = entry.get("typical_use_cases", [])
    if uses:
        lines += ["", "  TYPICAL USE CASES"]
        for i, use in enumerate(uses, 1):
            lines.append(f"    {i}. {use}")

    misa = entry.get("requires_misa_license", {})
    lines += [
        "",
        "  MISA LICENSE",
        f"    Applicable:   {_ybool(misa.get('applicable'))}",
        f"    Condition:    {misa.get('condition', '')}",
    ]
    if misa.get("condition_for_local_investors"):
        lines.append(f"    Local:        {misa['condition_for_local_investors']}")
    if misa.get("notes"):
        lines.append(_wrap(misa["notes"], 4))
    lines.append(f"    Verify at:    {misa.get('verify_at', '')}")

    sources = entry.get("official_sources", [])
    lines += ["", "  OFFICIAL SOURCES"]
    for i, src in enumerate(sources, 1):
        lines += [
            f"    {i}. {src['name']}",
            f"       Role:    {src['role']}",
            f"       Portal:  {src['portal']}",
        ]

    ph = entry.get("placeholders", [])
    if ph:
        lines += ["", f"  PLACEHOLDERS  ({len(ph)} pending verification)"]
        for i, p in enumerate(ph, 1):
            lines.append(f"    {i}. {p['field']}")
            lines.append(_wrap(p["description"], 7))
            lines.append(f"       → Verify at: {p['verify_at']}")

    lines += [
        "",
        _hr(),
        f"  Source: data/business-structures.{lang}.json  |  sources/index.md",
    ]
    return "\n".join(lines)


# ── CLI ───────────────────────────────────────────────────────────────────────

def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="query-structures",
        description="Query the Invest Gate KSA business structures dataset.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent("""\
            examples:
              python scripts/query-structures.py --list
              python scripts/query-structures.py --lang ar --list
              python scripts/query-structures.py --id llc
              python scripts/query-structures.py --lang ar --id joint_stock_company
              python scripts/query-structures.py --tag foreign_investment
        """),
    )
    parser.add_argument(
        "--lang", choices=["en", "ar"], default="en",
        metavar="LANG",
        help="Dataset language: en (default) or ar",
    )
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument(
        "--list", action="store_true",
        help="List all structures",
    )
    action.add_argument(
        "--id", metavar="ID",
        help="Show detail for one structure (e.g. llc, foreign_branch)",
    )
    action.add_argument(
        "--tag", metavar="TAG",
        help="Filter structures by tag (e.g. foreign_investment, non_commercial)",
    )
    return parser


def main() -> None:
    parser = _build_parser()
    args = parser.parse_args()
    data = DataLoader.load(args.lang)

    if args.list:
        count = len(list_all(data))
        title = f"Business Structures ({args.lang})  —  {count} entries"
        print(fmt_list_table(list_all(data), title))

    elif args.id:
        entry = get_by_id(data, args.id)
        if entry is None:
            print(f"No structure found with id '{args.id}'.")
            print(f"Available ids: {', '.join(all_ids(data))}")
            sys.exit(1)
        print(fmt_detail(entry, args.lang))

    elif args.tag:
        matches = get_by_tag(data, args.tag)
        if not matches:
            print(f"No structures found with tag '{args.tag}'.")
            print(f"Available tags: {', '.join(all_tags(data))}")
            sys.exit(1)
        title = f"Tag: {args.tag}  —  {len(matches)} match(es)  ({args.lang})"
        print(fmt_list_table(matches, title))


if __name__ == "__main__":
    main()
