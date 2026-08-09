# Lab 06 — Data Table & Excel (Hands-on)

**อ่านก่อน:** [LESSON.md](LESSON.md) · **หน้าปกบท:** [README.md](README.md) · **พื้นฐาน:** [`shared/PAD-FUNDAMENTALS.md`](../../shared/PAD-FUNDAMENTALS.md)

**วัน:** 2 · **ระดับ:** Intermediate  
**ทักษะ:** Launch Excel, Read/Write worksheet, Data table filter/sort/aggregate, **Run Excel macro**

## อ้างอิง (Aug 2026)

| แหล่ง | URL |
|-------|-----|
| Excel actions | [actions-reference/excel](https://learn.microsoft.com/power-automate/desktop-flows/actions-reference/excel) |
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

2. คัดลอก workbook จาก [`assets/`](assets/) ไปยัง:

```text
C:\PAD-Labs\working\lab06\
```

   (อย่าเขียนทับไฟล์ใน repo โดยตรง)
3. เตรียม macro ตาม [`assets/vba/README.md`](assets/vba/README.md) → ได้ไฟล์ `sales-report.xlsm` ใน working  
   - ถ้ายังมีแค่ CSV: เปิด `orders-input.csv` ใน Excel แล้ว Save As `.xlsx` / รวมเข้า `.xlsm` ตาม howto
4. ตรวจว่าใน working มีแผ่น `Orders` ตาม schema ใน [`shared/DATA-SCHEMAS.md`](../../shared/DATA-SCHEMAS.md) ส่วน Orders Scout

> ถ้าใช้ไดรฟ์อื่น (เช่น `D:\PAD-Labs\...`) ได้ — แต่ต้องใช้ path นั้นใน `%WorkingRoot%` / output ให้สม่ำเสมอทั้ง flow

## Input / Output

| | Path |
|--|------|
| Input workbook | [`assets/orders-input.xlsx`](assets/orders-input.xlsx) / CSV สำรอง |
| Macro source | [`assets/vba/FormatSummary.bas`](assets/vba/FormatSummary.bas) |
| Macro howto | [`assets/vba/README.md`](assets/vba/README.md) |
| Expected summary | [`assets/expected-summary.csv`](assets/expected-summary.csv) |
| Output | ดู code block ใน Step 1 (`OutputPath`) |

### โจทย์คำนวณ (ต้อง implement)

1. กรองเฉพาะ `Region = BKK` **หรือ** `Amount >= 10000`
2. เพิ่มคอลัมน์ `Tier` = `Gold` ถ้า Amount >= 12000 ไม่เช่นนั้น `Silver`
3. สรุปยอดรวม Amount ของชุดที่กรองแล้ว ลง sheet `Summary`
4. **Mission M — Excel Macro:** รัน `FormatSummary` เพื่อตัวหนา header / AutoFit / ไฮไลต์แถว Gold

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

4. (แนะนำ) **Set variable** Name: `SumAmount` ← **ไม่ใส่ `%`** · Value:

```text
0
```

### Step 2 — เปิด Excel และอ่านแผ่น Orders

1. ลาก **Launch Excel**
2. ตั้งค่า:
   - Launch Excel: with the following document (หรือเทียบเท่าใน designer)
   - Document path: (คัดลอกด้านล่างวางในช่อง)

```text
%WorkingRoot%\sales-report.xlsm
```

     (หรือ working copy ของ `orders-input.xlsx` แล้วค่อย Save as `.xlsm` ทีหลัง — แนะนำเปิด `.xlsm` ที่มี macro พร้อม)
3. **Variables produced:** `Excel` ← **ไม่ใส่ `%`**  
   (อ้างอิงด้วย `%Excel%`)
4. ลาก **Read from Excel worksheet** วางหลัง Launch Excel
5. ตั้งค่า:
   - Excel instance: (คัดลอกด้านล่างวางในช่อง)

```text
%Excel%
```

   - Worksheet: (คัดลอกด้านล่างวางในช่อง)

```text
Orders
```

   - First line of range contains column names: เปิด
6. **Variables produced:** `Orders` ← **ไม่ใส่ `%`**  
   (อ้างอิงด้วย `%Orders%`)

### Step 3 — สร้าง Data table ว่างสำหรับผลกรอง

1. ลาก **Create new data table** (หรือสร้างตารางว่างตามที่ designer รองรับ)
2. ตั้งคอลัมน์ให้ครบตามแถวต้นทาง **บวก** คอลัมน์ `Tier`
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
3. **ภายใน For each** ลาก **If**
4. เงื่อนไข (ใช้ OR ตามที่ designer รองรับ):
   - ฝั่งซ้าย (คัดลอกด้านล่างวางในช่อง)

```text
%CurrentRow['Region']%
```

     ตัวดำเนินการ **Equal to** · ฝั่งขวา (คัดลอกด้านล่างวางในช่อง)

```text
BKK
```

   - **หรือ** ฝั่งซ้าย (คัดลอกด้านล่างวางในช่อง)

```text
%CurrentRow['Amount']%
```

     ตัวดำเนินการ **Greater than or equal to** · ฝั่งขวา (คัดลอกด้านล่างวางในช่อง)

```text
10000
```

   (ถ้า Amount เป็น text ให้แปลงเป็นตัวเลขก่อนเทียบ)
5. **ภายใน If** ตั้ง Tier:
   - ลาก **If** ซ้อน
   - ฝั่งซ้าย (คัดลอก):

```text
%CurrentRow['Amount']%
```

   - ตัวดำเนินการ: **Greater than or equal to**
   - ฝั่งขวา (คัดลอก):

```text
12000
```

   - **ภายใน If ซ้อน** → **Set variable** Name: `Tier` ← **ไม่ใส่ `%`** · Value:

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
   - **New value(s):** ใส่รายการตามลำดับคอลัมน์ของ `%Filtered%` (รวม Tier) เช่น:

```text
%[%CurrentRow['OrderId']%, %CurrentRow['Customer']%, %CurrentRow['Product']%, %CurrentRow['Amount']%, %CurrentRow['OrderDate']%, %CurrentRow['Region']%, %Tier%]%
```

   (ถ้าคอลัมน์ของ `%Filtered%` ตรง `%Orders%` ยกเว้น Tier ให้สร้าง list ให้ครบทุกคอลัมน์ตามที่สร้างตารางไว้)
7. ปิด **End** (If กรอง) แล้ว **End** (For each)

โครงภายในลูป:

```text
For each CurrentRow in Orders
  If %CurrentRow['Region']% = BKK OR %CurrentRow['Amount']% >= 10000
    If %CurrentRow['Amount']% >= 12000 → Tier = Gold Else → Tier = Silver
    Insert row into Filtered (+ Tier)
  End
End
```

### Step 5 — สรุปยอด Amount

1. **หลัง** End ของ For each ลาก **For each** บน (คัดลอกด้านล่างวางในช่อง)

```text
%Filtered%
```

   (หรือรวมยอดระหว่างแทรกแถวก็ได้)
2. Store into: `FilteredRow` ← **ไม่ใส่ `%`**
3. ในลูป: อ่าน Amount แล้วบวกเข้า `SumAmount` — ใช้ (คัดลอก):

```text
%FilteredRow['Amount']%
```

   (ถ้าเป็นข้อความ: **Convert text to number** ก่อน)
4. ตอนอ้างอิงต่อใช้ `%SumAmount%`

### Step 6 — เขียน sheet Filtered และ Summary

1. ลาก **Write to Excel worksheet**
2. ตั้งค่า (sheet Filtered):
   - Excel instance: (คัดลอกด้านล่างวางในช่อง)

```text
%Excel%
```

   - Worksheet: (คัดลอกด้านล่างวางในช่อง)

```text
Filtered
```

     (สร้างใหม่ถ้ายังไม่มี ตามที่ action รองรับ)
   - Value to write: (คัดลอกด้านล่างวางในช่อง)

```text
%Filtered%
```

     (หรือเขียนทีละช่วงให้ได้ตารางครบ)
3. ลาก **Write to Excel worksheet** อีกชุดสำหรับ sheet Summary
4. ตั้งค่าตัวอย่าง:
   - Worksheet: (คัดลอกด้านล่างวางในช่อง)

```text
Summary
```

   - เซลล์ Label เช่น (คัดลอกด้านล่างวางในช่อง)

```text
TotalAmount
```

   - Value = (คัดลอกด้านล่างวางในช่อง)

```text
%SumAmount%
```

   - เพิ่มแถว Label อื่นได้ถ้าต้องการ (เช่นจำนวนแถวที่ผ่านเงื่อนไข)

### Step 7 — Mission M: Run Excel macro

1. ตรวจว่า workbook เป็น `.xlsm` และมี macro ชื่อ `FormatSummary` (ตาม [`assets/vba/README.md`](assets/vba/README.md))
2. ลาก **Run Excel macro**
3. ตั้งค่า:
   - Excel instance: (คัดลอกด้านล่างวางในช่อง)

```text
%Excel%
```

   - Macro: (คัดลอกด้านล่างวางในช่อง)

```text
FormatSummary
```

4. กด Save ในหน้าต่าง action

### Step 8 — บันทึก output แบบรันซ้ำได้ แล้วปิด Excel

นโยบาย Lab Kit: ก่อน **Save document as** ไป path คงที่ ต้องลบไฟล์เก่าก่อนถ้ามี

1. ลาก **If file exists**
2. ตั้งค่า:
   - File path: (คัดลอกด้านล่างวางในช่อง)

```text
%OutputPath%
```

3. **ภายใน If** ลาก **Delete file** → File: (คัดลอกด้านล่างวางในช่อง)

```text
%OutputPath%
```

4. ปิดด้วย **End**
5. ลาก **Save document as** (หรือชื่อเทียบเท่าในกลุ่ม Excel ที่บันทึกเป็น path ใหม่)
   - Excel instance: (คัดลอกด้านล่างวางในช่อง)

```text
%Excel%
```

   - Document path: (คัดลอกด้านล่างวางในช่อง)

```text
%OutputPath%
```

6. ลาก **Close Excel**
   - Excel instance: (คัดลอกด้านล่างวางในช่อง)

```text
%Excel%
```

   - ก่อนปิด: อย่าลืมว่าบันทึกแล้ว

> ทางเลือกที่ผ่านเกณฑ์เช่นกัน: เปิดไฟล์ output เดิมแล้ว **Save document** (ไม่ as) — แต่ใน Lab นี้แนะนำ If exists → Delete → Save document as ให้ชัด

### Step 9 — รันและตรวจ

1. กด **Run**
2. เปิด `orders-report.xlsm` ตรวจ sheet `Filtered` / `Summary` เทียบ [`assets/expected-summary.csv`](assets/expected-summary.csv)
3. หลัง macro: แถวหัวตัวหนา และแถว Gold มีสีพื้น (ถ้าใช้ `FormatSummary.bas` เต็ม)
4. รันซ้ำรอบสอง — ต้องไม่พังเพราะชื่อไฟล์ซ้ำ

### Challenge (ทางเลือก)

- เรียง `%Filtered%` ตาม Amount ก่อนเขียน sheet
- เพิ่ม sheet `Audit` บันทึกจำนวนแถวที่ถูกตัดออกจากการกรอง

---

## จุดที่มักทำผิด

| ผิด | ถูก |
|-----|-----|
| พิมพ์ `%Name%` ในช่อง Name / Store into / **Variables produced** | ใช้ชื่อเปล่าไม่มี `%` เช่น `WorkingRoot`, `Orders` |
| เขียนทับไฟล์ใน `assets/` ของ repo | คัดลอกไป `working\lab06` ก่อน |
| **Save document as** รอบสองโดยไม่ลบไฟล์เก่า | **If file exists** → **Delete file** ก่อน Save as |
| ลืม **Close Excel** | ปิด instance ทุกครั้งท้าย flow |
| Macro ชื่อผิด / ไฟล์ยังเป็น `.xlsx` | ใช้ `.xlsm` + macro = `FormatSummary` |
| เทียบ Amount เป็น text โดยไม่แปลง | Convert text to number ก่อน If |
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
| `SumAmount` | `%SumAmount%` | Numeric |
| `Tier` | `%Tier%` | Text |

## Expected Result

- จำนวนแถวที่ผ่านเงื่อนไขและยอดรวมตรงแนว `expected-summary.csv`
- ไฟล์ผลลัพธ์มีอย่างน้อย 2 sheets (`Filtered`, `Summary`)
- หลัง macro: header ตัวหนา และแถว Gold มีสีพื้น (ถ้าใช้ bas เต็ม)

## Acceptance Criteria

- [ ] อ่าน/เขียนด้วย Excel actions
- [ ] ปิด Excel instance ทุกครั้ง
- [ ] มีอย่างน้อย 2 sheets ในไฟล์ผลลัพธ์
- [ ] **รันซ้ำได้:** รัน flow ครั้งที่ 2 ด้วย path output เดิมโดยไม่ error ชื่อไฟล์ซ้ำ (**If file exists** → **Delete file** ก่อน Save as / หรือเปิดไฟล์เดิมแล้ว Save)
- [ ] **Mission M:** รัน **Run Excel macro** สำเร็จอย่างน้อย 1 ครั้ง (หรือวิทยากรตรวจว่า macro พร้อมแล้วแต่ถูกบล็อกโดยนโยบายเครื่อง)

## Troubleshooting

| อาการ | แก้ |
|-------|-----|
| Save as รอบสองล้ม (ไฟล์ซ้ำ) | ก่อน **Save document as** ใช้ **If file exists** → **Delete file** — ดู [`shared/BEST-PRACTICES.md`](../../shared/BEST-PRACTICES.md) ส่วน Excel |
| File locked | ปิด Excel UI ที่เปิดไฟล์อยู่ |
| Column not found | ตรวจชื่อ header ให้ตรง schema · อ้างคอลัมน์ด้วย `%CurrentRow['Amount']%` (พิมพ์เอง) |
| Number format | Convert text to number |
| หาคอลัมน์ใน If ไม่เจอ | ไม่มีในรายการตัวแปร — วาง `%CurrentRow['Region']%` / `%CurrentRow['Amount']%` |
| Macro disabled / not found | ตรวจ Trust Center + ชื่อ macro = `FormatSummary` + ไฟล์เป็น `.xlsm` |
| VBA project access | ดูขั้นตอน import ใน `assets/vba/README.md` |

## Cleanup

- ลบไฟล์ใน working/output ได้หลังตรวจ
- ไม่ต้องปรับเว็บ Lab Hub สำหรับ Lab นี้
