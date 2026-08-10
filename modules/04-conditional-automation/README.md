# Lab 04 — Conditional Automation

**วัน:** 2 · **ระดับ:** Intermediate · **เวลาโดยประมาณ:** อ่านความรู้ 15–25 นาที + Lab 45–60 นาที  
**ทักษะ:** If / Else If / Else, เปรียบเทียบข้อความ/ตัวเลข, จัดไฟล์ตามกฎธุรกิจ

## ลำดับการเรียน (จับมือทำ)

| ขั้น | ไฟล์ | ทำอะไร |
|------|------|--------|
| 0 | [`shared/PAD-FUNDAMENTALS.md`](../../shared/PAD-FUNDAMENTALS.md) | พื้นฐาน PAD / กฎ `%` (ถ้ายังไม่คุ้น designer) |
| 1 | **[LESSON.md](LESSON.md)** | อ่านความรู้: ศัพท์ แนวคิด If/AND/OR |
| 2 | **[LAB.md](LAB.md)** | Setup + Hands-on ทีละขั้นใน designer |


## Reference script (catch-up)

สำหรับนักเรียนที่ทำตามไม่ทัน — เปิด [`scripts/04-conditional-automation.robin`](scripts/04-conditional-automation.robin) แล้ว copy วางใน desktop flow ว่าง

- full — วางใน flow ว่างได้เลย
- ไม่แทนการทำ LAB หลัก; ใช้เทียบลำดับ action / กู้งานให้ทันชั้น

## วัตถุประสงค์
- ใช้เงื่อนไขแยกเส้นทาง Flow
- จัดประเภทคำขอใน inbox ตาม Priority และ Status
- เขียน `routing-log.csv` ตาม expected routing

## Prerequisites

- PAD ติดตั้งแล้ว (แนะนำ baseline **2607+** — ดู [PAD version matrix](https://learn.microsoft.com/power-platform/released-versions/power-automate-desktop))
- ผ่าน Lab 02 (แนวคิดไฟล์) จะช่วยได้

## Assets / Output

| | Path |
|--|------|
| Inbox samples | [`assets/inbox/`](assets/inbox/) |
| Rules | [`assets/business-rules.md`](assets/business-rules.md) |
| Expected | [`assets/expected-routing.csv`](assets/expected-routing.csv) |
| Log | `C:\PAD-Labs\output\lab04\routing-log.csv` |

## บทที่เกี่ยวข้อง

- พื้นฐานไฟล์: [Lab 02 File Management](../02-file-management/README.md)
- ลูป batch ต่อ: [Lab 05 Looping](../05-looping-files-data/README.md)
- Excel / Data table: [Lab 06 Data Table & Excel](../06-data-table-excel/README.md)
