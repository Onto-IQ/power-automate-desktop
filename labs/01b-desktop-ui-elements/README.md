# Lab 01b — Desktop UI Elements (Notepad + Calculator)

**วัน:** 1 · **ระดับ:** Beginner  
**ทักษะ:** UI Elements / Selectors บน Windows app, Run application / Focus / Close, Populate text, Click UI element และการอ่านค่าจาก UI  
**คู่กับสไลด์:** Working with UI Elements · Notepad · Calculator

> Lab นี้ไม่ต้องใช้เว็บ Lab Hub — ฝึกกับแอปมาตรฐานของ Windows  
> ส่วนฟอร์มบนเว็บอยู่ที่ [Lab 01](../01-record-replay/README.md) และงาน Desktop ที่ซับซ้อนขึ้นอยู่ที่ [Lab 07 Contoso](../07-contoso-invoice-ops/README.md)

## วัตถุประสงค์

- อธิบายได้ว่าทำไมควรใช้ **UI Elements** แทนการคลิกด้วยพิกัดจอ
- เปิด โฟกัส และปิดแอป Windows ด้วย action ที่เหมาะสม
- Capture selector ด้วย UI Picker แล้วทดสอบด้วย Validate/Test
- สร้าง flow สำหรับ Notepad และ Calculator ให้ Replay ได้

## Prerequisites

- ติดตั้ง PAD แล้ว
- มี `notepad.exe` และ Calculator ของ Windows (`calc.exe` หรือแอป Calculator)

## Setup

1. สร้าง flow ชื่อ `Lab01b_DesktopUIElements` (แนะนำแยก Subflow เป็น `SF_Notepad` และ `SF_Calculator`)
2. คัดลอกข้อความจาก [`assets/notepad-message.txt`](assets/notepad-message.txt)
3. กำหนด output (ทางเลือก) ที่ `C:\PAD-Labs\output\lab01b\notepad-output.txt`

## Part A — Notepad

### Expected flow

1. ใช้ **Run application** เปิด `notepad.exe`
2. ใช้ **Wait for window content** และ/หรือ **Focus window** ให้หน้าต่าง Notepad พร้อม
3. Capture UI Element ของพื้นที่พิมพ์ (Edit / Document)
4. ใช้ **Populate text field in window** กรอกข้อความจากไฟล์หรือตัวแปร `%NoteText%`
5. ใช้ **Send keys** เป็น `Ctrl+S` (หรือเมนู Save) แล้วบันทึกไฟล์ไปที่  
   `C:\PAD-Labs\output\lab01b\notepad-output.txt`
6. ปิดด้วย **Close window** และจัดการ Save dialog หากมี

### Variables

| Variable | ตัวอย่าง |
|----------|----------|
| `%NoteText%` | เนื้อหาจาก `notepad-message.txt` |
| `%NotepadPath%` | `C:\Windows\System32\notepad.exe` |
| `%OutFile%` | `C:\PAD-Labs\output\lab01b\notepad-output.txt` |

## Part B — Calculator

### Expected flow

1. เปิด Calculator ด้วย **Run application**
2. Capture ปุ่ม `7`, `+`, `8`, `=` และช่องแสดงผล
3. คลิกตามลำดับจนได้ผลลัพธ์ **15**
4. อ่านข้อความจากช่องแสดงผลไปเก็บใน `%CalcResult%`
5. ใช้ **If** ตรวจว่ามีค่า `15` หรือไม่ — ถ้าไม่ตรงให้ตั้งค่า error / Display message
6. ปิด Calculator ด้วย **Close window**

> บน Windows 11 ชื่อปุ่มอาจเป็น Automation name ตามภาษาของเครื่อง ให้ใช้ UI Picker แล้วตั้งชื่อ element ใน PAD เอง เช่น `Btn_Seven`, `Btn_Plus`

## PAD Tips (ตรงสไลด์)

- ใช้ **Ctrl + Left Click** ใน UI Picker เพื่อจับ element
- กด **Test** ใน Selector Builder ก่อนรันจริง
- หากเจอ Multiple Found ให้เพิ่ม Attribute ให้เฉพาะเจาะจงขึ้น
- หลีกเลี่ยงพิกัด X,Y ยกเว้นกรณีจำเป็นจริง ๆ

## Acceptance Criteria

- [ ] Notepad พิมพ์ข้อความและบันทึกไฟล์ได้ หรืออย่างน้อย populate สำเร็จแล้วปิดอย่างปลอดภัย
- [ ] Calculator ได้ผล 15 และอ่านค่าจาก display ได้
- [ ] UI Elements ถูกตั้งชื่อให้สื่อความหมาย
- [ ] มีขั้นตอนเปิดและปิดแอปครบ
- [ ] (Challenge) แยกเป็นอย่างน้อย 2 Subflows แล้วเรียกจาก Main

## Troubleshooting

| อาการ | แนวทางแก้ |
|-------|-----------|
| Calculator selector หลุด | Recapture หลังสลับโหมด Standard และอย่าใช้พิกัดจอ |
| มี Save dialog ของ Notepad | เพิ่ม UI element ของ Save As / Yes-No ให้ครบ |
| แอปเปิดซ้อนหลายตัว | ใช้ Close window หรือ Terminate process ก่อน Run application ใหม่ |

## Cleanup

- ปิด Notepad และ Calculator ที่ยังค้างอยู่
- ลบไฟล์ output ได้หลังตรวจผ่านแล้ว

## ไม่ต้องปรับเว็บ

Lab นี้ใช้เฉพาะ Windows apps จึงไม่เกี่ยวข้องกับ Lab Hub
