# Lab 05 — Looping Files / Data

**วัน:** 2 · **ระดับ:** Intermediate · **เวลาโดยประมาณ:** อ่านความรู้ 15–25 นาที + Lab 50–70 นาที  
**ทักษะ:** For each, Loop index, รวมผลจากหลายไฟล์, Do until (challenge)

## ลำดับการเรียน (จับมือทำ)

| ขั้น | ไฟล์ | ทำอะไร |
|------|------|--------|
| 0 | [`shared/PAD-FUNDAMENTALS.md`](../../shared/PAD-FUNDAMENTALS.md) | พื้นฐาน PAD / กฎ `%` (ถ้ายังไม่คุ้น designer) |
| 1 | **[LESSON.md](LESSON.md)** | อ่านความรู้: ลูปซ้อน Data table รวมยอด |
| 2 | **[LAB.md](LAB.md)** | Setup + Hands-on ทีละขั้นใน designer |

## วัตถุประสงค์

- ประมวลผลไฟล์เป็นชุด (batch)
- รวมยอด Amount จากหลาย CSV
- เขียนรายงานสรุปเดียว (`batch-summary.csv`, Grand total 46500)

## Prerequisites

- PAD ติดตั้งแล้ว (แนะนำ baseline **2607+** — ดู [PAD version matrix](https://learn.microsoft.com/power-platform/released-versions/power-automate-desktop))
- คุ้นกับ **Get files in folder** / **For each** จาก Lab 02 จะช่วยได้

## Assets / Output

| | Path |
|--|------|
| Batch files | [`assets/batch/`](assets/batch/) |
| Expected summary | [`assets/expected-batch-summary.csv`](assets/expected-batch-summary.csv) |
| Processed marker folder | `C:\PAD-Labs\working\lab05\processed\` |
| Your output | `C:\PAD-Labs\output\lab05\batch-summary.csv` |

## บทที่เกี่ยวข้อง

- พื้นฐานไฟล์: [Lab 02 File Management](../02-file-management/README.md)
- เงื่อนไขก่อนหน้า: [Lab 04 Conditional](../04-conditional-automation/README.md)
- Excel / Data table: [Lab 06 Data Table & Excel](../06-data-table-excel/README.md)
