# สไตล์ภาษาใน Lab Kit

ใช้เมื่อเขียนหรือแก้ README ของ Lab

## หลักการ

1. **ภาษาไทยเป็นประโยคอ่านลื่น** — ไม่ห้วนแบบคำสั่งสั้น ๆ จนขาดบริบท  
2. **ไม่แปล keyphrase / ชื่อ Action ทางการ** — คงคำอังกฤษตาม Microsoft Learn เช่น `Wait for web page content`, `On block error`, `UI Elements`, `desktop flow`  
3. คำอธิบายภาษาไทยวางต่อท้ายหรือในวงเล็บได้ เช่น  
   `ใช้ Wait for web page content เพื่อรอให้ช่องกรอกพร้อมก่อน Interact`
4. คำย่อที่ใช้ซ้ำได้: **PAD** = Power Automate for desktop  
5. หลีกเลี่ยงคำแปลที่ไม่เป็นธรรมชาติ เช่น “ปล่อยโฟลว์”, “จับข้อผิดพลาดแบบลอง-จับ”

## ตัวอย่าง

| หลีกเลี่ยง (ห้วน/แปลเกิน) | ใช้แทน |
|---------------------------|--------|
| ปิด Browser ท้าย Flow | ปิดเบราว์เซอร์ท้าย flow ด้วย **Close web browser** |
| รอ element ก่อนคลิก | ใช้ **Wait for web page content** ก่อน Interact กับ element |
| Try-Catch ครอบงาน | ใช้ **On block error** ครอบชุด action ที่เสี่ยง |
| ลาก Action วาง Workspace | ลาก action จาก **Actions Pane** ลงใน workspace |
