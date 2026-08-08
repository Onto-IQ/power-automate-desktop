# Lab 07 — Contoso Invoice Ops (Desktop Element UI)

**วัน:** 2 · **ระดับ:** Advanced  
**ทักษะ:** Launch/Focus/Close Windows app, UI Elements & Selectors บน Desktop, Excel → Contoso → Excel, Conditions, Loops, File attachments, Error handling รายแถว, Subflows

## ทำไม Lab นี้สำคัญ

Lab อื่นใช้ **Web UI** จาก [PAD Lab Hub](https://ontoiq.tech/pad/)  
Lab นี้โฟกัส **Element UI บนแอป Windows จริง** ด้วย [Contoso Invoicing](https://github.com/MicrosoftDocs/mslearn-developer-tools-power-platform/tree/master/power-automate-desktop/contoso-invoice-app) จาก Microsoft Learn — เป็นแบบฝึก Desktop RPA ที่ครบและซับซ้อนขึ้น

## วัตถุประสงค์

- ติดตั้งและสำรวจ Contoso Invoicing ให้ครบเมนูหลัก
- Capture UI Elements ของแอป Desktop ให้เสถียร (ไม่พึ่ง Recorder อย่างเดียว)
- อ่านชุดใบแจ้งหนี้จาก Excel แล้วสร้างใน Contoso เป็นลูป
- ใช้เงื่อนไขธุรกิจ (validate / priority / skip)
- จัดการไฟล์แนบจำลองต่อ Invoice
- เขียนสถานะกลับ Excel + สรุปผล พร้อมกู้ error รายแถวโดยไม่ให้ทั้ง Flow ตาย

## Prerequisites

| รายการ | หมายเหตุ |
|--------|----------|
| PAD | พร้อม Desktop UI automation |
| Excel | อ่าน/เขียน workbook |
| Contoso Invoicing | ติดตั้งจาก zip ด้านล่าง |
| Lab 06 | แนะนำให้ทำมาก่อน (Data Table / Excel) |

## Setup — ติดตั้ง Contoso Invoicing

1. ดาวน์โหลด: [ContosoInvoicingSetup.zip](https://github.com/MicrosoftDocs/mslearn-developer-tools-power-platform/raw/master/power-automate-desktop/contoso-invoice-app/ContosoInvoicingSetup.zip)
2. Extract → รัน installer ตามวิซาร์ด
3. เปิดแอปจาก Start menu ค้นหา `Contoso Invoicing`
4. ปักหมุดที่ Taskbar (แนะนำ)
5. สำรวจ UI ด้วยมือ 5–10 นาที ก่อนเริ่ม Flow (ดู [`assets/ui-map.md`](assets/ui-map.md))

อ้างอิง setup ทางการ: [Microsoft Learn — Set up Contoso Invoicing](https://learn.microsoft.com/training/modules/input-parameters/2-set-up)

### Sample packs เสริมจาก Microsoft (ทางเลือก)

วางไว้ใน `C:\PAD-Labs\working\lab07\ms-samples\` ถ้าวิทยากรแจก/ให้ดาวน์โหลด:

| Zip | ใช้ประกอบ |
|-----|-----------|
| [SampleInvoices.zip](https://github.com/MicrosoftDocs/mslearn-developer-tools-power-platform/raw/master/power-automate-desktop/SampleInvoices.zip) | ชุดใบแจ้งหนี้ตัวอย่าง |
| [newinvoice.zip](https://github.com/MicrosoftDocs/mslearn-developer-tools-power-platform/raw/master/power-automate-desktop/newinvoice.zip) | เคส invoice ใหม่ |
| [Customers.zip](https://github.com/MicrosoftDocs/mslearn-developer-tools-power-platform/raw/master/power-automate-desktop/Customers.zip) | ข้อมูลลูกค้าอ้างอิง |
| [Orders.zip](https://github.com/MicrosoftDocs/mslearn-developer-tools-power-platform/raw/master/power-automate-desktop/Orders.zip) | ออเดอร์อ้างอิง |
| [Employees.zip](https://github.com/MicrosoftDocs/mslearn-developer-tools-power-platform/raw/master/power-automate-desktop/Employees.zip) | พนักงานอ้างอิง |

ใน Lab Kit นี้มี **mock ครบใน `assets/`** อยู่แล้ว — sample packs ด้านบนเป็นของเสริมให้ใกล้เคียงคอร์ส Microsoft

## Setup — โฟลเดอร์ทำงาน

1. สร้าง Flow ชื่อ `Lab07_ContosoInvoiceOps`
2. คัดลอก `assets/` → `C:\PAD-Labs\working\lab07\`
3. สร้าง `C:\PAD-Labs\output\lab07\` และ `C:\PAD-Labs\logs\lab07\`

## Input / Output

| | Path |
|--|------|
| Invoice batch | [`assets/invoices-batch.csv`](assets/invoices-batch.csv) / [`assets/invoices-batch.xlsx`](assets/invoices-batch.xlsx) |
| Business rules | [`assets/business-rules.md`](assets/business-rules.md) |
| UI map | [`assets/ui-map.md`](assets/ui-map.md) |
| Mock attachments | [`assets/attachments/`](assets/attachments/) |
| Inbox notes | [`assets/invoices-inbox/`](assets/invoices-inbox/) |
| Expected | [`assets/expected/expected-results.csv`](assets/expected/expected-results.csv) |
| Your output | `C:\PAD-Labs\output\lab07\invoice-run-results.xlsx` |
| Log | `C:\PAD-Labs\logs\lab07\contoso-run-log.csv` |

## Business Rules (ต้อง implement ใน Flow)

| Rule | เงื่อนไข | Action |
|------|----------|--------|
| R1 Validate | `Account` ว่าง **หรือ** `Amount` ไม่ใช่ตัวเลข / <= 0 | `Status=Rejected`, ไม่เปิดฟอร์ม Contoso |
| R2 Skip seeded | `ProcessFlag=Skip` | ข้ามแถว, `Status=Skipped` |
| R3 Priority | `Amount >= 10000` | ใส่ `Priority=High` และตั้ง Status ในแอปตาม UI map (เช่น Paid / Open ตามที่หน้าจอรองรับ) |
| R4 Standard | ผ่าน R1 และไม่ Skip | สร้าง invoice ปกติ `Priority=Normal` |
| R5 Attachment | มีไฟล์ใน `attachments\{InvoiceId}.*` | Copy ไป `output\lab07\filed\{InvoiceId}\` หลังสร้างสำเร็จ |
| R6 Continue on error | UI ของแถวล้มเหลว | Log error ของแถวนั้น แล้วทำแถวถัดไป |

รายละเอียด: [`assets/business-rules.md`](assets/business-rules.md)

## PAD Action Sequence (แนะนำ — ซับซ้อน / ครบ)

### A. Init
1. ตั้ง `%WorkingRoot%`, `%OutputRoot%`, `%LogPath%`
2. Create folder ถ้ายังไม่มี: `filed`, logs
3. อ่าน Excel/CSV → `%Invoices%`
4. สร้าง `%Results%` (คอลัมน์ตาม expected)
5. เขียน header log

### B. Launch Contoso (ครั้งเดียว)
1. **Run application** ไปยัง path ของ Contoso Invoicing  
   (หาจาก Start Menu / Task Manager → Open file location แล้วเก็บใน `%ContosoPath%`)
2. **Wait for window content** จนหน้าต่างหลักพร้อม
3. **Focus window** Contoso
4. Capture UI Elements สำคัญเก็บใน repository ของ Flow (ดู ui-map)

### C. Process loop
สำหรับแต่ละแถวใน `%Invoices%`:

1. **On block error** ครอบทั้งแถว
2. Evaluate R1–R2 ด้วย If/Else → ถ้า Rejected/Skipped บันทึก Results แล้ว `Next`
3. Navigate ไปหน้าสร้าง Invoice (เมนู/ปุ่มตาม ui-map)
4. **Populate text field in window** / Set drop-down สำหรับ Account, Contact, Amount, Date, Status
5. Save / Submit invoice
6. (ถ้าทำได้) อ่านค่า confirmation หรือตรวจว่าแถวโผล่ใน grid
7. ทำ R5 แนบ/คัดลอกไฟล์
8. Add row ลง `%Results%` = `Created` / `Created-HighPriority`
9. On error: **Get last error** → `%LastError%` → append log ด้วย `%LastError.Message%` → Results=`Failed` → continue

### D. Post-process
1. (Challenge) **Extract data from window** จาก invoice grid บางส่วนเทียบกับจำนวนที่ Created
2. เขียน `%Results%` ลง Excel (`Results` sheet) + `Summary` (นับ Created/Rejected/Skipped/Failed)
3. **Close window** Contoso (ถ้าค้างใช้ **Terminate process** อย่างระวัง)
4. **Close Excel**

### E. Optional Outlook ping
สร้าง Draft หัวข้อ `[PAD-LAB-MOCK] Contoso Invoice Ops — {CreatedCount} created` สรุปสั้น ๆ (แนวเดียวกับ Capstone)

## Subflows ที่ควรแยก

| Subflow | หน้าที่ |
|---------|---------|
| `SF_InitPaths` | path + folders |
| `SF_LaunchContoso` | launch/focus/wait ready |
| `SF_ValidateInvoiceRow` | R1–R2 คืนค่า decision |
| `SF_CreateContosoInvoice` | กรอก+บันทึก UI |
| `SF_FileAttachment` | copy attachment ตาม InvoiceId |
| `SF_WriteResults` | Excel + summary |
| `SF_LogRowError` | เขียน log รายแถว |

## Variables

| Variable | Type | ความหมาย |
|----------|------|----------|
| `%ContosoPath%` | Text | path ไฟล์ .exe ของแอป |
| `%ContosoApp%` | Window/App instance | ตาม action ที่ใช้ |
| `%Invoices%` | Data table | input |
| `%Results%` | Data table | output |
| `%InvoiceId%` | Text | รหัสแถวปัจจุบัน |
| `%Priority%` | Text | High/Normal |
| `%RowDecision%` | Text | Create / Reject / Skip |
| `%CreatedCount%` | Numeric | สรุป |
| `%FailedCount%` | Numeric | สรุป |
| `%LastError%` | Text | error ล่าสุด |

## Expected Result

เทียบ [`assets/expected/expected-results.csv`](assets/expected/expected-results.csv):

- แถว invalid → `Rejected`
- แถว Skip → `Skipped`
- แถวปกติ → `Created` ใน Contoso
- แถว Amount สูง → `Created` + `Priority=High`
- มีไฟล์ผลลัพธ์ + log
- แอป Contoso ถูกปิดท้าย Flow

## Acceptance Criteria

- [ ] ติดตั้ง Contoso ได้และ Launch จาก Flow ได้
- [ ] UI Elements ของฟอร์ม Invoice ถูก capture เอง (ไม่พึ่งค่า hardcodeพิกัดจอ)
- [ ] อ่านจาก Excel/CSV เป็นลูป
- [ ] Implement กฎ R1–R6 ครบ
- [ ] มี Results + Summary ออกไฟล์
- [ ] Error รายแถวแล้ว Flow ไปต่อได้
- [ ] มีอย่างน้อย 3 Subflows
- [ ] (Challenge) มี attachment filing หรือ Outlook Draft

## Troubleshooting

| อาการ | แก้ |
|-------|-----|
| หา Contoso exe ไม่เจอ | เปิดแอปมือ → Task Manager → Open file location แล้วใส่ path ใน `%ContosoPath%` |
| Selector หลุดหลังอัปเดตแอป | Recapture UI element; หลีกเลี่ยง index อย่างเดียว |
| หน้าต่างถูกบัง | Focus window / Set window state = Normal/Maximized |
| กรอก Amount ไม่ติด | ส่งเป็น text ที่ format ตามแอป; Tab ออกจากฟิลด์ก่อน Save |
| แอปค้างหลาย instance | **Terminate process** ก่อน **Run application** ใหม่ |
| Contoso เปิดไม่ได้ / exception | ตรวจไฟล์ Excel ใต้ `Documents\Contoso Invoicing` — Sensitivity อย่าเป็น Confidential ([Q&A](https://learn.microsoft.com/answers/questions/2244882/how-to-resolve-contoso-invoicing-app-issue)) |
| Excel locked | ปิด workbook ที่เปิดซ้อน |
| UIPI / ส่ง input ไม่ได้ | รัน PAD กับ Contoso ที่สิทธิ์ elevation เดียวกัน |

## Cleanup

- ปิด Contoso / Excel ที่ค้าง
- ข้อมูล invoice ที่สร้างใน Contoso เป็นของ Lab — ล้างตามที่วิทยากรแนะนำก่อนรอบสาธิตถัดไป
- อย่า commit output/logs ส่วนตัว

## อ้างอิง

- App: [contoso-invoice-app](https://github.com/MicrosoftDocs/mslearn-developer-tools-power-platform/tree/master/power-automate-desktop/contoso-invoice-app)
- Learn setup: https://learn.microsoft.com/training/modules/input-parameters/2-set-up
- Web UI คู่ขนาน (Lab อื่น): https://ontoiq.tech/pad/
