# Lab 01 — Record & Replay

**วัน:** 1 · **ระดับ:** Beginner  
**ทักษะ:** Desktop/Web Recorder, การกรอกฟอร์ม, Submit และ Variables พื้นฐาน

## วัตถุประสงค์

- ใช้ **Recorder** สร้าง flow สำหรับกรอกฟอร์มบนเว็บ
- ตรวจและปรับ **UI Elements** หลัง Record ให้ selector เสถียรขึ้น
- Replay flow ให้ได้ผลลัพธ์ซ้ำกันได้อย่างน่าเชื่อถือ

## Prerequisites

- ติดตั้ง PAD พร้อม browser extension แล้ว
- เข้าถึงหน้า [01 Forms](https://ontoiq.tech/pad/01-forms.html) ได้

## Setup

1. สร้าง flow ชื่อ `Lab01_RecordReplay`
2. คัดลอก `assets/sample-form-input.csv` ไปที่ `C:\PAD-Labs\working\lab01\` (หรือกำหนดค่าลงตัวแปรตามขั้นตอนด้านล่าง)
3. เปิดหน้า Forms เพื่อยืนยันว่าโหลดได้ตามปกติ

## Input / Output

| | Path / ค่า |
|--|------------|
| Input mock | [`assets/sample-form-input.csv`](assets/sample-form-input.csv) |
| Web UI | https://ontoiq.tech/pad/01-forms.html |
| Expected | ฟอร์มถูกกรอกตามแถวแรก และ submit สำเร็จ โดยมีข้อความยืนยันบนหน้า |

### ข้อมูลตัวอย่าง (แถวแรก)

| Field | Value |
|-------|-------|
| Name | Somchai Demo |
| Email | somchai.demo@example.com |
| Date | 2026-08-08 |
| Message | Hello from Lab 01 Record & Replay |

## PAD Action Sequence (แนะนำ)

1. **Launch new Microsoft Edge** หรือ **Launch new Chrome** แล้วตั้ง URL เป็นหน้า Forms จากนั้นเก็บ instance เป็น `%Browser%`
2. **Wait for web page content** จนเห็นช่องชื่อ เช่น `#txt-name` หรือ `[data-pad=...]`
3. (ทางเลือก Recorder) กด Record แล้วกรอกฟอร์มด้วยมือหนึ่งรอบ จากนั้นหยุด Record
4. ปรับค่าที่ Record ได้ให้ดึงจากตัวแปร `%FullName%`, `%Email%`, `%FormDate%`, `%Message%`
5. ใช้ **Populate text field on web page** กรอกทีละช่อง
6. ใช้ **Press button on web page** หรือ **Click link on web page** สำหรับ submit เช่น `[data-pad="btn-submit"]`
7. ใช้ **Extract data from web page** หรืออ่านข้อความยืนยันด้วย UI element เพื่อพิสูจน์ว่าสำเร็จ
8. ปิดด้วย **Close web browser**

> หลัง Record ให้เปิด UI Elements pane ตรวจว่า selector อิง `id` / `data-pad` — ดูเพิ่มที่ [`shared/SELECTOR-CONVENTIONS.md`](../../shared/SELECTOR-CONVENTIONS.md)

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
- ค่าในฟอร์มมาจากตัวแปร (หลีกเลี่ยง hardcode ใน action หากทำได้)
- มีหลักฐานความสำเร็จ เช่น ข้อความที่ extract ได้ หรือ screenshot

## Acceptance Criteria

- [ ] ตั้งชื่อ flow ตาม convention
- [ ] Replay ได้สำเร็จอย่างน้อย 2 ครั้งติดต่อกัน
- [ ] UI Elements ใช้ selector ที่เสถียร
- [ ] ปิดเบราว์เซอร์ท้าย flow ด้วย **Close web browser**

## Troubleshooting

| อาการ | แนวทางแก้ |
|-------|-----------|
| Recorder จับ element ผิด | ลบ UI element เดิม แล้ว capture ใหม่ด้วย picker |
| กรอกวันที่ไม่ได้ | ตรวจรูปแบบ date ของ control หรือกรอกเป็นข้อความแทน |
| Submit ไม่เกิดผล | ใส่ Wait ก่อนคลิก และตรวจ validation ของฟอร์ม |

## Cleanup

- ปิดหน้าต่างเบราว์เซอร์ที่ยังค้างอยู่หลังจบการรัน
- ไม่ต้อง commit ค่าที่แก้ในโฟลเดอร์ working

## อ้างอิงเพิ่ม

- Desktop UI พื้นฐาน (Notepad/Calculator): [Lab 01b](../01b-desktop-ui-elements/README.md)
- Desktop Element UI เต็มรูปแบบ (วัน 2): [Lab 07 Contoso Invoice Ops](../07-contoso-invoice-ops/README.md)
- Microsoft sample desktop UI: [contoso-invoice-app](https://github.com/MicrosoftDocs/mslearn-developer-tools-power-platform/tree/master/power-automate-desktop/contoso-invoice-app)
