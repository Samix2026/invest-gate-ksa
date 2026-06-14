# Roadmap — Invest Gate KSA

This document outlines the planned development phases for the Invest Gate KSA knowledge repository.

---

## Phase 1 — Foundation (Complete)

**Goal:** Establish the repository structure and contribution framework.

- [x] Repository skeleton (directories, READMEs)
- [x] Bilingual structure (English + Arabic)
- [x] Source index and citation standards
- [x] Contributing guidelines
- [x] License
- [x] CLAUDE.md — AI assistant context file
- [x] `data/sources.{en,ar}.json` — regulatory body registry (supersedes planned `agencies.json`)

---

## Phase 2 — Core Content

**Goal:** Populate the repository with accurate, source-linked documentation covering the most common investor needs.

**English Docs (`docs/en/`)**
- [x] Overview of the Saudi investment landscape (`company-setup-overview.md`)
- [x] Guide: Business structures for foreign investors (`comparison-structures.md`)
- [x] Guide: MISA investment registration — types and process (`registration-types.md`)
- [x] Guide: Commercial registration (CR) (`commercial-registration.md` — April 2025 Royal Decree M/83, single national CR, Ejari, fees, timeline)
- [x] Guide: Special Economic Zones (`special-economic-zones.md`)
- [x] Guide: Saudization (Nitaqat) requirements (`nitaqat-saudization.md`)
- [x] Guide: Corporate banking basics (`corporate-banking.md`)
- [x] Guide: VAT and Zakat overview (`tax-compliance.md`)

**Arabic Docs (`docs/ar/`)**
- [x] Mirror of all English guides in Arabic (15 files, exact match with `docs/en/`)

**Structured Data (`data/`)**
- [x] `sectors.{en,ar}.json` — sector context, likely authorities, regulatory sensitivity (16 sectors)
- [x] `business-structures.{en,ar}.json` — entity types for foreign investors (4 types)
- [x] `investment-licenses.{en,ar}.json` — registration and licensing concepts (5 entries)
- [x] `sources.{en,ar}.json` — official Saudi government sources (16 entries)
- [x] `source-gaps.{en,ar}.json` — known data gaps awaiting official verification (23 entries)
- [x] `authority-relationships.{en,ar}.json` — conceptual relationships between regulatory bodies (12 entries)
- [x] `setup-flows.{en,ar}.json` — conceptual setup flows for common investor scenarios (4 flows)
- [x] `fees.{en,ar}.json` — official government fees (26 entries)
- [x] `timelines.{en,ar}.json` — typical processing durations (12 entries)
- [x] `sezs.{en,ar}.json` — special economic zones (5 zones, all verified)
- [x] `economic-activities.{en,ar}.json` — MISA-recognized economic activities (21 entries; 10 verified, 11 draft)

**Templates (`templates/`)**
- [x] LLC setup checklist (`templates/llc-checklist.md`)
- [x] Branch office checklist (`templates/branch-checklist.md`)
- [x] MISA document list (`templates/misa-documents.md`)

---

## Phase 3 — AI Integration

**Goal:** Make the repository usable as an AI knowledge base and MCP server.

- [x] MCP server (`mcp/invest_gate_mcp.py` — 10 tools, FastMCP)
- [x] Base system prompt for an Invest Gate KSA assistant
- [ ] RAG prompt templates
- [ ] MCP tool definitions (`prompts/mcp-tool-definitions.json`)
- [ ] Embedding-ready document format (chunked, metadata-tagged)
- [ ] Integration guide for Claude and other LLMs

---

## Phase 4 — Community & Maintenance

**Goal:** Establish ongoing quality and community processes.

- [x] Automated link-checking for official sources
- [ ] Versioning policy (content snapshots with dates)
- [ ] Review cadence (quarterly content audit)
- [ ] Translation workflow for keeping EN and AR in sync
- [x] Issue templates for reporting outdated information

---

## Phase 5 — Product Layer

**Goal:** Make the knowledge architecture easier to understand and explore.

- [x] Interactive system map
- [x] Automated GitHub Pages deployment
- [x] Arabic/English interface with Invest Saudi-inspired visual language
- [ ] Search and filtering interface for public datasets
- [ ] Hosted API or managed MCP endpoint

---

## Open Issues — Help Wanted

The following data gaps are tracked as GitHub Issues and need community help:

| Priority | Issue | Dataset | How to help |
|---|---|---|---|
| 🔴 High | [RHQ fee schedule](https://github.com/Samix2026/invest-gate-ksa/issues/2) | fees | Verify from MISA official source |
| 🔴 High | [SILZ tax incentives](https://github.com/Samix2026/invest-gate-ksa/issues/3) | sezs | Verify from ECZA official source |
| 🔴 High | [SEZ qualifying activities](https://github.com/Samix2026/invest-gate-ksa/issues/4) | sezs | Document from ecza.gov.sa |
| 🔴 High | [MISA fee amounts by activity](https://github.com/Samix2026/invest-gate-ksa/issues/5) | fees | Obtain from MISA e-portal |
| 🔴 High | [Foreign individual pathway](https://github.com/Samix2026/invest-gate-ksa/issues/6) | structures | Confirm from MISA Investment Law 2024 regs |

See [all open issues →](https://github.com/Samix2026/invest-gate-ksa/issues)

---

## Out of Scope (by design)

- Legal advice or jurisdiction-specific opinions
- Private company data or proprietary information
- Investment recommendations or financial projections
- Real-time regulatory data (use official portals directly)
