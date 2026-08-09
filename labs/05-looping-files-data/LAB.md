# Lab 05 — Looping Files / Data (Hands-on)

**อ่านก่อน:** [LESSON.md](LESSON.md) · **หน้าปกบท:** [README.md](README.md) · **พื้นฐาน:** [`shared/PAD-FUNDAMENTALS.md`](../../shared/PAD-FUNDAMENTALS.md)

**วัน:** 2 · **ระดับ:** Intermediate  
**ทักษะ:** For each, Loop index, รวมผลจากหลายไฟล์, Do until (challenge)

## อ้างอิง (Aug 2026)

| แหล่ง | URL |
|-------|-----|
| Folder actions | [actions-reference/folder](https://learn.microsoft.com/power-automate/desktop-flows/actions-reference/folder) |
| File actions | [actions-reference/file](https://learn.microsoft.com/power-automate/desktop-flows/actions-reference/file) |
| Getting started (file pattern) | [getting-started-freeorg](https://learn.microsoft.com/power-automate/desktop-flows/getting-started-freeorg) |

## Setup บนเครื่อง (ทำก่อนเปิด designer)

1. สร้างโฟลเดอร์ `C:\PAD-Labs\working\lab05\` และ `C:\PAD-Labs\output\lab05\`
2. คัดลอกทั้งโฟลเดอร์ [`assets/batch`](assets/batch/) ไปยัง `C:\PAD-Labs\working\lab05\batch`
3. สร้างโฟลเดอร์ว่าง `C:\PAD-Labs\working\lab05\processed\` (หรือให้ Flow สร้าง)
4. ตรวจว่าใน `batch` มีอย่างน้อย: `batch-01.csv`, `batch-02.csv`, `batch-03.csv`

> ถ้าใช้ไดรฟ์อื่นได้ — แต่ต้องใช้ path นั้นใน `%WorkingRoot%` ให้สม่ำเสมอทั้ง flow

## Input / Output

| | Path |
|--|------|
| Batch files | [`assets/batch/`](assets/batch/) |
| Expected summary | [`assets/expected-batch-summary.csv`](assets/expected-batch-summary.csv) |
| Processed marker folder | `C:\PAD-Labs\working\lab05\processed\` |
| Your output | `C:\PAD-Labs\output\lab05\batch-summary.csv` |

### ไฟล์ batch

| ไฟล์ | Orders | รวม Amount (ตรวจเองได้) |
|------|--------|-------------------------|
| `batch-01.csv` | 2 | 20000 |
| `batch-02.csv` | 2 | 17500 |
| `batch-03.csv` | 1 | 9000 |
| **Total** | **5** | **46500** |

Schema ในแต่ละไฟล์ (ตัวอย่าง `batch-01.csv`): `OrderId`, `Customer`, `Amount`, `Region`

---

## Hands-on ทีละขั้น

### Step 0 — สร้าง flow

1. เปิด Power Automate for desktop → **New flow**
2. ชื่อ: `Lab05_LoopingFilesData` → **Create**

> **กฎตัวแปรใน PAD (อ่านก่อนทำ Step ถัดไป)**  
> - ช่อง **Name** ของ **Set variable**, ชื่อ **produced variable**, และ **Store into** = พิมพ์ชื่ออย่างเดียว **ไม่มี `%`** เช่น `WorkingRoot`  
> - ช่องอื่นที่ต้องดึงค่าตัวแปร (Folder, File path, Text, …) = ใช้ `%WorkingRoot%` (**มี `%` ครบสองด้าน**)  
> - หลังสร้างแล้ว Variables pane อาจแสดงเป็น `%WorkingRoot%` — เป็นเรื่องปกติ

### Step 1 — ตั้ง path และตัวรวม

1. ลาก **Set variable**
2. ตั้งค่า:
   - Name: `WorkingRoot` ← **ไม่ใส่ `%`**
   - Value: `C:\PAD-Labs\working\lab05`
3. ลาก **Set variable**:
   - Name: `GrandTotal` ← **ไม่ใส่ `%`**
   - Value: `0`

### Step 2 — สร้างโฟลเดอร์ processed (ถ้ายังไม่มี)

1. ลาก **If folder exists**
2. Folder path: `%WorkingRoot%\processed`
3. ในกิ่ง **Else** ลาก **Create folder**
   - Folder name: `processed`
   - Into: `%WorkingRoot%`
4. ปิดด้วย **End**

### Step 3 — ดึงรายการ CSV จาก batch

1. ลาก **Get files in folder**
2. ตั้งค่า:
   - Folder: `%WorkingRoot%\batch`
   - File filter: `*.csv`
   - Include subfolders: ปิด
3. ชื่อ produced variable: `BatchFiles` ← **ไม่ใส่ `%`**  
   (เวลาอ้างอิงทีหลังใช้ `%BatchFiles%`)

### Step 4 — สร้าง Data table สรุป

1. ลาก **Create new data table**
2. ตั้งคอลัมน์: `FileName`, `RowCount`, `TotalAmount`
3. ชื่อ produced: `SummaryTable` ← **ไม่ใส่ `%`**  
   (อ้างอิงด้วย `%SummaryTable%`)

### Step 5 — For each ไฟล์ (ชั้นนอก)

1. ลาก **For each**
2. ตั้งค่า:
   - Value to iterate: `%BatchFiles%` ← **ใช้** (มี `%`)
   - Store into: `CurrentFile` ← **ไม่ใส่ `%`**
3. **ภายใน For each** ลาก **Get file path part** เพื่อได้ชื่อไฟล์
   - File path: `%CurrentFile%` ← **ใช้** (มี `%`)
   - ส่วนที่ต้องการ: Name / File name
   - ชื่อ produced: `FileName` ← **ไม่ใส่ `%`**
4. ลาก **Set variable**: Name `TotalAmount` = Value `0` ← **ไม่ใส่ `%` ใน Name**
5. ลาก **Set variable**: Name `RowCount` = Value `0`

### Step 6 — อ่าน CSV ของไฟล์ปัจจุบัน

ยังอยู่ภายใน For each ชั้นนอก:

1. อ่านเนื้อหาไฟล์เป็นตาราง — เลือกตามที่ designer ถนัด เช่น:
   - **Read text from file** แล้วแปลงเป็น Data table / หรือ
   - เปิดด้วย **Launch Excel** → **Read from Excel worksheet** แล้ว **Close Excel** (ถ้าแปลง CSV เป็น workbook ชั่วคราว)
2. ชื่อ produced ของตารางแถวข้อมูล: `FileTable` ← **ไม่ใส่ `%`**  
   (อ้างอิงด้วย `%FileTable%`)
3. ตั้งค่าให้แถวแรกเป็นชื่อคอลัมน์ (Skip first line / First line of range contains column names) เพื่อไม่นับ header เป็น order

### Step 7 — For each แถว (ชั้นใน) รวม Amount

ยังอยู่ภายใน For each ไฟล์:

1. ลาก **For each** ซ้อน
2. ตั้งค่า:
   - Value to iterate: `%FileTable%` ← **ใช้** (มี `%`)
   - Store into: `CurrentRow` ← **ไม่ใส่ `%`**
3. **ภายในลูปชั้นใน:**
   - อ่าน `%CurrentRow%['Amount']` (หรือคอลัมน์ Amount ตามชื่อจริง)
   - ถ้าเป็นข้อความ: ใช้ **Convert text to number** → ชื่อ produced: `AmountNumber` ← **ไม่ใส่ `%`**
   - ลาก **Increase variable** / Set variable: ใช้ `%TotalAmount%` = `%TotalAmount% + %AmountNumber%` ← **ใช้** ตัวแปร (มี `%`)
   - **Increase variable** เลือก `RowCount` (ไม่มี `%`) + `1`
4. ปิด **End** ของ For each ชั้นใน

### Step 8 — เพิ่มแถวสรุป + ย้ายไฟล์ไป processed

ยังอยู่ภายใน For each ไฟล์ หลังรวมยอด:

1. ลาก **Insert row into data table** เข้า `%SummaryTable%`
2. ค่า:
   - FileName = `%FileName%`
   - RowCount = `%RowCount%`
   - TotalAmount = `%TotalAmount%`
3. ลาก **Increase variable** / Set: `%GrandTotal%` = `%GrandTotal% + %TotalAmount%`
4. ลาก **Move file(s)** (หรือ **Copy file(s)** แล้วค่อยลบต้นทางก็ได้)
   - File(s): `%CurrentFile%`
   - Destination: `%WorkingRoot%\processed\`
5. ปิด **End** ของ For each ชั้นนอก

โครงที่ได้ควรคล้าย:

```text
For each CurrentFile in BatchFiles
  Get file path part → FileName
  TotalAmount = 0; RowCount = 0
  อ่านไฟล์ → FileTable
  For each CurrentRow in FileTable
    Convert Amount → number
    TotalAmount += Amount
    Increase RowCount
  End
  Insert row into SummaryTable
  GrandTotal += TotalAmount
  Move CurrentFile → processed\
End
```

### Step 9 — เขียน batch-summary.csv

1. **หลัง** End ของ For each ชั้นนอก แปลง `%SummaryTable%` เป็น CSV  
   (Write CSV / วนสร้างข้อความ — ให้ตรงรูป [`assets/expected-batch-summary.csv`](assets/expected-batch-summary.csv))
2. ลาก **Write text to file** (หรือ action เขียน CSV)
3. ตั้งค่า:
   - File path: `C:\PAD-Labs\output\lab05\batch-summary.csv`
   - If file exists: Overwrite
4. ตรวจว่า `%GrandTotal%` ควรได้ `46500` (เก็บใน Variables pane หรือเขียนท้ายไฟล์ก็ได้)

### Step 10 — รันและตรวจ

1. กด **Run**
2. เปิด `batch-summary.csv` เทียบ expected:
   - `batch-01.csv`, 2, 20000
   - `batch-02.csv`, 2, 17500
   - `batch-03.csv`, 1, 9000
3. ตรวจโฟลเดอร์ `processed\` ว่ามีไฟล์ครบ
4. ก่อนรันซ้ำ: คัดลอก `assets/batch` กลับไป `working\lab05\batch` และเคลียร์ `processed\` ถ้าต้องการทดสอบ Move อีกครั้ง

### Challenge (ทางเลือก) — Do until / Loop condition

จำลองรอไฟล์:

1. **Set variable** Name: `RetryCount` ← **ไม่ใส่ `%`** = Value `0`
2. ใช้ **Loop condition** / Do until จน `%RetryCount% > 3` **หรือ** **If file exists** ที่ path ที่คาดหวัง
3. ในลูป: **Increase variable** เลือก `RetryCount` (ไม่มี `%`) และ (ถ้าต้องการ) Wait สั้น ๆ
4. ไม่บังคับในเกณฑ์ผ่าน — ใช้ฝึกเงื่อนไขออกจากลูป

---

## จุดที่มักทำผิด

| ผิด | ถูก |
|-----|-----|
| พิมพ์ `%Name%` ในช่อง Name / Store into / ชื่อ produced | ใช้ชื่อเปล่าไม่มี `%` เช่น `WorkingRoot`, `CurrentFile` |
| อ่าน `batch-01` / `02` / `03` ด้วย 3 ชุด action แยกโดยไม่ลูป | ใช้ **For each** บน `%BatchFiles%` |
| นับแถว header เป็น order | Skip first line / ตั้ง column names |
| Amount เป็นข้อความแล้วบวกไม่ได้ | **Convert text to number** ก่อนรวม |
| สรุปไม่มีแถวต่อไฟล์ | **Insert row into data table** หลังรวมยอดแต่ละไฟล์ |
| ลืมย้ายไป processed | **Move file(s)** / Copy ไป `%WorkingRoot%\processed\` |
| Grand total ไม่ใช่ 46500 | ตรวจว่าวนครบ 3 ไฟล์และไม่ข้ามแถวข้อมูล |

---

## Variables

| ชื่อตอนสร้าง (ไม่มี `%`) | ตอนอ้างอิง | Type |
|--------------------------|------------|------|
| `WorkingRoot` | `%WorkingRoot%` | Text |
| `BatchFiles` | `%BatchFiles%` | File list |
| `CurrentFile` | `%CurrentFile%` | File |
| `FileTable` | `%FileTable%` | Data table |
| `SummaryTable` | `%SummaryTable%` | Data table |
| `CurrentRow` | `%CurrentRow%` | Data row |
| `TotalAmount` | `%TotalAmount%` | Numeric |
| `RowCount` | `%RowCount%` | Numeric |
| `GrandTotal` | `%GrandTotal%` | Numeric |

## Expected Result

- Summary มี 3 แถว (หนึ่งต่อไฟล์) และยอดรวม 46500
- ไฟล์ต้นทางถูกย้าย/คัดลอกไป `processed\`

## Acceptance Criteria

- [ ] ใช้ For each ซ้อนหรือ For each + การรวมค่า
- [ ] ไม่คัดลอก action อ่านไฟล์แบบ hardcode ทีละไฟล์ 3 ชุดโดยไม่ลูป
- [ ] ตัวเลขตรง expected (`expected-batch-summary.csv` และ Grand total 46500)

## Troubleshooting

| อาการ | แก้ |
|-------|-----|
| Amount เป็น text | Convert text to number |
| Header นับเป็นแถว | Skip first line / set column names |
| ไฟล์ใน batch หายหลังรัน | คาดได้ถ้าใช้ Move — กู้จาก `assets/batch` ก่อนรันซ้ำ |
| Summary ว่าง | ตรวจว่า Insert row อยู่ภายใน For each ไฟล์ หลังลูปแถว |

## Cleanup

- กู้ batch จาก `assets/batch` ก่อนรันซ้ำ
- ลบ `C:\PAD-Labs\working\lab05` ได้หลังผ่านเกณฑ์ — คงต้นฉบับใน repo ไว้
