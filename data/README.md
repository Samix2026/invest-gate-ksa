# Data Directory

This directory holds structured, machine-readable data derived from official sources.

> **Important:** All data must be sourced from official government publications, announcements, or verifiable public records. Never add invented or estimated values. Each dataset must include a source reference and a `last_verified` date.

---

## Datasets

| File | Description | Status |
|------|-------------|--------|
| `business-structures.en.json` | Legal entity types available to foreign investors — English | Draft |
| `business-structures.ar.json` | Legal entity types available to foreign investors — Arabic | Draft |
| `investment-licenses.en.json` | Investment licensing concepts (MISA, CR, municipal, VAT, GOSI) — English | Draft |
| `investment-licenses.ar.json` | Investment licensing concepts — Arabic | Draft |
| `sources.en.json` | Official source registry: government bodies, portals, and platforms — English | Draft |
| `sources.ar.json` | Official source registry — Arabic | Draft |
| `sectors.en.json` | Investment sectors: regulatory context, likely authorities, common confusions — English | Draft |
| `sectors.ar.json` | Investment sectors — Arabic | Draft |
| `source-gaps.en.json` | Authorities referenced in other datasets not yet verified in the sources registry — English | Draft |
| `source-gaps.ar.json` | Source gaps registry — Arabic | Draft |
| `authority-relationships.en.json` | Conceptual relationships between regulatory authorities in the Saudi investment context — English | Draft |
| `authority-relationships.ar.json` | Conceptual authority relationships — Arabic | Draft |
| `setup-flows.en.json` | Conceptual setup flows for common foreign investment scenarios — English | Draft |
| `setup-flows.ar.json` | Conceptual setup flows — Arabic | Draft |
| `fees.en.json` | Official government fees (registration, licensing, permits) — English | Draft |
| `fees.ar.json` | Official government fees — Arabic | Draft |
| `timelines.en.json` | Estimated processing durations for key procedures — English | Draft |
| `timelines.ar.json` | Estimated processing durations — Arabic | Draft |
| `sezs.en.json` | Special Economic Zones: tax incentives, sectors, infrastructure (ECZA) — English | Draft/Verified |
| `sezs.ar.json` | Special Economic Zones — Arabic | Draft/Verified |
| `economic-activities.en.json` | Economic activities: ISIC4 classification, foreign ownership limits, regulatory sensitivity — English | Draft/Verified |
| `economic-activities.ar.json` | Economic activities — Arabic | Draft/Verified |

---

## Schema Convention

Each JSON file should follow this pattern:

```json
{
  "meta": {
    "title": "Human-readable dataset name",
    "description": "What this dataset contains",
    "source": "Official source name and URL",
    "last_verified": "YYYY-MM-DD",
    "language": "en | ar | bilingual"
  },
  "data": []
}
```

---

## Field-level provenance (`business-structures`, `investment-licenses`, `fees`, `timelines`)

Entries in these datasets may carry two **optional** provenance properties so
that per-field verification state is structured and queryable (rather than buried
in free-text `notes`):

- `verification_method` — string. Free text describing what official source text
  was reviewed for the entry.
- `field_verifications` — array of objects, one per individually confirmed field:

```json
{
  "field": "minimum_capital",
  "value_summary": "Minimum issued capital SAR 500,000; at least one quarter paid up on incorporation.",
  "source": "Companies Law, Royal Decree No. M/132 (2022), official English translation by the Bureau of Experts at the Council of Ministers (misa.gov.sa)",
  "citation": "Art. 59: 'The issued capital of a joint-stock company shall not be less than five hundred thousand riyals and its paid-up capital upon incorporation shall not be less than a quarter of said capital.'",
  "verified_on": "2026-06-14"
}
```

These fields are optional and do **not** change an entry's `verification_status`.
An entry may record `field_verifications` for confirmed fields while remaining
`draft` because it still has open `placeholders`. The schemas keep
`additionalProperties: false`; unknown keys are still rejected.

---

## Validation

All datasets with a corresponding JSON Schema can be validated with the project's validation script.

**Requirements:** Python 3.10+ and the `jsonschema` package.

```bash
# Install dependency
pip install -r scripts/requirements.txt

# Run all checks
python3 scripts/validate-data.py
```

The script enforces the following rules:

| Check | Scope |
|---|---|
| JSON Schema compliance | Per file — structure, required fields, enum values |
| `official_sources` not empty | Per entry — every entry must cite at least one official source |
| `placeholders` present when `draft` | Per entry — draft entries must declare what needs verification |
| ID parity (same IDs, same order) | Cross-file — EN and AR files must be structurally mirrored |

Exit code `0` means all checks passed. Exit code `1` means at least one check failed, with details printed to stdout. Suitable for use in CI pipelines.

JSON Schemas live at `schemas/` — one per dataset: `business-structures`, `investment-licenses`, `sources`, `sectors`, `source-gaps`, `authority-relationships`, `setup-flows`, `fees`, `timelines`, `sezs`, and `economic-activities`.

---

## Adding Data

1. Create a new JSON file following the schema convention above.
2. Add an entry to the Datasets table in this README.
3. Add a source entry in [`../sources/index.md`](../sources/index.md).
4. Run `python3 scripts/validate-data.py` to confirm the file passes validation.
5. Keep data neutral and descriptive — no interpretation or advice.
