---
You are running a pre-publication quality check on invest-gate-ksa.

## Step 1 — Health check
Run: python3 scripts/check.py
Run: python3 scripts/validate-data.py
Both must pass with zero errors. Report the check count.

## Step 2 — Verification coverage report
Open all dataset files and count:
- Total entries across all datasets
- Entries with verification_status: "verified"
- Entries with verification_status: "draft"
- Entries that are placeholders (amount_sar: 0 with placeholder_reason)

Report as:
Verified:     X / Y entries (Z%)
Draft:        X / Y entries
Placeholders: X / Y entries

## Step 3 — Source gap review
Open data/source-gaps.en.json.
Count total gaps. List all gaps with priority: "high".
These must be acknowledged before publishing.

## Step 4 — Bilingual parity check
For each dataset, confirm EN entry count == AR entry count.
Report any mismatch.

## Step 5 — Dead link candidates
List all verify_at URLs that point to non-.gov.sa domains.
These are candidates for source upgrade — not errors, but worth reviewing.

## Step 6 — Terminology check
Search all markdown files in docs/ for:
- "MISA License" (should be "MISA Investment Registration")
- "annual renewal" related to CR (should reference April 2025 law)
- "رخصة" when referring to MISA registration types

Report any found instances.

## Step 7 — Summary report
Output a clean summary:

=== PRE-PUBLISH REPORT ===
Health checks:    ✅ {count}/{count}
Verified entries: {%}
High-priority gaps: {list}
Parity: ✅ / ❌
Terminology issues: {count}
Recommendation: READY / NOT READY (with reason)

Do not commit anything. This is a read-only audit command.
