#!/usr/bin/env python3
"""
Generic dataset query script for Invest Gate KSA.

Works with any dataset that follows the {meta, data} structure.
Entries must have at least: id, name, verification_status, tags.

For the business-structures dataset, the richer domain-specific formatter
in scripts/query-structures.py is also available.

Architecture
────────────
  DataLoader   loads and caches dataset files from disk
  Query layer  pure functions — no I/O, importable by an MCP server or API
  Formatter    generic renderer that handles arbitrary field types
  CLI          thin argparse wrapper over the query and formatter layers

MCP usage
─────────
  Import the query layer directly — no CLI needed:

    from scripts.query_dataset import DataLoader, get_by_id, get_by_tag, list_all

Usage
─────
  python scripts/query-dataset.py --dataset investment-licenses --list
  python scripts/query-dataset.py --dataset investment-licenses --lang ar --list
  python scripts/query-dataset.py --dataset investment-licenses --id misa_license
  python scripts/query-dataset.py --dataset investment-licenses --tag misa
  python scripts/query-dataset.py --dataset sources --list
  python scripts/query-dataset.py --dataset sources --authority-type government_ministry
  python scripts/query-dataset.py --dataset sources --lang ar --tag misa
  python scripts/query-dataset.py --dataset business-structures --list
  python scripts/query-dataset.py --dataset sectors --list
  python scripts/query-dataset.py --dataset sectors --lang ar --id fintech
  python scripts/query-dataset.py --dataset sectors --regulatory-sensitivity highly_regulated
"""

import argparse
import json
import os
import sys
import textwrap
from typing import Dict, List, Optional

# ── Dataset registry ──────────────────────────────────────────────────────────

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATASETS: Dict[str, Dict[str, str]] = {
    "business-structures": {
        "en": os.path.join(ROOT, "data", "business-structures.en.json"),
        "ar": os.path.join(ROOT, "data", "business-structures.ar.json"),
    },
    "investment-licenses": {
        "en": os.path.join(ROOT, "data", "investment-licenses.en.json"),
        "ar": os.path.join(ROOT, "data", "investment-licenses.ar.json"),
    },
    "sources": {
        "en": os.path.join(ROOT, "data", "sources.en.json"),
        "ar": os.path.join(ROOT, "data", "sources.ar.json"),
    },
    "sectors": {
        "en": os.path.join(ROOT, "data", "sectors.en.json"),
        "ar": os.path.join(ROOT, "data", "sectors.ar.json"),
    },
    "source-gaps": {
        "en": os.path.join(ROOT, "data", "source-gaps.en.json"),
        "ar": os.path.join(ROOT, "data", "source-gaps.ar.json"),
    },
    "authority-relationships": {
        "en": os.path.join(ROOT, "data", "authority-relationships.en.json"),
        "ar": os.path.join(ROOT, "data", "authority-relationships.ar.json"),
    },
    "setup-flows": {
        "en": os.path.join(ROOT, "data", "setup-flows.en.json"),
        "ar": os.path.join(ROOT, "data", "setup-flows.ar.json"),
    },
}

# ── Layout constants ──────────────────────────────────────────────────────────

WIDTH    = 80
COL_ID   = 34
COL_NAME = 30

# Fields rendered explicitly in the header/footer — skipped in the generic loop
_HEADER_FIELDS = frozenset({
    "id", "name", "name_alt", "abbreviation",
    "verification_status", "short_description",
    "official_sources", "placeholders", "tags",
})

# ── Data loader ───────────────────────────────────────────────────────────────

class DataLoader:
    """
    Loads and caches datasets from disk.

    MCP note: instantiate once at server start; call .load(dataset, lang) per
    request. The same cache key space supports all registered datasets.
    """

    _cache: Dict[str, dict] = {}

    @classmethod
    def load(cls, dataset: str, lang: str) -> dict:
        """Return the parsed dataset for the given dataset name and language."""
        if dataset not in DATASETS:
            _die(f"Unknown dataset '{dataset}'. Available: {', '.join(sorted(DATASETS))}")
        if lang not in ("en", "ar"):
            _die(f"Unknown language '{lang}'. Valid options: en, ar")
        cache_key = f"{dataset}:{lang}"
        if cache_key not in cls._cache:
            path = DATASETS[dataset][lang]
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


# ── Query layer (pure functions) ──────────────────────────────────────────────

def list_all(data: dict) -> List[dict]:
    """Return all entries in dataset order."""
    return list(data.get("data", []))


def get_by_id(data: dict, entry_id: str) -> Optional[dict]:
    """Return the entry matching entry_id, or None if not found."""
    for entry in data.get("data", []):
        if entry["id"] == entry_id:
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


def get_by_authority_type(data: dict, authority_type: str) -> List[dict]:
    """Return all entries whose authority_type matches exactly."""
    return [e for e in data.get("data", []) if e.get("authority_type") == authority_type]


def all_authority_types(data: dict) -> List[str]:
    """Return sorted list of every unique authority_type across all entries."""
    types: set = set()
    for entry in data.get("data", []):
        if entry.get("authority_type"):
            types.add(entry["authority_type"])
    return sorted(types)


def get_by_regulatory_sensitivity(data: dict, sensitivity: str) -> List[dict]:
    """Return all entries whose regulatory_sensitivity matches exactly."""
    return [e for e in data.get("data", []) if e.get("regulatory_sensitivity") == sensitivity]


def all_regulatory_sensitivities(data: dict) -> List[str]:
    """Return sorted list of every unique regulatory_sensitivity across all entries."""
    levels: set = set()
    for entry in data.get("data", []):
        if entry.get("regulatory_sensitivity"):
            levels.add(entry["regulatory_sensitivity"])
    return sorted(levels)


def get_by_relationship_type(data: dict, relationship_type: str) -> List[dict]:
    """Return all entries whose relationship_type matches exactly."""
    return [e for e in data.get("data", []) if e.get("relationship_type") == relationship_type]


def all_relationship_types(data: dict) -> List[str]:
    """Return sorted list of every unique relationship_type across all entries."""
    types: set = set()
    for entry in data.get("data", []):
        if entry.get("relationship_type"):
            types.add(entry["relationship_type"])
    return sorted(types)


def get_by_from_authority(data: dict, authority_id: str) -> List[dict]:
    """Return all entries whose from_authority.id matches exactly."""
    return [
        e for e in data.get("data", [])
        if e.get("from_authority", {}).get("id") == authority_id
    ]


def get_by_to_authority(data: dict, authority_id: str) -> List[dict]:
    """Return all entries whose to_authority.id matches exactly."""
    return [
        e for e in data.get("data", [])
        if e.get("to_authority") and e["to_authority"].get("id") == authority_id
    ]


def get_by_sector(data: dict, sector_id: str) -> List[dict]:
    """Return all entries that list the given sector_id in applies_to_sectors."""
    return [
        e for e in data.get("data", [])
        if sector_id in e.get("applies_to_sectors", [])
    ]


def get_by_related_sector(data: dict, sector_id: str) -> List[dict]:
    """Return all entries that list the given sector_id in related_sectors."""
    return [
        e for e in data.get("data", [])
        if sector_id in e.get("related_sectors", [])
    ]


# ── Formatting layer ──────────────────────────────────────────────────────────

def _hr() -> str:
    return "─" * WIDTH


def _wrap(text: str, indent: int = 4) -> str:
    prefix = " " * indent
    return textwrap.fill(
        text, width=WIDTH,
        initial_indent=prefix,
        subsequent_indent=prefix,
    )


def _trunc(text: str, max_len: int) -> str:
    return text if len(text) <= max_len else text[: max_len - 1] + "…"


def _ybool(value) -> str:
    if isinstance(value, bool):
        return "Yes" if value else "No"
    return str(value)


def _entry_name(entry: dict) -> str:
    """Return a display name for a list row.

    Falls back gracefully for entries without a top-level 'name' field
    (e.g. authority-relationships) by constructing 'from_id → to_id'.
    """
    if entry.get("name"):
        return entry["name"]
    from_auth = entry.get("from_authority")
    if from_auth:
        from_id = from_auth.get("id", "")
        to_auth  = entry.get("to_authority")
        to_id    = to_auth.get("id", "") if to_auth else "—"
        return f"{from_id} → {to_id}"
    desc = entry.get("conceptual_description", "")
    return desc


def fmt_list_table(entries: List[dict], title: str) -> str:
    """Render a compact table for --list and --tag."""
    lines = [
        "",
        title,
        _hr(),
        f"  {'ID':<{COL_ID}}{'NAME':<{COL_NAME}}STATUS",
        _hr(),
    ]
    for e in entries:
        name = _trunc(_entry_name(e), COL_NAME - 1)
        lines.append(
            f"  {e['id']:<{COL_ID}}{name:<{COL_NAME}}"
            f"{e.get('verification_status', '')}"
        )
    lines += [_hr(), f"  {len(entries)} entry/entries"]
    return "\n".join(lines)


def _render_field_lines(key: str, value) -> List[str]:
    """
    Return display lines for a single non-header field.
    Handles str, bool, dict, and list values generically.
    """
    if value is None or value == "" or value == []:
        return []

    label = f"  {key.replace('_', ' ').upper()}"
    pad4  = "    "
    pad7  = "       "

    if isinstance(value, bool):
        return ["", label, f"{pad4}{'Yes' if value else 'No'}"]

    if isinstance(value, str):
        return ["", label, _wrap(value, 4)]

    if isinstance(value, dict):
        lines = ["", label]
        for k, v in value.items():
            if v is None or v == "":
                continue
            sub = k.replace("_", " ").capitalize()
            lines.append(f"{pad4}{sub}:  {_ybool(v)}")
        return lines

    if isinstance(value, list):
        lines = ["", label]
        for i, item in enumerate(value, 1):
            if isinstance(item, str):
                lines.append(f"{pad4}{i}. {item}")
            elif isinstance(item, dict):
                item_name = item.get("name", f"Item {i}")
                lines.append(f"{pad4}{i}. {item_name}")
                for k, v in item.items():
                    if k == "name" or v is None or v == "":
                        continue
                    sub = k.replace("_", " ").capitalize()
                    lines.append(f"{pad7}{sub}: {v}")
        return lines

    return ["", label, f"    {value}"]


def fmt_detail(entry: dict, dataset: str, lang: str) -> str:
    """Render the full detail view of a single entry for --id."""
    lines = []

    # Header
    abbr = f" ({entry['abbreviation']})" if entry.get("abbreviation") else ""
    lines += [
        "",
        f"{entry['name']}{abbr}",
        _hr(),
        f"  ID:         {entry['id']}",
        f"  Status:     {entry.get('verification_status', '')}",
        f"  Also known: {entry.get('name_alt', '')}",
    ]

    # Description
    if entry.get("short_description"):
        lines += ["", "  DESCRIPTION"]
        lines.append(_wrap(entry["short_description"], 4))

    # All non-header fields rendered generically
    for key, value in entry.items():
        if key in _HEADER_FIELDS:
            continue
        lines.extend(_render_field_lines(key, value))

    # Official sources (always last-ish, fixed format)
    sources = entry.get("official_sources", [])
    if sources:
        lines += ["", "  OFFICIAL SOURCES"]
        for i, src in enumerate(sources, 1):
            lines += [
                f"    {i}. {src.get('name', '')}",
                f"       Role:    {src.get('role', '')}",
                f"       Portal:  {src.get('portal', '')}",
            ]

    # Placeholders
    ph = entry.get("placeholders", [])
    if ph:
        lines += ["", f"  PLACEHOLDERS  ({len(ph)} pending verification)"]
        for i, p in enumerate(ph, 1):
            lines.append(f"    {i}. {p.get('field', '')}")
            lines.append(_wrap(p.get("description", ""), 7))
            lines.append(f"       → Verify at: {p.get('verify_at', '')}")

    # Tags
    tags = entry.get("tags", [])
    if tags:
        lines += ["", "  TAGS"]
        lines.append(f"    {', '.join(tags)}")

    lines += [
        "",
        _hr(),
        f"  Source: data/{dataset}.{lang}.json  |  sources/index.md",
    ]
    return "\n".join(lines)


# ── CLI ───────────────────────────────────────────────────────────────────────

def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="query-dataset",
        description="Generic query tool for Invest Gate KSA datasets.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent("""\
            examples:
              python scripts/query-dataset.py --dataset investment-licenses --list
              python scripts/query-dataset.py --dataset investment-licenses --lang ar --list
              python scripts/query-dataset.py --dataset investment-licenses --id misa_license
              python scripts/query-dataset.py --dataset investment-licenses --tag misa
              python scripts/query-dataset.py --dataset business-structures --list
        """),
    )
    parser.add_argument(
        "--dataset",
        required=True,
        choices=sorted(DATASETS),
        metavar="DATASET",
        help=f"Dataset to query: {', '.join(sorted(DATASETS))}",
    )
    parser.add_argument(
        "--lang", choices=["en", "ar"], default="en",
        metavar="LANG",
        help="Dataset language: en (default) or ar",
    )
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument(
        "--list", action="store_true",
        help="List all entries",
    )
    action.add_argument(
        "--id", metavar="ID",
        help="Show detail for one entry",
    )
    action.add_argument(
        "--tag", metavar="TAG",
        help="Filter entries by tag",
    )
    action.add_argument(
        "--authority-type", metavar="TYPE",
        help="Filter entries by authority_type (e.g. government_ministry, government_portal)",
    )
    action.add_argument(
        "--regulatory-sensitivity", metavar="LEVEL",
        help="Filter entries by regulatory_sensitivity (e.g. standard, regulated, highly_regulated)",
    )
    action.add_argument(
        "--relationship-type", metavar="TYPE",
        help="Filter entries by relationship_type (e.g. foundational_dependency, sector_oversight, compliance_interaction)",
    )
    action.add_argument(
        "--from-authority", metavar="ID",
        help="Filter authority-relationships entries by from_authority.id (e.g. misa, ncec, zatca)",
    )
    action.add_argument(
        "--to-authority", metavar="ID",
        help="Filter authority-relationships entries by to_authority.id (e.g. ministry_of_commerce, balady)",
    )
    action.add_argument(
        "--sector", metavar="SECTOR",
        help="Filter authority-relationships entries by applies_to_sectors membership (e.g. fintech, manufacturing)",
    )
    action.add_argument(
        "--related-sector", metavar="SECTOR",
        help="Filter setup-flows entries by related_sectors membership (e.g. fintech, manufacturing, ecommerce)",
    )
    return parser


def main() -> None:
    parser = _build_parser()
    args = parser.parse_args()
    data = DataLoader.load(args.dataset, args.lang)

    if args.list:
        entries = list_all(data)
        title = f"{args.dataset}  ({args.lang})  —  {len(entries)} entries"
        print(fmt_list_table(entries, title))

    elif args.id:
        entry = get_by_id(data, args.id)
        if entry is None:
            print(f"No entry found with id '{args.id}'.")
            print(f"Available ids: {', '.join(all_ids(data))}")
            sys.exit(1)
        print(fmt_detail(entry, args.dataset, args.lang))

    elif args.tag:
        matches = get_by_tag(data, args.tag)
        if not matches:
            print(f"No entries found with tag '{args.tag}'.")
            print(f"Available tags: {', '.join(all_tags(data))}")
            sys.exit(1)
        title = f"Tag: {args.tag}  —  {len(matches)} match(es)  ({args.dataset}, {args.lang})"
        print(fmt_list_table(matches, title))

    elif args.authority_type:
        matches = get_by_authority_type(data, args.authority_type)
        if not matches:
            print(f"No entries found with authority_type '{args.authority_type}'.")
            types = all_authority_types(data)
            if types:
                print(f"Available authority types: {', '.join(types)}")
            else:
                print("This dataset does not use the authority_type field.")
            sys.exit(1)
        title = (
            f"Authority type: {args.authority_type}  —  {len(matches)} match(es)"
            f"  ({args.dataset}, {args.lang})"
        )
        print(fmt_list_table(matches, title))

    elif args.regulatory_sensitivity:
        matches = get_by_regulatory_sensitivity(data, args.regulatory_sensitivity)
        if not matches:
            print(f"No entries found with regulatory_sensitivity '{args.regulatory_sensitivity}'.")
            levels = all_regulatory_sensitivities(data)
            if levels:
                print(f"Available levels: {', '.join(levels)}")
            else:
                print("This dataset does not use the regulatory_sensitivity field.")
            sys.exit(1)
        title = (
            f"Regulatory sensitivity: {args.regulatory_sensitivity}  —  {len(matches)} match(es)"
            f"  ({args.dataset}, {args.lang})"
        )
        print(fmt_list_table(matches, title))

    elif args.relationship_type:
        matches = get_by_relationship_type(data, args.relationship_type)
        if not matches:
            print(f"No entries found with relationship_type '{args.relationship_type}'.")
            types = all_relationship_types(data)
            if types:
                print(f"Available relationship types: {', '.join(types)}")
            else:
                print("This dataset does not use the relationship_type field.")
            sys.exit(1)
        title = (
            f"Relationship type: {args.relationship_type}  —  {len(matches)} match(es)"
            f"  ({args.dataset}, {args.lang})"
        )
        print(fmt_list_table(matches, title))

    elif args.from_authority:
        matches = get_by_from_authority(data, args.from_authority)
        if not matches:
            print(f"No entries found with from_authority.id '{args.from_authority}'.")
            sys.exit(1)
        title = (
            f"From authority: {args.from_authority}  —  {len(matches)} match(es)"
            f"  ({args.dataset}, {args.lang})"
        )
        print(fmt_list_table(matches, title))

    elif args.to_authority:
        matches = get_by_to_authority(data, args.to_authority)
        if not matches:
            print(f"No entries found with to_authority.id '{args.to_authority}'.")
            sys.exit(1)
        title = (
            f"To authority: {args.to_authority}  —  {len(matches)} match(es)"
            f"  ({args.dataset}, {args.lang})"
        )
        print(fmt_list_table(matches, title))

    elif args.sector:
        matches = get_by_sector(data, args.sector)
        if not matches:
            print(f"No entries found with sector '{args.sector}' in applies_to_sectors.")
            sys.exit(1)
        title = (
            f"Sector: {args.sector}  —  {len(matches)} match(es)"
            f"  ({args.dataset}, {args.lang})"
        )
        print(fmt_list_table(matches, title))

    elif args.related_sector:
        matches = get_by_related_sector(data, args.related_sector)
        if not matches:
            print(f"No entries found with sector '{args.related_sector}' in related_sectors.")
            sys.exit(1)
        title = (
            f"Related sector: {args.related_sector}  —  {len(matches)} match(es)"
            f"  ({args.dataset}, {args.lang})"
        )
        print(fmt_list_table(matches, title))


if __name__ == "__main__":
    main()
