# Lab 09 — Error Handling (Hands-on)

**อ่านก่อน:** [LESSON.md](LESSON.md) · **หน้าปกบท:** [README.md](README.md) · **พื้นฐาน:** [`shared/PAD-FUNDAMENTALS.md`](../../shared/PAD-FUNDAMENTALS.md)

**วัน:** 2 · **ระดับ:** Advanced  
**ทักษะ:** **On block error**, **On error** (Retry / Continue flow run), **Get last error**, การบันทึก log, screenshot และการปิดแอปอย่างปลอดภัย

> **Browser บล็อก Capture element:** ทำ [Lab 09b WinApp (Notepad)](../09b-error-handling-winapp/LAB.md) แทน — สอนกลไก error เดียวกันโดยไม่ใช้ web automation

## อ้างอิง (Aug 2026)

| แหล่ง | URL |
|-------|-----|
| Handle errors (หลักของ Lab นี้) | [desktop-flows/errors](https://learn.microsoft.com/power-automate/desktop-flows/errors) |
| Actions pane / On error | [actions-pane](https://learn.microsoft.com/power-automate/desktop-flows/actions-pane) |
| Official terminology (Lab Kit) | [`shared/OFFICIAL-TERMINOLOGY.md`](../../shared/OFFICIAL-TERMINOLOGY.md) |

## Setup บนเครื่อง (ทำก่อนเปิด designer)

1. สร้างโฟลเดอร์ (คัดลอกได้):

```text
C:\PAD-Labs\working\lab09\
```

```text
C:\PAD-Labs\logs\lab09\
```

2. คัดลอกไฟล์ใน [`assets/`](assets/) ไป:

```text
C:\PAD-Labs\working\lab09\
```

3. เตรียม path log (คัดลอกได้):

```text
C:\PAD-Labs\logs\lab09\error-log.csv
```

4. อ่านสคริปต์ fault: [`assets/fault-injection.md`](assets/fault-injection.md)

## Test Cases (เจตนาให้พัง / กู้)

### Core cases

| Case | Phase 1 | ไฟล์/URL | พฤติกรรมที่คาด |
|------|---------|----------|----------------|
| A Missing file | — | path ใน [`assets/missing-file-path.txt`](assets/missing-file-path.txt) | **On block error** → **Get last error** → log → ไปต่อ |
| B Bad URL | — | [`assets/bad-url.txt`](assets/bad-url.txt) | จับ error เปิดเพจ → **Take screenshot of web page** (ถ้าได้) → continue |
| C Flaky wait | 11 | https://ontoiq.tech/pad/11-delay.html | **On error → Retry** และ/หรือ Loop + **Wait for web page content** สูงสุด 3 ครั้ง |
| D Dialog | 04 | https://ontoiq.tech/pad/04-dialogs.html | จัดการ alert/confirm โดยไม่ให้ flow ตายเงียบ |
| E Recover happy path | 01 | https://ontoiq.tech/pad/01-forms.html | หลัง error ก่อนหน้า ยัง Populate + Press button ได้ |

### Challenge cases (Phase 1 ที่เสริม)

| Case | Phase 1 | URL / ไฟล์ | พฤติกรรมที่คาด |
|------|---------|------------|----------------|
| F OCR mismatch | 10 | https://ontoiq.tech/pad/10-ocr.html | อ่านค่า OCR/hidden answer — ถ้าไม่ตรง log `OCR_MISMATCH` แล้ว continue |
| G Files fault | 05 | https://ontoiq.tech/pad/05-files.html | upload path ที่ไม่มี → จับ error แล้ว upload [`assets/recovery-upload.txt`](assets/recovery-upload.txt) |
| H Iframe trap | 08 | https://ontoiq.tech/pad/08-iframe.html | miss-frame แล้วกู้ด้วย set iframe ถูกต้อง |
| I API bad then good | 12 | https://ontoiq.tech/pad/12-api.html | endpoint ผิด → log → health ได้ 2xx |

รายละเอียดสคริปต์: [`assets/fault-injection.md`](assets/fault-injection.md)

## Input / Output

| | Path |
|--|------|
| Fault script | [`assets/fault-injection.md`](assets/fault-injection.md) |
| Log template | [`assets/error-log-template.csv`](assets/error-log-template.csv) |
| Your log | ดู code block ใน Setup / Step 1 |
| Missing path hint | [`assets/missing-file-path.txt`](assets/missing-file-path.txt) |
| Bad URL hint | [`assets/bad-url.txt`](assets/bad-url.txt) |

---

## Hands-on ทีละขั้น

### Step 0 — สร้าง flow

1. เปิด Power Automate for desktop → **New flow**
2. ชื่อ flow (คัดลอกได้):

```text
Lab09_ErrorHandling
```

3. กด **Create**

> **กฎตัวแปรใน PAD (อ่านก่อนทำ Step ถัดไป)**  
> - ช่อง **Name** ของ **Set variable**, ส่วน **Variables produced**, และ **Store into** = พิมพ์ชื่ออย่างเดียว **ไม่มี `%`** เช่น `WorkingRoot`  
> - ช่องอื่นที่ต้องดึงค่าตัวแปร (Folder, File path, Text, …) = ใช้ `%WorkingRoot%` (**มี `%` ครบสองด้าน**)  
> - หลังสร้างแล้ว Variables pane อาจแสดงเป็น `%WorkingRoot%` — เป็นเรื่องปกติ

### Step 1 — Init ตัวแปรและ header log

1. ลาก **Set variable** (Name ไม่มี `%`):
   - Name: `WorkingRoot` ← Value:

```text
C:\PAD-Labs\working\lab09
```

   - Name: `ErrorLogPath` ← Value:

```text
C:\PAD-Labs\logs\lab09\error-log.csv
```

   - Name: `RetryCount` ← Value:

```text
0
```

   - Name: `Fatal` ← Value:

```text
False
```

     (หรือตามที่ designer รองรับ)
2. นโยบายรันซ้ำสำหรับ log: เลือกระหว่าง Overwrite ตอนเริ่ม หรือ Append ทั้งรอบ — ให้ชัดเจน
3. ลาก **Write text to file**
   - File path: (คัดลอก)

```text
%ErrorLogPath%
```

   - Text: header ตาม [`assets/error-log-template.csv`](assets/error-log-template.csv)
   - If file exists: Overwrite (รอบเริ่มต้น) หรือตามนโยบายที่ประกาศใน Acceptance

### Step 2 — Case A: Missing file + On block error + Get last error

1. อ่าน path ที่ตั้งใจให้พังจาก File path (คัดลอก):

```text
%WorkingRoot%\missing-file-path.txt
```

   (ด้วย **Read text from file**) → **Variables produced:** `MissingPath` ← **ไม่ใส่ `%`**
2. ลาก **On block error** ครอบชุด action ของ Case A
3. **ภายในบล็อก** ลาก action ที่จะล้ม เช่น **Read text from file** / **Get files in folder** ไปที่ (คัดลอก):

```text
%MissingPath%
```

   (path ที่ไม่มีจริง)
4. ในหน้านโยบาย **On block error** (หรือกิ่ง Exception):
   - ลาก **Get last error**
   - **Variables produced:** `LastError` ← **ไม่ใส่ `%`** (อ้างอิงด้วย `%LastError%`)
   - **Write text to file** append แถว log — Case Value:

```text
A
```

     Message / Location (คัดลอก):

```text
%LastError.Message%
```

```text
%LastError.Location%
```

   - ตั้งให้ **Continue** flow ไป Case ถัดไป — อย่าหยุดทั้ง flow
5. ปิดบล็อกตามโครง designer

> จำไว้: ใช้ชื่อ **On block error** / **Get last error** — ไม่เขียนว่า “ใส่ Try-Catch”

### Step 3 — Case B: Bad URL + screenshot

1. **Read text from file** → **Variables produced:** `BadUrl` ← **ไม่ใส่ `%`** จากไฟล์ใน working (อ้างอิงด้วย `%BadUrl%`)
2. ลาก **On block error** (จุดที่ 2 ตามเกณฑ์อย่างน้อย 2 จุด) ครอบการเปิดเพจ
3. **ภายในบล็อก:**
   - **Launch new Microsoft Edge** หรือ **Launch new Chrome** (ถ้ายังไม่มี `%Browser%`) / **Go to web page** ไป URL (คัดลอก):

```text
%BadUrl%
```

4. เมื่อ error:
   - **Get last error** → log Case Value:

```text
B
```

   - ถ้ายังมี browser instance: **Take screenshot of web page** บันทึกใต้โฟลเดอร์ (คัดลอก):

```text
C:\PAD-Labs\logs\lab09\
```

   - Continue ไป Case C

### Step 4 — Case C: Flaky wait + On error → Retry

1. **Go to web page** → URL (คัดลอก):

```text
https://ontoiq.tech/pad/11-delay.html
```

2. ลาก **Wait for web page content** รอ element ที่จะพร้อมช้า
3. เปิดการตั้งค่า **On error** ของ action นี้ (ไอคอน/แท็บ On error ในหน้าต่าง action — ไม่ใช่ชื่อ Action ว่า Try-Catch):
   - **Retry** action ตามจำนวนที่จำกัด (รวมแล้วไม่เกินแนว 3 ครั้ง) และ/หรือ
   - ใช้ **Loop** / **Loop condition** กับ (คัดลอก):

```text
%RetryCount%
```

     สูงสุด 3 แล้วค่อยถือว่าล้มเหลวแบบควบคุม
4. เมื่อสำเร็จหรือหมดรอบ: append log Case Value:

```text
C
```

   (สำเร็จหรือหมด retry ให้ระบุใน Notes)

### Step 5 — Case D: Dialogs

1. **Go to web page** → URL (คัดลอก):

```text
https://ontoiq.tech/pad/04-dialogs.html
```

2. Interact กับปุ่มที่ขึ้น alert/confirm ตามหน้า
3. จัดการ dialog ด้วย action ที่เหมาะสม (กดยอมรับ/ยกเลิกตามที่หน้า Lab ออกแบบ) โดยครอบด้วย **On block error** หรือ **On error** ถ้าจำเป็น
4. Log ข้อความ (คัดลอก) ลง `%ErrorLogPath%`:

```text
DIALOG_HANDLED
```

5. Continue

### Step 6 — Case E: Recovery happy path (Forms)

เป้าหมาย: หลังมี error จาก A–D แล้ว flow ยังทำงานต่อได้

1. **Go to web page** → URL (คัดลอก):

```text
https://ontoiq.tech/pad/01-forms.html
```

2. **Wait for web page content**
3. **Populate text field on web page** กรอกค่าจำลองครบช่องบังคับ
4. **Press button on web page** Submit
5. Log ข้อความ (คัดลอก) ลง error-log:

```text
RECOVERY_OK
```

6. ถ้าขั้นตอนนี้พัง: **Get last error** แล้ว **Set variable** Name: `Fatal` ← **ไม่ใส่ `%`** ตามนโยบาย — แต่เกณฑ์ผ่านต้องการให้ Case E สำเร็จหลัง error ก่อนหน้า

### Step 7 — Challenge Cases F–I (ทำอย่างน้อย 2)

ทำต่อใน flow เดียวกัน ครอบด้วย **On block error** / **On error** ตามเคส:

| Case | ขั้นสั้น ๆ |
|------|------------|
| F | ไป `10-ocr.html` → อ่านค่า → ถ้าไม่ตรง log `OCR_MISMATCH` แล้ว continue |
| G | ไป `05-files.html` → upload path ผิด → จับ error → upload recovery file |
| H | ไป `08-iframe.html` → พลาด frame แล้วกู้ด้วย iframe ที่ถูก |
| I | ไป `12-api.html` → เรียก endpoint ผิด → log → เรียก health ได้ 2xx |

URL / path ที่ใช้ใน Challenge (คัดลอกได้):

**Case F**

```text
https://ontoiq.tech/pad/10-ocr.html
```

Log เมื่อไม่ตรง:

```text
OCR_MISMATCH
```

**Case G**

```text
https://ontoiq.tech/pad/05-files.html
```

Upload กู้:

```text
%WorkingRoot%\recovery-upload.txt
```

**Case H**

```text
https://ontoiq.tech/pad/08-iframe.html
```

**Case I**

```text
https://ontoiq.tech/pad/12-api.html
```

### Step 8 — Cleanup แม้เกิด error

1. ท้าย Main (และในกิ่ง error ระดับ flow ถ้ารองรับ): **Close web browser** ถ้ายังเปิด — Browser instance (คัดลอก):

```text
%Browser%
```

2. ถ้าเปิด Excel ระหว่างทดสอบ: **Close Excel**
3. อย่าปล่อย instance ค้างหลัง Run

### Step 9 — รันและตรวจ

1. กด **Run**
2. เปิด `error-log.csv` — ต้องมีอย่างน้อย 1 แถวของ Case A และมี `RECOVERY_OK` จาก Case E
3. รันซ้ำรอบสองที่ path log เดิม — ต้องไม่พัง (overwrite/append ชัด)
4. ตรวจว่าไม่มี browser/Excel ค้าง

---

## จุดที่มักทำผิด

| ผิด | ถูก |
|-----|-----|
| พิมพ์ `%Name%` ในช่อง Name / **Variables produced** | ใช้ชื่อเปล่าไม่มี `%` เช่น `WorkingRoot`, `LastError` |
| เรียกกลไกว่า “Try-Catch action” | ใช้ **On block error** / **On error** / **Get last error** |
| กลืน error โดยไม่ log | **Get last error** แล้วเขียน `%LastError.Message%` / `.Location%` |
| Retry ไม่จำกัด | จำกัดครั้งใน **On error → Retry** หรือ max loop |
| Case E ไม่ทำหลัง error | จัดลำดับ A→E ให้ recovery อยู่ท้ายชุด core |
| ลืมปิด browser | **Close web browser** ใน cleanup |
| Screenshot ทั้งที่ไม่มี browser | ตรวจว่ามี instance ก่อน **Take screenshot of web page** |

---

## Variables

| ชื่อตอนสร้าง (ไม่มี `%`) | ตอนอ้างอิง | Type |
|--------------------------|------------|------|
| `LastError` | `%LastError%` | Error (จาก **Get last error**) |
| `RetryCount` | `%RetryCount%` | Numeric |
| `ErrorLogPath` | `%ErrorLogPath%` | Text |
| `WorkingRoot` | `%WorkingRoot%` | Text |
| `Browser` | `%Browser%` | Browser |
| `Fatal` | `%Fatal%` | Boolean |
| `MissingPath` / `BadUrl` | `%MissingPath%` / `%BadUrl%` | Text |

## Expected Result

- มี error-log อย่างน้อย 1 แถวสำหรับ Case A
- Flow ไม่หยุดแบบ unmanaged ก่อนจบชุดทดสอบ
- Case E สำเร็จหลังมี error ก่อนหน้า

## Acceptance Criteria

- [ ] ใช้ **On block error** อย่างน้อย 2 จุด
- [ ] ใช้ **Get last error** อย่างน้อย 1 ครั้งเมื่อ log
- [ ] มีไฟล์ log
- [ ] **รันซ้ำได้:** รันครั้งที่ 2 แล้วเขียน log ที่ path เดิมได้โดยไม่พัง (overwrite / append policy ชัด)
- [ ] มีนโยบาย retry ชัดเจนสำหรับ Case C (**On error → Retry** และ/หรือ max loop)
- [ ] Cleanup ด้วย **Close web browser** / **Close Excel**
- [ ] (Challenge) ทำอย่างน้อย 2 จาก Cases F–I

## Troubleshooting

| อาการ | แก้ |
|-------|-----|
| Error ถูกกลืน ไม่รู้สาเหตุ | **Get last error** แล้ว log `%LastError.Message%` / `.Location%` |
| Retry ไม่จบ | จำกัดจำนวน retry ใน On error; หลีกเลี่ยง Repeat action ไม่จำกัด |
| Screenshot ว่าง | ตรวจว่ามี browser instance เปิดอยู่ |
| Selector ไม่เจอ | เพิ่ม **Wait for web page content** / recapture ([docs](https://learn.microsoft.com/troubleshoot/power-platform/power-automate/desktop-flows/ui-automation/failed-get-ui-element)) |

## Cleanup

- ล้าง logs เก่าก่อน demo รอบใหม่ถ้าต้องการไฟล์สะอาด

## หมายเหตุสไลด์ vs official

สไลด์อาจกล่าวถึง “Activate Phone Number Input” — **ไม่ใช่เกณฑ์บังคับของ Lab นี้** ให้ใช้ **Wait for window content** / **Focus window** / **On error** ตาม [official error handling](https://learn.microsoft.com/power-automate/desktop-flows/errors)

> **Catch-up:** ตามไม่ทัน → วาง [`scripts/09-error-handling.robin`](scripts/09-error-handling.robin) ใน flow **ว่าง** (partial-ui + bundled Delay / Dialogs / Forms; Cases A–E)
