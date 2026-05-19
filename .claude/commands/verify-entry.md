---
You are verifying an existing entry in the invest-gate-ksa knowledge base.

## Inputs
- Dataset: $ARGUMENTS (first word — e.g. fees, timelines, sources, sezs)
- Entry ID: $ARGUMENTS (second word)
- Official source URL: $ARGUMENTS (third word, if provided)

## Step 1 — Read current state
Open the relevant data/{dataset}.en.json and data/{dataset}.ar.json.
Find the entry with the specified id.
Read its current verification_status, placeholder_reason, and verify_at.

## Step 2 — Verify
If a source URL was provided, read the content at that URL.
Extract only facts that are explicitly stated in the official source.
Do NOT infer, interpolate, or use commercial sources as substitutes 
for official government sources.

## Step 3 — Update EN file
Update the entry with verified data:
- Replace placeholder values with actual verified values
- Set verification_status: "verified"
- Update placeholder_reason to describe what was confirmed and where
- Set verify_at to the official source URL
- Do not add fields not in the schema

## Step 4 — Update AR file  
Apply identical updates to data/{dataset}.ar.json.
Translate all text fields to Arabic MSA.
Rules: no tashkeel, English numerals, formal MSA.
id must remain identical to EN file.

## Step 5 — Check for downstream impact
Search docs/en/ and docs/ar/ for any mention of this entry or topic.
If any doc contains a placeholder or outdated value, update it.

## Step 6 — Remove from source-gaps if present
Search data/source-gaps.en.json and data/source-gaps.ar.json.
If an entry related to this topic exists, remove it (gap is now closed).
Apply to both EN and AR files.

## Step 7 — Validate and commit
Run: python3 scripts/check.py
Run: python3 scripts/validate-data.py
Both must pass.

Then commit:
git add -A
git commit -m "verified: {dataset}/{entry-id} — {one-line summary}

Source: {official-source-url}
Date: {today}"
git push origin main

## Hard rules
- verification_status: "verified" ONLY if confirmed by official government source
- If source is commercial only: set verification_status "draft", not "verified"
- Never invent amounts, rates, or timelines
- Never remove placeholder_reason entirely — replace it with confirmation text
- Arabic: no tashkeel, English numerals, formal MSA
- ids must be identical between EN and AR files
