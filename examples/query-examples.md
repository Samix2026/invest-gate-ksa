# Query Examples — Business Structures

Example commands and real terminal output for `scripts/query-structures.py`.

**Requirements:** Python 3.7+ — no additional packages needed.

Run all commands from the repository root.

---

## 1. List All Structures (English)

```bash
python scripts/query-structures.py --list
```

```
Business Structures (en)  —  4 entries
────────────────────────────────────────────────────────────────────────
  ID                      NAME                          COMM STATUS
────────────────────────────────────────────────────────────────────────
  llc                     Limited Liability Company     Yes  draft
  joint_stock_company     Joint Stock Company           Yes  draft
  foreign_branch          Branch of a Foreign Company   Yes  draft
  representative_office   Representative Office         No   draft
────────────────────────────────────────────────────────────────────────
  4 structure(s)
```

**`COMM`** — whether the structure can perform commercial activities and generate revenue.

---

## 2. List All Structures (Arabic)

```bash
python scripts/query-structures.py --lang ar --list
```

```
Business Structures (ar)  —  4 entries
────────────────────────────────────────────────────────────────────────
  ID                      NAME                          COMM STATUS
────────────────────────────────────────────────────────────────────────
  llc                     شركة ذات مسؤولية محدودة       Yes  draft
  joint_stock_company     شركة مساهمة                   Yes  draft
  foreign_branch          فرع شركة أجنبية               Yes  draft
  representative_office   مكتب التمثيل                  No   draft
────────────────────────────────────────────────────────────────────────
  4 structure(s)
```

IDs are always in English (they are machine-readable keys). Names and all descriptive content are in the requested language.

---

## 3. Detail View — Single Structure (English)

```bash
python scripts/query-structures.py --id llc
```

```
Limited Liability Company (LLC)
────────────────────────────────────────────────────────────────────────
  ID:         llc
  Status:     draft
  Also known: Sharika That Mas'uliyya Mahduda (ش.م.م)

  DESCRIPTION
    The most commonly used structure for foreign investors establishing
    an operating presence in Saudi Arabia. Partners' liability is
    generally limited to their capital contribution. Can be established
    with a single shareholder or multiple partners.

  OWNERSHIP
    Full foreign ownership:  sector_dependent
    Local ownership:         Yes
    Mixed ownership:         Yes
    Full foreign ownership is permitted in many sectors under Vision
    2030 reforms. Certain sectors may still require a local partner or
    remain restricted. Eligibility is determined by MISA's approved
    activity list.

  LEGAL ENTITY
    Separate legal entity:   Yes
    Liability model:         limited_to_capital_contribution
    Commercial activities:   Yes

  TYPICAL USE CASES
    1. General commercial and trading operations
    2. Professional and consulting services
    3. Manufacturing and industrial activities
    4. Technology and software services
    5. Real estate activities (sector rules apply)
    6. Retail and distribution (sector rules apply)

  MISA LICENSE
    Applicable:   Yes
    Condition:    required_for_foreign_investors
    Local:        not_applicable
    Foreign investors must obtain a MISA investment license before
    registering commercially. The license is activity-specific. Local
    (Saudi/GCC) investors register directly with the Ministry of
    Commerce without a MISA license.
    Verify at:    misa.gov.sa

  OFFICIAL SOURCES
    1. Ministry of Investment (MISA)
       Role:    Investment license issuance and sector eligibility
       Portal:  misa.gov.sa
    2. Ministry of Commerce
       Role:    Commercial registration and Companies Law
       Portal:  mc.gov.sa

  PLACEHOLDERS  (3 pending verification)
    1. ownership_type.allows_full_foreign_ownership
       The specific list of sectors open to 100% foreign LLC ownership
       is governed by MISA's approved activities list and may be
       updated. Verify current sector eligibility before proceeding.
       → Verify at: misa.gov.sa
    2. shareholder_requirements
       Minimum and maximum number of shareholders permitted under
       current Saudi Companies Law. Subject to legislative amendments.
       → Verify at: mc.gov.sa
    3. minimum_capital
       Minimum capital requirements, if any, for an LLC — including
       sector-specific thresholds. Not included in this dataset to avoid
       stating unverified figures.
       → Verify at: misa.gov.sa

────────────────────────────────────────────────────────────────────────
  Source: data/business-structures.en.json  |  sources/index.md
```

---

## 4. Detail View — Single Structure (Arabic)

```bash
python scripts/query-structures.py --lang ar --id representative_office
```

```
مكتب التمثيل
────────────────────────────────────────────────────────────────────────
  ID:         representative_office
  Status:     draft
  Also known: Representative Office

  DESCRIPTION
    حضور غير تجاري مرتبط بشركة أجنبية، مسموح به للأنشطة الترويجية
    والبحثية وأنشطة الارتباط فحسب. لا يجوز له إجراء معاملات تجارية
    مباشرة أو إبرام عقود تجارية باسمه الخاص أو توليد إيرادات في المملكة
    العربية السعودية.

  OWNERSHIP
    Full foreign ownership:  Yes
    Local ownership:         No
    Mixed ownership:         No
    مكتب التمثيل مرتبط مباشرةً بشركة أجنبية أم وتابع لها. ولا هيكل
    استقلالي للملكية.

  LEGAL ENTITY
    Separate legal entity:   No
    Liability model:         parent_linked
    Commercial activities:   No

  TYPICAL USE CASES
    1. أبحاث السوق ودراسات الجدوى
    2. الترويج للعلامة التجارية والارتباط التسويقي
    3. تنسيق أنشطة الشركة الأم وعلاقاتها في المملكة العربية السعودية
    4. الدخول الأولي للسوق قبل الالتزام بهيكل تجاري كامل

  MISA LICENSE
    Applicable:   Yes
    Condition:    required
    Local:        not_applicable
    تُشترط رخصة من وزارة الاستثمار لمكتب التمثيل. وقد يختلف نوع الرخصة
    عن تلك الصادرة للكيانات التجارية. تُحدَّد الأنشطة المسموح بها للمكتب
    بموجب الرخصة.
    Verify at:    misa.gov.sa

  OFFICIAL SOURCES
    1. وزارة الاستثمار (ماسة)
       Role:    رخصة مكتب التمثيل والأنشطة المسموح بها
       Portal:  misa.gov.sa

  PLACEHOLDERS  (3 pending verification)
    1. license_type_distinction
       فئة الرخصة المحددة الصادرة عن وزارة الاستثمار لمكتب التمثيل
       وكيفية اختلافها عن رخصة الكيان التجاري. يُستلزم التحقق مع وزارة
       الاستثمار.
       → Verify at: misa.gov.sa
    2. permitted_activities_detail
       النطاق الدقيق للأنشطة التي يُسمح لمكتب التمثيل بممارستها (كمدى
       صلاحيته لإبرام عقود نيابةً عن الشركة الأم أو توظيف موظفين سعوديين
       أو استئجار مكاتب).
       → Verify at: misa.gov.sa
    3. renewal_and_duration
       هل لرخصة مكتب التمثيل مدة ثابتة؟ وما اشتراطات تجديدها؟ وما شروط
       التحوّل منها إلى هيكل تجاري؟
       → Verify at: misa.gov.sa

────────────────────────────────────────────────────────────────────────
  Source: data/business-structures.ar.json  |  sources/index.md
```

---

## 5. Filter by Tag — Single Match

```bash
python scripts/query-structures.py --tag non_commercial
```

```
Tag: non_commercial  —  1 match(es)  (en)
────────────────────────────────────────────────────────────────────────
  ID                      NAME                          COMM STATUS
────────────────────────────────────────────────────────────────────────
  representative_office   Representative Office         No   draft
────────────────────────────────────────────────────────────────────────
  1 structure(s)
```

---

## 6. Filter by Tag — Multiple Matches

```bash
python scripts/query-structures.py --tag foreign_investment
```

```
Tag: foreign_investment  —  4 match(es)  (en)
────────────────────────────────────────────────────────────────────────
  ID                      NAME                          COMM STATUS
────────────────────────────────────────────────────────────────────────
  llc                     Limited Liability Company     Yes  draft
  joint_stock_company     Joint Stock Company           Yes  draft
  foreign_branch          Branch of a Foreign Company   Yes  draft
  representative_office   Representative Office         No   draft
────────────────────────────────────────────────────────────────────────
  4 structure(s)
```

Tags can be combined with `--lang`:

```bash
python scripts/query-structures.py --lang ar --tag capital_markets
```

```
Tag: capital_markets  —  1 match(es)  (ar)
────────────────────────────────────────────────────────────────────────
  ID                      NAME                          COMM STATUS
────────────────────────────────────────────────────────────────────────
  joint_stock_company     شركة مساهمة                   Yes  draft
────────────────────────────────────────────────────────────────────────
  1 structure(s)
```

---

## 7. Error: Unknown ID

```bash
python scripts/query-structures.py --id unknown_id
```

```
No structure found with id 'unknown_id'.
Available ids: llc, joint_stock_company, foreign_branch, representative_office
```

Exit code: `1`

---

## 8. Error: Unknown Tag

```bash
python scripts/query-structures.py --tag unknown_tag
```

```
No structures found with tag 'unknown_tag'.
Available tags: capital_markets, direct_extension, foreign_branch,
foreign_investment, ipo_eligible, large_enterprise, liaison,
limited_liability, local_investment, market_entry, most_common,
no_local_partner, no_revenue, non_commercial, operating_entity,
parent_liability, promotion_only, regulated_sectors, tadawul, vision_2030
```

Exit code: `1`

---

## Reference: All IDs and Tags

**Available IDs**

| ID | English Name |
|---|---|
| `llc` | Limited Liability Company |
| `joint_stock_company` | Joint Stock Company |
| `foreign_branch` | Branch of a Foreign Company |
| `representative_office` | Representative Office |

**Available Tags** (20 total)

| Tag | Structures |
|---|---|
| `capital_markets` | joint_stock_company |
| `direct_extension` | foreign_branch |
| `foreign_branch` | foreign_branch |
| `foreign_investment` | all 4 |
| `ipo_eligible` | joint_stock_company |
| `large_enterprise` | joint_stock_company |
| `liaison` | representative_office |
| `limited_liability` | llc |
| `local_investment` | llc, joint_stock_company |
| `market_entry` | representative_office |
| `most_common` | llc |
| `no_local_partner` | foreign_branch |
| `no_revenue` | representative_office |
| `non_commercial` | representative_office |
| `operating_entity` | llc |
| `parent_liability` | foreign_branch |
| `promotion_only` | representative_office |
| `regulated_sectors` | joint_stock_company |
| `tadawul` | joint_stock_company |
| `vision_2030` | llc |

---

## MCP / API Integration

The query functions in `scripts/query-structures.py` are pure — no I/O, no side effects — and can be imported directly into an MCP server or REST API without modification.

```python
from scripts.query_structures import DataLoader, get_by_id, get_by_tag, list_all

# MCP tool handler example
def handle_get_structure(tool_input: dict) -> dict:
    data = DataLoader.load(tool_input.get("lang", "en"))
    entry = get_by_id(data, tool_input["id"])
    return entry or {"error": "not_found", "id": tool_input["id"]}

# REST endpoint example
def api_list(lang: str = "en") -> list:
    data = DataLoader.load(lang)
    return list_all(data)
```

`DataLoader` caches datasets in memory after the first load, so repeated queries are served from cache without disk I/O.

See [`prompts/README.md`](../prompts/README.md) for the planned MCP tool definition schema.
