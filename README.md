![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)
![Languages: Arabic | English](https://img.shields.io/badge/Languages-Arabic%20%7C%20English-green.svg)
![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-brightgreen.svg)
![Health Checks](https://img.shields.io/badge/Health%20Checks-157%2F157-brightgreen.svg)

# Invest Gate KSA

<p align="center">
  <img src="assets/images/repo-cover.png" alt="Invest Gate KSA Cover" width="100%">
</p>

**A bilingual, open-source knowledge infrastructure for understanding investment, company setup, licensing, and business operations in Saudi Arabia.**

---

> **Disclaimer**
> This repository contains general educational information only. It is **not legal, financial, regulatory, or tax advice**. Laws, fees, and procedures in Saudi Arabia change — always verify information directly with official government sources and consult qualified practitioners before making any decision.

---

## The Problem

Saudi Arabia has opened significantly to foreign investment. But for an investor arriving from outside the Kingdom, the path is genuinely hard to navigate: information is scattered across a dozen government portals, often in Arabic only, frequently outdated on third-party sites, and rarely organized around the questions investors actually ask.

The result is that many foreign investors rely on expensive consultants for information that should be freely accessible — or worse, proceed on misinformation.

---

## What This Is

Invest Gate KSA is a structured, community-maintained knowledge repository that organizes publicly available information about investing in Saudi Arabia into clear, source-linked, bilingual documentation — and exposes it through a working MCP server for conversational AI querying.

It is not a consultancy. It is not a legal service. It is a **reference framework** — designed to be accurate, traceable, and queryable.

---

## Who This Is For

| Audience | How they use it |
|---|---|
| Foreign entrepreneurs and investors | Understand the regulatory landscape before engaging advisors |
| Business setup consultants | Reference and share structured process guides |
| Researchers and academics | Source-linked overview of the Saudi investment framework |
| Developers | Knowledge base for building investment-related tools and AI assistants |
| Translators and bilingual professionals | Arabic-English alignment of business and regulatory terminology |

---

## What's Inside

| Directory / File | Contents |
|---|---|
| `data/` | 9 structured bilingual JSON datasets (EN + AR) |
| `data/sectors` | 16 investment sectors with Vision 2030 alignment |
| `data/sources` | 14 verified regulatory authority sources |
| `data/source-gaps` | 24 tracked data gaps awaiting verification |
| `data/setup-flows` | Step-by-step registration flows by sector |
| `data/structures` | Business structure comparison data |
| `data/fees` | Fee schedules — verified entries cite official sources |
| `data/timelines` | Processing time estimates — verified against official publications |
| `data/sezs` | 5 Special Economic Zones (KAEC, Jazan, Ras Al-Khair, Cloud, SILZ) |
| `schemas/` | JSON Schema Draft-07 — strict typing, additionalProperties: false |
| `docs/en/` | English guides: registration, tax, SEZs, Vision 2030, structures |
| `docs/ar/` | Arabic mirrors (RTL) — full bilingual parity enforced |
| `mcp/` | FastMCP server — 8 query tools for Claude Desktop integration |
| `.claude/commands/` | 6 slash commands for daily repository operations |
| `prompts/` | AI system prompt (bilingual, citation rules, legal disclaimer) |
| `scripts/` | 157-check validation suite (JSON, schema, parity, cross-refs) |
| `sources/` | Citation registry — every claim source-linked |
| `templates/` | Investor checklists — planned |
| `.github/workflows/` | CI/CD — validation on every push and PR |

**Core coverage:**

- Business registration types: Standard Investment Registration, RHQ, Entrepreneurial
- Full regulatory path: MISA → CR → Chamber of Commerce → ZATCA → GOSI → Qiwa → Muqeem
- Tax framework: CIT 20% (foreign), Zakat 2.5% (Saudi/GCC), VAT 15%, WHT 5–20%
- Special Economic Zones: KAEC, Jazan, Ras Al-Khair, Cloud Computing, SILZ (5% CIT)
- Vision 2030 sector alignment: 16 sectors with official targets and supervising entities
- Fee schedules and processing timelines — verified against official sources
- 2025 regulatory updates: new CR Law (April 2025), Investment Law (August 2024)

---

## Project Status

| Phase | Progress | Status | Description |
|---|---|---|---|
| Phase 1 — Foundation | ██████████ | Complete | Schemas, CI/CD, 157-check validation suite |
| Phase 2 — Knowledge Base | ████████░░ | Active | 9 datasets, 5 verified core paths, SEZs, V2030 |
| Phase 3 — AI Workflows | ██████████ | Complete | System prompt, 8 MCP tools |
| Phase 4 — MCP Integration | ██████████ | Complete | Claude Desktop ready (stdio) |
| Phase 5 — Product Layer | ░░░░░░░░░░ | Planned | — |

**Verification status (2026-05-19):**
- ✅ Verified against official sources: MISA registration, CR (MoC), Chamber of Commerce, ZATCA (CIT + VAT + WHT), GOSI, Qiwa, Muqeem, SEZs (ECZA + Official Gazette Jan 2026), Vision 2030 KPIs
- ⚠️ Draft — pending official confirmation: RHQ registration fees, SILZ tax details
- 📋 Planned: economic-activities dataset, investor checklist templates

See [roadmap.md](roadmap.md) for the full task breakdown.

---

## MCP Server — Claude Desktop Integration

Connect Claude Desktop directly to this knowledge base for conversational querying.

**Install:**
```bash
pip3 install -r mcp/requirements.txt
```

**Configure** (`~/Library/Application Support/Claude/claude_desktop_config.json`):
```json
{
  "mcpServers": {
    "invest-gate-ksa": {
      "command": "python3",
      "args": ["/absolute/path/to/invest-gate-ksa/mcp/invest_gate_mcp.py"]
    }
  }
}
```

**Available tools:**
`query_sectors` · `query_authorities` · `query_setup_flows` · `query_fees` · `query_timelines` · `query_structures` · `get_investor_path` · `search_knowledge_base`

See [mcp/README.md](mcp/README.md) for full setup instructions.

---

## Verification Methodology

Every data entry carries an explicit verification status:
- **verified** — confirmed from an official government source (.gov.sa, ECZA, Official Gazette)
- **draft** — from credible commercial sources but not officially confirmed
- **placeholder** — gap acknowledged, not yet researched

Unverified entries are never presented as fact — they carry a disclaimer and a `verify_at` link. See [docs/en/source-verification.md](docs/en/source-verification.md) for the full workflow.

---

## Contributing

This project grows through the knowledge of people with direct, documented experience. We welcome contributions from consultants, lawyers, researchers, investors, and developers.

**What we need most:**
- Verified fee amounts from official sources (especially RHQ, SILZ)
- Economic activities dataset (MISA activity codes with foreign ownership eligibility)
- Investor checklist templates (LLC, Branch, MISA documents)
- Corrections to any outdated information

Every piece of content must cite an official source. See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

---

## Run Health Checks

```bash
python3 scripts/check.py
```

Runs 157 checks: required files, JSON validity, schema validation, alias integrity, cross-reference integrity, bilingual parity. Exits `0` on full pass.

---

## Browse the Docs

- [English Documentation →](docs/en/README.md)
- [الوثائق العربية →](docs/ar/README.md)
- [Registration Types →](docs/en/registration-types.md)
- [Special Economic Zones →](docs/en/special-economic-zones.md)
- [Vision 2030 Sector Guide →](docs/en/vision2030-sectors.md)
- [Tax Obligations →](docs/en/company-setup-overview.md)
- [Source Verification →](docs/en/source-verification.md)
- [Sources Index →](sources/index.md)

---

## License

[MIT License](LICENSE) — free to use, adapt, and distribute with attribution.

The content (guides, data, templates) is educational, not advisory. See [LICENSE](LICENSE) for the full disclaimer.
