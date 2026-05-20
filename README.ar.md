# بوابة الاستثمار — المملكة العربية السعودية
<p align="center">
  <img src="assets/images/repo-cover.png" alt="Invest Gate KSA Cover" width="100%">
</p>

![الرخصة: MIT](https://img.shields.io/badge/License-MIT-blue.svg)
![اللغات](https://img.shields.io/badge/Languages-Arabic%20%7C%20English-green.svg)
![فحوصات الصحة](https://img.shields.io/badge/Health%20Checks-166%2F166-brightgreen.svg)
![مجموعات البيانات](https://img.shields.io/badge/Datasets-10-blue.svg)
![ادخالات الرسوم](https://img.shields.io/badge/Fee%20Entries-24-blue.svg)
![المصادر الموثقة](https://img.shields.io/badge/Verified%20Sources-14-green.svg)
![جاهز للـ MCP](https://img.shields.io/badge/MCP-Ready-8A2BE2.svg)
![جاهز للذكاء الاصطناعي](https://img.shields.io/badge/AI-Ready-FF6B35.svg)
![اخر تحديث](https://img.shields.io/badge/Updated-May%202026-orange.svg)

**قاعدة معرفية مفتوحة المصدر وثنائية اللغة، تساعد المستثمرين الاجانب على فهم كيفية تاسيس الاعمال وادارتها في المملكة العربية السعودية.**

---

> **تنبيه مهم**
> يتضمن هذا المستودع معلومات تعليمية عامة فقط. وهو **ليس استشارة قانونية او مالية او تنظيمية او ضريبية**. لا ينبغي الاعتماد على ما يرد هنا بديلا عن استشارة متخصصين مؤهلين. تتغير القوانين والرسوم والاجراءات في المملكة العربية السعودية — تحقق دائما من المعلومات مباشرة عبر المصادر الحكومية الرسمية، واستشر ممارسين مؤهلين قبل اتخاذ اي قرار.

---

## المشكلة

انفتحت المملكة العربية السعودية على الاستثمار الاجنبي بشكل ملحوظ في السنوات الاخيرة. غير ان المستثمر القادم من خارج المملكة يجد نفسه امام مسار بالغ التعقيد: المعلومات مبعثرة عبر عشرات البوابات الحكومية، وكثير منها باللغة العربية حصرا، وكثيرا ما تكون المواقع غير الرسمية تحمل معلومات متقادمة، ونادرا ما ترتب حول الاسئلة التي يطرحها المستثمر فعلا.

والنتيجة ان كثيرا من المستثمرين الاجانب يدفعون مبالغ طائلة للمستشارين مقابل معلومات كان ينبغي ان تكون متاحة للجميع — او يمضون قدما بناء على معلومات مغلوطة.

---

## ما هذا المشروع؟

بوابة الاستثمار KSA مستودع معرفي منظم يديره المجتمع، يجمع المعلومات المتاحة للعموم حول الاستثمار في المملكة العربية السعودية ويقدمها في شكل توثيق واضح، مرتبط بالمصادر، وثنائي اللغة.

ليس استشارة. وليس خدمة قانونية. بل هو **اطار مرجعي** — مصمم ليكون دقيقا وقابلا للتتبع ومفيدا كنقطة انطلاق قبل التعاقد مع المتخصصين.

كما يصمم المستودع من الاساس ليتطور الى **مساعد ذكاء اصطناعي وخادم MCP**، بحيث يمكن الاستفسار عن المعرفة ذاتها باسلوب حواري.

---

## البدء السريع

#### الخيار A — الاستعلام المباشر عن البيانات (CLI)

```bash
# استنساخ المستودع
git clone https://github.com/Samix2026/invest-gate-ksa.git
cd invest-gate-ksa

# تثبيت المتطلبات
pip3 install -r scripts/requirements.txt

# الاستعلام عن جدول الرسوم
python3 scripts/query-dataset.py --dataset fees --lang en --list

# الاستعلام عن القطاعات بالعربية
python3 scripts/query-dataset.py --dataset sectors --lang ar --list

# الاستعلام عن المناطق الاقتصادية الخاصة
python3 scripts/query-dataset.py --dataset sezs --lang en --list

# البحث عبر جميع مجموعات البيانات
python3 scripts/query-dataset.py --dataset all --keyword "MISA" --lang en
```

#### الخيار B — الاتصال بـ Claude Desktop عبر MCP

```bash
pip3 install -r mcp/requirements.txt
```

اضف التالي الى `~/Library/Application Support/Claude/claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "invest-gate-ksa": {
      "command": "python3",
      "args": ["/absolute/path/to/invest-gate-ksa/mcp/invest_gate_mcp.py"]
    }
  }
}
```

اعد تشغيل Claude Desktop، ثم اسأل:
- "What are the steps to register a company in Saudi Arabia as a foreign investor?"
- "ما رسوم التسجيل في وزارة الاستثمار؟"
- "What are the tax obligations for a foreign company in Saudi Arabia?"

#### الخيار C — استخدام البيانات مباشرة في مشروعك

```python
import json

with open('data/fees.en.json') as f:
    fees = json.load(f)

for entry in fees['data']:
    if entry.get('verification_status') == 'verified' and entry.get('amount_sar', 0) != 0:
        print(f"{entry['id']}: SAR {entry['amount_sar']} ({entry.get('frequency', '')})")
```

---

## مثال على المخرجات

**استعلام جدول الرسوم** (`--dataset fees --lang en --list`):

```
fees  (en)  —  24 entries
────────────────────────────────────────────────────────────────────────────────
  ID                                NAME                          STATUS
────────────────────────────────────────────────────────────────────────────────
  misa_investment_registration_fee  Fee charged by the Ministry … verified
  misa_activity_amendment_fee       Fee charged by the Ministry … verified
  misa_ownership_amendment_fee      Fee charged by the Ministry … verified
  misa_annual_renewal_fee           Fee for the annual update of… verified
  misa_property_approval_fee        Fee charged by the Ministry … verified
  misa_registration_cancellation_fe Fee charged by the Ministry … verified
  commercial_registration_issuance_ Fee charged by the Ministry … verified
  branch_commercial_registration_fe Historical entry — Branch Co… verified
  chamber_of_commerce_fee           Annual mandatory Chamber of … verified
  cit_corporate_income_tax          Corporate Income Tax (CIT) c… verified
  zakat_saudi_gcc_shareholders      Zakat is an annual Islamic l… verified
  wht_withholding_tax               Withholding Tax (WHT) charge… verified
  entrepreneurial_license_fee_y1_3  Reduced MISA Entrepreneurial… verified
  entrepreneurial_license_fee_y4_5  MISA Entrepreneurial License… verified
  qiwa_employer_registration_fee    Fee for registering as an em… verified
  iqama_issuance_renewal_fee        Annual Iqama (residency perm… verified
  final_exit_visa_fee               Fee for issuing a final exit… verified
  exit_reentry_visa_extension_fee   Fee for extending an exit/re… verified
────────────────────────────────────────────────────────────────────────────────
  24 entry/entries
```

**استعلام القطاعات بالعربية** (`--dataset sectors --lang ar --list`):

```
sectors  (ar)  —  16 entries
────────────────────────────────────────────────────────────────────────────────
  ID                                NAME                          STATUS
────────────────────────────────────────────────────────────────────────────────
  technology                        التقنية                       draft
  consulting                        الاستشارات والخدمات المهنية   draft
  ecommerce                         التجارة الإلكترونية           draft
  food_and_beverage                 الأغذية والمشروبات            draft
  real_estate                       العقارات                      draft
  education                         التعليم                       draft
  healthcare                        الرعاية الصحية                draft
  fintech                           التقنية المالية (فينتك)       draft
  manufacturing                     التصنيع                       draft
  industrial_services               الخدمات الصناعية              draft
  mining                            التعدين والموارد المعدنية     draft
  tourism_and_hospitality           السياحة والضيافة              draft
  media_and_content                 الإعلام والمحتوى              draft
  hajj_umrah_services               خدمات الحج والعمرة            draft
  entertainment_and_events          الترفيه والفعاليات            draft
────────────────────────────────────────────────────────────────────────────────
  16 entry/entries
```

**استعلام المناطق الاقتصادية الخاصة** (`--dataset sezs --lang en --list`):

```
sezs  (en)  —  5 entries
────────────────────────────────────────────────────────────────────────────────
  ID                                NAME                          STATUS
────────────────────────────────────────────────────────────────────────────────
  kaec_sez                          King Abdullah Economic City … verified
  jazan_sez                         Jazan Special Economic Zone   verified
  ras_al_khair_sez                  Ras Al-Khair Special Economi… verified
  cloud_computing_sez               Cloud Computing Special Econ… verified
  silz                              Special Integrated Logistics… draft
────────────────────────────────────────────────────────────────────────────────
  5 entry/entries
```

---

## لمن هذا المشروع؟

| الجمهور | طريقة الاستفادة |
|---|---|
| رواد الاعمال والمستثمرون الاجانب | فهم البيئة الاستثمارية قبل التعاقد مع المستشارين |
| مستشارو تاسيس الاعمال | مرجع لمشاركة ادلة اجرائية منظمة |
| الباحثون والاكاديميون | نظرة شاملة مرتبطة بالمصادر عن اطار الاستثمار السعودي |
| المطورون | قاعدة معرفية لبناء ادوات استثمارية ومساعدين بالذكاء الاصطناعي |
| المترجمون والمتخصصون ثنائيو اللغة | توافق عربي-انجليزي للمصطلحات التجارية والتنظيمية |

---

## حالات الاستخدام

**للمطورين:**
- بناء مساعد ذكاء اصطناعي متخصص في توجيه الاستثمار في المملكة العربية السعودية
- تغذية وكيل ذكاء اصطناعي ببيانات تنظيمية منظمة
- التكامل عبر MCP مع Claude Desktop او اي عميل متوافق مع MCP

**لرواد الاعمال والمستثمرين:**
- فهم المسار التنظيمي الكامل قبل التعاقد مع المستشارين
- مقارنة هياكل الاعمال (ذ.م.م مقابل فرع مقابل مقر اقليمي)
- التحقق من تقديرات الرسوم بالرجوع الى المصادر الرسمية

**للباحثين:**
- مجموعة بيانات تنظيمية منظمة، ثنائية اللغة، مرتبطة بالمصادر
- تتبع صريح لفجوات البيانات — 25 فجوة بيانات موثقة
- محفوظة في Git مع سجل تغييرات كامل

**لبناة حلول الذكاء الاصطناعي:**
- 10 مجموعات بيانات JSON بمخطط صارم (Draft-07)
- ثنائية اللغة EN/AR مع فرض تكافؤ المعرفات
- خادم MCP بـ 8 ادوات — قابل للتوصيل بأي وكيل متوافق مع MCP
- موجه نظام مدرج لنشر مساعد ذكاء اصطناعي جاهز فورا

---

## محتويات المستودع

| المجلد / الملف | المحتوى |
|---|---|
| `data/` | 10 مجموعات بيانات ثنائية اللغة (EN + AR) |
| `data/sectors` | 16 قطاع استثماري مع توافق رؤية 2030 |
| `data/sources` | 14 مصدرا من الجهات التنظيمية الرسمية الموثقة |
| `data/source-gaps` | 24 فجوة بيانات متتبعة في انتظار التحقق |
| `data/fees` | 24 ادخال رسوم — الادخالات الموثقة تستشهد بالمصادر الرسمية |
| `data/timelines` | 10 ادخالات للمدد الزمنية — موثقة من منشورات رسمية |
| `data/sezs` | 5 مناطق اقتصادية خاصة (KAEC، جازان، راس الخير، السحابية، SILZ) |
| `data/setup-flows` | 4 مسارات تسجيل حسب السيناريو (استشارات، تجارة الكترونية، تصنيع، تقنية مالية) |
| `data/business-structures` | 4 انواع كيانات قانونية (ذ.م.م، شركة مساهمة، فرع، مكتب تمثيل) |
| `data/authority-relationships` | 12 خريطة علاقات بين الجهات التنظيمية |
| `data/investment-licenses` | 5 مفاهيم تسجيل وترخيص في تسلسل التاسيس |
| `schemas/` | JSON Schema Draft-07 — تنظيم صارم، additionalProperties: false |
| `docs/en/` | ادلة انجليزية: التسجيل، الضرائب، SEZs، رؤية 2030، الهياكل |
| `docs/ar/` | نظائر عربية (RTL) — تكافؤ ثنائي اللغة مطبق بالكامل |
| `mcp/` | خادم FastMCP — 8 ادوات استعلام لتكامل Claude Desktop |
| `.claude/commands/` | 6 اوامر slash للعمليات اليومية على المستودع |
| `prompts/` | موجه نظام الذكاء الاصطناعي (ثنائي اللغة، قواعد الاستشهاد، اخلاء المسؤولية) |
| `scripts/` | مجموعة فحص 166 نقطة (JSON، المخططات، التكافؤ، المراجع المتقاطعة) |
| `sources/` | سجل الاستشهادات — كل ادعاء مرتبط بمصدره |
| `templates/` | قوائم مراجعة للمستثمرين — مخطط لها |
| `.github/workflows/` | CI/CD — التحقق عند كل push وطلب دمج |

---

## التغطية الجوهرية

- المسار التنظيمي الكامل: MISA — السجل التجاري — الغرفة التجارية — ZATCA — GOSI — قوى — مقيم
- انواع تسجيل الاعمال: تسجيل الاستثمار القياسي، المقر الاقليمي (RHQ)، الريادي
- الاطار الضريبي: ضريبة دخل شركات 20% (اجانب)، زكاة 2.5% (سعوديون/خليجيون)، ضريبة قيمة مضافة 15%، استقطاع 5–20%
- المناطق الاقتصادية الخاصة: KAEC، جازان، راس الخير، الحوسبة السحابية، SILZ (ضريبة دخل 5%)
- توافق قطاعات رؤية 2030: 16 قطاعا باهداف رسمية وجهات اشراف محددة
- جداول الرسوم والمدد الزمنية — موثقة من مصادر رسمية
- التحديثات التنظيمية لعام 2025: نظام السجل التجاري الجديد (ابريل 2025)، نظام الاستثمار (اغسطس 2024)

---

## حالة المشروع

| المرحلة | التقدم | الحالة | الوصف |
|---|---|---|---|
| المرحلة 1 — الاساس | ██████████ | مكتملة | الهيكل، المخططات، مجموعة 166 فحص |
| المرحلة 2 — قاعدة المعرفة | ████████░░ | جارية | 10 مجموعات بيانات، مناطق SEZ، رؤية 2030 |
| المرحلة 3 — سير عمل الذكاء | ██████████ | مكتملة | موجه نظام الذكاء الاصطناعي، 8 ادوات MCP |
| المرحلة 4 — تكامل MCP | ██████████ | مكتملة | جاهز لـ Claude Desktop |
| المرحلة 5 — طبقة المنتج | ░░░░░░░░░░ | مخطط له | — |

**حالة التحقق (2026-05-20):**
- ✅ موثق من مصادر رسمية: تسجيل MISA، السجل التجاري، الغرفة التجارية، ZATCA، GOSI، قوى، مقيم، SEZs (ECZA + الجريدة الرسمية يناير 2026)، مؤشرات رؤية 2030
- ⚠️ مسودة — يحتاج تاكيدا رسميا: رسوم تسجيل RHQ، تفاصيل SILZ الضريبية
- 📋 مخطط له: مجموعة بيانات الانشطة الاقتصادية، قوالب قوائم المراجعة

راجع [roadmap.md](roadmap.md) للخطة الكاملة.

---

## المساهمة

يكبر هذا المشروع من خلال معرفة من لديهم خبرة مباشرة وموثقة. نرحب بمساهمات المستشارين والمحامين والباحثين والمستثمرين والمطورين.

**ما نحتاجه اكثر ما يكون الان:**
- مبالغ رسوم موثقة من مصادر رسمية (خاصة RHQ وSILZ)
- مجموعة بيانات الانشطة الاقتصادية (رموز نشاط MISA مع احكام الملكية الاجنبية)
- قوالب قوائم مراجعة للمستثمرين (ذ.م.م، فرع، وثائق MISA)
- تصحيحات لاي معلومات متقادمة

كل محتوى يجب ان يستشهد بمصدر رسمي. راجع [CONTRIBUTING.md](CONTRIBUTING.md) للاطلاع على الارشادات الكاملة.

---

## فحص صحة المشروع

```bash
python3 scripts/check.py
```

يشغل 166 فحصا: الملفات المطلوبة، صحة JSON، التحقق من المخططات، سلامة الاسماء البديلة، سلامة المراجع المتقاطعة، التكافؤ الثنائي. يخرج بالرمز `0` عند النجاح الكامل.

---

## خادم MCP — تكامل Claude Desktop

يتضمن هذا المستودع خادم MCP جاهزا يربط Claude Desktop مباشرة بقاعدة المعرفة.

**الادوات المتاحة:** استعلام القطاعات · استعلام الجهات التنظيمية · مسارات التاسيس · الرسوم · المدد الزمنية · الهياكل القانونية · مسار المستثمر · البحث الشامل

راجع [mcp/README.md](mcp/README.md) لتعليمات الاعداد الكاملة.

---

## تصفح الوثائق

- [الوثائق العربية ←](docs/ar/README.md)
- [English Documentation ←](docs/en/README.md)
- [انواع التسجيل ←](docs/ar/registration-types.md)
- [المناطق الاقتصادية الخاصة ←](docs/ar/special-economic-zones.md)
- [دليل قطاعات رؤية 2030 ←](docs/ar/vision2030-sectors.md)
- [الالتزامات الضريبية ←](docs/ar/company-setup-overview.md)
- [سير عمل التحقق من المصادر ←](docs/ar/source-verification.md)
- [فهرس المصادر ←](sources/index.md)

---

## الرخصة

[رخصة MIT](LICENSE) — حر الاستخدام والتعديل والتوزيع مع الاسناد.

يحمل المحتوى (الادلة، البيانات، القوالب) تنبيها اضافيا: هو تعليمي لا استشاري. راجع [LICENSE](LICENSE) للاطلاع على تنبيه المحتوى الكامل.
