# Lab 08 — Excel ↔ Web Round-trip

**วัน:** 2 · **ระดับ:** Intermediate–Advanced  
**ทักษะ:** อ่าน Excel → ป้อน Web UI → ดึงสถานะ/ข้อความจาก Web → เขียนกลับ Excel

## วัตถุประสงค์

- สร้าง Flow ธุรกิจสั้น: **Excel → Web → Excel**
- Login Lab Hub (demo) แล้วกรอกฟอร์มจากแต่ละแถว Lead
- อัปเดตคอลัมน์ Status / WebResult กลับลง workbook

## Setup

1. Flow `Lab08_ExcelWebRoundtrip`
2. คัดลอก `assets/leads-input.xlsx` (หรือสร้างจาก CSV) ไป working
3. Output: `C:\PAD-Labs\output\lab08\leads-output.xlsx`

## Web UI

| ขั้น | Phase 1 | URL | บัญชี / เงื่อนไข |
|------|---------|-----|------------------|
| Login | 06 | https://ontoiq.tech/pad/06-login.html | `demo` / `demo` |
| Forms (มาตรฐาน) | 01 | https://ontoiq.tech/pad/01-forms.html | ทุก lead ที่ `Status=New` และ Priority ≠ High |
| Wizard (Mission W) | 07 | https://ontoiq.tech/pad/07-wizard.html | lead ที่ `Priority=High` |

### Challenge missions

| Mission | Phase 1 | URL | เมื่อไร |
|---------|---------|-----|--------|
| I — Iframe lead | 08 | https://ontoiq.tech/pad/08-iframe.html | ทำกับ lead แรกที่ `Company` มีคำว่า `Fabrikam` (หรือแถวที่วิทยากรกำหนด) |
| J — Files proof | 05 | https://ontoiq.tech/pad/05-files.html | หลัง submit สำเร็จอย่างน้อย 1 แถว: upload `assets/roundtrip-proof.txt` แล้วบันทึกผลในคอลัมน์ `WebResult` หรือ sheet `Artifacts` |

## Input / Output

| | Path |
|--|------|
| Leads CSV | [`assets/leads-input.csv`](assets/leads-input.csv) |
| Output template | [`assets/leads-output-template.csv`](assets/leads-output-template.csv) |
| Files proof mock | [`assets/roundtrip-proof.txt`](assets/roundtrip-proof.txt) |
| Schema | [`shared/DATA-SCHEMAS.md`](../../shared/DATA-SCHEMAS.md) |

### Mapping Excel → Form

| Excel Column | Form field (แนวทาง) |
|--------------|---------------------|
| FullName | Name / `#txt-name` |
| Email | Email |
| Interest หรือ Message | Textarea / message |
| (วันนี้) | Date ใช้วันที่รัน Flow |

## PAD Action Sequence (แนะนำ)

1. **Launch Excel** → **Read from Excel worksheet** sheet `Leads` → `%Leads%`
2. **Launch new Microsoft Edge** หรือ **Launch new Chrome** → **06 Login** → **Populate text field on web page** `#txt-username` / `#txt-password` = `demo`/`demo` → **Press button on web page** `#btn-login`
3. **Wait for web page content** จนสำเร็จ / dashboard
4. **For each** lead ใน `%Leads%` ที่ `Status=New`:
   - **If** `Priority=High` → **Mission W (07 Wizard)** ทำครบทุก step แล้วเก็บผล
   - **Else** → ไป **01 Forms** → Populate + Press button ตาม mapping
   - Extract / อ่านข้อความผลลัพธ์ → `%WebResult%`
   - อัปเดต Status=`Submitted`, WebResult, SubmittedAt
5. (Challenge I) สำหรับ lead ที่เข้าเงื่อนไข → กรอกใน **08 Iframe**
6. (Challenge J) ไป **05 Files** อัปโหลด `roundtrip-proof.txt` แล้วบันทึกหลักฐาน
7. **Write to Excel worksheet** ทั้งตารางกลับ sheet `Leads` หรือ `Results`
8. Save + **Close Excel** + **Close web browser**

## Variables

| Variable | Type |
|----------|------|
| `%Excel%` | Excel |
| `%Browser%` | Browser |
| `%Leads%` | Data table |
| `%WebResult%` | Text |
| `%SubmittedAt%` | DateTime/Text |

## Expected Result

- แถวที่เป็น `New` ถูกเปลี่ยนเป็น `Submitted`
- มีค่า `WebResult` ไม่ว่าง
- ไฟล์ output แยกจาก input

## Acceptance Criteria

- [ ] Login ผ่านหน้า [06 Login](https://ontoiq.tech/pad/06-login.html) ก่อนทำงานกับฟอร์ม
- [ ] อ่านจาก Excel จริง ไม่ copy ค่าลงตัวแปรทีละคนแบบ hardcode ทั้งชุด
- [ ] ใช้ลูป For each
- [ ] **Mission W:** lead `Priority=High` ใช้ Wizard (07) ไม่ใช่ Forms อย่างเดียว
- [ ] ปิดด้วย **Close Excel** และ **Close web browser**
- [ ] มีอย่างน้อย 1 แถวอัปเดตสำเร็จ
- [ ] (Challenge) Mission I หรือ J อย่างน้อย 1 รายการ

## Challenge

- ข้ามแถวที่ Email ว่างด้วย If
- Mission I — Iframe / Mission J — Files ตามตารางด้านบน

## Troubleshooting

| อาการ | แก้ |
|-------|-----|
| Login หลุด | ทำ login ใหม่ในลูปหรือตรวจ cookie/session ของหน้า Lab |
| เขียน Excel ทับแถวผิด | ใช้ index / write cell ระมัดระวัง หรือเขียน sheet ใหม่ทั้งก้อน |
| ฟอร์ม validation | ตรวจรูปแบบ email/date |

## Cleanup

- ลบ working copies; คง CSV/XLSX ต้นฉบับใน assets
