# Lab 07 — Contoso Invoice Ops (Hands-on)

**อ่านก่อน:** [LESSON.md](LESSON.md) · **หน้าปกบท:** [README.md](README.md) · **พื้นฐาน:** [`shared/PAD-FUNDAMENTALS.md`](../../shared/PAD-FUNDAMENTALS.md)

**วัน:** 2 · **ระดับ:** Advanced · **เวลาเป้าหมาย (catch-up):** ~1 ชม.  
**ทักษะ:** Run application / Wait for window / Close, UI Elements (Contoso), Excel → Contoso → Excel, R1–R6, On block error (SET-only) + Get last error, Subflows

**สคริปต์อ้างอิง (แหล่งความจริงของ Lab นี้):** [`scripts/07-contoso-invoice-ops.robin`](scripts/07-contoso-invoice-ops.robin)

## อ้างอิง (Aug 2026)

| แหล่ง | URL |
|-------|-----|
| Contoso setup (Learn) | [Set up Contoso Invoicing](https://learn.microsoft.com/training/modules/input-parameters/2-set-up) |
| Contoso sample app | [contoso-invoice-app (GitHub)](https://github.com/MicrosoftDocs/mslearn-developer-tools-power-platform/tree/master/power-automate-desktop/contoso-invoice-app) |
| UI automation | [actions-reference/uiautomation](https://learn.microsoft.com/power-automate/desktop-flows/actions-reference/uiautomation) |
| Handle errors | [desktop-flows/errors](https://learn.microsoft.com/power-automate/desktop-flows/errors) |

## Setup — Contoso + โฟลเดอร์ทำงาน

1. ติดตั้ง Contoso จาก [ContosoInvoicingSetup.zip](https://github.com/MicrosoftDocs/mslearn-developer-tools-power-platform/raw/master/power-automate-desktop/contoso-invoice-app/ContosoInvoicingSetup.zip) → เปิดจาก Start: `Contoso Invoicing`
2. สร้างโฟลเดอร์:

```text
C:\PAD-Labs\working\lab07\
C:\PAD-Labs\output\lab07\
C:\PAD-Labs\output\lab07\filed\
C:\PAD-Labs\logs\lab07\
```

3. คัดลอกทั้งโฟลเดอร์ [`assets/`](assets/) ไปที่ `C:\PAD-Labs\working\lab07\`
4. จด path `.exe` จริง (Task Manager → Open file location) ใส่ในตัวแปร `ContosoPath`  
   ตัวอย่างในสคริปต์ (แก้ตามเครื่อง):

```text
D:\Program Files\Contoso, Inc\Contoso Invoicing\LegacyInvoicingApp.exe
```

## Input / Output (ตรงกับสคริปต์)

| | Path |
|--|------|
| Batch | `%WorkingRoot%\invoices-batch.xlsx` ← จาก [`assets/invoices-batch.xlsx`](assets/invoices-batch.xlsx) |
| Attachments | `%WorkingRoot%\attachments\{InvoiceId}*` |
| Results | `%ResultsPath%` = `C:\PAD-Labs\output\lab07\invoice-run-results.xlsx` |
| Log | `%LogPath%` = `C:\PAD-Labs\logs\lab07\contoso-run-log.csv` |
| Filed | `%OutputRoot%\filed\{InvoiceId}\` |
| Expected | [`assets/expected/expected-results.csv`](assets/expected/expected-results.csv) |
| UI map | [`assets/ui-map.md`](assets/ui-map.md) |
| Rules | [`assets/business-rules.md`](assets/business-rules.md) |

## Business Rules (R1–R6) — ตามสคริปต์

| Rule | ใน flow | ผล |
|------|---------|-----|
| R1 | Account ว่างหลัง Trim **หรือ** Amount ไม่ใช่ตัวเลข / `<= 0` | `RowDecision=Reject`, `Status=Rejected` — **ไม่แตะ Contoso UI** |
| R2 | `ProcessFlag=Skip` | `RowDecision=Skip`, `Status=Skipped` — **ไม่แตะ Contoso UI** |
| R3 | `AmountNumber >= 10000` | `Priority=High`, `Status=Created-HighPriority`, Notes มี `HIGH PRIORITY` |
| R4 | สร้างปกติ | `Priority=Normal`, `Status=Created` |
| R3/R4 Status ในแอป | ใช้ `%StatusToSet%` จากแถว (batch มี `Paid` / `Open`) | **Set drop-down** `Cmb_Status` |
| R5 | หลัง Create สำเร็จ | `Get files` filter `%InvoiceId%*` → copy ไป `filed\{InvoiceId}\` → `AttachmentFiled=Yes/No` |
| R6 | UI/แถวพัง | `ON BLOCK ERROR` → **SET เท่านั้น** (`RowFailed`, `Status=Failed`) แล้ว Increase/File/AddRow **นอก** handler |

## โครง SF_* ในสคริปต์ (Main หรือแยก Subflow)

| บล็อก | สิ่งที่ทำใน `.robin` |
|-------|---------------------|
| `SF_InitPaths` | path, `filed`, log header, อ่าน Excel → `Invoices`, สร้าง `Results` |
| `SF_LaunchContoso` | `Get path part` → WorkingDirectory, **Run application**, **Wait for window** (title) |
| `SF_ValidateInvoiceRow` | R1–R2 → `RowDecision` |
| `SF_CreateContosoInvoice` | R3/R4 + วันที่ MM/DD/YYYY + Click/Populate/Save |
| `SF_FileAttachment` | R5 |
| `SF_WriteResults` | ลบไฟล์ผลถ้ามี → เขียน Results ที่ A1 + Summary ที่ H:I → Close Contoso |

เกณฑ์ผ่าน: แยกอย่างน้อย **3 Subflows** จากชื่อด้านบน **หรือ** วาง catch-up แล้วมีคอมเมนต์ `# SF_*` ครบตามสคริปต์

---

## เส้นทาง A — Catch-up (~1 ชม., แนะนำถ้าตามไม่ทัน)

1. PAD → **New flow** ชื่อ:

```text
Lab07_ContosoInvoiceOps
```

2. เปิด [`scripts/07-contoso-invoice-ops.robin`](scripts/07-contoso-invoice-ops.robin) → คัดลอกทั้งไฟล์ → วางใน canvas ของ flow **ว่าง**
3. แก้ `ContosoPath` ให้ชี้ `.exe` บนเครื่องคุณ
4. เปิดแท็บ **UI elements** — ควรเห็น screen `Contoso Invoicing` และ:

```text
Btn_Invoices, Btn_NewInvoice, Txt_Date, Txt_Account, Txt_Contact, Txt_Amount, Cmb_Status, Btn_Save
```

   (ฝังใน `ControlRepository` ท้าย `.robin` — ถ้าไม่มี/แดง ให้ Recapture แล้ว Rename ตาม [`assets/ui-map.md`](assets/ui-map.md))
5. ตรวจว่ามี `C:\PAD-Labs\working\lab07\invoices-batch.xlsx` และโฟลเดอร์ attachments
6. **Run** → เทียบผลกับ expected + `filed\` + log (ดูท้าย LAB)

> **กฎ `%`:** Name / Store into / Variables produced = **ไม่มี `%`** · อ้างอิงค่า = `%Name%`

---

## เส้นทาง B — สร้างมือให้ตรงสคริปต์

### Step 0 — Flow + UI Elements

1. New flow `Lab07_ContosoInvoiceOps`
2. Capture / ตรวจ UI ตาม ui-map (ชื่อต้องตรงตารางด้านบน)
3. (ทางเลือก) แยก Subflow ตามตาราง SF_*

### Step 1 — SF_InitPaths

1. **Set variable** (Name ไม่มี `%`):

| Name | Value |
|------|--------|
| `WorkingRoot` | `C:\PAD-Labs\working\lab07` |
| `OutputRoot` | `C:\PAD-Labs\output\lab07` |
| `LogPath` | `C:\PAD-Labs\logs\lab07\contoso-run-log.csv` |
| `ContosoPath` | path `.exe` จริง |
| `ResultsPath` | `C:\PAD-Labs\output\lab07\invoice-run-results.xlsx` |
| `CreatedCount` / `FailedCount` / `RejectedCount` / `SkippedCount` / `HighPriorityCount` | `0` |
| `RowFailed` | `False` |

2. **Get path part** จาก `%ContosoPath%` → Directory = `ContosoWorkingDir`
3. **If folder exists** path `%OutputRoot%\filed` → ไม่มีแล้ว **Create folder**
4. **Write text to file** `%LogPath%` — Overwrite — ข้อความ:

```text
InvoiceId,Status,Priority,AttachmentFiled,ErrorMessage
```

5. **Launch Excel** `%WorkingRoot%\invoices-batch.xlsx` (Visible off, Read-only) → `ExcelIn`
6. **Read from Excel** First line = column names → `Invoices`
7. **Close Excel** `ExcelIn`
8. **Create new data table** → `Results` คอลัมน์:

```text
InvoiceId, Status, Priority, AttachmentFiled, ErrorMessage, Notes
```

### Step 2 — SF_LaunchContoso

1. **Run application**  
   - Application path: `%ContosoPath%`  
   - Working directory: `%ContosoWorkingDir%`
2. **Wait for window** — หาด้วย **Window title/class**  
   - Title: `Contoso Invoicing`  
   - Wait for: **Open** · Focus window: เปิด  
   - Timeout ตัวอย่าง: 30 วินาที  

   (ตรงกับสคริปต์: `WAIT (UIAutomation.WaitForWindow.ToOpenByTitleClass …) FOR 30` — **ไม่ใช่** Wait for window content)

### Step 3 — For each + On block error (R6)

1. **For each** `%Invoices%` → Store into `CurrentInvoice`
2. ตั้งจากแถว (Name ไม่มี `%`):

| Name | Value |
|------|--------|
| `InvoiceId` | `%CurrentInvoice['InvoiceId']%` |
| `Account` | `%CurrentInvoice['Account']%` |
| `AmountText` | `%CurrentInvoice['Amount']%` |
| `ProcessFlag` | `%CurrentInvoice['ProcessFlag']%` |
| `Contact` | `%CurrentInvoice['Contact']%` |
| `InvoiceDate` | `%CurrentInvoice['InvoiceDate']%` |
| `StatusToSet` | `%CurrentInvoice['StatusToSet']%` |

3. Reset รายแถว: `AttachmentFiled=No`, `ErrorMessage` / `Notes` / `Priority` / `Status` / `RowDecision` ว่าง, `DateForContoso=%InvoiceDate%`, `RowFailed=False`
4. **On block error** ครอบงานแถว (นโยบาย Continue ตาม R6)  
   - ในกิ่ง error: **Set variable เท่านั้น**  
     - `RowFailed` = `True`  
     - `Status` = `Failed`  
   - **ห้าม** Increase / Write text / Insert row / **Get last error** **ใน** handler (PAD มัก reject)

### Step 4 — SF_ValidateInvoiceRow (R1–R2)

1. **Trim text** `%Account%` → `AccountTrimmed`
2. ว่าง → `RowDecision=Reject`, `Status=Rejected`, Notes เช่น `R1 Account ว่าง`
3. ไม่ว่าง → **Convert text to number** `%AmountText%` → `AmountNumber`  
   - On error ของ action → Reject + Notes `R1 Amount ไม่ใช่ตัวเลข`
4. ถ้ายังไม่ Reject และ `AmountNumber <= 0` → Reject
5. Else if `ProcessFlag` = `Skip` → `RowDecision=Skip`, `Status=Skipped`
6. Else → `RowDecision=Create`

### Step 5 — บันทึก Reject / Skip (ไม่เปิด Contoso)

ถ้า `RowDecision` เป็น `Reject` **หรือ** `Skip`:

1. Increase `RejectedCount` หรือ `SkippedCount`
2. **Insert row** เข้า `%Results%`: InvoiceId, Status, Priority, AttachmentFiled, ErrorMessage, Notes
3. **Write text** append หนึ่งบรรทัด log:

```text
%InvoiceId%,%Status%,%Priority%,%AttachmentFiled%,%ErrorMessage%
```

### Step 6 — R3/R4 + SF_CreateContosoInvoice

เมื่อ `RowDecision` = `Create`:

1. ถ้า `AmountNumber >= 10000` → High / `Created-HighPriority` / Notes `HIGH PRIORITY` / Increase `HighPriorityCount`  
   Else → Normal / `Created`
2. แปลงวันที่: **Split text** `%InvoiceDate%` delimiter `-` → ถ้าได้ 3 ส่วน ตั้ง  
   `DateForContoso` = `%DateParts[1]%/%DateParts[2]%/%DateParts[0]%` (MM/DD/YYYY)
3. UI (ชื่อ element ต้องตรง):

| ลำดับ | Action | Element |
|-------|--------|---------|
| 1 | Click UI element | `Btn_Invoices` |
| 2 | Wait 1 วินาที | — |
| 3 | Click UI element | `Btn_NewInvoice` |
| 4 | Wait 1 วินาที | — |
| 5 | Populate text field | `Txt_Date` ← `%DateForContoso%` |
| 6 | Populate | `Txt_Account` ← `%AccountTrimmed%` |
| 7 | Populate | `Txt_Contact` ← `%Contact%` |
| 8 | Populate | `Txt_Amount` ← `%AmountText%` |
| 9 | Set drop-down list value (by name) | `Cmb_Status` ← `%StatusToSet%` |
| 10 | Click | `Btn_Save` |
| 11 | Wait 1 วินาที | — |
| 12 | Increase | `CreatedCount` |

### Step 7 — SF_FileAttachment (R5)

1. **Get files** folder `%WorkingRoot%\attachments` filter `%InvoiceId%*`
2. ถ้ามีไฟล์ → สร้าง `%OutputRoot%\filed\%InvoiceId%` ถ้ายังไม่มี → **Copy** → `AttachmentFiled=Yes`  
   Else → `No`
3. Insert row + append log (เช่นเดียวกับ Create สำเร็จ)

### Step 8 — บันทึก Failed นอก handler (Get last error → log)

หลังจบ **On block error** ของแถว (ยังใน For each):

1. If `%RowFailed%` = True:
   - **Get last error** → `LastError` (เปิด **Clear error**)
   - **Set variable** `ErrorMessage` ← `%LastError.Message%`
   - Increase `FailedCount`
   - **Insert row** เข้า `%Results%` (Status = Failed)
   - **Write text** append log:

```text
%InvoiceId%,Failed,%Priority%,%AttachmentFiled%,%ErrorMessage%
```

> อย่าใส่ข้อความตายตัวเช่น `Row processing error` ใน handler — ใช้ `%LastError.Message%` นอกบล็อกเพื่อให้ log มีสาเหตุจริง (Lab 09/09b จะทบทวนแพทเทิร์นนี้ต่อ)

### Step 9 — SF_WriteResults + ปิด Contoso

1. **If file exists** `%ResultsPath%` → **Delete file**
2. **Launch Excel** (เอกสารใหม่) → `ExcelOut`
3. **Write to Excel**  
   - เซลล์ A1 ← `%Results%` (data table)  
   - Summary คอลัมน์ H/I ตามสคริปต์:

| H | I |
|---|---|
| Created | `%CreatedCount%` |
| Rejected | `%RejectedCount%` |
| Skipped | `%SkippedCount%` |
| Failed | `%FailedCount%` |
| HighPriority | `%HighPriorityCount%` |

4. **Close Excel** + **Save as** → `%ResultsPath%`
5. **Close window** โดย title: `Contoso Invoicing`

### Step 10 — ตรวจผล

1. เทียบกับ [`assets/expected/expected-results.csv`](assets/expected/expected-results.csv)
2. ตรวจ `%OutputRoot%\filed\` (INV-7001, 7002, 7007 ควรมีไฟล์) และ `%LogPath%`
3. รันซ้ำรอบสอง — ต้องไม่พังเพราะไฟล์ผลซ้ำ

### Challenge (ทางเลือก)

- Extract จาก `Grid_InvoiceList` เทียบจำนวน Created
- Outlook Draft: `[PAD-LAB-MOCK] Contoso Invoice Ops — {CreatedCount} created`

---

## จุดที่มักทำผิด (ตรงกับสคริปต์)

| ผิด | ถูก |
|-----|-----|
| `%Name%` ในช่อง Name / Store into | ชื่อเปล่า เช่น `WorkingRoot` |
| Wait for window content / invent `WaitForWindowToOpen` | **Wait for window** title `Contoso Invoicing` + Focus |
| Increase/File/**Get last error** ใน On block error | ใน handler = **SET** อย่างเดียว (`RowFailed`, `Status`); **Get last error** + log **นอก**หลัง flag |
| ใส่ `ErrorMessage` ตายตัวใน handler | นอกบล็อก: `ErrorMessage` ← `%LastError.Message%` |
| Reject/Skip แล้วยัง Click New Invoice | เฉพาะ `RowDecision=Create` เท่านั้นที่แตะ UI |
| Save as รอบสองไม่ลบไฟล์เก่า | If file exists → Delete ที่ `%ResultsPath%` |
| ชื่อ UI ไม่ตรงสคริปต์ | Rename ตาม ui-map / ตารางใน Step 6 |
| ลืม Working directory ของ Contoso | **Get path part** → ใส่ใน Run application |

## Variables (หลักในสคริปต์)

| สร้าง (ไม่มี `%`) | อ้างอิง | ความหมาย |
|-------------------|--------|----------|
| `WorkingRoot` / `OutputRoot` / `LogPath` / `ResultsPath` / `ContosoPath` | `%…%` | path |
| `ContosoWorkingDir` | `%ContosoWorkingDir%` | โฟลเดอร์ exe |
| `Invoices` / `Results` / `CurrentInvoice` | `%…%` | batch / ผล / แถว |
| `InvoiceId`, `Account`, `AmountText`, `ProcessFlag`, `Contact`, `InvoiceDate`, `StatusToSet` | `%…%` | คอลัมน์แถว |
| `AccountTrimmed`, `AmountNumber`, `DateForContoso`, `DateParts` | `%…%` | validate / วันที่ |
| `RowDecision`, `Status`, `Priority`, `Notes`, `AttachmentFiled`, `ErrorMessage`, `RowFailed` | `%…%` | ตัดสินใจแถว |
| `LastError` | `%LastError%` / `%LastError.Message%` | จาก **Get last error** เมื่อ `RowFailed` |
| `CreatedCount`, `RejectedCount`, `SkippedCount`, `FailedCount`, `HighPriorityCount` | `%…%` | Summary |

## Acceptance Criteria

- [ ] Launch Contoso จาก Flow ได้ (`ContosoPath` + Working directory ถูก)
- [ ] UI Elements ชื่อตรงสคริปต์ (จาก catch-up repo หรือ capture เอง)
- [ ] อ่าน Excel เป็นลูป + R1–R6 ครบตามตารางด้านบน
- [ ] Results ที่ A1 + Summary ที่ H:I ใน `invoice-run-results.xlsx`
- [ ] รันซ้ำได้ (Delete ไฟล์ผลก่อน Save as)
- [ ] Error รายแถวแล้วไปต่อได้ (SET-only ใน On block error + **Get last error** นอก handler → `%LastError.Message%` ใน log)
- [ ] มีอย่างน้อย 3 ชื่อ `SF_*` (Subflow หรือคอมเมนต์ตาม catch-up)
- [ ] (Challenge) Extract grid หรือ Outlook Draft

## Troubleshooting

| อาการ | แก้ |
|-------|-----|
| UI element wasn't found หลังวาง Robin | ตรวจแท็บ UI elements / Recapture + Rename ตาม ui-map |
| หา Contoso exe ไม่เจอ | Task Manager → Open file location → แก้ `ContosoPath` |
| Selector หลุด | Recapture; อย่าพึ่งพิกัดจออย่างเดียว |
| กรอก Amount / Date ไม่ติด | ส่งข้อความ; วันที่เป็น MM/DD/YYYY ตามสคริปต์ |
| On block error แดงตอนใส่ Increase/File/Get last error | ย้ายออกนอก handler: flag ใน handler → **Get last error** + log หลัง `RowFailed` |
| Save as รอบสองล้ม | If file exists → Delete `%ResultsPath%` |
| UIPI | รัน PAD กับ Contoso elevation เดียวกัน |

## Cleanup

- ปิด Contoso / Excel ที่ค้าง
- ล้าง invoice ใน Contoso ตามที่วิทยากรแนะนำก่อนสาธิตรอบถัดไป
- อย่า commit output/logs ส่วนตัว

> **Catch-up:** วาง [`scripts/07-contoso-invoice-ops.robin`](scripts/07-contoso-invoice-ops.robin) ใน flow ว่าง — ลำดับ action / UI / R1–R6 ใน LAB นี้ต้องตรงไฟล์นั้น
