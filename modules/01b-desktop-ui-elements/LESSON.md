# Lab 01b — Desktop UI Elements (ความรู้)

**หน้าปก:** [README.md](README.md) · **ลงมือทำ:** [LAB.md](LAB.md) · **พื้นฐานร่วม:** [`shared/PAD-FUNDAMENTALS.md`](../../shared/PAD-FUNDAMENTALS.md)

**วัน:** 1 · **ระดับ:** Beginner · **อ่านประมาณ:** 15–25 นาที

## 1. บทนี้เรียนอะไร / จบแล้วทำอะไรได้

เมื่อจบบทนี้ คุณจะ:

- อธิบายได้ว่าทำไมต้องใช้ **UI Elements** / selector แทนการคลิกด้วยพิกัดจอ (X,Y)
- เปิด โฟกัส และปิดแอป Windows ด้วย **Run application**, **Wait for window content** / **Focus window**, **Close window**
- Capture element ด้วย UI Picker (**Ctrl + Left Click**) แล้ว **Test** ใน Selector Builder
- สร้าง flow Notepad (Populate + Save) และ Calculator (คลิก 7+8= แล้วอ่าน display เป็น 15)
- เข้าใจกฎ `%` ตอนสร้างชื่อตัวแปร vs ตอนอ้างอิงค่า

## 2. เรื่องราวจากงานจริง

หลายงานบนเครื่อง Windows ไม่ได้อยู่บนเว็บ — เช่น พิมพ์บันทึกใน Notepad แล้วเซฟไฟล์ หรือกดเครื่องคิดเลขเพื่อตรวจตัวเลขก่อนใส่รายงาน  
ถ้าคลิกตามพิกัดจอ เมื่อย้ายหน้าต่างหรือเปลี่ยนความละเอียด flow จะพัง งานของบทนี้คือฝึกจับ **UI Elements** บน Notepad และ Calculator ให้ Replay ได้ โดยไม่พึ่ง Lab Hub

## 3. ศัพท์ทีละคำ

| ศัพท์ | ความหมายภาษาคน | เห็นที่ไหนใน PAD |
|--------|----------------|------------------|
| **UI Element** | ตัวแทนของปุ่ม/ช่องบนหน้าต่างแอป | แผง **UI Elements** |
| **UI Picker** | เครื่องมือชี้ element บนจอ | Add element → **Ctrl + Left Click** |
| **Selector Builder** | หน้าต่างดู/ทดสอบ attribute ของ element | **Test** / Validate |
| **Run application** | สั่งเปิดโปรแกรมจาก path | Actions → System |
| **Focus window** | ดึงหน้าต่างมาอยู่ด้านหน้า | UI / Window actions |
| **Populate text field in window** | พิมพ์ข้อความลงช่องของแอป Windows | ต่างจาก Populate บนเว็บ |
| **Click UI element in window** | คลิกตาม element ที่ capture ไว้ | ไม่ใช่พิกัด X,Y |
| **UIPI** | ข้อจำกัดสิทธิ์ที่อาจบล็อก UI automation | เอกสาร troubleshooting ของ Microsoft |

## 4. แนวคิดหลัก

แนวคิดสำคัญ: **Capture element ที่เสถียร → Wait/Focus → Interact → Close**  
แยกชัด Web UI (Lab 01) กับ Desktop UI (Lab นี้) — ชื่อ action คนละกลุ่ม

```mermaid
flowchart TD
  vars[Set NotepadPath OutFile NoteText]
  runN[Run application Notepad]
  waitN[Wait / Focus window]
  pop[Populate Edit_NotepadBody]
  save[Send keys Ctrl+S + Save As]
  closeN[Close window Notepad]
  runC[Run application Calculator]
  click[Click 7 + 8 =]
  read[อ่าน Txt_CalcDisplay → CalcResult]
  check{Contains 15?}
  closeC[Close window Calculator]
  vars --> runN --> waitN --> pop --> save --> closeN
  closeN --> runC --> click --> read --> check --> closeC
```

Pseudo-flow:

```text
NotepadPath = C:\Windows\System32\notepad.exe
OutFile = C:\PAD-Labs\output\lab01b\notepad-output.txt
NoteText = เนื้อหาจาก notepad-message.txt
Run Notepad → Wait/Focus → Populate %NoteText% → Save As %OutFile% → Close
Run Calculator → Click Btn_Seven, Plus, Eight, Equals
อ่าน display → CalcResult ต้องมี 15 → Close
```

## 5. ตาราง Action ที่จะใช้

| Action (official) | ทำอะไร | Input สำคัญ | Produced (ชื่อตอนสร้าง — ไม่มี `%`) |
|-------------------|--------|-------------|--------------------------------------|
| **Set variable** | ตั้ง path / ข้อความ | Name, Value | — |
| **Run application** | เปิด Notepad / Calculator | Application path | ตามที่ designer มี |
| **Wait for window content** | รอเนื้อหาหน้าต่าง | หน้าต่าง / element | — |
| **Focus window** | โฟกัสหน้าต่าง | หน้าต่างเป้าหมาย | — |
| **Populate text field in window** | พิมพ์ลงช่อง | UI element, Text | — |
| **Send keys** | ส่งคีย์ลัด เช่น Ctrl+S | Keys, หน้าต่าง | — |
| **Click UI element in window** / **Press button in window** | คลิกปุ่ม | UI element | — |
| **Get details of UI element in window** (หรือเทียบเท่า) | อ่านข้อความจาก display | UI element | `CalcResult` |
| **If** | ตรวจผล Calculator | เงื่อนไข | — |
| **Close window** | ปิดหน้าต่างแอป | หน้าต่าง | — |
| **Terminate process** | ฆ่า process (สำรอง) | Process name | — |

## 6. เปรียบเทียบตัวเลือกที่มักสับสน

| หัวข้อ | ตัวเลือก A | ตัวเลือก B | เลือกเมื่อไหร่ |
|--------|------------|------------|----------------|
| เป้าหมายคลิก | **UI Element** | พิกัด X,Y | ใช้ UI Element เป็นหลัก |
| กรอกข้อความ | **Populate text field in window** | **Populate text field on web page** | in window = แอป Windows; on web page = เว็บ |
| ปิดแอป | **Close window** | **Terminate process** | Close ก่อน; Terminate เป็นทางสำรอง |
| ตรวจผล Calculator | อ่าน `%CalcResult%` แล้ว **If** | ดูด้วยตาอย่างเดียว | Acceptance บังคับอ่านจาก display |
| จัดโครง flow | Main ทั้งก้อน | Subflow `SF_Notepad` / `SF_Calculator` | Challenge แนะนำแยก Subflow |

## 7. กฎ `%` และ Variables pane

- ช่อง **Name** / ชื่อ produced → พิมพ์ `NoteText`, `OutFile`, `CalcResult` (**ไม่มี `%`**)
- ช่อง Application path / Text to fill-in → `%NotepadPath%`, `%NoteText%`, `%OutFile%` (**มี `%`**)
- รายละเอียดเต็ม: [`shared/PAD-FUNDAMENTALS.md`](../../shared/PAD-FUNDAMENTALS.md)

## 8. จุดที่มือใหม่พลาดบ่อย

| อาการ | สาเหตุที่พบบ่อย | วิธีสังเกต |
|-------|-----------------|------------|
| พิมพ์ไม่เข้า Notepad | ยังไม่ Focus / Wait | หน้าต่างอยู่ด้านหลัง |
| Save As ไม่ครบ | ลืม capture ช่อง path / ปุ่ม Yes | dialog ค้างตอนรัน |
| Calculator selector หลุด | โหมดเครื่องคิดเลขเปลี่ยน / พิกัดจอ | Recapture หลัง Standard mode |
| ได้ 15 แต่เกณฑ์ไม่ผ่าน | ไม่อ่านจาก display | ไม่มี `%CalcResult%` ใน Variables |
| Replay เปิดแอปซ้อน | ไม่ Close ก่อนรอบใหม่ | มีหลาย Notepad/Calculator |

## 9. คำถามทบทวน

**1.** ทำไมไม่ควรคลิกด้วยพิกัดจอเป็นหลัก?

<details>
<summary>เฉลย</summary>
เมื่อย้ายหน้าต่าง เปลี่ยนความละเอียด หรือ DPI ตำแหน่ง X,Y จะเพี้ยน — ใช้ <strong>UI Elements</strong> ที่ผูกกับ control จริงจะเสถียรกว่า
</details>

**2.** ใน UI Picker ใช้ปุ่มลัดอะไรจับ element?

<details>
<summary>เฉลย</summary>
<strong>Ctrl + Left Click</strong> แล้วตั้งชื่อสื่อความหมาย เช่น <code>Edit_NotepadBody</code>, <code>Btn_Seven</code>
</details>

**3.** Populate ของ Lab นี้ต่างจาก Lab 01 อย่างไร?

<details>
<summary>เฉลย</summary>
Lab นี้ใช้ <strong>Populate text field in window</strong> (แอป Windows) ส่วน Lab 01 ใช้ <strong>Populate text field on web page</strong>
</details>

**4.** หลังคลิก 7+8= ต้องทำอะไรเพื่อผ่าน Acceptance?

<details>
<summary>เฉลย</summary>
อ่านค่าจาก display เก็บเป็น <code>CalcResult</code> แล้วใช้ <strong>If</strong> ตรวจว่ามี <code>15</code> — ไม่พอแค่ดูผลบนจอ
</details>

**5.** ช่อง Name ของ Set variable ใส่ `%NoteText%` ได้หรือไม่?

<details>
<summary>เฉลย</summary>
ไม่ได้ — ตอนสร้างชื่อพิมพ์ <code>NoteText</code> ไม่มี <code>%</code>; ตอนอ้างอิงใน Text to fill-in ใช้ <code>%NoteText%</code>
</details>

## 10. อ้างอิง (Aug 2026)

| แหล่ง | URL |
|-------|-----|
| UI automation actions | https://learn.microsoft.com/power-automate/desktop-flows/actions-reference/uiautomation |
| System actions | https://learn.microsoft.com/power-automate/desktop-flows/actions-reference/system |
| UIPI troubleshooting | https://learn.microsoft.com/troubleshoot/power-platform/power-automate/desktop-flows/ui-automation/uipi-issues |
| รายการแหล่งใน Lab Kit | [`shared/SOURCES-AUG2026.md`](../../shared/SOURCES-AUG2026.md) |

---

**ถัดไป:** เปิด [LAB.md](LAB.md) แล้วทำ Hands-on ทีละขั้น
