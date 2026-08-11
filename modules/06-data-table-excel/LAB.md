# Lab 06 — Data Table & Excel (Hands-on)

**อ่านก่อน:** [LESSON.md](LESSON.md) · **หน้าปกบท:** [README.md](README.md) · **พื้นฐาน:** [`shared/PAD-FUNDAMENTALS.md`](../../shared/PAD-FUNDAMENTALS.md)

**วัน:** 2 · **ระดับ:** Intermediate  
**ทักษะ:** Launch Excel, Set active worksheet, Read/Write worksheet, Data table filter/aggregate, **Run Excel macro**

**สคริปต์อ้างอิง (แหล่งความจริงของ Lab นี้):** [`scripts/06-data-table-excel.robin`](scripts/06-data-table-excel.robin)

## อ้างอิง (Aug 2026)

| แหล่ง | URL |
|-------|-----|
| Excel actions | [actions-reference/excel](https://learn.microsoft.com/power-automate/desktop-flows/actions-reference/excel) |
| Run Excel macro | [how-to/run-macros-excel](https://learn.microsoft.com/power-automate/desktop-flows/how-to/run-macros-excel) |
| Excel troubleshooting | [troubleshoot Excel errors](https://learn.microsoft.com/troubleshoot/power-platform/power-automate/desktop-flows/office-automation/excel/troubleshoot-excel-errors) |
| Coding guidelines | [desktop-flow-coding-guidelines](https://learn.microsoft.com/power-automate/guidance/desktop-flow-coding-guidelines/) |

## Setup บนเครื่อง (ทำก่อนเปิด designer)

1. สร้างโฟลเดอร์ working และ output (คัดลอก path):

```text
C:\PAD-Labs\working\lab06\
```

```text
C:\PAD-Labs\output\lab06\
```

2. เตรียม **`sales-report.xlsm`** ตาม [`assets/vba/README.md`](assets/vba/README.md) แล้ววางที่ working (อย่าเขียนทับไฟล์ใน repo):

```text
C:\PAD-Labs\working\lab06\sales-report.xlsm
```

   Template ต้องครบตาม comment ในสคริปต์:
   - แผ่น **`Orders`** — ข้อมูลจาก [`assets/orders-input.xlsx`](assets/orders-input.xlsx) (หรือ CSV สำรอง)
   - แผ่น **`Filtered`** — ว่าง (สคริปต์จะเขียนทับ)
   - แผ่น **`Summary`** — ว่าง (สคริปต์จะเขียนทับ)
   - VBA module **`Lab06Macros`** + `Public Sub FormatSummary` (จาก [`FormatSummary.bas`](assets/vba/FormatSummary.bas))
3. (ทางเลือก) คัดลอก [`assets/expected-summary.csv`](assets/expected-summary.csv) ไป working เพื่อเทียบผลหลังรัน
4. ตรวจว่า flow จะเปิดไฟล์นี้เท่านั้น (ไม่เปิด `.xlsx` โดยตรง):

```text
C:\PAD-Labs\working\lab06\sales-report.xlsm
```

> **อย่า**พึ่ง **Add new worksheet** ตอนรัน flow เพื่อสร้าง `Filtered`/`Summary` — รันซ้ำจะเจอ error ชื่อแผ่นซ้ำ  
> ถ้าใช้ไดรฟ์อื่น (เช่น `D:\PAD-Labs\...`) ได้ — แต่ต้องใช้ path นั้นใน `%WorkingRoot%` / output ให้สม่ำเสมอทั้ง flow

## Input / Output (ตรงกับสคริปต์)

| | Path |
|--|------|
| Working | `%WorkingRoot%` = `C:\PAD-Labs\working\lab06` |
| Input workbook | `%WorkingRoot%\sales-report.xlsm` ← จาก [`assets/orders-input.xlsx`](assets/orders-input.xlsx) + macro |
| Macro source | [`assets/vba/FormatSummary.bas`](assets/vba/FormatSummary.bas) (module = `Lab06Macros`) |
| Macro howto | [`assets/vba/README.md`](assets/vba/README.md) |
| Expected summary | [`assets/expected-summary.csv`](assets/expected-summary.csv) |
| Output | `%OutputPath%` = `C:\PAD-Labs\output\lab06\orders-report.xlsm` |

### โจทย์คำนวณ (ต้อง implement — ตรง header สคริปต์)

1. กรองเฉพาะ `Region = BKK` **หรือ** `Amount >= 10000`
2. เพิ่มคอลัมน์ `Tier` = `Gold` ถ้า Amount >= 12000 ไม่เช่นนั้น `Silver`
3. สรุปยอดรวม Amount ของชุดที่กรองแล้ว ลง sheet `Summary` (`TotalAmount` / ค่า)
4. **Mission M — Excel Macro:** รัน `FormatSummary` เพื่อตัวหนา header / AutoFit / ไฮไลต์แถว Gold

### ลำดับ action (ตรง `06-data-table-excel.robin`)

| # | Designer action | ตัวแปร / ค่าสำคัญ |
|---|-----------------|-------------------|
| 1–3 | **Set variable** ×3 | `WorkingRoot`, `OutputPath`, `SumAmount` = `0` |
| 4 | **Launch Excel** | `%WorkingRoot%\sales-report.xlsm` · Load add-ins and macros · → `Excel` |
| 5 | **Set active Excel worksheet** | `Orders` |
| 6 | **Read from Excel worksheet** | All cells · First line = column names · → `Orders` |
| 7 | **Create new data table** | คอลัมน์ + `Tier` · → `Filtered` |
| 8 | **For each** | `%Orders%` → `CurrentRow` |
| 8a | **Convert text to number** | `%CurrentRow['Amount']%` → `AmountNumber` |
| 8b | **If** (OR) | Region = `BKK` **หรือ** `AmountNumber` ≥ `10000` |
| 8c | **If** / **Else** | ≥ `12000` → `Tier` = `Gold` / ไม่เช่นนั้น `Silver` |
| 8d | **Insert row into data table** | ต่อท้าย `%Filtered%` (รวม `Tier`) |
| 9 | **For each** | `%Filtered%` → `FilteredRow` |
| 9a | **Convert text to number** | → `FilteredAmount` |
| 9b | **Set variable** | `SumAmount` = `%SumAmount% + %FilteredAmount%` |
| 10 | **Set active** → **Write** ×2 | sheet `Filtered`: header ที่ A1 · data ที่ A2 |
| 11 | **Set active** → **Write** ×2 | sheet `Summary`: `TotalAmount` / `%SumAmount%` |
| 12 | **Run Excel macro** | `FormatSummary` |
| 13 | **If file exists** → **Delete file** | `%OutputPath%` |
| 14 | **Save Excel** (Save as) | `%OutputPath%` · From Extension |
| 15 | **Close Excel** | `%Excel%` |

> **ไม่มี** **Add new worksheet** ในสคริปต์ — แผ่น `Filtered` / `Summary` ต้องมีใน template แล้ว

---

## Hands-on ทีละขั้น

### Step 0 — สร้าง flow

1. เปิด Power Automate for desktop → **New flow**
2. ชื่อ flow (คัดลอกได้):

```text
Lab06_DataTableExcel
```

3. กด **Create**

> **กฎตัวแปรใน PAD (อ่านก่อนทำ Step ถัดไป)**  
> - ช่อง **Name** ของ **Set variable**, ส่วน **Variables produced**, และ **Store into** = พิมพ์ชื่ออย่างเดียว **ไม่มี `%`** เช่น `WorkingRoot`  
> - ช่องอื่นที่ต้องดึงค่าตัวแปร (Folder, File path, Text, …) = ใช้ `%WorkingRoot%` (**มี `%` ครบสองด้าน**)  
> - หลังสร้างแล้ว Variables pane อาจแสดงเป็น `%WorkingRoot%` — เป็นเรื่องปกติ

### Step 1 — ตั้ง path

1. ใน Actions Pane ค้นหา **Set variable** แล้วลากลง workspace
2. ตั้งค่า:
   - Name: `WorkingRoot` ← **ไม่ใส่ `%`**
   - Value: (คัดลอกด้านล่างวางในช่อง Value — หรือ path ที่คุณใช้จริง)

```text
C:\PAD-Labs\working\lab06
```

3. เพิ่ม **Set variable** อีกตัว:
   - Name: `OutputPath` ← **ไม่ใส่ `%`**
   - Value: (คัดลอกด้านล่างวางในช่อง Value)

```text
C:\PAD-Labs\output\lab06\orders-report.xlsm
```

4. **Set variable** Name: `SumAmount` ← **ไม่ใส่ `%`** · Value:

```text
0
```

### Step 2 — เปิด Excel → เปิดแผ่น Orders → อ่านทั้งแผ่น

1. ลาก **Launch Excel**
2. ตั้งค่า (ตรงสคริปต์ `LaunchAndOpen`):
   - Launch Excel: with the following document (หรือเทียบเท่าใน designer)
   - Document path: (คัดลอกด้านล่างวางในช่อง)

```text
%WorkingRoot%\sales-report.xlsm
```

   - Make instance visible: **เปิด**
   - Open as read-only: **ปิด**
   - Advanced: **Load add-ins and macros** = **เปิด** (จำเป็นสำหรับ Mission M)
3. **Variables produced:** `Excel` ← **ไม่ใส่ `%`**  
   (อ้างอิงด้วย `%Excel%`)
4. ลาก **Set active Excel worksheet**
   - Excel instance: (คัดลอก)

```text
%Excel%
```

   - Activate worksheet with name: (คัดลอก)

```text
Orders
```

5. ลาก **Read from Excel worksheet**
   - Excel instance: `%Excel%`
   - Retrieve: All available values from worksheet (หรือเทียบเท่า **Read all cells**)
   - First line of range contains column names: **เปิด**
6. **Variables produced:** `Orders` ← **ไม่ใส่ `%`**  
   (อ้างอิงด้วย `%Orders%`)

> ใน designer ปัจจุบัน **ไม่มี**พารามิเตอร์ Worksheet บน Read/Write — สลับแผ่นด้วย **Set active Excel worksheet** ก่อนเสมอ (ตรงกับ catch-up script)

### Step 3 — สร้าง Data table ว่างสำหรับผลกรอง

1. ลาก **Create new data table**
2. ตั้งคอลัมน์ตามลำดับนี้ (ตรงสคริปต์):

```text
OrderId, Customer, Product, Amount, OrderDate, Region, Tier
```

3. **Variables produced:** `Filtered` ← **ไม่ใส่ `%`**  
   (อ้างอิงด้วย `%Filtered%`)

### Step 4 — วนแถว กรอง และตั้ง Tier

1. ลาก **For each**
2. ตั้งค่า:
   - Value to iterate: (คัดลอกด้านล่างวางในช่อง)

```text
%Orders%
```

   - Store into: `CurrentRow` ← **ไม่ใส่ `%`**
3. **ภายใน For each** ลาก **Convert text to number**
   - Text to convert: (คัดลอก)

```text
%CurrentRow['Amount']%
```

   - **Variables produced:** `AmountNumber` ← **ไม่ใส่ `%`**
4. ลาก **If** — เงื่อนไข **OR** (ตามที่ designer รองรับ)

   **ทางลัด — Expression (คัดลอกวางได้เลย):**

```text
%CurrentRow['Region'] = $'''BKK''' OR AmountNumber >= 10000%
```

   อธิบาย Expression นี้สั้น ๆ:

   | ส่วน | ความหมาย |
   |------|----------|
   | `% … %` ครอบทั้งก้อน | บอก PAD ว่าเป็น expression แบบ classic (ไม่ใช่ Power Fx `=`) |
   | `CurrentRow['Region']` | ค่าคอลัมน์ Region ของแถวปัจจุบันใน For each |
   | `$'''BKK'''` | สตริง literal ใน Robin/designer (= ค่า `BKK`) |
   | `OR` | เข้าเงื่อนไขถ้าข้อใดข้อหนึ่งเป็นจริง |
   | `AmountNumber >= 10000` | ตัวเลขที่แปลงจาก Amount แล้ว (ต้องทำ Convert ก่อน) |

   วางในช่องเงื่อนไขของ **If** (โหมด Expression / ช่องเงื่อนไขเต็ม) — อย่าใส่ `%` ซ้ำซ้อนด้านนอกอีก

   **หรือตั้งทีละฝั่งใน designer:**
   - ฝั่งซ้าย (คัดลอก)

```text
%CurrentRow['Region']%
```

     ตัวดำเนินการ **Equal to** · ฝั่งขวา:

```text
BKK
```

   - **หรือ** ฝั่งซ้าย:

```text
%AmountNumber%
```

     ตัวดำเนินการ **Greater than or equal to** · ฝั่งขวา:

```text
10000
```

5. **ภายใน If** ตั้ง Tier:
   - ลาก **If** ซ้อน — ฝั่งซ้าย `%AmountNumber%` · **Greater than or equal to** · `12000`
   - **ภายใน If ซ้อน** → **Set variable** Name: `Tier` ← Value:

```text
Gold
```

   - **Else** → Name: `Tier` ← Value:

```text
Silver
```

   - → **End** (ปิด If ซ้อน)
6. ยังอยู่ในกิ่งกรอง: ลาก **Insert row into data table**
   - **Data table:** (คัดลอก)

```text
%Filtered%
```

   - **Into location:** **End of data table**
   - **New value(s)** — Expression (คัดลอกวางได้เลย; ลำดับคอลัมน์ตรง `%Filtered%`):

```text
%[CurrentRow['OrderId'], CurrentRow['Customer'], CurrentRow['Product'], CurrentRow['Amount'], CurrentRow['OrderDate'], CurrentRow['Region'], Tier]%
```

   อธิบาย Expression นี้สั้น ๆ:

   | ส่วน | ความหมาย |
   |------|----------|
   | `%[ … ]%` | list ค่าที่จะแทรกเป็นแถวใหม่ใน data table |
   | `CurrentRow['…']` | ค่าจากแถวปัจจุบัน — **ห้าม**เขียน `%CurrentRow['…']%` ซ้อนใน list |
   | `Tier` | ตัวแปรที่ตั้ง Gold/Silver ไว้ใน If ซ้อน (ไม่มี `%` ข้างใน list) |

   > กฎ: ข้างใน `%[ … ]%` ใช้ชื่อคอลัมน์/ตัวแปรเปล่า — อย่าซ้อน `%` เพิ่ม

7. ปิด **End** (If กรอง) แล้ว **End** (For each)

โครงภายในลูป (ตรงสคริปต์):

```text
For each CurrentRow in Orders
  Convert Amount → AmountNumber
  If %CurrentRow['Region'] = $'''BKK''' OR AmountNumber >= 10000%
    If AmountNumber >= 12000 → Tier = Gold Else → Tier = Silver
    Insert row into Filtered (+ Tier)
  End
End
```

### Step 5 — สรุปยอด Amount

1. **หลัง** End ของ For each ลาก **For each** บน (คัดลอก)

```text
%Filtered%
```

2. Store into: `FilteredRow` ← **ไม่ใส่ `%`**
3. ในลูป:
   - **Convert text to number** จาก `%FilteredRow['Amount']%` → `FilteredAmount`
   - **Set variable** `SumAmount` = `%SumAmount% + %FilteredAmount%` (หรือเทียบเท่าใน designer)
4. ตอนอ้างอิงต่อใช้ `%SumAmount%`

### Step 6 — เขียน sheet Filtered และ Summary

**อย่า**ใช้ **Add new worksheet** ในขั้นตอนนี้ — แผ่นต้องมีใน template แล้ว

#### 6a — Filtered (header แถว 1 + ข้อมูลแถว 2)

1. ลาก **Set active Excel worksheet** → ชื่อแผ่น:

```text
Filtered
```

2. ลาก **Write to Excel worksheet**
   - Excel instance: `%Excel%`
   - Value to write: (คัดลอก — เขียนหัวคอลัมน์)

```text
%Filtered.ColumnHeadersRow%
```

   - Write mode: On specified cell · Column: `A` · Row: `1`
3. ลาก **Write to Excel worksheet** อีกตัว
   - Value to write: (คัดลอก)

```text
%Filtered%
```

   - Column: `A` · Row: `2`

#### 6b — Summary

1. ลาก **Set active Excel worksheet** → ชื่อแผ่น:

```text
Summary
```

2. ลาก **Write to Excel worksheet**
   - Value:

```text
TotalAmount
```

   - Column: `A` · Row: `1`
3. ลาก **Write to Excel worksheet**
   - Value: (คัดลอก)

```text
%SumAmount%
```

   - Column: `B` · Row: `1`

### Step 7 — Mission M: Run Excel macro

1. ตรวจว่า workbook เป็น `.xlsm` และมี `Public Sub FormatSummary` ใน module **`Lab06Macros`** (ตาม [`assets/vba/README.md`](assets/vba/README.md))
2. ลาก **Run Excel macro**
3. ตั้งค่า:
   - Excel instance: (คัดลอก)

```text
%Excel%
```

   - Macro: (คัดลอก)

```text
FormatSummary
```

4. กด Save ในหน้าต่าง action

> ถ้าตั้งชื่อ VBA **module** ซ้ำกับ Sub (`FormatSummary`) → PAD จะ **Failed to run macro**  
> แก้: เปลี่ยนชื่อ module เป็น `Lab06Macros` หรือเรียก `Lab06Macros.FormatSummary`

### Step 8 — บันทึก output แบบรันซ้ำได้ แล้วปิด Excel

นโยบาย Lab Kit: ก่อน **Save Excel** (Save document as) ไป path คงที่ ต้องลบไฟล์เก่าก่อนถ้ามี

1. ลาก **If file exists**
2. ตั้งค่า:
   - File path: (คัดลอก)

```text
%OutputPath%
```

3. **ภายใน If** ลาก **Delete file** → File: `%OutputPath%`
4. ปิดด้วย **End**
5. ลาก **Save Excel** → โหมด **Save document as**
   - Excel instance: `%Excel%`
   - Document path: `%OutputPath%`
   - Document format: **Default (From Extension)** (ไฟล์ลงท้าย `.xlsm`)
6. ลาก **Close Excel**
   - Excel instance: `%Excel%`
   - ก่อนปิด: บันทึกแล้ว (อย่า Save อีกครั้งทับ working โดยไม่ตั้งใจ)

### Step 9 — รันและตรวจ

1. กด **Run**
2. เปิด `C:\PAD-Labs\output\lab06\orders-report.xlsm`
3. ตรวจ sheet `Filtered` / `Summary` เทียบ [`assets/expected-summary.csv`](assets/expected-summary.csv):
   - `Filtered` ≈ **4** แถวข้อมูล (+ header)
   - `Summary` A1 = `TotalAmount`, B1 = **56000**
4. หลัง macro: แถวหัวตัวหนา และแถว Gold มีสีพื้น (ถ้าใช้ `FormatSummary.bas` เต็ม)
5. รันซ้ำรอบสอง — ต้องไม่พังเพราะชื่อไฟล์ซ้ำ **และ** ไม่พังเพราะชื่อแผ่นซ้ำ (เพราะไม่มี Add worksheet)

### Challenge (ทางเลือก)

- เรียง `%Filtered%` ตาม Amount ก่อนเขียน sheet
- เพิ่ม sheet `Audit` ใน template แล้วบันทึกจำนวนแถวที่ถูกตัดออกจากการกรอง

---

## จุดที่มักทำผิด

| ผิด | ถูก |
|-----|-----|
| พิมพ์ `%Name%` ในช่อง Name / Store into / **Variables produced** | ใช้ชื่อเปล่าไม่มี `%` เช่น `WorkingRoot`, `Orders` |
| เขียนทับไฟล์ใน `assets/` ของ repo | คัดลอกไป `working\lab06` ก่อน |
| **Add new worksheet** สร้าง `Filtered`/`Summary` ตอนรัน | เตรียม 3 แผ่นใน `sales-report.xlsm` แล้วใช้ **Set active** |
| ใส่พารามิเตอร์ Worksheet บน Read/Write (designer ปัจจุบันไม่รับ) | **Set active Excel worksheet** ก่อน Read/Write |
| เขียนแค่ `%Filtered%` ที่ A1 โดยไม่มี header | เขียน `%Filtered.ColumnHeadersRow%` ที่ A1 แล้ว `%Filtered%` ที่ A2 |
| VBA module ชื่อ `FormatSummary` ซ้ำกับ Sub | module = `Lab06Macros`, Macro ใน PAD = `FormatSummary` |
| **Save document as** รอบสองโดยไม่ลบไฟล์เก่า | **If file exists** → **Delete file** ก่อน Save as |
| ลืม **Close Excel** | ปิด instance ทุกครั้งท้าย flow |
| เทียบ Amount เป็น text โดยไม่แปลง | **Convert text to number** → `AmountNumber` / `FilteredAmount` |
| กรองแค่ Region หรือแค่ Amount | ต้องเป็น BKK **หรือ** Amount >= 10000 |

---

## Variables

| ชื่อตอนสร้าง (ไม่มี `%`) | ตอนอ้างอิง | Type |
|--------------------------|------------|------|
| `WorkingRoot` | `%WorkingRoot%` | Text |
| `OutputPath` | `%OutputPath%` | Text |
| `Excel` | `%Excel%` | Excel instance |
| `Orders` | `%Orders%` | Data table |
| `Filtered` | `%Filtered%` | Data table |
| `CurrentRow` | `%CurrentRow%` | Data row |
| `AmountNumber` | `%AmountNumber%` | Numeric |
| `FilteredRow` | `%FilteredRow%` | Data row |
| `FilteredAmount` | `%FilteredAmount%` | Numeric |
| `SumAmount` | `%SumAmount%` | Numeric |
| `Tier` | `%Tier%` | Text |

## Expected Result

เทียบ [`assets/expected-summary.csv`](assets/expected-summary.csv) (ข้อมูล `orders-input` ปัจจุบัน):

| ตรวจ | ค่าที่คาด |
|------|-----------|
| แถวใน `Filtered` | **4** (`ORD-2001`, `2003`, `2005`, `2007`) |
| `Summary!B1` (`SumAmount`) | **56000** |
| Tier | Gold **3** / Silver **1** |
| แผ่นในไฟล์ผลลัพธ์ | `Orders` / `Filtered` / `Summary` |
| หลัง `FormatSummary` | header ตัวหนา · AutoFit · แถว Gold มีสีพื้น (ถ้าใช้ bas เต็ม) |

## Acceptance Criteria

- [ ] อ่าน/เขียนด้วย Excel actions + **Set active worksheet**
- [ ] ปิด Excel instance ทุกครั้ง
- [ ] มีอย่างน้อยแผ่น `Filtered` และ `Summary` ในไฟล์ผลลัพธ์
- [ ] **รันซ้ำได้:** รัน flow ครั้งที่ 2 ด้วย path output เดิมโดยไม่ error ชื่อไฟล์ซ้ำ (**If file exists** → **Delete file** ก่อน Save as)
- [ ] **Mission M:** รัน **Run Excel macro** สำเร็จอย่างน้อย 1 ครั้ง (หรือวิทยากรตรวจว่า macro พร้อมแล้วแต่ถูกบล็อกโดยนโยบายเครื่อง)

## Troubleshooting

| อาการ | แก้ |
|-------|-----|
| Save as รอบสองล้ม (ไฟล์ซ้ำ) | ก่อน **Save Excel** (as) ใช้ **If file exists** → **Delete file** — ดู [`shared/BEST-PRACTICES.md`](../../shared/BEST-PRACTICES.md) ส่วน Excel |
| ไม่สามารถสร้าง worksheet ชื่อ Filtered | อย่า Add ตอนรัน — ใส่แผ่นใน template แล้ว **Set active** (ดู Setup) |
| Failed to run macro | ตรวจ Trust Center · ไฟล์เป็น `.xlsm` · Macro = `FormatSummary` · **อย่า**ตั้งชื่อ module ซ้ำ Sub · เปิด **Load add-ins and macros** |
| File locked | ปิด Excel UI / ฆ่า `EXCEL.EXE` ที่ค้าง แล้วรันใหม่ |
| Column not found | ตรวจชื่อ header ให้ตรง schema · อ้างคอลัมน์ด้วย `%CurrentRow['Amount']%` |
| Number format | Convert text to number |
| หาคอลัมน์ใน If ไม่เจอ | ไม่มีในรายการตัวแปร — วาง `%CurrentRow['Region']%` / `%AmountNumber%` |

## Cleanup

- ลบไฟล์ใน working/output ได้หลังตรวจ
- ไม่ต้องปรับเว็บ Lab Hub สำหรับ Lab นี้

> **Catch-up:** ตามไม่ทัน → วาง [`scripts/06-data-table-excel.robin`](scripts/06-data-table-excel.robin) ใน **flow ว่าง** (full) — template ต้องมีแผ่น `Orders` / `Filtered` / `Summary` + macro พร้อม
