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

### Step 1b — เก็บ UI element ปุ่ม Next (ทำก่อนลูป)

1. เปิดแผง **UI Elements** → **Add UI element** (หรือ Add element) ด้วย UI Picker
2. ชี้ปุ่ม **Next** บนหน้า (`#btn-next-page`)
3. **Save** แล้ว Rename เป็น:

```text
Btn_NextPage
```

4. (ทางเลือก) เก็บตาราง `#tbl-products` แล้ว Rename เป็น `Tbl_Products` — ใช้กับ Wait ในลูปได้

อย่าข้ามขั้นนี้ — ในลูปต้องอ้าง `Btn_NextPage` ไม่ใช่ไปหาปุ่มใหม่ทุกครั้ง

### Step 2 — Loop หน้า + Extract

> **Tip:** มีลูปซ้อนกัน — **Loop condition** = วน **หน้า** · **For each** (ข้างใน) = วน **แถว** ของหน้าปัจจุบัน อย่าสลับบทบาท

1. **Loop condition** (First operand / Operator / Second operand — เช่น `%PageCount%` · **Less than (<)** · `%MaxPages%`)
2. ในลูป: **Wait for web page content** · Contain element · ตาราง `#tbl-products` / `Tbl_Products`
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
13. ตั้งค่า 3 ช่องให้ตรงนี้เท่านั้น:

| ช่องใน UI | ใส่ค่า |
|-----------|--------|
| **Data table** | `%CatalogHits%` (กด `{x}` เลือก `CatalogHits`) |
| **Into location** | **End of data table** |
| **New value(s)** | `%ProductRow%` (กด `{x}` เลือก `ProductRow`) ถ้าคอลัมน์ตรงกัน |

คัดลอกวาง Data table:

```text
%CatalogHits%
```

คัดลอกวาง New value(s):

```text
%ProductRow%
```

หรือใส่เป็น list (**ห้ามซ้อน `%` ข้างใน**) — คัดลอก:

```text
%[ProductRow['SKU'], ProductRow['Product'], ProductRow['Price'], ProductRow['Category']]%
```
14. **End** For each
15. **Increase variable** — **Variable name:** `%PageCount%` · **Increase by:** `1`
   (ตาม [Variables actions](https://learn.microsoft.com/power-automate/desktop-flows/actions-reference/variables#increase-variable))
16. ตรวจปุ่ม **Next** (`Btn_NextPage`) — ถ้ายังกดได้ → **Press button on web page** (หรือ **Click link on web page**) · UI element: `Btn_NextPage` · Browser: `%Browser%` แล้ววนต่อ
17. ถ้า disabled / กดไม่ได้ → **Exit loop**
18. **End** loop

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
- [ ] มี UI element `Btn_NextPage` (เก็บก่อนเข้าลูป)
- [ ] มีการกด Next อย่างน้อยหนึ่งครั้ง (ถ้ามีหลายหน้า)
- [ ] CSV มีแถวรวมหลายหน้า (~24)
- [ ] มี MaxPages / เงื่อนไขหยุด
- [ ] ปิดเบราว์เซอร์ท้าย flow

## Troubleshooting

| อาการ | แก้ |
|-------|-----|
| กด Next ไม่ได้ / หาปุ่มไม่เจอ | ทำ Step 1b ก่อน — Add UI element แล้ว Rename `Btn_NextPage` |
| ได้แค่หน้าแรก | ตรวจว่ามี Press/Click `Btn_NextPage` + Wait หลังเปลี่ยนหน้า |
| วนไม่จบ | ใช้ MaxPages + Exit เมื่อ Next disabled |
| หาคอลัมน์ Product ในรายการตัวแปรไม่เจอ | พิมพ์/วาง `%ProductRow['Product']%` เอง |
| สับสนกับ 03-table | 03-table ไม่มี Next — Lab นี้อยู่บน 19-catalog |

## Cleanup

ปิดเบราว์เซอร์ค้าง
