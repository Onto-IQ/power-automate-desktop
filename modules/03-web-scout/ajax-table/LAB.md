# Lab 03 — AJAX Table (Hands-on)

**อ่านก่อน:** [LESSON.md](LESSON.md) · **หน้าปก:** [README.md](README.md) · **พื้นฐาน:** [`shared/PAD-FUNDAMENTALS.md`](../../../shared/PAD-FUNDAMENTALS.md)

**Flow ชื่อ:** `Lab03_AjaxTable` · **Core**

## Setup

```text
C:\PAD-Labs\output\lab03\
```

อ่าน [`assets/scout-criteria.csv`](assets/scout-criteria.csv): `MinAmount=10000`

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

3. (แนะนำ) **Create new data table** → Variables produced: `Hits`
4. คอลัมน์ของ `Hits` ให้ตรง header บนหน้า: Order ID, Customer, Amount, Status  
   (ถ้าต้องการ Notes ด้วย ตอน Insert ต้องใช้ list ที่มีค่าครบทุกคอลัมน์ — ดู Step 4)

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
8. เปิดดู `%AjaxTable%` ใน Variables pane (หรือ preview หลัง Extract) — **ไม่ต้อง Map คอลัมน์เอง**
9. ชื่อคอลัมน์มาจาก header จริงบนหน้าแล้ว: `Order ID`, `Customer`, `Amount`, `Status`
10. จำชื่อเหล่านี้ไว้ใช้ตอน Step 4 (เช่น อ้าง Amount ด้วยชื่อคอลัมน์จริง ไม่ใช่ชื่อที่ตั้งเอง)

### Step 4 — กรองแล้วเก็บแถว

1. ลาก **For each**
2. Value to iterate: (คัดลอกด้านล่างวางในช่อง)

```text
%AjaxTable%
```

3. Store into: `AjaxRow` ← **ไม่ใส่ `%`**
4. **ภายใน For each** ลาก **If** (ค้นใน Actions Pane คำว่า `If`)
5. ตั้งเงื่อนไขดังนี้:
   - ฝั่งซ้าย / First operand: (คัดลอกด้านล่างวางในช่อง — **พิมพ์เอง** ไม่มีตัวเลือกคอลัมน์ในรายการตัวแปร)

```text
%AjaxRow['Amount']%
```

   - ตัวดำเนินการ: **Greater than or equal to**
   - ฝั่งขวา / Second operand: (คัดลอกด้านล่างวางในช่อง)

```text
%MinAmount%
```

6. ถ้ารันแล้วเทียบไม่ได้เพราะ Amount เป็นข้อความ: ก่อน If ใช้ **Convert text to number** จาก `%AjaxRow['Amount']%` แล้วเอาตัวแปรตัวเลขไปใส่ฝั่งซ้ายแทน
7. **ภายใน If** ลาก **Insert row into data table**
8. ในฟอร์มมีช่องหลัก 3 ช่องเท่านั้น — ตั้งดังนี้:
   - **Data table** = ตารางปลายทาง (คัดลอก):

```text
%Hits%
```

   - **Into location** = **End of data table**
   - **New value(s)** = ค่าแถวใหม่ทั้งแถว (ไม่ใช่ช่องทีละคอลัมน์)

**วิธีที่แนะนำ (ง่ายสุด):** ถ้าคอลัมน์ `%Hits%` ตรงกับ `%AjaxTable%` (Order ID, Customer, Amount, Status — **ยังไม่ใส่ Notes**) ให้ใส่:

```text
%AjaxRow%
```

**วิธีใส่รายการค่า + Notes:** ในนิพจน์หนึ่งคู่ `%...%` เท่านั้น — **ห้าม** ซ้อน `%` ใน list (จะ Syntax error)

คัดลอก:

```text
%[AjaxRow['Order ID'], AjaxRow['Customer'], AjaxRow['Amount'], AjaxRow['Status'], 'PRIORITY HIT']%
```

> ผิด: `%[%AjaxRow['Amount']%, ...]%` ← `%` ซ้อน  
> ถูก: `%[AjaxRow['Amount'], ...]%` ← ชื่อตัวแปรอยู่ใน `%` นอกสุดแล้ว

9. จำนวนค่าใน `New value(s)` ต้อง**เท่ากับจำนวนคอลัมน์ของ `%Hits%`** (ลำดับตรงคอลัมน์)
10. **อย่าสลับ:** Data table = `%Hits%` · New value(s) = `%AjaxRow%` หรือ list ด้านบน

11. **End** (ปิด If) แล้ว **End** (ปิด For each)

โครงภายในลูป:

```text
For each AjaxRow in AjaxTable
  If %AjaxRow['Amount']% >= %MinAmount%
    Insert row into Hits
      Data table = %Hits%
      New value(s) = %AjaxRow%   (หรือ %[AjaxRow['Order ID'], ..., 'PRIORITY HIT']%)
  End
End
```

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
| หาคอลัมน์ Amount ใน If ไม่เจอ | ไม่มีในรายการตัวแปร — พิมพ์/วาง `%AjaxRow['Amount']%` ในฝั่งซ้ายเอง |
| Insert row Syntax error | ใน list **อย่าซ้อน `%`** — ใช้ `%[AjaxRow['Amount'], ...]%` หรือใส่ `%AjaxRow%` ทั้งแถว |
| Insert row ใส่ค่าทีละคอลัมน์ไม่เจอ | UI มีแค่ **New value(s)** — ใส่ datarow หรือ list |
| Data table / New value(s) สลับกัน | Data table = `%Hits%` · New value(s) = ค่าแถวใหม่ |
| If ไม่เข้าทั้งที่ Amount ดูใหญ่ | Convert text to number ก่อนเทียบ · ตรวจชื่อคอลัมน์ให้ตรง header (`Amount`) |
| สับสนกับหลายหน้า | Lab นี้ไม่มี Next — ใช้ [Catalog](../catalog/README.md) |

## Cleanup

ปิดเบราว์เซอร์ค้าง
