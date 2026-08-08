# Lab Hub — รายการที่ควรเพิ่มบนเว็บ

แหล่งปัจจุบัน: [https://ontoiq.tech/pad/](https://ontoiq.tech/pad/)

## สถานะล่าสุด (ตรวจแล้ว)

| รายการ | สถานะ |
|--------|--------|
| [`19-catalog.html`](https://ontoiq.tech/pad/19-catalog.html) | **พร้อมใช้** |
| Hub index ลิงก์โมดูล 19 | **มี** |
| `GET /pad/api/products?page=&pageSize=` | **พร้อมใช้** |

### Acceptance ของหน้า catalog

- [x] เปิดบน `https://ontoiq.tech/pad/19-catalog.html` ได้
- [x] มีอย่างน้อย 3 หน้า (`totalPages=3`, หน้าละ 8 รายการ, รวม 24)
- [x] Product + Price ในตาราง (`#tbl-products`, `[data-pad="col-product"]`, `[data-pad="col-price"]`)
- [x] ปุ่ม Next คงที่: `#btn-next-page`, `[data-pad="page-next"]` (+ Prev / page label)
- [x] หน้าสุดท้าย Next disabled (`hasNext=false` ฝั่ง API; UI ระบุ disabled)
- [x] ลิงก์จาก Hub index

### Selectors ที่ใช้ใน PAD

```text
#tbl-products
#btn-prev-page
#btn-next-page
#lbl-page
[data-pad="page-next"]
[data-pad="col-product"]
[data-pad="col-price"]
```

### API ตัวอย่าง

```http
GET https://ontoiq.tech/pad/api/products?page=1&pageSize=8
```

Response มี `products`, `page`, `pageSize`, `total`, `totalPages`, `hasNext`, `hasPrev`

## ใช้ใน Lab Kit

| Lab | การใช้ |
|-----|--------|
| Lab 03 Mission P | Loop Extract → Click Next จน disabled |
| Lab 10 Capstone | แหล่งสินค้าหลักสำหรับส่วนลด/ภาษี |
| Lab 12 / API challenge | เรียก `/pad/api/products` โดยตรงได้ |

## ไม่จำเป็นต้องแก้เว็บเพิ่มสำหรับช่องว่างสไลด์อื่น

| ช่องว่าง | ทำที่ |
|----------|------|
| Notepad / Calculator | Lab 01b |
| Excel Macro | Lab 06 + VBA |
| Capstone ส่วนลด/ภาษี | Lab 10 `pricing-rules.md` |
