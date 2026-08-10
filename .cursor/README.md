# Cursor — skills / rules ของทีมพัฒนา (local)

โฟลเดอร์นี้เก็บ Cursor rules และ skills สำหรับ maintain lab kit — **ไม่แจกผู้เรียน**

| สถานะ | รายละเอียด |
|--------|------------|
| Git | เนื้อหาส่วนใหญ่ **ไม่ขึ้น GitHub** (gitignore) — มีแค่ README นี้ |
| ใครใช้ | ทีม Onto-IQ / วิทยากรที่แก้ `modules/` + Robin ด้วย Cursor |
| ผู้เรียน | **ไม่แจก** และไม่ใส่ลิงก์จาก README หลัก |

## ไฟล์ที่ควรมีบนเครื่องทีม (local)

| Path | หน้าที่ |
|------|---------|
| `rules/*.mdc` | Project rules (PAD Lab Kit, Robin, lab docs) |
| `skills/pad-robin/` | Skill + linter + action catalog สำหรับ `.robin` |
| `skills/power-automate/` | (ถ้ามี) plugin อื่น — คงเป็น local เท่านั้น |

ถ้าเครื่องใหม่ยังไม่มี ให้คัดลอกจากเครื่องทีมหรือ backup ภายใน — **อย่า commit กลับขึ้น repo สาธารณะ**

เอกสารผู้เรียน: [`../README.md`](../README.md) · [`../shared/`](../shared/) · [`../modules/`](../modules/)
