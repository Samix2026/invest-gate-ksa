#!/usr/bin/env python3
"""
Invest Gate KSA — MCP Server (FastMCP / stdio transport)

Exposes 10 tools for querying the invest-gate-ksa knowledge base.
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

_SEZS_PATHS: Dict[str, str] = {
    "en": str(ROOT / "data" / "sezs.en.json"),
    "ar": str(ROOT / "data" / "sezs.ar.json"),
}

_ACTIVITIES_PATHS: Dict[str, str] = {
    "en": str(ROOT / "data" / "economic-activities.en.json"),
    "ar": str(ROOT / "data" / "economic-activities.ar.json"),
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
        description=(
            "Investor profile: foreign_individual, foreign_company, "
            "individual_entrepreneur, sme, multinational"
        ),
    )
    lang: str = Field("en", description="Language: 'en' or 'ar'")


class QuerySezsInput(BaseModel):
    sez_id: Optional[str] = Field(
        None, description="SEZ ID (e.g. 'kaec_sez', 'jazan_sez', 'ras_al_khair_sez', 'cloud_computing_sez', 'silz')"
    )
    tag: Optional[str] = Field(None, description="Tag to filter by (e.g. 'verified', 'logistics', 'maritime')")
    lang: str = Field("en", description="Language: 'en' or 'ar'")


class QueryActivitiesInput(BaseModel):
    keyword: Optional[str] = Field(
        None,
        description="Search text matched against activity name, short description, and notes (both EN and AR).",
    )
    isic4_code: Optional[str] = Field(
        None, description="Filter by 4-digit ISIC4 class code (e.g. '7020', '6201', '8621')."
    )
    foreign_ownership_allowed: Optional[bool] = Field(
        None, description="Filter by ownership openness: true = open to foreign investment, false = restricted/excluded."
    )
    regulatory_sensitivity: Optional[str] = Field(
        None, description="Filter by regulatory burden: 'low', 'medium', or 'high'."
    )
    lang: str = Field("en", description="Language: 'en' or 'ar'")


class SearchKnowledgeBaseInput(BaseModel):
    query: str = Field(..., description="Search text to look for across datasets")
    datasets: Optional[List[str]] = Field(
        None,
        description=(
            "Datasets to search (default: all). Options: "
            "business-structures, investment-licenses, sources, sectors, "
            "source-gaps, authority-relationships, setup-flows, fees, timelines, sezs, economic-activities"
        ),
    )
    lang: str = Field("en", description="Language: 'en' or 'ar'")
    max_results: int = Field(10, description="Max results per dataset (default 10)")


# ── Tools ──────────────────────────────────────────────────────────────────────


_V2030_BADGES = {
    "critical":   "🎯 Critical",
    "high":       "🔵 High",
    "medium":     "⚪ Medium",
    "supporting": "⚪ Supporting",
}


def _enrich_sector(entry: dict) -> dict:
    """Add Vision 2030 summary fields to a sector entry for display."""
    result = dict(entry)
    priority = entry.get("vision2030_priority")
    if priority:
        result["vision2030_priority_display"] = _V2030_BADGES.get(priority, priority)
    # Drop null V2030 fields to keep output clean
    for field in ("vision2030_target_en", "vision2030_target_ar",
                  "supervising_vision_entity_en", "supervising_vision_entity_ar",
                  "fdi_target_usd_billion", "vision2030_verify_at"):
        if result.get(field) is None:
            result.pop(field, None)
    return result


@mcp.tool()
def query_sectors(params: QuerySectorsInput) -> str:
    """Query investment sectors. Returns sector data including regulatory sensitivity,
    typical business models, relevant authorities, common confusions, and Vision 2030
    priority / targets where available (🎯 Critical / 🔵 High / ⚪ Medium)."""
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
    results = [_enrich_sector(_clean(e)) for e in entries]
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
def query_sezs(params: QuerySezsInput) -> str:
    """Query Saudi Arabia's Special Economic Zones (SEZs): KAEC, Jazan, Ras Al-Khair,
    Cloud Computing SEZ, and SILZ. Returns tax incentives, qualifying activities,
    anchor infrastructure, and key distinctions between zones.
    All data is informational only — verify with ECZA and official sources."""
    lang = _valid_lang(params.lang)
    raw = _load_json(_SEZS_PATHS[lang])
    entries: list = raw.get("data", [])

    if params.sez_id:
        entries = [e for e in entries if e.get("id") == params.sez_id]
    elif params.tag:
        entries = [e for e in entries if params.tag in e.get("tags", [])]

    results = [_clean(e) for e in entries]
    return _respond(results if results else {"message": "No SEZ entries matched."})


@mcp.tool()
def query_activities(params: QueryActivitiesInput) -> str:
    """Query economic activities relevant to foreign investors in Saudi Arabia.
    Returns ISIC4 classification, foreign ownership allowance, ownership limits,
    regulatory sensitivity, relevant authorities, and common investor confusions.
    Covers open activities (100% foreign ownership), restricted activities, and
    excluded activities (reserved for Saudi nationals). Informational only —
    verify current approved-activities list with MISA before relying on this data."""
    lang = _valid_lang(params.lang)
    raw = _load_json(_ACTIVITIES_PATHS[lang])
    entries: list = raw.get("data", [])

    if params.isic4_code:
        entries = [
            e for e in entries
            if e.get("classification", {}).get("isic4", {}).get("class") == params.isic4_code
        ]
    if params.foreign_ownership_allowed is not None:
        entries = [
            e for e in entries
            if e.get("foreign_ownership_allowed") == params.foreign_ownership_allowed
        ]
    if params.regulatory_sensitivity:
        entries = [
            e for e in entries
            if e.get("regulatory_sensitivity") == params.regulatory_sensitivity
        ]
    if params.keyword:
        kw = params.keyword.lower()
        _kw_fields = ("name", "name_alt", "short_description", "notes")
        entries = [
            e for e in entries
            if any(kw in str(e.get(f, "")).lower() for f in _kw_fields)
            or any(kw in t.lower() for t in e.get("tags", []))
        ]

    results = [_clean(e) for e in entries]
    return _respond(results if results else {"message": "No activity entries matched."})


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

    fees_raw = _load_json(_FEES_PATHS[lang])
    misa_fee = next(
        (e for e in fees_raw.get("data", []) if e.get("id") == "misa_investment_registration_fee"),
        None,
    )

    # foreign_individual: eligibility gate — standard MISA registration requires an
    # established foreign company. Show the three concrete sub-paths; never default to
    # the generic LLC entry which would imply direct access.
    if params.investor_type == "foreign_individual":
        is_regulated = sector_entry and sector_entry.get("regulatory_sensitivity") in (
            "highly_regulated", "restricted"
        )
        if lang == "ar":
            warning = (
                "⚠️ تنبيه جوهري: المستثمر الفردي الأجنبي الذي لا تتوفر لديه شركة أجنبية قائمة "
                "(سجل تجاري + قوائم مالية معتمدة من السفارة السعودية) لا يستطيع التسجيل في وزارة "
                "الاستثمار عبر المسار الأساسي. "
                "المصدر: دليل المستثمر — وزارة الاستثمار، الطبعة الثانية عشرة، مارس 2025، القسم 3.1.1."
            )
            paths: Dict[str, Any] = {
                "path_a": {
                    "label": "المسار أ — لديه شركة أجنبية قائمة (سنة أو أكثر)",
                    "applicable_if": "شركة أجنبية بسجل تجاري وقوائم مالية مدققة معتمدة من السفارة السعودية",
                    "sequence": "تسجيل الاستثمار القياسي — السجل التجاري — الغرفة التجارية — ZATCA — GOSI — قوى — مقيم",
                    "note": "يجب أن تكون الشركة قائمة منذ سنة على الأقل مع سجل تجاري وقوائم مالية مدققة معتمدة.",
                    "source": "دليل المستثمر — وزارة الاستثمار، الطبعة الثانية عشرة، مارس 2025، القسم 3.1.1",
                },
                "path_b": {
                    "label": "المسار ب — حامل الإقامة المميزة",
                    "applicable_if": "يحمل المستثمر إقامة مميزة سعودية",
                    "sequence": "تسجيل الاستثمار القياسي (إعفاء من الوثائق) — السجل التجاري — الغرفة التجارية — ZATCA — GOSI — قوى — مقيم",
                    "note": "حاملو الإقامة المميزة معفيون من تقديم السجل التجاري والقوائم المالية وفق القسم 3.1.1.",
                    "source": "دليل المستثمر — وزارة الاستثمار، الطبعة الثانية عشرة، مارس 2025، القسم 3.1.1",
                },
                "path_c": {
                    "label": "المسار ج — قطاع مبتكر أو تقني + دعم من حاضنة أو رأسمال مغامر معتمد",
                    "applicable_if": "نشاط مبتكر أو يعتمد التقنية + خطاب دعم من جهة معتمدة لدى وزارة الاستثمار",
                    "sequence": "تسجيل ريادي — السجل التجاري — الغرفة التجارية — ZATCA — GOSI — قوى — مقيم",
                    "note": "يستلزم خطاب دعم من جهة معتمدة. الرسم: 2,000 ريال سعودي/سنوياً (السنوات 1–3). غير متاح للأعمال التقليدية.",
                    "source": "دليل المستثمر — وزارة الاستثمار، الطبعة الثانية عشرة، مارس 2025، القسم 3.1.1",
                },
                "path_d": {
                    "label": "لا ينطبق أي من المسارات السابقة",
                    "guidance": (
                        "لا يتوفر مسار مباشر حالياً عبر وزارة الاستثمار. "
                        "الخيارات المتاحة: (1) تأسيس شركة خارج المملكة والانتظار سنة كاملة قبل التقديم، "
                        "(2) التقديم للإقامة المميزة إذا توفرت الشروط، "
                        "(3) إذا كان النشاط مبتكراً والحصول على دعم من حاضنة أعمال معتمدة."
                    ),
                    "note": "فجوة موثقة. راجع source-gaps/foreign_individual_no_company_pathway.",
                },
            }
            sector_note = (
                f"قطاع '{params.sector}' يستلزم ترخيصاً قطاعياً إضافياً بجانب تسجيل وزارة الاستثمار. "
                "تواصل مع الجهة التنظيمية القطاعية المختصة في مرحلة مبكرة من العملية."
            ) if is_regulated else None
        else:
            warning = (
                "⚠️ IMPORTANT: Standard MISA Investment Registration requires (1) commercial "
                "registration of the applicant's foreign establishment authenticated by the Saudi "
                "Embassy, and (2) audited financial statements for the last fiscal year. "
                "Foreign individuals WITHOUT an established foreign company (minimum 1 year of "
                "operation) do NOT qualify for standard registration. "
                "Source: MISA Investor Guide 12th Edition, March 2025, §3.1.1."
            )
            paths = {
                "path_a": {
                    "label": "Path A — Has established foreign company (1+ year)",
                    "applicable_if": "Foreign company with CR and audited financials authenticated by Saudi Embassy",
                    "sequence": "Standard Investment Registration → CR → Chamber of Commerce → ZATCA → GOSI → Qiwa → Muqeem",
                    "note": "Company must have been established for at least 1 year with CR and audited financials authenticated by the Saudi Embassy.",
                    "source": "MISA Investor Guide 12th Edition, March 2025, §3.1.1",
                },
                "path_b": {
                    "label": "Path B — Premium Residency holder",
                    "applicable_if": "Investor holds Saudi Premium Residency",
                    "sequence": "Standard Investment Registration (documents waived) → CR → Chamber of Commerce → ZATCA → GOSI → Qiwa → Muqeem",
                    "note": "Premium Residency holders are exempt from submitting CR and financial statements per MISA Investor Guide §3.1.1.",
                    "source": "MISA Investor Guide 12th Edition, March 2025, §3.1.1",
                },
                "path_c": {
                    "label": "Path C — Innovative/tech sector + VC or incubator backing",
                    "applicable_if": "Business is innovative/tech-enabled and investor has support letter from MISA-recognized entity",
                    "sequence": "Entrepreneurial Registration → CR → Chamber of Commerce → ZATCA → GOSI → Qiwa → Muqeem",
                    "note": "Requires support letter from MISA-recognized entity. Fee: SAR 2,000/year (years 1-3). Not available for traditional businesses.",
                    "source": "MISA Investor Guide 12th Edition, March 2025, §3.1.1",
                },
                "path_d": {
                    "label": "Path D — None of the above apply",
                    "guidance": (
                        "No direct MISA pathway currently available. "
                        "Options: (1) Establish a foreign company and wait 1 full year before applying. "
                        "(2) Apply for Saudi Premium Residency if eligible. "
                        "(3) If the business is innovative and you can secure incubator/VC backing, "
                        "consider Entrepreneurial Registration."
                    ),
                    "note": "This is a documented limitation. See source-gaps/foreign_individual_no_company_pathway.",
                },
            }
            sector_note = (
                f"Sector '{params.sector}' requires additional sectoral licensing beyond "
                "standard investment registration. Contact the relevant sectoral authority "
                "early in the process."
            ) if is_regulated else None

        if lang == "ar":
            post_reg = (
                "## خدمات ما بعد التسجيل\n"
                "**برنامج ميزة** (مجاني): وصول لـ 12 محفظة خدمية تشمل دعم دخول السوق والمواهب "
                "والاستشارات القانونية والخدمات الرقمية. التسجيل عبر: investsaudi.sa\n"
                "**برنامج المستثمر الاستراتيجي**: دعم متميز مع مدير علاقات مخصص وتسهيل الإقامة "
                "المميزة والاستشارات التشريعية. حسب الأهلية. التقديم عبر: investsaudi.sa"
            )
        else:
            post_reg = (
                "## Post-Registration Support\n"
                "**Miza Program** (free): Access 12 service portfolios including market entry "
                "support, talent solutions, legal advisory, and digital services. "
                "Register at: investsaudi.sa\n"
                "**Strategic Investor Program**: Premium support with dedicated relationship "
                "manager, premium residency facilitation, and legislative advisory. "
                "Eligibility-based. Apply at: investsaudi.sa"
            )

        path: Dict[str, Any] = {
            "investor_context": {
                "sector": params.sector,
                "has_parent_company": params.has_parent_company,
                "investor_type": params.investor_type,
            },
            "eligibility_warning": warning,
            "registration_paths": paths,
            "sector_overview": (
                _clean(sector_entry)
                if sector_entry
                else {"_note": f"Sector '{params.sector}' not found in dataset."}
            ),
            "misa_registration_fee": _clean(misa_fee) if misa_fee else None,
            "post_registration_support": post_reg,
        }
        if sector_note:
            path["sector_note"] = sector_note
        return _respond(path)

    # General path for all other investor types
    flows_data = _dataset("setup-flows", lang)
    related_flows = _qd.get_by_related_sector(flows_data, params.sector)

    struct_data = _qs.DataLoader.load(lang=lang)
    all_structs = _qs.list_all(struct_data)
    if params.investor_type == "foreign_company":
        # Foreign company can establish a new LLC presence or extend via Branch.
        relevant_structs = [
            e for e in all_structs
            if e["id"] in ("llc", "foreign_branch")
        ]
    elif not params.has_parent_company:
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

    notes: List[str] = []

    # Type-specific notes — only add what is relevant to this investor type.
    if params.investor_type == "individual_entrepreneur" and not params.has_parent_company:
        notes.append(
            "Without a foreign parent company, the Entrepreneurial License may apply "
            "for innovative or tech-enabled businesses. Requires a support letter from "
            "a MISA-recognised incubator, accelerator, or VC. Verify eligibility at "
            "misa.gov.sa."
        )
    elif params.investor_type == "multinational":
        notes.append(
            "Multinationals may qualify for a Regional Headquarters (RHQ) License in "
            "addition to standard investment registration. The RHQ cannot generate "
            "direct commercial revenue — it covers management functions only. "
            "Verify at investsaudi.sa."
        )
    elif params.investor_type == "foreign_company" and params.sector in ("consulting",):
        # RHQ is relevant only for foreign companies with regional management operations.
        notes.append(
            "For regional management operations, a Regional Headquarters (RHQ) License "
            "may also be an option. Verify eligibility at investsaudi.sa."
        )

    # Sectoral note: surface the additional licensing layer only.
    if sector_entry and sector_entry.get("regulatory_sensitivity") in (
        "highly_regulated", "restricted"
    ):
        notes.append(
            f"Sector '{params.sector}' requires additional sectoral licensing beyond "
            "standard investment registration. Contact the relevant sectoral authority "
            "early in the process."
        )

    if lang == "ar":
        post_reg = (
            "## خدمات ما بعد التسجيل\n"
            "**برنامج ميزة** (مجاني): وصول لـ 12 محفظة خدمية تشمل دعم دخول السوق والمواهب "
            "والاستشارات القانونية والخدمات الرقمية. التسجيل عبر: investsaudi.sa\n"
            "**برنامج المستثمر الاستراتيجي**: دعم متميز مع مدير علاقات مخصص وتسهيل الإقامة "
            "المميزة والاستشارات التشريعية. حسب الأهلية. التقديم عبر: investsaudi.sa"
        )
    else:
        post_reg = (
            "## Post-Registration Support\n"
            "**Miza Program** (free): Access 12 service portfolios including market entry "
            "support, talent solutions, legal advisory, and digital services. "
            "Register at: investsaudi.sa\n"
            "**Strategic Investor Program**: Premium support with dedicated relationship "
            "manager, premium residency facilitation, and legislative advisory. "
            "Eligibility-based. Apply at: investsaudi.sa"
        )

    result: Dict[str, Any] = {
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
        "post_registration_support": post_reg,
    }
    return _respond(result)


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
    targets = params.datasets or (_CORE + ["fees", "timelines", "sezs", "economic-activities"])
    core_targets = [d for d in targets if d in _CORE]
    want_fees = "fees" in targets
    want_timelines = "timelines" in targets
    want_sezs = "sezs" in targets
    want_activities = "economic-activities" in targets

    _SEARCH_FIELDS = [
        "id", "name", "name_alt", "description", "notes", "title", "label",
        "conceptual_description", "process_name", "placeholder_reason",
        "short_description",
        "name_en", "name_ar", "notes_en", "notes_ar",
        "strategic_advantage_en", "strategic_advantage_ar",
    ]

    def _hits(entry: dict) -> bool:
        for field in _SEARCH_FIELDS:
            val = entry.get(field)
            if isinstance(val, str) and query in val.lower():
                return True
        if any(query in t.lower() for t in entry.get("tags", [])):
            return True
        return any(
            query in item.lower()
            for field in ("qualifying_activities",)
            for item in entry.get(field, [])
            if isinstance(item, str)
        )

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

    if want_sezs:
        raw = _load_json(_SEZS_PATHS[lang])
        matched = [_clean(e) for e in raw.get("data", []) if _hits(e)][:limit]
        if matched:
            results["sezs"] = matched

    if want_activities:
        raw = _load_json(_ACTIVITIES_PATHS[lang])
        matched = [_clean(e) for e in raw.get("data", []) if _hits(e)][:limit]
        if matched:
            results["economic-activities"] = matched

    if not results:
        return _respond({"message": f"No results found for: '{params.query}'"})
    return _respond(results)


# ── Entry point ────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    mcp.run(transport="stdio")
