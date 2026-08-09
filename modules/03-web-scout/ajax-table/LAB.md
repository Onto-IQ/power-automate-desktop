# Lab 03 — AJAX Table (Hands-on)

**อ่านก่อน:** [LESSON.md](LESSON.md) · **หน้าปก:** [README.md](README.md) · **พื้นฐาน:** [`shared/PAD-FUNDAMENTALS.md`](../../../shared/PAD-FUNDAMENTALS.md)

**Flow ชื่อ:** `Lab03_AjaxTable` · **Core**

## Setup

```text
C:\PAD-Labs\output\lab03\
```

อ่าน [`assets/scout-criteria.csv`](assets/scout-criteria.csv): `MinAmount=10000`, `TargetRegion=BKK`

## Hands-on

### Step 0 — สร้าง flow + criteria

1. **New flow** → ชื่อ:

```text
Lab03_AjaxTable
```

2. **Set variable** Name `MinAmount` ← Value:

```text
10000
```

3. **Set variable** Name `TargetRegion` ← Value:

```text
BKK
```

4. (แนะนำ) **Create new data table** → Variables produced: `Hits`
5. คอลัมน์อย่างน้อย: OrderId, Customer, Amount, Region, Notes

### Step 1 — Launch

1. **Launch** Edge/Chrome · Initial URL:

```text
https://pad.ontoiq.tech/pad/09-ajax-table.html
```

2. Variables produced: `Browser`

### Step 2 — โหลดแถวแล้ว Wait

1. เปิดแผง **UI Elements** → **Add UI element** (หรือ Add element) ด้วย UI Picker
2. ชี้ปุ่ม **Refresh orders** บนหน้า (`#btn-refresh-orders` ตาม Hints)
3. **Save** แล้ว Rename เป็น:

```text
Btn_RefreshOrders
```

4. ถ้าหน้าขึ้นว่าง / ยังไม่มีแถว: ใช้ **Press button on web page** (หรือ **Click link on web page**) · UI element: `Btn_RefreshOrders` · Browser: `%Browser%`
5. **Wait for web page content** · `%Browser%` · **Contain element**
6. ชี้ตาราง `#tbl-orders` หรือแถวข้อมูลแรก
7. **อย่า** ใช้ Wait วินาทีอย่างเดียวเป็นเกณฑ์หลัก
8. (ทางเลือก) Rename UI element ของตารางเป็น `Tbl_Orders`

### Step 3 — Extract

1. ให้เบราว์เซอร์ของ flow เปิดค้างที่ URL ด้านล่าง และมีแถวในตารางแล้ว (หลัง Refresh + Wait ใน Step 2)

```text
https://pad.ontoiq.tech/pad/09-ajax-table.html
```

2. **Extract data from web page** · Browser: `%Browser%`
3. PAD จะเปิด **live web helper** บนหน้านั้น
4. ชี้ตารางออเดอร์ (`#tbl-orders`)
5. **คลิกขวา** บนตาราง/เซลล์ในตาราง
6. เลือก **Extract Entire HTML Table**
7. Variables produced: `AjaxTable`
8. Map คอลัมน์ใกล้เคียง: OrderId, Customer, Amount, Region (ชื่อจริงบนหน้าอาจต่าง)

### Step 4 — กรองแล้วเก็บแถว

1. **For each** · Value to iterate: `%AjaxTable%` · Store into: `AjaxRow`
2. ภายในลูป **If** เช่น Amount >= `%MinAmount%` และ/หรือ Region ตรง `%TargetRegion%`
3. เมื่อผ่าน: **Insert row** เข้า `%Hits%`
4. Notes ถ้า Amount ≥ MinAmount ใส่ค่า:

```text
PRIORITY HIT
```

5. **End** If + For each

### Step 5 — เขียน CSV

1. เขียน `%Hits%` (หรือทั้ง `%AjaxTable%` ถ้า Lab อนุญาต) เป็น:

```text
C:\PAD-Labs\output\lab03\ajax-orders.csv
```

2. **Close web browser** · `%Browser%`

### Step 6 — Replay

รัน 2 ครั้ง · ตรวจว่าไม่ได้ Extract ตอนตารางยังว่าง

## Acceptance

- [ ] Flow ชื่อ `Lab03_AjaxTable`
- [ ] มี Wait จนมีแถวก่อน Extract
- [ ] มีไฟล์ `ajax-orders.csv`
- [ ] ปิดเบราว์เซอร์ท้าย flow

## Troubleshooting

| อาการ | แก้ |
|-------|-----|
| ตารางว่าง | กด Refresh + Wait element แถว/ตาราง |
| สับสนกับหลายหน้า | Lab นี้ไม่มี Next — ใช้ [Catalog](../catalog/README.md) |

## Cleanup

ปิดเบราว์เซอร์ค้าง
