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
   คอลัมน์อย่างน้อย: OrderId, Customer, Amount, Region, Notes

### Step 1 — Launch

1. **Launch** Edge/Chrome · Initial URL:

```text
https://pad.ontoiq.tech/pad/09-ajax-table.html
```

2. Variables produced: `Browser`

### Step 2 — โหลดแถวแล้ว Wait

1. ถ้าหน้าขึ้นว่าง: กด/คลิก **Refresh orders** (`#btn-refresh-orders`) ด้วย **Press button** / **Click link**
2. **Wait for web page content** · `%Browser%` · **Contain element**  
   - ชี้ตาราง `#tbl-orders` หรือแถวข้อมูลแรก  
   - **อย่า** ใช้ Wait วินาทีอย่างเดียวเป็นเกณฑ์หลัก
3. (ทางเลือก) Rename UI element เป็น `Tbl_Orders`

### Step 3 — Extract

1. **Extract data from web page** → Variables produced: `AjaxTable`
2. Map คอลัมน์ใกล้เคียง: OrderId, Customer, Amount, Region (ชื่อจริงบนหน้าอาจต่าง)

### Step 4 — กรองแล้วเก็บแถว

1. **For each** · Value to iterate: `%AjaxTable%` · Store into: `AjaxRow`
2. ภายในลูป **If** เช่น Amount >= `%MinAmount%` และ/หรือ Region ตรง `%TargetRegion%`
3. เมื่อผ่าน: **Insert row** เข้า `%Hits%`  
   - Notes ถ้า Amount ≥ MinAmount:

```text
PRIORITY HIT
```

4. **End** If + For each

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
