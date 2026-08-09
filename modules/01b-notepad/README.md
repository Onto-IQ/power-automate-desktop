# Lab 01b — Notepad (Desktop UI)

**วัน:** 1 · **ระดับ:** Beginner · **เวลาโดยประมาณ:** อ่านความรู้ 10–15 นาที + Lab 25–35 นาที  
**ทักษะ:** UI Elements / Selectors บน Windows app, Run application / Wait / Close, Populate text + Simulate action  
**คู่กับสไลด์:** Working with UI Elements · Notepad  
**Flow ชื่อ:** `Lab01b_Notepad`

## ลำดับการเรียน (จับมือทำ)

| ขั้น | ไฟล์ | ทำอะไร |
|------|------|--------|
| 0 | [`shared/PAD-FUNDAMENTALS.md`](../../shared/PAD-FUNDAMENTALS.md) | พื้นฐาน PAD / กฎ `%` (ถ้ายังไม่คุ้น designer) |
| 1 | **[LESSON.md](LESSON.md)** | อ่านความรู้: UI Elements บน Windows + Notepad |
| 2 | **[LAB.md](LAB.md)** | Setup + Hands-on ใน designer |

## วัตถุประสงค์

- อธิบายได้ว่าทำไมควรใช้ **UI Elements** แทนการคลิกด้วยพิกัดจอ
- เปิด รอ และปิด Notepad ด้วย action ที่เหมาะสม
- Capture selector ด้วย UI Picker แล้วทดสอบด้วย Validate/Test
- Populate ข้อความด้วย **Simulate action** แล้ว Save As ให้ Replay ได้

## Prerequisites

- ติดตั้ง PAD แล้ว (แนะนำ baseline **2607+** — ดู [PAD version matrix](https://learn.microsoft.com/power-platform/released-versions/power-automate-desktop))
- มี `notepad.exe`

## Assets / Output

| | Path |
|--|------|
| ข้อความ Notepad | [`assets/notepad-message.txt`](assets/notepad-message.txt) |
| Output | `C:\PAD-Labs\output\lab01b\notepad-output.txt` |

## บทที่เกี่ยวข้อง

- ฟอร์มบนเว็บ: [Lab 01 Record & Replay](../01-record-replay/README.md)
- Calculator (optional วัน 1): [Lab 01b Calculator](../01b-calculator/README.md)
- Desktop ที่ซับซ้อนขึ้น: [Lab 07 Contoso Invoice Ops](../07-contoso-invoice-ops/README.md)
