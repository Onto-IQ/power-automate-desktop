# พื้นฐาน Power Automate for desktop (สำหรับผู้เริ่มต้น)

อ่านเอกสารนี้ **ก่อนทำ Lab แรก** หรือเมื่อสับสนเรื่องตัวแปร / การรัน / หน้าจอ designer  
ชื่อผลิตภัณฑ์ทางการคือ **Power Automate for desktop** (ย่อ **PAD**) — สร้างสิ่งที่เรียกว่า **desktop flow**

อ้างอิงเวอร์ชัน PAD: [https://learn.microsoft.com/power-platform/released-versions/power-automate-desktop](https://learn.microsoft.com/power-platform/released-versions/power-automate-desktop) · ชื่อ Action: [`OFFICIAL-TERMINOLOGY.md`](OFFICIAL-TERMINOLOGY.md)

## RPA คืออะไร (ภาษาคน)

**RPA (Robotic Process Automation)** คือการให้โปรแกรมทำงานซ้ำแทนคน เช่น คัดลอกไฟล์ กรอกฟอร์ม อ่าน Excel แล้วส่งอีเมล  
PAD คือเครื่องมือของ Microsoft ที่ให้คุณ **ลาก action** มาเรียงเป็นขั้นตอน แล้วกด Run ให้เครื่องทำตาม

| คำ | ความหมายสั้น |
|----|---------------|
| **desktop flow** | ชุดขั้นตอนที่รันบนเครื่อง Windows ของคุณ |
| **cloud flow** | Flow บนเว็บ Power Automate (คนละชนิด — คอร์สนี้โฟกัส desktop) |
| **Action** | หนึ่งคำสั่งใน flow เช่น Copy file, Launch Excel |
| **Variable** | “กล่องเก็บค่า” ที่ใช้ส่งต่อระหว่าง action |

## หน้าจอหลักที่ต้องรู้จัก

### Console

หน้าต่างแรกหลังเปิด PAD — ใช้สร้าง flow ใหม่ เปิด flow เดิม รัน flow

1. กด **New flow**
2. ตั้งชื่อตาม convention เช่น `Lab02_FileManagement`
3. กด **Create** → เปิด **Flow designer**

### Flow designer

พื้นที่ออกแบบขั้นตอน

| ส่วน | อยู่ทางไหน (โดยทั่วไป) | ใช้ทำอะไร |
|------|------------------------|-----------|
| **Actions pane** | ซ้าย | ค้นหาและลาก action ลง workspace |
| **Workspace** | กลาง | เรียงลำดับขั้นตอนของ flow |
| **Variables pane** | ขวา | ดูค่าตัวแปรหลังรัน / ตอน debug |
| **UI elements** | แท็บ/แผงแยก | เก็บ selector ของปุ่ม ช่องกรอก บนเว็บหรือแอป |

## ชนิดข้อมูลที่ใช้บ่อยใน Lab

| ชนิด | ตัวอย่างในชีวิตจริง | เห็นใน Lab |
|------|---------------------|------------|
| Text | ข้อความ path, ชื่อไฟล์ | `%WorkingRoot%` |
| Numeric | จำนวนนับ | `%CsvCount%` |
| Boolean | จริง/เท็จ | เงื่อนไข If |
| List / File list | รายการไฟล์หลายไฟล์ | `%InboxFiles%` |
| Data table | ตารางเหมือน Excel ในหน่วยความจำ | `%Orders%`, `%Leads%` |
| Browser / Excel instance | “ที่จับ” ของเบราว์เซอร์หรือ Excel ที่เปิดอยู่ | `%Browser%`, `%Excel%` |
| Error | รายละเอียด error ล่าสุด | `%LastError%` จาก **Get last error** |

## กฎตัวแปร `%` (สำคัญที่สุดสำหรับมือใหม่)

ใน PAD:

- **ตอนสร้าง/ตั้งชื่อ** ตัวแปร → **ไม่ใส่ `%`**
- **ตอนใช้ค่า** ในช่องอื่น → **ใส่ `%ชื่อ%`**

| สถานการณ์ | ใส่ในช่อง | ตัวอย่าง |
|-----------|-----------|----------|
| **Set variable** → Name | ไม่มี `%` | `WorkingRoot` |
| **For each** → Store into | ไม่มี `%` | `CurrentFile` |
| เปลี่ยนชื่อในส่วน **Variables produced** | ไม่มี `%` | `InboxFiles` |
| Folder / File path / Text ที่ต้องการดึงค่า | มี `%` | `%WorkingRoot%\inbox` |
| คอลัมน์ของแถวใน **For each** (Data table) | มี `%` + ชื่อคอลัมน์ใน `['...']` | `%CurrentRow['Amount']%` |

หลังสร้างแล้ว Variables pane มักแสดงเป็น `%WorkingRoot%` — เป็นเรื่องปกติ

### อ้างคอลัมน์ในแถว Data table (สำคัญ)

ตอน **For each** ตาราง แล้วต้องการค่าในคอลัมน์ไปใส่ **If** / **Set variable** / **Populate**:

- ในรายการตัวแปรมักเห็นแค่ `%CurrentRow%` (ทั้งแถว) — **ไม่มีรายการย่อยเป็นคอลัมน์**
- ต้อง**พิมพ์/วางเอง**ในช่อง เช่น:

```text
%CurrentRow['Amount']%
```

- ชื่อใน `['...']` ต้อง**ตรง header** (เช่น `Order ID` มีช่องว่างได้: `%AjaxRow['Order ID']%`)
- รูปแบบที่ผิดบ่อย: `%CurrentRow%['Amount']` (วงเล็บอยู่นอก `%`)
- ใน **list / New value(s)** ใช้ `%...%` คู่เดียว — **ห้ามซ้อน** เช่น ถูก: `%[CurrentRow['Amount'], Tier]%` · ผิด: `%[%CurrentRow['Amount']%, %Tier%]%`

## การรันและดีบัก

| ปุ่ม / วิธี | ใช้เมื่อ |
|-------------|----------|
| **Run** | รันทั้ง flow จากต้นจนจบ |
| **Run next action** | เดินทีละ action เพื่อดูค่าตัวแปร |
| **Breakpoint** | หยุดที่บรรทัดที่เลือก แล้วค่อยดู Variables pane |
| **Stop** | หยุดการรันทันที |

เมื่อพัง: ดูข้อความ error → ใช้ **Get last error** ใน Lab ที่เกี่ยวกับ error handling → อ่าน `%LastError.Message%`

## การตั้งชื่อที่แนะนำ

| ประเภท | รูปแบบ | ตัวอย่าง |
|--------|--------|----------|
| Flow | `LabXX_ShortName` | `Lab02_FileManagement` |
| Subflow | `SF_<VerbNoun>` | `SF_WriteExcelReport` |
| Variable (ชื่อตอนสร้าง) | PascalCase | `WorkingRoot`, `InboxFiles` |
| UI Element | บทบาทชัด | `Btn_Submit`, `Txt_Name` |

ดูเพิ่ม: [`BEST-PRACTICES.md`](BEST-PRACTICES.md)

## โฟลเดอร์ทำงานบนเครื่อง (มาตรฐานคอร์ส)

```text
C:\PAD-Labs\
  ├── working\     ← สำเนา assets ที่แก้/รันได้
  ├── output\      ← ผลลัพธ์จาก flow
  └── logs\        ← log / screenshot
```

**ห้ามแก้ไฟล์ต้นฉบับในโฟลเดอร์ `assets/` ของ repo** — ให้คัดลอกไป `working` ก่อนเสมอ

## Wait ที่ถูกต้อง

อย่ารอด้วยการหน่วงวินาทีอย่างเดียวเป็นหลัก  
ใช้ **Wait for web page content** (เว็บ) หรือ **Wait for window content** (แอป Desktop) จน element พร้อมก่อน Click / Populate

## Error handling (ภาพรวม — ลงลึกใน Lab 09)

| กลไก | ความหมาย |
|------|----------|
| **On error** (ใน action) | เมื่อ action นี้พัง: Retry / Continue / ตั้งค่า |
| **On block error** | ครอบหลาย action ด้วยนโยบายเดียวกัน |
| **Get last error** | ดึงรายละเอียด error ล่าสุดไป log |

ไม่มี Action ชื่อ “Try-Catch” ใน designer — ใช้สองกลไกด้านบนแทน

## ลำดับการเรียนต่อหนึ่งบท

1. อ่าน [`PAD-FUNDAMENTALS.md`](PAD-FUNDAMENTALS.md) (ไฟล์นี้) ถ้ายังไม่คุ้น designer  
2. เปิด `modules/<บท>/README.md` → อ่าน **LESSON.md**  
3. ทำ **LAB.md** ทีละขั้น  
4. เทียบ Expected / Acceptance ใน LAB

## อ่านต่อเมื่อพร้อม

| หัวข้อ | ไฟล์ |
|--------|------|
| ตารางสอน 12 ชม. | [`CLASSROOM-SCHEDULE-12H.md`](CLASSROOM-SCHEDULE-12H.md) |
| ติดตั้งก่อนเรียน | [`PRECLASS-SETUP.md`](PRECLASS-SETUP.md) |
| Selector บน Lab Hub | [`SELECTOR-CONVENTIONS.md`](SELECTOR-CONVENTIONS.md) |
| Coding guidelines (official) | https://learn.microsoft.com/power-automate/guidance/desktop-flow-coding-guidelines/ |
