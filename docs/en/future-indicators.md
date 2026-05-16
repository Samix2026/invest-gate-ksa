# Future Indicators — Economic and Statistical Context

> **Disclaimer:** This document is for general informational purposes only. It describes potential future additions to this repository — not current verified data. Any economic or statistical indicator added to this repository must be sourced from an official authority, timestamped, and re-verified regularly. Do not rely on this document as investment guidance.

---

## Purpose

This document outlines categories of economic and statistical indicators that may be added to this repository in future development phases. It is a planning reference for contributors — not a data source.

Economic indicators can help foreign investors understand the broader context for investment decisions. However, indicators are inherently time-sensitive: figures become stale, methodologies change, and rankings can shift dramatically between publication cycles. Any such data added to this repository will require:

- **A confirmed official source** — a `.gov.sa` domain or a recognized international statistical authority
- **A publication date** — the date the figure was published by the source
- **A verification date** — the date a contributor verified the figure against the live source
- **A methodology note** — a brief description of how the indicator is calculated or ranked, as methodologies can change between editions

This repository will not store indicators without all four elements. Until they are added with full provenance, this document serves as the placeholder.

---

## Potential Indicator Categories

### 1. FDI Flows

**What this covers:** Foreign direct investment inflows and outflows — the volume and direction of foreign capital entering Saudi Arabia as new investment (greenfield projects, expansions, or acquisitions).

**Why it matters to investors:** FDI data signals overall investment sentiment, sectoral attractiveness, and the trajectory of the economy as a reform destination.

**Likely authoritative sources:** The General Authority for Statistics (GASTAT) publishes national accounts and investment statistics. UNCTAD (United Nations Conference on Trade and Development) and the IMF also publish Saudi FDI data using internationally comparable methodologies.

**Verification and timeliness notes:**
- FDI figures are typically published with a lag of one to two reporting periods. Always check the reference year, not just the publication date.
- Methodological definitions of FDI (threshold for controlling interest, treatment of reinvested earnings, etc.) can differ between sources. Always note which methodology and which source edition the figure comes from.
- Figures may be revised after initial publication — do not treat any figure as final until confirmed as such by the source.

---

### 2. Sector Growth

**What this covers:** GDP contribution and growth rates by economic sector — for example, non-oil GDP growth, manufacturing sector output, and services sector expansion.

**Why it matters to investors:** Sector growth data indicates which parts of the economy are expanding and provides context for sectoral investment decisions.

**Likely authoritative sources:** GASTAT publishes GDP by sector as part of national accounts. The Saudi Central Bank (SAMA) also publishes economic indicators including sectoral data.

**Verification and timeliness notes:**
- National accounts data is typically released quarterly or annually and is subject to revision.
- "Non-oil GDP" is a frequently cited indicator for Saudi economic diversification — verify the calculation methodology and reference period for any figure used.
- Sector classifications may change over time; ensure the classification used in one period is consistent with another when making comparisons.

---

### 3. Labor Market Indicators

**What this covers:** Employment rates, labor force participation rates, Saudization (Nitaqat) compliance rates, and unemployment rates broken down by demographic category.

**Why it matters to investors:** Labor market conditions affect workforce availability, hiring costs, and regulatory compliance planning for Saudization requirements.

**Likely authoritative sources:** GASTAT publishes the Labor Force Survey. The Ministry of Human Resources and Social Development (MHRSD) publishes Nitaqat compliance data.

**Verification and timeliness notes:**
- Labor force surveys use sampling methodologies that can change between survey editions — check the methodology note for each edition before comparing figures across periods.
- Saudization (Nitaqat) band thresholds are periodically revised by MHRSD. Any figures cited must be matched to the regulatory version in force at the time.
- Unemployment figures may be broken down by nationality and gender; ensure figures are used in context and not compared across incompatible demographic definitions.

---

### 4. Ease of Doing Business Alternatives

**What this covers:** Composite indicators or sub-indicators that measure the regulatory environment for business — covering areas such as starting a business, obtaining permits, registering property, and enforcing contracts.

**Background:** The World Bank Doing Business report, which was the primary global reference for this category, was discontinued in 2021. Alternative frameworks and indicators now exist, but no universally adopted replacement has emerged. Any indicator in this category must clearly identify the framework, the methodology, and the publication edition used.

**Likely authoritative sources:** The World Economic Forum (Global Competitiveness Index), the IMD World Competitiveness Ranking, and Saudi government reform tracking dashboards (where officially published) may serve as references. Official Saudi government sources take precedence for domestic regulatory process data.

**Verification and timeliness notes:**
- Rankings in this category are methodologically heterogeneous — a country's position can change significantly simply because the ranking methodology changed, not because the underlying business environment changed.
- Do not cite a ranking without specifying the edition year and methodology version.
- Government-published reform progress reports should be dated and linked to the official publication.

---

### 5. Logistics Performance

**What this covers:** Indicators measuring trade logistics infrastructure, customs efficiency, and supply chain reliability — including port performance, customs clearance processes, and logistics cost benchmarks.

**Why it matters to investors:** Logistics performance affects import-export costs, supply chain planning, and the feasibility of manufacturing and distribution operations.

**Likely authoritative sources:** The World Bank Logistics Performance Index (LPI) is a commonly referenced composite indicator. GASTAT and the Saudi Ports Authority (Mawani) may publish domestic logistics data.

**Verification and timeliness notes:**
- The LPI is published periodically (not annually) — always cite the edition year.
- Sub-indicators (customs, infrastructure, timeliness) are more actionable than the composite score; consider citing the relevant sub-indicator rather than the overall rank.
- Domestic logistics data from official Saudi sources takes precedence over composite international indices for operational planning purposes.

---

### 6. Digital Economy Indicators

**What this covers:** Indicators measuring the scale and maturity of digital infrastructure and activity — including internet penetration, e-government adoption, digital payment volumes, and the ICT sector's contribution to GDP.

**Why it matters to investors:** Digital economy indicators are particularly relevant for technology, fintech, and e-commerce investors evaluating market readiness and infrastructure.

**Likely authoritative sources:** GASTAT publishes ICT statistics. The Communications, Space and Technology Commission (CST) publishes sector-specific data on telecommunications and digital services. The International Telecommunication Union (ITU) publishes internationally comparable data.

**Verification and timeliness notes:**
- Digital economy definitions vary across sources — what one source classifies as the "digital economy" may differ from another. Note the definition used.
- Penetration and adoption metrics can change rapidly; figures older than one to two years may not reflect current conditions in fast-moving digital markets.
- Data on e-government adoption and digital payments from Saudi official sources should be preferred over international composite indices for operational planning.

---

## Requirements for Adding Indicators to This Repository

Before any indicator is added to a dataset in this repository, the contributor must record all of the following:

1. **Source name and authority type** — official government body, international statistical organization, or recognized composite index publisher
2. **Publication date** — the date the figure was published by the source (not the date it was added to this repository)
3. **Reference period** — the time period the figure covers (calendar year, quarter, survey wave)
4. **Verification date** — the date a contributor verified the figure against the live official source
5. **Methodology note** — a brief description of how the indicator is defined and calculated, noting any known limitations or caveats
6. **Version identifier** — the edition or version of the publication (especially critical for rankings and indices that change methodology between editions)

Figures added without all six elements will be given `verification_status: "draft"` and must include placeholder entries for any missing fields. Rankings and composite scores that do not include a methodology version and edition year will not be accepted.

---

## Status

This document is a planning reference. No statistical or economic indicator datasets have been added to the repository yet. See [roadmap.md](../../roadmap.md) for the development plan.
