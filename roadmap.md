# Roadmap — Invest Gate KSA

This document outlines the planned development phases for the Invest Gate KSA knowledge repository.

---

## Phase 1 — Foundation (Current)

**Goal:** Establish the repository structure and contribution framework.

- [x] Repository skeleton (directories, READMEs)
- [x] Bilingual structure (English + Arabic)
- [x] Source index and citation standards
- [x] Contributing guidelines
- [x] License
- [x] CLAUDE.md — AI assistant context file
- [ ] Initial `data/agencies.json` — regulatory body registry

---

## Phase 2 — Core Content

**Goal:** Populate the repository with accurate, source-linked documentation covering the most common investor needs.

**English Docs (`docs/en/`)**
- [ ] Overview of the Saudi investment landscape
- [ ] Guide: Business structures for foreign investors
- [ ] Guide: MISA investment registration — types and process
- [ ] Guide: Commercial registration (CR)
- [ ] Guide: Special Economic Zones
- [ ] Guide: Saudization (Nitaqat) requirements
- [ ] Guide: Corporate banking basics
- [ ] Guide: VAT and Zakat overview

**Arabic Docs (`docs/ar/`)**
- [ ] Mirror of all English guides in Arabic

**Structured Data (`data/`)**
- [x] `sectors.json` — sector context, likely authorities, regulatory sensitivity (8 initial sectors; open/restricted classification requires official verification)
- [ ] `fees.json` — official government fees
- [ ] `timelines.json` — typical processing durations
- [ ] `zones.json` — economic zones

**Templates (`templates/`)**
- [ ] LLC setup checklist
- [ ] Branch office checklist
- [ ] MISA document list

---

## Phase 3 — AI Integration

**Goal:** Make the repository usable as an AI knowledge base and MCP server.

- [ ] Base system prompt for an Invest Gate KSA assistant
- [ ] RAG prompt templates
- [ ] MCP tool definitions (`prompts/mcp-tool-definitions.json`)
- [ ] Embedding-ready document format (chunked, metadata-tagged)
- [ ] Basic MCP server scaffold (Node.js or Python)
- [ ] Integration guide for Claude and other LLMs

---

## Phase 4 — Community & Maintenance

**Goal:** Establish ongoing quality and community processes.

- [ ] Automated link-checking for official sources
- [ ] Versioning policy (content snapshots with dates)
- [ ] Review cadence (quarterly content audit)
- [ ] Translation workflow for keeping EN and AR in sync
- [ ] Issue templates for reporting outdated information

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
| 🟡 Medium | [Economic activities dataset](https://github.com/Samix2026/invest-gate-ksa/issues/8) | economic-activities | Populate from MISA activity list |
| 🟢 Good first issue | [AR translation review](https://github.com/Samix2026/invest-gate-ksa/issues/7) | docs/ar | Arabic speakers welcome |

See [all open issues →](https://github.com/Samix2026/invest-gate-ksa/issues)

---

## Out of Scope (by design)

- Legal advice or jurisdiction-specific opinions
- Private company data or proprietary information
- Investment recommendations or financial projections
- Real-time regulatory data (use official portals directly)
