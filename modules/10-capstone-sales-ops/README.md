# Lab 10 — Capstone: Web Scout & Sales Operations

**วัน:** 2 (Workshop) · **ระดับ:** Advanced / Capstone · **เวลาโดยประมาณ:** อ่านความรู้ 25–35 นาที + Lab 120–180 นาที  
**ทักษะรวม:** Excel · Web Scout · Pricing · Form round-trip · Error handling · Outlook Draft · Subflows

## ลำดับการเรียน (จับมือทำ)

| ขั้น | ไฟล์ | ทำอะไร |
|------|------|--------|
| 0 | [`shared/PAD-FUNDAMENTALS.md`](../../shared/PAD-FUNDAMENTALS.md) | พื้นฐาน PAD / กฎ `%` (ถ้ายังไม่คุ้น designer) |
| 1 | **[LESSON.md](LESSON.md)** | อ่านความรู้: Scout Ops story, pricing, DraftOnly |
| 2 | **[LAB.md](LAB.md)** | Setup + Hands-on ตาม Rubric / checklist |

## วัตถุประสงค์

- Scout Lab Hub (AJAX + catalog pagination) แล้วคิดส่วนลด/VAT ใน Excel
- Round-trip leads (Login → Forms/Wizard) แล้วเขียนรายงานครบ sheet
- สร้าง Outlook **Draft** แนบรายงาน (`SendMode=DraftOnly`) พร้อม error log

## Prerequisites

- ผ่านแนวคิด Lab 03, 06, 08, 09 (แนะนำ Lab 07 ถ้าทำ Challenge Contoso)
- Excel + Outlook Desktop
- เข้าถึง [PAD Lab Hub](https://ontoiq.tech/pad/)
- PAD baseline แนะนำ **2607+**

## Assets / Output

| | Path |
|--|------|
| Mission / Pricing | [`assets/mission-brief.md`](assets/mission-brief.md) · [`assets/pricing-rules.md`](assets/pricing-rules.md) |
| Leads / targets | [`assets/leads.csv`](assets/leads.csv) · [`assets/scout-targets.csv`](assets/scout-targets.csv) |
| Recipients / email | [`assets/recipients.csv`](assets/recipients.csv) · [`assets/email-template.md`](assets/email-template.md) |
| Checklist | [`assets/checklist.md`](assets/checklist.md) |
| Report output | `C:\PAD-Labs\output\lab10\sales-ops-report.xlsx` |
| Error log | `C:\PAD-Labs\logs\lab10\capstone-error-log.csv` |

## บทที่เกี่ยวข้อง

- Round-trip: [Lab 08](../08-excel-web-roundtrip/README.md) · Error: [Lab 09](../09-error-handling/README.md)
- Desktop (Challenge): [Lab 07 Contoso](../07-contoso-invoice-ops/README.md)
- Best practices: [`shared/BEST-PRACTICES.md`](../../shared/BEST-PRACTICES.md)
