---
title: "Source Verification Workflow"
language: en
last_verified: "[PLACEHOLDER — add date when this workflow is reviewed and approved]"
related:
  - docs/ar/source-verification.md
  - sources/index.md
  - data/sources.en.json
  - templates/source-review.md
---

# Source Verification Workflow

This document describes how contributors verify official sources before setting or updating a `verification_status` field in any dataset in this repository. It applies to entries in `data/sources.en.json`, `data/business-structures.en.json`, `data/investment-licenses.en.json`, and any future dataset with a `verification_status` field.

When completing a review, record your findings using the [source review template](../../templates/source-review.md).

---

## 1. How to Verify an Official Source

Verification means confirming that specific information in a dataset entry is currently present and accurate on the official source itself — not on a third-party summary, a cached version, or an older document.

**Steps:**

1. **Navigate directly.** Type the domain into your browser manually. Do not rely on search engine results, which may surface cached, outdated, or unofficial pages.

2. **Confirm the domain.** Check that the domain in your browser matches the `official_website` field recorded in the dataset entry. If they differ, note the discrepancy before proceeding.

3. **Locate the specific content.** Find the page or section that contains the information you are verifying. If the page cannot be found, follow the procedure in [Section 5](#5-how-to-handle-stale-or-moved-pages).

4. **Read, do not assume.** Confirm the information is present on the page as it currently reads. Do not infer from a general description of the body's role.

5. **Record what you checked.** Note the section name or page title where you found the information. Do not record full URLs as data fields in the JSON — use the `verification_method` field to describe what you reviewed and where.

6. **Record the date.** Set `last_verified` to the date you completed the review in `YYYY-MM-DD` format.

> **One reviewer per entry.** Do not mark a source as verified based on a review you did not personally conduct. If inheriting someone else's review, treat the entry as `draft` until you have personally confirmed it.

---

## 2. How to Decide If a Source Is Authoritative

Not every government-looking website is authoritative for the topic you are documenting. Before citing a source, confirm it is the appropriate primary authority.

**A source is likely authoritative if:**

- It uses a `.gov.sa` domain or a nationally recognized official domain for the body it represents.
- The body is the primary regulatory or issuing authority for the topic — not a portal that aggregates information from other bodies.
- The body is named by legislation, regulation, or royal decree as responsible for the domain in question.
- The information is consistent with what the primary body publishes through its own channels.

**A source is likely not authoritative if:**

- It is a third-party summary, a consultancy guide, or a news article about the regulation.
- It is a government portal that aggregates services but does not itself set rules (e.g., a unified portal). Such portals are useful for procedure, but the underlying authority for any rule remains the ministry or body that issued it.
- It is a translation of another body's content without citing the primary source.
- The domain does not clearly identify the issuing body.

**When authority is unclear:**

Do not guess. Add a placeholder noting that the authority for this topic needs to be confirmed, and record the competing sources in the `notes` field.

---

## 3. How to Record `last_verified`

The `last_verified` field records when the content of a dataset entry was last confirmed against a live official source.

**Format:** `YYYY-MM-DD` (ISO 8601). Example: `2025-11-14`.

**What it represents:** The date you personally reviewed the source and confirmed the information was present and accurate at that time.

**What it does not represent:** The date the official source last updated its content, or the date the dataset entry was created.

**Complementary field — `verification_method`:** Record a brief description of how you verified the entry. Examples:

- `"Manual review of the official portal on 2025-11-14. Located the relevant section under [section name]."`
- `"Reviewed the publicly accessible page. Content behind login was not reviewed and is marked as placeholder."`

**Do not:**
- Use a relative date ("last week", "recently").
- Set `last_verified` to a date in the future.
- Copy a `last_verified` date from another entry unless you personally reviewed that source on that date.

---

## 4. How to Handle Portals With Login Pages

Some official portals require user registration or login to access certain services or documentation. This affects what can be independently verified.

**Publicly accessible content:**

If the information you need is visible without logging in, verify it normally and record what you reviewed.

**Content behind a login wall:**

If specific information is only accessible after logging in (e.g., live fee schedules inside an account dashboard, or step-by-step process flows inside a registered employer account):

- Do not claim to have verified information you accessed only through a personal account, as it may be personalised or role-specific.
- Add a `placeholder` entry for any field that relies on login-only content.
- In the placeholder's `description`, note that the information is accessible only after login and requires in-person or account-based verification.
- Set `verification_method` to reflect what was and was not reviewed.

**Example placeholder for login-gated content:**

```json
{
  "field": "specific_procedure_steps",
  "description": "The step-by-step process for this action is only visible inside a logged-in account dashboard and could not be independently verified from the public portal.",
  "verify_at": "relevant-portal.gov.sa"
}
```

---

## 5. How to Handle Stale or Moved Pages

Official government portals are reorganized, and pages move or are removed. When a cited page no longer resolves:

**Step 1 — Check for a redirect.** Visit the URL. If it redirects to a new location on the same domain, confirm the content is still there and update `verification_method` to note the redirect.

**Step 2 — Search the portal.** Use the portal's own search function to look for the content by topic or keyword. If found at a new path, update `verification_method` accordingly.

**Step 3 — Check the portal homepage or sitemap.** Navigation menus and sitemaps often reveal where content has been reorganized.

**Step 4 — If not found:**

- Do not fabricate a replacement URL.
- Add or update a `placeholder` for the affected field, noting that the page could not be located.
- Set `verification_status` back to `draft` if the entry was previously `verified`.
- In `notes`, record what was searched and when.

**If the entire portal domain has changed:**

- Confirm the new domain from an official announcement or from cross-referencing other official sources that link to it.
- Update `official_website` in the dataset entry.
- Document the domain change in `verification_method`.
- Do not update the domain based on a search result alone.

---

## 6. How to Handle Conflicting Sources

Occasionally, two official sources will state different things about the same rule, threshold, or requirement. This can happen when one body has updated its guidance and another has not, or when portals aggregate information at different cadences.

**Do not choose one arbitrarily.** Record the conflict explicitly.

**Steps:**

1. Identify which body is the primary regulatory authority for the specific topic (see [Section 2](#2-how-to-decide-if-a-source-is-authoritative)).

2. If one source is clearly primary (e.g., the ministry that issues the regulation) and the other is secondary (e.g., a portal that summarizes it), give precedence to the primary source — but note the discrepancy in `notes`.

3. If both sources are primary and they conflict:
   - Set the affected field to a value that reflects both positions, or leave it as a placeholder.
   - Add a `placeholder` entry describing the conflict, what each source states, and where each was found.
   - Do not set `verification_status` to `verified` while the conflict remains unresolved.

4. In the `notes` field, briefly describe the conflict: which sources conflict, on what point, and what was done.

**Example note entry:**

> "As of [date], [Source A] states X, while [Source B] states Y on the same topic. Source A is the primary regulatory body. Discrepancy noted. Placeholder added pending resolution."

---

## 7. When to Mark a Source as `draft`

Set `verification_status` to `draft` when:

- The entry has just been created and has not yet been manually reviewed against a live official source.
- Any field in the entry contains a placeholder (i.e., `placeholders` array is non-empty).
- The entry was previously `verified` but a review found the content has changed, moved, or could not be confirmed.
- A conflicting source has been identified and the conflict is unresolved.
- `last_verified` is more than 12 months old and the entry has not been re-reviewed.
- You are uncertain about the accuracy of any field and cannot immediately resolve it.

`draft` is the safe, default state. It signals that the entry is present in the dataset but should not be treated as confirmed.

---

## 8. When to Mark a Source as `verified`

Set `verification_status` to `verified` only when **all** of the following conditions are met:

- [ ] You have personally reviewed the source against a live official portal.
- [ ] All fields in the entry reflect what the official source currently states.
- [ ] The `placeholders` array is empty — every placeholder has been resolved.
- [ ] `last_verified` is set to the date of your review in `YYYY-MM-DD` format.
- [ ] `verification_method` describes what you reviewed and how.
- [ ] No unresolved conflicts with other official sources exist.
- [ ] Content behind login walls is either not relevant to the entry or is explicitly documented as a placeholder.

If any condition is not met, the entry must remain `draft`.

> **Verified does not mean permanent.** A verified entry can become outdated. Contributors should flag entries for re-review if they have reason to believe the underlying source has changed.

---

## Summary Checklist

Use this as a quick-reference before updating `verification_status`.

| Check | Required for `verified` |
|---|---|
| Navigated directly to official domain | Yes |
| Domain matches `official_website` field | Yes |
| Specific content located on the page | Yes |
| `last_verified` set to `YYYY-MM-DD` | Yes |
| `verification_method` describes what was reviewed | Yes |
| `placeholders` array is empty | Yes |
| No unresolved conflicting sources | Yes |
| Login-gated content documented if applicable | Yes |
| Source is primary authority for the topic | Yes |

---

*See also: [Source Review Template](../../templates/source-review.md) — [Arabic version](../ar/source-verification.md)*
