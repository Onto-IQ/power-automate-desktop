# TA Cheat Sheet — อาการที่เจอบ่อยและวิธีแก้เร็ว

ใช้ในห้อง: วิทยากร 1 + TA 2 · คนเรียน ~30  
เป้า: แก้ให้จบใน **1–3 นาที** ต่อเคส — ถ้าเกินให้ยกให้วิทยากร

ตารางสอน: [`CLASSROOM-SCHEDULE-12H.md`](CLASSROOM-SCHEDULE-12H.md) · ติดตั้ง: [`PRECLASS-SETUP.md`](PRECLASS-SETUP.md) · กฎ `%`: [`PAD-FUNDAMENTALS.md`](PAD-FUNDAMENTALS.md)

## กติกา TA ในห้อง

1. คนติด **เกิน 3 นาที** แล้วยังไม่ขยับ → เข้าไปช่วย (อย่ารอให้ยกมือนาน)  
2. ช่วย **Core** ก่อน Challenge  
3. อย่าแก้เครื่องทั้งห้องด้วยการ demo ซ้ำยาว — ส่งต่อวิทยากรถ้าเป็นบั๊กกลาง  
4. ห้ามแนะนำให้ส่ง Outlook จริง — **DraftOnly**

## Top 15 — อาการ → ตรวจ → แก้

### 1) พิมพ์ `%WorkingRoot%` ในช่อง Name

| | |
|--|--|
| **อาการ** | Error / ตัวแปรแปลก / สร้างไม่สำเร็จ |
| **ตรวจ** | ช่อง Name ของ Set variable |
| **แก้** | ลบ `%` ทั้งสองด้าน → เหลือ `WorkingRoot` แล้ว Save |

### 2) Copy ทั้งลิสต์ใน For each

| | |
|--|--|
| **อาการ** | ไฟล์ซ้ำเต็มโฟลเดอร์ / ช้าผิดปกติ |
| **ตรวจ** | Copy file(s) → File(s) to copy |
| **แก้** | เปลี่ยนเป็น `%CurrentFile%` (หรือชื่อ Store into ของลูป) **ห้าม** `%InboxFiles%` |

### 3) Get files ชี้ผิดโฟลเดอร์

| | |
|--|--|
| **อาการ** | ลิสต์ว่าง / ไม่เจอ csv |
| **ตรวจ** | Folder ของ Get files in folder |
| **แก้** | Lab 02 ต้องเป็น `%WorkingRoot%\inbox` ไม่ใช่แค่ `%WorkingRoot%` |

### 4) Path not found / โฟลเดอร์ไม่มี

| | |
|--|--|
| **อาการ** | Action ไฟล์/โฟลเดอร์พังตั้งแต่ต้น |
| **ตรวจ** | มี `C:\PAD-Labs\working\...` จริงไหม |
| **แก้** | รันสคริปต์ใน [`PRECLASS-SETUP.md`](PRECLASS-SETUP.md) แล้วสร้างโฟลเดอร์ด้วย If folder exists / Create folder ใน flow |

### 5) Extension มี/ไม่มีจุดไม่ตรง If

| | |
|--|--|
| **อาการ** | ไฟล์ไม่เข้าสาขา csv/txt |
| **ตรวจ** | Run next action → ดู `%FileExtension%` |
| **แก้** | เทียบ Equal to ให้ตรงค่าจริง (`.csv` หรือ `csv`) |

### 6) Browser extension / Launch ไม่ขึ้น

| | |
|--|--|
| **อาการ** | Launch Edge/Chrome พัง หรือหา element ไม่เจอ |
| **ตรวจ** | ติดตั้ง extension ของ PAD แล้วหรือยัง · เปิดหน้า Lab Hub ด้วยมือได้ไหม |
| **แก้** | ติดตั้ง extension → ปิดเปิดเบราว์เซอร์ → Launch ใหม่ · URL ใช้จาก code block ใน `LAB.md` |

### 7) Selector ไม่เจอ (Web)

| | |
|--|--|
| **อาการ** | Populate / Click หา element ไม่เจอ |
| **ตรวจ** | UI element ใช้ text บนจอหรือ index ยาวไหม |
| **แก้** | Recapture · ล็อก `#id` หรือ `[data-pad="..."]` · มี **Wait for web page content** ก่อน Interact |

### 8) AJAX / ตารางว่าง

| | |
|--|--|
| **อาการ** | Extract ได้ 0 แถวบนหน้า ajax |
| **ตรวจ** | มี Wait ก่อน Extract หรือยัง |
| **แก้** | **Wait for web page content** จนแถวแรกพร้อม แล้วค่อย Extract |

### 9) Excel locked / file in use

| | |
|--|--|
| **อาการ** | Read/Write/Save Excel พัง |
| **ตรวจ** | มีหน้าต่าง Excel เปิดไฟล์ค้างไหม · flow มี Close Excel ไหม |
| **แก้** | ปิด Excel ด้วยมือ → ใส่ **Close Excel** ท้าย flow → อย่าเปิดไฟล์ output ค้างตอนรัน |

### 10) Save as รอบสองพัง (ไฟล์ซ้ำ)

| | |
|--|--|
| **อาการ** | รัน Lab Excel ครั้งที่ 2 แล้ว Failed to save |
| **ตรวจ** | path output ชื่อคงที่ซ้ำ |
| **แก้** | **If file exists** → **Delete file** ก่อน Save as หรือเปิดไฟล์เดิมแล้ว Save — ดู [`BEST-PRACTICES.md`](BEST-PRACTICES.md) |

### 11) Contoso เปิดไม่ได้ / กรอกไม่ได้

| | |
|--|--|
| **อาการ** | Run application พัง หรือ Populate ในหน้าต่างไม่ได้ |
| **ตรวจ** | path .exe · หน้าต่างถูกบัง · elevation คนละระดับกับ PAD |
| **แก้** | เปิด Contoso ด้วยมือจาก Start → Task Manager → Open file location ใส่ `%ContosoPath%` · **Focus window** ก่อนกรอก · รัน PAD กับแอปที่สิทธิ์เท่ากัน ([UIPI](https://learn.microsoft.com/troubleshoot/power-platform/power-automate/desktop-flows/ui-automation/uipi-issues)) |

### 12) Login Lab Hub ไม่ผ่าน

| | |
|--|--|
| **อาการ** | ไป Forms แล้ว session ไม่พร้อม |
| **ตรวจ** | ทำหน้า 06 Login ก่อนหรือยัง |
| **แก้** | Username / Password จาก code block: `demo` / `demo` · Wait หลัง login ก่อนไปหน้าถัดไป |

### 13) Outlook ไม่เจอ / ส่งไม่ได้

| | |
|--|--|
| **อาการ** | Action Outlook error |
| **ตรวจ** | Outlook Desktop เปิดโปรไฟล์ได้ไหม |
| **แก้** | เปิด Outlook ก่อน · สร้างเป็น **Draft** เท่านั้น · ใช้ผู้รับจาก `recipients.csv` |

### 14) Lab Hub เปิดไม่ได้ / เน็ต

| | |
|--|--|
| **อาการ** | หน้า ontoiq.tech/pad โหลดไม่ได้ |
| **ตรวจ** | เน็ต / proxy / DNS |
| **แก้** | ลองมือบน Edge · เปลี่ยนเครือข่าย · แจ้งวิทยากรถ้าทั้งห้องพัง (ปัญหาเซิร์ฟเวอร์) |

### 15) คนล้ำ Challenge จนช้า

| | |
|--|--|
| **อาการ** | ยังไม่ผ่าน Core แต่ทำ Mission พิเศษ |
| **ตรวจ** | สิ่งที่ค้างใน Acceptance Core |
| **แก้** | หยุด Challenge → กลับ Core ตาม [`CLASSROOM-SCHEDULE-12H.md`](CLASSROOM-SCHEDULE-12H.md) |

---

## เช็กลิสต์เร็วต่อ Lab (Core)

| Lab | ผ่านห้องเมื่อ |
|-----|----------------|
| 01 | กรอกจากตัวแปร + Submit + Close browser · รันซ้ำได้ |
| 01b | Notepad พิมพ์+บันทึกหรือ populate ได้ · ปิดหน้าต่าง |
| 02 | มีไฟล์ใน csv/txt/ignored ตามนามสกุล + `summary.txt` |
| 03 | Extract ตาราง static + AJAX มี Wait · มี output อย่างน้อยบางส่วน |
| 04 | ไฟล์ไป approved/rejected/review ถูกกฎ |
| 05 | Summary ยอดรวมตรงแนว expected |
| 06 | มี Filtered/Summary ใน Excel · Close Excel |
| 07 | อ่าน Excel → สร้างอย่างน้อยบางแถวใน Contoso → มี results |
| 08 | Login demo/demo → submit อย่างน้อย 1 lead → เขียนกลับ Excel |
| 09 | On block error + log อย่างน้อย Case A · ปิด browser |
| 10 ย่อ | มีไฟล์รายงาน + Outlook Draft (ไม่ส่งจริง) |

## สิ่งที่ TA ไม่ต้องทำ

- ไม่ต้องเขียน flow ให้ผู้เรียนทั้งก้อน (ชี้ `LAB.md` + code block ให้ copy)  
- ไม่ต้องอนุญาตส่งอีเมลจริง  
- ไม่ต้องเปลี่ยนเกณฑ์ Core กลางคอร์สโดยไม่ผ่านวิทยากร  

## ลิงก์ด่วน

| เรื่อง | ที่ |
|--------|-----|
| กฎ `%` | [`PAD-FUNDAMENTALS.md`](PAD-FUNDAMENTALS.md) |
| Selector Lab Hub | [`SELECTOR-CONVENTIONS.md`](SELECTOR-CONVENTIONS.md) |
| Excel รันซ้ำ | [`BEST-PRACTICES.md`](BEST-PRACTICES.md) |
| Handle errors (official) | https://learn.microsoft.com/power-automate/desktop-flows/errors |
