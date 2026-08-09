# Lab 01b — Desktop UI Elements (Hands-on)

**อ่านก่อน:** [LESSON.md](LESSON.md) · **หน้าปกบท:** [README.md](README.md) · **พื้นฐาน:** [`shared/PAD-FUNDAMENTALS.md`](../../shared/PAD-FUNDAMENTALS.md)

**วัน:** 1 · **ระดับ:** Beginner  
**ทักษะ:** UI Elements / Selectors บน Windows app, Run application / Focus / Close, Populate text, Click UI element และการอ่านค่าจาก UI  
**คู่กับสไลด์:** Working with UI Elements · Notepad · Calculator

> Lab นี้ไม่ต้องใช้เว็บ Lab Hub — ฝึกกับแอปมาตรฐานของ Windows  
> ส่วนฟอร์มบนเว็บอยู่ที่ [Lab 01](../01-record-replay/README.md) และงาน Desktop ที่ซับซ้อนขึ้นอยู่ที่ [Lab 07 Contoso](../07-contoso-invoice-ops/README.md)

## อ้างอิง (Aug 2026)

| แหล่ง | URL |
|-------|-----|
| UI automation actions | [actions-reference/uiautomation](https://learn.microsoft.com/power-automate/desktop-flows/actions-reference/uiautomation) |
| System actions | [actions-reference/system](https://learn.microsoft.com/power-automate/desktop-flows/actions-reference/system) |
| UIPI troubleshooting | [uipi-issues](https://learn.microsoft.com/troubleshoot/power-platform/power-automate/desktop-flows/ui-automation/uipi-issues) |

## Setup บนเครื่อง (ทำก่อนเปิด designer)

1. สร้างโฟลเดอร์ output (คัดลอก path):

```text
C:\PAD-Labs\output\lab01b\
```

2. เปิด [`assets/notepad-message.txt`](assets/notepad-message.txt) อ่านข้อความที่จะใช้กรอก (หรือคัดลอกไฟล์ไป working ก็ได้) — เนื้อหาเต็มอยู่ใน Step A1
3. ปิด Notepad / Calculator ที่เปิดค้างอยู่ก่อนรัน Lab

## Input / Output

| | Path |
|--|------|
| ข้อความ Notepad | [`assets/notepad-message.txt`](assets/notepad-message.txt) |
| Output (ทางเลือก) | ดู code block ใน Step A1 (`OutFile`) |

---

## Hands-on ทีละขั้น — Part A: Notepad

### Step A0 — สร้าง flow

1. เปิด Power Automate for desktop → **New flow**
2. ชื่อ flow (คัดลอกได้):

```text
Lab01b_DesktopUIElements
```

3. กด **Create**

> **กฎตัวแปรใน PAD (อ่านก่อนทำ Step ถัดไป)**  
> - ช่อง **Name** ของ **Set variable**, ส่วน **Variables produced**, และ **Store into** = พิมพ์ชื่ออย่างเดียว **ไม่มี `%`** เช่น `WorkingRoot`  
> - ช่องอื่นที่ต้องดึงค่าตัวแปร (Folder, File path, Text, …) = ใช้ `%WorkingRoot%` (**มี `%` ครบสองด้าน**)  
> - หลังสร้างแล้ว Variables pane อาจแสดงเป็น `%WorkingRoot%` — เป็นเรื่องปกติ

### Step A1 — ตั้ง path และข้อความ

1. ใน Actions Pane ค้นหา **Set variable** แล้วลากลง workspace
2. ตั้งค่า:
   - Name: `NotepadPath` ← **ไม่ใส่ `%`**
   - Value: (คัดลอกด้านล่างวางในช่อง Value)

```text
C:\Windows\System32\notepad.exe
```

3. เพิ่ม **Set variable** (Name ไม่มี `%`):
   - Name: `OutFile` ← **ไม่ใส่ `%`**
   - Value: (คัดลอกด้านล่างวางในช่อง Value)

```text
C:\PAD-Labs\output\lab01b\notepad-output.txt
```

4. เพิ่ม **Set variable**:
   - Name: `NoteText` ← **ไม่ใส่ `%`**
   - Value: (คัดลอกด้านล่างวางในช่อง Value — เนื้อหาเต็มจาก `notepad-message.txt`)

```text
PAD Lab 01b — Desktop UI Elements
ข้อความนี้ถูกพิมพ์ลง Notepad โดย Power Automate Desktop
วันที่เป้าหมาย: 2026-08-08
```

### Step A2 — เปิด Notepad

1. ลาก **Run application** วางหลังชุด Set variable
2. ตั้งค่า:
   - Application path: (คัดลอกด้านล่างวางในช่อง)

```text
%NotepadPath%
```

   - Window style: Normal (หรือตามที่มี)
3. Produced / รอให้แอปเริ่มได้ตามค่าในหน้าต่าง action
4. กด Save

### Step A3 — รอให้หน้าต่างพร้อม

เส้นทางหลักของวัน 1: ใช้ **Wait for window content** ให้ Notepad พร้อมก่อน Interact — ไม่บังคับ **Focus window** ถ้า Wait แล้วพิมพ์เข้าได้

1. ลาก **Wait for window content**
2. ตั้งค่าให้ชี้หน้าต่าง Notepad / พื้นที่ Edit
3. กด Save

> **Focus window ใส่เมื่อไหร่:** ถ้า Replay แล้วพิมพ์ไม่เข้า หรือหน้าต่างอยู่ด้านหลัง ให้เพิ่ม **Focus window** หลัง Wait (ข้อ 1–2) — ไม่ต้องใช้ Focus แทน Wait และไม่ต้องใส่ Focus ซ้ำถ้าเลือก Focus ไปแล้ว

### Step A4 — Capture UI Element ของพื้นที่พิมพ์

1. เปิด **UI Elements** pane → Add element ด้วย UI Picker
2. ใช้ **Ctrl + Left Click** จับพื้นที่พิมพ์ของ Notepad (Edit / Document)
3. ตั้งชื่อ element: `Edit_NotepadBody`
4. ใน Selector Builder กด **Test** / Validate ก่อนใช้จริง

### Step A5 — กรอกข้อความ

1. ลาก **Populate text field in window**
2. ตั้งค่า:
   - UI element: `Edit_NotepadBody`
   - Text to fill-in: (คัดลอกด้านล่างวางในช่อง)

```text
%NoteText%
```

   - **Simulate action:** เปิด **On** (แนะนำสำหรับ Lab นี้)

3. กด Save

> **ทำไมต้อง Simulate action:** ตอน **Off** PAD จำลองเมาส์/คีย์บอร์ดจริง (physical) — ถ้าโฟกัสไม่นิ่งหรือพิมพ์เร็ว ข้อความ `%NoteText%` อาจขาดหายบางส่วน  
> ตอน **On** จะใส่ข้อความทั้งก้อนแบบ programmatic ตาม [UI automation](https://learn.microsoft.com/power-automate/desktop-flows/actions-reference/uiautomation) ไม่พึ่งคีย์ทีละตัว จึงครบและเสถียรกว่ากับ Notepad  
> ถ้า Simulate ใช้กับ element นั้นไม่ได้ ให้กลับไป **Wait** ให้พร้อม + **Focus window** แล้วลอง Off อีกรอบ หรือใช้ **Focus text field in window** + **Send keys** ตาม [Microsoft troubleshooting](https://learn.microsoft.com/troubleshoot/power-platform/power-automate/desktop-flows/ui-automation/wrong-ui-element-clicked-populated)

### Step A6 — บันทึกไฟล์

1. ลาก **Send keys** (หรือใช้เมนู Save ผ่าน **Click UI element in window** ถ้า capture เมนูได้)
2. ตั้งค่าให้ส่ง `Ctrl+S` ไปที่หน้าต่าง Notepad
3. เมื่อมี Save As:
   - Capture ช่องชื่อไฟล์ → **Populate text field in window** ด้วย (คัดลอกด้านล่างวางในช่อง)

```text
%OutFile%
```

   - Capture ปุ่ม Save → **Press button in window** หรือ **Click UI element in window**
4. จัดการ dialog ทับไฟล์ (Yes/Replace) ถ้ามี — capture UI element ให้ครบ

### Step A7 — ปิด Notepad

1. ลาก **Close window**
2. ตั้งค่า (แนะนำสำหรับ Lab นี้ — เพราะชื่อหน้าต่าง Notepad **เปลี่ยนหลัง Save As**):
   - Find window mode: **By title and/or class**
   - Window title: **ปล่อยว่าง**
   - Window class: (คัดลอก)

```text
Notepad
```

3. ถ้ามี Save dialog หลังปิด ให้มี UI element ของ Don't Save / Yes ตามสถานการณ์จริง
4. กด Save

> อย่าล็อกด้วย title แบบ `Untitled - Notepad` อย่างเดียว — หลังบันทึกไฟล์ title จะเป็นเช่น `notepad-output.txt - Notepad` แล้ว Close จะหาไม่เจอ  
> ปิด Notepad อื่นที่เปิดค้างก่อนรัน Lab — mode นี้ปิดทุกหน้าต่าง class `Notepad`

### Step A8 — รันตรวจ Part A

1. กด **Run**
2. ตรวจว่ามีไฟล์ตาม path นี้ (หรืออย่างน้อย populate สำเร็จแล้วปิดอย่างปลอดภัย):

```text
C:\PAD-Labs\output\lab01b\notepad-output.txt
```

---

## Hands-on ทีละขั้น — Part B: Calculator

วางต่อท้าย Part A ใน Main

### Step B1 — เปิด Calculator

1. ลาก **Run application**
2. ตั้งค่า Application path เป็น path ของ Calculator บนเครื่อง เช่น (คัดลอกด้านล่างวางในช่อง — หรือ path จริงบนเครื่องคุณ):

```text
calc
```

   (บนเครื่องคุณลองเปิดจาก Run `calc` แล้วดู path จริงถ้าจำเป็น)
3. กด Save

### Step B2 — Capture ปุ่มและช่องแสดงผล

1. เปิด UI Picker → **Ctrl + Left Click** จับทีละปุ่ม:
   - `7` → ชื่อใน PAD: `Btn_Seven`
   - `+` → `Btn_Plus`
   - `8` → `Btn_Eight`
   - `=` → `Btn_Equals`
2. จับช่องแสดงผล (Display) → ชื่อ `Txt_CalcDisplay`
3. กด **Test** ใน Selector Builder แต่ละตัว

> บน Windows 11 ชื่อปุ่มอาจเป็น Automation name ตามภาษาของเครื่อง — ใช้ชื่อที่ตั้งเองใน PAD ตามด้านบนได้

### Step B3 — คลิกลำดับ 7 + 8 =

1. ลาก **Click UI element in window** (หรือ **Press button in window** ถ้าเหมาะกับ control)
2. UI element: `Btn_Seven` → Save
3. ทำซ้ำสำหรับ `Btn_Plus`, `Btn_Eight`, `Btn_Equals` ตามลำดับ (วางต่อกันใน workspace)
4. ผลบนจอควรเป็น **15**

### Step B4 — อ่านค่าจาก display

1. ลาก action ที่อ่านข้อความจาก UI element ของหน้าต่าง (เช่น Get details of UI element in window / เทียบเท่าในกลุ่ม UI automation ที่ designer มี)
2. ชี้ `Txt_CalcDisplay`
3. **Variables produced:** `CalcResult` ← **ไม่ใส่ `%`**  
   (อ้างอิงด้วย `%CalcResult%`)

### Step B5 — ตรวจว่าได้ 15

1. ลาก **If**
2. เงื่อนไข: ฝั่งซ้าย (คัดลอกด้านล่างวางในช่อง)

```text
%CalcResult%
```

   ตัวดำเนินการ **Contains** (หรือ Equal to) · ฝั่งขวา (คัดลอกด้านล่างวางในช่อง — ถ้ารูปแบบ display มีทศนิยม/เครื่องหมาย ให้ Contains แล้วปรับตามค่าจริงใน Variables pane):

```text
15
```

3. ในกิ่ง **Else**:
   - ลาก **Set variable** Name: `CalcError` ← **ไม่ใส่ `%`**
   - Value: (คัดลอกด้านล่างวางในช่อง Value)

```text
Unexpected calculator result
```

   - และ/หรือ **Display message** แจ้งว่าค่าไม่ตรง
4. ปิดด้วย **End**

### Step B6 — ปิด Calculator

1. ลาก **Close window** ชี้หน้าต่าง Calculator
2. ถ้าปิดไม่สำเร็จเป็นครั้งคราว ใช้ **Terminate process** เป็นทางสำรอง (ระวังอย่าปิด process อื่น)
3. กด Save

### Step B7 — รันตรวจ Part B

1. กด **Run** ทั้ง flow (Part A + B)
2. ตรวจ `%CalcResult%` ใน Variables pane ว่ามี `15`
3. Replay อีกครั้งหลังปิดแอปค้างทั้งหมด

### Challenge (ทางเลือก)

- ก่อน **Run application** ใช้ **Terminate process** / **Close window** เคลียร์ instance ค้าง แล้ว Replay ให้ผ่านสองครั้งติดกัน

---

## PAD Tips (ตรงสไลด์)

- ใช้ **Ctrl + Left Click** ใน UI Picker เพื่อจับ element
- กด **Test** ใน Selector Builder ก่อนรันจริง
- หากเจอ Multiple Found ให้เพิ่ม Attribute ให้เฉพาะเจาะจงขึ้น
- หลีกเลี่ยงพิกัด X,Y ยกเว้นกรณีจำเป็นจริง ๆ

---

## จุดที่มักทำผิด

| ผิด | ถูก |
|-----|-----|
| พิมพ์ `%Name%` ในช่อง Name / **Variables produced** | ใช้ชื่อเปล่าไม่มี `%` เช่น `NoteText`, `CalcResult` |
| คลิกด้วยพิกัดจอเป็นหลัก | Capture **UI Elements** แล้ว Click / Populate ตาม element |
| ข้อความใน Notepad ไม่ครบ | ใน **Populate text field in window** เปิด **Simulate action** |
| ไม่ Wait ก่อนพิมพ์ | มี **Wait for window content** ก่อน Populate (เพิ่ม **Focus window** เฉพาะเมื่อพิมพ์ไม่เข้า) |
| ลืม Save As path ของ Notepad | ใส่ `%OutFile%` และจัดการ dialog ให้ครบ |
| Calculator ได้ 15 แต่ไม่อ่านจาก display | ต้องเก็บ `%CalcResult%` แล้ว **If** ตรวจ |
| เปิดแอปซ้อนหลายตัวตอน Replay | Close / Terminate ก่อนรันรอบใหม่ |

---

## Variables

| ชื่อตอนสร้าง (ไม่มี `%`) | ตอนอ้างอิง | Type | ตัวอย่าง |
|--------------------------|------------|------|----------|
| `NoteText` | `%NoteText%` | Text | เนื้อหาจาก `notepad-message.txt` |
| `NotepadPath` | `%NotepadPath%` | Text | `C:\Windows\System32\notepad.exe` |
| `OutFile` | `%OutFile%` | Text | `C:\PAD-Labs\output\lab01b\notepad-output.txt` |
| `CalcResult` | `%CalcResult%` | Text | ข้อความจาก display (ควรมี `15`) |

## Expected Result

- Notepad มีข้อความจาก `%NoteText%` และบันทึกไฟล์ได้ (หรือ populate + ปิดอย่างปลอดภัย)
- Calculator ได้ผล 15 และอ่านค่าจาก display เก็บใน `%CalcResult%`
- UI Elements ตั้งชื่อสื่อความหมาย (`Edit_NotepadBody`, `Btn_Seven`, …)

## Acceptance Criteria

- [ ] Notepad พิมพ์ข้อความและบันทึกไฟล์ได้ หรืออย่างน้อย populate สำเร็จแล้วปิดอย่างปลอดภัย
- [ ] Calculator ได้ผล 15 และอ่านค่าจาก display ได้
- [ ] UI Elements ถูกตั้งชื่อให้สื่อความหมาย
- [ ] มีขั้นตอนเปิดและปิดแอปครบ

## Troubleshooting

| อาการ | แก้ |
|-------|-----|
| ข้อความใน Notepad ไม่ครบ / ขาดตัว | เปิด **Simulate action** ใน **Populate text field in window** |
| Close Notepad ไม่เจอหลัง Save As | title เปลี่ยนแล้ว | ใช้ **By title and/or class** + Window class `Notepad` (title ว่าง) |
| Calculator selector หลุด | Recapture หลังสลับโหมด Standard และอย่าใช้พิกัดจอ |
| มี Save dialog ของ Notepad | เพิ่ม UI element ของ Save As / Yes-No ให้ครบ |
| แอปเปิดซ้อนหลายตัว | ใช้ **Close window** หรือ **Terminate process** ก่อน **Run application** ใหม่ |
| คลิกไม่ได้ / UIPI | ดู [UIPI issues](https://learn.microsoft.com/troubleshoot/power-platform/power-automate/desktop-flows/ui-automation/uipi-issues) และรัน PAD ในสิทธิ์ที่เหมาะสม |

## Cleanup

- ปิด Notepad และ Calculator ที่ยังค้างอยู่
- ลบไฟล์ output ได้หลังตรวจผ่านแล้ว

## ไม่ต้องปรับเว็บ

Lab นี้ใช้เฉพาะ Windows apps จึงไม่เกี่ยวข้องกับ Lab Hub
