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

## Adding Data

1. Create a new JSON file following the schema above.
2. Add a source entry in [`../sources/index.md`](../sources/index.md).
3. Keep data neutral and descriptive — no interpretation or advice.
