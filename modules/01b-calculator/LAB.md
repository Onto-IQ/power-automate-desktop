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

> **`Txt_CalcDisplay` ไม่ได้อยู่ใน Calculator** — เป็นชื่อที่ **คุณตั้งเองในแผง UI Elements** ของ PAD หลังจับช่องแสดงผล (เหมือน `Btn_Seven`)

1. เปิด UI Picker → **Ctrl + Left Click** จับทีละปุ่ม:
   - ปุ่ม `7` → ใน UI Elements ตั้งชื่อเป็น `Btn_Seven`
   - ปุ่ม `+` → `Btn_Plus`
   - ปุ่ม `8` → `Btn_Eight`
   - ปุ่ม `=` → `Btn_Equals`
2. จับช่องแสดงผลด้านบน (ตัวเลขผลลัพธ์) — PAD อาจตั้งชื่อเริ่มต้นแบบ `Text 'Display is 0'` หรือคล้ายกัน
3. ในแผง **UI Elements** → คลิกขวา / Rename element นั้นเป็น:

```text
Txt_CalcDisplay
```

4. เปิด Selector ของ `Txt_CalcDisplay` → กด **Test**
5. ถ้า selector อิงข้อความ `Display is 0` / `Display is 15` เป็นหลัก ให้ปรับให้เสถียรขึ้น (เช่นใช้ AutomationId / attribute ที่ไม่เปลี่ยนตามตัวเลข) แล้ว Test อีกครั้ง

> บน Windows 11 ชื่อที่ PAD โชว์ตอนจับมักเป็น accessibility text ตามภาษาเครื่อง — **ชื่อใน PAD ที่เราตั้งเอง** (`Txt_CalcDisplay`) คนละอย่างกับข้อความบนจอ

### Step 3 — คลิกลำดับ 7 + 8 =

1. ลาก **Click UI element in window** (หรือ **Press button in window** ถ้าเหมาะกับ control)
2. UI element: `Btn_Seven` → Save
3. ทำซ้ำสำหรับ `Btn_Plus`, `Btn_Eight`, `Btn_Equals` ตามลำดับ
4. ผลบนจอควรเป็น **15**

### Step 4 — อ่านค่าจาก display

ใช้ **Get details of UI element in window** ชี้ element ที่ rename เป็น `Txt_CalcDisplay` แล้ว — **อย่าใช้** Get window title

1. ลาก **Get details of UI element in window**
2. UI element: เลือก `Txt_CalcDisplay`  
   (ถ้ายังเห็นชื่อเดิม `Text 'Display is 0'` → ไป Rename ใน UI Elements ให้เป็น `Txt_CalcDisplay` ก่อน)
3. Attribute: ลอง **Own Text** / Name / Value ตามที่มีในรายการ — ค่าที่ได้อาจเป็น `15` หรือ `Display is 15` ก็ใช้ได้
4. **Variables produced:** `CalcResult` ← **ไม่ใส่ `%`**

> ตัวอย่างจากเครื่องจริง: Own Text ได้ `Display is 15` — เป็นเรื่องปกติของ Calculator ไม่ใช่ Data type ผิด

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
| หา `Txt_CalcDisplay` ไม่เจอใน Calculator | ชื่อนี้ตั้งเองในแผง **UI Elements** — จับช่องแสดงผลแล้ว Rename จากเช่น `Text 'Display is 0'` |
| ใช้ Get window title / Equal to แล้วเข้า Else | อ่านจาก UI element + If **Contains** `15` |
| If แบบ Equal to `15` แล้วเข้า Else ทั้งที่ Own Text เป็น `Display is 15` | เปลี่ยนเป็น **Contains** `15` — ไม่ต้องแก้ Data type |
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
| หา `Txt_CalcDisplay` ไม่เจอ | ไม่ใช่ชื่อในแอป — จับช่องแสดงผลแล้ว **Rename** ใน UI Elements เป็น `Txt_CalcDisplay` |
| `%CalcResult%` เป็น `Display is 15` แล้วเข้า Else | If ใช้ **Contains** `15` (Equal to จะไม่ผ่าน) |
| Selector หลุดหลังคำนวณ | อย่าล็อก Name เป็น `Display is 0` — ปรับ selector ให้เสถียรแล้ว Test |
| แอปเปิดซ้อนหลายตัว | **Close window** หรือ **Terminate process** ก่อนรันใหม่ |
| คลิกไม่ได้ / UIPI | ดู [UIPI issues](https://learn.microsoft.com/troubleshoot/power-platform/power-automate/desktop-flows/ui-automation/uipi-issues) |

## Cleanup

- ปิด Calculator ที่ยังค้างอยู่

## ไม่ต้องปรับเว็บ

Lab นี้ใช้เฉพาะ Calculator จึงไม่เกี่ยวข้องกับ Lab Hub
