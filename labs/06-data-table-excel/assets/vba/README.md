# How to enable Excel Macro for Lab 06

PAD action: **Run Excel macro** ต้องการ workbook ที่เป็น `.xlsm` และมี macro ชื่อ `FormatSummary`

## วิธีเตรียม (ครั้งเดียวต่อเครื่องวิทยากร/ผู้เรียน)

### ตัวเลือก A — Import `.bas`

1. เปิด Excel → สร้างไฟล์ว่าง → Save As `sales-report.xlsm` (Excel Macro-Enabled Workbook)
2. กด `Alt+F11` เปิด VBA Editor
3. File → Import File → เลือก [`FormatSummary.bas`](FormatSummary.bas)
4. Save แล้วปิด Excel
5. คัดลอก `sales-report.xlsm` ไป `C:\PAD-Labs\working\lab06\`

### ตัวเลือก B — พิมพ์มือสั้น ๆ

ใน VBA module ใหม่ วาง:

```vb
Sub FormatSummary()
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
