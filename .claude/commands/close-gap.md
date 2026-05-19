---
You are closing a tracked source gap in invest-gate-ksa.

## Inputs
- Gap keyword or id: $ARGUMENTS (first part)
- Official source URL: $ARGUMENTS (if provided)

## Step 1 — Find the gap
Open data/source-gaps.en.json.
Find the entry matching the keyword or id.
Read its full description and priority level.

## Step 2 — Verify the information
If a source URL was provided, fetch and read it.
Extract only officially stated facts.
If the source is not official (.gov.sa or ecza.gov.sa), 
update the relevant data file as "draft" not "verified".

## Step 3 — Update the relevant dataset
Based on what the gap describes, identify which dataset to update:
fees, timelines, sources, sezs, sectors, structures, or setup-flows.
Apply the verified data to that dataset following verify-entry rules.

## Step 4 — Remove the gap entry
Remove the gap entry from data/source-gaps.en.json.
Remove the matching entry from data/source-gaps.ar.json.
Maintain bilingual parity — both files must have identical id counts.

## Step 5 — Validate and commit
Run: python3 scripts/check.py
Run: python3 scripts/validate-data.py

git add -A
git commit -m "fix: close source gap — {gap-description}

Resolved with: {source-url}
Updated: {dataset}/{entry-id}
Status: {verified|draft}"
git push origin main

## Hard rules
- Do not close a gap without actual verified data to replace it
- If source is insufficient, update placeholder_reason with better 
  guidance and leave the gap open
- Both source-gaps EN and AR must be updated together
- Never reduce gap count without adding verified data somewhere
