# CLAUDE.md — AI Assistant Context

This file provides context for AI assistants (Claude Code, MCP clients, RAG systems) working in this repository.

---

## What This Repository Is

**Invest Gate KSA** is a bilingual (Arabic/English), open-source knowledge repository about investing and doing business in Saudi Arabia. It is structured for both human contributors and AI consumption. The long-term goal is to serve as the knowledge base for an MCP server and conversational AI assistant.

**What it is:** A structured reference framework for foreign investors — accurate, source-linked, and auditable.

**What it is not:** Legal advice, financial advice, or a regulatory filing service. No content in this repository should be read as a substitute for professional counsel.

---

## Content Constraints

These constraints apply to all content generation, editing, and responses in this repository:

- **No legal advice.** Never characterize something as required, permitted, or prohibited without a cited official source.
- **No fabricated data.** Do not invent fees, thresholds, timelines, processing durations, or ownership percentages. If a value is unknown, use a placeholder.
- **No fabricated URLs.** Do not construct or guess URLs for government portals. Record only domains confirmed from official sources.
- **No speculative requirements.** Do not add "typically" or "usually" language around procedural steps unless directly supported by cited sources.
- **Official sources only.** All factual claims must trace to a `.gov.sa` domain or an officially recognized national authority. Third-party summaries, consultant guides, and news articles are not citable sources.
- **Placeholder discipline.** Any field that cannot be verified must contain a `placeholder` entry, not a guess.
- **Educational tone.** Describe processes and structures; do not advise on which option to choose.
- **Bilingual parity.** Every English document and dataset entry must have a corresponding Arabic equivalent with the same IDs, same structure, and the same verification status.

---

## Repository Layout

```
invest-gate-ksa/
├── CLAUDE.md              ← this file
├── README.md              ← project overview (English)
├── README.ar.md           ← project overview (Arabic)
├── CONTRIBUTING.md        ← contribution guidelines
├── roadmap.md             ← development phases and task list
├── LICENSE
│
├── data/                  ← structured JSON datasets
│   ├── business-structures.en.json
│   ├── business-structures.ar.json
│   ├── investment-licenses.en.json
│   ├── investment-licenses.ar.json
│   ├── sources.en.json
│   ├── sources.ar.json
│   └── README.md          ← dataset index and schema convention
│
├── schemas/               ← JSON Schema Draft-07 for each dataset
│   ├── business-structures.schema.json
│   ├── investment-licenses.schema.json
│   └── sources.schema.json
│
├── docs/
│   ├── en/                ← English narrative documentation
│   │   ├── README.md
│   │   ├── company-setup-overview.md
│   │   └── source-verification.md
│   └── ar/                ← Arabic documentation (mirrors en/)
│       ├── README.md
│       ├── company-setup-overview.md
│       └── source-verification.md
│
├── templates/             ← fill-in forms for contributors
│   └── source-review.md   ← verification review record template
│
├── sources/
│   └── index.md           ← registry of all official sources cited
│
├── examples/
│   └── query-examples.md  ← example CLI query commands
│
├── prompts/
│   └── README.md          ← AI prompt and MCP tool definitions (planned)
│
└── scripts/
    ├── check.py            ← project health check (4 suites)
    ├── validate-data.py    ← JSON Schema + semantic dataset validation
    ├── query-structures.py ← query the business-structures dataset
    ├── query-dataset.py    ← generic query for any dataset
    └── requirements.txt    ← Python dependencies (jsonschema)
```

---

## Available Datasets

All datasets follow the same top-level structure:
```json
{
  "meta": { "title": "...", "description": "...", "language": "en|ar", "last_verified": "..." },
  "data": [ /* array of entries */ ]
}
```

Every entry has:
- `id` — unique string identifier, same in EN and AR files
- `verification_status` — `"draft"` (not yet verified) or `"verified"` (personally reviewed against live source)
- `placeholders` — array of `{field, description, verify_at}` objects; **must be non-empty when status is `"draft"`**
- `last_verified` — `YYYY-MM-DD` date string or a placeholder string
- `tags` — array of string tags for filtering

### `business-structures` (4 entries)

Entity types available to foreign investors: LLC, JSC, Branch Office, Representative Office.

Key fields: `name`, `abbreviation`, `ownership_structure`, `liability`, `minimum_requirements`, `regulatory_bodies`, `official_sources`, `aliases`.

Query: `python3 scripts/query-structures.py --list|--id LLC|--tag branch`

### `investment-licenses` (5 entries)

Registration and licensing concepts in the typical setup sequence: `misa_license`, `commercial_registration`, `municipal_license`, `vat_registration`, `gosi_registration`.

Note: The `misa_license` entry is now titled "MISA Investment Registration" — older terms ("investment license", "MISA license") are treated as legacy terminology. All other entries retain "license" where the concept genuinely is a license (municipal, municipality operating).

Key fields: `issuing_authority` (object with `id`, `name`, `portal`), `applies_to`, `depends_on` (conceptual only — IDs of prior entries), `common_confusions`.

Query: `python3 scripts/query-dataset.py --dataset investment-licenses --lang en --list`

### `sources` (10 entries)

Official Saudi government bodies, authorities, and platforms relevant to investors: MISA, Ministry of Commerce, ZATCA, MHRSD, GOSI, Saudi Business Center, Balady, Qiwa, Muqeem, Absher Business.

Key fields: `authority_type` (enum), `jurisdiction`, `official_website`, `documentation_sections`, `reliability_level` (enum), `notes`.

`authority_type` values: `government_ministry`, `government_authority`, `government_organization`, `government_portal`, `government_platform`.

Query: `python3 scripts/query-dataset.py --dataset sources --lang en --authority-type government_ministry`

### `sectors` (15 entries)

Investment sectors relevant to foreign investors: technology, consulting, ecommerce, food_and_beverage, real_estate, education, healthcare, fintech, manufacturing, industrial_services, mining, tourism_and_hospitality, media_and_content, hajj_umrah_services, entertainment_and_events.

Key fields: `typical_business_models` (array), `likely_authorities` (array of `{id, name, role}` objects), `related_license_concepts` (array of investment-licenses IDs), `regulatory_sensitivity` (enum), `common_confusions` (array).

`regulatory_sensitivity` values: `standard`, `regulated`, `highly_regulated`, `restricted`.

Note: `likely_authorities` items reference both confirmed sources (from `data/sources.en.json`) and sector-specific bodies not yet in the sources registry (CST, SFDA, REGA, MoE, MoH, SAMA, CMA, Ministry of Industry and Mineral Resources, MODON, Ministry of Tourism, Ministry of Media, Ministry of Interior, Ministry of Hajj and Umrah, NCEC, SAIP, GEA). The latter are marked in each entry's `placeholders` array.

Query: `python3 scripts/query-dataset.py --dataset sectors --lang en --regulatory-sensitivity highly_regulated`

### `authority-relationships` (12 entries)

Conceptual relationships between regulatory authorities in the Saudi investment context. All entries are architectural and informational only — not legal obligations or procedural requirements.

Key fields: `from_authority` (object: `{id, name}`), `to_authority` (object or null), `relationship_type` (enum), `relationship_direction` (enum), `conceptual_description`, `applies_to_sectors` (array), `examples` (array).

`relationship_type` values: `foundational_dependency`, `operational_dependency`, `sector_oversight`, `compliance_interaction`, `infrastructure_relationship`, `strategic_coordination`.

`relationship_direction` values: `unidirectional`, `bidirectional`, `contextual`.

Note: `to_authority` is `null` for horizontal compliance and service authorities (NCEC, SAIP, ZATCA) whose relationships are sector-spanning rather than authority-to-authority.

Query examples:
```bash
python3 scripts/query-dataset.py --dataset authority-relationships --list
python3 scripts/query-dataset.py --dataset authority-relationships --relationship-type sector_oversight
python3 scripts/query-dataset.py --dataset authority-relationships --from-authority misa
python3 scripts/query-dataset.py --dataset authority-relationships --to-authority ministry_of_commerce
python3 scripts/query-dataset.py --dataset authority-relationships --sector fintech
```

### `setup-flows` (4 entries)

Conceptual setup flows for common foreign investment scenarios in Saudi Arabia. All flows are architectural and informational only — not procedural instructions, approval timelines, or legal requirements.

Flows: `foreign_consulting_company_setup`, `ecommerce_company_setup`, `manufacturing_company_setup`, `fintech_market_entry`.

Key fields: `target_investor_type` (string), `related_sectors` (array of sector IDs), `steps` (array of step objects), `decision_points` (array of branching decisions), `related_authorities` (array of `{id, name, role}`), `source_dependencies` (array of `{dataset, entry_id, description}`).

Step fields: `step_number`, `label`, `description`, `authority` (object or null), `depends_on_step` (integer or null), `notes` (string or null).

Note: All entries are `"draft"`. Steps reference authority IDs from `sources` and `source-gaps` datasets; `source_dependencies` cross-reference entries in `investment-licenses`, `authority-relationships`, and `sectors`.

Query examples:
```bash
python3 scripts/query-dataset.py --dataset setup-flows --list
python3 scripts/query-dataset.py --dataset setup-flows --id fintech_market_entry
python3 scripts/query-dataset.py --dataset setup-flows --related-sector manufacturing
python3 scripts/query-dataset.py --dataset setup-flows --tag setup_flow
```

---

## Scripts

### Health check

```bash
python3 scripts/check.py
```

Runs four suites: required files, JSON validity, dataset validation (delegates to validate-data.py), and local markdown link resolution. Exits `0` on full pass. No internet required.

### Dataset validation

```bash
python3 scripts/validate-data.py
```

Validates all three datasets against their JSON Schemas. Also checks: `official_sources` not empty (where applicable), `placeholders` present when `draft`, ID parity between EN and AR files. Exits `0` on full pass.

### Querying

```bash
# Business structures
python3 scripts/query-structures.py --list
python3 scripts/query-structures.py --id llc
python3 scripts/query-structures.py --tag foreign_ownership

# Any dataset (--lang / --language both accepted)
python3 scripts/query-dataset.py --dataset sources --lang en --list
python3 scripts/query-dataset.py --dataset investment-licenses --lang ar --id misa_license
python3 scripts/query-dataset.py --dataset sources --lang en --tag ministry
python3 scripts/query-dataset.py --dataset sources --lang en --authority-type government_portal
python3 scripts/query-dataset.py --dataset sectors --lang en --list
python3 scripts/query-dataset.py --dataset sectors --lang ar --id fintech
python3 scripts/query-dataset.py --dataset sectors --regulatory-sensitivity highly_regulated
python3 scripts/query-dataset.py --dataset authority-relationships --list
python3 scripts/query-dataset.py --dataset authority-relationships --relationship-type sector_oversight
python3 scripts/query-dataset.py --dataset authority-relationships --from-authority misa
python3 scripts/query-dataset.py --dataset authority-relationships --sector fintech
python3 scripts/query-dataset.py --dataset setup-flows --list
python3 scripts/query-dataset.py --dataset setup-flows --id fintech_market_entry
python3 scripts/query-dataset.py --dataset setup-flows --related-sector manufacturing
python3 scripts/query-dataset.py --dataset fees --lang en --list
python3 scripts/query-dataset.py --dataset timelines --lang en --list
python3 scripts/query-dataset.py --dataset sezs --lang en --list
python3 scripts/query-dataset.py --dataset all --keyword "MISA" --lang en
```

---

## Verification Model

All dataset entries are `"draft"` until a contributor personally reviews the live official source and records:
- `last_verified`: date of review
- `verification_method`: what was reviewed and how
- Resolved `placeholders`: each removed once the field is confirmed

See `docs/en/source-verification.md` for the full workflow. Use `templates/source-review.md` when updating a `verification_status` field.

`"verified"` status requires: empty `placeholders` array, `last_verified` set to an ISO date, `verification_method` documented, no unresolved source conflicts.

---

## Development Phases

| Phase | Status |
|---|---|
| 1 — Foundation (repo structure, datasets, validation, verification workflow) | Nearly complete |
| 2 — Core Content (bilingual guides, additional datasets) | In progress |
| 3 — AI Integration (system prompts, RAG templates, MCP server) | Planned |
| 4 — Community (review cadence, translation workflow, automated checks) | Planned |

The Phase 3 MCP server will expose the datasets as queryable tools. The `prompts/` directory is the planned location for system prompts and MCP tool definitions.

---

## Key Invariants for AI Assistants

When generating or editing content in this repository:

1. **Do not set `verification_status: "verified"`** unless you have personally reviewed the source. Leave all new entries as `"draft"` with placeholder entries.
2. **Do not remove placeholders** unless the field has been verified against a live official source.
3. **EN and AR files must mirror each other** — same number of entries, same IDs, same order.
4. **Do not add entries to `data/sources.en.json`** unless the source uses a `.gov.sa` domain or is an officially recognized national platform.
5. **`depends_on` in investment-licenses** is conceptual only — it records which licenses typically precede others in the setup flow. It is not enforced by referential integrity checks.
6. **The `data/README.md` Datasets table** must be updated whenever a new dataset file is added.
7. **`check.py` REQUIRED_FILES list** must be updated whenever a new required file is added to the repository.
