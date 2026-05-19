---
name: Source Verification
about: Report that you have verified a draft entry against its official source
title: "[VERIFIED] "
labels: verification, source-gap
assignees: ''
---

## Entry being verified

**Dataset:**
<!-- e.g. business-structures, investment-licenses, sectors -->

**Entry ID:**
<!-- e.g. llc, misa_license, fintech -->

**Language:**
- [ ] English
- [ ] Arabic
- [ ] Both

---

## Verification details

**Official source name:**

**Official source URL (domain only — do not guess full paths):**

**Section / page reference:**

**Date you reviewed the source:**

**Verification method:**
<!-- e.g. "Read Section 3.1 of the MISA Investor Guide 12th Edition, March 2025" -->

---

## Fields verified

_List each placeholder field you have resolved and provide the verified value._

| Field | Verified value | Source reference |
|---|---|---|
| | | |

---

## Fields still unresolved

_List any placeholder fields you could not verify._

| Field | Reason unresolved |
|---|---|
| | |

---

## Proposed changes

_Paste the updated JSON snippet or document section with verified values filled in and resolved placeholders removed._

```json
```

---

## Checklist

- [ ] I personally reviewed the live official source (not a third-party summary)
- [ ] All verified fields have source references
- [ ] Unresolved placeholders remain in the `placeholders` array
- [ ] `last_verified` date is set to today's date
- [ ] `verification_method` field describes how I verified
- [ ] Both EN and AR files are updated (or I have noted which needs updating)
