# ตารางสอน 12 ชั่วโมง (Core) — คน ~30 · วิทยากร 1 + TA 2

ใช้เมื่อสอนหลักสูตร PAD 2 วัน (6+6 ชม.)  
เป้า: **ตรงเวลา** โดยแยก **Core ในห้อง** กับ **Optional / Challenge บ้าน**

อ่านคู่กับ: [`PRECLASS-SETUP.md`](PRECLASS-SETUP.md) · [`PAD-FUNDAMENTALS.md`](PAD-FUNDAMENTALS.md)

## หลักการคุมเวลา

1. **Demo แล้วค่อยทำ** — วิทยากร demo 8–12 นาที แล้วให้ทำตาม `LAB.md`  
2. **Core ผ่านก่อน Challenge** — ห้ามล้ำ Challenge จนเพื่อนรอ  
3. **ติดเกิน 3 นาที → ยกมือเรียก TA** — อย่าให้ทั้งห้องหยุด  
4. Lab 07 กับ 08 **เลือกเส้นหนึ่งในห้อง** (อีกเส้น = บ้าน/โบนัส)  
5. Capstone ในห้อง = **เวอร์ชันย่อ** ตามตารางด้านล่าง

## หน้าที่ในห้อง

| บทบาท | รับผิดชอบ |
|--------|-----------|
| **วิทยากร** | Demo หน้าห้อง, จังหวะเวลา, Contoso/Capstone, คนติดหนัก |
| **TA1** | โต๊ะ/โซน A (ประมาณคนที่ 1–15) · ติดตั้ง · File labs (02, 04, 05) |
| **TA2** | โต๊ะ/โซน B (ประมาณคนที่ 16–30) · Browser extension · Web labs (01, 03, 08) |

## Core vs Optional (ประกาศเช้าวัน 1)

| รหัส | ในห้อง (Core) | Optional / บ้าน |
|------|----------------|-----------------|
| 01 | บังคับ | Challenge แถวที่ 2 |
| 01b | Notepad (`Lab01b_Notepad`) | Calculator แยก flow (`Lab01b_Calculator`) |
| 02 | บังคับครบ | Delete inbox หลัง Copy |
| 03 | Mission A + C | B, D, P, E–H |
| 04 | บังคับ | — |
| 05 | บังคับ | Do until challenge |
| 06 | อ่าน/กรอง/เขียน Excel | Macro FormatSummary |
| 07 **หรือ** 08 | **เลือกหนึ่ง** ในห้อง | อีกตัวทำบ้าน |
| 09 | ย่อ: Case A + C + E | Case อื่น / Challenge |
| 10 | ย่อ: scout 1 แหล่ง + สรุป Excel + Outlook **Draft** | Pagination / OCR / API / Contoso cross |

---

## วัน 1 — Fundamentals (~6 ชั่วโมง)

| เวลา (ตัวอย่าง) | นาที | บล็อก | เอกสาร | หมายเหตุ |
|-----------------|------|--------|--------|----------|
| 09:00–09:15 | 15 | เปิดคอร์ส + กติกาห้อง + Core/Optional | ไฟล์นี้ | แจ้งโซน TA |
| 09:15–09:45 | 30 | Fundamentals + ตรวจพรีคลาส | [`PAD-FUNDAMENTALS.md`](PAD-FUNDAMENTALS.md) · [`PRECLASS-SETUP.md`](PRECLASS-SETUP.md) | คนที่ยังไม่ติดตั้ง → TA ช่วยทันที |
| 09:45–10:35 | 50 | Lab 01 Record & Replay | [`modules/01-record-replay/`](../modules/01-record-replay/) | Demo 10 + ทำ 40 |
| 10:35–10:45 | 10 | พักสั้น | — | |
| 10:45–11:25 | 40 | Lab 01b Notepad | [`modules/01b-notepad/`](../modules/01b-notepad/) | Calculator optional: [`01b-calculator`](../modules/01b-calculator/) |
| 11:25–12:15 | 50 | Lab 02 File Management | [`modules/02-file-management/`](../modules/02-file-management/) | เน้นกฎ `%` |
| 12:15–13:15 | 60 | พักกลางวัน | — | |
| 13:15–14:15 | 60 | Lab 03 Web Scout (A + C) | [`modules/03-web-scout/`](../modules/03-web-scout/) | ตัด Challenge ในห้อง |
| 14:15–14:45 | 30 | บัฟเฟอร์ช่วยเหลือ + ทบทวนวัน 1 | คู่มือ TA บนเครื่องทีม (`ops/TA-CHEATSHEET.md`) | จบเมื่อ Core 01/02/03A+C ผ่าน |

**เกณฑ์ผ่านวัน 1:** Flow 01 รันซ้ำได้ · Lab 02 มี summary ถูก · Lab 03 extract ได้อย่างน้อย 1 ตาราง (+ AJAX มี Wait)

---

## วัน 2 — Logic + เส้นทาง + Capstone ย่อ (~6 ชั่วโมง)

| เวลา (ตัวอย่าง) | นาที | บล็อก | เอกสาร | หมายเหตุ |
|-----------------|------|--------|--------|----------|
| 09:00–09:10 | 10 | ทบทวน `%` / For each / If | — | Quick quiz ปากเปล่าได้ |
| 09:10–10:20 | 70 | Lab 04 + 05 | [`04`](../modules/04-conditional-automation/) · [`05`](../modules/05-looping-files-data/) | Demo รวม 15 แล้วทำต่อเนื่อง |
| 10:20–10:30 | 10 | พักสั้น | — | |
| 10:30–11:20 | 50 | Lab 06 Excel (ไม่บังคับ macro) | [`modules/06-data-table-excel/`](../modules/06-data-table-excel/) | Mission M = บ้าน |
| 11:20–12:50 | 90 | **เส้นทาง A:** Lab 07 Contoso **หรือ** **เส้นทาง B:** Lab 08 + Lab 09 ย่อ | [`07`](../modules/07-contoso-invoice-ops/) · [`08`](../modules/08-excel-web-roundtrip/) · [`09`](../modules/09-error-handling/) | ห้องเลือกเส้นเดียวกันทั้งรุ่น (วิทยากรตัดสินใจก่อนวันสอน) |
| 12:50–13:50 | 60 | พักกลางวัน | — | |
| 13:50–15:10 | 80 | Capstone 10 ย่อ | [`modules/10-capstone-sales-ops/`](../modules/10-capstone-sales-ops/) | Scout 1 แหล่ง + Excel สรุป + Outlook DraftOnly |
| 15:10–15:30 | 20 | สรุป Best Practices + Q&A + ส่งงาน | [`BEST-PRACTICES.md`](BEST-PRACTICES.md) | |

### คำแนะนำเลือกเส้นทางวัน 2

| เส้น | เหมาะเมื่อ | ในห้องทำ |
|------|------------|----------|
| **A — Contoso (07)** | เน้น Desktop UI / ใกล้สไลด์ Trainocate | Lab 07 Core (R1–R4 อย่างน้อย) |
| **B — Web + Error (08+09)** | เน้น Lab Hub / ไม่ติดตั้ง Contoso | Lab 08 Login+Forms · Lab 09 Case A+C+E |

อย่าบังคับ A+B เต็มใน 90 นาทีเดียวกัน

**เกณฑ์ผ่านวัน 2:** 04+05 ถูก · 06 มี sheet ผล · เส้นทางที่เลือกผ่านเกณฑ์ย่อ · Capstone มีรายงาน + Draft (หรือหลักฐาน Draft)

---

## สัญญาณสี (วิทยากรใช้คุมจังหวะ)

| สัญญาณ | ความหมาย |
|--------|----------|
| เหลือง | เหลือ 10 นาทีในบล็อก — TA ช่วยเฉพาะคนที่ยังไม่ผ่าน Core |
| แดง | หมดเวลาบล็อก — เก็บ Challenge เป็นบ้าน ไปหัวข้อถัดไป |
| เขียว | ส่วน 70%+ ผ่าน Core ของบล็อก — ไปต่อได้ |

## สิ่งที่ห้ามในห้อง (ลดงาน)

- อย่าไล่ทำ Challenge ทุก Mission ของ Lab 03/08/09/10 ในเวลาคอร์ส  
- อย่าให้ทั้งห้องรอคนที่ยังติดตั้งไม่เสร็จเกิน 15 นาทีเช้าวัน 1 — แยกคลื่นกับ TA  
- อย่าเปิด Outlook ส่งจริง — **DraftOnly** เท่านั้น  

## Checklist วิทยากรก่อนเปิดคอร์ส

- [ ] แจก [`PRECLASS-SETUP.md`](PRECLASS-SETUP.md) อย่างน้อย 2–3 วันล่วงหน้า  
- [ ] ตัดสินใจเส้นทางวัน 2 (A หรือ B)  
- [ ] ทดสอบ Lab Hub + (ถ้าเส้น A) Contoso บนเครื่อง demo  
- [ ] แบ่งโซนโต๊ะให้ TA1 / TA2  
- [ ] ทีมสอนเปิด `ops/TA-CHEATSHEET.md` (local) ให้ TA
