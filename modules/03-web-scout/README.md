# Lab 03 — Web Scout

**วัน:** 1 · **ระดับ:** Intermediate · **เวลาโดยประมาณ:** อ่านความรู้ 20–30 นาที + Lab 60–90 นาที  
**ทักษะ:** Launch browser, Extract HTML table, Controls, Wait for AJAX, Files download/upload, บันทึกผลลงไฟล์

## ลำดับการเรียน (จับมือทำ)

| ขั้น | ไฟล์ | ทำอะไร |
|------|------|--------|
| 0 | [`shared/PAD-FUNDAMENTALS.md`](../../shared/PAD-FUNDAMENTALS.md) | พื้นฐาน PAD / กฎ `%` (ถ้ายังไม่คุ้น designer) |
| 1 | **[LESSON.md](LESSON.md)** | อ่านความรู้: Scout missions, Extract, AJAX, catalog loop |
| 2 | **[LAB.md](LAB.md)** | Setup + Hands-on Mission A–D / P ใน designer |

## วัตถุประสงค์

- ทำ **Web Scout** แบบสนุก: เก็บข้อมูลจากหลายหน้าบน PAD Lab Hub
- Extract ตาราง static และรอตาราง dynamic (AJAX)
- ส่งออกผลเป็น CSV

## Prerequisites

- PAD + browser extension (แนะนำ baseline **2607+** — ดู [PAD version matrix](https://learn.microsoft.com/power-platform/released-versions/power-automate-desktop))
- อ่าน [`shared/SELECTOR-CONVENTIONS.md`](../../shared/SELECTOR-CONVENTIONS.md)

## Assets / Output

| | Path |
|--|------|
| Criteria | [`assets/scout-criteria.csv`](assets/scout-criteria.csv) |
| Upload mock | [`assets/upload-sample.txt`](assets/upload-sample.txt) |
| Scout brief | [`assets/scout-brief.md`](assets/scout-brief.md) |
| Output template | [`assets/scout-results-template.csv`](assets/scout-results-template.csv) |
| Expected shape | [`assets/expected-scout-results.csv`](assets/expected-scout-results.csv) |
| Your output | `C:\PAD-Labs\output\lab03\scout-results.csv` |
| Downloads | `C:\PAD-Labs\output\lab03\downloads\` |

## บทที่เกี่ยวข้อง

- พื้นฐานเว็บก่อนหน้า: [Lab 01 Record & Replay](../01-record-replay/README.md)
- ใช้แนวคิดไฟล์: [Lab 02 File Management](../02-file-management/README.md)
