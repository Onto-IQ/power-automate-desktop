# Lab 08 — Excel ↔ Web Round-trip

**วัน:** 2 · **ระดับ:** Intermediate–Advanced · **เวลาโดยประมาณ:** อ่านความรู้ 15–25 นาที + Lab 60–90 นาที  
**ทักษะ:** Excel → Web → Excel, Lab Hub Login/Forms/Wizard, For each

## ลำดับการเรียน (จับมือทำ)

| ขั้น | ไฟล์ | ทำอะไร |
|------|------|--------|
| 0 | [`shared/PAD-FUNDAMENTALS.md`](../../shared/PAD-FUNDAMENTALS.md) | พื้นฐาน PAD / กฎ `%` (ถ้ายังไม่คุ้น designer) |
| 1 | **[LESSON.md](LESSON.md)** | อ่านความรู้: round-trip, Mission W, Actions |
| 2 | **[LAB.md](LAB.md)** | Setup + Hands-on ทีละขั้นใน designer |


## Reference script (catch-up)

สำหรับนักเรียนที่ทำตามไม่ทัน — เปิด [`scripts/08-excel-web-roundtrip.robin`](scripts/08-excel-web-roundtrip.robin) แล้ว copy วางใน desktop flow ว่าง

- partial-ui — rebind web + Excel
- ไม่แทนการทำ LAB หลัก; ใช้เทียบลำดับ action / กู้งานให้ทันชั้น

## วัตถุประสงค์
- สร้าง Flow ธุรกิจสั้น: **Excel → Web → Excel**
- Login Lab Hub แล้วกรอกฟอร์ม/ Wizard จากแต่ละแถว Lead
- อัปเดตคอลัมน์ Status / WebResult กลับ workbook output

## Prerequisites

- PAD + browser extension (แนะนำ baseline **2607+**)
- Microsoft Excel
- เข้าถึง [PAD Lab Hub](https://ontoiq.tech/pad/)
- แนะนำทำ [Lab 03 Static/AJAX](../03-web-scout/README.md) / Lab 06 มาก่อน

## Assets / Output

| | Path |
|--|------|
| Leads input | [`assets/leads-input.csv`](assets/leads-input.csv) |
| Output template | [`assets/leads-output-template.csv`](assets/leads-output-template.csv) |
| Files proof | [`assets/roundtrip-proof.txt`](assets/roundtrip-proof.txt) |
| Schema | [`shared/DATA-SCHEMAS.md`](../../shared/DATA-SCHEMAS.md) |
| Your output | `C:\PAD-Labs\output\lab08\leads-output.xlsx` |

## บทที่เกี่ยวข้อง

- Web พื้นฐาน: [Lab 03 index](../03-web-scout/README.md) · Excel: [Lab 06](../06-data-table-excel/README.md)
- Desktop คู่ขนาน: [Lab 07 Contoso](../07-contoso-invoice-ops/README.md)
- ใช้ต่อใน Capstone: [Lab 10](../10-capstone-sales-ops/README.md)
