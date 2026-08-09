# Lab 01b — Calculator (ความรู้)

**หน้าปก:** [README.md](README.md) · **ลงมือทำ:** [LAB.md](LAB.md) · **พื้นฐานร่วม:** [`shared/PAD-FUNDAMENTALS.md`](../../shared/PAD-FUNDAMENTALS.md)

**วัน:** 1 · **ระดับ:** Beginner · **อ่านประมาณ:** 8–12 นาที · **Optional**

## 1. บทนี้เรียนอะไร / จบแล้วทำอะไรได้

เมื่อจบบทนี้ คุณจะ:

- Capture ปุ่ม Calculator ด้วย UI Picker แล้วตั้งชื่อสื่อความหมาย
- คลิก `7 + 8 =` ด้วย **Click UI element in window** / **Press button in window**
- อ่านค่าจาก display เป็น `%CalcResult%` แล้วใช้ **If** ตรวจว่ามี `15`
- ปิด Calculator ด้วย **Close window** (Terminate เป็นทางสำรอง)

## 2. เรื่องราวจากงานจริง

บางงานต้องกดเครื่องคิดเลขหรือแอปตัวเลขบน Windows เพื่อตรวจผลก่อนใส่รายงาน — ถ้าคลิกตามพิกัดจอ เมื่อย้ายหน้าต่างหรือเปลี่ยนโหมด Calculator flow จะพัง  
งานของบทนี้คือฝึกจับปุ่มและอ่าน display ให้ Replay ได้

## 3. ศัพท์ทีละคำ

| ศัพท์ | ความหมายภาษาคน | เห็นที่ไหนใน PAD |
|--------|----------------|------------------|
| **Click UI element in window** | คลิกตาม element ที่ capture ไว้ | ไม่ใช่พิกัด X,Y |
| **Get details of UI element in window** | อ่านข้อความ/attribute จาก control | เก็บเป็น `CalcResult` |
| **If** | แตกกิ่งตามเงื่อนไข | ตรวจว่าผลมี `15` |
| **Close window** / **Terminate process** | ปิดแอปอย่างสุภาพ / ฆ่า process | Close ก่อน |

## 4. แนวคิดหลัก

```mermaid
flowchart TD
  runC[Run application Calculator]
  waitC[Wait for window content]
  click[Click 7 + 8 =]
  read[อ่าน Txt_CalcDisplay → CalcResult]
  check{Contains 15?}
  closeC[Close window]
  runC --> waitC --> click --> read --> check --> closeC
```

Pseudo-flow:

```text
Run Calculator → Wait
Click Btn_Seven, Btn_Plus, Btn_Eight, Btn_Equals
อ่าน display → CalcResult ต้องมี 15 → Close
```

## 5. ตาราง Action ที่จะใช้

| Action (official) | ทำอะไร | Input สำคัญ | **Variables produced** |
|-------------------|--------|-------------|------------------------|
| **Run application** | เปิด Calculator | Application path เช่น `calc` | ตาม designer |
| **Wait for window content** | รอหน้าต่างพร้อม | หน้าต่าง / element | — |
| **Click UI element in window** / **Press button in window** | คลิกปุ่ม | UI element | — |
| **Get details of UI element in window** (หรือเทียบเท่า) | อ่าน display | UI element | `CalcResult` |
| **If** | ตรวจผล | เงื่อนไข Contains / Equal | — |
| **Close window** | ปิดหน้าต่าง | หน้าต่าง Calculator | — |
| **Terminate process** | สำรองถ้า Close ไม่สำเร็จ | Process name | — |

## 6. เปรียบเทียบตัวเลือกที่มักสับสน

| หัวข้อ | ตัวเลือก A | ตัวเลือก B | เลือกเมื่อไหร่ |
|--------|------------|------------|----------------|
| คลิกปุ่ม | **UI Element** | พิกัด X,Y | ใช้ UI Element เป็นหลัก |
| ตรวจผล | อ่าน `%CalcResult%` แล้ว **If** | ดูด้วยตาอย่างเดียว | Acceptance บังคับอ่านจาก display |
| ปิดแอป | **Close window** | **Terminate process** | Close ก่อน |

## 7. จุดที่มือใหม่พลาดบ่อย

| อาการ | สาเหตุที่พบบ่อย | วิธีสังเกต |
|-------|-----------------|------------|
| Selector หลุด | โหมดเครื่องคิดเลขไม่ใช่ Standard | Recapture หลังสลับโหมด |
| ได้ 15 แต่เกณฑ์ไม่ผ่าน | ไม่อ่านจาก display | ไม่มี `%CalcResult%` |
| Replay เปิดแอปซ้อน | ไม่ Close ก่อนรอบใหม่ | มีหลาย Calculator |

## 8. คำถามทบทวน

**1.** หลังคลิก 7+8= ต้องทำอะไรเพื่อผ่าน Acceptance?

<details>
<summary>เฉลย</summary>
อ่านค่าจาก display เก็บเป็น <code>CalcResult</code> แล้วใช้ <strong>If</strong> ตรวจว่ามี <code>15</code> — ไม่พอแค่ดูผลบนจอ
</details>

**2.** ทำไมไม่ควรใช้พิกัดจอคลิกปุ่ม Calculator?

<details>
<summary>เฉลย</summary>
ตำแหน่งปุ่มเปลี่ยนตามขนาดหน้าต่าง โหมด และ DPI — ใช้ UI Element ที่จับปุ่มจริงจะเสถียรกว่า
</details>

## 9. อ้างอิง (Aug 2026)

| แหล่ง | URL |
|-------|-----|
| UI automation actions | https://learn.microsoft.com/power-automate/desktop-flows/actions-reference/uiautomation |
| UIPI troubleshooting | https://learn.microsoft.com/troubleshoot/power-platform/power-automate/desktop-flows/ui-automation/uipi-issues |

---

**ถัดไป:** เปิด [LAB.md](LAB.md) · กลับไป Core: [Lab 01b Notepad](../01b-notepad/README.md)
