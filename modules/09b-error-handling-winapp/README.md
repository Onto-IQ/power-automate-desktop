# Lab 09b — Error Handling (Windows / Notepad)

**วัน:** 2 · **ระดับ:** Advanced · **เวลาโดยประมาณ:** อ่านความรู้ 15–20 นาที + Lab 50–70 นาที  
**ทักษะ:** On block error, On error (Stop / Continue / Retry), Get last error, logging, Cleanup บน Desktop UI  
**Flow ชื่อ:** `Lab09b_ErrorHandling_WinApp`  
**ทดแทน:** [Lab 09 Error Handling (web)](../09-error-handling/README.md) เมื่อ browser บล็อก **Capture element**

> **ใช้เมื่อไหร่:** ลูกค้า/ห้องเรียนที่ Web browser ป้องกันการ Capture element (Secure Isolation / policy)  
> **อย่าใช้แทนเมื่อ:** Capture บน Lab Hub ได้ปกติ — ให้ทำ [Lab 09 web](../09-error-handling/README.md) ก่อน

## ลำดับการเรียน (จับมือทำ)

| ขั้น | ไฟล์ | ทำอะไร |
|------|------|--------|
| 0 | [`shared/PAD-FUNDAMENTALS.md`](../../shared/PAD-FUNDAMENTALS.md) | พื้นฐาน PAD / กฎ `%` (ถ้ายังไม่คุ้น designer) |
| 1 | **[LESSON.md](LESSON.md)** | อ่านความรู้: กลไก error จริงของ PAD บน Desktop |
| 2 | **[LAB.md](LAB.md)** | Fault cases A–E (+ Challenge F–H) ทีละขั้น |

## Reference script (catch-up)

สำหรับนักเรียนที่ทำตามไม่ทัน — เปิด [`scripts/09b-error-handling-winapp.robin`](scripts/09b-error-handling-winapp.robin) แล้ว copy วางใน desktop flow ว่าง

- partial-ui — Cases A–C รันได้จาก logic; D/E อาจต้อง rebind UI Elements ของ Notepad / Save dialog
- Get last error ใน catch-up: `ERROR => LastError Reset: True` (Clear error)
- ไม่แทนการทำ LAB หลัก; ใช้เทียบลำดับ action / กู้งานให้ทันชั้น

## วัตถุประสงค์

- ทำให้ desktop flow ทนต่อความล้มเหลวที่ตั้งใจจำลอง **โดยไม่พึ่ง browser**
- บันทึก log ให้ตรวจสอบย้อนหลังได้ และไม่ทิ้ง Notepad ค้าง
- แยกได้ว่า error ใดควร retry และ error ใดควรถือว่าจบงานอย่างควบคุม

## Prerequisites

- PAD ติดตั้งแล้ว (แนะนำ baseline **2607+**)
- มี `C:\Windows\System32\notepad.exe`
- แนะนำทำ [Lab 01b Notepad](../01b-notepad/README.md) มาก่อน (UI Elements พื้นฐาน)
- ทบทวน R6 จาก [Lab 07 Contoso](../07-contoso-invoice-ops/README.md) (SET-only + Get last error)
- **ไม่ต้อง** มี browser extension / Lab Hub
- อ่านสั้น ๆ: [Handle errors](https://learn.microsoft.com/power-automate/desktop-flows/errors)

## Assets / Output

| | Path |
|--|------|
| Fault script | [`assets/fault-injection.md`](assets/fault-injection.md) |
| Log template | [`assets/error-log-template.csv`](assets/error-log-template.csv) |
| Your log | `C:\PAD-Labs\logs\lab09b\error-log.csv` |
| Missing path / Bad app | [`assets/missing-file-path.txt`](assets/missing-file-path.txt) · [`assets/bad-app-path.txt`](assets/bad-app-path.txt) |
| Recovery text | [`assets/notepad-recovery.txt`](assets/notepad-recovery.txt) |
| Output Save As | `C:\PAD-Labs\output\lab09b\recovery-ok.txt` |

## บทที่เกี่ยวข้อง

- ก่อนหน้า (R6 ที่ Contoso): [Lab 07 Contoso Invoice Ops](../07-contoso-invoice-ops/README.md)
- Desktop พื้นฐาน: [Lab 01b Notepad](../01b-notepad/README.md)
- Lab มาตรฐาน (web): [Lab 09 Error Handling](../09-error-handling/README.md)
- ถัดไป: [Lab 10 Capstone](../10-capstone-sales-ops/README.md)
- คำศัพท์ทางการ: [`shared/OFFICIAL-TERMINOLOGY.md`](../../shared/OFFICIAL-TERMINOLOGY.md)
