# Business Rules — Lab 07 Contoso Invoice Ops

## R1 — Validate

Reject เมื่อ:

- `Account` ว่างหลัง Trim
- `Amount` ว่าง, ไม่ใช่ตัวเลข, หรือ `Amount <= 0`

ผล: `Status=Rejected`, `ContosoRef=`ว่าง, ไม่ต้องแตะ UI Contoso

## R2 — Skip

ถ้า `ProcessFlag=Skip` → `Status=Skipped` (มีลำดับก่อน Create)

## R3 — Priority High

ถ้าผ่าน validate และ `Amount >= 10000`:

- `%Priority% = High`
- พยายามตั้ง Status ใน Contoso เป็นค่าที่ธุรกิจกำหนดในแถว `StatusToSet` (ค่าเริ่มต้นแนะนำ `Paid` ถ้ามีใน UI)
- Notes ต้องมีข้อความ `HIGH PRIORITY`

## R4 — Standard create

นอกนั้น `%Priority% = Normal` และใช้ `StatusToSet` จากแถว (ค่าเริ่มต้น `Open`)

## R5 — Attachment filing

หลัง `Created*`:

1. หาไฟล์ใน `working\lab07\attachments` ที่ชื่อขึ้นต้นด้วย `InvoiceId`
2. ถ้าเจอ → สร้างโฟลเดอร์ `output\lab07\filed\{InvoiceId}\` แล้ว Copy เข้าไป
3. ใส่ `AttachmentFiled=Yes/No` ใน Results

## R6 — Continue on error

ทุกแถวอยู่ใน On block error (นโยบาย Continue):

- ใน handler: **SET เท่านั้น** — เช่น `RowFailed=True`, `Status=Failed` (ห้าม Increase / File / Get last error ในนี้)
- นอก handler เมื่อ `RowFailed`: **Get last error** → ใส่ `%LastError.Message%` ใน `ErrorMessage` → log / Results → ไปแถวถัดไป
- ห้าม Terminate ทั้ง Flow ยกเว้น Contoso Launch ล้มเหลวตั้งแต่ต้น (Fatal)
- แพทเทิร์นนี้ Lab 09 / 09b จะทบทวนต่อ (flag ใน handler → Get last error / log นอกบล็อก)

## สรุป Summary sheet

| Metric | ความหมาย |
|--------|----------|
| CreatedCount | รวม Created + Created-HighPriority |
| RejectedCount | R1 |
| SkippedCount | R2 |
| FailedCount | UI/runtime error |
| HighPriorityCount | Priority=High ที่สร้างสำเร็จ |
