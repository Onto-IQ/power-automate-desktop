# Contoso Invoicing — UI Map (Lab 07)

แผนที่องค์ประกอบสำหรับ capture ใน PAD  
ชื่อบนหน้าจออาจต่างเล็กน้อยตามเวอร์ชัน installer — ให้ยึดสิ่งที่เห็นในแอปจริงเป็นหลัก

**Catch-up script** [`scripts/07-contoso-invoice-ops.robin`](../scripts/07-contoso-invoice-ops.robin) **ฝัง Contoso UI Elements มาให้แล้ว** (บล็อก `ControlRepository` ท้ายไฟล์) — วางใน flow ว่างแล้วควรขึ้นในแท็บ UI elements โดยชื่อด้านล่าง ถ้า selector หลุดค่อย Recapture/Rename



## หน้าต่างหลัก

| PAD name | การใช้งาน | Hint จาก Contoso (Automation Id / ชื่อตอน capture) |
|----------|-----------|------------------------------------------------------|
| Screen: `Contoso Invoicing` | หน้าต่างหลักหลัง Launch | Window name = `Contoso Invoicing`, Process = `LegacyInvoicingApp` |
| `Btn_Invoices` | เข้าโมดูล Invoices | Text `Invoices` ใน TreeView |
| `Btn_NewInvoice` | เปิดฟอร์มสร้างใหม่ | `btnNew` / NewFileIcon / Image New |
| `Grid_InvoiceList` | รายการ invoice (challenge) | Data grid หลัง Save |

## ฟอร์ม New Invoice (ค่าที่ Lab ใช้)

| PAD name | Map จาก Excel | Hint / Automation Id |
|----------|---------------|----------------------|
| `Txt_Date` | InvoiceDate | `txtDate*` — แนะนำรูปแบบ `MM/DD/YYYY` |
| `Txt_Account` | Account | `txtAccount*` / CompanyAccount |
| `Txt_Contact` | Contact | `txtContact*` / Mail (ชื่อหรืออีเมลตามฟิลด์จริง) |
| `Txt_Amount` | Amount | `txtAmount*` — ส่งเป็นตัวเลขข้อความ |
| `Cmb_Status` | StatusToSet | `cmbStatusChooser*` — ค่าเช่น `Open` / `Paid` |
| `Btn_Save` | — | `btnSave` / SaveIcon / Image Save |

## ลำดับคลิกที่แนะนำ (สไตล์ Microsoft Contoso sample)

```text
Launch Contoso (+ WorkingDirectory ของโฟลเดอร์ exe)
→ Wait for window title Contoso Invoicing + Focus
→ Click Btn_Invoices
→ Click Btn_NewInvoice
→ Populate Txt_Date → Txt_Account → Txt_Contact → Txt_Amount
→ Set drop-down Cmb_Status (High→Paid, Normal→Open)
→ Click Btn_Save
→ Close window ท้าย flow
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
