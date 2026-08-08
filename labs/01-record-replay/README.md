# Lab 01 — Record & Replay

**วัน:** 1 · **ระดับ:** Beginner  
**ทักษะ:** Desktop/Web Recorder, Fill form, Submit, Variables พื้นฐาน

## วัตถุประสงค์

- ใช้ Recorder สร้าง Flow กรอกฟอร์มบน Web
- ตรวจ/ปรับ UI Elements หลัง Record
- Replay Flow ให้ผลลัพธ์ซ้ำได้

## Prerequisites

- PAD พร้อม browser extension
- เข้าถึง [01 Forms](https://ontoiq.tech/pad/01-forms.html)

## Setup

1. สร้าง Flow ชื่อ `Lab01_RecordReplay`
2. คัดลอก `assets/sample-form-input.csv` ไปที่ `C:\PAD-Labs\working\lab01\` (หรืออ่านค่าจากตัวแปรคงที่ตามขั้นตอนด้านล่าง)
3. เปิดหน้า Forms เพื่อตรวจว่าโหลดได้

## Input / Output

| | Path / ค่า |
|--|------------|
| Input mock | [`assets/sample-form-input.csv`](assets/sample-form-input.csv) |
| Web UI | https://ontoiq.tech/pad/01-forms.html |
| Expected | ฟอร์มถูกกรอกตามแถวแรก และ submit สำเร็จ (มีข้อความยืนยันบนหน้า) |

### ข้อมูลตัวอย่าง (แถวแรก)

| Field | Value |
|-------|-------|
| Name | Somchai Demo |
| Email | somchai.demo@example.com |
| Date | 2026-08-08 |
| Message | Hello from Lab 01 Record & Replay |

## PAD Action Sequence (แนะนำ)

1. **Launch new Microsoft Edge** หรือ **Launch new Chrome** → URL = Forms page → เก็บ instance เป็น `%Browser%`
2. **Wait for web page content** — element ของช่องชื่อ (เช่น `#txt-name` หรือ `[data-pad=...]`)
3. (ทางเลือก Recorder) กด Record แล้วกรอกฟอร์มด้วยมือ 1 รอบ → หยุด Record
4. ปรับค่าที่ Record ได้ให้ดึงจากตัวแปร:
   - `%FullName%`, `%Email%`, `%FormDate%`, `%Message%`
5. **Populate text field on web page** สำหรับแต่ละช่อง
6. **Press button on web page** / **Click link on web page** สำหรับ submit (`[data-pad="btn-submit"]` หรือ id ที่หน้ากำหนด)
7. **Extract data from web page** หรือ Get details เพื่อยืนยันข้อความ success (หรืออ่านข้อความด้วย UI element)
8. **Close web browser**

> หลัง Record ให้เปิด UI Elements pane ตรวจว่า selector ใช้ `id` / `data-pad` — ดู [`shared/SELECTOR-CONVENTIONS.md`](../../shared/SELECTOR-CONVENTIONS.md)

## Variables

| Variable | Type | ตัวอย่าง |
|----------|------|----------|
| `%Browser%` | Browser | — |
| `%FullName%` | Text | Somchai Demo |
| `%Email%` | Text | somchai.demo@example.com |
| `%FormDate%` | Text | 2026-08-08 |
| `%Message%` | Text | Hello from Lab 01... |
| `%SubmitResult%` | Text | ข้อความยืนยันจากหน้า |

## Expected Result

- Flow รันจบโดยไม่มี error
- ฟอร์มถูกกรอกด้วยค่าจากตัวแปร (ไม่ hardcode ใน action ถ้าทำได้)
- มีหลักฐาน success (extract text หรือ screenshot)

## Acceptance Criteria

- [ ] Flow ชื่อตาม convention
- [ ] Replay ได้อย่างน้อย 2 ครั้งติดต่อกัน
- [ ] UI Elements ใช้ selector ที่เสถียร
- [ ] Browser ถูกปิดท้าย Flow ด้วย **Close web browser**

## Troubleshooting

| อาการ | แก้ |
|-------|-----|
| Recorder จับ element ผิด | ลบ UI element แล้ว capture ใหม่ด้วย picker |
| วันที่กรอกไม่ได้ | ตรวจรูปแบบ date ของ control / พิมพ์เป็น text |
| Submit ไม่เกิดผล | Wait ก่อนคลิก; ตรวจ validation ของฟอร์ม |

## Cleanup

- ปิด browser instances ที่ค้าง
- ไม่ต้อง commit ค่าที่แก้ใน working folder

## อ้างอิงเพิ่ม

- Desktop UI พื้นฐาน (Notepad/Calculator): [Lab 01b](../01b-desktop-ui-elements/README.md)
- Desktop Element UI เต็มรูปแบบ (วัน 2): [Lab 07 Contoso Invoice Ops](../07-contoso-invoice-ops/README.md)
- Microsoft sample desktop UI: [contoso-invoice-app](https://github.com/MicrosoftDocs/mslearn-developer-tools-power-platform/tree/master/power-automate-desktop/contoso-invoice-app)
