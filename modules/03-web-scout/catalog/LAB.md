# Lab 03 — Catalog (Hands-on)

**อ่านก่อน:** [LESSON.md](LESSON.md) · **หน้าปก:** [README.md](README.md)

**Flow ชื่อ:** `Lab03_Catalog` · **Optional**

## Setup

```text
C:\PAD-Labs\output\lab03\
```

## Hands-on

### Step 0 — สร้าง flow + ตัวแปรช่วย

1. **New flow** → ชื่อ:

```text
Lab03_Catalog
```

2. **Create new data table** → `CatalogHits` · คอลัมน์: SKU, Product, Price, Category
3. **Set variable** `MaxPages` ← `10` (safety)
4. **Set variable** `PageCount` ← `0`

### Step 1 — Launch

1. **Launch** Edge/Chrome · Initial URL:

```text
https://pad.ontoiq.tech/pad/19-catalog.html
```

2. Variables produced: `Browser`

### Step 2 — Loop หน้า + Extract

1. **Loop** หรือ **Loop while** (เงื่อนไข เช่น `%PageCount% < %MaxPages%`)
2. ในลูป: **Wait for web page content** · Contain element · ตาราง `#tbl-products` (Rename เป็น `Tbl_Products` ได้)
3. ให้หน้ายังอยู่ที่ [19-catalog](https://pad.ontoiq.tech/pad/19-catalog.html) (หลังกด Next แล้วยังต้องเป็นหน้านี้)
4. **Extract data from web page** · Browser: `%Browser%`
5. PAD จะเปิด **live web helper** บนหน้านั้น
6. ชี้ `#tbl-products`
7. **คลิกขวา** บนตาราง/เซลล์ในตาราง
8. เลือก **Extract Entire HTML Table** · Variables produced: `PageTable`
9. รอบแรกตั้งค่า helper · รอบถัดไปใช้ extract เดิมบนตารางหน้าปัจจุบัน
10. ลาก **For each** · Value to iterate: (คัดลอก)

```text
%PageTable%
```

11. Store into: `ProductRow` ← **ไม่ใส่ `%`**
12. **ภายใน For each** ลาก **Insert row into data table**
13. ตั้งค่าตาม UI (มี 3 ช่องหลัก):
    - **Data table:** (คัดลอก)

```text
%CatalogHits%
```

    - **Into location:** **End of data table**
    - **New value(s):** ถ้าคอลัมน์ตรงกัน ใช้ (คัดลอก):

```text
%ProductRow%
```

    - หรือใส่เป็น list (**ห้ามซ้อน `%` ข้างใน**):

```text
%[ProductRow['SKU'], ProductRow['Product'], ProductRow['Price'], ProductRow['Category']]%
```
14. **End** For each
15. เพิ่ม `PageCount` += 1
16. หาปุ่ม **Next**
17. ถ้ากดได้ → **Click** Next แล้ววนต่อ
18. ถ้า disabled / ไม่มี → **Exit loop**
19. **End** loop

เป้าหมาย: รวมแถวประมาณ **24** รายการ (ตามที่ hub ออกแบบ)

### Step 3 — เขียน CSV + ปิด

1. เขียนผลเป็น:

```text
C:\PAD-Labs\output\lab03\catalog-products.csv
```

2. **Close web browser** · `%Browser%`

### Step 4 — Replay

รัน 2 ครั้ง · ตรวจจำนวนแถวใน CSV

## Acceptance

- [ ] Flow ชื่อ `Lab03_Catalog`
- [ ] มีการกด Next อย่างน้อยหนึ่งครั้ง (ถ้ามีหลายหน้า)
- [ ] CSV มีแถวรวมหลายหน้า (~24)
- [ ] มี MaxPages / เงื่อนไขหยุด
- [ ] ปิดเบราว์เซอร์ท้าย flow

## Troubleshooting

| อาการ | แก้ |
|-------|-----|
| ได้แค่หน้าแรก | ตรวจว่ามี Click Next + Wait หลังเปลี่ยนหน้า |
| วนไม่จบ | ใช้ MaxPages + Exit เมื่อ Next ใช้ไม่ได้ |
| หาคอลัมน์ Product ในรายการตัวแปรไม่เจอ | พิมพ์/วาง `%ProductRow['Product']%` เอง |
| สับสนกับ 03-table | 03-table ไม่มี Next — Lab นี้อยู่บน 19-catalog |

## Cleanup

ปิดเบราว์เซอร์ค้าง
