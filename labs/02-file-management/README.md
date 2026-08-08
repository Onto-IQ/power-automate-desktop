# Lab 02 — File Management

**วัน:** 1 · **ระดับ:** Beginner  
**ทักษะ:** Folder/File actions, Get files, Copy/Move/Rename, Read/Write text

## วัตถุประสงค์

- สร้างโครงสร้างโฟลเดอร์ด้วย PAD
- คัดลอก/ย้ายไฟล์ตามนามสกุล
- อ่านและเขียน text file สรุปผล

## Prerequisites

- PAD ติดตั้งแล้ว
- ไม่จำเป็นต้องใช้ Web UI

## Setup

1. สร้าง Flow `Lab02_FileManagement`
2. คัดลอกทั้งโฟลเดอร์ `assets/inbox` ไปยัง  
   `C:\PAD-Labs\working\lab02\inbox`
3. สร้างโฟลเดอร์ว่าง:
   - `C:\PAD-Labs\working\lab02\archive`
   - `C:\PAD-Labs\output\lab02`

## Input / Output

| | Path |
|--|------|
| Mock inbox | [`assets/inbox/`](assets/inbox/) |
| Expected mapping | [`assets/expected/expected-manifest.csv`](assets/expected/expected-manifest.csv) |
| Output summary | `C:\PAD-Labs\output\lab02\summary.txt` |

### ไฟล์ใน inbox (mock)

| ไฟล์ | ประเภท | การจัดการที่ต้องการ |
|------|--------|---------------------|
| `order-1001.csv` | CSV | คัดลอกไป `archive\csv\` |
| `order-1002.csv` | CSV | คัดลอกไป `archive\csv\` |
| `readme-note.txt` | TXT | คัดลอกไป `archive\txt\` |
| `invoice-demo.txt` | TXT | คัดลอกไป `archive\txt\` |
| `skip-me.tmp` | TMP | **ไม่** ต้องคัดลอก (หรือย้ายไป `archive\ignored\`) |

## PAD Action Sequence (แนะนำ)

1. ตั้ง `%WorkingRoot%` = `C:\PAD-Labs\working\lab02`
2. **If folder not exists** → **Create folder** สำหรับ `archive\csv`, `archive\txt`, `archive\ignored`
3. **Get files in folder** จาก `%WorkingRoot%\inbox` → `%InboxFiles%`
4. **For each** `%CurrentFile%` in `%InboxFiles%`
   - **Get file path part** / extension
   - **If** extension = `.csv` → **Copy file** ไป `archive\csv\`
   - **Else if** extension = `.txt` → **Copy file** ไป `archive\txt\`
   - **Else** → Copy/Move ไป `archive\ignored\` หรือข้าม
5. นับจำนวนไฟล์แต่ละประเภทเก็บในตัวแปร
6. **Write text to file** สร้าง `summary.txt` เช่น  
   `CSV=2; TXT=2; IGNORED=1; Done`
7. (Challenge) **Delete** สำเนาใน inbox หลังคัดลอกสำเร็จ — ทำเฉพาะใน working copy

## Variables

| Variable | Type |
|----------|------|
| `%WorkingRoot%` | Text |
| `%InboxFiles%` | File list |
| `%CurrentFile%` | File |
| `%CsvCount%` / `%TxtCount%` / `%IgnoredCount%` | Numeric |
| `%SummaryText%` | Text |

## Expected Result

- มีโฟลเดอร์ `archive\csv` และ `archive\txt` พร้อมไฟล์ครบ
- `skip-me.tmp` ไม่อยู่ใน csv/txt
- มี `summary.txt` ที่ตัวเลขตรงกับ expected manifest

## Acceptance Criteria

- [ ] สร้างโฟลเดอร์ด้วย Flow (ไม่สร้างมือทั้งหมด)
- [ ] คัดลอกตามนามสกุลถูกต้อง
- [ ] มีไฟล์สรุปผล
- [ ] รันซ้ำได้โดยไม่พัง (ใช้ If exists / overwrite policy ให้ชัด)

## Troubleshooting

| อาการ | แก้ |
|-------|-----|
| File in use | ปิดโปรแกรมที่เปิดไฟล์อยู่ |
| Path not found | ตรวจ `%WorkingRoot%` และ Create folder ก่อน |
| นับไฟล์ไม่ตรง | กรองเฉพาะไฟล์ ไม่รวม subfolder |

## Cleanup

- ลบ `C:\PAD-Labs\working\lab02` ได้หลังผ่านเกณฑ์
- คงต้นฉบับใน repo `assets/` ไว้เสมอ
