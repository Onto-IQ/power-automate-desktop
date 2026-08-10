# Lab 04 — Conditional Automation (Hands-on)

**อ่านก่อน:** [LESSON.md](LESSON.md) · **หน้าปกบท:** [README.md](README.md) · **พื้นฐาน:** [`shared/PAD-FUNDAMENTALS.md`](../../shared/PAD-FUNDAMENTALS.md)

**วัน:** 2 · **ระดับ:** Intermediate  
**ทักษะ:** If / Else If / Else, เปรียบเทียบข้อความ/ตัวเลข, จัดไฟล์ตามกฎธุรกิจ

## อ้างอิง (Aug 2026)

| แหล่ง | URL |
|-------|-----|
| Folder actions | [actions-reference/folder](https://learn.microsoft.com/power-automate/desktop-flows/actions-reference/folder) |
| File actions | [actions-reference/file](https://learn.microsoft.com/power-automate/desktop-flows/actions-reference/file) |
| Getting started (file pattern) | [getting-started-freeorg](https://learn.microsoft.com/power-automate/desktop-flows/getting-started-freeorg) |

## Setup บนเครื่อง (ทำก่อนเปิด designer)

1. สร้างโฟลเดอร์ working และ output (คัดลอก path):

```text
C:\PAD-Labs\working\lab04\
```

```text
C:\PAD-Labs\output\lab04\
```

2. คัดลอกทั้งโฟลเดอร์ [`assets/inbox`](assets/inbox/) ไปยัง:

```text
C:\PAD-Labs\working\lab04\inbox
```

3. เตรียมโฟลเดอร์ปลายทางภายใต้ working (หรือให้ Flow สร้างใน Hands-on):

```text
C:\PAD-Labs\working\lab04\approved
```

```text
C:\PAD-Labs\working\lab04\rejected
```

```text
C:\PAD-Labs\working\lab04\review
```

4. อ่านกฎใน [`assets/business-rules.md`](assets/business-rules.md)

> ถ้าใช้ไดรฟ์อื่นได้ — แต่ต้องใช้ path นั้นใน `%WorkingRoot%` ให้สม่ำเสมอทั้ง flow

## Business Rules

| เงื่อนไข | Action |
|----------|--------|
| `Priority=High` และ `Status=Ready` | ย้ายไป `approved/` |
| `Priority=Low` หรือ `Status=Invalid` | ย้ายไป `rejected/` |
| อื่น ๆ | ย้ายไป `review/` |

รูปแบบชื่อไฟล์ mock: `REQ-{LeadId}-{Priority}-{Status}.txt`  
ตัวอย่าง: `REQ-L1001-High-Ready.txt`

กฎอยู่ใน [`assets/business-rules.md`](assets/business-rules.md) และสะท้อนในชื่อไฟล์ inbox

## Input / Output

| | Path |
|--|------|
| Inbox samples | [`assets/inbox/`](assets/inbox/) |
| Rules | [`assets/business-rules.md`](assets/business-rules.md) |
| Expected | [`assets/expected-routing.csv`](assets/expected-routing.csv) |
| Log | ดู code block ใน Step 6 |

### Expected routing (จาก expected-routing.csv)

| FileName | ExpectedFolder |
|----------|----------------|
| `REQ-L1001-High-Ready.txt` | approved |
| `REQ-L1002-Low-New.txt` | rejected |
| `REQ-L1003-Medium-Ready.txt` | review |
| `REQ-L1004-High-Invalid.txt` | rejected |
| `REQ-L1005-High-New.txt` | review |

---

## Hands-on ทีละขั้น

### Step 0 — สร้าง flow

1. เปิด Power Automate for desktop → **New flow**
2. ชื่อ flow (คัดลอกได้):

```text
Lab04_ConditionalAutomation
```

3. กด **Create**

> **กฎตัวแปรใน PAD (อ่านก่อนทำ Step ถัดไป)**  
> - ช่อง **Name** ของ **Set variable**, ส่วน **Variables produced**, และ **Store into** = พิมพ์ชื่ออย่างเดียว **ไม่มี `%`** เช่น `WorkingRoot`  
> - ช่องอื่นที่ต้องดึงค่าตัวแปร (Folder, File path, Text, …) = ใช้ `%WorkingRoot%` (**มี `%` ครบสองด้าน**)  
> - หลังสร้างแล้ว Variables pane อาจแสดงเป็น `%WorkingRoot%` — เป็นเรื่องปกติ

### Step 1 — ตั้ง path และตัวนับ

1. ลาก **Set variable**
2. ตั้งค่า:
   - Name: `WorkingRoot` ← **ไม่ใส่ `%`**
   - Value: (คัดลอกด้านล่างวางในช่อง Value — หรือ path ที่คุณใช้จริง)

```text
C:\PAD-Labs\working\lab04
```

3. เพิ่ม **Set variable** อีก 3 ตัว (Name ไม่มี `%`):
   - Name: `ApprovedCount` ← Value:

```text
0
```

   - Name: `RejectedCount` ← Value:

```text
0
```

   - Name: `ReviewCount` ← Value:

```text
0
```

4. (แนะนำ) ตั้งตัวแปรข้อความ log เริ่มต้น:
   - Name: `RoutingLog` ← **ไม่ใส่ `%`**
   - Value: (คัดลอกด้านล่างวางในช่อง Value — บรรทัดหัวตาราง CSV)

```text
FileName,Folder,Priority,Status
```

### Step 2 — สร้างโฟลเดอร์ปลายทาง

ทำซ้ำ 3 ชุด (อย่า hardcode คนละไดรฟ์กับ `%WorkingRoot%`)

**ชุด approved — If folder exists (คัดลอก path):**

```text
%WorkingRoot%\approved
```

Create folder: ชื่อโฟลเดอร์

```text
approved
```

Into:

```text
%WorkingRoot%
```

**ชุด rejected — If folder exists:**

```text
%WorkingRoot%\rejected
```

Create folder ชื่อ:

```text
rejected
```

Into:

```text
%WorkingRoot%
```

**ชุด review — If folder exists:**

```text
%WorkingRoot%\review
```

Create folder ชื่อ:

```text
review
```

Into:

```text
%WorkingRoot%
```

ขั้นตอนต่อหนึ่งชุด:

1. ลาก **If folder exists** → วาง path จาก code block ด้านบน
2. ในกิ่ง **Else** ลาก **Create folder** ตามชื่อ + Into จาก code block
3. ปิดด้วย **End**

### Step 3 — ดึงรายการไฟล์จาก inbox

1. ลาก **Get files in folder**
2. ตั้งค่า:
   - Folder: (คัดลอกด้านล่างวางในช่อง)

```text
%WorkingRoot%\inbox
```

   - File filter: (คัดลอกด้านล่างวางในช่อง — หรือ `*` ถ้าต้องการรวม csv ที่เกี่ยวข้อง)

```text
*.txt
```

   - Include subfolders: ปิด
3. **Variables produced:** `InboxFiles` ← **ไม่ใส่ `%`**  
   (เวลาอ้างอิงทีหลังใช้ `%InboxFiles%`)

### Step 4 — วนทีละไฟล์ + อ่าน Priority / Status

1. ลาก **For each**
2. ตั้งค่า:
   - Value to iterate: (คัดลอกด้านล่างวางในช่อง)

```text
%InboxFiles%
```

   - Store into: `CurrentFile` ← **ไม่ใส่ `%`**
3. **ภายใน For each** เลือกอย่างน้อยหนึ่งวิธีอ่านค่า:

**วิธีแนะนำ — parse จากชื่อไฟล์** (`REQ-{id}-{Priority}-{Status}.txt`)

1. ลาก **Get file path part** → ได้ชื่อไฟล์ (Name without extension หรือ File name)
2. **Variables produced** เช่น `FileNameOnly` ← **ไม่ใส่ `%`** (อ้างอิงด้วย `%FileNameOnly%`)
3. ใช้ **Split text** / **Parse text** / ดึงส่วนตาม `-` ให้ได้ตัวแปรชื่อตอนสร้าง (ไม่มี `%`):
   - `Priority` → อ้างอิง `%Priority%` (เช่น `High`, `Low`, `Medium`)
   - `Status` → อ้างอิง `%Status%` (เช่น `Ready`, `New`, `Invalid`)

**วิธีสำรอง — อ่านเนื้อหาไฟล์**

1. ลาก **Read text from file** → File path: (คัดลอกด้านล่างวางในช่อง)

```text
%CurrentFile%
```

2. **Variables produced:** `FileText` ← **ไม่ใส่ `%`**
3. ดึงบรรทัด `Priority:` และ `Status:` ไปใส่ตัวแปร `Priority` / `Status` (Trim ช่องว่าง; อ้างอิงด้วย `%Priority%` / `%Status%`)

> ก่อนเทียบเงื่อนไข ใช้ Trim / ตรวจตัวพิมพ์ให้ตรง `High`, `Ready`, … ตาม business rules

### Step 5 — If / Else if / Else แล้ว Move

ยังอยู่ **ภายใน For each** หลังได้ `%Priority%` และ `%Status%`:

1. ลาก **If**
2. เงื่อนไขแบบ AND:
   - ฝั่งซ้าย (คัดลอกด้านล่างวางในช่อง)

```text
%Priority%
```

     ตัวดำเนินการ **Equal to** · ฝั่งขวา (คัดลอกด้านล่างวางในช่อง)

```text
High
```

   - **และ** ฝั่งซ้าย (คัดลอกด้านล่างวางในช่อง)

```text
%Status%
```

     ตัวดำเนินการ **Equal to** · ฝั่งขวา (คัดลอกด้านล่างวางในช่อง)

```text
Ready
```

3. **ภายใน If** ลาก **Move file(s)**
   - File(s) to move: (คัดลอกด้านล่างวางในช่อง — ไม่ใช่ทั้งลิสต์)

```text
%CurrentFile%
```

   - Destination folder: (คัดลอกด้านล่างวางในช่อง)

```text
%WorkingRoot%\approved\
```

4. ลาก **Increase variable** → เลือกตัวแปร `ApprovedCount` (ไม่มี `%` ในรายการเลือก) แล้ว + `1`
5. ต่อท้าย log (Set variable / Append): เพิ่มแถว (คัดลอกด้านล่างเป็นสูตรตัวอย่าง)

```text
%FileNameOnly%,approved,%Priority%,%Status%
```

6. เพิ่ม **Else if** เงื่อนไขแบบ OR:
   - ฝั่งซ้าย (คัดลอกด้านล่างวางในช่อง)

```text
%Priority%
```

     **Equal to** ฝั่งขวา:

```text
Low
```

   - **หรือ** ฝั่งซ้าย (คัดลอกด้านล่างวางในช่อง)

```text
%Status%
```

     **Equal to** ฝั่งขวา:

```text
Invalid
```

   - **Move file(s)** File(s):

```text
%CurrentFile%
```

     Destination:

```text
%WorkingRoot%\rejected\
```

   - **Increase variable** `RejectedCount` + 1
   - Append log → folder `rejected`

7. เพิ่ม **Else**:
   - **Move file(s)** File(s):

```text
%CurrentFile%
```

     Destination:

```text
%WorkingRoot%\review\
```

   - **Increase variable** `ReviewCount` + 1
   - Append log → folder `review`

8. ปิดด้วย **End** (If) แล้ว **End** (For each)

โครงภายในลูป:

```text
For each CurrentFile in InboxFiles
  (อ่าน Priority / Status)
  If Priority = High AND Status = Ready
    Move → approved\
    Increase ApprovedCount
  Else if Priority = Low OR Status = Invalid
    Move → rejected\
    Increase RejectedCount
  Else
    Move → review\
    Increase ReviewCount
  End
  (append routing log row)
End
```

### Step 6 — เขียน routing-log.csv และสรุปจำนวน

1. **หลัง** End ของ For each ลาก **Write text to file**
2. ตั้งค่า:
   - File path: (คัดลอกด้านล่างวางในช่อง)

```text
C:\PAD-Labs\output\lab04\routing-log.csv
```

   - Text to write: (คัดลอกด้านล่างวางในช่อง — หรือข้อความ CSV ที่สะสมไว้)

```text
%RoutingLog%
```

   - If file exists: Overwrite
3. (แนะนำ) เขียนบรรทัดสรุปเพิ่ม หรือไฟล์สรุปสั้น ๆ เช่น (คัดลอกด้านล่าง):

```text
Approved=%ApprovedCount%; Rejected=%RejectedCount%; Review=%ReviewCount%
```

### Step 7 — รันและเทียบ expected

1. กด **Run**
2. เปิดโฟลเดอร์ `approved`, `rejected`, `review` เทียบตาราง Expected routing
3. เปิด `routing-log.csv` ตรวจชื่อไฟล์และปลายทาง
4. ก่อนสาธิตซ้ำ: คัดลอก `assets/inbox` ทับ working อีกครั้ง (เพราะไฟล์ถูก Move ไปแล้ว)

---

## จุดที่มักทำผิด

| ผิด | ถูก |
|-----|-----|
| พิมพ์ `%Name%` ในช่อง Name / Store into / **Variables produced** | ใช้ชื่อเปล่าไม่มี `%` เช่น `WorkingRoot`, `CurrentFile` |
| Hardcode ย้ายทีละไฟล์ 5 action แยก | ใช้ **For each** + เงื่อนไข |
| ใส่ `%InboxFiles%` ใน Move | ใส่ `%CurrentFile%` |
| สลับ AND/OR ของกฎ | High+Ready → approved; Low **หรือ** Invalid → rejected |
| ไม่ Trim / ตัวพิมพ์ไม่ตรง | Trim แล้วเทียบค่าตาม business-rules |
| ไม่สร้างโฟลเดอร์ปลายทาง | Step 2 มี If folder exists / Create folder |
| ไม่มี log | Step 6 เขียน `routing-log.csv` |

---

## Variables

| ชื่อตอนสร้าง (ไม่มี `%`) | ตอนอ้างอิง | Type |
|--------------------------|------------|------|
| `WorkingRoot` | `%WorkingRoot%` | Text |
| `InboxFiles` | `%InboxFiles%` | File list |
| `CurrentFile` | `%CurrentFile%` | File |
| `Priority` | `%Priority%` | Text |
| `Status` | `%Status%` | Text |
| `ApprovedCount` | `%ApprovedCount%` | Numeric |
| `RejectedCount` | `%RejectedCount%` | Numeric |
| `ReviewCount` | `%ReviewCount%` | Numeric |
| `RoutingLog` | `%RoutingLog%` | Text |

## Expected Result

ตรงกับ [`assets/expected-routing.csv`](assets/expected-routing.csv) (จำนวนและปลายทาง)

## Acceptance Criteria

- [ ] ใช้ If / Else If / Else อย่างชัดเจน
- [ ] ไม่ hardcode รายชื่อไฟล์ทีละไฟล์ในหลาย action แยก (ใช้ลูป)
- [ ] มี log ผลลัพธ์ (`routing-log.csv`)

## Troubleshooting

| อาการ | แก้ |
|-------|-----|
| เงื่อนไขไม่เข้าสาขา | ตรวจตัวพิมพ์เล็ก-ใหญ่; ใช้ Trim; ตรวจว่า parse ส่วน Priority/Status จากชื่อไฟล์ถูกตำแหน่ง |
| Move ล้มเหลว | สร้างโฟลเดอร์ปลายทางก่อน; ตรวจว่าไฟล์ยังอยู่ใน inbox |
| นับไม่ตรง expected | รีเซ็ต inbox จาก assets แล้วรันใหม่; อย่ารันซ้ำบนโฟลเดอร์ที่ย้ายไปแล้ว |

## Cleanup

- รีเซ็ต working จาก `assets/inbox` ก่อนสาธิตซ้ำ
- ลบ `C:\PAD-Labs\working\lab04` ได้หลังผ่านเกณฑ์ — คงต้นฉบับใน repo ไว้

> **Catch-up:** ตามไม่ทัน → วาง [`scripts/04-conditional-automation.robin`](scripts/04-conditional-automation.robin) ใน flow ว่าง (full)
