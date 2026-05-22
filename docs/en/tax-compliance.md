---
title: "Tax Compliance for Foreign Investors in Saudi Arabia"
language: en
last_verified: "2026-05-21"
verification_method: "Data cross-referenced from data/fees.en.json entries (verified) and docs/en/company-setup-overview.md. ZATCA obligations verified from zatca.gov.sa published guidance."
sources:
  - zatca.gov.sa
related:
  - docs/ar/tax-compliance.md
  - docs/en/corporate-banking.md
  - data/fees.en.json
---

# Tax Compliance for Foreign Investors in Saudi Arabia

> **Disclaimer:** This document is for general educational purposes only. It is not tax or legal advice. Tax rates, thresholds, and filing requirements change. Always verify current obligations directly with ZATCA at [zatca.gov.sa](https://zatca.gov.sa) and consult a qualified tax professional before filing.

---

## Overview — The Saudi Dual Tax System

Saudi Arabia uses a **dual-track tax system** that applies different taxes depending on the ownership structure of the company:

- **Foreign shareholders** are subject to **Corporate Income Tax (CIT)** on their share of profits
- **Saudi and GCC shareholders** are subject to **Zakat** on their share of the net worth base

Both can apply simultaneously in a mixed-ownership company. VAT and Withholding Tax (WHT) apply regardless of ownership structure.

All tax obligations are administered by the **Zakat, Tax and Customs Authority (ZATCA)** at [zatca.gov.sa](https://zatca.gov.sa).

See `data/fees.en.json` entries `cit_corporate_income_tax`, `zakat_saudi_gcc_shareholders`, and `wht_withholding_tax` for the underlying verified dataset records.

---

## Summary Table

| Tax | Rate | Applies To | Basis |
|-----|------|------------|-------|
| Corporate Income Tax (CIT) | 20% | Foreign shareholders' share | Net adjusted profits |
| Zakat | 2.5% | Saudi/GCC shareholders' share | Net worth base (not profits) |
| VAT | 15% | All registered businesses | Taxable supplies |
| WHT — Dividends | 5% | Payments to non-residents | Gross amount |
| WHT — Royalties | 15% | Payments to non-residents | Gross amount |
| WHT — Services | Up to 20% | Payments to non-residents | Gross amount (varies by treaty) |

---

## Corporate Income Tax (CIT) — Foreign Shareholders

**Rate:** 20% of net adjusted profits attributable to foreign shareholders.

CIT applies to the **foreign shareholder's share** of the company's net profits, not to the company's total profits. In a 100% foreign-owned entity, CIT applies to 100% of net profits. In a mixed-ownership entity, CIT applies only to the foreign-ownership percentage.

**Filing authority:** ZATCA  
**Filing deadline:** Within 120 days after the fiscal year end  
**Payment:** With the annual tax return submission

CIT is calculated on net adjusted profits — not gross revenue. Allowable deductions include business expenses, depreciation, and other ZATCA-approved items.

---

## Zakat — Saudi and GCC Shareholders

**Rate:** 2.5% of the Zakat base (net worth base, not profits).

Zakat is an Islamic levy on wealth, not income. The Zakat base is broadly the company's net worth attributable to Saudi/GCC shareholders, calculated per ZATCA's Zakat rules. This means Zakat can be due even in a loss-making year if the net worth base is positive.

**Filing authority:** ZATCA  
**Filing deadline:** Within 120 days after the fiscal year end

For 100% foreign-owned companies, Zakat does not apply — only CIT applies.

---

## VAT

**Rate:** 15% on taxable supplies of goods and services.

**Registration thresholds:**
- Mandatory registration: annual taxable supplies exceeding SAR 375,000
- Voluntary registration: annual taxable supplies exceeding SAR 187,500

**Filing frequency:**
- Monthly: companies with annual revenue above SAR 40 million
- Quarterly: all other registered companies

Input VAT paid on business purchases can be offset against output VAT collected on sales. The net amount is remitted to ZATCA.

**Registration deadline:** Within 30 days of exceeding the mandatory threshold, or 60 days from commencing business (whichever applies).

---

## Withholding Tax (WHT)

WHT applies to certain payments made by a Saudi-registered company to **non-resident** recipients — companies or individuals not registered in Saudi Arabia.

| Payment Type | WHT Rate |
|-------------|----------|
| Dividends | 5% |
| Loan interest | 5% |
| Royalties and technical fees | 15% |
| Management fees | 20% |
| Services (general) | 5–20% (varies) |
| Air/sea freight | 5% |

**Payment deadline:** WHT must be remitted to ZATCA by the first 10 days of the month following the payment month.

**Double Taxation Treaties (DTTs):** Saudi Arabia has concluded DTTs with numerous countries. A DTT may reduce or eliminate the applicable WHT rate. Verify treaty applicability and claim procedures at [zatca.gov.sa](https://zatca.gov.sa).

---

## Key Deadlines

| Obligation | Deadline | Authority |
|------------|----------|-----------|
| ZATCA registration | Within 60 days of commencing business | ZATCA |
| VAT registration (mandatory) | Within 30 days of exceeding SAR 375,000 threshold | ZATCA |
| Annual tax return (CIT/Zakat) | Within 120 days after fiscal year end | ZATCA |
| VAT filing — monthly | By the 15th of the following month | ZATCA |
| VAT filing — quarterly | By the 15th of the month following the quarter | ZATCA |
| WHT payment | First 10 days of the following month | ZATCA |
| Record retention | 10 years from the end of the tax year | ZATCA |

---

## E-Invoicing (Fatoora)

Saudi Arabia mandates electronic invoicing for all B2B and B2G transactions under the **Fatoora** e-invoicing system.

**Phase 2 (Integration Phase):** Mandatory from 2025 for companies meeting the revenue threshold. Requires integration with ZATCA's e-invoicing platform. All invoices must be generated and submitted through a ZATCA-compliant e-invoicing solution.

Failure to comply with Fatoora requirements exposes the company to ZATCA penalties.

**Verify current rollout scope and thresholds at:** [zatca.gov.sa](https://zatca.gov.sa)

---

## Mixed Ownership Example

For a company with 60% Saudi ownership and 40% foreign ownership:

| Shareholder | Ownership | Tax Applied | Basis |
|-------------|-----------|------------|-------|
| Saudi shareholder | 60% | Zakat (2.5%) | 60% of Zakat base (net worth) |
| Foreign shareholder | 40% | CIT (20%) | 40% of net adjusted profits |

Both taxes are filed and paid to ZATCA. The company files a combined annual return covering both obligations.

Note: This example illustrates the general principle. Actual Zakat and CIT calculations involve detailed ZATCA rules. Engage a qualified tax advisor for actual filing.

---

## Official Sources

| Authority | URL |
|-----------|-----|
| ZATCA (Zakat, Tax and Customs Authority) | [zatca.gov.sa](https://zatca.gov.sa) |
| ZATCA e-invoicing (Fatoora) | [fatoora.zatca.gov.sa](https://fatoora.zatca.gov.sa) |
| Repository dataset | `data/fees.en.json` — entries `cit_corporate_income_tax`, `zakat_saudi_gcc_shareholders`, `wht_withholding_tax` |
