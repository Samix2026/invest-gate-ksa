# Invest Gate KSA
<p align="center">
  <img src="assets/images/repo-cover.png" alt="Invest Gate KSA Cover" width="100%">
</p>

![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)
![Languages: Arabic | English](https://img.shields.io/badge/Languages-Arabic%20%7C%20English-green.svg)
![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-brightgreen.svg)

**A bilingual, open-source knowledge base that helps foreign investors understand how to set up and operate a business in Saudi Arabia.**

---

> **Disclaimer**
> This repository contains general educational information only. It is **not legal, financial, regulatory, or tax advice**. Nothing here should be relied upon as a substitute for professional counsel. Laws, fees, and procedures in Saudi Arabia change — always verify information directly with official government sources and consult qualified practitioners before making any decision.

---

## The Problem

Saudi Arabia has opened significantly to foreign investment in recent years. But for an investor arriving from outside the Kingdom, the path is genuinely hard to navigate: information is scattered across a dozen government portals, often in Arabic only, frequently outdated on third-party sites, and rarely organized around the questions investors actually ask.

The result is that many foreign investors rely on expensive consultants for information that should be freely accessible — or worse, proceed on misinformation.

---

## What This Is

Invest Gate KSA is a structured, community-maintained knowledge repository that organizes publicly available information about investing in Saudi Arabia into clear, source-linked, bilingual documentation.

It is not a consultancy. It is not a legal service. It is a **reference framework** — designed to be accurate, traceable, and useful as a starting point before engaging professionals.

The repository is also designed from the ground up to grow into an **AI assistant and MCP server**, so the same knowledge can be queried conversationally.

---

## Who This Is For

| Audience | How they use it |
|---|---|
| Foreign entrepreneurs and investors | Understand the landscape before engaging advisors |
| Business setup consultants | Reference and share structured process guides |
| Researchers and academics | Source-linked overview of the Saudi investment framework |
| Developers | Knowledge base for building investment-related tools and AI assistants |
| Translators and bilingual professionals | Arabic-English alignment of business and regulatory terminology |

---

## What's Inside

```
invest-gate-ksa/
├── data/              # 9 structured bilingual JSON datasets
│   ├── sectors        # Investment sectors with V2030 alignment
│   ├── sources        # 13 regulatory authority sources
│   ├── source-gaps    # Tracked data gaps awaiting verification
│   ├── setup-flows    # Step-by-step registration flows by sector
│   ├── structures     # Business structure comparison data
│   ├── fees           # Fee schedules (verified + draft with citations)
│   ├── timelines      # Processing time estimates (verified sources)
│   └── economic-activities  # Schema ready — data planned
├── schemas/           # JSON Schema Draft-07 — all datasets strictly typed
├── docs/
│   ├── en/            # English guides: registration types, tax, setup, comparison
│   └── ar/            # Arabic mirrors (RTL) — full bilingual parity enforced
├── mcp/               # MCP server for Claude Desktop integration
│   ├── invest_gate_mcp.py   # FastMCP server — 8 query tools
│   ├── requirements.txt
│   └── README.md      # Setup instructions + Claude Desktop config
├── prompts/           # AI system prompts
│   └── system-prompt-base.md
├── scripts/           # Validation and query utilities (143-check health suite)
├── sources/           # Citation registry — every claim source-linked
├── templates/         # Investor checklists and document guides
├── .github/workflows/ # CI/CD — validation runs on every push and PR
├── roadmap.md
├── CONTRIBUTING.md
└── LICENSE
```

**Core topics covered:**

- Business registration types for foreign investors (Standard, RHQ, Entrepreneurial)
- MISA investment registration process and Investment Registration Certificate (IRC)
- Commercial Registration (CR) — unified single CR under April 2025 law
- Key regulatory bodies and what they govern (MISA, MoC, ZATCA, GOSI, SAMA, CMA)
- Tax obligations: CIT 20% (foreign), Zakat 2.5% (Saudi/GCC), VAT 15%, WHT 5–20%
- Fee schedules with verification status — verified entries cite official sources
- Processing timelines verified against official government publications
- Special Economic Zones and Vision 2030 sector priorities
- Labor, Saudization (Nitaqat), and operational requirements

---

## Project Status

| Phase | Progress | Status | Description |
|---|---|---|---|
| Phase 1 — Foundation | ██████████ | Complete | Schemas, CI/CD, validation suite |
| Phase 2 — Knowledge Base | ████████░░ | Active | 9 datasets, 5 verified core paths |
| Phase 3 — AI Workflows | ██████████ | Complete | System prompt, 8 MCP tools |
| Phase 4 — MCP Integration | ██████████ | Complete | Claude Desktop ready (stdio) |
| Phase 5 — Product Layer | ░░░░░░░░░░ | Planned | — |

**Verification status as of 2026-05-18:**
- ✅ Verified against official sources: MISA investment registration, Commercial Registration, Chamber of Commerce, ZATCA (CIT + VAT + WHT), GOSI
- ⚠️ Draft — pending official confirmation: RHQ registration fees
- 📋 Planned: economic-activities dataset, investor checklist templates

See [roadmap.md](roadmap.md) for the full task breakdown.

---

## Contributing

This project grows through the knowledge of people with direct, documented experience. We welcome contributions from consultants, lawyers, researchers, investors, and developers.

**What we need most right now:**
- Accurate, source-linked process descriptions in English and Arabic
- Corrections to any outdated information
- Translations that preserve precision over simplicity
- Structured data (official fees, timelines, sector lists) with verified sources

Every piece of content must cite an official source. See [CONTRIBUTING.md](CONTRIBUTING.md) for the full guidelines.

---

## Project Checks

```bash
python3 scripts/check.py
```

Verifies required files, JSON validity, dataset schema validation, alias integrity, and local markdown link resolution. Exits `0` on full pass — useful to run before opening a pull request.

---

## MCP Server — Claude Desktop Integration

This repository includes a ready-to-use MCP server that connects Claude Desktop
directly to the knowledge base for conversational querying.

**Install:**
```bash
pip3 install -r mcp/requirements.txt
```

**Configure Claude Desktop** (`~/Library/Application Support/Claude/claude_desktop_config.json`):
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

**Available tools:** `query_sectors` · `query_authorities` · `query_setup_flows` ·
`query_fees` · `query_timelines` · `query_structures` · `get_investor_path` ·
`search_knowledge_base`

See [mcp/README.md](mcp/README.md) for full setup instructions.

---

## Browse the Docs

- [English Documentation →](docs/en/README.md)
- [الوثائق العربية →](docs/ar/README.md)
- [Source Verification Workflow →](docs/en/source-verification.md)
- [Sources Index →](sources/index.md)

---

## License

[MIT License](LICENSE) — free to use, adapt, and distribute with attribution.

The content (guides, data, templates) carries an additional disclaimer: it is educational, not advisory. See [LICENSE](LICENSE) for the full content disclaimer.

