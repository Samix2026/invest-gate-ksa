# Data Directory

This directory holds structured, machine-readable data derived from official sources.

> **Important:** All data must be sourced from official government publications, announcements, or verifiable public records. Never add invented or estimated values. Each dataset must include a source reference and a `last_verified` date.

---

## Datasets

| File | Description | Status |
|------|-------------|--------|
| `business-structures.en.json` | Legal entity types available to foreign investors — English | Draft |
| `business-structures.ar.json` | Legal entity types available to foreign investors — Arabic | Draft |
| `fees.json` | Official government fees (registration, licensing, permits) | Planned |
| `timelines.json` | Estimated processing durations for key procedures | Planned |
| `sectors.json` | Sectors open/restricted/prohibited to foreign investment | Planned |
| `zones.json` | Economic zones, locations, and key incentives | Planned |
| `agencies.json` | Regulatory bodies, roles, and official websites | Planned |
| `ownership_limits.json` | Foreign ownership thresholds by sector | Planned |

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

## Validation

All datasets with a corresponding JSON Schema can be validated with the project's validation script.

**Requirements:** Python 3.7+ and the `jsonschema` package.

```bash
# Install dependency
pip install -r scripts/requirements.txt

# Run all checks
python scripts/validate-data.py
```

The script enforces the following rules:

| Check | Scope |
|---|---|
| JSON Schema compliance | Per file — structure, required fields, enum values |
| `official_sources` not empty | Per entry — every entry must cite at least one official source |
| `placeholders` present when `draft` | Per entry — draft entries must declare what needs verification |
| ID parity (same IDs, same order) | Cross-file — EN and AR files must be structurally mirrored |

Exit code `0` means all checks passed. Exit code `1` means at least one check failed, with details printed to stdout. Suitable for use in CI pipelines.

The JSON Schema lives at [`schemas/business-structures.schema.json`](../schemas/business-structures.schema.json).

---

## Adding Data

1. Create a new JSON file following the schema convention above.
2. Add an entry to the Datasets table in this README.
3. Add a source entry in [`../sources/index.md`](../sources/index.md).
4. Run `python scripts/validate-data.py` to confirm the file passes validation.
5. Keep data neutral and descriptive — no interpretation or advice.
