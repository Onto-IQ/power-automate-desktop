# Lab 01b — Calculator (Hands-on)

**อ่านก่อน:** [LESSON.md](LESSON.md) · **หน้าปกบท:** [README.md](README.md) · **พื้นฐาน:** [`shared/PAD-FUNDAMENTALS.md`](../../shared/PAD-FUNDAMENTALS.md)

**วัน:** 1 · **ระดับ:** Beginner · **Optional**  
**ทักษะ:** Click UI element, อ่านค่าจาก display, If ตรวจผล  
**คู่กับสไลด์:** Calculator  
**Flow ชื่อ:** `Lab01b_Calculator`

> แนะนำทำ [Lab 01b Notepad](../01b-notepad/LAB.md) ให้ผ่านก่อน  
> Lab นี้เป็น flow **แยก** — อย่าวางต่อท้าย flow Notepad

## อ้างอิง (Aug 2026)

| แหล่ง | URL |
|-------|-----|
| UI automation actions | [actions-reference/uiautomation](https://learn.microsoft.com/power-automate/desktop-flows/actions-reference/uiautomation) |
| UIPI troubleshooting | [uipi-issues](https://learn.microsoft.com/troubleshoot/power-platform/power-automate/desktop-flows/ui-automation/uipi-issues) |

## Setup บนเครื่อง

1. ปิด Calculator ที่เปิดค้างอยู่
2. เปิด Calculator ด้วยมือหนึ่งครั้ง → สลับเป็นโหมด **Standard** แล้วปิด

---

## Hands-on ทีละขั้น

### Step 0 — สร้าง flow

1. เปิด Power Automate for desktop → **New flow**
2. ชื่อ flow (คัดลอกได้):

```text
Lab01b_Calculator
```

3. กด **Create**

> **กฎตัวแปร:** ช่อง Name / Variables produced = ไม่มี `%` · ช่องอ้างอิงค่า = มี `%` ครบสองด้าน

### Step 1 — เปิด Calculator

1. ลาก **Run application**
2. ตั้งค่า Application path (คัดลอก — หรือ path จริงบนเครื่องคุณ):

```text
calc
```

3. กด Save
4. (แนะนำ) ลาก **Wait for window content** ให้หน้าต่าง Calculator พร้อม

### Step 2 — Capture ปุ่มและช่องแสดงผล

1. เปิด UI Picker → **Ctrl + Left Click** จับทีละปุ่ม:
   - `7` → ชื่อใน PAD: `Btn_Seven`
   - `+` → `Btn_Plus`
   - `8` → `Btn_Eight`
   - `=` → `Btn_Equals`
2. จับช่องแสดงผล (Display) → ชื่อ `Txt_CalcDisplay`
3. กด **Test** ใน Selector Builder แต่ละตัว

> บน Windows 11 ชื่อปุ่มอาจเป็น Automation name ตามภาษาของเครื่อง — ใช้ชื่อที่ตั้งเองใน PAD ตามด้านบนได้

### Step 3 — คลิกลำดับ 7 + 8 =

1. ลาก **Click UI element in window** (หรือ **Press button in window** ถ้าเหมาะกับ control)
2. UI element: `Btn_Seven` → Save
3. ทำซ้ำสำหรับ `Btn_Plus`, `Btn_Eight`, `Btn_Equals` ตามลำดับ
4. ผลบนจอควรเป็น **15**

### Step 4 — อ่านค่าจาก display

ใช้ **Get details of UI element in window** ชี้ element ช่องแสดงผล — **อย่าใช้** **Get details of window** → Get window title

1. ลาก **Get details of UI element in window**
2. UI element: `Txt_CalcDisplay` (ช่องแสดงผลที่ capture ใน Step 2)
3. Attribute / รายละเอียดที่อ่าน: เลือกข้อความของ control (เช่น Name / Value / Text ตามที่ designer แสดงหลัง Test — ต้องมีเลขผลลัพธ์)
4. **Variables produced:** `CalcResult` ← **ไม่ใส่ `%`**  
   (อ้างอิงด้วย `%CalcResult%`)

> ถ้าใช้ Get window title จะได้ข้อความแบบ accessibility เช่น `Display is 15` ไม่ใช่ค่าในช่องแสดงผลโดยตรง — แล้วยังไม่ใช่ปัญหา Data type (ยังเป็น Text อยู่)

### Step 5 — ตรวจว่าได้ 15

1. ลาก **If**
2. เงื่อนไข: ฝั่งซ้าย (คัดลอก)

```text
%CalcResult%
```

   ตัวดำเนินการ **Contains** (แนะนำ) · ฝั่งขวา (คัดลอก):

```text
15
```

> ใช้ **Contains** ไม่ใช้ **Equal to** เป็นหลัก — ค่าที่อ่านได้มักเป็นข้อความ เช่น `15` หรือบางเครื่อง `Display is 15` / มีทศนิยม  
> แก้ที่เงื่อนไข If + แหล่งที่อ่าน (UI element) — **ไม่ต้องเปลี่ยน Data type** ของตัวแปร

3. ในกิ่ง **Else**:
   - ลาก **Set variable** Name: `CalcError` ← **ไม่ใส่ `%`**
   - Value: (คัดลอก)

```text
Unexpected calculator result
```

   - และ/หรือ **Display message** แจ้งว่าค่าไม่ตรง
4. ปิดด้วย **End**

### Step 6 — ปิด Calculator

1. ลาก **Close window**
2. ตั้งค่า (แนะนำ — **ไม่ใช้แบบ Notepad ที่ปล่อย title ว่าง**):
   - Find window mode: **By title and/or class**
   - Window title: (คัดลอก — หรือชื่อตามภาษา UI ของเครื่อง เช่น `เครื่องคิดเลข`)

```text
Calculator
```

   - Window class: (ทางเลือก ถ้า title อย่างเดียวเจอหลายหน้าต่าง)

```text
ApplicationFrameWindow
```

3. ถ้าปิดไม่สำเร็จเป็นครั้งคราว ใช้ **Terminate process** เป็นทางสำรอง — process ที่พบบ่อยคือ `CalculatorApp` (ระวังอย่าปิด process อื่น)
4. กด Save

> **ทำไมไม่เหมือน Notepad:** Notepad ใช้ class `Notepad` เพราะ title เปลี่ยนหลัง Save As  
> Calculator title ค่อนข้างคงที่ แต่ class `ApplicationFrameWindow` เป็นของแอป Store/UWP หลายตัว — **ห้ามปล่อย title ว่างแล้วปิดด้วย class อย่างเดียว**

### Step 7 — รันตรวจ

1. กด **Run**
2. ตรวจ `%CalcResult%` ใน Variables pane ว่ามี `15`
3. Replay อีกครั้งหลังปิดแอปค้างทั้งหมด

### Challenge (ทางเลือก)

- ก่อน **Run application** ใช้ **Terminate process** / **Close window** เคลียร์ instance ค้าง แล้ว Replay ให้ผ่านสองครั้งติดกัน

---

## PAD Tips

- ใช้ **Ctrl + Left Click** ใน UI Picker
- กด **Test** ใน Selector Builder ก่อนรันจริง
- หากเจอ Multiple Found ให้เพิ่ม Attribute ให้เฉพาะเจาะจงขึ้น
- หลีกเลี่ยงพิกัด X,Y

---

## จุดที่มักทำผิด

| ผิด | ถูก |
|-----|-----|
| ใช้ Get window title แล้วได้ `Display is 15` | ใช้ **Get details of UI element in window** ชี้ `Txt_CalcDisplay` |
| If แบบ Equal to `15` แล้วเข้า Else | เปลี่ยนเป็น **Contains** `15` — ไม่ต้องแก้ Data type |
| พิมพ์ `%CalcResult%` ในช่อง Variables produced | ใช้ชื่อเปล่า `CalcResult` |
| คลิกด้วยพิกัดจอ | Capture UI Elements แล้ว Click |
| ปิดด้วย class อย่างเดียวเหมือน Notepad | ใส่ **Window title** `Calculator` (หรือชื่อภาษาเครื่อง) — อย่าปล่อย title ว่างกับ class `ApplicationFrameWindow` |
| ได้ 15 แต่ไม่อ่านจาก display | เก็บ `%CalcResult%` แล้ว **If** ตรวจ |
| เปิดแอปซ้อนตอน Replay | Close / Terminate ก่อนรันรอบใหม่ |

---

## Variables

| ชื่อตอนสร้าง (ไม่มี `%`) | ตอนอ้างอิง | Type | ตัวอย่าง |
|--------------------------|------------|------|----------|
| `CalcResult` | `%CalcResult%` | Text | ข้อความจาก display (ควรมี `15`) |
| `CalcError` | `%CalcError%` | Text | Unexpected calculator result |

## Expected Result

- Calculator ได้ผล 15 และอ่านค่าจาก display เก็บใน `%CalcResult%`
- UI Elements ตั้งชื่อสื่อความหมาย (`Btn_Seven`, `Txt_CalcDisplay`, …)

## Acceptance Criteria

- [ ] ตั้งชื่อ flow `Lab01b_Calculator`
- [ ] Calculator ได้ผล 15 และอ่านค่าจาก display ได้
- [ ] มี **If** ตรวจ `%CalcResult%`
- [ ] มีขั้นตอนเปิดและปิดแอปครบ
- [ ] UI Elements ถูกตั้งชื่อให้สื่อความหมาย

## Troubleshooting

| อาการ | แก้ |
|-------|-----|
| `%CalcResult%` เป็น `Display is 15` แล้วเข้า Else | อย่าใช้ Get window title — เปลี่ยนเป็น **Get details of UI element in window** + If **Contains** `15` |
| Selector หลุด | Recapture หลังสลับโหมด Standard และอย่าใช้พิกัดจอ |
| แอปเปิดซ้อนหลายตัว | **Close window** หรือ **Terminate process** ก่อนรันใหม่ |
| คลิกไม่ได้ / UIPI | ดู [UIPI issues](https://learn.microsoft.com/troubleshoot/power-platform/power-automate/desktop-flows/ui-automation/uipi-issues) |

## Cleanup

- ปิด Calculator ที่ยังค้างอยู่

## ไม่ต้องปรับเว็บ

Lab นี้ใช้เฉพาะ Calculator จึงไม่เกี่ยวข้องกับ Lab Hub
