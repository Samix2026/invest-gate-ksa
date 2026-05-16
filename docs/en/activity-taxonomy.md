# Economic Activity Taxonomy — Foundation Layer

> **Disclaimer:** This document is for general informational and architectural purposes only. It describes the classification framework that will underpin future datasets in this repository — not regulatory guidance. No activity codes, ownership determinations, or licensing claims appear here. Verify all regulatory requirements with official Saudi government sources.

---

## Purpose

This document establishes the conceptual and architectural foundation for a future economic activities dataset in this repository. It explains what activity classification is, why it matters for investors, how ISIC4 relates to the Saudi national classification, and how this layer fits into the broader data model.

No activity data has been added yet. The companion schema (`schemas/economic-activities.schema.json`) defines what a future dataset entry will look like. This document explains the reasoning behind that design.

---

## What is ISIC4?

The **International Standard Industrial Classification of All Economic Activities, Revision 4** (ISIC4) is the United Nations classification framework for economic activities. It is published and maintained by the United Nations Statistics Division (UNSD) and serves as the international reference point from which most national classification systems are derived.

ISIC4 organizes all economic activity into a four-level hierarchy:

| Level | Notation | Description |
|---|---|---|
| Section | Single letter (A–U) | Broadest grouping — e.g. "Information and Communication" |
| Division | 2-digit code | Major sub-grouping within a section |
| Group | 3-digit code | Finer grouping within a division |
| Class | 4-digit code | Most granular level — the unit typically used for classification |

Each class has an official label describing the economic activities it covers. The current revision (Rev. 4) was published in 2008. National statistical offices and regulators typically adapt ISIC4 into local classifications suited to their economic structure and regulatory needs.

ISIC4 serves two purposes in this repository: it provides an internationally comparable reference point for each activity, and it enables cross-referencing with international datasets (FDI statistics, sector growth data, labor market surveys) that use ISIC4 as a reporting standard.

---

## ISIC4 and Saudi Activity Classification

Saudi Arabia uses its own **National Classification of Economic Activities**, which is aligned with ISIC4 but includes local adaptations reflecting the structure of the Saudi economy and its regulatory framework. The national classification is used in official statistical reporting by the General Authority for Statistics (GASTAT).

For foreign investors, the more directly relevant reference is **MISA's Approved Activities List** (قائمة الأنشطة المعتمدة) — the official list of economic activities open to foreign investors, maintained by the Ministry of Investment. Each activity on this list has an official name in both Arabic and English and an associated code used in the investment registration process.

The Ministry of Commerce uses activity codes in commercial registration, determining the legal scope of what an entity is authorized to do.

**The relationship between ISIC4 and the Saudi classification is not one-to-one.** Three patterns commonly arise:

1. **Many-to-one:** A Saudi activity may span what ISIC4 treats as multiple classes — the Saudi classification groups them under a single activity category.
2. **One-to-many:** An ISIC4 class may be split into multiple Saudi activities with different names, codes, or regulatory paths.
3. **No direct equivalent:** Some Saudi-specific activities (particularly those arising from local regulatory structure or Vision 2030 programs) may not have a close ISIC4 analogue.

This is why the dataset schema tracks ISIC4 and Saudi classification fields separately, each nullable, rather than assuming direct correspondence.

---

## Why Activity Classification Matters

For foreign investors in Saudi Arabia, the specific activity code is not a bureaucratic detail — it is the central variable that determines the regulatory path.

**MISA investment registration is activity-specific.** A foreign investor does not register for a general business purpose; they register to conduct specific, named activities. The registration authorizes those activities and defines the permitted scope of the entity. A change in business activity may require updating or replacing the registration.

**Different activities trigger different regulatory authorities.** Beyond the universal MISA and Ministry of Commerce steps, specific activities may involve sector regulators. An activity in financial services involves SAMA or the CMA. An activity in healthcare involves the Ministry of Health. An activity in food production involves the SFDA. The applicable regulatory path is determined by activity type, not by sector label.

**Saudization (Nitaqat) requirements vary by activity.** The required ratio of Saudi nationals in the workforce is calculated using activity-based classifications. Two businesses in the same broad sector may face different Nitaqat targets depending on their registered activity categories.

**Some activities have foreign ownership restrictions.** The list of activities open to 100% foreign ownership, activities requiring a local partner, and activities that are restricted entirely is defined and updated by MISA at the activity level — not at the sector level. The sector is an orientation category; the activity code is the regulatory unit.

---

## Sectors vs. Activities

The `data/sectors.*.json` dataset in this repository contains 11 entries: broad groupings like "Technology", "Healthcare", "Manufacturing", and "Fintech". These sector entries serve as orientation guides — they describe the typical regulatory landscape, common business models, and key authorities for a broad area of investment.

Activities are a different level of granularity. A single sector entry may encompass dozens or hundreds of individual activities, each with its own official name, code, and potentially distinct regulatory treatment.

To illustrate the distinction without using specific codes: the "Technology" sector entry in this repository describes the landscape for technology businesses in general. Within that sector, a software development activity, a data center operations activity, and a cybersecurity services activity each have their own MISA activity name and code, and may face different regulatory considerations — one may require engagement with the Communications, Space and Technology Commission (CST), another may not.

The relationship between sectors and activities in this repository is intended to be:

- **Sectors provide strategic orientation** — useful for investors asking "is this the right broad area for my business?"
- **Activities provide operational precision** — required for investors asking "exactly what am I registering for, and what does that require?"

The future activity dataset will link each activity to one or more sector entries via the `related_sectors` field, enabling navigation in both directions: from sector to activities, and from activity to sector context.

---

## Why Activities Must Not Be Free-Text

Free-text activity descriptions — arbitrary phrases describing what a business does — cannot serve the regulatory purpose that activity classification serves. There are four reasons this matters for this repository.

**1. Regulatory systems require selection from an approved list.** MISA requires investors to select activities from the approved activities list. Arbitrary text is not accepted. The official name used in the registration must match the name on the list. A description that captures the investor's intent in natural language may not correspond to any approved activity name.

**2. Official names are precise and non-obvious.** Colloquial descriptions of a business activity often differ from its official classification name. An activity that an investor describes as "building mobile apps" may officially be classified under a specific software development or application development activity name — or it may span multiple activities depending on the nature of the work. Only the official name and code carry regulatory meaning.

**3. Similar-sounding activities can have different regulatory paths.** "Advisory services" and "financial advisory services" may appear nearly synonymous in natural language, but one may require sector-specific licensing from a financial regulator while the other does not. "Recruitment services" and "executive recruitment services" may have different Nitaqat implications. Free-text descriptions cannot distinguish these cases reliably.

**4. Data integrity for AI and MCP use.** This repository is intended to serve as a knowledge base for AI-assisted investor guidance and an MCP server. For that purpose, activity data must be structured, coded, and linked — not stored as unstructured text. A natural-language activity description cannot be programmatically resolved to a regulatory path, an authority, or a setup flow. Structured activity codes with verified official names can be.

---

## Future Dataset Plans

The economic activities dataset, once populated, is planned to support the following mappings:

**Activity → Sector:** Each activity will link to one or more sector entries in `data/sectors.*.json`, enabling a user who starts from a sector to drill down to specific activities, and a user who starts from an activity to navigate to sector-level regulatory context.

**Activity → Authorities:** Each activity will identify the regulatory authorities relevant specifically to that activity, complementing the broader authority coverage in the sector entries. This supports activity-level queries of the form "what authorities are involved when registering to do X?"

**Activity → License Concepts:** Each activity will link to the relevant license concepts in `data/investment-licenses.*.json` — MISA investment registration, commercial registration, municipal license, and so on — with any activity-specific notes that differ from the general description.

**Activity-level verification notes:** Some activities have specific points of confusion, historical classification changes, or regulatory edge cases that do not arise at the sector level. These will be captured in the `common_confusions` and `notes` fields of each activity entry.

The goal is to enable queries at activity granularity — "I want to do X: what is the setup path, which authorities are involved, and what are the common mistakes?" — rather than relying solely on sector-level orientation.

---

## Schema Design Notes

The schema at `schemas/economic-activities.schema.json` establishes the field structure for future activity entries. Key design decisions:

**Dual classification fields.** Each entry carries both an `isic4` object (section, division, group, class, label, alignment note) and a `saudi` object (activity code, official Arabic name, official English name, MISA approved list status, alignment note). These are kept separate because the mapping between them is not always direct. All sub-fields are nullable to allow draft entries to be created before full classification research is complete.

**Official names must not be paraphrased.** The schema description on `activity_name_en` and `activity_name_ar` requires that these fields contain the exact official name from the source. This is enforced editorially (not by the schema validator) and documented in the field descriptions.

**Draft/verified lifecycle.** Consistent with all other datasets in this repository, draft entries require at least one placeholder. An entry may be created with nullable classification fields and placeholder entries explaining what verification is needed; the entry graduates to `"verified"` only when all placeholders are resolved against live official sources.

**Cross-dataset references.** The `related_sectors`, `likely_authorities`, and `related_license_concepts` fields use IDs from other datasets in this repository — enabling programmatic joins and consistent navigation across the data model.

---

## Status

No activity data has been added to this repository. This document and `schemas/economic-activities.schema.json` define the foundation layer. Activity data will be added in a future development phase after the source verification workflow for activity classification is established. See [roadmap.md](../../roadmap.md) for the development plan.
