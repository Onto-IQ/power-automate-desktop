# Lab 09 — Error Handling

**วัน:** 2 · **ระดับ:** Advanced · **เวลาโดยประมาณ:** อ่านความรู้ 20–30 นาที + Lab 60–90 นาที  
**ทักษะ:** On block error, On error (Retry/Continue), Get last error, logging, cleanup

> **Browser บล็อก Capture element:** ใช้เส้นทดแทน Desktop/Notepad ที่ [`../09b-error-handling-winapp/`](../09b-error-handling-winapp/README.md) — ไม่ต้องพึ่ง Lab Hub / browser extension

## ลำดับการเรียน (จับมือทำ)

| ขั้น | ไฟล์ | ทำอะไร |
|------|------|--------|
| 0 | [`shared/PAD-FUNDAMENTALS.md`](../../shared/PAD-FUNDAMENTALS.md) | พื้นฐาน PAD / กฎ `%` (ถ้ายังไม่คุ้น designer) |
| 1 | **[LESSON.md](LESSON.md)** | อ่านความรู้: กลไก error จริงของ PAD (ไม่ใช่ Try-Catch) |
| 2 | **[LAB.md](LAB.md)** | Fault cases A–E (+ Challenge F–I) ทีละขั้น |


## Reference script (catch-up)

สำหรับนักเรียนที่ทำตามไม่ทัน — เปิด [`scripts/09-error-handling.robin`](scripts/09-error-handling.robin) แล้ว copy วางใน desktop flow ว่าง

- partial-ui — Cases A–E; Chrome + bundled Delay / Dialogs / Forms (F–I ยังเป็น challenge stub)
- Get last error ใน catch-up: `ERROR => LastError Reset: True`
- ไม่แทนการทำ LAB หลัก; ใช้เทียบลำดับ action / กู้งานให้ทันชั้น

## วัตถุประสงค์
- ทำให้ desktop flow ทนต่อความล้มเหลวที่ตั้งใจจำลอง
- บันทึก log ให้ตรวจสอบย้อนหลังได้ และไม่ทิ้ง Excel/browser ค้าง
- แยกได้ว่า error ใดควร retry และ error ใดควรถือว่าจบงานอย่างควบคุม

## Prerequisites

- PAD ติดตั้งแล้ว (แนะนำ baseline **2607+**)
- Browser extension สำหรับ Web cases
- อ่านสั้น ๆ: [Handle errors](https://learn.microsoft.com/power-automate/desktop-flows/errors)

## Assets / Output

| | Path |
|--|------|
| Fault script | [`assets/fault-injection.md`](assets/fault-injection.md) |
| Log template | [`assets/error-log-template.csv`](assets/error-log-template.csv) |
| Your log | `C:\PAD-Labs\logs\lab09\error-log.csv` |
| Missing path / Bad URL | [`assets/missing-file-path.txt`](assets/missing-file-path.txt) · [`assets/bad-url.txt`](assets/bad-url.txt) |

## บทที่เกี่ยวข้อง

- ทดแทนเมื่อ Capture ไม่ได้: [Lab 09b Error Handling WinApp](../09b-error-handling-winapp/README.md)
- ใช้แนวคิดนี้ใน: [Lab 07 Contoso](../07-contoso-invoice-ops/README.md) · [Lab 10 Capstone](../10-capstone-sales-ops/README.md)
- คำศัพท์ทางการ: [`shared/OFFICIAL-TERMINOLOGY.md`](../../shared/OFFICIAL-TERMINOLOGY.md)
