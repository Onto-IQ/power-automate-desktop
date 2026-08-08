# Lab 06 — Data Table & Excel

**วัน:** 2 · **ระดับ:** Intermediate  
**ทักษะ:** Launch Excel, Read/Write worksheet, Data table filter/sort/aggregate, **Run Excel macro**

## วัตถุประสงค์

- อ่าน Excel เป็น Data table
- แปลงข้อมูล (เพิ่มคอลัมน์, กรอง, สรุป)
- เขียนผลกลับเป็น sheet ใหม่
- (ตรงสไลด์) รัน Excel Macro จัดฟอร์แมตรายงาน

## Setup

1. Flow `Lab06_DataTableExcel`
2. คัดลอก workbook จาก `assets/` ไป `C:\PAD-Labs\working\lab06\`
3. เตรียม macro ตาม [`assets/vba/README.md`](assets/vba/README.md) → ได้ไฟล์ `sales-report.xlsm` ใน working
4. อย่าเขียนทับไฟล์ใน repo โดยตรง

## Input / Output

| | Path |
|--|------|
| Input workbook | [`assets/orders-input.xlsx`](assets/orders-input.xlsx) / CSV สำรอง |
| Macro source | [`assets/vba/FormatSummary.bas`](assets/vba/FormatSummary.bas) |
| Macro howto | [`assets/vba/README.md`](assets/vba/README.md) |
| Expected summary | [`assets/expected-summary.csv`](assets/expected-summary.csv) |
| Output | `C:\PAD-Labs\output\lab06\orders-report.xlsm` (หรือ `.xlsx` ถ้ายังไม่รัน macro) |

### Schema แผ่น `Orders`

ดู [`shared/DATA-SCHEMAS.md`](../../shared/DATA-SCHEMAS.md) ส่วน Orders Scout

โจทย์คำนวณ:

1. กรองเฉพาะ `Region = BKK` **หรือ** `Amount >= 10000`
2. เพิ่มคอลัมน์ `Tier` = `Gold` ถ้า Amount >= 12000 ไม่เช่นนั้น `Silver`
3. สรุปยอดรวม Amount ของชุดที่กรองแล้ว ลง sheet `Summary`
4. **Mission M — Excel Macro:** รัน `FormatSummary` เพื่อตัวหนา header / AutoFit / ไฮไลต์แถว Gold

## PAD Action Sequence (แนะนำ)

1. **Launch Excel** → เปิด working copy (แนะนำเป็น `.xlsm` ที่มี macro พร้อม)
2. **Read from Excel worksheet** sheet `Orders` → `%Orders%` (first line = column names)
3. สร้าง `%Filtered%` ว่าง
4. For each row:
   - If Region=BKK OR Amount>=10000 → ตั้ง Tier → Add row to `%Filtered%`
5. คำนวณ `%SumAmount%`
6. **Write to Excel worksheet**
   - sheet `Filtered` จาก `%Filtered%`
   - sheet `Summary` ค่า Label/Value
7. **Run Excel macro** → `FormatSummary`
8. **Save Excel** / **Close Excel**

> ถ้ายังไม่มี .xlsx: เปิด `orders-input.csv` ใน Excel แล้ว Save As `.xlsx`  
> สำหรับ Macro: ตาม `assets/vba/README.md` ให้ได้ `.xlsm`

## Variables

| Variable | Type |
|----------|------|
| `%Excel%` | Excel instance |
| `%Orders%` | Data table |
| `%Filtered%` | Data table |
| `%SumAmount%` | Numeric |
| `%Tier%` | Text |

## Expected Result

ตรงแนว `expected-summary.csv` (จำนวนแถวที่ผ่านเงื่อนไขและยอดรวม)  
หลัง macro: แถวหัวตารางตัวหนา และแถว Gold มีสีพื้น (ถ้าใช้ `FormatSummary.bas` เต็ม)

## Acceptance Criteria

- [ ] อ่าน/เขียนด้วย Excel actions
- [ ] ปิด Excel instance ทุกครั้ง
- [ ] มีอย่างน้อย 2 sheets ในไฟล์ผลลัพธ์
- [ ] **Mission M:** รัน **Run Excel macro** สำเร็จอย่างน้อย 1 ครั้ง (หรือวิทยากรตรวจว่า macro พร้อมแล้วแต่ถูกบล็อกโดยนโยบายเครื่อง)

## Troubleshooting

| อาการ | แก้ |
|-------|-----|
| File locked | ปิด Excel UI ที่เปิดไฟล์อยู่ |
| Column not found | ตรวจชื่อ header ให้ตรง |
| Number format | Convert text to number |
| Macro disabled / not found | ตรวจ Trust Center + ชื่อ macro = `FormatSummary` + ไฟล์เป็น `.xlsm` |
| VBA project access | ดูขั้นตอน import ใน `assets/vba/README.md` |

## Cleanup

- ลบไฟล์ใน working/output ได้หลังตรวจ
- ไม่ต้องปรับเว็บ Lab Hub สำหรับ Lab นี้
