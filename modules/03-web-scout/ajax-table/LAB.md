# Lab 03 — AJAX Table (Hands-on)

**อ่านก่อน:** [LESSON.md](LESSON.md) · **หน้าปก:** [README.md](README.md) · **พื้นฐาน:** [`shared/PAD-FUNDAMENTALS.md`](../../../shared/PAD-FUNDAMENTALS.md)

**Flow ชื่อ:** `Lab03_AjaxTable` · **Core**

## Setup

```text
C:\PAD-Labs\output\lab03\
```

อ่าน [`assets/scout-criteria.csv`](assets/scout-criteria.csv): `MinAmount=1500`  
(ข้อมูลตัวอย่างบน hub มี Amount ประมาณ 400–2400 — **อย่าใช้ 10000** จะไม่มีแถวผ่าน If)

## Hands-on

### Step 0 — สร้าง flow + criteria + ตาราง Hits

1. **New flow** → ชื่อ:

```text
Lab03_AjaxTable
```

2. **Set variable** Name `MinAmount` ← Value:

```text
1500
```

3. **บังคับ:** ลาก **Create new data table** (ค้น Actions Pane คำว่า `Create new data table`)
4. กด **Edit** ในฟอร์ม action เพื่อเปิดตัวสร้างตาราง
5. ใช้ปุ่ม **+** เพิ่มคอลัมน์ให้ได้ 4 คอลัมน์ แล้วตั้งชื่อให้ตรง header บนหน้าเป๊ะ:

```text
Order ID
Customer
Amount
Status
```

6. ไม่ต้องใส่แถวข้อมูลตอนนี้ (0 rows ก็ได้) → **Save** ตัวสร้างตาราง
7. **Variables produced:** เปลี่ยนชื่อเป็น `Hits` ← **ไม่ใส่ `%`**  
   (อ้างอิงทีหลังด้วย `%Hits%`)
8. ตรวจใน Variables pane ว่ามี `%Hits%` ก่อนไป Step 1 — **ถ้ายังไม่มี `%Hits%` จะ Insert ไม่ได้**

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

### Step 4 — กรองแล้วเก็บแถวลง `%Hits%`

> ไม่มี action ชื่อ “Insert into Hits”  
> ต้องใช้ **Insert row into data table** แล้วชี้ **Data table** = `%Hits%`

1. ลาก **For each**
2. Value to iterate: (คัดลอกด้านล่างวางในช่อง)

```text
%AjaxTable%
```

3. Store into: `AjaxRow` ← **ไม่ใส่ `%`**
4. **ภายใน For each** (ต้องเยื้องเข้าในลูป) ลาก **If** (ค้นคำว่า `If`)
5. ตั้งเงื่อนไข:
   - ฝั่งซ้าย / First operand: (คัดลอก — พิมพ์เอง)

```text
%AjaxRow['Amount']%
```

   - ตัวดำเนินการ: **Greater than or equal to**
   - ฝั่งขวา / Second operand: (คัดลอก)

```text
%MinAmount%
```

6. ถ้ารันแล้วเทียบไม่ได้เพราะ Amount เป็นข้อความ: ก่อน If ใช้ **Convert text to number** จาก `%AjaxRow['Amount']%` แล้วเอาตัวแปรตัวเลขไปใส่ฝั่งซ้ายแทน
7. **ภายในกิ่ง If** (เยื้องเข้าไปอีกชั้น — อย่าวางข้างนอก If) ค้น Actions Pane แล้วลาก:

```text
Insert row into data table
```

8. ตั้งค่า 3 ช่องให้ตรงนี้เท่านั้น:

| ช่องใน UI | ใส่ค่า |
|-----------|--------|
| **Data table** | `%Hits%` (กด `{x}` เลือก `Hits` — **ไม่ใช่** `AjaxRow`) |
| **Into location** | **End of data table** |
| **New value(s)** | `%AjaxRow%` (กด `{x}` เลือก `AjaxRow`) |

คัดลอกวาง New value(s) ได้:

```text
%AjaxRow%
```

9. กด **Save** ของ action Insert — บน workspace ควรเห็นประมาณ:

```text
Insert row into data table %Hits%
```

10. **End** (ปิด If) แล้ว **End** (ปิด For each)

โครงที่ถูกต้อง:

```text
For each AjaxRow in AjaxTable
  If %AjaxRow['Amount']% >= %MinAmount%
    Insert row into data table   ← Data table=%Hits% · New value(s)=%AjaxRow%
  End
End
```

### Step 5 — เขียน `%Hits%` ลง CSV

ทำ**หลัง** End ของ For each ใน Step 4 (อย่าเขียนไฟล์ข้างในลูปกรอง)

เป้าหมายของ Step นี้: แปลงตาราง `%Hits%` เป็นข้อความ CSV เก็บในตัวแปร `CsvBody` แล้วเขียนลงไฟล์

#### 5.1 เริ่มต้นข้อความด้วยหัวตาราง

1. ลาก **Set variable**
2. Name: `CsvBody` ← **ไม่ใส่ `%`**
3. Value: (คัดลอกด้านล่างวางในช่อง Value)

```text
Order ID,Customer,Amount,Status
```

ตอนนี `%CsvBody%` มีแค่บรรทัดหัวตาราง

#### 5.2 วนแต่ละแถวใน `%Hits%` แล้วต่อข้อความ

1. ลาก **For each**
2. Value to iterate: (คัดลอก)

```text
%Hits%
```

3. Store into: `HitRow` ← **ไม่ใส่ `%`**
4. **ภายใน For each** — สร้างข้อความ**หนึ่งแถว**ก่อน: ลาก **Set variable**
5. Name: `CsvLine` ← **ไม่ใส่ `%`**
6. Value: (คัดลอกทั้งก้อนวางในช่อง Value)

```text
%HitRow['Order ID'] + ',' + HitRow['Customer'] + ',' + HitRow['Amount'] + ',' + HitRow['Status']%
```

ความหมาย: เอา 4 คอลัมน์ของแถวปัจจุบันมาต่อด้วยเครื่องหมาย `,`

7. ยัง**ภายใน For each** — ต่อแถวนี้เข้าข้อความรวม: ลาก **Set variable** อีกตัว
8. Name: `CsvBody` ← **ไม่ใส่ `%`** (ชื่อเดิม — จะอัปเดตค่า)
9. Value: (คัดลอกทั้งก้อนวางในช่อง Value)

```text
%CsvBody + '
' + CsvLine%
```

ความหมาย: เอา `%CsvBody%` เดิม + ขึ้นบรรทัดใหม่ + `%CsvLine%` ที่เพิ่งสร้าง

> ใช้ `%...%` **คู่เดียวครอบทั้งนิพจน์** — อย่าเขียน `%CsvBody% + %CsvLine%` (จะ Syntax error)

10. **End** For each

#### 5.3 เขียนไฟล์

1. **หลัง End** ของ For each ลาก **Write text to file** (ค้นคำว่า `Write text to file`)
2. **File path:** (คัดลอก)

```text
C:\PAD-Labs\output\lab03\ajax-orders.csv
```

3. **Text to write:** (คัดลอก)

```text
%CsvBody%
```

4. **If file exists:** **Overwrite**
5. Encoding: แนะนำ **UTF-8** (ถ้ามีช่องให้เลือก)
6. กด **Save**
7. หลังรัน flow เปิด `C:\PAD-Labs\output\lab03\ajax-orders.csv` ตรวจหัวตาราง + แถวที่ผ่านเกณฑ์

### Step 6 — ปิดเบราว์เซอร์ + Replay

1. ลาก **Close web browser** · Web browser instance: (คัดลอก)

```text
%Browser%
```

2. กด **Run** อย่างน้อย 2 ครั้ง
3. ตรวจว่าไม่ได้ Extract ตอนตารางยังว่าง
4. เปิด `ajax-orders.csv` — ควรมีเฉพาะแถวที่ Amount >= `%MinAmount%` (เช่น 1500)

## Acceptance

- [ ] Flow ชื่อ `Lab03_AjaxTable`
- [ ] มี Wait จนมีแถวก่อน Extract
- [ ] มีไฟล์ `ajax-orders.csv` ภายใต้ `C:\PAD-Labs\output\lab03\`
- [ ] CSV มีหัวตาราง + แถวที่ผ่านเกณฑ์ MinAmount
- [ ] ปิดเบราว์เซอร์ท้าย flow

## Troubleshooting

| อาการ | แก้ |
|-------|-----|
| หา “Insert into Hits” ไม่เจอ | ไม่มีชื่อนี้ — ค้น **Insert row into data table** แล้วตั้ง Data table = `%Hits%` |
| `%Hits%` ไม่มีใน `{x}` | ยังไม่ได้ทำ Step 0 **Create new data table** + rename เป็น `Hits` |
| Insert อยู่นอก If / นอก For each | ลากให้เยื้องเข้าในกิ่ง If (ในลูป) |
| ตารางว่างตอน Extract | กด Refresh + Wait element แถว/ตาราง |
| หาคอลัมน์ Amount ใน If ไม่เจอ | พิมพ์/วาง `%AjaxRow['Amount']%` ในฝั่งซ้ายเอง |
| Data table / New value(s) สลับกัน | Data table = `%Hits%` · New value(s) = `%AjaxRow%` |
| If ไม่เข้า · Hits ว่างหลังรัน | ตรวจ `%MinAmount%` = `1500` (ข้อมูลจริงสูงสุด ~2400) · หรือ Convert text to number ก่อนเทียบ |
| Column count ไม่ตรง | `%Hits%` ต้องมี 4 คอลัมน์ชื่อเดียวกับ `%AjaxTable%` |
| หา Write CSV / เขียนไฟล์ไม่เจอ | ค้น **Write text to file** · Text = `%CsvBody%` · path ตาม Step 5 |
| CSV ว่าง / มีแต่หัวตาราง | `%Hits%` ว่าง — กลับไปตรวจ If + MinAmount=1500 |
| สับสนกับหลายหน้า | Lab นี้ไม่มี Next — ใช้ [Catalog](../catalog/README.md) |

## Cleanup

ปิดเบราว์เซอร์ค้าง
