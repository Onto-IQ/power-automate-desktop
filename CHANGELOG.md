# Changelog

บันทึกเวอร์ชันของ **Power Automate Desktop Lab Kit**  
GitHub Releases: https://github.com/Onto-IQ/power-automate-desktop/releases

รูปแบบเวอร์ชัน: SemVer (`MAJOR.MINOR.PATCH`)  
PAD baseline ของชุดเอกสาร: **2607+** (สิงหาคม 2026)

---

## [Unreleased]

### Module เฉพาะกิจ
- เพิ่ม `modules/scb-secure-isolation-alt/` สำหรับห้องที่ Browser Secure Isolation กั้น Lab Hub — ใช้เฉพาะ `bot.or.th` / `scb.co.th` ทดแทน Lab 01 + Lab 03 Core (Form Search · Static FX Table · AJAX FX Rates)

---

## [1.1.0] — 2026-08-09

ปรับ Lab ให้สอนในห้องได้ลื่นขึ้นหลังรอบ polish หลัง `v1.0.0` (ผู้เรียน clone จาก `main` / tag `v1.1.0`)

### โครงสร้างบทเรียน
- แยก Lab 01b เป็นโมดูลแยก: `01b-notepad` (Core) และ `01b-calculator` (Optional)
- แยก Lab 03 เป็น flow ย่อยใต้ `03-web-scout/` (Static / AJAX / Catalog / Controls / Files)

### Lab 01–02
- Lab 01 กรอกฟอร์มครบทุกช่อง + เตือน Autofill ที่ขัด Recorder
- Lab 01b: Wait เป็นหลัก / Focus สำรอง · Simulate action · ปิดหน้าต่างด้วย selector ที่เสถียร
- Lab 02: รูปแบบ If folder Doesn't exist, For each/If ชัดขึ้น, summary path แบบ dynamic

### Lab 03 Web Scout
- Static Table: Wait ชี้ `#tbl-employees` และขั้นตอน Extract สอดคล้อง PAD UI
- AJAX Table: Wait แถว, กรองด้วยคอลัมน์, Insert row / CSV export (`CsvLine` → Overwrite/Append)
- Catalog (optional): Loop condition + หยุดเมื่อ Next ปิด, ส่งออก CSV ด้วย Write text to file

### ความสอดคล้องกับ PAD UI
- ใช้คำว่า **Variables produced** ตาม UI จริง
- จัด syntax รายการ Insert row / data-row ให้คัดลอกวางได้โดยไม่ซ้อน `%`

---

## [1.0.0] — 2026-08-09

Release แรกที่พร้อมใช้สอนในห้อง (ผู้เรียน clone จาก `main` / tag `v1.0.0`)

### โครงสร้างหลักสูตร
- แยกแต่ละบทเป็น `README.md` (หน้าปก) + `LESSON.md` (ความรู้) + `LAB.md` (จับมือทำ)
- โฟลเดอร์บทเรียนใช้ชื่อ `modules/` (เดิม `labs/`)
- ค่าที่ต้องวางใน PAD อยู่ในบล็อก ` ```text ` เพื่อคัดลอกง่าย

### เอกสารผู้เรียน (`shared/`)
- พื้นฐาน PAD และกฎตัวแปร `%` (`PAD-FUNDAMENTALS.md`)
- Checklist ก่อนเรียน (`PRECLASS-SETUP.md`)
- ตารางสอน 12 ชม. Core / Optional (`CLASSROOM-SCHEDULE-12H.md`)
- คำศัพท์ทางการ, selector Lab Hub, best practices, data schemas

### เอกสารทีม (local — ไม่ขึ้น GitHub)
- `authoring/` — แม่แบบ LESSON/LAB, สไตล์ภาษา, รายการอ้างอิง Aug 2026
- `ops/` — TA cheat sheet, สถานะ Lab Hub, โน้ตเซิร์ฟเวอร์
- `slides/` — PPTX / PDF outline

### การจัดส่งในห้อง
- แผน Core 12 ชม. สำหรับ ~30 คน + วิทยากร 1 + TA 2
- วัน 2 เลือกเส้น Contoso (07) หรือ Web+Error (08/09) ในห้อง

### อ้างอิง PAD
- จัดเนื้อหาให้สอดคล้อง Power Automate for desktop ช่วงสิงหาคม 2026 (baseline **2607+**)
- เวอร์ชัน PAD อย่างเป็นทางการ: [released-versions](https://learn.microsoft.com/power-platform/released-versions/power-automate-desktop)

---

## ลิงก์ที่เกี่ยวข้อง

| รายการ | URL |
|--------|-----|
| แท็กนี้ | https://github.com/Onto-IQ/power-automate-desktop/releases/tag/v1.1.0 |
| Lab Hub | https://ontoiq.tech/pad/ |
| PAD version matrix | https://learn.microsoft.com/power-platform/released-versions/power-automate-desktop |
