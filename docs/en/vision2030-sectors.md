# Vision 2030 — Sector Alignment for Foreign Investors

> **Educational context only.** This document summarises publicly reported Vision 2030 targets for investment-relevant sectors. It is not investment advice, regulatory guidance, or a guarantee of incentives. All targets are government-stated aspirations; actual outcomes depend on policy implementation.

---

## Macroeconomic Overview

Vision 2030 was launched in 2016. As of 2025, headline macro targets are:

| Indicator | 2016 Baseline | 2025 Actual | 2030 Target |
|---|---|---|---|
| Non-oil GDP share | ~16% | ~55% | 50%+ |
| Private sector GDP share | ~40% | ~46% | 65% |
| Unemployment rate (Saudi nationals) | ~12.8% | ~7.0% | 7% — **achieved Q4 2024** |
| FDI annual inflows (USD billion) | ~USD 7B | ~USD 35B | USD 103B |
| Tourism contribution to GDP | ~3% | ~7% | 10% |
| International tourist arrivals | ~18M | ~100M+ | 150M |
| Renewable energy share of electricity | ~0% | ~18% | 50% |
| Non-oil exports share | ~16% | ~35% | 50% |

*Sources: Vision 2030 Annual Report 2025; NIS; Arab News; MISA.*
*All macro-level figures are reported/estimated. Verify individual targets at official Vision 2030 portals before citing.*

---

## Priority Sectors for Foreign Investment

Sectors are classified by their tier in the Vision 2030 National Investment Strategy (NIS).

### 🎯 Critical Priority

These sectors are central to the Vision 2030 diversification mandate and receive the most active FDI policy support.

#### Technology
- **V2030 Target:** Establish Saudi Arabia as a regional tech hub; attract leading global technology companies; build local digital infrastructure capacity.
- **Supervising Program:** Digital Government Authority (DGA) / Saudi Vision 2030 Digital Pillar
- **Regulatory Sensitivity:** Regulated
- **SEZ Availability:** Cloud Computing SEZ (Riyadh) — OECD-aligned framework
- **Setup Flow:** E-commerce Company Setup (query: `python3 scripts/query-dataset.py --dataset setup-flows --id ecommerce_company_setup`)

#### Fintech
- **V2030 Target:** 70% cashless transactions by 2030 (reported ~79% actual as of 2024)
- **Supervising Program:** Saudi Central Bank (SAMA) Fintech Initiative; Financial Sector Development Program (FSDP)
- **Regulatory Sensitivity:** Highly Regulated (SAMA + CMA dual oversight for some activities)
- **SEZ Availability:** Not applicable (financial services regulated on mainland)
- **Setup Flow:** Fintech Market Entry (query: `python3 scripts/query-dataset.py --dataset setup-flows --id fintech_market_entry`)

#### Manufacturing
- **V2030 Target:** USD 148B manufacturing GDP by 2035; 1.6M new manufacturing jobs
- **Supervising Program:** National Industrial Development and Logistics Program (NIDLP) / Ministry of Industry and Mineral Resources
- **Regulatory Sensitivity:** Regulated
- **SEZ Availability:** KAEC SEZ, Jazan SEZ, Ras Al-Khair SEZ — 5% CIT for 20 years, customs exemptions
- **Setup Flow:** Manufacturing Company Setup (query: `python3 scripts/query-dataset.py --dataset setup-flows --id manufacturing_company_setup`)

#### Tourism and Hospitality
- **V2030 Target:** 10% GDP contribution; 150M international visitors; 1.6M tourism sector jobs
- **Supervising Program:** Ministry of Tourism; Tourism Development Fund (TDF)
- **Regulatory Sensitivity:** Regulated (hotel licensing, tourism operator permits)
- **SEZ Availability:** Evaluated case-by-case in NEOM, Red Sea Project, Diriyah Gate zones

---

### 🔵 High Priority

These sectors have official V2030 programs and measurable targets, but with more sector-specific regulatory gatekeeping.

#### Healthcare
- **V2030 Target:** Increase private sector share of healthcare to 35%; expand insurance coverage to 100%
- **Supervising Program:** Vision 2030 Health Sector Transformation Program (HSTP)
- **Regulatory Sensitivity:** Highly Regulated (Saudi Health Council, SFDA, MoH)
- **Note:** Foreign ownership in healthcare requires specific MISA approvals; some sub-sectors restricted

#### Mining
- **V2030 Target:** Develop SAR 1.3 trillion (USD ~350B) in untapped mineral resources; mining to become third pillar of economy
- **Supervising Program:** Ministry of Industry and Mineral Resources; Saudi Arabian Mining Company (Maaden)
- **Regulatory Sensitivity:** Highly Regulated (Mining Investment Law; concession-based)
- **SEZ Availability:** Ras Al-Khair SEZ — industrial/mining focus

#### Entertainment and Events
- **V2030 Target:** 6% entertainment household spending (from <1% in 2016); develop domestic entertainment economy
- **Supervising Program:** General Entertainment Authority (GEA)
- **Regulatory Sensitivity:** Regulated (event licensing; GEA permits)

#### Media and Content
- **V2030 Target:** Regional media hub; develop Saudi content production industry
- **Supervising Program:** Ministry of Media; Saudi Broadcasting Authority
- **Regulatory Sensitivity:** Highly Regulated (content licensing; publishing restrictions apply)

---

### ⚪ Medium Priority

#### Real Estate
- **Regulatory Sensitivity:** Highly Regulated (foreign ownership restrictions; REGA licensing for brokers)
- **Note:** Real estate development for own use is more accessible than speculative residential investment for foreigners. Specific MISA registration required.

---

### ⚪ Supporting (Standard/Contextual)

The following sectors support the V2030 economy but are not named NIS investment priority targets:

| Sector | Regulatory Sensitivity | Notes |
|---|---|---|
| Consulting | Standard | Broad professional services; standard MISA + CR setup |
| E-commerce | Regulated | Digital platforms; ZATCA e-invoicing required |
| Food and Beverage | Regulated | SFDA licensing; municipal operating license |
| Education | Regulated | Ministry of Education approval for private institutions |
| Industrial Services | Regulated | Often linked to manufacturing and SEZ tenants |
| Hajj and Umrah Services | Highly Regulated | Ministry of Hajj and Umrah permits; seasonal demand |

---

## Cross-Reference: Setup Flows

Query setup flows via:
```bash
python3 scripts/query-dataset.py --dataset setup-flows --list
python3 scripts/query-dataset.py --dataset setup-flows --id foreign_consulting_company_setup
python3 scripts/query-dataset.py --dataset setup-flows --id ecommerce_company_setup
python3 scripts/query-dataset.py --dataset setup-flows --id manufacturing_company_setup
python3 scripts/query-dataset.py --dataset setup-flows --id fintech_market_entry
```

---

## Official Sources

- Vision 2030 Annual Report 2025: [vision2030.gov.sa](https://www.vision2030.gov.sa)
- National Investment Strategy (NIS): [nis.gov.sa](https://www.nis.gov.sa)
- MISA Sector Information: [misa.gov.sa](https://www.misa.gov.sa)
- Saudi Vision 2030 Macro Data: Arab News, NIS 2021 publication

> All V2030 sector targets marked `"draft"` in the dataset must be verified at the official Vision 2030 or NIS portals before use in investor-facing materials.
