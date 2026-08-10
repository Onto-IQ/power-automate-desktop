# Lab 01b — Calculator (Desktop UI)

**วัน:** 1 · **ระดับ:** Beginner · **เวลาโดยประมาณ:** อ่านความรู้ 8–12 นาที + Lab 20–30 นาที  
**ทักษะ:** Click UI element, อ่านค่าจาก display, If ตรวจผล  
**คู่กับสไลด์:** Working with UI Elements · Calculator  
**Flow ชื่อ:** `Lab01b_Calculator`  
**สถานะในตารางสอน:** Optional / ทำเมื่อเหลือเวลาหลัง [Lab 01b Notepad](../01b-notepad/README.md)

## ลำดับการเรียน (จับมือทำ)

| ขั้น | ไฟล์ | ทำอะไร |
|------|------|--------|
| 0 | ทำ [Lab 01b Notepad](../01b-notepad/README.md) ให้ผ่านก่อน (แนะนำ) | พื้นฐาน UI Elements บน Desktop |
| 1 | **[LESSON.md](LESSON.md)** | อ่านความรู้: Click + อ่าน display |
| 2 | **[LAB.md](LAB.md)** | Hands-on Calculator ใน designer |

## Reference scripts (catch-up)

| ไฟล์ | ลำดับปุ่ม | ใช้เมื่อ |
|------|-----------|---------|
| [`scripts/01b-calculator-basic.robin`](scripts/01b-calculator-basic.robin) | `7 + 8 =` → ตรวจ Contains `15` | ตาม LAB หลัก / ตามไม่ทัน |
| [`scripts/01b-calculator-extended.robin`](scripts/01b-calculator-extended.robin) | `7 + 8 ÷ 5 =` → ตรวจ Contains `15` | Challenge / ฝึกกิ่ง Else |

## วัตถุประสงค์

- Capture ปุ่มและช่องแสดงผลของ Calculator ด้วย UI Picker
- คลิกลำดับ `7 + 8 =` ด้วย **Click UI element in window** (ไม่ใช้พิกัดจอ)
- อ่านค่าจาก display เก็บในตัวแปร แล้วใช้ **If** ตรวจว่ามี `15`
- ปิด Calculator อย่างปลอดภัย

## Prerequisites

- ติดตั้ง PAD แล้ว (แนะนำ baseline **2607+**)
- มี Calculator ของ Windows (`calc` / แอป Calculator)
- แนะนำทำ [Lab 01b Notepad](../01b-notepad/README.md) มาก่อน

## บทที่เกี่ยวข้อง

- Notepad (Core วัน 1): [Lab 01b Notepad](../01b-notepad/README.md)
- Desktop เต็มรูปแบบ: [Lab 07 Contoso Invoice Ops](../07-contoso-invoice-ops/README.md)
