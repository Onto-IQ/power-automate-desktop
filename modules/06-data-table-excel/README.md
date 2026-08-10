# Lab 06 — Data Table & Excel

**วัน:** 2 · **ระดับ:** Intermediate · **เวลาโดยประมาณ:** อ่านความรู้ 15–25 นาที + Lab 50–70 นาที  
**ทักษะ:** Launch Excel, Read/Write worksheet, Data table filter/sort/aggregate, **Run Excel macro**

## ลำดับการเรียน (จับมือทำ)

| ขั้น | ไฟล์ | ทำอะไร |
|------|------|--------|
| 0 | [`shared/PAD-FUNDAMENTALS.md`](../../shared/PAD-FUNDAMENTALS.md) | พื้นฐาน PAD / กฎ `%` (ถ้ายังไม่คุ้น designer) |
| 1 | **[LESSON.md](LESSON.md)** | อ่านความรู้: Excel instance, กรอง, Tier, macro |
| 2 | **[LAB.md](LAB.md)** | Setup + Hands-on ทีละขั้นใน designer |


## Reference script (catch-up)

สำหรับนักเรียนที่ทำตามไม่ทัน — เปิด [`scripts/06-data-table-excel.robin`](scripts/06-data-table-excel.robin) แล้ว copy วางใน desktop flow ว่าง

- full — ต้องมี sales-report.xlsm + macro
- ไม่แทนการทำ LAB หลัก; ใช้เทียบลำดับ action / กู้งานให้ทันชั้น

## วัตถุประสงค์
- อ่าน Excel เป็น Data table
- แปลงข้อมูล (เพิ่มคอลัมน์, กรอง, สรุป)
- เขียนผลกลับเป็น sheet ใหม่
- รัน Excel Macro จัดฟอร์แมตรายงาน (Mission M)

## Prerequisites

- PAD ติดตั้งแล้ว (แนะนำ baseline **2607+** — ดู [PAD version matrix](https://learn.microsoft.com/power-platform/released-versions/power-automate-desktop))
- Microsoft Excel บนเครื่อง
- ทำ Lab ที่เกี่ยวกับ Excel/Data table มาก่อนจะช่วยให้ลื่นขึ้น

## Assets / Output

| | Path |
|--|------|
| Input workbook | [`assets/orders-input.xlsx`](assets/orders-input.xlsx) / CSV สำรอง |
| Macro source | [`assets/vba/FormatSummary.bas`](assets/vba/FormatSummary.bas) |
| Macro howto | [`assets/vba/README.md`](assets/vba/README.md) |
| Expected summary | [`assets/expected-summary.csv`](assets/expected-summary.csv) |
| Output | `C:\PAD-Labs\output\lab06\orders-report.xlsm` |

## บทที่เกี่ยวข้อง

- เงื่อนไข: [Lab 04 Conditional](../04-conditional-automation/README.md)
- ลูป / Data table: [Lab 05 Looping](../05-looping-files-data/README.md)
- Schema Orders: [`shared/DATA-SCHEMAS.md`](../../shared/DATA-SCHEMAS.md)
