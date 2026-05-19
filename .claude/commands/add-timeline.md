---
You are adding a processing timeline entry to invest-gate-ksa.

## Inputs
- Process name: $ARGUMENTS (words before the authority id)
- Authority ID: $ARGUMENTS (must exist in sources.en.json)
- Source URL: $ARGUMENTS (last word if starts with http)

## Step 1 — Verify authority exists
Open data/sources.en.json. Confirm authority id exists.

## Step 2 — Check schema
Open schemas/timelines.schema.json. Read all required fields.

## Step 3 — Determine values
- min_days: minimum confirmed processing time in working days
- max_days: maximum confirmed processing time in working days  
- typical_days: most common case in working days
- If any value is unknown: set to null with explanation in 
  placeholder_reason or conditions field
- unit: always "working_days" unless explicitly stated otherwise

## Step 4 — Determine verification_status
Official .gov.sa source: "verified"
Commercial source only: "draft"

## Step 5 — Add to data/timelines.en.json
Follow existing entry patterns. Generate id in lowercase_snake_case.

## Step 6 — Add to data/timelines.ar.json
Mirror. id identical. Arabic MSA. No tashkeel. English numerals.

## Step 7 — Validate and commit
Run: python3 scripts/check.py
Run: python3 scripts/validate-data.py

git add -A
git commit -m "feat: add timeline — {process-name}

Authority: {authority-id}
Duration: {min}–{max} working days (typical: {typical})
Status: {verification_status}
Source: {source-url}"
git push origin main

## Hard rules
- Never fabricate timeline numbers
- If unknown: null + placeholder_reason
- working_days is the standard unit
- ids identical between EN and AR
