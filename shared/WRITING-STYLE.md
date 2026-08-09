# คู่มือสไตล์ภาษา — สำหรับผู้เขียนหลักสูตร (ภายใน)

**กลุ่มเป้าหมาย:** ทีมพัฒนาเอกสาร / วิทยากรที่แก้ Module  
**ไม่ใช่เอกสารผู้เรียน** — ไม่ต้องแจกลิงก์นี้ในห้องเรียนหรือสไลด์ผู้เรียน

ใช้เมื่อเขียนหรือแก้ `modules/*/README.md`, `LESSON.md`, `LAB.md` และเอกสารใน `shared/` ที่ผู้เรียนอ่านได้

## หลักการสำหรับเอกสารที่ผู้เรียนเห็น

1. **ภาษาไทยเป็นประโยคอ่านลื่น** — ไม่ห้วนแบบคำสั่งสั้น ๆ จนขาดบริบท  
2. **ไม่แปล keyphrase / ชื่อ Action ทางการ** — คงคำอังกฤษตาม Microsoft Learn เช่น `Wait for web page content`, `On block error`, `UI Elements`, `desktop flow`  
3. คำอธิบายภาษาไทยวางต่อท้ายหรือในวงเล็บได้ เช่น  
   `ใช้ Wait for web page content เพื่อรอให้ช่องกรอกพร้อมก่อน Interact`
4. คำย่อที่ใช้ซ้ำได้: **PAD** = Power Automate for desktop  
5. หลีกเลี่ยงคำแปลที่ไม่เป็นธรรมชาติ เช่น “ปล่อยโฟลว์”, “จับข้อผิดพลาดแบบลอง-จับ”
6. **Hands-on ทีละขั้น** — ใน `LAB.md` ให้บอกค่าในช่อง action, ตัวแปร produced และตำแหน่งใน workspace ตาม [`HANDS-ON-LAB-TEMPLATE.md`](HANDS-ON-LAB-TEMPLATE.md)  
7. อ้างอิงเอกสารภายนอกให้จำกัดช่วง **สิงหาคม 2026** ตาม [`SOURCES-AUG2026.md`](SOURCES-AUG2026.md)  
8. **ตัวแปร `%`** — แยก “ตั้งชื่อ” กับ “อ้างอิง”: Name / Store into / ชื่อ produced **ไม่มี `%`**; ช่องที่ใช้ค่า **มี `%ชื่อ%`**

## โทนเอกสารผู้เรียน (สำคัญ)

- เขียนให้เหมือนเอกสารหลักสูตรที่ทีม Onto-IQ / วิทยากรจัดทำ  
- **ห้าม** ใส่ข้อความใน Module หรือสไลด์ผู้เรียนที่สื่อว่าเอกสารถูกสร้างหรือตรวจด้วย AI / chatbot / ผู้ช่วยอัตโนมัติ  
- **ห้าม** อ้างเครื่องมือเขียนเอกสารภายในทีมในเนื้อหาที่ผู้เรียนอ่าน  
- อ้างอิงภายนอกให้ชี้ไปที่ Microsoft Learn, Lab Hub, Contoso ตามปกติของหลักสูตร

## ตัวอย่าง

| หลีกเลี่ยง (ห้วน/แปลเกิน) | ใช้แทน |
|---------------------------|--------|
| ปิด Browser ท้าย Flow | ปิดเบราว์เซอร์ท้าย flow ด้วย **Close web browser** |
| รอ element ก่อนคลิก | ใช้ **Wait for web page content** ก่อน Interact กับ element |
| Try-Catch ครอบงาน | ใช้ **On block error** ครอบชุด action ที่เสี่ยง |
| ลาก Action วาง Workspace | ลาก action จาก **Actions Pane** ลงใน workspace |
| Produced variable: `%InboxFiles%` (อย่างเดียว) | ชื่อ produced: `InboxFiles` (ไม่มี `%`) — อ้างอิงด้วย `%InboxFiles%` |
| Set variable Name เป็น `%WorkingRoot%` | Name: `WorkingRoot` แล้วในช่องอื่นค่อยใช้ `%WorkingRoot%` |

## เอกสารที่เกี่ยวข้อง (ผู้เขียน)

| ไฟล์ | ใช้เมื่อ |
|------|---------|
| [`LESSON-TEMPLATE.md`](LESSON-TEMPLATE.md) | โครง `LESSON.md` |
| [`HANDS-ON-LAB-TEMPLATE.md`](HANDS-ON-LAB-TEMPLATE.md) | โครง `LAB.md` |
| [`OFFICIAL-TERMINOLOGY.md`](OFFICIAL-TERMINOLOGY.md) | ชื่อ Action ทางการ |
| [`CLASSROOM-SCHEDULE-12H.md`](CLASSROOM-SCHEDULE-12H.md) | ขอบเขต Core ในห้อง |
