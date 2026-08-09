# Lab 02 — File Management (Hands-on)

**อ่านก่อน:** [LESSON.md](LESSON.md) · **หน้าปกบท:** [README.md](README.md) · **พื้นฐาน:** [`shared/PAD-FUNDAMENTALS.md`](../../shared/PAD-FUNDAMENTALS.md)

**วัน:** 1 · **ระดับ:** Beginner  
**ทักษะ:** Folder/File actions, Get files, Copy/Move, Get file path part, Read/Write text

## อ้างอิง (Aug 2026)

| แหล่ง | URL |
|-------|-----|
| Official tutorial (pattern เดียวกับ Lab นี้) | [Getting started — free org](https://learn.microsoft.com/power-automate/desktop-flows/getting-started-freeorg) |
| Folder actions | [actions-reference/folder](https://learn.microsoft.com/power-automate/desktop-flows/actions-reference/folder) |
| File actions | [actions-reference/file](https://learn.microsoft.com/power-automate/desktop-flows/actions-reference/file) |

## Setup บนเครื่อง (ทำก่อนเปิด designer)

1. สร้างโฟลเดอร์ working และ output (คัดลอกได้):

```text
C:\PAD-Labs\working\lab02\
```

```text
C:\PAD-Labs\output\lab02\
```

2. คัดลอกทั้งโฟลเดอร์ [`assets/inbox`](assets/inbox/) ไปยัง:

```text
C:\PAD-Labs\working\lab02\inbox
```

3. สร้างโฟลเดอร์ว่าง (ถ้ายังไม่มี):

```text
C:\PAD-Labs\working\lab02\archive
```

4. ตรวจว่าใน `inbox` มีไฟล์อย่างน้อย: `order-1001.csv`, `order-1002.csv`, `readme-note.txt`, `invoice-demo.txt`, `skip-me.tmp`

> ถ้าใช้ไดรฟ์อื่น (เช่น `D:\PAD-Labs\...`) ได้ — แต่ต้องใช้ path นั้นใน `%WorkingRoot%` ให้สม่ำเสมอทั้ง flow

## Input / Output

| | Path |
|--|------|
| Mock inbox | [`assets/inbox/`](assets/inbox/) |
| Expected mapping | [`assets/expected/expected-manifest.csv`](assets/expected/expected-manifest.csv) |
| Output summary | ดู code block ใน Step 6 |

| ไฟล์ใน inbox | การจัดการ |
|--------------|-----------|
| `order-1001.csv`, `order-1002.csv` | Copy → `archive\csv\` |
| `readme-note.txt`, `invoice-demo.txt` | Copy → `archive\txt\` |
| `skip-me.tmp` | Copy/Move → `archive\ignored\` (หรือข้าม แต่ต้องนับเป็น IGNORED) |

---

## Hands-on ทีละขั้น

### Step 0 — สร้าง flow

1. เปิด Power Automate for desktop → **New flow**
2. ชื่อ flow (คัดลอกได้):

```text
Lab02_FileManagement
```

3. กด **Create**

> **กฎตัวแปรใน PAD (อ่านก่อนทำ Step ถัดไป)**  
> - ช่อง **Name** ของ **Set variable**, ชื่อ **produced variable**, และ **Store into** = พิมพ์ชื่ออย่างเดียว **ไม่มี `%`** เช่น `WorkingRoot`  
> - ช่องอื่นที่ต้องดึงค่าตัวแปร (Folder, File path, Text, …) = ใช้ `%WorkingRoot%` (**มี `%` ครบสองด้าน**)  
> - หลังสร้างแล้ว Variables pane อาจแสดงเป็น `%WorkingRoot%` — เป็นเรื่องปกติ

### Step 1 — ตั้ง path และตัวนับ

1. ลาก **Set variable** ลง workspace
2. ตั้งค่า:
   - Name: `WorkingRoot` ← **ไม่ใส่ `%`**
   - Value: (คัดลอกด้านล่างวางในช่อง Value — หรือ path ที่คุณใช้จริง)

```text
C:\PAD-Labs\working\lab02
```

3. เพิ่ม **Set variable** อีก 3 ตัว (Name ไม่มี `%`):
   - Name: `CsvCount` ← Value:

```text
0
```

   - Name: `TxtCount` ← Value:

```text
0
```

   - Name: `IgnoredCount` ← Value:

```text
0
```

> Tip (2606+): ถ้า Variables pane รองรับ **Default value** ตั้งค่าเริ่มต้นที่นั่นได้ — แต่ใน Lab นี้ใช้ Set variable ก็ผ่านเกณฑ์

### Step 2 — สร้างโฟลเดอร์ปลายทาง (csv / txt / ignored)

ทำซ้ำ 3 ชุด (csv / txt / ignored) — อย่า hardcode คนละไดรฟ์กับ `%WorkingRoot%`

> **ตั้งค่า If folder:** เลือก **Doesn't exist** (ไม่ใช้ค่าเริ่มต้น Exists)  
> แปลว่า “ถ้าโฟลเดอร์**ยังไม่มี** → ทำในกิ่ง Then” — วาง **Create folder** ใน Then ได้เลย **ไม่ต้องใช้ Else**

ขั้นตอนต่อหนึ่งชุด:

1. ลาก **If folder exists**  
2. ตั้ง **If folder** = **Doesn't exist**  
3. ช่อง Folder path วาง path จากตารางด้านล่าง  
4. **ในกิ่ง Then** ลาก **Create folder** → ชื่อโฟลเดอร์ + Into จากตาราง  
5. ปิดด้วย **End** (ไม่ต้องเพิ่ม Else)

| ชุด | Folder path | ชื่อโฟลเดอร์ (`Create folder` ใน **Then**) | Into |
|-----|-------------|---------------------------------------------|------|
| csv | `%WorkingRoot%\archive\csv` | `csv` | `%WorkingRoot%\archive` |
| txt | `%WorkingRoot%\archive\txt` | `txt` | `%WorkingRoot%\archive` |
| ignored | `%WorkingRoot%\archive\ignored` | `ignored` | `%WorkingRoot%\archive` |

คัดลอกทีละช่อง:

**csv — Folder path**

```text
%WorkingRoot%\archive\csv
```

**csv — ชื่อโฟลเดอร์ (Then → Create folder)**

```text
csv
```

**csv — Into (Then → Create folder)**

```text
%WorkingRoot%\archive
```

**txt — Folder path**

```text
%WorkingRoot%\archive\txt
```

**txt — ชื่อโฟลเดอร์ (Then)**

```text
txt
```

**txt — Into (Then)**

```text
%WorkingRoot%\archive
```

**ignored — Folder path**

```text
%WorkingRoot%\archive\ignored
```

**ignored — ชื่อโฟลเดอร์ (Then)**

```text
ignored
```

**ignored — Into (Then)**

```text
%WorkingRoot%\archive
```

โครงที่ได้ควรคล้าย:

```text
If folder doesn't exist %WorkingRoot%\archive\csv
  Create folder csv into %WorkingRoot%\archive
End
(… txt …)
(… ignored …)
```

### Step 3 — ดึงรายการไฟล์จาก inbox

1. ลาก **Get files in folder**
2. ตั้งค่า:
   - Folder: (คัดลอก — **ใช้** ตัวแปร มี `%` และต่อ `\inbox`)

```text
%WorkingRoot%\inbox
```

   - File filter:

```text
*
```

   - Include subfolders: ปิด
3. ชื่อ produced variable: `InboxFiles` ← **ไม่ใส่ `%`**  
   (เวลาอ้างอิงทีหลังใช้ `%InboxFiles%`)

อ้างอิงทางการ: action นี้คืน **List of files** แล้วนำไปวนด้วย **For each** — ตาม [Getting started](https://learn.microsoft.com/power-automate/desktop-flows/getting-started-freeorg)

### Step 4 — วนทีละไฟล์ + อ่านนามสกุล

1. ลาก **For each**
2. ตั้งค่า:
   - Value to iterate: (คัดลอก)

```text
%InboxFiles%
```

   - Store into: `CurrentFile` ← **ไม่ใส่ `%`**  
     (ชื่ออื่นเช่น `CurrentItem` ก็ได้ แต่ต้องใช้ชื่อเดียวกันทั้งลูป)
3. **ภายใน For each** ลาก **Get file path part**
4. ตั้งค่า:
   - File path: (คัดลอก — ไฟล์ปัจจุบัน ไม่ใช่ทั้งลิสต์)

```text
%CurrentFile%
```

   - ส่วนที่ต้องการ: Extension (หรือเลือกให้ได้ extension)
5. ชื่อ produced: `FileExtension` ← **ไม่ใส่ `%`**  
   (อ้างอิงด้วย `%FileExtension%`)

### Step 5 — แยกตามนามสกุลแล้ว Copy ทีละไฟล์

ยังอยู่ **ภายใน For each** หลัง Get file path part:

1. ลาก **If**
2. เงื่อนไข: ฝั่งซ้าย (คัดลอก)

```text
%FileExtension%
```

   ตัวดำเนินการ **Equal to** · ฝั่งขวา (คัดลอก — ถ้าค่าใน Variables ไม่มีจุด ให้ใช้ `csv` แทน):

```text
.csv
```

3. **ภายใน If** ลาก **Copy file(s)**
4. ตั้งค่าให้ถูก:
   - File(s) to copy: (คัดลอก — **ห้าม** ใส่ `%InboxFiles%`)

```text
%CurrentFile%
```

   - Destination folder:

```text
%WorkingRoot%\archive\csv\
```

   - If file exists: Overwrite (หรือตามนโยบายที่ชัด)
5. ชื่อ produced list (ถ้ามี): `CopiedFiles` ← ไม่ใส่ `%` — ไม่บังคับใช้ต่อ
6. ลาก **Increase variable** → เลือกตัวแปร `CsvCount` (ไม่มี `%` ในรายการเลือก) แล้ว + `1`

7. เพิ่ม **Else if**: ฝั่งขวา

```text
.txt
```

   - **Copy file(s)**  
     File(s):

```text
%CurrentFile%
```

     Destination:

```text
%WorkingRoot%\archive\txt\
```

   - **Increase variable** `TxtCount` + 1

8. เพิ่ม **Else**:
   - **Copy file(s)** (หรือ **Move file(s)**)  
     File(s):

```text
%CurrentFile%
```

     Destination:

```text
%WorkingRoot%\archive\ignored\
```

   - **Increase variable** `IgnoredCount` + 1

9. ปิดด้วย **End** (If) แล้ว **End** (For each)

โครงภายในลูป:

```text
For each CurrentFile in InboxFiles
  Get file path part → FileExtension
  If FileExtension = '.csv'
    Copy CurrentFile → archive\csv\
    Increase CsvCount
  Else if FileExtension = '.txt'
    Copy CurrentFile → archive\txt\
    Increase TxtCount
  Else
    Copy CurrentFile → archive\ignored\
    Increase IgnoredCount
  End
End
```

### Step 6 — เขียน summary.txt

1. **หลัง** End ของ For each ลาก **Set variable**
2. Name: `SummaryText` ← **ไม่ใส่ `%`**
3. Value: (คัดลอกทั้งบรรทัด — `%CsvCount%` คือการ **ใช้** ค่าตัวแปร มี `%` ถูกต้องแล้ว)

```text
CSV=%CsvCount%; TXT=%TxtCount%; IGNORED=%IgnoredCount%; Done
```

4. ลาก **Write text to file**
5. ตั้งค่า:
   - File path: (คัดลอก)

```text
C:\PAD-Labs\output\lab02\summary.txt
```

   - Text to write: (คัดลอก)

```text
%SummaryText%
```

   - If file exists: Overwrite
6. (ทางเลือก) สร้างโฟลเดอร์ `output\lab02` ด้วย **If folder exists** (**Doesn't exist**) + **Create folder** ใน Then ก่อนเขียนไฟล์

### Step 7 — รันและตรวจ

1. กด **Run**
2. เปิดโฟลเดอร์ `archive\csv`, `archive\txt`, `archive\ignored` เทียบตารางด้านบน
3. เปิด `summary.txt` ต้องได้แนว:

```text
CSV=2; TXT=2; IGNORED=1; Done
```

4. รันซ้ำรอบสอง — ต้องไม่พัง (มี overwrite / If exists ชัด)

### Challenge (ทางเลือก)

หลัง Copy สำเร็จ ใช้ **Delete file** ลบไฟล์ต้นทางใน `inbox` — ทำเฉพาะ working copy ห้ามลบใน repo `assets/`

---

## จุดที่มักทำผิด

| ผิด | ถูก |
|-----|-----|
| พิมพ์ `%WorkingRoot%` ในช่อง **Name** ของ Set variable | Name = `WorkingRoot` (ไม่มี `%`) |
| **Copy file(s)** ใส่ `%InboxFiles%` ในลูป | ใส่ `%CurrentFile%` (ใช้ตัวแปรไฟล์ปัจจุบัน) |
| **Get files in folder** จาก `%WorkingRoot%` | จาก `%WorkingRoot%\inbox` |
| Hardcode `D:\...` ปนกับ `%WorkingRoot%` คนละราก | ใช้ `%WorkingRoot%` ทั้ง flow ตอนอ้างอิง path |
| ลืมตั้ง **Doesn't exist** แล้ววาง Create ใน Then | ตั้ง **If folder** = **Doesn't exist** แล้ว Create ใน Then |
| มีแค่สาขา `.csv` | ต้องมี `.txt` และ Else (ignored) |
| ไม่เขียน `summary.txt` | Step 6 บังคับตามเกณฑ์ผ่าน |

---

## Variables

| ชื่อตอนสร้าง (ไม่มี `%`) | ตอนอ้างอิง | Type |
|--------------------------|------------|------|
| `WorkingRoot` | `%WorkingRoot%` | Text |
| `InboxFiles` | `%InboxFiles%` | File list |
| `CurrentFile` | `%CurrentFile%` | File |
| `FileExtension` | `%FileExtension%` | Text |
| `CsvCount` / `TxtCount` / `IgnoredCount` | `%CsvCount%` ฯลฯ | Numeric |
| `SummaryText` | `%SummaryText%` | Text |

## Expected Result

- `archive\csv\` มี CSV สองไฟล์, `archive\txt\` มี TXT สองไฟล์
- `skip-me.tmp` ไม่อยู่ใน csv/txt
- `summary.txt` ตัวเลขตรง expected manifest

## Acceptance Criteria

- [ ] สร้างโฟลเดอร์ด้วย Flow (ไม่สร้างมือทั้งหมด)
- [ ] คัดลอกตามนามสกุลถูกต้อง และ Copy เป็นทีละไฟล์ใน For each
- [ ] มีไฟล์สรุปผล
- [ ] รันซ้ำได้โดยไม่พัง (If exists / overwrite ชัด)

## Troubleshooting

| อาการ | แก้ |
|-------|-----|
| File in use | ปิดโปรแกรมที่เปิดไฟล์อยู่ |
| Path not found | ตรวจ `%WorkingRoot%` และ Create folder ก่อน; ตรวจว่ามีโฟลเดอร์ `inbox` |
| นับไฟล์ไม่ตรง | กรองเฉพาะไฟล์ ไม่รวม subfolder; ตรวจ extension มีจุดหรือไม่ |
| Copy ทั้งชุดซ้ำ | ตรวจว่าไม่ได้ใส่ `%InboxFiles%` ใน Copy |

## Cleanup

- ลบ `C:\PAD-Labs\working\lab02` ได้หลังผ่านเกณฑ์
- คงต้นฉบับใน repo `assets/` ไว้เสมอ
