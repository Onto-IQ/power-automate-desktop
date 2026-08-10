# Lab 03 — Static Table

**วัน:** 1 · **ระดับ:** Intermediate · **เวลาโดยประมาณ:** อ่าน 10–15 นาที + Lab 25–35 นาที  
**ทักษะ:** Wait for web page content, Extract HTML table, For each, Write CSV  
**Flow ชื่อ:** `Lab03_StaticTable`  
**สถานะ:** Core

## ลำดับการเรียน

| ขั้น | ไฟล์ | ทำอะไร |
|------|------|--------|
| 0 | [`shared/PAD-FUNDAMENTALS.md`](../../../shared/PAD-FUNDAMENTALS.md) | กฎ `%` |
| 1 | **[LESSON.md](LESSON.md)** | ตาราง static หน้าเดียว |
| 2 | **[LAB.md](LAB.md)** | Hands-on |


## Reference script (catch-up)

สำหรับนักเรียนที่ทำตามไม่ทัน — เปิด [`scripts/03-static-table.robin`](scripts/03-static-table.robin) แล้ว copy วางใน desktop flow ว่าง

- partial-ui
- ไม่แทนการทำ LAB หลัก; ใช้เทียบลำดับ action / กู้งานให้ทันชั้น

## วัตถุประสงค์
- เปิด [03-table](https://pad.ontoiq.tech/pad/03-table.html) แล้ว Wait + Extract ตาราง `#tbl-employees`
- เข้าใจว่าหน้านี้**ไม่มี** pagination (ไม่มี Prev/Next)
- วนแถวด้วย For each แล้วเขียน CSV

## Prerequisites

- PAD + browser extension (แนะนำ **2607+**)
- เข้า [Lab Hub](https://pad.ontoiq.tech/pad/) ได้

## Assets / Output

| | Path |
|--|------|
| Web | https://pad.ontoiq.tech/pad/03-table.html |
| Output | `C:\PAD-Labs\output\lab03\static-table.csv` |

## บทที่เกี่ยวข้อง

- แผนที่ Lab 03: [03 Web Scout index](../README.md)
- AJAX (Core): [Lab 03 Ajax Table](../ajax-table/README.md)
- Catalog หลายหน้า (Optional): [Lab 03 Catalog](../catalog/README.md)
