# LLC Formation Checklist — Foreign Investor

> **Disclaimer:** This checklist is for general educational purposes only. It is not legal, financial, or regulatory advice. Requirements, fees, and timelines change. Always verify current requirements with the relevant authority and consult qualified professionals before proceeding.

**Entity type:** Limited Liability Company (LLC) — foreign-owned  
**Primary path:** Standard MISA Investment Registration → Commercial Registration → post-registration compliance

Use this checklist sequentially. Each step must be complete before the next step can begin.

---

## Pre-Checklist — Eligibility

Before starting, confirm eligibility for the standard MISA path:

- [ ] Applicant has an established foreign company (minimum 1 year of operation)
- [ ] Foreign company has a valid Commercial Registration (CR) in its home country
- [ ] Foreign company has audited financial statements for the last fiscal year
- [ ] Both documents are authenticated by the Saudi Embassy in the company's home country

> **If the applicant is an individual without an established foreign company:**  
> The standard path does not apply. Consider: (a) Saudi Premium Residency pathway, (b) GCC national pathway (registers directly with Ministry of Commerce), or (c) MISA Entrepreneurial Registration (requires support letter from MISA-recognized incubator/VC).  
> See: `docs/en/registration-types.md`

---

## Step 1 — MISA Investment Registration

**Authority:** Ministry of Investment (MISA)  
**Portal:** misa.gov.sa  
**Timeline:** 1–10 business days (simple cases: 1 day; regulated sectors: longer)  
**Fee:** Determined by MISA after approval and notified to applicant — not published in advance. Payment required within 15 business days of notification.

### Documents required

- [ ] Completed application via MISA e-portal
- [ ] Foreign company Commercial Registration — authenticated by the Saudi Embassy in the company's home country
- [ ] Audited financial statements (last fiscal year) — authenticated by the Saudi Embassy
- [ ] Articles of Association of the foreign parent company — authenticated by the Saudi Embassy
- [ ] Board Resolution authorizing the Saudi investment — notarized and authenticated by the Saudi Embassy
- [ ] Power of Attorney for the authorized representative in Saudi Arabia — notarized and authenticated
- [ ] Passport of the authorized representative

### Checklist

- [ ] Application submitted via MISA e-portal
- [ ] Fee notification received from MISA
- [ ] Fee paid within 15 business days of notification
- [ ] **Investment Registration Certificate (IRC) issued and active**

> **Common mistake:** Assuming the MISA registration fee is zero or fixed. The fee is activity-specific and communicated after approval. Budget for this before applying.  
> **Tip:** The IRC is activity-specific. If the business adds activities later, notify MISA — an amendment may be required.  
> See: `data/fees.en.json` — entry `misa_investment_registration_fee`

---

## Step 2 — Trade Name Reservation

**Authority:** Ministry of Commerce via Saudi Business Center (SBC)  
**Portal:** saudibc.gov.sa  
**Timeline:** Same day to 1–2 business days if the name requires review  
**Fee:** [placeholder — verify current fee at saudibc.gov.sa]

### Checklist

- [ ] Proposed trade name checked for availability via SBC portal
- [ ] Trade name reservation submitted
- [ ] **Trade name reservation confirmed**

> **Common mistake:** Choosing a name that conflicts with an existing registered trade name or that contains restricted words (government, national, Saudi, etc.) without approval.

---

## Step 3 — Business Premises and Electronic Lease (Ejari)

**Authority:** Ejar platform (Ministry of Housing)  
**Portal:** ejar.sa  
**Timeline:** Same day if landlord cooperates  
**Fee:** No government fee — lease registration is between landlord and tenant

### Checklist

- [ ] Business premises identified and lease agreed with landlord
- [ ] Electronic tenancy contract registered on the Ejar platform (both landlord and tenant must be registered)
- [ ] **Ejari lease certificate obtained for the business address**

> **Common mistake:** Using a paper tenancy contract or an unregistered lease. The Ministry of Commerce will not accept paper contracts — only Ejari-registered electronic leases are accepted for CR purposes.

---

## Step 4 — Articles of Association (AoA)

**Authority:** Ministry of Commerce (notarization)  
**Timeline:** 1–3 business days  
**Fee:** [placeholder — notarization fees vary; verify with a notary public]

### Documents required

- [ ] Draft AoA prepared in Arabic (bilingual drafts acceptable; Arabic is the legal version)
- [ ] AoA specifies: company name, purpose, capital contribution, partner details, profit distribution, management structure

### Checklist

- [ ] AoA drafted by a qualified legal advisor or using the Ministry of Commerce template
- [ ] **AoA notarized at a notary public office**

---

## Step 5 — Commercial Registration (CR)

**Authority:** Ministry of Commerce via Saudi Business Center (SBC)  
**Portal:** saudibc.gov.sa or mc.gov.sa  
**Timeline:** Same day to 7 business days (typical: 1 business day for standard activities)  
**Fee:** SAR 200/year (annual confirmation) + SAR 800+/year Chamber of Commerce membership

### Documents required

- [ ] Active MISA Investment Registration Certificate (IRC)
- [ ] Reserved trade name
- [ ] Ejari-registered electronic lease for business premises
- [ ] Notarized Articles of Association

### Checklist

- [ ] CR application submitted via SBC portal
- [ ] CR annual confirmation fee paid (SAR 200/year)
- [ ] Chamber of Commerce membership fee paid (SAR 800+/year)
- [ ] **Commercial Registration (CR) issued — 10-digit number starting with 7**

> **Note (April 2025 change):** A single national CR now covers all activities and branches nationwide. No separate branch CRs are required or available. CR has no expiry date — annual data confirmation replaces renewal.  
> **Common mistake:** Attempting to obtain a separate branch CR for a second location. Branch CRs were abolished in April 2025. A single CR covers all branches.  
> See: `data/fees.en.json` — entries `commercial_registration_issuance_fee` and `chamber_of_commerce_fee`  
> See: `docs/en/commercial-registration.md`

---

## Step 6 — Municipality Operating License (Balady)

**Authority:** Local municipality / Balady portal  
**Portal:** balady.gov.sa  
**Timeline:** [placeholder — varies by city and activity type; verify at balady.gov.sa]  
**Fee:** [placeholder — varies by city, premises size, and activity; verify at balady.gov.sa]

### Documents required

- [ ] Active Commercial Registration (CR)
- [ ] Ejari-registered electronic lease for the specific premises
- [ ] Premises inspection (where required by the municipality)
- [ ] Activity-specific approvals (e.g., civil defense, health, food safety) where applicable

### Checklist

- [ ] Balady portal account registered
- [ ] Operating license application submitted for business premises
- [ ] Any required inspections completed
- [ ] **Municipality Operating License (Balady license) issued for business premises**

> **Common mistake:** Opening to the public or commencing operations at the premises before the Balady license is issued.  
> **Tip:** Some activity types require additional sector regulator approvals (e.g., SFDA for food, MOH for health) before Balady will issue the license. Check requirements for your specific activity.

---

## Step 7 — ZATCA Tax Registration

**Authority:** Zakat, Tax and Customs Authority (ZATCA)  
**Portal:** zatca.gov.sa  
**Timeline:** [placeholder — verify current processing time at zatca.gov.sa]  
**Fee:** [placeholder — verify whether ZATCA charges a registration fee; see `data/fees.en.json` entry `zatca_vat_registration_fee`]

### Checklist

- [ ] ZATCA registration submitted (VAT registration when taxable turnover meets or exceeds the mandatory threshold)
- [ ] Tax Registration Number (TRN) received
- [ ] **ZATCA registration active**

> **Note:** VAT registration is threshold-based — not all companies must register immediately. Assess whether your projected turnover meets the mandatory VAT threshold.  
> For tax obligations (CIT 20%, Zakat 2.5% for Saudi/GCC shareholders, WHT rates), see: `docs/en/tax-compliance.md`  
> See: `data/fees.en.json` — entries `cit_corporate_income_tax`, `zakat_saudi_gcc_shareholders`, `wht_withholding_tax`

---

## Step 8 — GOSI Employer Registration

**Authority:** General Organization for Social Insurance (GOSI)  
**Portal:** gosi.gov.sa  
**Timeline:** [placeholder — verify current processing time at gosi.gov.sa]  
**Fee:** [placeholder — verify whether GOSI charges an employer registration fee; see `data/fees.en.json` entry `gosi_employer_registration_fee`]

**When required:** Before hiring any employees. GOSI registration is not required before commencing operations if there are no employees.

### Checklist

- [ ] GOSI employer account registered via gosi.gov.sa
- [ ] **GOSI employer registration confirmed**
- [ ] First employee registered with GOSI within the required timeframe after hire

> **Tip:** GOSI registration links to Nitaqat (Saudization) tracking. Employees must be GOSI-registered to count toward your Nitaqat quota.  
> See: `docs/en/nitaqat-saudization.md`

---

## Step 9 — Qiwa Employer Registration

**Authority:** Ministry of Human Resources and Social Development (MHRSD)  
**Portal:** qiwa.sa  
**Timeline:** 1 business day  
**Fee:** Free

### Checklist

- [ ] Qiwa employer account registered via qiwa.sa
- [ ] **Qiwa employer registration confirmed**

> **When required:** Before hiring any employees. Employment contracts for expatriate staff must be authenticated via the Qiwa platform.  
> See: `data/fees.en.json` — entry `qiwa_employer_registration_fee`

---

## Step 10 — Muqeem (Expatriate Employees Only)

**Authority:** Ministry of Interior — General Directorate of Passports (Jawazat)  
**Portal:** muqeem.sa  
**Fee:** SAR 51.75/year per employee (Iqama issuance/renewal)

**When required:** When hiring expatriate employees. Saudi employees do not require Muqeem / Iqama processing.

### Checklist

- [ ] Muqeem portal account linked to employer CR and GOSI registration
- [ ] Work permit obtained for each expatriate employee (via MHRSD / Absher)
- [ ] Iqama application submitted within 90 days of each employee's arrival
- [ ] Iqama fee paid (SAR 51.75/year per employee)
- [ ] **Iqama issued for each expatriate employee**

> **Critical:** Iqama must be issued within 90 days of the employee's arrival. Late issuance triggers penalties: SAR 500 first offense, SAR 1,000 second offense, then deportation proceedings.  
> See: `data/fees.en.json` — entries `iqama_issuance_renewal_fee`, `final_exit_visa_fee`, `exit_reentry_visa_extension_fee`

---

## Step 11 — Corporate Bank Account

**Authority:** SAMA-regulated Saudi bank (chosen by the company)  
**Timeline:** 7–28 business days from complete document submission  
**Fee:** No government fee — banks set their own account maintenance terms

**Prerequisites before visiting the bank:**

- [ ] Active MISA Investment Registration Certificate (IRC)
- [ ] Active Commercial Registration (CR) with current annual confirmation
- [ ] National Address registered via Absher Business (absher.sa)
- [ ] General Manager Iqama — valid, not expired

> See: `docs/en/corporate-banking.md` for full bank selection and document requirements.

### Checklist

- [ ] Bank selected and appointment scheduled at branch handling foreign-entity onboarding
- [ ] Complete document package prepared (see `docs/en/corporate-banking.md`)
- [ ] KYC review completed by bank
- [ ] **Corporate bank account active**
- [ ] WPS (Mudad) integration set up if employees will be paid salaries

---

## Common Mistakes Summary

| Stage | Common Mistake |
|-------|---------------|
| MISA eligibility | Applying without an established foreign company (minimum 1 year) |
| MISA fee | Assuming the fee is zero or a fixed amount — it is determined after approval |
| Electronic lease | Using a paper tenancy contract instead of an Ejari-registered electronic lease |
| Branch CR | Attempting to obtain a separate branch CR — branch CRs were abolished in April 2025 |
| Balady license | Starting operations at premises before the municipality license is issued |
| GOSI/Qiwa | Hiring employees before completing GOSI and Qiwa registration |
| Iqama deadline | Missing the 90-day Iqama issuance deadline for expatriate employees |
| Bank prerequisites | Visiting the bank before the CR, IRC, National Address, and GM Iqama are all in place |
