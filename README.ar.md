# بوابة الاستثمار — المملكة العربية السعودية
<p align="center">
  <img src="assets/images/repo-cover.png" alt="Invest Gate KSA Cover" width="100%">
</p>

![الرخصة: MIT](https://img.shields.io/badge/License-MIT-blue.svg)
![اللغات](https://img.shields.io/badge/Languages-Arabic%20%7C%20English-green.svg)
![فحوصات الصحة](https://img.shields.io/badge/Health%20Checks-189%2F189-brightgreen.svg)<!--badge:health_checks-->
![مجموعات البيانات](https://img.shields.io/badge/Datasets-11-blue.svg)<!--badge:datasets-->
![ادخالات الرسوم](https://img.shields.io/badge/Fee%20Entries-26-blue.svg)<!--badge:fees-->
![المصادر](https://img.shields.io/badge/Sources-17-green.svg)<!--badge:sources_total-->
![جاهز للـ MCP](https://img.shields.io/badge/MCP-Ready-8A2BE2.svg)
![جاهز للذكاء الاصطناعي](https://img.shields.io/badge/AI-Ready-FF6B35.svg)
![اخر تحديث](https://img.shields.io/badge/Updated-June%202026-orange.svg)

## المعمارية

> كيف يتحول السؤال إلى إجابة موثقة

### خريطة النظام التفاعلية

استكشف كيف ينتقل سؤال المستثمر عبر أدوات MCP ومجموعات البيانات ثنائية اللغة
وطبقة التحقق حتى يصل إلى إجابة مرتبطة بالمصدر.

[![فتح الشرح التفاعلي](https://img.shields.io/badge/فتح-خريطة_النظام_التفاعلية-37D39A?style=for-the-badge&logo=github)](https://samix2026.github.io/invest-gate-ksa/)

> تُنشر الصفحة التفاعلية تلقائيا عبر GitHub Pages. ويمكن أيضا
> [عرض الكود المصدري](assets/interactive/repo-explainer.html).

المستثمر يسأل بالعربي أو الإنجليزي ← Claude Desktop يوجه عبر <!--count:mcp_tools-->10<!--/count--> أدوات MCP ←
الخادم يستعلم <!--count:datasets-->11<!--/count--> مجموعة بيانات ثنائية اللغة ← كل إجابة تستشهد بمصدرها الرسمي
مع حالة التحقق (✓ موثق من مصدر رسمي / ⚠ مسودة في انتظار التحقق).

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

ويتضمن المستودع **خادم MCP عاملا وموجها أساسيا للذكاء الاصطناعي**، بحيث يمكن الاستفسار عن المعرفة ذاتها بأسلوب حواري.

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

**استعلام جدول الرسوم** (`--dataset fees --lang en --list`) يعرض حاليا:

```
fees  (en)  —  26 entries
20 verified · 6 draft
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
- تتبع صريح لفجوات البيانات — <!--count:source_gaps-->23<!--/count--> فجوة بيانات موثقة
- محفوظة في Git مع سجل تغييرات كامل

**لبناة حلول الذكاء الاصطناعي:**
- <!--count:datasets-->11<!--/count--> مجموعة بيانات JSON بمخطط صارم (Draft-07)
- ثنائية اللغة EN/AR مع فرض تكافؤ المعرفات
- خادم MCP بـ <!--count:mcp_tools-->10<!--/count--> ادوات — قابل للتوصيل بأي وكيل متوافق مع MCP
- موجه نظام مدرج لنشر مساعد ذكاء اصطناعي جاهز فورا

---

## محتويات المستودع

| المجلد / الملف | المحتوى |
|---|---|
| `data/` | <!--count:datasets-->11<!--/count--> مجموعة بيانات ثنائية اللغة (EN + AR) |
| `data/sectors` | <!--count:sectors-->16<!--/count--> قطاع استثماري مع توافق رؤية 2030 |
| `data/sources` | <!--count:sources_total-->17<!--/count--> ادخال مصدر — <!--count:sources_verified-->5<!--/count--> موثقة و<!--count:sources_draft-->12<!--/count--> مسودة |
| `data/source-gaps` | <!--count:source_gaps-->23<!--/count--> فجوة بيانات متتبعة في انتظار التحقق |
| `data/fees` | <!--count:fees-->26<!--/count--> ادخال رسوم — <!--count:fees_verified-->20<!--/count--> موثقة و<!--count:fees_draft-->6<!--/count--> مسودة |
| `data/timelines` | <!--count:timelines-->12<!--/count--> ادخال مدة زمنية — <!--count:timelines_verified-->8<!--/count--> موثقة و<!--count:timelines_draft-->4<!--/count--> مسودة |
| `data/sezs` | <!--count:sezs-->5<!--/count--> مناطق اقتصادية خاصة (KAEC، جازان، راس الخير، السحابية، SILZ) |
| `data/economic-activities` | <!--count:economic_activities-->21<!--/count--> نشاطا اقتصاديا — <!--count:economic_activities_verified-->10<!--/count--> موثقة و<!--count:economic_activities_draft-->11<!--/count--> مسودة |
| `data/setup-flows` | <!--count:setup_flows-->4<!--/count--> مسارات تسجيل حسب السيناريو (استشارات، تجارة الكترونية، تصنيع، تقنية مالية) |
| `data/business-structures` | <!--count:business_structures-->4<!--/count--> انواع كيانات قانونية (ذ.م.م، شركة مساهمة، فرع، مكتب تمثيل) |
| `data/authority-relationships` | <!--count:authority_relationships-->12<!--/count--> خريطة علاقات بين الجهات التنظيمية |
| `data/investment-licenses` | <!--count:investment_licenses-->5<!--/count--> مفاهيم تسجيل وترخيص في تسلسل التاسيس |
| `schemas/` | JSON Schema Draft-07 — تنظيم صارم، additionalProperties: false |
| `docs/en/` | ادلة انجليزية: التسجيل، الضرائب، SEZs، رؤية 2030، الهياكل |
| `docs/ar/` | نظائر عربية (RTL) — تكافؤ ثنائي اللغة مطبق بالكامل |
| `mcp/` | خادم FastMCP — <!--count:mcp_tools-->10<!--/count--> ادوات استعلام لتكامل Claude Desktop |
| `.claude/commands/` | <!--count:commands-->6<!--/count--> اوامر slash للعمليات اليومية على المستودع |
| `prompts/` | موجه نظام الذكاء الاصطناعي (ثنائي اللغة، قواعد الاستشهاد، اخلاء المسؤولية) |
| `scripts/` | مجموعة فحص <!--count:health_checks-->189<!--/count--> نقطة (JSON، المخططات، التكافؤ، المراجع المتقاطعة) |
| `sources/` | سجل الاستشهادات — كل ادعاء مرتبط بمصدره |
| `templates/` | قوائم مراجعة للشركة ذات المسؤولية المحدودة والفرع ووثائق MISA والتحقق من المصادر |
| `.github/workflows/` | CI/CD — التحقق عند كل push وطلب دمج |

---

## التغطية الجوهرية

- المسار التنظيمي الكامل: MISA — السجل التجاري — الغرفة التجارية — ZATCA — GOSI — قوى — مقيم
- انواع تسجيل الاعمال: تسجيل الاستثمار القياسي، المقر الاقليمي (RHQ)، الريادي
- الاطار الضريبي: ضريبة دخل شركات 20% (اجانب)، زكاة 2.5% (سعوديون/خليجيون)، ضريبة قيمة مضافة 15%، استقطاع 5–20%
- المناطق الاقتصادية الخاصة: KAEC، جازان، راس الخير، الحوسبة السحابية، SILZ (ضريبة دخل 5%)
- توافق قطاعات رؤية 2030: <!--count:sectors-->16<!--/count--> قطاعا باهداف رسمية وجهات اشراف محددة
- جداول الرسوم والمدد الزمنية — موثقة من مصادر رسمية
- التحديثات التنظيمية لعام 2025: نظام السجل التجاري الجديد (ابريل 2025)، نظام الاستثمار (اغسطس 2024)

---

## حالة المشروع

| المرحلة | التقدم | الحالة | الوصف |
|---|---|---|---|
| المرحلة 1 — الاساس | ██████████ | مكتملة | الهيكل، المخططات، مجموعة <!--count:health_checks-->189<!--/count--> فحص |
| المرحلة 2 — قاعدة المعرفة | ████████░░ | جارية | <!--count:datasets-->11<!--/count--> مجموعة بيانات، ادلة ثنائية اللغة، مناطق SEZ، رؤية 2030 |
| المرحلة 3 — سير عمل الذكاء | ██████████ | مكتملة | موجه نظام الذكاء الاصطناعي، <!--count:mcp_tools-->10<!--/count--> ادوات MCP |
| المرحلة 4 — تكامل MCP | ██████████ | مكتملة | جاهز لـ Claude Desktop |
| المرحلة 5 — طبقة المنتج | ██████░░░░ | جارية | خريطة النظام التفاعلية منشورة عبر GitHub Pages |

**لقطة حالة المستودع (2026-06-14):**
- ✅ موثق من مصادر رسمية: تسجيل MISA، السجل التجاري، الغرفة التجارية، ZATCA، GOSI، قوى، مقيم، SEZs (ECZA + الجريدة الرسمية يناير 2026)، مؤشرات رؤية 2030
- ⚠️ مسودة — يحتاج تاكيدا رسميا: رسوم تسجيل RHQ، تفاصيل SILZ الضريبية
- 📋 التالي: توثيق الانشطة المسودة ورسوم RHQ وتفاصيل SILZ

راجع [roadmap.md](roadmap.md) للخطة الكاملة.

---

## منهجية التحقق

يحمل كل ادخال بيانات حالة تحقق صريحة: **موثق** (مؤكد من مصدر رسمي على نطاق .gov.sa او الجريدة الرسمية)، او **مسودة** (من مصادر موثوقة لكن دون تاكيد رسمي)، او **عنصر نائب** (فجوة معترف بها لم تبحث بعد). لا تقدم الادخالات غير الموثقة على انها حقائق — بل تحمل تنبيها ورابط `verify_at`. راجع [docs/ar/source-verification.md](docs/ar/source-verification.md) لسير العمل الكامل.

---

## المساهمة

يكبر هذا المشروع من خلال معرفة من لديهم خبرة مباشرة وموثقة. نرحب بمساهمات المستشارين والمحامين والباحثين والمستثمرين والمطورين.

**ما نحتاجه اكثر ما يكون الان:**
- مبالغ رسوم موثقة من مصادر رسمية (خاصة RHQ وSILZ)
- التحقق من <!--count:economic_activities_draft-->11<!--/count--> ادخال نشاط اقتصادي ما زال في حالة مسودة
- توسيع سيناريوهات المستثمرين وقوائم المراجعة
- تصحيحات لاي معلومات متقادمة

كل محتوى يجب ان يستشهد بمصدر رسمي. راجع [CONTRIBUTING.md](CONTRIBUTING.md) للاطلاع على الارشادات الكاملة.

---

## فحص صحة المشروع

```bash
python3 scripts/check.py
```

يشغل <!--count:health_checks-->189<!--/count--> فحصا: الملفات المطلوبة، صحة JSON، التحقق من المخططات، سلامة الاسماء البديلة، سلامة المراجع المتقاطعة، التكافؤ الثنائي. يخرج بالرمز `0` عند النجاح الكامل.

---

## خادم MCP — تكامل Claude Desktop

يتضمن هذا المستودع خادم MCP جاهزا يربط Claude Desktop مباشرة بقاعدة المعرفة.

**الادوات المتاحة:** استعلام القطاعات · استعلام الجهات التنظيمية · مسارات التاسيس · الرسوم · المدد الزمنية · المناطق الاقتصادية الخاصة · الانشطة الاقتصادية · الهياكل القانونية · مسار المستثمر · البحث الشامل

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
