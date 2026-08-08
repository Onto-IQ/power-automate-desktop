# Contoso Invoicing — UI Map (Lab 07)

แผนที่องค์ประกอบสำหรับ capture ใน PAD  
ชื่อบนหน้าจออาจต่างเล็กน้อยตามเวอร์ชัน installer — ให้ยึดสิ่งที่เห็นในแอปจริงเป็นหลัก

## หน้าต่างหลัก

| Element (ตั้งชื่อใน PAD) | การใช้งาน |
|--------------------------|-----------|
| `Win_ContosoMain` | หน้าต่างหลักหลัง Launch |
| `Btn_Invoices` / `Menu_Invoices` | เข้าโมดูล Invoices |
| `Btn_NewInvoice` | เปิดฟอร์มสร้างใหม่ |
| `Grid_InvoiceList` | รายการ invoice (สำหรับ extract/verify) |

## ฟอร์ม New Invoice (ค่าที่ Lab ใช้)

| PAD name | Map จาก Excel | หมายเหตุ |
|----------|---------------|----------|
| `Txt_Account` | Account | บังคับ |
| `Txt_Contact` | Contact | บังคับถ้ามีบนฟอร์ม |
| `Txt_Amount` | Amount | ตัวเลข |
| `Txt_Date` หรือ `Date_InvoiceDate` | InvoiceDate | ใช้รูปแบบที่แอปยอมรับ |
| `Cmb_Status` / `Txt_Status` | StatusToSet | Open / Paid / Other ตาม control จริง |
| `Btn_Save` / `Btn_Submit` | — | บันทึก |

## ลำดับคลิกที่แนะนำ

```text
Launch Contoso
→ Wait Win_ContosoMain
→ Invoices
→ New Invoice
→ Populate fields
→ Save
→ (optional) กลับ list แล้วตรวจสอบ
```

## แนวทาง Selector บน Desktop

1. ใช้ UI element picker ของ PAD บนหน้าต่าง Contoso
2. ตั้งชื่อ element ให้สื่อบทบาท (ตารางด้านบน)
3. หลีกเลี่ยงการคลิกด้วยพิกัดจอเป็นหลัก
4. หลัง Save ให้ Wait จนฟอร์มปิดหรือแถวใหม่พร้อม

## ตรวจสุขภาพแอปก่อนเริ่ม Lab

- [ ] เปิด Contoso ด้วยมือได้
- [ ] สร้าง invoice 1 ใบด้วยมือสำเร็จ
- [ ] ปิดแอปแล้วเปิดใหม่ได้โดยไม่ error
