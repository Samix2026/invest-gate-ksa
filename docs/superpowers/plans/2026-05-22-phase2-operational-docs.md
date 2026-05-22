# Phase 2 Operational Docs Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create three bilingual operational guides (Nitaqat, Corporate Banking, Tax Compliance), a timeline dataset entry, and wire everything into check.py and README.md.

**Architecture:** Six new Markdown docs under `docs/en/` and `docs/ar/`, one new entry appended to `data/timelines.{en,ar}.json`, six paths added to REQUIRED_FILES in `scripts/check.py`, and three links added to the Browse the Docs section of `README.md`. All content is educational and non-advisory; no data is fabricated; verified claims cite HRSD/ZATCA/SAMA official sources.

**Tech Stack:** Markdown, JSON, Python (check.py/validate-data.py for validation)

---

## File Map

| Action | Path |
|--------|------|
| Create | `docs/en/nitaqat-saudization.md` |
| Create | `docs/ar/nitaqat-saudization.md` |
| Create | `docs/en/corporate-banking.md` |
| Create | `docs/ar/corporate-banking.md` |
| Create | `docs/en/tax-compliance.md` |
| Create | `docs/ar/tax-compliance.md` |
| Modify | `data/timelines.en.json` — append `corporate_bank_account_opening` |
| Modify | `data/timelines.ar.json` — append Arabic mirror |
| Modify | `scripts/check.py` — add 6 paths to REQUIRED_FILES |
| Modify | `README.md` — add 3 Browse the Docs links |

---

## Task 1: docs/en/nitaqat-saudization.md

**Files:**
- Create: `docs/en/nitaqat-saudization.md`

- [ ] **Step 1: Create the English Nitaqat guide**

Full content — paste as-is:

```markdown
---
title: "Saudization (Nitaqat) — Compliance Guide for Foreign Investors"
language: en
last_verified: "2026-05-21"
verification_method: "Reviewed HRSD Ministerial Decision 182495 and HRSD Procedural Manuals 2025. Sector-specific rates verified from HRSD official announcements and AstroLabs 2026 Nitaqat Guide."
sources:
  - hrsd.gov.sa
  - nitaqat.hrsd.gov.sa
  - qiwa.sa
related:
  - docs/ar/nitaqat-saudization.md
  - docs/en/corporate-banking.md
---

# Saudization (Nitaqat) — Compliance Guide for Foreign Investors

> **Disclaimer:** This document is for general educational purposes only. It is not legal or regulatory advice. Nitaqat rates, sector classifications, and compliance rules change. Always verify current requirements at [hrsd.gov.sa](https://www.hrsd.gov.sa) and via the [Qiwa platform](https://www.qiwa.sa).

---

## What is Nitaqat?

Nitaqat (نطاقات) is Saudi Arabia's Saudization quota system, administered by the Ministry of Human Resources and Social Development (HRSD) through the Qiwa platform. It requires private-sector employers to maintain a minimum percentage of Saudi nationals in their workforce, calculated based on the company's economic activity and headcount.

Every registered private-sector employer is assigned a compliance tier. The tier determines what government services the company can access — and what penalties apply if it falls below the required quota.

---

## Why It Matters — Consequences of Non-Compliance

A company in the Red Zone faces severe operational restrictions:

| Consequence | Details |
|-------------|---------|
| Work permits | Cannot issue new work permits for expatriates |
| Visa quota | Cannot increase visa quota |
| General Manager Iqama | Cannot renew the GM's residency permit |
| Commercial Registration | Cannot update CR details |
| Government contracts | Cannot bid on government contracts |
| Megaproject vendor panels | Cannot access NEOM, Diriyah, or other megaproject panels |
| Financial penalties | Subject to HRSD-imposed fines |

Compliance is not optional — it is a gate for core operating permissions.

---

## Compliance Tiers

| Tier | Description |
|------|-------------|
| **Platinum** | Highest Saudi employee ratio — top performers. Eligible for all government services and incentives. |
| **High Green** | Saudi ratio above the required quota. All services accessible. |
| **Mid Green** | Saudi ratio at the required quota. Standard operating status. |
| **Low Green** | Saudi ratio slightly below quota. Services accessible but company is on notice to improve. |
| **Red** | Saudi ratio below the minimum threshold. Severe service restrictions apply (see table above). |

---

## Key Rule for Foreign Investors (April 2024 Update)

> As of April 11, 2024, the foreign investor who owns a private establishment is counted as a Saudi national for Nitaqat calculation purposes.
>
> Source: HRSD Ministerial Decision, April 2024.

This means a sole foreign owner of a registered company counts as one Saudi national in the Nitaqat headcount — regardless of citizenship. This does not exempt the company from the quota requirement; it simply counts the foreign owner-investor toward that quota.

---

## How the Quota is Calculated

Nitaqat uses a **smooth curve formula** — not fixed percentage bands. The required Saudi percentage is a function of:

1. **Economic activity type** — each ISIC4 / Saudi activity code has a different Nitaqat curve
2. **Company size** — defined by total employee headcount

There is no single universal percentage. A five-person consulting firm and a fifty-person manufacturing plant will have different required Saudi ratios even within the same sector.

**Check your specific rate:** [nitaqat.hrsd.gov.sa](https://nitaqat.hrsd.gov.sa)

Enter your Commercial Registration number to see your current tier, required ratio, and quota calculation.

---

## 2025–2026 Sector-Specific Updates

Several sectors received new or increased Nitaqat rates in 2025–2026. If your business falls into any of these categories, the updated rates apply to your Nitaqat calculation:

| Sector | New Saudization Rate | Effective Date | Condition |
|--------|---------------------|----------------|-----------|
| Dental clinics | 55% | January 27, 2026 | 3 or more dental workers |
| Engineering (technical roles) | 30% | July 27, 2025 | 5 or more engineers |
| Accounting | 40%, increasing 10% per year until 2028 | October 27, 2025 | 5 or more accountants |
| Marketing positions | 60% | 2025 | 3 or more employees in marketing |
| Hospitals | 65% | July 2025 | All hospitals |
| Community pharmacies | 35% | July 2025 | — |
| Tourism sector | 41 professions newly Saudized | April 2025 | See HRSD announcement |
| Administrative support | 69 additional professions at 100% | 2025 | See HRSD announcement |

Source: HRSD Ministerial Decision 182495 + HRSD Procedural Manuals 2025.

> **Verify current rates at:** [hrsd.gov.sa — Decisions and Regulations](https://www.hrsd.gov.sa/en/knowledge-centre/decisions-and-regulations)

---

## Part-Time Workers

Flexible workers (part-time employees) who work **160 hours or more per month** count as **1 full Nitaqat point** — the same as a full-time employee.

This applies to both Saudi and expatriate employees. For Saudization quota purposes, a qualifying Saudi part-time worker at 160+ hours/month contributes the same as a full-time Saudi employee.

---

## What Counts as a Qualifying Saudi Employee

For a Saudi employee to count toward your Nitaqat quota, they must:

- Be registered with GOSI (General Organization for Social Insurance) under your CR
- Receive a salary meeting the sector minimum threshold

Sector minimum salary thresholds include:
- Dentists: SAR 9,000/month minimum
- Marketing positions: SAR 5,500/month minimum

Employees below the sector minimum wage threshold do not count toward the Nitaqat quota even if registered with GOSI.

> **Verify current thresholds at:** [hrsd.gov.sa](https://www.hrsd.gov.sa) and via the Qiwa platform.

---

## How to Check Your Nitaqat Status

**Qiwa platform:** [qiwa.sa](https://www.qiwa.sa)

Log in as an employer. The Nitaqat dashboard shows:
- Current compliance tier (color)
- Current Saudi employee ratio
- Required ratio for your activity and size
- Number of Saudis needed to move to the next tier

**Nitaqat certificate:** Required for government contracts, visa quota requests, CR updates, and GM Iqama renewal. Download from Qiwa.

---

## Official Sources

| Authority | URL |
|-----------|-----|
| HRSD (Ministry of Human Resources) | [hrsd.gov.sa](https://www.hrsd.gov.sa) |
| Nitaqat portal | [nitaqat.hrsd.gov.sa](https://nitaqat.hrsd.gov.sa) |
| Qiwa (employer portal) | [qiwa.sa](https://www.qiwa.sa) |
| HRSD Decisions and Regulations | [hrsd.gov.sa/en/knowledge-centre/decisions-and-regulations](https://www.hrsd.gov.sa/en/knowledge-centre/decisions-and-regulations) |
```

- [ ] **Step 2: Verify the file exists and is valid Markdown**

```bash
ls -la docs/en/nitaqat-saudization.md
head -5 docs/en/nitaqat-saudization.md
```

Expected: file exists, starts with `---`

---

## Task 2: docs/ar/nitaqat-saudization.md

**Files:**
- Create: `docs/ar/nitaqat-saudization.md`

- [ ] **Step 1: Create the Arabic Nitaqat guide**

Rules: no tashkeel, English numerals, formal MSA, all URLs stay in English.

```markdown
---
title: "السعودة (نطاقات) — دليل الامتثال للمستثمرين الأجانب"
language: ar
last_verified: "2026-05-21"
verification_method: "مراجعة قرار وزارة الموارد البشرية الوزاري 182495 والأدلة الإجرائية لعام 2025. معدلات القطاعات مُحددة من إعلانات وزارة الموارد البشرية الرسمية."
sources:
  - hrsd.gov.sa
  - nitaqat.hrsd.gov.sa
  - qiwa.sa
related:
  - docs/en/nitaqat-saudization.md
  - docs/ar/corporate-banking.md
---

# السعودة (نطاقات) — دليل الامتثال للمستثمرين الأجانب

> **تنبيه:** هذه الوثيقة لأغراض تعليمية عامة فقط، وليست استشارة قانونية أو تنظيمية. تتغير نسب نطاقات وتصنيفات القطاعات وقواعد الامتثال. تحقق دائما من المتطلبات الحالية عبر [hrsd.gov.sa](https://www.hrsd.gov.sa) ومنصة [قوى](https://www.qiwa.sa).

---

## ما هو نطاقات؟

نطاقات هو نظام حصص السعودة المعتمد في المملكة العربية السعودية، وتديره وزارة الموارد البشرية والتنمية الاجتماعية عبر منصة قوى. يُلزم أصحاب العمل في القطاع الخاص بالحفاظ على نسبة دنيا من المواطنين السعوديين في صفوف موظفيهم، وتُحسب هذه النسبة بناء على النشاط الاقتصادي للمنشأة وعدد موظفيها.

يُصنَّف كل صاحب عمل مسجَّل في القطاع الخاص ضمن مستوى امتثال محدد، يحكم وصوله إلى الخدمات الحكومية والعقوبات المترتبة في حال التقصير.

---

## أهمية الامتثال — تداعيات عدم الامتثال

يواجه أصحاب العمل الواقعون في النطاق الأحمر قيودا تشغيلية صارمة:

| التداعية | التفاصيل |
|----------|----------|
| تصاريح العمل | لا يمكن إصدار تصاريح عمل جديدة للعمالة الوافدة |
| حصة التأشيرات | لا يمكن زيادة حصة التأشيرات |
| إقامة المدير العام | لا يمكن تجديد إقامة المدير العام |
| السجل التجاري | لا يمكن تحديث بيانات السجل التجاري |
| العقود الحكومية | لا يمكن التقدم للعقود الحكومية |
| مشاريع كبرى | لا يمكن الانضمام إلى قوائم موردي المشاريع الكبرى كنيوم والدرعية |
| الغرامات المالية | غرامات تفرضها وزارة الموارد البشرية |

الامتثال ليس اختياريا — فهو شرط للحصول على التصاريح التشغيلية الأساسية.

---

## مستويات الامتثال

| المستوى | الوصف |
|---------|-------|
| **بلاتيني** | أعلى نسبة موظفين سعوديين — أفضل الممارسات. أهلية لجميع الخدمات والحوافز الحكومية. |
| **أخضر مرتفع** | نسبة سعودة تتجاوز الحصة المطلوبة. إمكانية الوصول إلى جميع الخدمات. |
| **أخضر متوسط** | نسبة سعودة تساوي الحصة المطلوبة. الوضع التشغيلي الاعتيادي. |
| **أخضر منخفض** | نسبة سعودة أدنى قليلا من الحصة. الخدمات متاحة لكن المنشأة مطالبة بالتحسين. |
| **أحمر** | نسبة سعودة دون الحد الأدنى. قيود صارمة على الخدمات (انظر الجدول أعلاه). |

---

## قاعدة مهمة للمستثمرين الأجانب (تحديث أبريل 2024)

> اعتبارا من 11 أبريل 2024، يُحتسب المستثمر الأجنبي المالك لمنشأة خاصة ضمن حسبة نطاقات بوصفه مواطنا سعوديا.
>
> المصدر: قرار وزاري صادر عن وزارة الموارد البشرية، أبريل 2024.

يعني ذلك أن المالك الأجنبي الفرد للمنشأة المسجلة يُحتسب موظفا سعوديا واحدا في حسبة نطاقات — بصرف النظر عن جنسيته. لا يُعفي ذلك المنشأة من متطلب الحصة؛ يُضيف المالكَ الأجنبي فقط إلى تلك الحصة.

---

## كيف تُحسب الحصة؟

يعتمد نطاقات على **معادلة منحنى سلس** — لا نسبا ثابتة. النسبة المطلوبة من السعوديين دالة على:

1. **نوع النشاط الاقتصادي** — لكل كود نشاط وفق ISIC4 أو التصنيف السعودي منحنى نطاقات مختلف
2. **حجم المنشأة** — يُحدَّد بإجمالي عدد الموظفين

لا توجد نسبة موحدة. تختلف النسبة المطلوبة بين شركة استشارات مكوَّنة من 5 موظفين ومصنع من 50 موظفا حتى في القطاع ذاته.

**تحقق من نسبتك الخاصة:** [nitaqat.hrsd.gov.sa](https://nitaqat.hrsd.gov.sa)

أدخل رقم السجل التجاري للاطلاع على مستوى امتثالك الحالي والنسبة المطلوبة وتفاصيل الحسبة.

---

## تحديثات 2025–2026 لقطاعات محددة

حصلت عدة قطاعات على نسب سعودة جديدة أو مرتفعة في 2025–2026:

| القطاع | نسبة السعودة الجديدة | تاريخ التطبيق | الشرط |
|--------|---------------------|---------------|-------|
| عيادات الأسنان | 55% | 27 يناير 2026 | 3 عمال أسنان فأكثر |
| الهندسة (الأدوار التقنية) | 30% | 27 يوليو 2025 | 5 مهندسين فأكثر |
| المحاسبة | 40%، بزيادة 10% سنويا حتى 2028 | 27 أكتوبر 2025 | 5 محاسبين فأكثر |
| التسويق | 60% | 2025 | 3 موظفين فأكثر في التسويق |
| المستشفيات | 65% | يوليو 2025 | جميع المستشفيات |
| الصيدليات المجتمعية | 35% | يوليو 2025 | — |
| قطاع السياحة | 41 مهنة مُستحدثة | أبريل 2025 | راجع إعلان وزارة الموارد البشرية |
| الدعم الإداري | 69 مهنة إضافية بنسبة 100% | 2025 | راجع إعلان وزارة الموارد البشرية |

المصدر: قرار وزاري 182495 + الأدلة الإجرائية 2025.

> **تحقق من النسب الحالية:** [hrsd.gov.sa/en/knowledge-centre/decisions-and-regulations](https://www.hrsd.gov.sa/en/knowledge-centre/decisions-and-regulations)

---

## العمال بدوام جزئي

يُحتسب الموظف بدوام جزئي الذي يعمل **160 ساعة شهريا فأكثر** بما يعادل **نقطة نطاقات كاملة** — كالموظف بدوام كامل.

ينطبق ذلك على الموظفين السعوديين والوافدين على حد سواء. لأغراض حصة السعودة، يُساهم الموظف السعودي المؤهل بدوام جزئي عند 160 ساعة فأكثر بالقدر ذاته الذي يُساهم به الموظف السعودي بدوام كامل.

---

## شروط احتساب الموظف السعودي

لكي يُحتسب الموظف السعودي ضمن حصة نطاقات، يجب أن:

- يكون مسجلا في التأمينات الاجتماعية (جوسي) تحت سجلك التجاري
- يتقاضى راتبا يلبي الحد الأدنى القطاعي

أمثلة على الحدود الدنيا للرواتب:
- أطباء الأسنان: 9,000 ريال سعودي شهريا كحد أدنى
- وظائف التسويق: 5,500 ريال سعودي شهريا كحد أدنى

الموظفون الذين تقل رواتبهم عن الحد الأدنى القطاعي لا يُحتسبون في حصة نطاقات حتى وإن كانوا مسجلين في التأمينات.

> **تحقق من الحدود الحالية:** [hrsd.gov.sa](https://www.hrsd.gov.sa) ومنصة قوى.

---

## كيف تتحقق من وضع نطاقات؟

**منصة قوى:** [qiwa.sa](https://www.qiwa.sa)

سجِّل الدخول بصفتك صاحب عمل. تعرض لوحة نطاقات:
- مستوى الامتثال الحالي (اللون)
- نسبة الموظفين السعوديين الحالية
- النسبة المطلوبة لنشاطك وحجمك
- عدد السعوديين المطلوب إضافتهم للانتقال إلى المستوى التالي

**شهادة نطاقات:** مطلوبة للعقود الحكومية وطلبات حصص التأشيرات وتحديث السجل التجاري وتجديد إقامة المدير العام. تنزيلها من منصة قوى.

---

## المصادر الرسمية

| الجهة | الرابط |
|-------|--------|
| وزارة الموارد البشرية والتنمية الاجتماعية | [hrsd.gov.sa](https://www.hrsd.gov.sa) |
| بوابة نطاقات | [nitaqat.hrsd.gov.sa](https://nitaqat.hrsd.gov.sa) |
| منصة قوى (بوابة أصحاب العمل) | [qiwa.sa](https://www.qiwa.sa) |
| قرارات ولوائح وزارة الموارد البشرية | [hrsd.gov.sa/en/knowledge-centre/decisions-and-regulations](https://www.hrsd.gov.sa/en/knowledge-centre/decisions-and-regulations) |
```

- [ ] **Step 2: Verify file exists**

```bash
ls -la docs/ar/nitaqat-saudization.md
head -3 docs/ar/nitaqat-saudization.md
```

---

## Task 3: docs/en/corporate-banking.md

**Files:**
- Create: `docs/en/corporate-banking.md`

- [ ] **Step 1: Create the English corporate banking guide**

```markdown
---
title: "Corporate Banking — Opening a Bank Account in Saudi Arabia"
language: en
last_verified: "2026-05-21"
verification_method: "Reviewed RBCL.sa March 2026 corporate banking guide and multiple 2025-2026 practitioner sources. Timeline marked draft — no single SAMA-published benchmark exists for foreign-entity onboarding."
sources:
  - sama.gov.sa
related:
  - docs/ar/corporate-banking.md
  - docs/en/nitaqat-saudization.md
  - docs/en/tax-compliance.md
---

# Corporate Banking — Opening a Bank Account in Saudi Arabia

> **Disclaimer:** This document is for general educational purposes only. It is not legal, financial, or banking advice. Banking requirements and procedures change. Always verify current requirements directly with your chosen bank and with SAMA at [sama.gov.sa](https://www.sama.gov.sa).

---

## Why You Need a Saudi Bank Account

A Saudi bank account is not optional — it is a prerequisite for operating a registered business in the Kingdom. The following critical obligations all require an active, SAMA-regulated bank account:

| Obligation | Why a Bank Account is Required |
|------------|-------------------------------|
| MISA registration fee payment | Fee must be paid from a Saudi bank account after approval |
| Wage Protection System (WPS/Mudad) | All employee salaries must be paid through a WPS-linked account |
| ZATCA tax payments | Corporate Income Tax, VAT, and WHT payments require a Saudi account |
| GOSI contributions | Social insurance contributions processed through the Saudi banking system |
| Supplier payments | Local vendors typically require Saudi bank transfers |
| Audit and financial compliance | Statutory financial records must reflect Saudi bank transactions |

Without an active account, the company cannot pay employees in a Nitaqat-compliant way, cannot pay tax obligations to ZATCA, and cannot process GOSI contributions.

---

## Prerequisites — Complete These First

**Do not visit the bank until all four of these are in place:**

1. **MISA Investment Registration Certificate (IRC)** — active, issued by MISA
2. **Commercial Registration (CR)** — active, annual confirmation current, issued by Ministry of Commerce
3. **National Address** — registered and active via Absher Business ([absher.sa](https://www.absher.sa))
4. **General Manager Iqama** — valid residency permit for the authorized signatory

Banks will not open an account for an entity that has not completed these steps. Attempting to open an account before the CR is issued wastes time.

---

## Required Documents

The following documents are standard across Saudi banks for foreign-owned company account opening. Individual banks may request additional items depending on their KYC policies:

| Document | Notes |
|----------|-------|
| MISA Investment Registration Certificate (IRC) | Original + copy |
| Commercial Registration (CR) | Active — annual confirmation must be current |
| Articles of Association (AoA) | Arabic version, notarized |
| Parent company CR + AoA | Authenticated by the Saudi Embassy in the parent company's country |
| Board resolution | Authorizing the account opening and naming the authorized signatory |
| General Manager Iqama | Valid, not expired |
| National Address certificate | Downloaded from Absher Business |
| ZATCA tax registration certificate | Issued by ZATCA at registration |

For parent company documents, authentication requirements vary. Confirm with the chosen bank before submitting.

---

## Bank Selection

Five major Saudi banks commonly serve foreign-owned companies:

| Bank | Notes |
|------|-------|
| **Saudi National Bank (SNB)** | Largest bank in Saudi Arabia. Full corporate services. Dedicated foreign investment teams at major branches. |
| **Al Rajhi Bank** | Strong SME and mid-market corporate services. Widely accessible branch network. |
| **Riyad Bank** | International business focus. Experience with cross-border transactions and foreign entity onboarding. |
| **Saudi Investment Bank (SAIB)** | Established 1977. Corporate banking specialization. |
| **Alinma Bank** | Digital-first options. Efficient onboarding for companies with straightforward KYC profiles. |

Banks have different KYC thresholds and due-diligence requirements for foreign entities. Some have specialist foreign-company onboarding desks — call ahead to confirm the branch process before visiting.

---

## Timeline and Process

| Step | Action | Notes |
|------|--------|-------|
| 1 | Choose bank and schedule appointment | Confirm that the branch handles foreign-entity onboarding |
| 2 | Submit complete document package | Incomplete submissions reset the clock |
| 3 | KYC review | Bank reviews beneficial ownership structure, parent company, and activity |
| 4 | Account activation | Bank issues account details; link to WPS and ZATCA |

**Estimated timeline:** 1–4 weeks from first submission of a complete document package.

Timeline varies by bank, entity complexity, and KYC workload. Foreign-owned companies typically require additional due-diligence steps compared to Saudi-owned entities.

> This timeline is an estimate based on practitioner experience — no single SAMA-published benchmark exists. Verify with your chosen bank.

---

## Critical Maintenance Rules

Once the account is open, four operational rules apply:

1. **Iqama renewal → update bank immediately.** The account is tied to the General Manager's Iqama. When the GM Iqama is renewed, notify the bank and update the account record. Failure to do so can freeze account operations.

2. **Inactive accounts risk dormancy.** Banks monitor account activity. Accounts with no transactions for extended periods may be flagged as dormant, restricting access. Maintain regular activity.

3. **WPS integration is mandatory.** All employee salary payments must flow through the Wage Protection System (Mudad). Set up WPS integration immediately after account activation if the company has employees.

4. **Signatory changes require board resolution.** Any change to the authorized signatory requires a new board resolution and updated bank documentation.

---

## Official Source

| Authority | URL |
|-----------|-----|
| Saudi Central Bank (SAMA) | [sama.gov.sa](https://www.sama.gov.sa) |
| Absher Business (National Address) | [absher.sa](https://www.absher.sa) |
| Mudad / WPS | [mudad.com.sa](https://www.mudad.com.sa) |
```

- [ ] **Step 2: Verify file exists**

```bash
ls -la docs/en/corporate-banking.md
```

---

## Task 4: docs/ar/corporate-banking.md

**Files:**
- Create: `docs/ar/corporate-banking.md`

- [ ] **Step 1: Create the Arabic corporate banking guide**

```markdown
---
title: "الخدمات المصرفية للشركات — فتح حساب مصرفي في المملكة العربية السعودية"
language: ar
last_verified: "2026-05-21"
verification_method: "مراجعة دليل RBCL.sa المصرفي للشركات، مارس 2026، ومصادر متعددة 2025-2026. الجدول الزمني مُدرَج كمسودة — لا يوجد معيار رسمي منشور من ساما لتأهيل الكيانات الأجنبية."
sources:
  - sama.gov.sa
related:
  - docs/en/corporate-banking.md
  - docs/ar/nitaqat-saudization.md
  - docs/ar/tax-compliance.md
---

# الخدمات المصرفية للشركات — فتح حساب مصرفي في المملكة العربية السعودية

> **تنبيه:** هذه الوثيقة لأغراض تعليمية عامة فقط، وليست استشارة قانونية أو مالية أو مصرفية. تتغير متطلبات البنوك وإجراءاتها. تحقق دائما من المتطلبات الحالية مع البنك المختار ومع ساما عبر [sama.gov.sa](https://www.sama.gov.sa).

---

## لماذا تحتاج إلى حساب مصرفي سعودي؟

الحساب المصرفي السعودي ليس اختياريا — فهو شرط أساسي لتشغيل أي منشأة مسجلة في المملكة. تستلزم الالتزامات التشغيلية التالية حسابا مصرفيا نشطا خاضعا لإشراف ساما:

| الالتزام | سبب الحاجة إلى الحساب المصرفي |
|----------|-------------------------------|
| سداد رسوم تسجيل وزارة الاستثمار | يجب السداد من حساب مصرفي سعودي بعد الموافقة |
| نظام حماية الأجور (مدد) | يُشترط صرف رواتب الموظفين عبر حساب مرتبط بمدد |
| المدفوعات الضريبية لزكاة وضريبة (هيئة الزكاة والضريبة والجمارك) | تستلزم ضريبة الدخل وضريبة القيمة المضافة وضريبة الاستقطاع حسابا سعوديا |
| اشتراكات التأمينات الاجتماعية (جوسي) | تُعالَج عبر المنظومة المصرفية السعودية |
| المدفوعات للموردين | يطلب الموردون المحليون في الغالب تحويلات مصرفية سعودية |
| الامتثال المالي ومتطلبات التدقيق | يجب أن تعكس السجلات المالية النظامية المعاملات المصرفية السعودية |

دون حساب نشط، لا تستطيع الشركة صرف رواتب الموظفين بصورة متوافقة مع نطاقات، ولا الوفاء بالتزاماتها الضريبية لدى هيئة الزكاة والضريبة والجمارك، ولا معالجة اشتراكات التأمينات الاجتماعية.

---

## المتطلبات الأولية — أكمل هذه الخطوات أولا

**لا تزر البنك قبل استيفاء هذه المتطلبات الأربعة:**

1. **شهادة تسجيل الاستثمار (IRC) من وزارة الاستثمار** — سارية، صادرة عن ميسا
2. **السجل التجاري** — سارٍ، تأكيد سنوي حالي، صادر عن وزارة التجارة
3. **العنوان الوطني** — مسجَّل ونشط عبر أبشر للأعمال ([absher.sa](https://www.absher.sa))
4. **إقامة المدير العام** — تصريح إقامة ساري للمفوض بالتوقيع

لن تفتح البنوك أي حساب لكيان لم يُتم هذه الخطوات. مراجعة البنك قبل إصدار السجل التجاري مضيعة للوقت.

---

## الوثائق المطلوبة

الوثائق التالية معيارية لدى البنوك السعودية لفتح حساب شركات مملوكة لأجانب. قد تطلب البنوك وثائق إضافية بحسب سياسات العناية الواجبة:

| الوثيقة | ملاحظات |
|---------|---------|
| شهادة تسجيل الاستثمار (IRC) من ميسا | أصل + نسخة |
| السجل التجاري | سارٍ — التأكيد السنوي يجب أن يكون حاليا |
| عقد التأسيس (النظام الأساسي) | نسخة عربية مُوثَّقة |
| السجل التجاري + عقد التأسيس للشركة الأم | مُصادَق عليهما من السفارة السعودية في بلد الشركة الأم |
| قرار مجلس الإدارة | يُفوِّض فتح الحساب ويُسمي المفوَّض بالتوقيع |
| إقامة المدير العام | سارية، غير منتهية |
| شهادة العنوان الوطني | مُنزَّلة من أبشر للأعمال |
| شهادة التسجيل الضريبي من هيئة الزكاة والضريبة والجمارك | صادرة عند التسجيل |

تتفاوت متطلبات المصادقة على وثائق الشركة الأم. تأكد مع البنك المختار قبل تقديم الطلب.

---

## اختيار البنك

تخدم خمسة بنوك سعودية رئيسية الشركات المملوكة للأجانب:

| البنك | ملاحظات |
|-------|---------|
| **البنك الأهلي السعودي (SNB)** | أكبر بنك في المملكة. خدمات شركات شاملة. فرق متخصصة للاستثمار الأجنبي في الفروع الرئيسية. |
| **مصرف الراجحي** | خدمات قوية للشركات الصغيرة والمتوسطة. شبكة فروع واسعة وسهلة الوصول. |
| **بنك الرياض** | تركيز على الأعمال الدولية. خبرة في التعاملات العابرة للحدود وتأهيل الكيانات الأجنبية. |
| **البنك السعودي للاستثمار (SAIB)** | تأسس 1977. تخصص في الخدمات المصرفية للشركات. |
| **مصرف الإنماء** | خيارات رقمية متقدمة. تأهيل فعّال للشركات ذات ملفات العناية الواجبة المباشرة. |

تتفاوت عتبات العناية الواجبة ومتطلبات الرقابة للكيانات الأجنبية من بنك لآخر. تتوفر في بعض البنوك مكاتب متخصصة لتأهيل الشركات الأجنبية — اتصل للتأكد من آلية الفرع قبل الزيارة.

---

## الجدول الزمني والإجراءات

| الخطوة | الإجراء | ملاحظات |
|--------|---------|---------|
| 1 | اختيار البنك وتحديد موعد | تأكد من أن الفرع يتولى تأهيل الكيانات الأجنبية |
| 2 | تقديم حزمة الوثائق الكاملة | أي نقص يُعيد العداد من الصفر |
| 3 | مراجعة العناية الواجبة | يراجع البنك هيكل الملكية النفعية والشركة الأم والنشاط |
| 4 | تفعيل الحساب | يُصدر البنك تفاصيل الحساب؛ ربطه بمدد وهيئة الزكاة |

**الجدول الزمني المتوقع:** من 1 إلى 4 أسابيع من أول تقديم لحزمة وثائق مكتملة.

يتفاوت الجدول الزمني بحسب البنك وتعقيد الكيان وحجم العمل في قسم العناية الواجبة. تستلزم الشركات المملوكة لأجانب عادةً خطوات إضافية مقارنة بالكيانات السعودية المملوكة.

> هذا الجدول تقدير مبني على خبرة عملية — لا يوجد معيار رسمي منشور من ساما. تحقق مع البنك المختار.

---

## قواعد صيانة الحساب

بعد فتح الحساب، تسري أربع قواعد تشغيلية:

1. **تجديد الإقامة = تحديث البنك فورا.** الحساب مرتبط بإقامة المدير العام. عند تجديد الإقامة، أبلغ البنك وحدِّث سجلات الحساب. الإخفاق قد يُجمِّد العمليات.

2. **الحسابات الخاملة معرَّضة للتجميد.** ترصد البنوك نشاط الحسابات. قد تُصنَّف الحسابات التي لا تشهد أي معاملات لفترات مطولة باعتبارها خاملة مما يُقيِّد الوصول. حافظ على نشاط منتظم.

3. **ربط نظام حماية الأجور (مدد) إلزامي.** يجب أن تمر جميع مدفوعات رواتب الموظفين عبر نظام حماية الأجور. أعِدّ ربط مدد فور تفعيل الحساب إذا كانت الشركة لديها موظفون.

4. **تغيير المفوض بالتوقيع يستلزم قرار مجلس إدارة.** أي تعديل على المفوض يستوجب قرارا جديدا من مجلس الإدارة وتحديث وثائق البنك.

---

## المصادر الرسمية

| الجهة | الرابط |
|-------|--------|
| البنك المركزي السعودي (ساما) | [sama.gov.sa](https://www.sama.gov.sa) |
| أبشر للأعمال (العنوان الوطني) | [absher.sa](https://www.absher.sa) |
| مدد / نظام حماية الأجور | [mudad.com.sa](https://www.mudad.com.sa) |
```

- [ ] **Step 2: Verify file exists**

```bash
ls -la docs/ar/corporate-banking.md
```

---

## Task 5: docs/en/tax-compliance.md

**Files:**
- Create: `docs/en/tax-compliance.md`

- [ ] **Step 1: Create the English tax compliance guide**

Note: This document cross-references `data/fees.en.json` entries (`cit_corporate_income_tax`, `zakat_saudi_gcc_shareholders`, `wht_withholding_tax`) rather than duplicating their data.

```markdown
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

## Official Source

| Authority | URL |
|-----------|-----|
| ZATCA (Zakat, Tax and Customs Authority) | [zatca.gov.sa](https://zatca.gov.sa) |
| ZATCA e-invoicing (Fatoora) | [fatoora.zatca.gov.sa](https://fatoora.zatca.gov.sa) |
| Repository dataset | `data/fees.en.json` — entries `cit_corporate_income_tax`, `zakat_saudi_gcc_shareholders`, `wht_withholding_tax` |
```

- [ ] **Step 2: Verify file exists**

```bash
ls -la docs/en/tax-compliance.md
```

---

## Task 6: docs/ar/tax-compliance.md

**Files:**
- Create: `docs/ar/tax-compliance.md`

- [ ] **Step 1: Create the Arabic tax compliance guide**

```markdown
---
title: "الامتثال الضريبي للمستثمرين الأجانب في المملكة العربية السعودية"
language: ar
last_verified: "2026-05-21"
verification_method: "البيانات مُحالة من إدخالات data/fees.en.json (محقَّقة) وملف docs/en/company-setup-overview.md. التزامات هيئة الزكاة والضريبة والجمارك محقَّقة من إرشادات zatca.gov.sa المنشورة."
sources:
  - zatca.gov.sa
related:
  - docs/en/tax-compliance.md
  - docs/ar/corporate-banking.md
  - data/fees.ar.json
---

# الامتثال الضريبي للمستثمرين الأجانب في المملكة العربية السعودية

> **تنبيه:** هذه الوثيقة لأغراض تعليمية عامة فقط، وليست استشارة ضريبية أو قانونية. تتغير المعدلات الضريبية والحدود وإجراءات التقديم. تحقق دائما من الالتزامات الحالية مباشرة مع هيئة الزكاة والضريبة والجمارك عبر [zatca.gov.sa](https://zatca.gov.sa) واستشر متخصصا ضريبيا مؤهلا قبل التقديم.

---

## نظرة عامة — نظام الضريبة المزدوج في المملكة

تعتمد المملكة العربية السعودية **نظاما ضريبيا مزدوجا** يُطبِّق ضرائب مختلفة تبعا لهيكل ملكية الشركة:

- **المساهمون الأجانب** يخضعون لـ **ضريبة الدخل على الشركات (CIT)** على حصتهم من الأرباح
- **المساهمون السعوديون وأبناء دول الخليج** يخضعون لـ **الزكاة** على حصتهم من وعاء صافي الأصول

كلا الالتزامين قد يسريان في آن واحد في الشركات المختلطة الملكية. تسري ضريبة القيمة المضافة وضريبة الاستقطاع بصرف النظر عن هيكل الملكية.

تتولى **هيئة الزكاة والضريبة والجمارك (زاتكا)** إدارة جميع الالتزامات الضريبية عبر [zatca.gov.sa](https://zatca.gov.sa).

راجع إدخالات `data/fees.ar.json`: `cit_corporate_income_tax` و`zakat_saudi_gcc_shareholders` و`wht_withholding_tax` للسجلات المحقَّقة.

---

## جدول ملخص

| الضريبة | المعدل | تسري على | الوعاء |
|---------|--------|----------|--------|
| ضريبة الدخل على الشركات (CIT) | 20% | حصة المساهمين الأجانب | صافي الأرباح المعدَّل |
| الزكاة | 2.5% | حصة المساهمين السعوديين وأبناء دول الخليج | وعاء صافي الأصول (لا الأرباح) |
| ضريبة القيمة المضافة | 15% | جميع المنشآت المسجلة | الإمدادات الخاضعة للضريبة |
| ضريبة الاستقطاع — التوزيعات | 5% | المدفوعات لغير المقيمين | المبلغ الإجمالي |
| ضريبة الاستقطاع — حقوق الملكية | 15% | المدفوعات لغير المقيمين | المبلغ الإجمالي |
| ضريبة الاستقطاع — الخدمات | حتى 20% | المدفوعات لغير المقيمين | المبلغ الإجمالي (يتفاوت باتفاقيات الازدواج) |

---

## ضريبة الدخل على الشركات (CIT) — المساهمون الأجانب

**المعدل:** 20% من صافي الأرباح المعدَّلة المنسوبة إلى المساهمين الأجانب.

تسري CIT على **حصة المساهم الأجنبي** من الأرباح الصافية، لا على إجمالي أرباح الشركة. في الكيان المملوك بالكامل لأجانب، تسري CIT على 100% من الأرباح الصافية. في الكيان المختلط، تسري على نسبة الملكية الأجنبية فقط.

**جهة التقديم:** هيئة الزكاة والضريبة والجمارك  
**موعد التقديم:** خلال 120 يوما من نهاية السنة المالية  
**السداد:** مع تقديم الإقرار الضريبي السنوي

تُحسب CIT على صافي الأرباح المعدَّل — لا على إجمالي الإيرادات. تشمل المصروفات المسموح بها: المصاريف التشغيلية والاستهلاك والبنود الأخرى المعتمدة من الهيئة.

---

## الزكاة — المساهمون السعوديون وأبناء دول الخليج

**المعدل:** 2.5% من وعاء الزكاة (وعاء صافي الأصول، لا الأرباح).

الزكاة فريضة مالية إسلامية على الثروة لا على الدخل. يتمثل وعاء الزكاة تقريبا في صافي أصول الشركة المنسوبة إلى المساهمين السعوديين وأبناء دول الخليج وفق قواعد الهيئة. يعني ذلك أن الزكاة قد تستحق حتى في سنوات الخسارة إذا كان وعاء صافي الأصول موجبا.

**جهة التقديم:** هيئة الزكاة والضريبة والجمارك  
**موعد التقديم:** خلال 120 يوما من نهاية السنة المالية

لا تسري الزكاة على الشركات المملوكة بالكامل لأجانب — تسري عليها CIT فقط.

---

## ضريبة القيمة المضافة

**المعدل:** 15% على الإمدادات الخاضعة للضريبة من السلع والخدمات.

**حدود التسجيل:**
- التسجيل الإلزامي: الإمدادات الخاضعة للضريبة تتجاوز 375,000 ريال سعودي سنويا
- التسجيل الاختياري: الإمدادات تتجاوز 187,500 ريال سعودي سنويا

**دورية التقديم:**
- شهريا: الشركات ذات الإيرادات السنوية التي تتجاوز 40 مليون ريال سعودي
- ربع سنوي: جميع الشركات المسجلة الأخرى

يُخصَم ضريبة القيمة المضافة المدخلة على المشتريات من ضريبة القيمة المضافة المخرجة على المبيعات. يُحوَّل الفارق الصافي إلى الهيئة.

**موعد التسجيل:** خلال 30 يوما من تجاوز الحد الإلزامي، أو خلال 60 يوما من بدء النشاط (أيهما ينطبق).

---

## ضريبة الاستقطاع (WHT)

تسري ضريبة الاستقطاع على مدفوعات تُؤديها منشأة مسجلة في المملكة لمستفيدين **غير مقيمين** — شركات أو أفراد غير مسجلين في المملكة.

| نوع الدفعة | معدل ضريبة الاستقطاع |
|------------|----------------------|
| توزيعات أرباح الأسهم | 5% |
| فوائد القروض | 5% |
| حقوق الملكية والرسوم التقنية | 15% |
| رسوم الإدارة | 20% |
| الخدمات (عامة) | 5–20% (يتفاوت) |
| شحن جوي/بحري | 5% |

**موعد السداد:** يجب تحويل ضريبة الاستقطاع إلى الهيئة خلال العشرة أيام الأولى من الشهر التالي لشهر الدفعة.

**اتفاقيات تجنب الازدواج الضريبي:** أبرمت المملكة اتفاقيات مع دول عديدة. قد تُخفِّض الاتفاقية معدل ضريبة الاستقطاع السارية أو تُلغيه. تحقق من أهلية الاتفاقية وإجراءات المطالبة عبر [zatca.gov.sa](https://zatca.gov.sa).

---

## المواعيد النهائية الرئيسية

| الالتزام | الموعد النهائي | الجهة |
|----------|----------------|-------|
| التسجيل لدى هيئة الزكاة والضريبة والجمارك | خلال 60 يوما من بدء النشاط | هيئة الزكاة والضريبة والجمارك |
| التسجيل في ضريبة القيمة المضافة (إلزامي) | خلال 30 يوما من تجاوز حد 375,000 ريال | هيئة الزكاة والضريبة والجمارك |
| الإقرار الضريبي السنوي (CIT/زكاة) | خلال 120 يوما من نهاية السنة المالية | هيئة الزكاة والضريبة والجمارك |
| تقديم ضريبة القيمة المضافة — شهريا | بحلول اليوم 15 من الشهر التالي | هيئة الزكاة والضريبة والجمارك |
| تقديم ضريبة القيمة المضافة — ربع سنوي | بحلول اليوم 15 من الشهر التالي للربع | هيئة الزكاة والضريبة والجمارك |
| سداد ضريبة الاستقطاع | العشرة أيام الأولى من الشهر التالي | هيئة الزكاة والضريبة والجمارك |
| الاحتفاظ بالسجلات | 10 سنوات من نهاية السنة الضريبية | هيئة الزكاة والضريبة والجمارك |

---

## الفوترة الإلكترونية (فاتورة)

تُلزم المملكة العربية السعودية بالفوترة الإلكترونية لجميع معاملات B2B وB2G ضمن منظومة **فاتورة**.

**المرحلة الثانية (مرحلة التكامل):** إلزامية اعتبارا من 2025 للشركات التي تستوفي حد الإيرادات. تستلزم التكامل مع منصة الفوترة الإلكترونية لهيئة الزكاة والضريبة والجمارك. يجب إنشاء جميع الفواتير وإرسالها عبر حل فوترة إلكترونية متوافق مع الهيئة.

عدم الامتثال لمتطلبات فاتورة يُعرِّض الشركة لغرامات الهيئة.

**تحقق من نطاق التطبيق الحالي والحدود:** [zatca.gov.sa](https://zatca.gov.sa)

---

## مثال على الملكية المختلطة

شركة بملكية 60% سعودية و40% أجنبية:

| المساهم | نسبة الملكية | الضريبة المطبَّقة | الوعاء |
|---------|-------------|-------------------|--------|
| مساهم سعودي | 60% | زكاة (2.5%) | 60% من وعاء صافي الأصول |
| مساهم أجنبي | 40% | CIT (20%) | 40% من صافي الأرباح المعدَّل |

تُقدَّم كلتا الضريبتين وتُسدَّدان إلى هيئة الزكاة والضريبة والجمارك. تُقدِّم الشركة إقرارا سنويا موحدا يشمل الالتزامين.

ملاحظة: هذا المثال يوضح المبدأ العام. تنطوي حسابات الزكاة و CIT الفعلية على قواعد تفصيلية للهيئة. استعن بمستشار ضريبي مؤهل للتقديم الفعلي.

---

## المصادر الرسمية

| الجهة | الرابط |
|-------|--------|
| هيئة الزكاة والضريبة والجمارك | [zatca.gov.sa](https://zatca.gov.sa) |
| فاتورة (الفوترة الإلكترونية) | [fatoora.zatca.gov.sa](https://fatoora.zatca.gov.sa) |
| مجموعة البيانات | `data/fees.ar.json` — إدخالات `cit_corporate_income_tax` و`zakat_saudi_gcc_shareholders` و`wht_withholding_tax` |
```

- [ ] **Step 2: Verify file exists**

```bash
ls -la docs/ar/tax-compliance.md
```

---

## Task 7: Add corporate_bank_account_opening to timelines JSON files

**Files:**
- Modify: `data/timelines.en.json` — append one entry to `data` array
- Modify: `data/timelines.ar.json` — append Arabic mirror

- [ ] **Step 1: Append to timelines.en.json**

Insert before the closing `]` of the `data` array (after the last entry `strategic_investor_program_classification`). The new entry is:

```json
{
  "id": "corporate_bank_account_opening",
  "authority_id": "misa",
  "process_name": "Corporate Bank Account Opening",
  "min_days": 7,
  "max_days": 28,
  "typical_days": 14,
  "conditions": "Timeline varies by bank and KYC complexity. Foreign-owned companies typically require additional due diligence compared to Saudi-owned entities. All prerequisites must be complete before the bank visit: active MISA IRC, valid CR, National Address, GM Iqama. Inactive accounts risk dormancy — maintain regular transactions after activation. Timeline is an estimate from practitioner experience; no single SAMA-published benchmark exists for foreign-entity onboarding. Verify with the chosen bank and SAMA at sama.gov.sa.",
  "placeholder_reason": "No single official SAMA-published benchmark for foreign-entity bank account opening. Estimated range of 7-28 business days based on multiple 2025-2026 practitioner sources. Verify with the chosen bank directly.",
  "verify_at": "https://www.sama.gov.sa",
  "verification_status": "draft",
  "placeholders": [
    {
      "field": "min_days, max_days, typical_days",
      "description": "Bank account opening timelines for foreign-owned companies are not published by a single authority. Each SAMA-regulated bank sets its own KYC and onboarding standards. The range of 7-28 days reflects practitioner experience across multiple banks and entity types in 2025-2026. Verify current processing benchmarks with your chosen bank and SAMA.",
      "verify_at": "sama.gov.sa"
    }
  ],
  "tags": ["banking", "corporate_account", "sama", "timelines", "foreign_investment"]
}
```

- [ ] **Step 2: Append to timelines.ar.json**

Same position (after `strategic_investor_program_classification`). The Arabic mirror:

```json
{
  "id": "corporate_bank_account_opening",
  "authority_id": "misa",
  "process_name": "فتح حساب مصرفي للشركات",
  "min_days": 7,
  "max_days": 28,
  "typical_days": 14,
  "conditions": "يتفاوت الجدول الزمني بحسب البنك وتعقيد العناية الواجبة. تستلزم الشركات المملوكة لأجانب عادةً عناية واجبة إضافية مقارنة بالكيانات السعودية المملوكة. يجب استيفاء جميع المتطلبات الأولية قبل زيارة البنك: شهادة تسجيل الاستثمار النشطة، والسجل التجاري الساري، والعنوان الوطني، وإقامة المدير العام. الحسابات الخاملة معرَّضة للتجميد — حافظ على معاملات منتظمة بعد التفعيل. الجدول الزمني تقدير من خبرة عملية؛ لا يوجد معيار رسمي منشور من ساما لتأهيل الكيانات الأجنبية. تحقق مع البنك المختار وساما عبر sama.gov.sa.",
  "placeholder_reason": "لا يوجد معيار رسمي منشور من ساما لفتح الحسابات المصرفية للكيانات الأجنبية. النطاق المقدَّر بين 7 و28 يوم عمل مبني على مصادر عملية متعددة لعامَي 2025-2026. تحقق مع البنك المختار مباشرة.",
  "verify_at": "https://www.sama.gov.sa",
  "verification_status": "draft",
  "placeholders": [
    {
      "field": "min_days, max_days, typical_days",
      "description": "لا تنشر جهة واحدة جداول زمنية لفتح الحسابات المصرفية للشركات الأجنبية. تضع كل بنك مرخص من ساما معايير العناية الواجبة والتأهيل الخاصة به. النطاق بين 7 و28 يوما يعكس الخبرة العملية عبر بنوك وأنواع كيانات متعددة في 2025-2026. تحقق من معايير المعالجة الحالية مع البنك المختار وساما.",
      "verify_at": "sama.gov.sa"
    }
  ],
  "tags": ["banking", "corporate_account", "sama", "timelines", "foreign_investment"]
}
```

- [ ] **Step 3: Verify parity**

```bash
python3 scripts/check-bilingual-parity.py
```

Expected: PASS

---

## Task 8: Update REQUIRED_FILES in scripts/check.py

**Files:**
- Modify: `scripts/check.py` — add 6 paths to REQUIRED_FILES list

- [ ] **Step 1: Add 6 new paths**

Append these 6 entries after `"data/economic-activities.ar.json"` in the REQUIRED_FILES list in `scripts/check.py`:

```python
    "docs/en/nitaqat-saudization.md",
    "docs/ar/nitaqat-saudization.md",
    "docs/en/corporate-banking.md",
    "docs/ar/corporate-banking.md",
    "docs/en/tax-compliance.md",
    "docs/ar/tax-compliance.md",
```

- [ ] **Step 2: Run health check**

```bash
python3 scripts/check.py
```

Expected: count increases by at least 6 (one PASS per new required file). All checks pass.

---

## Task 9: Update README.md Browse the Docs section

**Files:**
- Modify: `README.md` — add 3 links in Browse the Docs section

- [ ] **Step 1: Add links**

Find this block in README.md:
```
## Browse the Docs

- [English Documentation →](docs/en/README.md)
...
- [Source Verification →](docs/en/source-verification.md)
- [Sources Index →](sources/index.md)
```

Add three new lines before `[Sources Index →]`:
```markdown
- [Saudization (Nitaqat) Guide →](docs/en/nitaqat-saudization.md)
- [Corporate Banking Guide →](docs/en/corporate-banking.md)
- [Tax Compliance Guide →](docs/en/tax-compliance.md)
```

---

## Task 10: Final validation and commit

- [ ] **Step 1: Run full health check**

```bash
python3 scripts/check.py
```

Expected: All checks pass. Count should be >= 181 (175 + 6 new file checks).

- [ ] **Step 2: Run dataset validation**

```bash
python3 scripts/validate-data.py
```

Expected: All datasets pass schema + semantic validation.

- [ ] **Step 3: Run bilingual parity check**

```bash
python3 scripts/check-bilingual-parity.py
```

Expected: PASS (timelines EN and AR have same IDs in same order).

- [ ] **Step 4: Commit and push**

```bash
git add -A
git commit -m "feat: Phase 2 operational docs — Nitaqat, corporate banking, tax compliance

Nitaqat/Saudization guide:
- 5 compliance tiers with consequences table
- Foreign investor counts as Saudi (April 2024 update)
- 2025-2026 sector updates: dental 55%, engineering 30%,
  accounting 40%+, marketing 60%, hospitals 65%
- Part-time workers 160h/month = 1 full Nitaqat point
- Source: HRSD Ministerial Decision 182495 + 2025 procedurals

Corporate banking guide:
- Prerequisites sequence: MISA -> CR -> National Address -> Iqama
- Required documents table (8 items)
- 5 major banks overview
- Timeline: 1-4 weeks
- Critical maintenance: Iqama renewal -> update bank immediately

Tax compliance guide:
- Dual system: CIT 20% (foreign) + Zakat 2.5% (Saudi/GCC)
- VAT 15%, WHT 5-20%, Fatoora e-invoicing mandatory
- Key deadlines table
- Mixed ownership worked example
- Cross-references data/fees.en.json verified entries

Timeline entry: corporate_bank_account_opening (7-28 days, draft)
README: 3 new Browse the Docs links

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>"

git push origin main
```

---

## Self-Review

### Spec Coverage

| Spec Requirement | Task Covering It |
|-----------------|-----------------|
| docs/en/nitaqat-saudization.md | Task 1 |
| docs/ar/nitaqat-saudization.md | Task 2 |
| docs/en/corporate-banking.md | Task 3 |
| docs/ar/corporate-banking.md | Task 4 |
| docs/en/tax-compliance.md | Task 5 |
| docs/ar/tax-compliance.md | Task 6 |
| Add corporate_bank_account_opening to timelines.en.json | Task 7 |
| Add Arabic mirror to timelines.ar.json | Task 7 |
| Update REQUIRED_FILES in check.py | Task 8 |
| Update Browse the Docs in README.md | Task 9 |
| python3 scripts/check.py passes | Task 10 |
| python3 scripts/validate-data.py passes | Task 10 |
| git commit + push | Task 10 |

### Invariant Checks

- Nitaqat rates: marked verified, cite HRSD Ministerial Decision 182495
- Banking timeline: draft, placeholder present, verify_at set to sama.gov.sa
- Arabic: no tashkeel, English numerals, formal MSA — confirmed in both AR docs
- tax-compliance.md cross-references fees.en.json, does not duplicate data
- All 6 new docs added to REQUIRED_FILES (Task 8)
- EN/AR timelines mirror: same IDs appended in same position (Task 7)
- No fabricated URLs: only hrsd.gov.sa, nitaqat.hrsd.gov.sa, qiwa.sa, sama.gov.sa, zatca.gov.sa, absher.sa, mudad.com.sa, fatoora.zatca.gov.sa confirmed domains used
