# Lab 03 — AJAX Table

**วัน:** 1 · **ระดับ:** Intermediate · **เวลาโดยประมาณ:** อ่าน 10–15 นาที + Lab 25–35 นาที  
**ทักษะ:** Wait for dynamic rows, Extract, If กรอง criteria, Write CSV  
**Flow ชื่อ:** `Lab03_AjaxTable`  
**สถานะ:** Core

## ลำดับการเรียน

| ขั้น | ไฟล์ | ทำอะไร |
|------|------|--------|
| 0 | [`shared/PAD-FUNDAMENTALS.md`](../../../shared/PAD-FUNDAMENTALS.md) | กฎ `%` |
| 1 | **[LESSON.md](LESSON.md)** | AJAX vs static |
| 2 | **[LAB.md](LAB.md)** | Hands-on |


## Reference script (catch-up)

สำหรับนักเรียนที่ทำตามไม่ทัน — เปิด [`scripts/03-ajax-table.robin`](scripts/03-ajax-table.robin) แล้ว copy วางใน desktop flow ว่าง

- partial-ui — Chrome + bundled `Lab03 Ajax` (`Btn_RefreshOrders`, `Tbl_Orders`)
- ไม่แทนการทำ LAB หลัก; ใช้เทียบลำดับ action / กู้งานให้ทันชั้น

## วัตถุประสงค์
- เปิด [09-ajax-table](https://pad.ontoiq.tech/pad/09-ajax-table.html) แล้ว **Wait จนมีแถว** ก่อน Extract
- กรองตาม criteria (`MinAmount=1500`) แล้วเขียน CSV
- แยกจาก static หน้าเดียว และ catalog pagination

## Prerequisites

- PAD + browser extension
- แนะนำทำ [Lab 03 Static Table](../static-table/README.md) ก่อน

## Assets / Output

| | Path |
|--|------|
| Criteria | [`assets/scout-criteria.csv`](assets/scout-criteria.csv) |
| Web | https://pad.ontoiq.tech/pad/09-ajax-table.html |
| Output | `C:\PAD-Labs\output\lab03\ajax-orders.csv` |

## บทที่เกี่ยวข้อง

- [03 Web Scout index](../README.md)
- Static: [Lab 03 Static Table](../static-table/README.md)
- Catalog pagination: [Lab 03 Catalog](../catalog/README.md)
