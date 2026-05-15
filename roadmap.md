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

## Out of Scope (by design)

- Legal advice or jurisdiction-specific opinions
- Private company data or proprietary information
- Investment recommendations or financial projections
- Real-time regulatory data (use official portals directly)
