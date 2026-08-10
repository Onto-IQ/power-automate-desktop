# Lab 03 — Catalog (Pagination)

**วัน:** 1 · **ระดับ:** Intermediate · **เวลาโดยประมาณ:** อ่าน 10–15 นาที + Lab 30–40 นาที  
**ทักษะ:** Loop Next + Extract ตารางหลายหน้า  
**Flow ชื่อ:** `Lab03_Catalog`  
**สถานะ:** Optional (pagination)

## ลำดับการเรียน

| ขั้น | ไฟล์ | ทำอะไร |
|------|------|--------|
| 1 | **[LESSON.md](LESSON.md)** | Pagination vs static |
| 2 | **[LAB.md](LAB.md)** | Hands-on |


## Reference script (catch-up)

สำหรับนักเรียนที่ทำตามไม่ทัน — เปิด [`scripts/03-catalog.robin`](scripts/03-catalog.robin) แล้ว copy วางใน desktop flow ว่าง

- partial-ui — Chrome + bundled `Lab03 Catalog` (`Tbl_Products`, `Btn_NextPage`)
- ไม่แทนการทำ LAB หลัก; ใช้เทียบลำดับ action / กู้งานให้ทันชั้น

## วัตถุประสงค์
- เปิด [19-catalog](https://pad.ontoiq.tech/pad/19-catalog.html)
- Extract `#tbl-products` แล้วกด **Next** วนจนได้ประมาณ 24 รายการ
- เขียน CSV รวมทุกหน้า

## Prerequisites

- ทำ [Lab 03 Static Table](../static-table/README.md) ก่อน (เข้าใจ Extract หน้าเดียว)

## Assets / Output

| | Path |
|--|------|
| Web | https://pad.ontoiq.tech/pad/19-catalog.html |
| Output | `C:\PAD-Labs\output\lab03\catalog-products.csv` |

## บทที่เกี่ยวข้อง

- [03 Web Scout index](../README.md)
- Static (ไม่มี Next): [Lab 03 Static Table](../static-table/README.md)
