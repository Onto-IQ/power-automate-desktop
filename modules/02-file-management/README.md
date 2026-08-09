# Lab 02 — File Management

**วัน:** 1 · **ระดับ:** Beginner · **เวลาโดยประมาณ:** อ่านความรู้ 15–25 นาที + Lab 45–60 นาที  
**ทักษะ:** Folder/File actions, Get files, For each, Copy/Move, Read/Write text

## ลำดับการเรียน (จับมือทำ)

| ขั้น | ไฟล์ | ทำอะไร |
|------|------|--------|
| 0 | [`shared/PAD-FUNDAMENTALS.md`](../../shared/PAD-FUNDAMENTALS.md) | พื้นฐาน PAD / กฎ `%` (ถ้ายังไม่คุ้น designer) |
| 1 | **[LESSON.md](LESSON.md)** | อ่านความรู้: ศัพท์ แนวคิด Action ที่ใช้ |
| 2 | **[LAB.md](LAB.md)** | Setup + Hands-on ทีละขั้นใน designer |

## วัตถุประสงค์

- สร้างโครงสร้างโฟลเดอร์ด้วย PAD
- คัดลอกไฟล์ตามนามสกุลด้วย **For each** (ทีละไฟล์ ไม่ทั้งลิสต์)
- เขียน `summary.txt` สรุปจำนวนไฟล์

## Prerequisites

- PAD ติดตั้งแล้ว (แนะนำ baseline **2607+** — ดู [PAD version matrix](https://learn.microsoft.com/power-platform/released-versions/power-automate-desktop))
- ไม่จำเป็นต้องใช้ Web UI

## Assets / Output

| | Path |
|--|------|
| Mock inbox | [`assets/inbox/`](assets/inbox/) |
| Expected mapping | [`assets/expected/expected-manifest.csv`](assets/expected/expected-manifest.csv) |
| ภาพอ้างอิงลูป If/Copy | [`assets/reference-loop-if-copy.png`](assets/reference-loop-if-copy.png) |
| Output summary | `C:\PAD-Labs\output\lab02\summary.txt` |

## บทที่เกี่ยวข้อง

- พื้นฐานก่อนหน้า: [Lab 01 Record & Replay](../01-record-replay/README.md)
- ใช้แนวคิดไฟล์ต่อ: [Lab 04 Conditional](../04-conditional-automation/README.md) · [Lab 05 Looping](../05-looping-files-data/README.md)
