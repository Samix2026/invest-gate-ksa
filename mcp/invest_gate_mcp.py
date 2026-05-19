#!/usr/bin/env python3
"""
Invest Gate KSA — MCP Server (FastMCP / stdio transport)

Exposes 8 tools for querying the invest-gate-ksa knowledge base.
All responses include a legal disclaimer; unverified entries carry a
verification warning so the caller knows exactly what to confirm.

Usage:
    See mcp/README.md for Claude Desktop configuration.

Requirements:
    pip install mcp[cli] pydantic
"""

import importlib.util
import json
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

from mcp.server.fastmcp import FastMCP
from pydantic import BaseModel, Field

# ── Paths ─────────────────────────────────────────────────────────────────────

ROOT = Path(__file__).parent.parent


def _import_script(module_name: str, filename: str):
    path = ROOT / "scripts" / filename
    spec = importlib.util.spec_from_file_location(module_name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = mod
    spec.loader.exec_module(mod)
    return mod


_qd = _import_script("query_dataset", "query-dataset.py")
_qs = _import_script("query_structures", "query-structures.py")

# ── MCP server ────────────────────────────────────────────────────────────────

mcp = FastMCP("invest_gate_ksa_mcp")

# ── Constants ─────────────────────────────────────────────────────────────────

_LEGAL = (
    "DISCLAIMER: For general educational purposes only. Not legal, financial, "
    "regulatory, or tax advice. Requirements, fees, and eligibility rules change. "
    "Always verify with official Saudi government portals and consult qualified "
    "professionals before making any decision."
)

_FEES_PATHS: Dict[str, str] = {
    "en": str(ROOT / "data" / "fees.en.json"),
    "ar": str(ROOT / "data" / "fees.ar.json"),
}

_TIMELINES_PATHS: Dict[str, str] = {
    "en": str(ROOT / "data" / "timelines.en.json"),
    "ar": str(ROOT / "data" / "timelines.ar.json"),
}

_JSON_CACHE: Dict[str, dict] = {}

# ── Shared helpers ─────────────────────────────────────────────────────────────


def _load_json(path: str) -> dict:
    if path not in _JSON_CACHE:
        with open(path, encoding="utf-8") as fh:
            _JSON_CACHE[path] = json.load(fh)
    return _JSON_CACHE[path]


def _valid_lang(lang: str) -> str:
    return lang if lang in ("en", "ar") else "en"


def _dataset(name: str, lang: str) -> dict:
    return _qd.DataLoader.load(name, lang)


def _verify_warning(entry: dict) -> Optional[str]:
    if entry.get("verification_status") != "verified":
        vat = entry.get("verify_at", "")
        return f"⚠️ Unverified — confirm at: {vat}" if vat else "⚠️ Unverified"
    return None


def _clean(entry: dict) -> dict:
    """Return a serialisable entry with zero-amount placeholders suppressed."""
    out: dict = {}
    for k, v in entry.items():
        if v is None:
            continue
        if isinstance(v, list) and len(v) == 0:
            continue
        # Never surface amount_sar=0 as a fee amount when there is a placeholder_reason
        if k == "amount_sar" and v == 0 and entry.get("placeholder_reason"):
            continue
        out[k] = v
    warn = _verify_warning(entry)
    if warn:
        out["_verification_warning"] = warn
    if entry.get("placeholder_reason"):
        out["_note"] = entry["placeholder_reason"]
    return out


def _respond(data: Any) -> str:
    return json.dumps(
        {"result": data, "disclaimer": _LEGAL},
        ensure_ascii=False,
        indent=2,
    )


# ── Input models ───────────────────────────────────────────────────────────────


class QuerySectorsInput(BaseModel):
    sector_id: Optional[str] = Field(
        None, description="Sector ID (e.g. 'fintech', 'healthcare', 'manufacturing')"
    )
    regulatory_sensitivity: Optional[str] = Field(
        None,
        description="Filter by sensitivity: standard, regulated, highly_regulated, restricted",
    )
    tag: Optional[str] = Field(None, description="Tag to filter by")
    lang: str = Field("en", description="Language: 'en' or 'ar'")


class QueryAuthoritiesInput(BaseModel):
    authority_id: Optional[str] = Field(
        None, description="Authority ID (e.g. 'misa', 'zatca', 'gosi')"
    )
    authority_type: Optional[str] = Field(
        None,
        description=(
            "Authority type: government_ministry, government_authority, "
            "government_organization, government_portal, government_platform"
        ),
    )
    tag: Optional[str] = Field(None, description="Tag to filter by")
    lang: str = Field("en", description="Language: 'en' or 'ar'")


class QuerySetupFlowsInput(BaseModel):
    flow_id: Optional[str] = Field(
        None,
        description=(
            "Flow ID (e.g. 'foreign_consulting_company_setup', 'fintech_market_entry')"
        ),
    )
    related_sector: Optional[str] = Field(
        None, description="Filter by related sector ID (e.g. 'consulting', 'fintech')"
    )
    tag: Optional[str] = Field(None, description="Tag to filter by")
    lang: str = Field("en", description="Language: 'en' or 'ar'")


class QueryFeesInput(BaseModel):
    authority_id: Optional[str] = Field(
        None,
        description="Authority ID to filter by (e.g. 'misa', 'ministry_of_commerce', 'zatca')",
    )
    fee_type: Optional[str] = Field(
        None,
        description="Fee type: registration, renewal, issuance, amendment, certificate, inspection, other",
    )
    tag: Optional[str] = Field(None, description="Tag to filter by")
    lang: str = Field("en", description="Language: 'en' or 'ar'")
    exclude_historical: bool = Field(
        True, description="Exclude abolished/historical entries (default True)"
    )


class QueryTimelinesInput(BaseModel):
    authority_id: Optional[str] = Field(
        None, description="Authority ID to filter by"
    )
    process_id: Optional[str] = Field(
        None, description="Specific process ID to retrieve"
    )
    tag: Optional[str] = Field(None, description="Tag to filter by")
    lang: str = Field("en", description="Language: 'en' or 'ar'")


class QueryStructuresInput(BaseModel):
    structure_id: Optional[str] = Field(
        None,
        description=(
            "Structure ID or alias "
            "(e.g. 'llc', 'jsc', 'branch', 'branch_office', 'rep_office', 'representative_office')"
        ),
    )
    tag: Optional[str] = Field(None, description="Tag to filter by")
    lang: str = Field("en", description="Language: 'en' or 'ar'")


class GetInvestorPathInput(BaseModel):
    sector: str = Field(
        ...,
        description="Investment sector (e.g. 'fintech', 'consulting', 'manufacturing', 'healthcare')",
    )
    has_parent_company: bool = Field(
        ...,
        description="True if the investor has an established foreign parent company",
    )
    investor_type: str = Field(
        "sme",
        description="Investor profile: individual_entrepreneur, sme, multinational",
    )
    lang: str = Field("en", description="Language: 'en' or 'ar'")


class SearchKnowledgeBaseInput(BaseModel):
    query: str = Field(..., description="Search text to look for across datasets")
    datasets: Optional[List[str]] = Field(
        None,
        description=(
            "Datasets to search (default: all). Options: "
            "business-structures, investment-licenses, sources, sectors, "
            "source-gaps, authority-relationships, setup-flows, fees, timelines"
        ),
    )
    lang: str = Field("en", description="Language: 'en' or 'ar'")
    max_results: int = Field(10, description="Max results per dataset (default 10)")


# ── Tools ──────────────────────────────────────────────────────────────────────


@mcp.tool()
def query_sectors(params: QuerySectorsInput) -> str:
    """Query investment sectors. Returns sector data including regulatory sensitivity,
    typical business models, relevant authorities, and common confusions."""
    data = _dataset("sectors", _valid_lang(params.lang))
    if params.sector_id:
        entry = _qd.get_by_id(data, params.sector_id)
        entries = [entry] if entry else []
    elif params.regulatory_sensitivity:
        entries = _qd.get_by_regulatory_sensitivity(data, params.regulatory_sensitivity)
    elif params.tag:
        entries = _qd.get_by_tag(data, params.tag)
    else:
        entries = _qd.list_all(data)
    results = [_clean(e) for e in entries]
    return _respond(results if results else {"message": "No sectors matched."})


@mcp.tool()
def query_authorities(params: QueryAuthoritiesInput) -> str:
    """Query official Saudi government authorities and portals relevant to foreign
    investors. Returns registration bodies, tax authorities, labor platforms, and
    open data portals with official websites and documentation sections."""
    data = _dataset("sources", _valid_lang(params.lang))
    if params.authority_id:
        entry = _qd.get_by_id(data, params.authority_id)
        entries = [entry] if entry else []
    elif params.authority_type:
        entries = _qd.get_by_authority_type(data, params.authority_type)
    elif params.tag:
        entries = _qd.get_by_tag(data, params.tag)
    else:
        entries = _qd.list_all(data)
    results = [_clean(e) for e in entries]
    return _respond(results if results else {"message": "No authorities matched."})


@mcp.tool()
def query_setup_flows(params: QuerySetupFlowsInput) -> str:
    """Query conceptual setup flows for common foreign investment scenarios
    (consulting company, e-commerce, manufacturing, fintech). Returns step-by-step
    flows with authority references and decision points.
    Informational only — not procedural instructions or legal requirements."""
    data = _dataset("setup-flows", _valid_lang(params.lang))
    if params.flow_id:
        entry = _qd.get_by_id(data, params.flow_id)
        entries = [entry] if entry else []
    elif params.related_sector:
        entries = _qd.get_by_related_sector(data, params.related_sector)
    elif params.tag:
        entries = _qd.get_by_tag(data, params.tag)
    else:
        entries = _qd.list_all(data)
    results = [_clean(e) for e in entries]
    return _respond(results if results else {"message": "No setup flows matched."})


@mcp.tool()
def query_fees(params: QueryFeesInput) -> str:
    """Query government fees for registration, licensing, and certification.
    Unverified amounts are suppressed — the _note field shows the placeholder_reason
    explaining the actual fee structure. Always confirm fees with official sources
    before budgeting."""
    lang = _valid_lang(params.lang)
    raw = _load_json(_FEES_PATHS[lang])
    entries: list = raw.get("data", [])

    if params.exclude_historical:
        entries = [e for e in entries if "historical" not in e.get("tags", [])]
    if params.authority_id:
        entries = [e for e in entries if e.get("authority_id") == params.authority_id]
    if params.fee_type:
        entries = [e for e in entries if e.get("fee_type") == params.fee_type]
    if params.tag:
        entries = [e for e in entries if params.tag in e.get("tags", [])]

    results = [_clean(e) for e in entries]
    return _respond(results if results else {"message": "No fee entries matched."})


@mcp.tool()
def query_timelines(params: QueryTimelinesInput) -> str:
    """Query processing timelines for key government procedures including MISA
    registration, commercial registration, work permits, and residency permits.
    Returns estimated business-day durations with conditions and verification status."""
    lang = _valid_lang(params.lang)
    raw = _load_json(_TIMELINES_PATHS[lang])
    entries: list = raw.get("data", [])

    if params.process_id:
        entries = [e for e in entries if e.get("id") == params.process_id]
    elif params.authority_id:
        entries = [e for e in entries if e.get("authority_id") == params.authority_id]
    elif params.tag:
        entries = [e for e in entries if params.tag in e.get("tags", [])]

    results = [_clean(e) for e in entries]
    return _respond(results if results else {"message": "No timeline entries matched."})


@mcp.tool()
def query_structures(params: QueryStructuresInput) -> str:
    """Query legal entity structures available to foreign investors in Saudi Arabia:
    LLC, JSC, Branch Office, Representative Office. Supports aliases —
    'branch' resolves to 'foreign_branch', 'rep_office' to 'representative_office', etc."""
    lang = _valid_lang(params.lang)
    data = _qs.DataLoader.load(lang=lang)
    if params.structure_id:
        resolved = _qs.resolve_alias(params.structure_id)
        entry = _qs.get_by_id(data, resolved)
        entries = [entry] if entry else []
    elif params.tag:
        entries = _qs.get_by_tag(data, params.tag)
    else:
        entries = _qs.list_all(data)
    results = [_clean(e) for e in entries]
    return _respond(results if results else {"message": "No business structures matched."})


@mcp.tool()
def get_investor_path(params: GetInvestorPathInput) -> str:
    """Build a contextual investor path overview for a given sector, parent company
    status, and investor type. Cross-queries sectors, setup-flows, business structures,
    and fees datasets to surface a structured starting point.
    All output is informational only — not legal or procedural guidance."""
    lang = _valid_lang(params.lang)

    sectors_data = _dataset("sectors", lang)
    sector_entry = _qd.get_by_id(sectors_data, params.sector)

    flows_data = _dataset("setup-flows", lang)
    related_flows = _qd.get_by_related_sector(flows_data, params.sector)

    struct_data = _qs.DataLoader.load(lang=lang)
    all_structs = _qs.list_all(struct_data)
    if not params.has_parent_company:
        relevant_structs = [
            e for e in all_structs
            if e["id"] not in ("foreign_branch", "representative_office")
        ]
    elif params.investor_type == "multinational":
        relevant_structs = all_structs
    else:
        relevant_structs = [
            e for e in all_structs if e["id"] != "representative_office"
        ]

    fees_raw = _load_json(_FEES_PATHS[lang])
    misa_fee = next(
        (e for e in fees_raw.get("data", []) if e.get("id") == "misa_investment_registration_fee"),
        None,
    )

    notes: List[str] = []
    if not params.has_parent_company and params.investor_type == "individual_entrepreneur":
        notes.append(
            "Without a foreign parent company, the Entrepreneurial License may apply "
            "for innovative or tech-enabled businesses. Requires a support letter from "
            "a MISA-recognised incubator, accelerator, or VC. Verify eligibility at "
            "misa.gov.sa."
        )
    if params.investor_type == "multinational":
        notes.append(
            "Multinationals may qualify for a Regional Headquarters (RHQ) License in "
            "addition to standard investment registration. The RHQ cannot generate "
            "direct commercial revenue — it covers management functions only. "
            "Verify at investsaudi.sa."
        )
    if sector_entry and sector_entry.get("regulatory_sensitivity") in (
        "highly_regulated", "restricted"
    ):
        notes.append(
            f"Sector '{params.sector}' is classified as "
            f"'{sector_entry['regulatory_sensitivity']}'. Additional authority "
            "approvals are likely required and MISA registration may take longer."
        )

    path = {
        "investor_context": {
            "sector": params.sector,
            "has_parent_company": params.has_parent_company,
            "investor_type": params.investor_type,
        },
        "sector_overview": (
            _clean(sector_entry)
            if sector_entry
            else {"_note": f"Sector '{params.sector}' not found in dataset."}
        ),
        "available_structures": [_clean(e) for e in relevant_structs],
        "related_setup_flows": [_clean(e) for e in related_flows],
        "misa_registration_fee": _clean(misa_fee) if misa_fee else None,
        "pathway_notes": notes,
    }
    return _respond(path)


@mcp.tool()
def search_knowledge_base(params: SearchKnowledgeBaseInput) -> str:
    """Full-text search across one or more knowledge base datasets. Searches id, name,
    description, notes, tags, and other text fields. Returns matched entries grouped by
    dataset, each with verification warnings where applicable."""
    query = params.query.lower()
    lang = _valid_lang(params.lang)
    limit = max(1, params.max_results)

    _CORE = [
        "business-structures",
        "investment-licenses",
        "sources",
        "sectors",
        "source-gaps",
        "authority-relationships",
        "setup-flows",
    ]
    targets = params.datasets or (_CORE + ["fees", "timelines"])
    core_targets = [d for d in targets if d in _CORE]
    want_fees = "fees" in targets
    want_timelines = "timelines" in targets

    _SEARCH_FIELDS = [
        "id", "name", "description", "notes", "title", "label",
        "conceptual_description", "process_name", "placeholder_reason",
        "short_description",
    ]

    def _hits(entry: dict) -> bool:
        for field in _SEARCH_FIELDS:
            val = entry.get(field)
            if isinstance(val, str) and query in val.lower():
                return True
        return any(query in t.lower() for t in entry.get("tags", []))

    results: Dict[str, list] = {}

    for ds in core_targets:
        try:
            data = _dataset(ds, lang)
            matched = [_clean(e) for e in data.get("data", []) if _hits(e)][:limit]
            if matched:
                results[ds] = matched
        except SystemExit:
            pass

    if want_fees:
        raw = _load_json(_FEES_PATHS[lang])
        matched = [_clean(e) for e in raw.get("data", []) if _hits(e)][:limit]
        if matched:
            results["fees"] = matched

    if want_timelines:
        raw = _load_json(_TIMELINES_PATHS[lang])
        matched = [_clean(e) for e in raw.get("data", []) if _hits(e)][:limit]
        if matched:
            results["timelines"] = matched

    if not results:
        return _respond({"message": f"No results found for: '{params.query}'"})
    return _respond(results)


# ── Entry point ────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    mcp.run(transport="stdio")
