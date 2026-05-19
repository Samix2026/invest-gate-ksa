# Contributing to Invest Gate KSA

Thank you for your interest in contributing. This guide explains how to add value while maintaining the quality and integrity of the repository.

---

## Who Should Contribute

We welcome contributions from:

- Business setup consultants and corporate lawyers (sharing general process knowledge, not specific advice)
- Researchers and academics studying the Saudi investment environment
- Investors with direct, documented experience
- Translators with legal/business Arabic expertise
- Developers building on the knowledge base

---

## What You Can Contribute

| Contribution Type | Welcome? | Notes |
|---|---|---|
| Factual process descriptions | Yes | Must cite official sources |
| Translations (EN ↔ AR) | Yes | Must preserve accuracy, not add interpretation |
| Structured data (fees, timelines, sectors) | Yes | Must include source and verification date |
| Templates and checklists | Yes | Must include disclaimers |
| AI prompts | Yes | Must enforce disclaimer and source-citation behavior |
| Links to official sources | Yes | Must verify the link is current |
| Corrections to outdated content | Yes | Note the change and new source |
| Legal opinions or advice | **No** | Out of scope by design |
| Invented or unverified regulations | **No** | Risk of harm to users |
| Proprietary or confidential information | **No** | Legal risk |

---

## Content Standards

### Source Requirement
Every factual claim must be traceable to an official source. Use this inline format:

```
[Source: Ministry of Investment (MISA)](https://misa.gov.sa)
```

Add new sources to [`sources/index.md`](sources/index.md).

### Disclaimer
Any document that describes a process or provides instructions must include this notice at the top:

> **Disclaimer:** This content is for general informational purposes only. It is not legal, financial, or regulatory advice. Verify all information with official Saudi government sources and consult qualified professionals before taking action.

### Dates
Include a `last_verified` date on any document containing fees, timelines, or procedural steps. Requirements change — stale information is harmful.

### Language
- English docs go in `docs/en/`
- Arabic docs go in `docs/ar/`
- Keep translations synchronized — if you update one language, note that the other needs updating
- Arabic content should be right-to-left (RTL) friendly in markup

---

## Verification Standards

All dataset entries follow a two-state verification model.

| Status | Meaning | Requirements |
|---|---|---|
| `"draft"` | Content has not been independently reviewed against a live official source | Non-empty `placeholders` array; `last_verified` is a placeholder string |
| `"verified"` | A contributor personally reviewed the live official source | Empty `placeholders` array; `last_verified` set to ISO date; `verification_method` documented |

**Rules:**

- Never set `verification_status: "verified"` unless you have personally reviewed the live official source (not a third-party summary or AI output).
- Never remove a placeholder field without replacing it with a verified value.
- Verified entries must use `templates/source-review.md` to document what was reviewed.
- All verifiable sources must use a `.gov.sa` domain or officially recognized national authority.

See `docs/en/source-verification.md` for the full workflow.

---

## Automated Quality Checks

Every pull request runs five automated checks via GitHub Actions (`.github/workflows/pr-quality.yml`). Run them locally before submitting.

| Check | Script | What it validates |
|---|---|---|
| Health checks | `python3 scripts/check.py` | Required files, JSON validity, dataset validation, local markdown links |
| Schema validation | `python3 scripts/validate-data.py` | JSON Schema conformance, `official_sources` not empty, placeholder presence |
| Bilingual parity | `python3 scripts/check-bilingual-parity.py` | EN and AR files have identical entry IDs in identical order |
| Data entry quality | `python3 scripts/check-data-quality.py` | `draft` entries have placeholders; `verified` entries have real dates |
| Amount plausibility | `python3 scripts/check-amounts.py` | Numeric `amount` fields do not exceed 1,000,000 SAR (catches copy-paste errors) |

**To run all checks locally:**

```bash
python3 scripts/check.py
python3 scripts/validate-data.py
python3 scripts/check-bilingual-parity.py
python3 scripts/check-data-quality.py
python3 scripts/check-amounts.py
```

All five must pass before a PR can be merged.

---

## How to Contribute

### For small changes (typos, broken links, updated values)
1. Fork the repository
2. Make your change with a clear commit message referencing the source
3. Open a pull request describing what changed and why

### For new content
1. Open an issue first to discuss scope and sources
2. Fork and create a branch named `content/<topic>`
3. Follow the content standards above
4. Submit a pull request with:
   - Summary of what was added
   - Sources cited
   - Date information was verified

### For translations
1. Ensure the source-language document is stable before translating
2. Translate meaning accurately — do not interpret, expand, or simplify
3. Flag any terms where the translation requires a note for clarity

---

## Pull Request Review Criteria

PRs will be reviewed for:

- **Accuracy** — does it match official sources?
- **Sourcing** — is every claim cited?
- **Tone** — informational, not advisory
- **Completeness** — does it include a disclaimer where needed?
- **Sync** — if EN was updated, is AR flagged for update (or updated too)?

---

## Code of Conduct

Be respectful and professional. This is an educational resource — contributions should prioritize accuracy and usefulness over opinion.
