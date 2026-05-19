---
You are adding a new fee entry to invest-gate-ksa.

## Inputs
- Authority ID: $ARGUMENTS (first word — must exist in sources.en.json)
- Fee description: $ARGUMENTS (middle words)
- Source URL: $ARGUMENTS (last word if starts with http)

## Step 1 — Verify authority exists
Open data/sources.en.json.
Confirm the authority id exists. If not, stop and instruct to run 
/project:add-source first.

## Step 2 — Check schema
Open schemas/fees.schema.json.
Read all required fields and the fee_type enum values.
Your new entry must use only schema-defined fields and valid enum values.

## Step 3 — Determine verification_status
If source URL is an official government domain (.gov.sa or ecza.gov.sa):
  Set verification_status: "verified"
If source is a commercial or legal advisory site:
  Set verification_status: "draft"
  Set placeholder_reason to explain: "Reported by [source] but not confirmed 
  from official government source. Verify at: [official URL]"

## Step 4 — Add to data/fees.en.json
Generate a unique id following existing patterns (lowercase_snake_case).
Add entry with all required schema fields.
If amount is unknown: amount_sar: 0 with detailed placeholder_reason.
If amount is zero (confirmed free): amount_sar: 0 with placeholder_reason 
stating "Confirmed free per [source]."

## Step 5 — Add to data/fees.ar.json
Mirror entry. id identical. Text fields in Arabic MSA.
No tashkeel. English numerals.

## Step 6 — Validate and commit
Run: python3 scripts/check.py
Run: python3 scripts/validate-data.py

git add -A
git commit -m "feat: add fee — {authority}/{fee-type}

Amount: SAR {amount} ({frequency})
Status: {verification_status}
Source: {source-url}"
git push origin main

## Hard rules
- amount_sar must never be fabricated — use 0 + placeholder_reason if unknown
- verification_status: "verified" only for .gov.sa sources
- fee_type must use valid schema enum value
- Never skip the AR mirror
- ids identical between EN and AR
