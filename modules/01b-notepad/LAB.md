# Lab 01b — Notepad (Hands-on)

**อ่านก่อน:** [LESSON.md](LESSON.md) · **หน้าปกบท:** [README.md](README.md) · **พื้นฐาน:** [`shared/PAD-FUNDAMENTALS.md`](../../shared/PAD-FUNDAMENTALS.md)

**วัน:** 1 · **ระดับ:** Beginner  
**ทักษะ:** UI Elements / Selectors บน Windows app, Run application / Wait / Close, Populate text + Simulate action  
**คู่กับสไลด์:** Working with UI Elements · Notepad  
**Flow ชื่อ:** `Lab01b_Notepad`

> Lab นี้ไม่ต้องใช้เว็บ Lab Hub — ฝึกกับ Notepad  
> Calculator (optional): [Lab 01b Calculator](../01b-calculator/README.md) · Desktop เต็มรูปแบบ: [Lab 07 Contoso](../07-contoso-invoice-ops/README.md)

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

2. เปิด [`assets/notepad-message.txt`](assets/notepad-message.txt) อ่านข้อความที่จะใช้กรอก — เนื้อหาเต็มอยู่ใน Step 1
3. ปิด Notepad ที่เปิดค้างอยู่ก่อนรัน Lab

## Input / Output

| | Path |
|--|------|
| ข้อความ Notepad | [`assets/notepad-message.txt`](assets/notepad-message.txt) |
| Output | ดู code block ใน Step 1 (`OutFile`) |

---

## Hands-on ทีละขั้น

### Step 0 — สร้าง flow

1. เปิด Power Automate for desktop → **New flow**
2. ชื่อ flow (คัดลอกได้):

```text
Lab01b_Notepad
```

3. กด **Create**

> **กฎตัวแปรใน PAD (อ่านก่อนทำ Step ถัดไป)**  
> - ช่อง **Name** ของ **Set variable**, ส่วน **Variables produced**, และ **Store into** = พิมพ์ชื่ออย่างเดียว **ไม่มี `%`** เช่น `WorkingRoot`  
> - ช่องอื่นที่ต้องดึงค่าตัวแปร (Folder, File path, Text, …) = ใช้ `%WorkingRoot%` (**มี `%` ครบสองด้าน**)  
> - หลังสร้างแล้ว Variables pane อาจแสดงเป็น `%WorkingRoot%` — เป็นเรื่องปกติ

### Step 1 — ตั้ง path และข้อความ

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
PAD Lab 01b — Notepad
ข้อความนี้ถูกพิมพ์ลง Notepad โดย Power Automate Desktop
วันที่เป้าหมาย: 2026-08-08
```

### Step 2 — เปิด Notepad

1. ลาก **Run application** วางหลังชุด Set variable
2. ตั้งค่า:
   - Application path: (คัดลอกด้านล่างวางในช่อง)

```text
%NotepadPath%
```

   - Window style: Normal (หรือตามที่มี)
3. Produced / รอให้แอปเริ่มได้ตามค่าในหน้าต่าง action
4. กด Save

### Step 3 — รอให้หน้าต่างพร้อม

เส้นทางหลัก: ใช้ **Wait for window content** ให้ Notepad พร้อมก่อน Interact — ไม่บังคับ **Focus window** ถ้า Wait แล้วพิมพ์เข้าได้

1. ลาก **Wait for window content**
2. ตั้งค่าให้ชี้หน้าต่าง Notepad / พื้นที่ Edit
3. กด Save

> **Focus window ใส่เมื่อไหร่:** ถ้า Replay แล้วพิมพ์ไม่เข้า หรือหน้าต่างอยู่ด้านหลัง ให้เพิ่ม **Focus window** หลัง Wait — ไม่ต้องใช้ Focus แทน Wait

### Step 4 — Capture UI Element ของพื้นที่พิมพ์

1. เปิด **UI Elements** pane → Add element ด้วย UI Picker
2. ใช้ **Ctrl + Left Click** จับพื้นที่พิมพ์ของ Notepad (Edit / Document)
3. ตั้งชื่อ element: `Edit_NotepadBody`
4. ใน Selector Builder กด **Test** / Validate ก่อนใช้จริง

### Step 5 — กรอกข้อความ

1. ลาก **Populate text field in window**
2. ตั้งค่า:
   - UI element: `Edit_NotepadBody`
   - Text to fill-in: (คัดลอกด้านล่างวางในช่อง)

```text
%NoteText%
```

   - **Simulate action:** เปิด **On** (แนะนำสำหรับ Lab นี้)

3. กด Save

> **ทำไมต้อง Simulate action:** ตอน **Off** PAD จำลองเมาส์/คีย์บอร์ดจริง — ข้อความอาจขาดหายบางส่วน  
> ตอน **On** ใส่ข้อความทั้งก้อนแบบ programmatic ตาม [UI automation](https://learn.microsoft.com/power-automate/desktop-flows/actions-reference/uiautomation)  
> ถ้า Simulate ใช้ไม่ได้: Wait + **Focus window** แล้วลอง Off หรือใช้ **Focus text field in window** + **Send keys** ตาม [troubleshooting](https://learn.microsoft.com/troubleshoot/power-platform/power-automate/desktop-flows/ui-automation/wrong-ui-element-clicked-populated)

### Step 6 — บันทึกไฟล์

1. ลาก **Send keys** (หรือใช้เมนู Save ผ่าน **Click UI element in window** ถ้า capture เมนูได้)
2. ตั้งค่าให้ส่ง `Ctrl+S` ไปที่หน้าต่าง Notepad
3. เมื่อมี Save As:
   - Capture ช่องชื่อไฟล์ → **Populate text field in window** ด้วย (คัดลอกด้านล่างวางในช่อง)

```text
%OutFile%
```

   - Capture ปุ่ม Save → **Press button in window** หรือ **Click UI element in window**
4. จัดการ dialog ทับไฟล์ (Yes/Replace) ถ้ามี — capture UI element ให้ครบ

### Step 7 — ปิด Notepad

1. ลาก **Close window**
2. ตั้งค่า (แนะนำ — เพราะชื่อหน้าต่าง Notepad **เปลี่ยนหลัง Save As**):
   - Find window mode: **By title and/or class**
   - Window title: **ปล่อยว่าง**
   - Window class: (คัดลอก)

```text
Notepad
```

3. ถ้ามี Save dialog หลังปิด ให้มี UI element ของ Don't Save / Yes ตามสถานการณ์จริง
4. กด Save

> อย่าล็อกด้วย title แบบ `Untitled - Notepad` อย่างเดียว — หลังบันทึก title จะเปลี่ยนแล้ว Close จะหาไม่เจอ  
> ปิด Notepad อื่นที่เปิดค้างก่อนรัน Lab — mode นี้ปิดทุกหน้าต่าง class `Notepad`

### Step 8 — รันตรวจ

1. กด **Run**
2. ตรวจว่ามีไฟล์ตาม path นี้ (หรืออย่างน้อย populate สำเร็จแล้วปิดอย่างปลอดภัย):

```text
C:\PAD-Labs\output\lab01b\notepad-output.txt
```

3. Replay อีกครั้งหลังปิดแอปค้าง

### Challenge (ทางเลือก)

- ก่อน **Run application** ใช้ **Terminate process** / **Close window** เคลียร์ instance ค้าง แล้ว Replay ให้ผ่านสองครั้งติดกัน
- ทำต่อ [Lab 01b Calculator](../01b-calculator/LAB.md) ถ้าเหลือเวลา

---

## PAD Tips

- ใช้ **Ctrl + Left Click** ใน UI Picker เพื่อจับ element
- กด **Test** ใน Selector Builder ก่อนรันจริง
- หากเจอ Multiple Found ให้เพิ่ม Attribute ให้เฉพาะเจาะจงขึ้น
- หลีกเลี่ยงพิกัด X,Y ยกเว้นกรณีจำเป็นจริง ๆ

---

## จุดที่มักทำผิด

| ผิด | ถูก |
|-----|-----|
| พิมพ์ `%Name%` ในช่อง Name / **Variables produced** | ใช้ชื่อเปล่าไม่มี `%` เช่น `NoteText`, `OutFile` |
| คลิกด้วยพิกัดจอเป็นหลัก | Capture **UI Elements** แล้ว Populate ตาม element |
| ข้อความใน Notepad ไม่ครบ | เปิด **Simulate action** |
| ไม่ Wait ก่อนพิมพ์ | มี **Wait for window content** ก่อน Populate |
| ลืม Save As path | ใส่ `%OutFile%` และจัดการ dialog ให้ครบ |
| Close ด้วย title เดิมหลัง Save As | ใช้ Window class `Notepad` |
| เปิดแอปซ้อนหลายตัวตอน Replay | Close / Terminate ก่อนรันรอบใหม่ |

---

## Variables

| ชื่อตอนสร้าง (ไม่มี `%`) | ตอนอ้างอิง | Type | ตัวอย่าง |
|--------------------------|------------|------|----------|
| `NoteText` | `%NoteText%` | Text | เนื้อหาจาก `notepad-message.txt` |
| `NotepadPath` | `%NotepadPath%` | Text | `C:\Windows\System32\notepad.exe` |
| `OutFile` | `%OutFile%` | Text | `C:\PAD-Labs\output\lab01b\notepad-output.txt` |

## Expected Result

- Notepad มีข้อความจาก `%NoteText%` และบันทึกไฟล์ได้ (หรือ populate + ปิดอย่างปลอดภัย)
- UI Elements ตั้งชื่อสื่อความหมาย (`Edit_NotepadBody`, …)

## Acceptance Criteria

- [ ] ตั้งชื่อ flow `Lab01b_Notepad`
- [ ] Notepad พิมพ์ข้อความและบันทึกไฟล์ได้ หรืออย่างน้อย populate สำเร็จแล้วปิดอย่างปลอดภัย
- [ ] Populate เปิด **Simulate action**
- [ ] Close ใช้ Window class `Notepad` (หรือเทียบเท่าที่เสถียรหลัง Save As)
- [ ] UI Elements ถูกตั้งชื่อให้สื่อความหมาย

## Troubleshooting

| อาการ | แก้ |
|-------|-----|
| ข้อความไม่ครบ / ขาดตัว | เปิด **Simulate action** ใน **Populate text field in window** |
| Close ไม่เจอหลัง Save As | ใช้ **By title and/or class** + Window class `Notepad` (title ว่าง) |
| มี Save dialog | เพิ่ม UI element ของ Save As / Yes-No ให้ครบ |
| แอปเปิดซ้อนหลายตัว | **Close window** หรือ **Terminate process** ก่อน **Run application** ใหม่ |
| คลิกไม่ได้ / UIPI | ดู [UIPI issues](https://learn.microsoft.com/troubleshoot/power-platform/power-automate/desktop-flows/ui-automation/uipi-issues) |

## Cleanup

- ปิด Notepad ที่ยังค้างอยู่
- ลบไฟล์ output ได้หลังตรวจผ่านแล้ว

## ไม่ต้องปรับเว็บ

Lab นี้ใช้เฉพาะ Notepad จึงไม่เกี่ยวข้องกับ Lab Hub
