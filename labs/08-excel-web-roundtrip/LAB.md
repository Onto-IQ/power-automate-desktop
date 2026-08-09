# Lab 08 — Excel ↔ Web Round-trip (Hands-on)

**อ่านก่อน:** [LESSON.md](LESSON.md) · **หน้าปกบท:** [README.md](README.md) · **พื้นฐาน:** [`shared/PAD-FUNDAMENTALS.md`](../../shared/PAD-FUNDAMENTALS.md)

**วัน:** 2 · **ระดับ:** Intermediate–Advanced  
**ทักษะ:** อ่าน Excel → ป้อน Web UI → ดึงสถานะ/ข้อความจาก Web → เขียนกลับ Excel

## อ้างอิง (Aug 2026)

| แหล่ง | URL |
|-------|-----|
| Web automation | [automation-web](https://learn.microsoft.com/power-automate/desktop-flows/automation-web) |
| Web actions | [actions-reference/webautomation](https://learn.microsoft.com/power-automate/desktop-flows/actions-reference/webautomation) |
| Excel actions | [actions-reference/excel](https://learn.microsoft.com/power-automate/desktop-flows/actions-reference/excel) |

## Setup บนเครื่อง (ทำก่อนเปิด designer)

1. สร้างโฟลเดอร์ `C:\PAD-Labs\working\lab08\` และ `C:\PAD-Labs\output\lab08\`
2. คัดลอก [`assets/leads-input.xlsx`](assets/leads-input.xlsx) (หรือสร้างจาก [`assets/leads-input.csv`](assets/leads-input.csv)) ไป `C:\PAD-Labs\working\lab08\`
3. คัดลอก [`assets/roundtrip-proof.txt`](assets/roundtrip-proof.txt) ไป working (สำหรับ Challenge J)
4. Output เป้าหมาย: `C:\PAD-Labs\output\lab08\leads-output.xlsx`

> ถ้าใช้ไดรฟ์อื่น ให้คง path นั้นใน `%WorkingRoot%` / `%OutputPath%` ทั้ง flow

## Web UI

| ขั้น | Phase 1 | URL | บัญชี / เงื่อนไข |
|------|---------|-----|------------------|
| Login | 06 | https://ontoiq.tech/pad/06-login.html | `demo` / `demo` |
| Forms (มาตรฐาน) | 01 | https://ontoiq.tech/pad/01-forms.html | ทุก lead ที่ `Status=New` และ Priority ≠ High |
| Wizard (Mission W) | 07 | https://ontoiq.tech/pad/07-wizard.html | lead ที่ `Priority=High` |

### Challenge missions

| Mission | Phase 1 | URL | เมื่อไร |
|---------|---------|-----|--------|
| I — Iframe lead | 08 | https://ontoiq.tech/pad/08-iframe.html | ทำกับ lead แรกที่ `Company` มีคำว่า `Fabrikam` (หรือแถวที่วิทยากรกำหนด) |
| J — Files proof | 05 | https://ontoiq.tech/pad/05-files.html | หลัง submit สำเร็จอย่างน้อย 1 แถว: upload `assets/roundtrip-proof.txt` แล้วบันทึกผลในคอลัมน์ `WebResult` หรือ sheet `Artifacts` |

## Input / Output

| | Path |
|--|------|
| Leads CSV | [`assets/leads-input.csv`](assets/leads-input.csv) |
| Output template | [`assets/leads-output-template.csv`](assets/leads-output-template.csv) |
| Files proof mock | [`assets/roundtrip-proof.txt`](assets/roundtrip-proof.txt) |
| Schema | [`shared/DATA-SCHEMAS.md`](../../shared/DATA-SCHEMAS.md) |
| Your output | `C:\PAD-Labs\output\lab08\leads-output.xlsx` |

### Mapping Excel → Form

| Excel Column | Form field (แนวทาง) |
|--------------|---------------------|
| FullName | Name / `#txt-name` |
| Email | Email |
| Interest หรือ Message | Textarea / message |
| (วันนี้) | Date ใช้วันที่รัน Flow |

---

## Hands-on ทีละขั้น

### Step 0 — สร้าง flow

1. เปิด Power Automate for desktop → **New flow**
2. ชื่อ: `Lab08_ExcelWebRoundtrip` → **Create**

> **กฎตัวแปรใน PAD (อ่านก่อนทำ Step ถัดไป)**  
> - ช่อง **Name** ของ **Set variable**, ชื่อ **produced variable**, และ **Store into** = พิมพ์ชื่ออย่างเดียว **ไม่มี `%`** เช่น `WorkingRoot`  
> - ช่องอื่นที่ต้องดึงค่าตัวแปร (Folder, File path, Text, …) = ใช้ `%WorkingRoot%` (**มี `%` ครบสองด้าน**)  
> - หลังสร้างแล้ว Variables pane อาจแสดงเป็น `%WorkingRoot%` — เป็นเรื่องปกติ

### Step 1 — ตั้ง path

1. ลาก **Set variable** (Name ไม่มี `%`):
   - Name `WorkingRoot` = Value `C:\PAD-Labs\working\lab08`
   - Name `OutputPath` = Value `C:\PAD-Labs\output\lab08\leads-output.xlsx`

### Step 2 — อ่าน Leads จาก Excel

1. ลาก **Launch Excel**
2. ตั้งค่า: เปิด `%WorkingRoot%\leads-input.xlsx` ← **ใช้** (มี `%`)
3. ชื่อ produced: `Excel` ← **ไม่ใส่ `%`** (อ้างอิงด้วย `%Excel%`)
4. ลาก **Read from Excel worksheet**
   - Excel instance: `%Excel%` ← **ใช้** (มี `%`)
   - Worksheet: `Leads`
   - First line of range contains column names: เปิด
5. ชื่อ produced: `Leads` ← **ไม่ใส่ `%`** (อ้างอิงด้วย `%Leads%`)

> ห้าม hardcode ค่า lead ทั้งชุดลงตัวแปรทีละคน — ต้องอ่านจาก Excel แล้วใช้ลูป

### Step 3 — Login Lab Hub

1. ลาก **Launch new Microsoft Edge** (หรือ **Launch new Chrome**)
2. ตั้งค่า:
   - Initial URL: `https://ontoiq.tech/pad/06-login.html`
3. ชื่อ produced: `Browser` ← **ไม่ใส่ `%`** (อ้างอิงด้วย `%Browser%`)
4. ลาก **Wait for web page content** จนช่อง login พร้อม (เช่น `#txt-username`)
5. ลาก **Populate text field on web page**
   - UI element: `#txt-username` → Text: `demo`
6. ลาก **Populate text field on web page**
   - `#txt-password` → `demo`
7. ลาก **Press button on web page** → `#btn-login`
8. ลาก **Wait for web page content** จนสำเร็จ / dashboard พร้อมก่อนเข้าลูป

### Step 4 — For each lead ที่ Status = New

1. ลาก **For each**
   - Value to iterate: `%Leads%` ← **ใช้** (มี `%`)
   - Store into: `CurrentLead` ← **ไม่ใส่ `%`**
2. **ภายใน For each** ลาก **If**
   - เงื่อนไข: Status ของแถว Equal to `New`
3. (แนะนำ Challenge) **Else** / If ซ้อน: ถ้า Email ว่าง → ข้ามแถว
4. งาน submit ทั้งหมดอยู่ **ภายใน** กิ่ง `Status=New`

### Step 5 — Mission W: Priority=High ใช้ Wizard (07)

ยังอยู่ภายในกิ่ง New:

1. ลาก **If**
   - `%CurrentLead['Priority']%` Equal to `High`
2. **ภายใน If (High):**
   - **Go to web page** → `https://ontoiq.tech/pad/07-wizard.html`
   - **Wait for web page content**
   - ทำ Wizard ครบทุก step ด้วย **Populate text field on web page** / **Press button on web page** / **Click link on web page** ตามที่หน้ามี
   - อ่านข้อความผลลัพธ์ → **Set variable** Name: `WebResult` ← **ไม่ใส่ `%`**
3. **Else** (ไม่ High) → ไป Step 6 (Forms)
4. **End**

### Step 6 — Forms มาตรฐาน (01) สำหรับ lead ทั่วไป

ในกิ่ง Else ของ Priority:

1. **Go to web page** → `https://ontoiq.tech/pad/01-forms.html`
2. **Wait for web page content** จนฟอร์มพร้อม
3. **Populate text field on web page** ตาม mapping:
   - Name ← FullName
   - Email ← Email
   - Message/Interest ← คอลัมน์ที่เกี่ยวข้อง
   - Date ← วันที่รัน flow
4. **Press button on web page** (ปุ่ม Submit)
5. อ่าน/Extract ข้อความผลลัพธ์ → ชื่อ produced / Set variable: `WebResult` ← **ไม่ใส่ `%`**  
   (อ้างอิงด้วย `%WebResult%`; ใช้ **Extract data from web page** กับ **live web helper** หรืออ่านข้อความที่โผล่หลัง submit)

### Step 7 — อัปเดตสถานะแถวในหน่วยความจำ

หลัง submit สำเร็จ (ทั้ง Wizard และ Forms):

1. **Set variable** / อัปเดตคอลัมน์ของแถวหรือตาราง (Name ไม่มี `%`):
   - Status = `Submitted`
   - WebResult = `%WebResult%` ← **ใช้** ค่าที่เก็บไว้ (มี `%`)
   - Name `SubmittedAt` = เวลาปัจจุบัน (อ้างอิงด้วย `%SubmittedAt%`)
2. ออกแบบให้ `%Leads%` (หรือตารางผลแยก) เก็บค่าอัปเดตครบก่อนเขียน Excel ท้าย flow

### Step 8 — Challenge I / J (ทางเลือก แต่มีในเกณฑ์ Challenge)

**Mission I — Iframe**

1. ในลูป: **If** Company Contains `Fabrikam` (แถวแรกที่เข้าเงื่อนไข)
2. **Go to web page** → `https://ontoiq.tech/pad/08-iframe.html`
3. สลับเข้า iframe ที่ถูกต้องแล้ว Populate / Submit ตามหน้า
4. บันทึกผลลง WebResult หรือ Notes

**Mission J — Files proof**

1. **หลัง** submit สำเร็จอย่างน้อย 1 แถว (นอกหรือท้ายลูปก็ได้ตามออกแบบ)
2. **Go to web page** → `https://ontoiq.tech/pad/05-files.html`
3. Upload `%WorkingRoot%\roundtrip-proof.txt`
4. บันทึกผลในคอลัมน์ `WebResult` หรือ sheet `Artifacts`

### Step 9 — เขียนกลับ Excel + รันซ้ำได้ + ปิดทรัพยากร

1. ลาก **If file exists**
   - File path: `%OutputPath%`
2. **ภายใน If** → **Delete file** → `%OutputPath%`
3. **End**
4. **Write to Excel worksheet** ทั้งตารางกลับ sheet `Leads` หรือ `Results` (ใช้ `%Excel%` หรือ Launch Excel ใหม่สำหรับ output ตามที่ออกแบบ)
5. **Save document as** → `%OutputPath%`
6. **Close Excel**
7. **Close web browser** → `%Browser%`

### Step 10 — รันและตรวจ

1. กด **Run**
2. เปิด `leads-output.xlsx` — แถว New ต้องเป็น `Submitted` และ `WebResult` ไม่ว่าง
3. ตรวจว่า Priority=High ไป Wizard ไม่ใช่ Forms อย่างเดียว
4. รันซ้ำรอบสองด้วย path output เดิม — ต้องไม่พังเพราะชื่อไฟล์ซ้ำ

---

## จุดที่มักทำผิด

| ผิด | ถูก |
|-----|-----|
| พิมพ์ `%Name%` ในช่อง Name / Store into / ชื่อ produced | ใช้ชื่อเปล่าไม่มี `%` เช่น `WorkingRoot`, `CurrentLead` |
| Hardcode lead ทั้งชุดลงตัวแปร | **Read from Excel worksheet** + **For each** |
| ข้าม Login แล้วไป Forms ตรง ๆ | ทำ **06 Login** (`demo`/`demo`) ก่อน |
| High ยังไป Forms อย่างเดียว | **Mission W:** High → **07 Wizard** |
| ลืม **Close Excel** / **Close web browser** | ปิดท้าย flow ทุกครั้ง |
| Save as รอบสองโดยไม่ลบไฟล์เก่า | **If file exists** → **Delete file** ก่อน **Save document as** |
| เขียน Excel ทับแถวผิด index | เขียนทั้งตารางกลับ sheet หรือใช้ index ระมัดระวัง |

---

## Variables

| ชื่อตอนสร้าง (ไม่มี `%`) | ตอนอ้างอิง | Type |
|--------------------------|------------|------|
| `WorkingRoot` / `OutputPath` | `%WorkingRoot%` / `%OutputPath%` | Text |
| `Excel` | `%Excel%` | Excel instance |
| `Browser` | `%Browser%` | Browser |
| `Leads` | `%Leads%` | Data table |
| `CurrentLead` | `%CurrentLead%` | Data row |
| `WebResult` | `%WebResult%` | Text |
| `SubmittedAt` | `%SubmittedAt%` | DateTime/Text |

## Expected Result

- แถวที่เป็น `New` ถูกเปลี่ยนเป็น `Submitted`
- มีค่า `WebResult` ไม่ว่าง
- ไฟล์ output แยกจาก input

## Acceptance Criteria

- [ ] Login ผ่านหน้า [06 Login](https://ontoiq.tech/pad/06-login.html) ก่อนทำงานกับฟอร์ม
- [ ] อ่านจาก Excel จริง ไม่ copy ค่าลงตัวแปรทีละคนแบบ hardcode ทั้งชุด
- [ ] ใช้ลูป **For each**
- [ ] **Mission W:** lead `Priority=High` ใช้ Wizard (07) ไม่ใช่ Forms อย่างเดียว
- [ ] ปิดด้วย **Close Excel** และ **Close web browser**
- [ ] มีอย่างน้อย 1 แถวอัปเดตสำเร็จ
- [ ] **รันซ้ำได้:** รันครั้งที่ 2 ด้วย path output เดิม (`leads-output.xlsx`) โดยไม่ error ชื่อไฟล์ซ้ำ — **If file exists** → **Delete file** หรือเปิดไฟล์เดิมแล้ว Save
- [ ] (Challenge) Mission I หรือ J อย่างน้อย 1 รายการ

## Challenge

- ข้ามแถวที่ Email ว่างด้วย **If**
- Mission I — Iframe / Mission J — Files ตามตารางด้านบน

## Troubleshooting

| อาการ | แก้ |
|-------|-----|
| Login หลุด | ทำ login ใหม่ในลูปหรือตรวจ cookie/session ของหน้า Lab |
| เขียน Excel ทับแถวผิด | ใช้ index / write cell ระมัดระวัง หรือเขียน sheet ใหม่ทั้งก้อน |
| Save as รอบสองล้ม (ไฟล์ซ้ำ) | **If file exists** → **Delete file** ก่อน Save as |
| ฟอร์ม validation | ตรวจรูปแบบ email/date |
| Element ไม่เจอ | เพิ่ม **Wait for web page content** ก่อน Interact |

## Cleanup

- ลบ working copies; คง CSV/XLSX ต้นฉบับใน assets
