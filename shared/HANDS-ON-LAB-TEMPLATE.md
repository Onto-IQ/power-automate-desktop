# แม่แบบ Hands-on Lab (ทีละขั้น)

ใช้โครงสร้างนี้เมื่อเขียนหรือปรับ **`modules/*/LAB.md`** (เอกสารจับมือทำ)  
หน้าปกบทอยู่ที่ **`modules/*/README.md`** · ความรู้อยู่ที่ **`modules/*/LESSON.md`**  
เป้าหมาย: ผู้เรียนทำตามได้โดยไม่ต้องเดาว่าต้องคลิกอะไรใน designer

ลำดับต่อบท: [`PAD-FUNDAMENTALS.md`](PAD-FUNDAMENTALS.md) → `LESSON.md` → `LAB.md`  
แม่แบบความรู้: [`LESSON-TEMPLATE.md`](LESSON-TEMPLATE.md)

## โครงมาตรฐานของ LAB.md

1. **หัวเรื่อง + ลิงก์กลับ** README / LESSON  
2. **Setup บนเครื่อง** (คัดลอกไฟล์ / สร้างโฟลเดอร์ — ทีละข้อ)  
3. **Input / Output**  
4. **อ้างอิง Aug 2026** (ลิงก์สั้น 1–3 รายการจาก [`SOURCES-AUG2026.md`](SOURCES-AUG2026.md)) — หรืออ้างใน LESSON แล้วใส่สั้น ๆ  
5. **Hands-on ทีละขั้น** ← ส่วนหลัก (บังคับ)  
6. **จุดที่มักทำผิด** (Common mistakes)  
7. **Variables** (คอลัมน์: ชื่อตอนสร้าง | ตอนอ้างอิง | Type)  
8. **Expected Result** + **Acceptance Criteria**  
9. **Troubleshooting** + **Cleanup**

## กติกาตัวแปร `%` (สำคัญ — ผู้เรียนมักสับสน)

ใน PAD **ตอนสร้าง/ตั้งชื่อตัวแปรไม่ใส่ `%`** แต่ **ตอนอ้างอิงในช่องอื่นใส่ `%ชื่อ%`**

| สถานการณ์ใน designer | ใส่ในช่องอย่างไร | ตัวอย่าง |
|----------------------|------------------|----------|
| **Set variable** → Name | ชื่อเปล่า ไม่มี `%` | `WorkingRoot` |
| **Increase variable** / เลือกตัวแปรจากรายการ | ชื่อเปล่า / เลือกจาก list | `CsvCount` |
| **For each** → Store into | ชื่อเปล่า ไม่มี `%` | `CurrentFile` |
| เปลี่ยนชื่อ **Produced variable** ของ action | ชื่อเปล่า ไม่มี `%` | `InboxFiles` |
| ช่องค่าอื่นที่ต้อง **ใช้** ตัวแปร (Folder, File path, Text, …) | ห่อด้วย `%` ทั้งสองด้าน | `%WorkingRoot%\inbox` |
| นิพจน์ในช่องค่า | ทั้งนิพจน์อยู่ใน `%...%` | `%CsvCount + 1%` |

ใน LAB ให้เขียนแยกชัดเสมอ เช่น:

```text
- Name: `WorkingRoot`          ← สร้าง (ไม่มี %)
- Folder: `%WorkingRoot%\inbox` ← ใช้ (มี %)
- ชื่อ produced: `InboxFiles`   ← สร้าง/เปลี่ยนชื่อ (ไม่มี %)
  เวลาอ้างอิงทีหลังใช้ `%InboxFiles%`
```

อย่าเขียนแค่ `Produced variable: %InboxFiles%` โดยไม่บอกว่าช่องชื่อไม่ใส่ `%` — ผู้เรียนจะพิมพ์ `%` ลงช่อง Name แล้วสับสน

Callout มาตรฐานที่ควรมีใกล้ Step แรกที่มีตัวแปร:

```markdown
> **กฎตัวแปรใน PAD:** ช่อง **Name** / ชื่อ produced / Store into = พิมพ์ชื่ออย่างเดียว เช่น `WorkingRoot`  
> ช่องอื่นที่ต้องดึงค่าตัวแปร = ใช้ `%WorkingRoot%` (มี `%` ครบสองด้าน)
```

## กติกา “ค่าที่ต้องวางในช่อง” = fenced code block (copy ได้ง่าย)

ผู้เรียนเป็น user ทั่วไป — **ทุกค่าที่ต้องพิมพ์/วางลงช่องใน PAD** ให้ใส่ใน fenced code block (` ```text `) เพื่อกด Copy บน GitHub/viewer ได้

| ใส่ fenced block | คงเป็น inline \`...\` ได้ |
|------------------|---------------------------|
| Path โฟลเดอร์/ไฟล์ (`C:\PAD-Labs\...`) | ชื่อตัวแปรตอนสร้าง (`WorkingRoot`) |
| URL ของ Lab Hub | ชื่อ Action ทางการ |
| ข้อความ Value ยาว / สูตร summary | ชื่อ UI element สั้น |
| เนื้อหาหลายบรรทัด (Notepad, email body) | คำอธิบายสั้น ๆ |
| Username/password demo ของ Lab | — |

รูปแบบที่แนะนำ:

````markdown
- Name: `WorkingRoot` ← **ไม่ใส่ `%`**
- Value: (คัดลอกด้านล่างวางในช่อง Value)

```text
C:\PAD-Labs\working\lab02
```
````

อย่าฝัง path ยาวไว้ในประโยคอย่างเดียวโดยไม่มี code block แยก — ผู้เรียนจะ copy พลาดช่องว่าง/เครื่องหมาย

---

## กติกาเขียน “Hands-on ทีละขั้น”

แต่ละ Step ต้องมีอย่างน้อย:

| องค์ประกอบ | ตัวอย่าง |
|------------|----------|
| หมายเลข Step | `### Step 3 — ดึงรายการไฟล์` |
| ชื่อ Action ทางการ | `Get files in folder` (ไม่แปลชื่อ) |
| ค่าที่ใส่ในช่อง (เมื่อ **ใช้** ตัวแปร) | Folder = `%WorkingRoot%\inbox` |
| ชื่อตัวแปรที่ **สร้าง/เปลี่ยนชื่อ** | Name / produced / Store into = `InboxFiles` (ไม่มี `%`) |
| ตำแหน่งใน workspace | “วางหลัง Step 2”, “ภายใน For each” |

รูปแบบประโยคที่แนะนำ:

```text
1. ใน Actions Pane ค้นหา **Get files in folder** แล้วลากลง workspace
2. ตั้งค่า:
   - Folder: `%WorkingRoot%\inbox`   ← ใช้ตัวแปร (มี %)
   - File filter: `*`
   - Include subfolders: ปิด
3. ชื่อ produced variable: `InboxFiles`  ← ไม่ใส่ %
   (เวลาอ้างอิงทีหลังใช้ `%InboxFiles%`)
4. กด Save ในหน้าต่าง action
```

## สิ่งที่ห้ามในส่วน Hands-on

- สรุปแบบ “ใช้ If ตามนามสกุลแล้ว Copy” โดยไม่บอกตัวแปรต้นทาง/ปลายทาง
- สลับ path hardcode กับ `%WorkingRoot%` โดยไม่บอกว่าอันไหนเป็นหลัก
- ใช้ชื่อ Action ที่ไม่ตรง [`OFFICIAL-TERMINOLOGY.md`](OFFICIAL-TERMINOLOGY.md)
- สั่งให้พิมพ์ `%` ในช่อง Name / Store into / ชื่อ produced

## สไตล์ภาษา

ตาม [`WRITING-STYLE.md`](WRITING-STYLE.md) — ไทยอ่านลื่น + คงชื่อ Action อังกฤษ
