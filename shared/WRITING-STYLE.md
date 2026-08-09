# สไตล์ภาษาใน Lab Kit

ใช้เมื่อเขียนหรือแก้ README ของ Lab

## หลักการ

1. **ภาษาไทยเป็นประโยคอ่านลื่น** — ไม่ห้วนแบบคำสั่งสั้น ๆ จนขาดบริบท  
2. **ไม่แปล keyphrase / ชื่อ Action ทางการ** — คงคำอังกฤษตาม Microsoft Learn เช่น `Wait for web page content`, `On block error`, `UI Elements`, `desktop flow`  
3. คำอธิบายภาษาไทยวางต่อท้ายหรือในวงเล็บได้ เช่น  
   `ใช้ Wait for web page content เพื่อรอให้ช่องกรอกพร้อมก่อน Interact`
4. คำย่อที่ใช้ซ้ำได้: **PAD** = Power Automate for desktop  
5. หลีกเลี่ยงคำแปลที่ไม่เป็นธรรมชาติ เช่น “ปล่อยโฟลว์”, “จับข้อผิดพลาดแบบลอง-จับ”
6. **Hands-on ทีละขั้น** — ใน README ของ Lab ให้มีส่วนที่บอกค่าในช่อง action, ตัวแปร produced และตำแหน่งใน workspace ตาม [`HANDS-ON-LAB-TEMPLATE.md`](HANDS-ON-LAB-TEMPLATE.md) ไม่สรุปเป็น bullet คลุมเครืออย่างเดียว
7. อ้างอิงเอกสารภายนอกให้จำกัดช่วง **สิงหาคม 2026** ตาม [`SOURCES-AUG2026.md`](SOURCES-AUG2026.md)
8. **ตัวแปร `%`** — แยกคำว่า “ตั้งชื่อ” กับ “อ้างอิง” ให้ชัด: ช่อง Name / Store into / ชื่อ produced **ไม่มี `%`**; ช่องที่ใช้ค่าตัวแปร **มี `%ชื่อ%`** (ดูรายละเอียดในแม่แบบ Hands-on)

## ตัวอย่าง

| หลีกเลี่ยง (ห้วน/แปลเกิน) | ใช้แทน |
|---------------------------|--------|
| ปิด Browser ท้าย Flow | ปิดเบราว์เซอร์ท้าย flow ด้วย **Close web browser** |
| รอ element ก่อนคลิก | ใช้ **Wait for web page content** ก่อน Interact กับ element |
| Try-Catch ครอบงาน | ใช้ **On block error** ครอบชุด action ที่เสี่ยง |
| ลาก Action วาง Workspace | ลาก action จาก **Actions Pane** ลงใน workspace |
| Produced variable: `%InboxFiles%` (อย่างเดียว) | ชื่อ produced: `InboxFiles` (ไม่มี `%`) — อ้างอิงด้วย `%InboxFiles%` |
| Set variable Name เป็น `%WorkingRoot%` | Name: `WorkingRoot` แล้วในช่องอื่นค่อยใช้ `%WorkingRoot%` |
