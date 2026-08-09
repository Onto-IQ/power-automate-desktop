# Shared resources

เอกสารกลางที่ใช้ร่วมหลาย Lab

| ไฟล์ | คำอธิบาย |
|------|----------|
| [PAD-FUNDAMENTALS.md](PAD-FUNDAMENTALS.md) | พื้นฐาน PAD สำหรับผู้เริ่มต้น (อ่านก่อน Lab แรก) |
| [PRECLASS-SETUP.md](PRECLASS-SETUP.md) | Checklist ติดตั้งก่อนวันเรียน (ผู้เรียน) |
| [CLASSROOM-SCHEDULE-12H.md](CLASSROOM-SCHEDULE-12H.md) | ตารางสอน 12 ชม. Core/Optional + หน้าที่ TA |
| [TA-CHEATSHEET.md](TA-CHEATSHEET.md) | อาการที่เจอบ่อยและวิธีแก้เร็วสำหรับ TA |
| [LESSON-TEMPLATE.md](LESSON-TEMPLATE.md) | แม่แบบ `LESSON.md` (ความรู้ 10 หัวข้อ) |
| [HANDS-ON-LAB-TEMPLATE.md](HANDS-ON-LAB-TEMPLATE.md) | แม่แบบ `LAB.md` (Hands-on ทีละขั้นใน designer) |
| [WRITING-STYLE.md](WRITING-STYLE.md) | สไตล์ภาษาไทย: ไม่ห้วนเกินไป และไม่แปล keyphrase |
| [SOURCES-AUG2026.md](SOURCES-AUG2026.md) | อ้างอิง official / blog / community เฉพาะสิงหาคม 2026 |
| [OFFICIAL-TERMINOLOGY.md](OFFICIAL-TERMINOLOGY.md) | ชื่อ Action / ศัพท์ตาม Microsoft Learn (Aug 2026) |
| [SELECTOR-CONVENTIONS.md](SELECTOR-CONVENTIONS.md) | CSS / data-pad / wait strategy สำหรับ PAD Lab Hub |
| [BEST-PRACTICES.md](BEST-PRACTICES.md) | Naming, variables, subflows, Outlook/Excel safety |
| [DATA-SCHEMAS.md](DATA-SCHEMAS.md) | Schema ของ mock leads / orders / scout / recipients |
| [WEB-HUB-REQUESTS.md](WEB-HUB-REQUESTS.md) | สถานะหน้า Lab Hub (รวม 19 Catalog) |
| [generate_mock_xlsx.py](generate_mock_xlsx.py) | สร้างไฟล์ `.xlsx` จาก CSV ใน Labs 06, 07, 08, 10 |

## โครงสร้างเอกสารต่อหนึ่ง Module

```text
modules/<module>/
  README.md   ← หน้าปก / สารบัญ
  LESSON.md   ← ความรู้ (อ่านก่อน)
  LAB.md      ← จับมือทำ
  assets/     ← ข้อมูลตัวอย่าง (ถ้ามี)
```

> รากโฟลเดอร์บทเรียน = `modules/` · ไฟล์แบบฝึกหัดยังชื่อ `LAB.md`

## Regenerating Excel mocks

จากราก repo:

```powershell
python shared\generate_mock_xlsx.py
```
