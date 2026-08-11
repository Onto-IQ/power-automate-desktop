# Lab 07 — Contoso Invoice Ops

**วัน:** 2 · **ระดับ:** Advanced · **เวลาโดยประมาณ:** อ่านความรู้ 25–35 นาที + Lab ~60 นาที (catch-up) / 90–120 นาที (สร้างมือ)  
**ทักษะ:** Desktop UI (Contoso), Excel ↔ Contoso, R1–R6, Subflows, On block error (SET-only) + Get last error

## ลำดับการเรียน (จับมือทำ)

| ขั้น | ไฟล์ | ทำอะไร |
|------|------|--------|
| 0 | [`shared/PAD-FUNDAMENTALS.md`](../../shared/PAD-FUNDAMENTALS.md) | พื้นฐาน PAD / กฎ `%` (ถ้ายังไม่คุ้น designer) |
| 1 | **[LESSON.md](LESSON.md)** | อ่านความรู้: Contoso UI, R1–R6, Actions |
| 2 | **[LAB.md](LAB.md)** | ติดตั้ง Contoso + Setup + Hands-on ทีละขั้น |


## Reference script (catch-up)

สำหรับนักเรียนที่ทำตามไม่ทัน — เปิด [`scripts/07-contoso-invoice-ops.robin`](scripts/07-contoso-invoice-ops.robin) แล้ว copy วางใน desktop flow ว่าง (เวอร์ชันย่อ ~1 ชม. ครบ R1–R6 + Contoso UI คอมเมนต์ไทย; มี ControlRepository ท้ายไฟล์)

## วัตถุประสงค์
- ติดตั้ง Contoso Invoicing แล้ว Launch จาก Flow
- Capture UI Elements ของฟอร์ม Invoice (ไม่พึ่งพิกัดจอ)
- อ่าน batch จาก Excel → สร้างใน Contoso ตามกฎ R1–R6 → เขียน Results/Summary

## Prerequisites

- PAD พร้อม Desktop UI automation (แนะนำ baseline **2607+**)
- Excel อ่าน/เขียน workbook
- Contoso Invoicing จาก zip ใน [LAB.md](LAB.md)
- แนะนำทำ Lab 06 มาก่อน

## Assets / Output

| | Path |
|--|------|
| Invoice batch | [`assets/invoices-batch.csv`](assets/invoices-batch.csv) |
| Business rules | [`assets/business-rules.md`](assets/business-rules.md) |
| UI map | [`assets/ui-map.md`](assets/ui-map.md) |
| Expected | [`assets/expected/expected-results.csv`](assets/expected/expected-results.csv) |
| Output | `C:\PAD-Labs\output\lab07\invoice-run-results.xlsx` |
| Log | `C:\PAD-Labs\logs\lab07\contoso-run-log.csv` |

## บทที่เกี่ยวข้อง

- ก่อนหน้า: [Lab 06 Excel & Data Tables](../06-excel-data-tables/README.md)
- ถัดไป: [Lab 08](../08-excel-web-roundtrip/README.md) · [Lab 09 Error Handling](../09-error-handling/README.md) (ทบทวน R6) · [Lab 10 Capstone](../10-capstone-sales-ops/README.md)
