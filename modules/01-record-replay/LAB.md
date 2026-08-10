# Lab 01 — Record & Replay (Hands-on)

**อ่านก่อน:** [LESSON.md](LESSON.md) · **หน้าปกบท:** [README.md](README.md) · **พื้นฐาน:** [`shared/PAD-FUNDAMENTALS.md`](../../shared/PAD-FUNDAMENTALS.md)

**วัน:** 1 · **ระดับ:** Beginner  
**ทักษะ:** Desktop/Web Recorder, การกรอกฟอร์ม, Submit และ Variables พื้นฐาน

## อ้างอิง (Aug 2026)

| แหล่ง | URL |
|-------|-----|
| Web automation | [automation-web](https://learn.microsoft.com/power-automate/desktop-flows/automation-web) |
| Web actions | [actions-reference/webautomation](https://learn.microsoft.com/power-automate/desktop-flows/actions-reference/webautomation) |
| Actions pane / On error | [actions-pane](https://learn.microsoft.com/power-automate/desktop-flows/actions-pane) |
| Community: Autofill ขัด PAD | [Power Platform Community thread](https://community.powerplatform.com/forums/thread/details/?threadid=5b9067f5-2fec-4e44-b05e-9549f05ea7bd) |

## Setup บนเครื่อง (ทำก่อนเปิด designer)

1. สร้างโฟลเดอร์ working และ output (คัดลอก path):

```text
C:\PAD-Labs\working\lab01\
```

```text
C:\PAD-Labs\output\lab01\
```

2. คัดลอก [`assets/sample-form-input.csv`](assets/sample-form-input.csv) ไปโฟลเดอร์ working
3. เปิด URL นี้ใน **Chrome** ด้วยมือหนึ่งครั้ง เพื่อยืนยันว่าโหลดได้:

```text
https://ontoiq.tech/pad/01-forms.html
```

4. ตรวจว่าติดตั้ง **Power Automate** Chrome extension แล้ว (MSI PAD แนะนำ)

## Input / Output

| | Path / ค่า |
|--|------------|
| Input mock | [`assets/sample-form-input.csv`](assets/sample-form-input.csv) |
| Web UI | `https://ontoiq.tech/pad/01-forms.html` |
| Browser | **Chrome** (หลัก) · Edge เป็นทางเลือก |
| UI screen (PAD) | `Lab01 Forms` |
| UI elements | `Txt_Name`, `Txt_Email`, `Txt_Amount`, `Txt_Date`, `Txt_Note`, `Btn_Submit` |
| Screenshot proof | `C:\PAD-Labs\output\lab01\submit-proof.png` |
| Expected | กรอกครบ 5 ช่องจากตัวแปร → Submit → มี screenshot หลักฐาน → Close browser |

### ข้อมูลตัวอย่าง (แถวแรก — ใช้ใน Hands-on / ตรงกับ catch-up)

คัดลอกทีละค่าไปวางในช่อง **Value** ของ **Set variable** — ต้องใช้ครบ **5 ค่า** ให้ตรงทุกช่องบนฟอร์ม:

**Name / FullName** → ช่อง `#txt-name`

```text
Somchai Demo
```

**Email** → ช่อง `#txt-email`

```text
somchai.demo@example.com
```

**Amount** → ช่อง `#txt-amount`

```text
3000
```

**Date / FormDate** → ช่อง `#txt-date`

```text
2026-08-08
```

**Message** → ช่อง `#txt-note`

```text
Hello from Lab 01 Record & Replay
```

---

## Hands-on ทีละขั้น

### Step 0 — สร้าง flow

1. เปิด Power Automate for desktop → **New flow**
2. ชื่อ flow (คัดลอกได้):

```text
Lab01_RecordReplay
```

3. กด **Create**

> **กฎตัวแปรใน PAD (อ่านก่อนทำ Step ถัดไป)**  
> - ช่อง **Name** ของ **Set variable**, ส่วน **Variables produced**, และ **Store into** = พิมพ์ชื่ออย่างเดียว **ไม่มี `%`** เช่น `WorkingRoot`  
> - ช่องอื่นที่ต้องดึงค่าตัวแปร (Folder, File path, Text, …) = ใช้ `%WorkingRoot%` (**มี `%` ครบสองด้าน**)  
> - หลังสร้างแล้ว Variables pane อาจแสดงเป็น `%WorkingRoot%` — เป็นเรื่องปกติ

### Step 1 — ตั้งค่าตัวแปรจากแถวแรก

1. ใน Actions Pane ค้นหา **Set variable** แล้วลากลง workspace
2. ตั้งค่า:
   - Name: `FullName` ← **ไม่ใส่ `%`**
   - Value: (คัดลอกด้านล่างวางในช่อง Value)

```text
Somchai Demo
```

3. เพิ่ม **Set variable** อีก 4 ตัว (Name ไม่มี `%`; วางต่อท้าย Step 1) ให้ครบทุกช่องฟอร์ม:

   - Name: `Email` ← Value:

```text
somchai.demo@example.com
```

   - Name: `Amount` ← Value:

```text
3000
```

   - Name: `FormDate` ← Value:

```text
2026-08-08
```

   - Name: `Message` ← Value:

```text
Hello from Lab 01 Record & Replay
```

> Tip: แถวที่สองใน CSV (`Nicha Example` …) เก็บไว้ทำ Challenge ได้ — ไม่บังคับในเกณฑ์ผ่าน
> ต้องมีตัวแปรครบ 5 ตัว: `FullName`, `Email`, `Amount`, `FormDate`, `Message`
### Step 2 — เปิด Chrome ไปหน้า Forms

1. ใน Actions Pane ค้นหา **Launch new Chrome** (หรือ **Launch new Microsoft Edge** ถ้าไม่มี Chrome) แล้วลากลง workspace **หลัง** ชุด Set variable
2. ตั้งค่า:
   - Initial URL: (คัดลอกด้านล่าง)

```text
https://ontoiq.tech/pad/01-forms.html
```

   - Window state: Normal
   - Timeout for webpage to load: `60` (ถ้ามีใน designer)
3. **Variables produced:** `Browser` ← **ไม่ใส่ `%`**  
   (เวลาอ้างอิงทีหลังใช้ `%Browser%`)
4. กด Save ในหน้าต่าง action

> Catch-up script ใช้ Chrome — ให้ชั้นเรียนใช้ Chrome เป็นหลักเพื่อให้ผลเหมือนกัน

### Step 3 — รอให้ช่องฟอร์มพร้อม

1. ลาก **Wait for web page content** วางหลัง Launch
2. ตั้งค่า:
   - Browser instance: `%Browser%`
   - Wait for web page to: **Contain element**
   - UI element: ช่องชื่อ — selector ที่แนะนำ (คัดลอกได้):

```text
#txt-name
```

     หรือ `[data-pad="txt-name"]`
   - ตั้งชื่อ UI element ใน PAD ว่า `Txt_Name` และจัดอยู่ใต้ screen **`Lab01 Forms`** (ชื่อต้องตรงนี้ — ตรงกับ catch-up)
3. กด Save

> อย่ารอด้วย Wait วินาทีอย่างเดียวเป็นเกณฑ์หลัก — ใช้ Wait for web page content ตาม [Web automation](https://learn.microsoft.com/power-automate/desktop-flows/automation-web)  
> ใน Robin รูปแบบที่ถูกต้องคือ `WAIT (…WebPageToContainElement…) FOR 60` — **ไม่มี** argument ชื่อ `Timeout` บน action นี้

### Step 4 — Record หนึ่งรอบด้วยมือ (เส้นทางหลักของบทนี้)

เป้าหมายบทนี้คือโชว์ **Web Recorder** — ให้ Record แล้วได้ชุด Populate / Press button ครบ แล้วค่อยแทนค่าเป็นตัวแปรใน Step 5

1. ใน designer กด **Record** (Web recorder)
2. กรอกฟอร์มด้วยมือหนึ่งรอบให้ครบทุกช่องด้วยค่าจาก code block ด้านบน (ชื่อ อีเมล จำนวนเงิน วันที่ หมายเหตุ) แล้วกด Submit
3. หยุด Record
4. กลับมาที่ workspace — จะมีชุด action / UI Elements จาก Recorder

> **ก่อน Record / Replay — ปิด Browser Autofill**  
> อาการคลาสสิก: กรอกได้แค่ช่อง Name แล้วช่องถัดไปไม่เข้า / มีกล่อง suggestion ทับฟอร์ม  
> สาเหตุที่พบบ่อยคือ Autofill ของ Chrome/Edge หรือ **Microsoft Autofill** extension ไม่ใช่ Recorder จับ Label ผิด  
> วิธีที่ community ยืนยัน: ปิด Autofill extension ตอนรัน automation แล้วค่อยเปิดกลับหลังจบ Lab — [Power Platform Community](https://community.powerplatform.com/forums/thread/details/?threadid=5b9067f5-2fec-4e44-b05e-9549f05ea7bd)

**Checklist เร็ว (ทำครั้งเดียวต่อเบราว์เซอร์ที่ใช้กับ PAD):**

1. ปิด extension **Microsoft Autofill** (ถ้ามี) ชั่วคราวระหว่าง Lab
2. Chrome (หรือ Edge) → Settings → Autofill / Passwords → ปิด **Save passwords** และ **Autofill forms / addresses** ในโปรไฟล์ที่ใช้เรียน
3. ตอน Record: ถ้ามี suggestion โผล่ ให้กด **Esc** ให้ปิดก่อนไปช่องถัดไป

จากนั้นทำ Step 5–7 เพื่อแทนที่ค่า hardcode ด้วยตัวแปร และตรวจว่า Replay กรอกครบทุกช่อง

ถ้า Recorder ใช้ไม่ได้ชั่วคราว ให้ข้ามไป Step 5 แล้ว capture UI Elements ด้วย picker เอง (fallback)

### Step 5 — กรอกฟอร์มด้วยตัวแปร (ครบทุกช่อง)

วาง **หลัง** Wait (หรือแทนที่ action จาก Recorder ที่กรอกข้อความตายตัว):

ต้องมี **Populate text field on web page** ครบ 5 ช่อง ตามลำดับบนหน้า:

| ลำดับ | ช่องบนหน้า | Selector | UI element (ชื่อใน PAD) | Text to fill-in |
|-------|------------|----------|-------------------------|-----------------|
| 1 | ชื่อ | `#txt-name` | `Txt_Name` | `%FullName%` |
| 2 | อีเมล | `#txt-email` | `Txt_Email` | `%Email%` |
| 3 | จำนวนเงิน | `#txt-amount` | `Txt_Amount` | `%Amount%` |
| 4 | วันที่ต้องการ | `#txt-date` | `Txt_Date` | `%FormDate%` |
| 5 | หมายเหตุ | `#txt-note` | `Txt_Note` | `%Message%` |

1. ลาก **Populate text field on web page**
2. ตั้งค่าแถวแรก:
   - Browser instance: `%Browser%`
   - UI element: ช่อง Name (`#txt-name`) — ชื่อ `Txt_Name` ใต้ screen `Lab01 Forms`
   - Text to fill-in: (คัดลอก)

```text
%FullName%
```

   - **Emulate typing:** ปิด (Off) — ใส่ค่าทีเดียว ลด Autofill suggestion (ตรงกับ catch-up)
   - **Unfocus after populate:** เปิด (On) ถ้ามีใน designer
3. ทำซ้ำให้ครบอีก 4 ช่อง:

   - Email → Text:

```text
%Email%
```

     (element `Txt_Email` / `#txt-email`)

   - Amount → Text:

```text
%Amount%
```

     (element `Txt_Amount` / `#txt-amount`)

   - Date → Text:

```text
%FormDate%
```

     (element `Txt_Date` / `#txt-date`)

   - Message (หมายเหตุ) → Text:

```text
%Message%
```

     (element `Txt_Note` / `#txt-note`)

4. แต่ละ action กด Save

> อย่าข้าม Amount — หน้าฟอร์มมี 5 ช่อง; กรอกไม่ครบถือว่ายังไม่ผ่าน Lab นี้  
> ชื่อ element ต้องตรงตารางด้านบน — catch-up อ้าง `appmask['Lab01 Forms']['Txt_…']`

### Step 6 — Submit ฟอร์ม

1. ลาก **Press button on web page** (หรือ **Click link on web page** / Click บน element ปุ่ม)
2. ตั้งค่า:
   - Browser instance: `%Browser%`
   - UI element: ปุ่ม submit — selector ที่แนะนำ:

```text
[data-pad="btn-submit-form"]
```

     หรือ `#btn-submit-form` — ตั้งชื่อใน PAD ว่า `Btn_Submit` ใต้ screen `Lab01 Forms`
3. กด Save

### Step 7 — เก็บหลักฐาน (Screenshot — ตรงกับ catch-up)

1. ตรวจว่ามีโฟลเดอร์ (คัดลอก):

```text
C:\PAD-Labs\output\lab01\
```

2. ลาก **Take screenshot of web page**
3. ตั้งค่า:
   - Browser instance: `%Browser%`
   - Save mode: **File** (ไม่ใช่ Clipboard)
   - Image file:

```text
C:\PAD-Labs\output\lab01\submit-proof.png
```

   - File format: **PNG**
4. กด Save

> Catch-up บังคับ screenshot path นี้ — ถือเป็นเกณฑ์ผ่านหลัก  
> (ทางเลือก) Extract ข้อความยืนยันจาก `#form-status` / `[data-pad="form-status"]` → `SubmitResult` ได้ถ้าทำทัน แต่ไม่บังคับ

### Step 8 — ปิดเบราว์เซอร์

1. ลาก **Close web browser** วางท้าย flow
2. Browser instance: `%Browser%`
3. กด Save

### Step 9 — ตรวจ UI Elements แล้ว Replay

1. เปิด **UI Elements** pane
2. ตรวจว่ามี screen **`Lab01 Forms`** และ element ครบ: `Txt_Name`, `Txt_Email`, `Txt_Amount`, `Txt_Date`, `Txt_Note`, `Btn_Submit`
3. ตรวจว่า selector อิง `id` / `data-pad` เป็นหลัก — ดู [`shared/SELECTOR-CONVENTIONS.md`](../../shared/SELECTOR-CONVENTIONS.md)
4. กด **Run** ครั้งที่ 1 → ฟอร์มกรอกจากตัวแปร → มีไฟล์ `submit-proof.png`
5. กด **Run** ครั้งที่ 2 ติดกัน — ต้องผ่านเหมือนกัน

### Challenge (ทางเลือก)

อ่านแถวที่สองจาก `sample-form-input.csv` แล้วกรอก/submit อีกครั้ง (For each หรือ Set variable ชุดที่สอง) — ไม่บังคับในเกณฑ์ผ่าน

---

## จุดที่มักทำผิด

| ผิด | ถูก |
|-----|-----|
| พิมพ์ `%Name%` ในช่อง Name / **Variables produced** | ใช้ชื่อเปล่าไม่มี `%` เช่น `FullName`, `Browser` |
| Hardcode ข้อความใน Populate หลัง Record | เปลี่ยนเป็น `%FullName%`, `%Email%`, `%Amount%`, `%FormDate%`, `%Message%` |
| กรอกไม่ครบทุกช่องบนหน้า | มี Populate ครบ 5 ช่อง รวม `#txt-amount` |
| เปิด Emulate typing แล้ว Autofill แทรก | ปิด **Emulate typing** (ตรง catch-up) |
| เปิด Autofill / Microsoft Autofill แล้ว Replay กรอกไม่ครบ | ปิด Autofill ตาม Step 4 แล้วรันใหม่ |
| Submit ทันทีโดยไม่มี Wait | มี **Wait for web page content** ก่อน Interact / หลังโหลดหน้า |
| ตั้งชื่อ screen/element คนละชื่อกับ catch-up | ใช้ screen `Lab01 Forms` + `Txt_*` / `Btn_Submit` |
| Screenshot ไป Clipboard หรือ path อื่น | Save เป็น File → `C:\PAD-Labs\output\lab01\submit-proof.png` (PNG) |
| Selector อิงข้อความบนจอที่เปลี่ยนบ่อย | ใช้ `id` / `data-pad` ตาม Selector Conventions |
| ไม่ปิดเบราว์เซอร์ | ท้าย flow มี **Close web browser** |
| Replay ครั้งเดียวแล้วจบ | ต้อง Replay สำเร็จอย่างน้อย 2 ครั้งติดกัน |

---

## Variables

| ชื่อตอนสร้าง (ไม่มี `%`) | ตอนอ้างอิง | Type | ตัวอย่าง |
|--------------------------|------------|------|----------|
| `Browser` | `%Browser%` | Browser | — |
| `FullName` | `%FullName%` | Text | Somchai Demo |
| `Email` | `%Email%` | Text | somchai.demo@example.com |
| `Amount` | `%Amount%` | Text | 3000 |
| `FormDate` | `%FormDate%` | Text | 2026-08-08 |
| `Message` | `%Message%` | Text | Hello from Lab 01... |
| `SubmitResult` | `%SubmitResult%` | Text | *(ทางเลือก)* ข้อความยืนยันจากหน้า |

## Expected Result

- Flow รันจบโดยไม่มี error (Chrome)
- กรอกครบ 5 ช่อง: ชื่อ อีเมล จำนวนเงิน วันที่ หมายเหตุ — ค่ามาจากตัวแปร
- มีไฟล์ `C:\PAD-Labs\output\lab01\submit-proof.png`
- ปิดเบราว์เซอร์ท้าย flow

## Acceptance Criteria

- [ ] ตั้งชื่อ flow ตาม convention (`Lab01_RecordReplay`)
- [ ] ใช้ **Launch new Chrome** (หรือ Edge ถ้าไม่มี Chrome) ไป `https://ontoiq.tech/pad/01-forms.html`
- [ ] มี **Wait for web page content** ชี้ `Txt_Name` ก่อน Populate
- [ ] มี Populate ครบ 5 ช่อง (`Txt_Name` … `Txt_Note`) ใต้ screen `Lab01 Forms` — Emulate typing ปิด
- [ ] กด `Btn_Submit` แล้วได้ screenshot ที่ `C:\PAD-Labs\output\lab01\submit-proof.png`
- [ ] Replay ได้สำเร็จอย่างน้อย 2 ครั้งติดต่อกัน โดยฟอร์มถูกกรอกครบก่อน Submit
- [ ] UI Elements ใช้ selector ที่เสถียร (`id` / `data-pad`)
- [ ] ปิดเบราว์เซอร์ท้าย flow ด้วย **Close web browser**

## Troubleshooting

| อาการ | แก้ |
|-------|-----|
| กรอกได้แค่ช่องแรก / มีกล่อง suggestion ทับฟอร์ม | **Browser Autofill** — ปิด Microsoft Autofill + Save passwords / Autofill forms ใน Chrome แล้ว Replay; Populate ปิด Emulate typing ([community](https://community.powerplatform.com/forums/thread/details/?threadid=5b9067f5-2fec-4e44-b05e-9549f05ea7bd)) |
| Autofill ยังโผล่หลังปิด settings | หลัง **Populate** ใส่ **Send keys** `{Escape}` ก่อนช่องถัดไป |
| ขาดช่อง Amount / กรอกไม่ครบ 5 ช่อง | เพิ่ม Populate สำหรับ `#txt-amount` ด้วย `%Amount%` — ดูตาราง Step 5 |
| Errors: UI element `Lab01 Forms > …` wasn't found | ตั้งชื่อ screen/element ให้ตรงตาราง Input/Output หรือวาง catch-up (ฝัง UI Elements แล้ว) ใน flow ว่าง |
| Errors: Unknown argument(s): `Timeout` | Wait for web page content **ไม่มี** `Timeout` — ตั้งเวลารอในโหมด Wait ของ designer / ใช้รูปแบบ `WAIT (…) FOR N` ใน Robin |
| Errors: Unknown argument(s): `File` บน screenshot | เลือก Save เป็น **File** + PNG (action Save to file) |
| Recorder จับ element ผิด | ลบ UI element เดิม แล้ว capture ใหม่ด้วย picker → rename ตามตาราง |
| กรอกวันที่ไม่ได้ | ใช้ค่า `2026-08-08` ตามตัวแปร `FormDate` |
| Submit ไม่เกิดผล | มี Wait ก่อน Interact; ตรวจ validation; ปิด Autofill ทับปุ่มด้วย Esc |
| Extension ไม่ทำงาน | ติดตั้ง Chrome extension ของ PAD แล้วรีสตาร์ทเบราว์เซอร์ (แนะนำ MSI PAD) |
| ไม่มีโฟลเดอร์ output | สร้าง `C:\PAD-Labs\output\lab01\` ก่อน Take screenshot |

## Cleanup

- ปิดหน้าต่างเบราว์เซอร์ที่ยังค้างอยู่หลังจบการรัน
- ไม่ต้อง commit ค่าที่แก้ในโฟลเดอร์ working / output

## อ้างอิงเพิ่มใน Lab Kit

- Desktop UI พื้นฐาน: [Lab 01b Notepad](../01b-notepad/README.md) · [Lab 01b Calculator](../01b-calculator/README.md) *(optional)*
- Desktop Element UI เต็มรูปแบบ (วัน 2): [Lab 07 Contoso Invoice Ops](../07-contoso-invoice-ops/README.md)
- Microsoft sample desktop UI: [contoso-invoice-app](https://github.com/MicrosoftDocs/mslearn-developer-tools-power-platform/tree/master/power-automate-desktop/contoso-invoice-app)

> **Catch-up:** ตามไม่ทัน → วาง [`scripts/01-record-replay.robin`](scripts/01-record-replay.robin) ใน **flow ว่าง** (Ctrl+A แล้ว Ctrl+V)  
> สคริปต์มี: Set 5 ตัวแปร · สร้าง `output\lab01` · **Launch Chrome** · Wait `Txt_Name` · Populate 5 ช่อง (Emulate typing ปิด) · Click `Btn_Submit` · Screenshot `submit-proof.png` · Close browser  
> + ฝัง UI Elements screen **`Lab01 Forms`** ครบแล้ว — วางแล้วควรเห็นในแท็บ UI elements และรันกรอกฟอร์มได้
