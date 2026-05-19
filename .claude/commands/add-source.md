---
You are adding a new regulatory authority or official source to invest-gate-ksa.

## Inputs
- Authority name: $ARGUMENTS (first part)
- Official URL: $ARGUMENTS (last part if it starts with http)

## Step 1 — Check for duplicates
Open data/sources.en.json.
Search for any existing entry with a similar name or URL.
If found, report it and stop — do not create a duplicate.

## Step 2 — Determine the correct id
Follow existing id patterns in sources.en.json.
Format: lowercase_snake_case, abbreviation preferred (e.g. "misa", "zatca", "ecza").
The id must match the pattern ^[a-z][a-z0-9_]*$

## Step 3 — Add to data/sources.en.json
Add a new entry following the existing schema fields exactly.
Required fields: id, name, name_alt (abbreviation), authority_type, 
official_website, documentation_sections, verification_status, last_verified.
Set verification_status: "verified" only if you have confirmed this is 
an active official source.
Set last_verified: today's date.

## Step 4 — Add to data/sources.ar.json
Mirror entry with Arabic field values.
id must be identical to EN entry.
Arabic: no tashkeel, English numerals, formal MSA.

## Step 5 — Update sources/index.md
Add the new source to the appropriate table section in sources/index.md.
Format: | id | Name | Owner | Type | URL |

## Step 6 — Validate and commit
Run: python3 scripts/check.py
Run: python3 scripts/validate-data.py
Both must pass.

git add -A
git commit -m "feat: add source — {authority-name}

URL: {official-url}
Type: {authority_type}
Verified: {date}"
git push origin main

## Hard rules
- Never add a source without an official government or regulatory URL
- Never duplicate an existing source
- id must be identical between EN and AR
- Arabic: no tashkeel, English numerals, formal MSA
