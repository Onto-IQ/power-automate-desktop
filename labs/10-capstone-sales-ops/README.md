# Lab 10 — Capstone: Web Scout & Sales Operations

**วัน:** 2 (Workshop) · **ระดับ:** Advanced / Capstone  
**ทักษะรวม:** Excel · Web Scout · Form round-trip · Error handling · Outlook Draft · Subflows

## เรื่องราว (สนุก)

คุณคือทีม **Onto Scout Ops**  
ภารกิจ: อ่าน leads จาก Excel → สอดแนม Lab Hub หาสัญญาณออเดอร์ → กรอกฟอร์มติดตาม → เขียนรายงานกลับ Excel → สร้างอีเมล Outlook **Draft** แนบรายงานส่งให้ทีมจำลอง

> ส่งอีเมลจริงเฉพาะเมื่อวิทยากรอนุญาต — ค่าเริ่มต้นของ Lab นี้คือ **DraftOnly**

## วัตถุประสงค์

1. อ่าน lead/product criteria จาก Excel → Data table  
2. Web Scout หลายแหล่ง/หลายหน้า (อย่างน้อย table + AJAX; pagination จริงเมื่อมีหน้า catalog)  
3. **คำนวณส่วนลดและภาษีใน Excel** ตาม [`assets/pricing-rules.md`](assets/pricing-rules.md)  
4. Excel → Web form → เขียนผลกลับ Excel  
5. สร้าง Outlook message สนุกแต่สุภาพ พร้อมแนบ report  
6. ครอบ error handling + logging

## Prerequisites

- ผ่านแนวคิด Lab 03, 06, 08, 09 (แนะนำให้ผ่าน Lab 07 Contoso ด้วย ถ้าต้องการ Challenge Desktop+Web)
- Excel + Outlook Desktop
- เข้าถึง [PAD Lab Hub](https://ontoiq.tech/pad/)

## Setup

1. Flow ชื่อ `Lab10_CapstoneSalesOps`
2. คัดลอกไฟล์ใน [`assets/`](assets/) ไป `C:\PAD-Labs\working\lab10\`
3. สร้าง `C:\PAD-Labs\output\lab10\` และ `C:\PAD-Labs\logs\lab10\`
4. อ่าน brief: [`assets/mission-brief.md`](assets/mission-brief.md)

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

> Catalog: Loop Extract → Click `#btn-next-page` จน disabled (หน้า 3/3, รวม ~24 รายการ) — รายละเอียดใน [`shared/WEB-HUB-REQUESTS.md`](../../shared/WEB-HUB-REQUESTS.md)

Login: https://ontoiq.tech/pad/06-login.html (`demo`/`demo`)  
Form follow-up: https://ontoiq.tech/pad/01-forms.html

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

## PAD Action Sequence (ภาพรวม)

```text
InitPaths
→ Read leads + scout targets
→ Try
    → Open browser (+ login)
    → Scout pages → %ScoutResults% / %Products%
    → Price engine: Discount + VAT → sheet Priced + Summary totals
    → For each New lead → submit form/wizard → update status
    → Write report workbook (Products, Priced, Results, Summary, Scout)
    → Create Outlook Draft (attach report)
→ On error → LogError (+ screenshot)
→ Cleanup close Excel/Browser/Outlook UI ถ้าเปิด
```

## Variables (Contract)

| Variable | Type | ความหมาย |
|----------|------|----------|
| `%WorkingRoot%` | Text | working path |
| `%Leads%` | Data table | จาก Excel |
| `%ScoutResults%` | Data table | จาก Web |
| `%ReportPath%` | Text | ไฟล์รายงาน |
| `%SubmittedCount%` | Numeric | จำนวนที่ส่งฟอร์มสำเร็จ |
| `%ScoutHitCount%` | Numeric | จำนวน scout ที่ match criteria |
| `%LastError%` | Text | error ล่าสุด |
| `%MailStatus%` | Text | `DraftCreated` / `Skipped` / `Sent` |

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
| Error Handling — On-block error + log ไม่ crash ง่าย | ต้องมี |
| Output & Notification — ไฟล์รายงาน + Outlook Draft แนบไฟล์ | ต้องมี |
| Login (06) + form/wizard round-trip | ต้องมี |
| Phase 1 Files (05) evidence | Mission |
| Subflows แยกชัด ≥ 3 | แนะนำ |
| Phase 1 challenge: Iframe / OCR / API | Challenge โบนัส |
| Advanced page (hover/shadow/popup) | Challenge โบนัส |
| Contoso cross-check | Challenge โบนัส — Lab 07 |
| Pagination จริงบน `19-catalog` | **ต้องมี** (หน้าพร้อมแล้ว) |

เช็กลิสต์เต็ม: [`assets/checklist.md`](assets/checklist.md)

## Outlook Safety

- ใช้เฉพาะอีเมลใน `recipients.csv` (โดเมน `.mock.local`)
- Subject ขึ้นต้นด้วย `[PAD-LAB-MOCK]`
- ค่า `SendMode=DraftOnly` — อย่าเปลี่ยนเป็น Send จริงในชั้นเรียนสาธารณะ

## Troubleshooting

| อาการ | แก้ |
|-------|-----|
| Outlook action ไม่พบ profile | เปิด Outlook ก่อน แล้วใช้บัญชีเริ่มต้น |
| Attachment path ผิด | บันทึก report ก่อนสร้างอีเมล |
| AJAX ว่าง | Wait นานขึ้น / รอ element แถว |
| Excel lock | Close instance + ปิดหน้าต่าง Excel |

## Cleanup

- ลบ Draft ทดสอบหลังตรวจ
- อย่า commit ไฟล์ output/logs จริงที่มีข้อมูลรันส่วนตัว

## อ้างอิง

- Web UI: [https://ontoiq.tech/pad/](https://ontoiq.tech/pad/)
- Element UI / sample data: [Microsoft Learn PAD samples](https://github.com/MicrosoftDocs/mslearn-developer-tools-power-platform/tree/master/power-automate-desktop)
- Course outline PDF ที่ราก repo
