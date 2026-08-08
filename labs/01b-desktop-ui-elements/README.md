# Lab 01b — Desktop UI Elements (Notepad + Calculator)

**วัน:** 1 · **ระดับ:** Beginner  
**ทักษะ:** UI Elements / Selectors บน Windows app, Launch / Focus / Close, Populate text, Click UI element, อ่านค่าจาก UI  
**คู่กับสไลด์:** Working with UI Elements · Notepad · Calculator

> Lab นี้**ไม่ต้องใช้เว็บ** — ใช้แอปมาตรฐานของ Windows  
> Web form อยู่ที่ [Lab 01](../01-record-replay/README.md) · Desktop ซับซ้อนขึ้นอยู่ที่ [Lab 07 Contoso](../07-contoso-invoice-ops/README.md)

## วัตถุประสงค์

- เข้าใจว่าทำไมต้องใช้ UI Elements แทนพิกัดจอ
- Launch / Focus / Close แอป Windows
- Capture selector ด้วย UI Picker แล้ว Validate
- สร้าง Flow Notepad และ Calculator ให้ Replay ได้

## Prerequisites

- PAD ติดตั้งแล้ว
- มี `notepad.exe` และ Calculator ของ Windows (`calc.exe` หรือแอป Calculator)

## Setup

1. Flow ชื่อ `Lab01b_DesktopUIElements` (แนะนำแยก Subflow: `SF_Notepad`, `SF_Calculator`)
2. คัดลอกข้อความจาก [`assets/notepad-message.txt`](assets/notepad-message.txt)
3. Output (ทางเลือก): `C:\PAD-Labs\output\lab01b\notepad-output.txt`

## Part A — Notepad

### Expected flow

1. **Run application** → `notepad.exe`
2. **Wait for window content** / **Focus window** หน้าต่าง Notepad
3. Capture UI Element ของพื้นที่พิมพ์ (Edit / Document)
4. **Populate text field in window** ด้วยข้อความจากไฟล์หรือตัวแปร `%NoteText%`
5. **Send keys** `Ctrl+S` (หรือเมนู Save) → บันทึกเป็น  
   `C:\PAD-Labs\output\lab01b\notepad-output.txt`
6. **Close window** (จัดการ Save dialog ถ้ามี)

### Variables

| Variable | ตัวอย่าง |
|----------|----------|
| `%NoteText%` | เนื้อจาก `notepad-message.txt` |
| `%NotepadPath%` | `C:\Windows\System32\notepad.exe` |
| `%OutFile%` | `C:\PAD-Labs\output\lab01b\notepad-output.txt` |

## Part B — Calculator

### Expected flow

1. Launch Calculator
2. Capture ปุ่ม `7`, `+`, `8`, `=` และช่องแสดงผล
3. คลิกตามลำดับให้ได้ผล **15**
4. **Extract** ข้อความผลลัพธ์จาก display → `%CalcResult%`
5. **If** `%CalcResult%` ไม่มี `15` → ตั้ง `%LastError%` / Display message
6. Close Calculator

> บน Windows 11 ชื่อปุ่มอาจเป็น Automation name ภาษาเครื่อง — ใช้ UI Picker แล้วตั้งชื่อ element ใน PAD เอง เช่น `Btn_Seven`, `Btn_Plus`

## PAD Tips (ตรงสไลด์)

- ใช้ **Ctrl + Left Click** ใน UI Picker
- กด **Test** ใน Selector Builder ก่อนรัน
- ถ้าเจอ Multiple Found → เพิ่ม Attribute ให้เฉพาะเจาะจง
- หลีกเลี่ยงพิกัด X,Y ยกเว้นกรณีจำเป็นจริง ๆ

## Acceptance Criteria

- [ ] Notepad พิมพ์ข้อความและบันทึกไฟล์ได้ (หรืออย่างน้อย populate สำเร็จแล้วปิดอย่างปลอดภัย)
- [ ] Calculator ได้ผล 15 และอ่านค่า display ได้
- [ ] UI Elements ถูกตั้งชื่อสื่อความหมาย
- [ ] มี Launch + Close ครบ
- [ ] (Challenge) แยกเป็น 2 Subflows แล้วเรียกจาก Main

## Troubleshooting

| อาการ | แก้ |
|-------|-----|
| Calculator selector หลุด | Recapture หลังสลับโหมด Standard; อย่าใช้พิกัด |
| Notepad Save dialog | เพิ่ม UI element ของ Save As / Yes-No |
| แอปเปิดซ้อน | Close/Terminate process ก่อน Launch |

## Cleanup

- ปิด Notepad/Calculator ที่ค้าง
- ลบไฟล์ output ได้หลังตรวจ

## ไม่ต้องปรับเว็บ

Lab นี้ใช้ Windows apps เท่านั้น — ไม่เกี่ยวกับ Lab Hub
