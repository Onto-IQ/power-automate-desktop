# Lab 10 — Capstone: Web Scout & Sales Operations (Hands-on)

**อ่านก่อน:** [LESSON.md](LESSON.md) · **หน้าปกบท:** [README.md](README.md) · **พื้นฐาน:** [`shared/PAD-FUNDAMENTALS.md`](../../shared/PAD-FUNDAMENTALS.md)

**วัน:** 2 (Workshop) · **ระดับ:** Advanced / Capstone  
**ทักษะรวม:** Excel · Web Scout · Form round-trip · Error handling · Outlook Draft · Subflows

## อ้างอิง (Aug 2026)

| แหล่ง | URL |
|-------|-----|
| Web automation | [automation-web](https://learn.microsoft.com/power-automate/desktop-flows/automation-web) |
| Web actions | [actions-reference/webautomation](https://learn.microsoft.com/power-automate/desktop-flows/actions-reference/webautomation) |
| Handle errors | [desktop-flows/errors](https://learn.microsoft.com/power-automate/desktop-flows/errors) |
| Excel actions | [actions-reference/excel](https://learn.microsoft.com/power-automate/desktop-flows/actions-reference/excel) |

## Setup บนเครื่อง (ทำก่อนเปิด designer)

1. สร้างโฟลเดอร์ (คัดลอกได้):

```text
C:\PAD-Labs\working\lab10\
```

```text
C:\PAD-Labs\output\lab10\
```

```text
C:\PAD-Labs\logs\lab10\
```

2. คัดลอกไฟล์ใน [`assets/`](assets/) ไป:

```text
C:\PAD-Labs\working\lab10\
```

3. อ่าน brief: [`assets/mission-brief.md`](assets/mission-brief.md)
4. อ่าน pricing: [`assets/pricing-rules.md`](assets/pricing-rules.md) และตัวอย่าง [`assets/expected-pricing-examples.csv`](assets/expected-pricing-examples.csv)
5. เปิด Outlook Desktop อย่างน้อยหนึ่งครั้งให้มี profile พร้อมก่อนรัน flow

## Assets

| ไฟล์ | ใช้ทำอะไร |
|------|-----------|
| [`assets/leads.csv`](assets/leads.csv) / `leads.xlsx` | Input leads |
| [`assets/scout-targets.csv`](assets/scout-targets.csv) | รายการหน้าให้ scout |
| [`assets/recipients.csv`](assets/recipients.csv) | ผู้รับ Outlook จำลอง |
| [`assets/email-template.md`](assets/email-template.md) | โครง subject/body |
| [`assets/report-template.csv`](assets/report-template.csv) | โครงรายงาน |
| [`assets/pricing-rules.md`](assets/pricing-rules.md) | สูตรส่วนลด/ภาษี (ตรงสไลด์) |
| [`assets/expected-pricing-examples.csv`](assets/expected-pricing-examples.csv) | ตัวอย่างคำนวณตรวจมือ |
| [`assets/checklist.md`](assets/checklist.md) | เกณฑ์ส่งงาน |

## Web Scout Map

### ขั้นต่ำที่ต้องทำ

| ลำดับ | Phase 1 | URL | เก็บ |
|-------|---------|-----|------|
| 1 | 09 | https://ontoiq.tech/pad/09-ajax-table.html | ตารางออเดอร์ dynamic (เสริม) |
| 2 | **19** | https://ontoiq.tech/pad/19-catalog.html | **สินค้า + ราคา แบบ pagination (หลัก)** |
| 3 | 06 + 01 | Login แล้ว Forms | session + follow-up leads |

> Catalog: Loop Extract → Click `#btn-next-page` จน disabled (หน้า 3/3, รวม ~24 รายการ) — ใช้หน้า catalog บน Lab Hub

Login URL (คัดลอกได้):

```text
https://ontoiq.tech/pad/06-login.html
```

Username:

```text
demo
```

Password:

```text
demo
```

Form follow-up URL (คัดลอกได้):

```text
https://ontoiq.tech/pad/01-forms.html
```

### Phase 1 missions / challenges (เลือกให้ครบชุดที่ขาด)

| Mission | Phase 1 | URL | ระดับ |
|---------|---------|-----|--------|
| Files evidence | 05 | https://ontoiq.tech/pad/05-files.html | Mission — download/upload แล้วแนบหลักฐานเข้า report folder |
| Wizard VIP | 07 | https://ontoiq.tech/pad/07-wizard.html | Mission — lead `Priority=High` ใช้ Wizard แทน Forms |
| Iframe nest | 08 | https://ontoiq.tech/pad/08-iframe.html | Challenge |
| OCR invoice sniff | 10 | https://ontoiq.tech/pad/10-ocr.html | Challenge — เก็บค่าที่อ่านได้ลง Scout Notes |
| API pulse | 12 | https://ontoiq.tech/pad/12-api.html | Challenge — health/orders ลง Scout |

### Phase 2 challenges

| Mission | URL |
|---------|-----|
| Hover / Multi-select / Shadow / Popup | https://ontoiq.tech/pad/13-hover.html · [15](https://ontoiq.tech/pad/15-multiselect.html) · [16](https://ontoiq.tech/pad/16-shadow.html) · [18](https://ontoiq.tech/pad/18-popup.html) |

## Recommended Subflows

ดู [`shared/BEST-PRACTICES.md`](../../shared/BEST-PRACTICES.md)

| Subflow | หน้าที่ |
|---------|---------|
| `SF_InitPaths` | ตั้ง path, สร้างโฟลเดอร์ |
| `SF_ReadExcelSheet` | อ่าน leads |
| `SF_OpenLabHub` | launch/navigate |
| `SF_ScoutAjaxOrders` | extract AJAX |
| `SF_SubmitLeadForms` | Excel→Web→อัปเดตสถานะ |
| `SF_WriteExcelReport` | เขียน Results + Summary |
| `SF_SendOutlookDraft` | สร้าง Draft + attach |
| `SF_LogError` | เขียน log |

เกณฑ์แนะนำ: แยกอย่างน้อย **3 Subflows**

## Outlook Safety

- ใช้เฉพาะอีเมลใน `recipients.csv` (โดเมน `.mock.local`)
- Subject ขึ้นต้นด้วย `[PAD-LAB-MOCK]` — ดู code block ใน Step 8
- ค่า `SendMode=DraftOnly` — อย่าเปลี่ยนเป็น Send จริงในชั้นเรียนสาธารณะ

---

## Hands-on ทีละขั้น

### Step 0 — สร้าง flow และ Subflows

1. เปิด Power Automate for desktop → **New flow**
2. ชื่อ flow (คัดลอกได้):

```text
Lab10_CapstoneSalesOps
```

3. กด **Create**
4. สร้าง Subflows ตามตารางด้านบน (อย่างน้อย 3 ชื่อ)

> **กฎตัวแปรใน PAD (อ่านก่อนทำ Step ถัดไป)**  
> - ช่อง **Name** ของ **Set variable**, ชื่อ **produced variable**, และ **Store into** = พิมพ์ชื่ออย่างเดียว **ไม่มี `%`** เช่น `WorkingRoot`  
> - ช่องอื่นที่ต้องดึงค่าตัวแปร (Folder, File path, Text, …) = ใช้ `%WorkingRoot%` (**มี `%` ครบสองด้าน**)  
> - หลังสร้างแล้ว Variables pane อาจแสดงเป็น `%WorkingRoot%` — เป็นเรื่องปกติ

### Step 1 — SF_InitPaths

1. ลาก **Set variable** (Name ไม่มี `%`):
   - Name: `WorkingRoot` ← Value:

```text
C:\PAD-Labs\working\lab10
```

   - Name: `OutputRoot` ← Value:

```text
C:\PAD-Labs\output\lab10
```

   - Name: `LogPath` ← Value:

```text
C:\PAD-Labs\logs\lab10\capstone-error-log.csv
```

   - Name: `ReportPath` ← Value:

```text
C:\PAD-Labs\output\lab10\sales-ops-report.xlsx
```

   - Name: `SubmittedCount` ← Value:

```text
0
```

   - Name: `ScoutHitCount` ← Value:

```text
0
```

   - Name: `MailStatus` ← Value:

```text
Skipped
```

   - Name: `SendMode` ← Value:

```text
DraftOnly
```

2. **If folder exists** / **Create folder** สำหรับ output, logs, และโฟลเดอร์ evidence เช่น:

```text
%OutputRoot%\evidence
```

3. เขียน header log ที่ File path (คัดลอก):

```text
%LogPath%
```

   ด้วย **Write text to file**

ใน Main: **Run subflow** `SF_InitPaths`

### Step 2 — SF_ReadExcelSheet: อ่าน leads (+ targets)

1. **Launch Excel** → Document path (คัดลอก):

```text
%WorkingRoot%\leads.xlsx
```

   (หรือแปลงจาก CSV)
2. ชื่อ produced: `Excel` ← **ไม่ใส่ `%`** (อ้างอิงด้วย `%Excel%`)
3. **Read from Excel worksheet** sheet leads → ชื่อ produced: `Leads` ← **ไม่ใส่ `%`** (first line = column names; อ้างอิงด้วย `%Leads%`)
4. อ่าน `scout-targets.csv` / sheet ที่เกี่ยวข้องถ้ามี → ใช้เป็นรายการหน้า scout
5. เก็บ instance หรือ **Close Excel** ตามออกแบบ ก่อนเปิดรายงานใหม่ทีหลัง

### Step 3 — เปิด browser + Login (SF_OpenLabHub)

วางงานเสี่ยงภายใต้ **On block error** (ระดับชุดใหญ่) — เมื่อพังให้ **Run subflow** `SF_LogError` + **Get last error** แล้ว cleanup

1. **Launch new Microsoft Edge** หรือ **Launch new Chrome**
   - Initial URL: (คัดลอก)

```text
https://ontoiq.tech/pad/06-login.html
```

2. ชื่อ produced: `Browser` ← **ไม่ใส่ `%`** (อ้างอิงด้วย `%Browser%`)
3. **Wait for web page content**
4. **Populate text field on web page** `#txt-username` → Text (คัดลอก — username):

```text
demo
```

5. **Populate text field on web page** `#txt-password` → Text (คัดลอก — password):

```text
demo
```

6. **Press button on web page** → selector (คัดลอกได้):

```text
#btn-login
```

7. **Wait for web page content** จนเข้าสู่ session ได้

### Step 4 — Web Scout: AJAX + Catalog pagination (บังคับ)

**AJAX (09)**

1. **Go to web page** → URL (คัดลอก):

```text
https://ontoiq.tech/pad/09-ajax-table.html
```

2. **Wait for web page content** จนมีแถว
3. **Extract data from web page** (ใช้ **live web helper**) → append เข้า (คัดลอก):

```text
%ScoutResults%
```

   / ตารางออเดอร์  
   (ถ้ายังไม่มี: ชื่อ produced ของตาราง = `ScoutResults` ← **ไม่ใส่ `%`**)

**Catalog pagination (19) — ต้องมี**

1. **Go to web page** → URL (คัดลอก):

```text
https://ontoiq.tech/pad/19-catalog.html
```

2. **Wait for web page content** → selector (คัดลอกได้):

```text
#tbl-products
```

3. **Create new data table** → ชื่อ produced: `Products` ← **ไม่ใส่ `%`** (ถ้ายังไม่มี; อ้างอิงด้วย `%Products%`)
4. **Extract data from web page** ตาราง Product + Price → append เข้า (คัดลอก):

```text
%Products%
```

5. ลาก **Loop** / **Loop condition** ตราบที่ Next ยังใช้ได้:
   - **Click link on web page** หรือ **Press button on web page** → selector (คัดลอกได้):

```text
#btn-next-page
```

     หรือ

```text
[data-pad="page-next"]
```

   - **Wait for web page content** ตาราง
   - **Extract data from web page** ต่อ → append (คัดลอก):

```text
%Products%
```

6. เมื่อ Next **disabled** (หน้า 3/3, รวม ~24 รายการ) → ออกจากลูป
7. อัปเดตตัวนับ scout ตามเกณฑ์ที่ match criteria — อ้างอิง (คัดลอก):

```text
%ScoutHitCount%
```

Selectors คงที่:

```text
#tbl-products
```

```text
#btn-next-page
```

```text
#lbl-page
```

### Step 5 — Price engine (Discount + VAT)

ตาม [`assets/pricing-rules.md`](assets/pricing-rules.md) สำหรับแต่ละแถวที่มี Amount/ราคา:

1. ในลูปบน (คัดลอก):

```text
%Products%
```

   (หรือตารางที่ scout ได้):
   - ถ้า Amount >= (คัดลอก):

```text
15000
```

     → Name: `DiscountRate` ← Value:

```text
0.10
```

   - Else if Amount >= (คัดลอก):

```text
10000
```

     → Value:

```text
0.05
```

   - Else → Value:

```text
0.00
```

2. คำนวณด้วย **Set variable** / การคำนวณใน PAD (Name ไม่มี `%`; ตอนอ้างอิงใช้ `%...%`):
   - Name: `DiscountAmount` = Amount * DiscountRate
   - Name: `NetBeforeTax` = Amount - DiscountAmount
   - Name: `TaxAmount` = NetBeforeTax * (คัดลอกอัตรา VAT):

```text
0.07
```

   - Name: `GrandTotal` = NetBeforeTax + TaxAmount
3. สร้าง/เติม Data table ชื่อ produced: `Priced` ← **ไม่ใส่ `%`** ให้มีคอลัมน์ด้านบนครบ (อ้างอิงด้วย `%Priced%`)
4. รวมยอด Summary: Sum Amount, Sum Discount, Sum Tax, Sum GrandTotal
5. เทียบมือกับ [`assets/expected-pricing-examples.csv`](assets/expected-pricing-examples.csv) สำหรับเคสเดียวกัน

### Step 6 — SF_SubmitLeadForms: Excel → Web → อัปเดตสถานะ

1. **For each** → Value to iterate: (คัดลอก)

```text
%Leads%
```

   → Store into: `CurrentLead` ← **ไม่ใส่ `%`**
2. **If** Status Equal to (คัดลอก):

```text
New
```

   - **If** Priority Equal to (คัดลอก):

```text
High
```

     → **Go to web page** URL (คัดลอก):

```text
https://ontoiq.tech/pad/07-wizard.html
```

     ทำ Wizard ครบ (Mission VIP)
   - **Else** → **Go to web page** URL (คัดลอก):

```text
https://ontoiq.tech/pad/01-forms.html
```

     → **Populate text field on web page** + **Press button on web page**
3. อัปเดต Status / WebResult / SubmittedAt ของแถว
4. **Increase variable** เลือก `SubmittedCount` (ไม่มี `%`) เมื่อสำเร็จ
5. **End** For each

**Mission Files (05):** หลังมีผล scout/submit — ไป URL (คัดลอก):

```text
https://ontoiq.tech/pad/05-files.html
```

download/upload แล้วเก็บหลักฐานใต้:

```text
%OutputRoot%\evidence\
```

### Step 7 — SF_WriteExcelReport + นโยบายรันซ้ำ

1. ลาก **If file exists**
   - File path: (คัดลอก)

```text
%ReportPath%
```

2. **ภายใน If** → **Delete file** → (คัดลอก):

```text
%ReportPath%
```

3. **End**
4. **Launch Excel** (เอกสารใหม่) ถ้ายังไม่มี instance สำหรับรายงาน
5. **Write to Excel worksheet** อย่างน้อย sheet:
   - `Products` / `Scout` — ข้อมูลดิบ
   - `Priced` — หลังคำนวณ
   - `Results` — สถานะ leads
   - `Summary` — ยอดรวม + SubmittedCount + MailStatus
   - (แนะนำ) `Scout` notes จาก challenge
6. **Save document as** → (คัดลอก):

```text
%ReportPath%
```

7. ยังไม่ต้อง Close ถ้า Step 8 ต้องแนบไฟล์จาก path นี้ — หรือ Close แล้วแนบจาก disk ก็ได้

### Step 8 — SF_SendOutlookDraft (DraftOnly)

1. อ่านผู้รับจาก File path (คัดลอก):

```text
%WorkingRoot%\recipients.csv
```

   — ใช้เฉพาะโดเมน `.mock.local`
2. สร้างข้อความตาม [`assets/email-template.md`](assets/email-template.md)
   - Subject (คัดลอกโครง — แทนค่าตัวเลขจริงตอนรัน):

```text
[PAD-LAB-MOCK] Scout Ops Report — {SubmittedCount} follows-ups, {ScoutHitCount} scout hits
```

3. ใช้ Outlook actions ใน PAD สร้างข้อความใหม่ → บันทึกเป็น **Draft** (ไม่ Send)
4. Attach (คัดลอก):

```text
%ReportPath%
```

5. **Set variable** Name: `MailStatus` ← Value:

```text
DraftCreated
```

   ← **ไม่ใส่ `%` ใน Name**
6. ถ้า Outlook ไม่พร้อม: log แล้วตั้ง Name: `MailStatus` ← Value:

```text
Skipped
```

   — อย่า Send ออกนอก Lab

### Step 9 — Error log + Cleanup

ใน `SF_LogError` (เรียกจาก **On block error** / **On error**):

1. **Get last error** → ชื่อ produced: `LastError` ← **ไม่ใส่ `%`** (อ้างอิงด้วย `%LastError%`)
2. Append File path (คัดลอก):

```text
%LogPath%
```

   ด้วย (คัดลอก):

```text
%LastError.Message%
```

```text
%LastError.Location%
```

3. (แนะนำ) **Take screenshot of web page** ถ้า browser ยังเปิด

ท้าย Main (ทั้งกรณีสำเร็จและหลังกู้):

1. **Close Excel**
2. **Close web browser**
3. ปิด UI Outlook ถ้าเปิดค้างจากการสร้าง Draft

### Step 10 — รัน ตรวจ และรันซ้ำ

1. กด **Run**
2. เปิดรายงาน — มี Products/Scout, **Priced**, Summary (Discount/Tax/GrandTotal)
3. ตรวจเลข pricing กับตัวอย่าง
4. ตรวจ Draft ใน Outlook + ไฟล์แนบ
5. มี error log (อย่างน้อย header)
6. รันครั้งที่ 2 ด้วย path เดิม (คัดลอก):

```text
%ReportPath%
```

   — ต้องไม่พังเพราะชื่อไฟล์ซ้ำ

### Challenge (โบนัส)

- Iframe / OCR / API ตามตาราง Phase 1
- Phase 2: hover / multiselect / shadow / popup
- Contoso cross-check จาก Lab 07

---

## จุดที่มักทำผิด

| ผิด | ถูก |
|-----|-----|
| พิมพ์ `%Name%` ในช่อง Name / Store into / ชื่อ produced | ใช้ชื่อเปล่าไม่มี `%` เช่น `WorkingRoot`, `CurrentLead` |
| Catalog ดึงแค่หน้าแรก | Loop จน `#btn-next-page` disabled (~24 รายการ) |
| สูตรส่วนลด/ภาษีไม่ตรง pricing-rules | ทำตามอัตรา 10%/5%/0% + VAT 7% |
| Send อีเมลจริงในชั้นเรียน | `SendMode=DraftOnly` + subject `[PAD-LAB-MOCK]` |
| ไม่มี **On block error** / log | ครอบชุดเสี่ยง + **Get last error** + เขียน log |
| Save as รอบสองไม่ลบไฟล์เก่า | **If file exists** → **Delete file** ก่อน **Save document as** |
| ลืมปิด Excel/Browser | Cleanup ท้าย flow ทุกครั้ง |
| ผู้รับนอก `recipients.csv` | ใช้เฉพาะ `.mock.local` จากไฟล์ Lab |

---

## Variables (Contract)

| ชื่อตอนสร้าง (ไม่มี `%`) | ตอนอ้างอิง | Type | ความหมาย |
|--------------------------|------------|------|----------|
| `WorkingRoot` | `%WorkingRoot%` | Text | working path |
| `Leads` | `%Leads%` | Data table | จาก Excel |
| `ScoutResults` / `Products` / `Priced` | `%ScoutResults%` ฯลฯ | Data table | จาก Web / หลังคิดราคา |
| `ReportPath` | `%ReportPath%` | Text | ไฟล์รายงาน |
| `SubmittedCount` | `%SubmittedCount%` | Numeric | จำนวนที่ส่งฟอร์มสำเร็จ |
| `ScoutHitCount` | `%ScoutHitCount%` | Numeric | จำนวน scout ที่ match criteria |
| `LastError` | `%LastError%` | Error | จาก **Get last error** |
| `MailStatus` | `%MailStatus%` | Text | `DraftCreated` / `Skipped` / `Sent` |
| `Browser` / `Excel` | `%Browser%` / `%Excel%` | instances | ใช้ต่อเนื่องใน flow |
| `CurrentLead` | `%CurrentLead%` | Data row | แถว lead ในลูป |

## Expected Result

1. มี workbook รายงานใน output มีอย่างน้อย: Products/Scout, **Priced**, Summary (มียอด Discount/Tax/GrandTotal)  
2. ตัวเลขส่วนลด/ภาษีตรงตัวอย่างใน `expected-pricing-examples.csv` สำหรับเคสเดียวกัน  
3. Leads ที่เป็น `New` ถูกอัปเดตสถานะหลังเข้า Web  
4. มี Outlook **Draft** ตาม template (ยังไม่ต้องส่ง)  
5. มี error log แม้จะว่างเปล่า (header ก็ได้)

## Acceptance Criteria / Rubric

ตรงแนวสไลด์ Capstone Evaluation Matrix:

| เกณฑ์ | คะแนนแนวทาง |
|-------|--------------|
| Web Scraping — ดึงตารางครบ (≥2 แหล่ง หรือ multi-page) | ต้องมี |
| Excel Processing — ส่วนลด + ภาษีถูกต้อง | ต้องมี |
| Error Handling — **On block error** + log ไม่ crash ง่าย | ต้องมี |
| Output & Notification — ไฟล์รายงาน + Outlook Draft แนบไฟล์ | ต้องมี |
| **รันซ้ำได้** — รันครั้งที่ 2 ด้วย path Excel output เดิมโดยไม่ error ชื่อไฟล์ซ้ำ (**If file exists** → **Delete file** / เปิดเดิม+Save / timestamp) | ต้องมี |
| Login (06) + form/wizard round-trip | ต้องมี |
| Phase 1 Files (05) evidence | Mission |
| Subflows แยกชัด ≥ 3 | แนะนำ |
| Phase 1 challenge: Iframe / OCR / API | Challenge โบนัส |
| Advanced page (hover/shadow/popup) | Challenge โบนัส |
| Contoso cross-check | Challenge โบนัส — Lab 07 |
| Pagination จริงบน `19-catalog` | **ต้องมี** (หน้าพร้อมแล้ว) |

เช็กลิสต์เต็ม: [`assets/checklist.md`](assets/checklist.md)

## Troubleshooting

| อาการ | แก้ |
|-------|-----|
| Outlook action ไม่พบ profile | เปิด Outlook ก่อน แล้วใช้บัญชีเริ่มต้น |
| Attachment path ผิด | บันทึก report ก่อนสร้างอีเมล |
| AJAX ว่าง | **Wait for web page content** นานขึ้น / รอ element แถว |
| Excel lock | **Close Excel** + ปิดหน้าต่าง Excel |
| Save as รอบสองล้ม (ไฟล์ซ้ำ) | **If file exists** → **Delete file** ก่อน Save as — ดู Best Practices |
| Catalog ได้ไม่ครบ | ตรวจว่า Loop หยุดเมื่อ Next disabled ไม่ใช่หลังหน้าแรก |

## Cleanup

- ลบ Draft ทดสอบหลังตรวจ
- อย่า commit ไฟล์ output/logs จริงที่มีข้อมูลรันส่วนตัว

## อ้างอิงเพิ่ม

- Web UI: [https://ontoiq.tech/pad/](https://ontoiq.tech/pad/)
- Element UI / sample data: [Microsoft Learn PAD samples](https://github.com/MicrosoftDocs/mslearn-developer-tools-power-platform/tree/master/power-automate-desktop)
- Course outline PDF ที่ราก repo
