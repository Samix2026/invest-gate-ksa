# Source Review Record

Use this template to document a source verification review. Copy this file, fill in each section, and attach it to your pull request or commit when updating a `verification_status` field.

Reference: [Source Verification Workflow](../docs/en/source-verification.md)

---

## Review Metadata

| Field | Value |
|---|---|
| **Source ID** | <!-- e.g. misa, zatca, gosi --> |
| **Dataset file** | <!-- e.g. data/sources.en.json --> |
| **Reviewer** | <!-- your name or GitHub handle --> |
| **Review date** | <!-- YYYY-MM-DD --> |
| **Current status (before this review)** | <!-- draft / verified / placeholder --> |
| **Proposed status (after this review)** | <!-- draft / verified --> |

---

## 1. Domain Check

- [ ] Navigated directly to the official domain (typed manually, not via search)
- [ ] Domain in browser matches the `official_website` field in the dataset

**Domain reviewed:** <!-- e.g. misa.gov.sa -->  
**Match:** <!-- Yes / No / Partial — explain if not Yes -->  
**Notes:**

---

## 2. Content Verification

- [ ] Located the specific page or section containing the information
- [ ] Information confirmed present as of review date
- [ ] Content is publicly accessible (no login required for the sections reviewed)

**Section or page title reviewed:**  
**What was confirmed:**  
**What could not be confirmed:**  
**Method:** <!-- e.g. manual browse, portal search, document download -->  

---

## 3. Authority Check

- [ ] This body is the primary regulatory authority for the topic documented
- [ ] Domain is `.gov.sa` or an officially recognized national domain

**Is this body named in legislation or regulation as responsible for this topic?**  
<!-- Yes / No / Unknown — if Unknown, add a placeholder -->

**Notes:**

---

## 4. Login / Access Wall

- [ ] All reviewed content is publicly accessible
- [ ] Content behind login was encountered

**If login-gated content was encountered:**  
Describe what was and was not reviewed, and whether a placeholder was added:

---

## 5. Stale or Moved Pages

- [ ] All expected pages resolved without errors
- [ ] A redirect was encountered (describe below)
- [ ] A page was not found (describe below)

**Details (if applicable):**  
**Action taken:**

---

## 6. Conflicting Sources

- [ ] No conflicting information found across official sources
- [ ] A conflict was identified (describe below)

**Conflict description (if applicable):**  
**Sources involved:**  
**Resolution or action taken:**

---

## 7. Fields Updated

List every field in the dataset entry that was updated as a result of this review.

| Field | Previous value | New value | Notes |
|---|---|---|---|
| `verification_status` | | | |
| `last_verified` | | | |
| `verification_method` | | | |
| <!-- other field --> | | | |

**Placeholders resolved (if any):**  
**Placeholders added (if any):**

---

## 8. Decision

**Final `verification_status`:** <!-- draft / verified -->

**Reason (if remaining as draft):**  
<!-- List any unresolved placeholders, conflicts, or inaccessible content -->

**Ready for merge:** <!-- Yes / No / Conditional -->  
**Conditions (if Conditional):**

---

## Sign-off

> I confirm that I personally reviewed the source(s) listed above on the date recorded, and that the dataset entry reflects what was present on the official portal at the time of review.

**Reviewer:** ___________________________  
**Date:** ___________________________
