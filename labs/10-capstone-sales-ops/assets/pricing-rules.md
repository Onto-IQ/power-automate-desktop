# Pricing Rules — Capstone (ตรงสไลด์ Evaluation Matrix)

ใช้กับข้อมูลที่ Scout จาก Web (03-table + 09-ajax / หรือ catalog เมื่อมี)

## สูตร

สำหรับแต่ละแถวที่มี `Amount` (หรือราคา):

1. `DiscountRate`
   - ถ้า `Amount >= 15000` → `0.10`
   - ถ้า `Amount >= 10000` → `0.05`
   - อื่น ๆ → `0.00`
2. `DiscountAmount` = `Amount * DiscountRate`
3. `NetBeforeTax` = `Amount - DiscountAmount`
4. `TaxRate` = `0.07` (VAT 7%)
5. `TaxAmount` = `NetBeforeTax * TaxRate`
6. `GrandTotal` = `NetBeforeTax + TaxAmount`

## Sheet ที่ต้องมีในรายงาน

| Sheet | เนื้อหา |
|-------|---------|
| `Products` / `Scout` | ข้อมูลดิบจากเว็บ |
| `Priced` | หลังคำนวณคอลัมน์ด้านบน |
| `Summary` | Sum Amount, Sum Discount, Sum Tax, Sum GrandTotal, SubmittedCount, MailStatus |

## เกณฑ์ผ่าน (จากสไลด์ Capstone)

| หมวด | เกณฑ์ |
|------|------|
| Web Scraping | ดึงครบจากอย่างน้อย 2 แหล่ง (หรือ multi-page เมื่อมี catalog) |
| Excel Processing | ส่วนลด/ภาษีถูกต้องตามตารางนี้ |
| Error Handling | มี On-block error + log |
| Output & Notification | มีไฟล์รายงาน + Outlook Draft แนบไฟล์ |
