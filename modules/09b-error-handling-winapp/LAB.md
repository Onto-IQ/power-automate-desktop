# Lab 09b — Error Handling WinApp (Hands-on)

**อ่านก่อน:** [LESSON.md](LESSON.md) · **หน้าปกบท:** [README.md](README.md) · **พื้นฐาน:** [`shared/PAD-FUNDAMENTALS.md`](../../shared/PAD-FUNDAMENTALS.md)

**วัน:** 2 · **ระดับ:** Advanced  
**ทักษะ:** **On block error** (SET-only), **Get last error**, logging, **Wait for window** + retry, Cleanup บน Notepad  
**Flow ชื่อ:** `Lab09b_ErrorHandling_WinApp`  
**ทดแทน:** [Lab 09 web](../09-error-handling/LAB.md) เมื่อ browser บล็อก Capture element  
**อ้างอิงลำดับ action:** [`scripts/09b-error-handling-winapp.robin`](scripts/09b-error-handling-winapp.robin)

> Lab นี้**ไม่ใช้** Launch browser / Wait for web page content  
> พื้นฐาน Notepad: [Lab 01b](../01b-notepad/LAB.md) · ทบทวน R6 จาก [Lab 07 Contoso](../07-contoso-invoice-ops/LAB.md) (SET-only + Get last error นอก handler)

## อ้างอิง (Aug 2026)

| แหล่ง | URL |
|-------|-----|
| Handle errors | [desktop-flows/errors](https://learn.microsoft.com/power-automate/desktop-flows/errors) |
| Get last error | [flowcontrol#getlasterror](https://learn.microsoft.com/power-automate/desktop-flows/actions-reference/flowcontrol#getlasterror) |
| UI automation | [actions-reference/uiautomation](https://learn.microsoft.com/power-automate/desktop-flows/actions-reference/uiautomation) |
| Official terminology | [`shared/OFFICIAL-TERMINOLOGY.md`](../../shared/OFFICIAL-TERMINOLOGY.md) |

## Setup บนเครื่อง (ทำก่อนเปิด designer)

1. สร้างโฟลเดอร์ (คัดลอกได้):

```text
C:\PAD-Labs\working\lab09b\
```

```text
C:\PAD-Labs\logs\lab09b\
```

```text
C:\PAD-Labs\output\lab09b\
```

2. คัดลอกไฟล์ใน [`assets/`](assets/) ไป:

```text
C:\PAD-Labs\working\lab09b\
```

3. เตรียม path log:

```text
C:\PAD-Labs\logs\lab09b\error-log.csv
```

4. ปิด Notepad ที่เปิดค้างก่อนรัน Lab  
5. อ่านสคริปต์ fault: [`assets/fault-injection.md`](assets/fault-injection.md)

## Test Cases (ตรงกับ catch-up)

### Core (A–E)

| Case | ใน script | พฤติกรรมที่คาด |
|------|-----------|----------------|
| A | Read path ที่ไม่มี | **On block error** (SET `CaseFailed`) → นอกบล็อก: **Get last error** → log Case `A` → ไปต่อ |
| B | **Run application** path จาก `bad-app-path.txt` | เหมือน A → log Case `B` |
| C | เปิด Notepad → Loop ≤3 Wait title `ThisWindowDoesNotExist` | แต่ละครั้งพัง log `RETRY_WAIT` → แล้ว Wait class `Notepad` → log `wait-success` |
| D | Focus + **Send keys** → **Close window** → `{Alt}({N})` | log `DIALOG_HANDLED` (ถ้าพังในบล็อก → `DIALOG_PENDING_REBIND`) |
| E | Notepad ใหม่ → Send keys ข้อความ + Ctrl+S + `%OutputPath%` + Enter | log `RECOVERY_OK` |

### Challenge

| Case | ใน catch-up | พฤติกรรมที่คาด |
|------|-------------|----------------|
| G | มีครบ | Copy ไฟล์ที่ไม่มี → `FILE_MISSING` → Copy `recovery-upload.txt` → `FILE_OK` |
| H | มีครบ | Focus title ผิด → `FOCUS_MISS` → Focus class `Notepad` → `FOCUS_OK` |
| F | stub (ทำในชั้น) | Wait/Populate ผิด element → `UI_MISMATCH` แล้วกู้ |

Acceptance Challenge: ทำอย่างน้อย 2 จาก F–H (catch-up ครอบ G+H แล้ว)

## Input / Output

| | Path |
|--|------|
| Fault script | [`assets/fault-injection.md`](assets/fault-injection.md) |
| Log header | `Timestamp,CaseId,Severity,Message,RetryCount,Fatal` |
| Your log | `C:\PAD-Labs\logs\lab09b\error-log.csv` |
| Missing / Bad app | [`assets/missing-file-path.txt`](assets/missing-file-path.txt) · [`assets/bad-app-path.txt`](assets/bad-app-path.txt) |
| Recovery text | [`assets/notepad-recovery.txt`](assets/notepad-recovery.txt) |
| Output Save As | `C:\PAD-Labs\output\lab09b\recovery-ok.txt` |

### โครง On block error (บังคับให้ตรง catch-up)

ใน handler ของ **On block error** ใส่ได้แค่ **Set variable** (SET-only) — ทบทวนกฎจาก Lab 07 R6  
**Get last error**, **Get current date and time**, **Write text to file**, **Increase variable** ทำ**นอก**บล็อกหลัง flag

```text
CaseFailed = False
On block error { งานที่ตั้งใจให้พัง }  → เมื่อพัง: CaseFailed = True
ถ้า CaseFailed = True:
  Get last error → LastError (Clear error / Reset On)
  Get current date and time → Now
  Write text to file (append log)
```

Robin ของ Get last error ที่ paste ได้:

```text
ERROR => LastError Reset: True
```

(`Reset` = **Clear error** ตาม Learn)

---

## Hands-on ทีละขั้น

### Step 0 — สร้าง flow

1. เปิด Power Automate for desktop → **New flow**
2. ชื่อ flow:

```text
Lab09b_ErrorHandling_WinApp
```

3. กด **Create**

> **กฎ `%`:** Name / Variables produced / Store into = **ไม่มี `%`** · อ้างอิงใช้ `%Name%`

### Step 1 — Init ตัวแปร + สร้างโฟลเดอร์ + header log

1. **Set variable** (Name ไม่มี `%`) ตาม catch-up:

| Name | Value |
|------|--------|
| `WorkingRoot` | `C:\PAD-Labs\working\lab09b` |
| `ErrorLogPath` | `C:\PAD-Labs\logs\lab09b\error-log.csv` |
| `OutputPath` | `C:\PAD-Labs\output\lab09b\recovery-ok.txt` |
| `OutputRoot` | `C:\PAD-Labs\output\lab09b` |
| `RetryCount` | `0` |
| `Fatal` | `False` |
| `CaseFailed` | `False` |
| `WaitFailed` | `False` |
| `ErrorLogHeader` | `Timestamp,CaseId,Severity,Message,RetryCount,Fatal` |

Values คัดลอกได้:

```text
C:\PAD-Labs\working\lab09b
```

```text
C:\PAD-Labs\logs\lab09b\error-log.csv
```

```text
C:\PAD-Labs\output\lab09b\recovery-ok.txt
```

```text
C:\PAD-Labs\output\lab09b
```

```text
Timestamp,CaseId,Severity,Message,RetryCount,Fatal
```

2. (แนะนำตาม script) **If folder** ไม่มี → **Create folder** สำหรับ `C:\PAD-Labs\logs\lab09b` และ `%OutputRoot%`
3. **Write text to file**
   - File path: `%ErrorLogPath%`
   - Text: `%ErrorLogHeader%`
   - If file exists: **Overwrite**

### Step 2 — Case A: Missing file

1. **Read text from file** จาก:

```text
%WorkingRoot%\missing-file-path.txt
```

   → **Variables produced:** `MissingPath`
2. **Set variable** `CaseFailed` ← `False`
3. **On block error** ครอบ:
   - ในกิ่ง error: **Set variable** `CaseFailed` ← `True` เท่านั้น
   - ในบล็อกงาน: **Read text from file** path `%MissingPath%` → `MissingContent`
4. **หลัง**ปิดบล็อก — **If** `%CaseFailed%` = True:
   - **Get last error** → `LastError` (เปิด Clear error)
   - **Get current date and time** → `Now`
   - **Write text to file** append ไป `%ErrorLogPath%` — แถวแนว:

```text
%Now%,A,Error,%LastError.Message%,0,False
```

### Step 3 — Case B: Bad application path

1. **Read text from file** จาก:

```text
%WorkingRoot%\bad-app-path.txt
```

   → `BadAppPath`
2. โครงเดียวกับ Case A: `CaseFailed` + **On block error** (SET-only) ครอบ **Run application** path `%BadAppPath%`
3. นอกบล็อกเมื่อพัง: **Get last error** → log:

```text
%Now%,B,Error,%LastError.Message%,0,False
```

### Step 4 — Case C: Flaky wait + Retry (Notepad)

1. **Run application**:

```text
C:\Windows\System32\notepad.exe
```

2. **Loop while** `%RetryCount%` < `3`:
   - `WaitFailed` ← `False`
   - **On block error** (SET `WaitFailed` = True) ครอบ **Wait for window**
     - Title:

```text
ThisWindowDoesNotExist
```

     - Class: ว่าง · Focus: Off · timeout สั้น (**3** วินาที ตาม catch-up)
   - ถ้า `%WaitFailed%` = True: **Increase variable** `RetryCount` +1 แล้ว append log:

```text
%Now%,C,Warning,RETRY_WAIT,%RetryCount%,False
```

3. หลังออกจาก Loop: **Wait for window**
   - Title: **ว่าง**
   - Class:

```text
Notepad
```

   - Focus: On · timeout **30** วินาที
4. Append log:

```text
%Now%,C,Info,wait-success,%RetryCount%,False
```

### Step 5 — Case D: Save dialog (Don't Save)

ตาม catch-up (ใช้ **Send keys** — ไม่บังคับ Capture Edit):

1. **Focus window** — Title ว่าง · Class `Notepad`
2. **Send keys**:

```text
Lab09b dialog test
```

3. `CaseFailed` ← `False`
4. **On block error** (SET-only) ครอบ:
   - **Close window** — Title ว่าง · Class `Notepad`
   - **Wait** 1 วินาที
   - **Send keys**:

```text
{Alt}({N})
```

   (Don't Save — ถ้า Win11 ไม่รับ ให้ REBIND ปุ่ม Don't Save)
5. นอกบล็อก: ถ้าพัง log `DIALOG_PENDING_REBIND` ไม่เช่นนั้น:

```text
DIALOG_HANDLED
```

   แถวเต็มแนว: `%Now%,D,Info,DIALOG_HANDLED,0,False`

### Step 6 — Case E: Recovery (Save As)

1. **Read text from file** → `NoteText` จาก:

```text
%WorkingRoot%\notepad-recovery.txt
```

2. **Run application** → `notepad.exe` อีกครั้ง
3. **Wait for window** class `Notepad` (Focus On) · **Focus window** class `Notepad`
4. ตาม catch-up ใช้ **Send keys** (REBIND เป็น **Populate text field in window** + Simulate ได้ถ้าต้องการ):
   - ส่ง `%NoteText%`
   - ส่ง `{Control}{S}`
   - **Wait** 1 วินาที
   - ส่ง `%OutputPath%`
   - ส่ง `{Enter}`
   - (ถ้ามี Confirm overwrite → REBIND Yes/Replace)
5. Append log:

```text
%Now%,E,Info,RECOVERY_OK,0,False
```

### Step 7 — Challenge G + H (ใน catch-up) และ F (ในชั้น)

**Case G** (ตรง script):

1. **On block error** + SET `CaseFailed` ครอบ **Copy file(s)** จาก path ที่ไม่มี:

```text
%WorkingRoot%\this-file-does-not-exist.txt
```

   ไป `%OutputRoot%` → เมื่อพัง log `FILE_MISSING`
2. **Copy file(s)** กู้:

```text
%WorkingRoot%\recovery-upload.txt
```

```text
C:\PAD-Labs\output\lab09b\
```

   → log `FILE_OK`

**Case H** (ตรง script):

1. **On block error** ครอบ **Focus window** title:

```text
ThisWindowDoesNotExist
```

   → log `FOCUS_MISS`
2. **Focus window** class `Notepad` → log `FOCUS_OK`

**Case F** (ทำในชั้น — ไม่มีใน catch-up): Wait/Populate ผิด element → log `UI_MISMATCH` แล้วกู้

### Step 8 — Cleanup

ตาม catch-up — ครอบด้วย **On block error** (handler ว่างได้):

1. **Close window** — Title ว่าง · Class `Notepad`
2. **Wait** 1 วินาที
3. **Send keys** `{Alt}({N})` เผื่อ Save dialog ค้าง
4. อย่าปล่อย Notepad ค้างหลัง Run

### Step 9 — รันและตรวจ

1. กด **Run**
2. เปิด `C:\PAD-Labs\logs\lab09b\error-log.csv` — ต้องมี Case `A` (และ ideally `B`,`C`,`E`) และมี `RECOVERY_OK`
3. ตรวจ output (ถ้า Save As สำเร็จ):

```text
C:\PAD-Labs\output\lab09b\recovery-ok.txt
```

4. Challenge: มี `FILE_OK` / `FOCUS_OK` ถ้าทำ G/H
5. รันซ้ำรอบสอง — header Overwrite ที่ต้นรอบ / append แถวเคส ต้องไม่พัง
6. ไม่มี Notepad ค้าง

---

## จุดที่มักทำผิด

| ผิด | ถูก |
|-----|-----|
| ใส่ **Get last error** / **Write text** ในกิ่ง On block error ตอน paste Robin | ใน handler ใช้แค่ **Set variable** flag — Get last error / log อยู่นอกบล็อก |
| ใช้ `FlowControl.GetLastError` ใน Robin | ใช้ `ERROR => LastError Reset: True` หรือลากใน designer |
| พิมพ์ `%Name%` ในช่อง Name | ชื่อเปล่า เช่น `CaseFailed`, `LastError` |
| Retry ไม่จำกัด | Loop `RetryCount` < 3 ตาม catch-up |
| Close ด้วย title `Untitled - Notepad` อย่างเดียว | Class `Notepad` (title ว่าง) |
| ลืมปิด Notepad | Cleanup Close + Alt+N |

---

## Variables (ตรง catch-up)

| ชื่อตอนสร้าง | ตอนอ้างอิง | ใช้เมื่อ |
|--------------|------------|---------|
| `WorkingRoot` | `%WorkingRoot%` | path working |
| `ErrorLogPath` | `%ErrorLogPath%` | log CSV |
| `OutputPath` | `%OutputPath%` | Save As Case E |
| `OutputRoot` | `%OutputRoot%` | Copy Challenge G |
| `RetryCount` | `%RetryCount%` | Case C |
| `Fatal` | `%Fatal%` | สำรอง |
| `CaseFailed` / `WaitFailed` | `%CaseFailed%` / `%WaitFailed%` | flag นอก handler |
| `ErrorLogHeader` | `%ErrorLogHeader%` | header แถวแรก |
| `MissingPath` / `BadAppPath` / `NoteText` | `%…%` | Case A / B / E |
| `LastError` | `%LastError.Message%` | หลัง Get last error |
| `Now` | `%Now%` | timestamp ใน log |
| `LogLine` | `%LogLine%` | ข้อความแถว log |

## Expected Result

- `error-log.csv` มีแถว Case A ที่มาจาก **Get last error** (`%LastError.Message%`)
- Flow ไม่ unmanaged-crash ก่อนจบ A→E (+ G/H ถ้าทำ)
- Case E log `RECOVERY_OK` หลังมี error ก่อนหน้า

## Acceptance Criteria

- [ ] **On block error** ≥ 2 จุด และใน handler เป็น **SET-only** (ตรง catch-up)
- [ ] **Get last error** ≥ 1 ครั้งเมื่อ log Case A (และ/หรือ B)
- [ ] มี `C:\PAD-Labs\logs\lab09b\error-log.csv` schema ตาม header
- [ ] Case C: Loop retry สูงสุด 3 + log `RETRY_WAIT` / `wait-success`
- [ ] Case E: log `RECOVERY_OK`
- [ ] Cleanup **Close window** class `Notepad`
- [ ] **ไม่มี** Launch browser เป็นเกณฑ์บังคับ
- [ ] Challenge ≥ 2 จาก F–H (catch-up มี G+H)

## Troubleshooting

| อาการ | แก้ |
|-------|-----|
| statement isn't allowed inside exception handling | ย้าย Get last error / File / Increase ออกนอก On block error |
| Module GetLastError wasn't found (ตอน paste) | ใช้ `ERROR => LastError Reset: True` หรือลากจาก Actions |
| Retry ไม่จบ | ตรวจ Loop `RetryCount` < 3 |
| Close / Focus หาหน้าต่างไม่เจอ | Class `Notepad` · ปิด instance ค้างก่อนรัน |
| Don't Save ไม่ทำงาน | REBIND ปุ่ม Don't Save (Win11) แทน `{Alt}({N})` |
| Can't access UI elements | elevation เดียวกันระหว่าง PAD กับ Notepad |

## Cleanup

- ล้าง `error-log.csv` เก่าก่อน demo ถ้าต้องการไฟล์สะอาด
- ปิด Notepad ค้างด้วยมือถ้า flow หยุดกลางทาง

> **Catch-up:** วาง [`scripts/09b-error-handling-winapp.robin`](scripts/09b-error-handling-winapp.robin) ใน flow ว่าง (partial-ui — D/E อาจต้อง REBIND บน Win11)  
> ลำดับใน LAB นี้ = ลำดับใน script (A→E → G → H → Cleanup)
