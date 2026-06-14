# Invest Gate KSA — MCP Server

FastMCP server exposing 10 tools for querying the invest-gate-ksa knowledge base over stdio transport.

## Requirements

Python 3.10+ and the `mcp` package:

```bash
pip install mcp[cli] pydantic
```

## Claude Desktop Configuration

Add the following block to your Claude Desktop config file.

**macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`
**Windows:** `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "invest_gate_ksa": {
      "command": "python3",
      "args": ["/ABSOLUTE/PATH/TO/invest-gate-ksa/mcp/invest_gate_mcp.py"],
      "env": {}
    }
  }
}
```

Replace `/ABSOLUTE/PATH/TO/invest-gate-ksa` with the actual path on your system. On macOS you can run `pwd` inside the repository root to get the path.

Restart Claude Desktop after saving the config.

## Available Tools

| Tool | Description |
|------|-------------|
| `query_sectors` | Query investment sectors by ID, regulatory sensitivity, or tag |
| `query_authorities` | Query official Saudi government bodies and portals |
| `query_setup_flows` | Query conceptual setup flows for investment scenarios |
| `query_fees` | Query government fees (unverified amounts show a source to verify) |
| `query_timelines` | Query processing timelines for registration and licensing |
| `query_sezs` | Query Special Economic Zones and their verification status |
| `query_activities` | Query economic activities by code, sector, authority, or keyword |
| `query_structures` | Query legal entity structures (LLC, JSC, Branch, Rep Office) |
| `get_investor_path` | Cross-dataset overview for a sector, parent company status, and investor type |
| `search_knowledge_base` | Full-text search across one or more datasets |

## Response Format

Every tool returns JSON with two top-level keys:

```json
{
  "result": { ... },
  "disclaimer": "DISCLAIMER: For general educational purposes only..."
}
```

### Verification warnings

Entries that have not been independently verified against a live official source carry a `_verification_warning` field:

```json
{
  "id": "rhq_license_year1_fee",
  "_verification_warning": "⚠️ Unverified — confirm at: https://investsaudi.sa/en/rhq",
  "_note": "Fee structure reported by commercial sources as SAR 10,000 year 1 ..."
}
```

Fee entries where the amount is not published in advance (e.g. the MISA investment registration fee) suppress `amount_sar` from the output — the `_note` field explains the actual fee structure.

## Language

> **Language:** All tools default to English (`lang="en"`).
> Pass `lang="ar"` to receive Arabic responses.
All tools accept a `lang` parameter (`"en"` or `"ar"`). Passing `lang: "ar"` returns data from the Arabic dataset files.

## Data Status

All entries carry `verification_status: "verified"` or `"draft"`. Verified entries have been reviewed against a live official source. Draft entries are research starting points only.
