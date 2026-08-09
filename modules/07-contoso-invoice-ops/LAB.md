# Lab 07 — Contoso Invoice Ops (Hands-on)

**อ่านก่อน:** [LESSON.md](LESSON.md) · **หน้าปกบท:** [README.md](README.md) · **พื้นฐาน:** [`shared/PAD-FUNDAMENTALS.md`](../../shared/PAD-FUNDAMENTALS.md)

**วัน:** 2 · **ระดับ:** Advanced  
**ทักษะ:** Run application / Focus / Close บน Windows app, UI Elements & Selectors บน Desktop, Excel → Contoso → Excel, Conditions, Loops, ไฟล์แนบ, Error handling รายแถว และ Subflows

## อ้างอิง (Aug 2026)

| แหล่ง | URL |
|-------|-----|
| Contoso setup (Learn) | [Set up Contoso Invoicing](https://learn.microsoft.com/training/modules/input-parameters/2-set-up) |
| Contoso sample app | [contoso-invoice-app (GitHub)](https://github.com/MicrosoftDocs/mslearn-developer-tools-power-platform/tree/master/power-automate-desktop/contoso-invoice-app) |
| UI automation actions | [actions-reference/uiautomation](https://learn.microsoft.com/power-automate/desktop-flows/actions-reference/uiautomation) |
| Handle errors | [desktop-flows/errors](https://learn.microsoft.com/power-automate/desktop-flows/errors) |

## Setup — ติดตั้ง Contoso Invoicing

1. ดาวน์โหลด: [ContosoInvoicingSetup.zip](https://github.com/MicrosoftDocs/mslearn-developer-tools-power-platform/raw/master/power-automate-desktop/contoso-invoice-app/ContosoInvoicingSetup.zip)
2. Extract → รัน installer ตามวิซาร์ด
3. เปิดแอปจาก Start menu ค้นหา (คัดลอกได้):

```text
Contoso Invoicing
```

4. ปักหมุดที่ Taskbar (แนะนำ)
5. สำรวจ UI ด้วยมือ 5–10 นาที ก่อนเริ่ม Flow (ดู [`assets/ui-map.md`](assets/ui-map.md))

อ้างอิง setup ทางการ: [Microsoft Learn — Set up Contoso Invoicing](https://learn.microsoft.com/training/modules/input-parameters/2-set-up)

### Sample packs เสริมจาก Microsoft (ทางเลือก)

วางไว้ในโฟลเดอร์นี้ถ้าวิทยากรแจก/ให้ดาวน์โหลด:

```text
C:\PAD-Labs\working\lab07\ms-samples\
```

| Zip | ใช้ประกอบ |
|-----|-----------|
| [SampleInvoices.zip](https://github.com/MicrosoftDocs/mslearn-developer-tools-power-platform/raw/master/power-automate-desktop/SampleInvoices.zip) | ชุดใบแจ้งหนี้ตัวอย่าง |
| [newinvoice.zip](https://github.com/MicrosoftDocs/mslearn-developer-tools-power-platform/raw/master/power-automate-desktop/newinvoice.zip) | เคส invoice ใหม่ |
| [Customers.zip](https://github.com/MicrosoftDocs/mslearn-developer-tools-power-platform/raw/master/power-automate-desktop/Customers.zip) | ข้อมูลลูกค้าอ้างอิง |
| [Orders.zip](https://github.com/MicrosoftDocs/mslearn-developer-tools-power-platform/raw/master/power-automate-desktop/Orders.zip) | ออเดอร์อ้างอิง |
| [Employees.zip](https://github.com/MicrosoftDocs/mslearn-developer-tools-power-platform/raw/master/power-automate-desktop/Employees.zip) | พนักงานอ้างอิง |

ใน Lab Kit นี้มี **mock ครบใน `assets/`** อยู่แล้ว — sample packs ด้านบนเป็นของเสริมให้ใกล้เคียงคอร์ส Microsoft

## Setup บนเครื่อง (โฟลเดอร์ทำงาน)

1. สร้างโฟลเดอร์ (คัดลอกได้):

```text
C:\PAD-Labs\working\lab07\
```

```text
C:\PAD-Labs\output\lab07\
```

```text
C:\PAD-Labs\logs\lab07\
```

2. คัดลอกทั้งโฟลเดอร์ [`assets/`](assets/) ไปยัง:

```text
C:\PAD-Labs\working\lab07\
```

3. สร้างโฟลเดอร์ว่าง (ถ้ายังไม่มี):

```text
C:\PAD-Labs\output\lab07\filed
```

4. จด path ของ Contoso `.exe` (เปิดแอปมือ → Task Manager → Open file location) ไว้ใส่ Value ของ `ContosoPath` (อ้างอิงด้วย `%ContosoPath%`)

## Input / Output

| | Path |
|--|------|
| Invoice batch | [`assets/invoices-batch.csv`](assets/invoices-batch.csv) / [`assets/invoices-batch.xlsx`](assets/invoices-batch.xlsx) |
| Business rules | [`assets/business-rules.md`](assets/business-rules.md) |
| UI map | [`assets/ui-map.md`](assets/ui-map.md) |
| Mock attachments | [`assets/attachments/`](assets/attachments/) |
| Inbox notes | [`assets/invoices-inbox/`](assets/invoices-inbox/) |
| Expected | [`assets/expected/expected-results.csv`](assets/expected/expected-results.csv) |
| Your output | ดู code block ใน Step 9 |
| Log | ดู code block ใน Step 1 |

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

เกณฑ์ผ่าน: มีอย่างน้อย **3 Subflows** จากตารางด้านบน

---

## Hands-on ทีละขั้น

### Step 0 — สร้าง flow และ UI Elements

1. เปิด Power Automate for desktop → **New flow**
2. ชื่อ flow (คัดลอกได้):

```text
Lab07_ContosoInvoiceOps
```

3. กด **Create**
4. เปิด Contoso ด้วยมือ → ใน designer ใช้เครื่องมือ capture **UI Elements** ตาม [`assets/ui-map.md`](assets/ui-map.md)  
   (ฟอร์ม Invoice: Account, Contact, Amount, Date, Status, ปุ่ม Save/Submit, เมนูสร้าง Invoice)
5. สร้าง Subflows ตามตารางด้านบน (อย่างน้อย 3 ชื่อ) จากแถบ Subflows

> **กฎตัวแปรใน PAD (อ่านก่อนทำ Step ถัดไป)**  
> - ช่อง **Name** ของ **Set variable**, ส่วน **Variables produced**, และ **Store into** = พิมพ์ชื่ออย่างเดียว **ไม่มี `%`** เช่น `WorkingRoot`  
> - ช่องอื่นที่ต้องดึงค่าตัวแปร (Folder, File path, Text, …) = ใช้ `%WorkingRoot%` (**มี `%` ครบสองด้าน**)  
> - หลังสร้างแล้ว Variables pane อาจแสดงเป็น `%WorkingRoot%` — เป็นเรื่องปกติ

### Step 1 — SF_InitPaths: path และโฟลเดอร์

วางใน subflow `SF_InitPaths` (หรือต้น Main แล้วค่อยย้าย):

1. ลาก **Set variable** (Name ไม่มี `%`):
   - Name: `WorkingRoot` ← Value:

```text
C:\PAD-Labs\working\lab07
```

   - Name: `OutputRoot` ← Value:

```text
C:\PAD-Labs\output\lab07
```

   - Name: `LogPath` ← Value:

```text
C:\PAD-Labs\logs\lab07\contoso-run-log.csv
```

   - Name: `ContosoPath` ← Value: path `.exe` จริงบนเครื่องคุณ (คัดลอกจาก Task Manager → Open file location)
   - Name: `CreatedCount` ← Value:

```text
0
```

   - Name: `FailedCount` ← Value:

```text
0
```

     (และตัวนับอื่นตามต้องการ)

2. สำหรับแต่ละโฟลเดอร์ที่ต้องมี (`filed`, logs ถ้ายังไม่มี):
   - **If folder exists** → path ตามต้องการ เช่น:

```text
%OutputRoot%\filed
```

   - **Else** → **Create folder**
   - **End**

### Step 2 — อ่าน batch และเตรียม Results / log header

1. ลาก **Launch Excel** → Document path (คัดลอก):

```text
%WorkingRoot%\invoices-batch.xlsx
```

   (หรือแปลงจาก CSV)
2. **Variables produced:** `ExcelIn` ← **ไม่ใส่ `%`** (อ้างอิงด้วย `%ExcelIn%`)
3. ลาก **Read from Excel worksheet**
   - Worksheet: แผ่นที่มีข้อมูล batch (หรือชื่อที่คุณตั้ง)
   - First line contains column names: เปิด
4. **Variables produced:** `Invoices` ← **ไม่ใส่ `%`** (อ้างอิงด้วย `%Invoices%`)
5. **Create new data table** → **Variables produced:** `Results` ← **ไม่ใส่ `%`** คอลัมน์ให้สอดคล้อง [`assets/expected/expected-results.csv`](assets/expected/expected-results.csv)
6. เขียน header log ด้วย **Write text to file** ที่ File path:

```text
%LogPath%
```

   (If file exists: Overwrite ในรอบเริ่มต้น หรือตามนโยบาย append ที่ชัด)
7. **Close Excel** ของ input ถ้าไม่ใช้ instance นี้ต่อ (หรือเก็บไว้ถ้าจะเขียนผลลงไฟล์เดิมแยก sheet)

ใน Main: **Run subflow** `SF_InitPaths` ก่อนเข้าส่วนนี้

### Step 3 — SF_LaunchContoso: เปิดแอปครั้งเดียว

วางใน `SF_LaunchContoso`:

1. (แนะนำ) ถ้ามี instance ค้าง: **Terminate process** ชื่อกระบวนการ Contoso — ใช้อย่างระวัง
2. ลาก **Run application**
   - Application path: (คัดลอก)

```text
%ContosoPath%
```

3. ลาก **Wait for window content** จนหน้าต่างหลักพร้อม (เลือก UI element / title ตาม ui-map)
4. ลาก **Focus window** ไปที่ Contoso
5. ตรวจด้วยตาว่าแอปพร้อมก่อนไปลูป

ใน Main: **Run subflow** `SF_LaunchContoso` **ครั้งเดียวก่อน** For each

### Step 4 — ลูปประมวลผลทีละแถว + On block error (R6)

1. ใน Main ลาก **For each**
   - Value to iterate: (คัดลอก)

```text
%Invoices%
```

   - Store into: `CurrentInvoice` ← **ไม่ใส่ `%`**
2. **ภายใน For each** ตั้งตัวแปร Name: `InvoiceId` ← **ไม่ใส่ `%`** จากคอลัมน์ของแถว (อ้างอิงด้วย `%InvoiceId%`)
3. ลาก **On block error** ครอบทั้งชุดงานของแถว (ตั้งแต่ validate จนถึงบันทึก Results)
4. ในนโยบายของบล็อก: เมื่อ error → ไปรันขั้นตอนกู้ (หรือ **Run subflow** `SF_LogRowError`) แล้ว **Continue** แถวถัดไป — **ห้าม** Terminate ทั้ง flow เพราะ UI แถวเดียวพัง

### Step 5 — SF_ValidateInvoiceRow: R1–R2

ภายใน On block error / เรียก subflow `SF_ValidateInvoiceRow`:

1. **If** Account ว่างหลัง Trim **หรือ** Amount ไม่ใช่ตัวเลข / <= 0  
   → **Set variable** Name: `RowDecision` ← Value:

```text
Reject
```

   Name: `Status` ← Value:

```text
Rejected
```

   ← **ไม่ใส่ `%` ใน Name** → ไม่แตะ Contoso UI

2. **Else if** `ProcessFlag` Equal to (คัดลอก):

```text
Skip
```

   → Name: `RowDecision` ← Value:

```text
Skip
```

   Name: `Status` ← Value:

```text
Skipped
```

3. **Else** → Name: `RowDecision` ← Value:

```text
Create
```

4. ถ้า Reject/Skip: **Insert row into data table** (คัดลอก):

```text
%Results%
```

   แล้วข้ามไปแถวถัดไป (อย่าเรียก Create UI)

### Step 6 — R3/R4 + SF_CreateContosoInvoice

เมื่อเงื่อนไข `%RowDecision%` Equal to (คัดลอก):

```text
Create
```

1. **If** Amount >= (คัดลอก):

```text
10000
```

   → **Set variable** Name: `Priority` ← Value:

```text
High
```

   (R3) ← **ไม่ใส่ `%` ใน Name**

   **Else** → Name: `Priority` ← Value:

```text
Normal
```

   (R4)

2. ใน `SF_CreateContosoInvoice`:
   - Navigate ไปหน้าสร้าง Invoice (เมนู/ปุ่มตาม ui-map) ด้วย **Click UI element in window** / **Press button in window**
   - **Wait for window content** จนฟอร์มพร้อม
   - **Populate text field in window** สำหรับ Account, Contact, Amount, Date ตามคอลัมน์แถว
   - ตั้ง Status / Priority ตาม UI map และ `StatusToSet` (High → พยายาม `Paid` หรือค่าที่หน้าจอรองรับ; Normal → `Open` เป็นต้น)
   - Save / Submit ด้วย **Click UI element in window** หรือ **Press button in window**
3. (ถ้าทำได้) อ่าน confirmation หรือตรวจแถวใน grid
4. ตั้ง Status ผลลัพธ์ — Value:

```text
Created
```

   หรือ

```text
Created-HighPriority
```

   + Notes มีข้อความ (คัดลอกถ้าใช้):

```text
HIGH PRIORITY
```

   เมื่อเป็น High
5. **Increase variable** เลือก `CreatedCount` (ไม่มี `%` ในรายการเลือก)

### Step 7 — R5: SF_FileAttachment

หลังสร้างสำเร็จ:

1. ใน `SF_FileAttachment` ใช้ **Get files in folder**
   - Folder: (คัดลอก)

```text
%WorkingRoot%\attachments
```

   - File filter: (คัดลอก — หรือกรองชื่อขึ้นต้นด้วย InvoiceId)

```text
%InvoiceId%*
```

2. **If** มีไฟล์:
   - **If folder exists** / **Create folder** → path (คัดลอก):

```text
%OutputRoot%\filed\%InvoiceId%
```

   - **Copy file(s)** → โฟลเดอร์นั้น
   - ตั้ง Name: `AttachmentFiled` ← Value:

```text
Yes
```

3. **Else** → Name: `AttachmentFiled` ← Value:

```text
No
```

4. **Insert row into data table** (คัดลอก):

```text
%Results%
```

### Step 8 — กู้ error รายแถว (Get last error)

ภายในกิ่ง error ของ **On block error** (หรือ `SF_LogRowError`):

1. ลาก **Get last error**
2. **Variables produced:** `LastError` ← **ไม่ใส่ `%`** (ชนิด Error; อ้างอิงด้วย `%LastError%`)
3. Append log ด้วย **Write text to file** — ใส่ (คัดลอกตามช่องที่ใช้):

```text
%LastError.Message%
```

```text
%LastError.Location%
```

```text
%InvoiceId%
```

4. **Insert row into data table** (คัดลอก):

```text
%Results%
```

   → Status Value:

```text
Failed
```

   `ErrorMessage` จาก (คัดลอก):

```text
%LastError.Message%
```

5. **Increase variable** เลือก `FailedCount` (ไม่มี `%`)
6. ออกแบบให้ลูป **ไปต่อแถวถัดไป** (R6)

### Step 9 — SF_WriteResults: Excel + Summary + รันซ้ำได้

1. ลาก **If file exists**
   - File path: (คัดลอก)

```text
%OutputRoot%\invoice-run-results.xlsx
```

2. **ภายใน If** → **Delete file** ที่ path เดิม
3. **End**
4. **Launch Excel** (สร้างเอกสารใหม่ หรือเปิด template)
5. **Write to Excel worksheet** sheet `Results` จาก (คัดลอก):

```text
%Results%
```

6. เขียน sheet `Summary`: Created / Rejected / Skipped / Failed / HighPriority ตาม [`assets/business-rules.md`](assets/business-rules.md)
7. **Save document as** → (คัดลอก):

```text
%OutputRoot%\invoice-run-results.xlsx
```

8. **Close Excel**

### Step 10 — ปิด Contoso และรันตรวจ

1. ลาก **Close window** Contoso (ถ้าค้างใช้ **Terminate process** อย่างระวัง)
2. กด **Run** ทั้ง flow
3. เทียบ Results กับ [`assets/expected/expected-results.csv`](assets/expected/expected-results.csv)
4. ตรวจโฟลเดอร์ filed และ log:

```text
%OutputRoot%\filed\
```

```text
%LogPath%
```

5. รันซ้ำรอบสอง — path output เดิมต้องไม่พังเพราะชื่อไฟล์ซ้ำ

### Challenge (ทางเลือก)

- **Extract data from window** จาก invoice grid บางส่วน เทียบจำนวน Created
- สร้าง Outlook Draft หัวข้อ (คัดลอกโครง — แทนค่า `{CreatedCount}` ด้วยจำนวนจริง):

```text
[PAD-LAB-MOCK] Contoso Invoice Ops — {CreatedCount} created
```

  สรุปสั้น ๆ (แนวเดียวกับ Capstone)
- Attachment filing ครบทุกแถวที่มีไฟล์ใน `attachments\`

---

## จุดที่มักทำผิด

| ผิด | ถูก |
|-----|-----|
| พิมพ์ `%Name%` ในช่อง Name / Store into / **Variables produced** | ใช้ชื่อเปล่าไม่มี `%` เช่น `WorkingRoot`, `CurrentInvoice` |
| พึ่งพิกัดจอ / Recorder อย่างเดียว | Capture **UI Elements** ให้เสถียรตาม ui-map |
| Error แถวเดียวแล้วทั้ง flow ตาย | **On block error** + **Get last error** แล้ว continue (R6) |
| ลืม R1/R2 แล้วยังเปิดฟอร์ม Contoso | Reject/Skip ต้องไม่แตะ UI สร้าง Invoice |
| **Save document as** รอบสองไม่ลบไฟล์เก่า | **If file exists** → **Delete file** ก่อน |
| Hardcode path Contoso คนละเครื่อง | ใช้ `%ContosoPath%` ที่หาจากเครื่องจริง |
| ไม่มี Subflow | แยกอย่างน้อย 3 Subflows |

---

## Variables

| ชื่อตอนสร้าง (ไม่มี `%`) | ตอนอ้างอิง | Type | ความหมาย |
|--------------------------|------------|------|----------|
| `ContosoPath` | `%ContosoPath%` | Text | path ไฟล์ .exe ของแอป |
| `ContosoApp` | `%ContosoApp%` | Window/App instance | ตาม action ที่ใช้ |
| `WorkingRoot` / `OutputRoot` / `LogPath` | `%WorkingRoot%` ฯลฯ | Text | path งาน |
| `Invoices` | `%Invoices%` | Data table | input |
| `Results` | `%Results%` | Data table | output |
| `CurrentInvoice` | `%CurrentInvoice%` | Data row | แถวปัจจุบันในลูป |
| `InvoiceId` | `%InvoiceId%` | Text | รหัสแถวปัจจุบัน |
| `Priority` | `%Priority%` | Text | High/Normal |
| `RowDecision` | `%RowDecision%` | Text | Create / Reject / Skip |
| `CreatedCount` / `FailedCount` | `%CreatedCount%` ฯลฯ | Numeric | สรุป |
| `LastError` | `%LastError%` | Error | จาก **Get last error** |

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
- [ ] UI Elements ของฟอร์ม Invoice ถูก capture เอง (ไม่พึ่งค่า hardcode พิกัดจอ)
- [ ] อ่านจาก Excel/CSV เป็นลูป
- [ ] Implement กฎ R1–R6 ครบ
- [ ] มี Results + Summary ออกไฟล์
- [ ] **รันซ้ำได้:** รันครั้งที่ 2 ด้วย path output เดิม (`invoice-run-results.xlsx`) โดยไม่ error ชื่อไฟล์ซ้ำ — **If file exists** → **Delete file** หรือเปิดไฟล์เดิมแล้ว Save
- [ ] Error รายแถวแล้ว Flow ไปต่อได้
- [ ] มีอย่างน้อย 3 Subflows
- [ ] (Challenge) มี attachment filing หรือ Outlook Draft

## Troubleshooting

| อาการ | แก้ |
|-------|-----|
| หา Contoso exe ไม่เจอ | เปิดแอปมือ → Task Manager → Open file location แล้วใส่ path ใน `%ContosoPath%` |
| Selector หลุดหลังอัปเดตแอป | Recapture UI element; หลีกเลี่ยง index อย่างเดียว |
| หน้าต่างถูกบัง | **Focus window** / Set window state = Normal/Maximized |
| กรอก Amount ไม่ติด | ส่งเป็น text ที่ format ตามแอป; Tab ออกจากฟิลด์ก่อน Save |
| แอปค้างหลาย instance | **Terminate process** ก่อน **Run application** ใหม่ |
| Contoso เปิดไม่ได้ / exception | ตรวจไฟล์ Excel ใต้ `Documents\Contoso Invoicing` — Sensitivity อย่าเป็น Confidential ([Q&A](https://learn.microsoft.com/answers/questions/2244882/how-to-resolve-contoso-invoicing-app-issue)) |
| Excel locked | ปิด workbook ที่เปิดซ้อน |
| Save as รอบสองล้ม (ไฟล์ซ้ำ) | ก่อน Save as ที่ `invoice-run-results.xlsx` ใช้ **If file exists** → **Delete file** |
| UIPI / ส่ง input ไม่ได้ | รัน PAD กับ Contoso ที่สิทธิ์ elevation เดียวกัน — [UIPI issues](https://learn.microsoft.com/troubleshoot/power-platform/power-automate/desktop-flows/ui-automation/uipi-issues) |

## Cleanup

- ปิด Contoso / Excel ที่ค้าง
- ข้อมูล invoice ที่สร้างใน Contoso เป็นของ Lab — ล้างตามที่วิทยากรแนะนำก่อนรอบสาธิตถัดไป
- อย่า commit output/logs ส่วนตัว
