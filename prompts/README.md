# Prompts Directory

AI prompt templates for building assistants, chatbots, or MCP server tools on top of this knowledge base.

---

## Purpose

This directory contains:

- **System prompts** — baseline instructions for an AI assistant grounded in this repository
- **Query templates** — structured prompts for extracting specific information from the knowledge base
- **RAG prompts** — retrieval-augmented generation prompts for use with vector databases
- **MCP tool definitions** — tool schemas for exposing repository content via the Model Context Protocol

---

## Prompt Assets

| File | Description | Status |
|------|-------------|--------|
| `system-prompt-base.md` | Core system prompt for an Invest Gate KSA assistant | Available |
| `query-business-structure.md` | Prompt for comparing entity types | Planned |
| `query-registration-steps.md` | Prompt for walking through registration processes | Planned |
| `query-sector-eligibility.md` | Prompt for checking foreign ownership rules by sector | Planned |
| `rag-context-template.md` | Template for injecting retrieved context into answers | Planned |
| `mcp-tool-definitions.json` | MCP tool schemas for knowledge base queries | Planned |

---

## Usage Principles

All prompts in this directory must:

1. Instruct the AI to **cite sources** when answering
2. Include a **disclaimer** that answers are informational, not legal advice
3. Instruct the AI to **acknowledge uncertainty** rather than invent facts
4. Be designed to **refuse requests for specific legal or financial advice**
5. Direct users to official sources (misa.gov.sa, mc.gov.sa, zatca.gov.sa, etc.)

---

## MCP Server

The working MCP server is implemented in `mcp/invest_gate_mcp.py` and currently exposes 10 tools. A standalone `mcp-tool-definitions.json` export remains planned for clients that need static tool schemas.
