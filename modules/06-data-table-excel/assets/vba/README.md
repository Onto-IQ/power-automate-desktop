# How to enable Excel Macro for Lab 06

PAD action: **Run Excel macro** ต้องการ workbook ที่เป็น `.xlsm` และมี macro ชื่อ `FormatSummary`

> **สำคัญ:** อย่าตั้งชื่อ VBA **module** ว่า `FormatSummary` ถ้า Sub ก็ชื่อ `FormatSummary` — Excel/PAD จะรันไม่สำเร็จ (ต้องเรียก `ModuleName.FormatSummary`)  
> ไฟล์ [`FormatSummary.bas`](FormatSummary.bas) ใช้ชื่อ module = `Lab06Macros` แล้ว

## วิธีเตรียม (ครั้งเดียวต่อเครื่องวิทยากร/ผู้เรียน)

### ตัวเลือก A — Import `.bas`

1. เปิด Excel → สร้างไฟล์ว่าง → Save As `sales-report.xlsm` (Excel Macro-Enabled Workbook)
2. เตรียม 3 แผ่น: `Orders` (ข้อมูล), `Filtered` (ว่าง), `Summary` (ว่าง) — catch-up script **ไม่** Add worksheet ตอนรัน (กัน error ชื่อซ้ำตอนรันซ้ำ)
3. กด `Alt+F11` เปิด VBA Editor
4. File → Import File → เลือก [`FormatSummary.bas`](FormatSummary.bas) → ได้ module `Lab06Macros`
5. Save แล้วปิด Excel
6. คัดลอก `sales-report.xlsm` ไป `C:\PAD-Labs\working\lab06\`

### ตัวเลือก B — พิมพ์มือสั้น ๆ

ใน VBA module ใหม่ (ตั้งชื่อ module อื่น เช่น `Lab06Macros` — **ห้าม**ชื่อ `FormatSummary`) วาง:

```vb
Public Sub FormatSummary()
    Sheets(1).Rows(1).Font.Bold = True
    Sheets(1).Columns("A:Z").AutoFit
End Sub
```

บันทึกเป็น `.xlsm`

## ใน PAD (หลังเขียน Filtered sheet แล้ว)

1. ถ้าผลลัพธ์เป็น `.xlsx` — **Save As** เป็น `.xlsm` ที่เตรียมไว้ หรือเขียนลง workbook `.xlsm` ตั้งแต่ต้น
2. Action **Run Excel macro**
   - Macro: `FormatSummary`
   - Excel instance: `%Excel%`
3. Save + **Close Excel**

## นโยบายความปลอดภัย

- Lab ใช้ macro ที่เราสร้างเองเท่านั้น
- อาจต้องตั้ง Trust Center → Enable macros สำหรับไฟล์ในโฟลเดอร์ Lab (ตามนโยบายองค์กร)
