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

2. **Create new data table** → `CatalogHits` (คอลัมน์ตามที่ extract ได้ เช่น Product, Price, …)
3. **Set variable** `MaxPages` ← `10` (safety)
4. **Set variable** `PageCount` ← `0`

### Step 1 — Launch

```text
https://pad.ontoiq.tech/pad/19-catalog.html
```

Variables produced: `Browser`

### Step 2 — Loop หน้า + Extract

1. **Loop** หรือ **Loop while** (เงื่อนไข เช่น `%PageCount% < %MaxPages%`)
2. ในลูป:
   - **Wait for web page content** · Contain element · ตาราง `#tbl-products` (Rename เป็น `Tbl_Products` ได้)
   - **Extract data from web page** → `PageTable`
   - **For each** `%PageTable%` → Insert เข้า `%CatalogHits%`
   - เพิ่ม `PageCount` += 1
   - หาปุ่ม **Next**:
     - ถ้ากดได้ → **Click** Next แล้ววนต่อ
     - ถ้า disabled / ไม่มี → **Exit loop**
3. **End** loop

เป้าหมาย: รวมแถวประมาณ **24** รายการ (ตามที่ hub ออกแบบ)

### Step 3 — เขียน CSV + ปิด

```text
C:\PAD-Labs\output\lab03\catalog-products.csv
```

**Close web browser** · `%Browser%`

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
| สับสนกับ 03-table | 03-table ไม่มี Next — Lab นี้อยู่บน 19-catalog |

## Cleanup

ปิดเบราว์เซอร์ค้าง
