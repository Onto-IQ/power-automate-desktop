# Lab 01 — Record & Replay

**วัน:** 1 · **ระดับ:** Beginner · **เวลาโดยประมาณ:** อ่านความรู้ 15–25 นาที + Lab 45–60 นาที  
**ทักษะ:** Desktop/Web Recorder, การกรอกฟอร์ม, Submit และ Variables พื้นฐาน

## ลำดับการเรียน (จับมือทำ)

| ขั้น | ไฟล์ | ทำอะไร |
|------|------|--------|
| 0 | [`shared/PAD-FUNDAMENTALS.md`](../../shared/PAD-FUNDAMENTALS.md) | พื้นฐาน PAD / กฎ `%` (ถ้ายังไม่คุ้น designer) |
| 1 | **[LESSON.md](LESSON.md)** | อ่านความรู้: Recorder, UI Elements, Web actions |
| 2 | **[LAB.md](LAB.md)** | Setup + Hands-on ทีละขั้นใน designer |

## วัตถุประสงค์

- ใช้ **Recorder** สร้าง flow สำหรับกรอกฟอร์มบนเว็บ
- ตรวจและปรับ **UI Elements** หลัง Record ให้ selector เสถียรขึ้น
- Replay flow ให้ได้ผลลัพธ์ซ้ำกันได้อย่างน่าเชื่อถือ

## Prerequisites

- ติดตั้ง PAD พร้อม browser extension แล้ว (แนะนำ baseline **2607+** — ดู [`shared/SOURCES-AUG2026.md`](../../shared/SOURCES-AUG2026.md))
- เข้าถึงหน้า [01 Forms](https://ontoiq.tech/pad/01-forms.html) ได้

## Assets / Output

| | Path / ค่า |
|--|------------|
| Input mock | [`assets/sample-form-input.csv`](assets/sample-form-input.csv) |
| Web UI | https://ontoiq.tech/pad/01-forms.html |
| Screenshot (ทางเลือก) | `C:\PAD-Labs\output\lab01\submit-proof.png` |

## บทที่เกี่ยวข้อง

- Desktop UI พื้นฐาน (Notepad/Calculator): [Lab 01b](../01b-desktop-ui-elements/README.md)
- Desktop Element UI เต็มรูปแบบ (วัน 2): [Lab 07 Contoso Invoice Ops](../07-contoso-invoice-ops/README.md)
