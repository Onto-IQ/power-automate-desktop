# Power Automate Desktop — Lab Kit (3 Days)

ชุดเอกสารและ mock assets สำหรับหลักสูตร **Power Automate Desktop (PAD) 2 วัน**  
แนวทาง: Hands-on Labs + Capstone Workshop

| รายการ | รายละเอียด |
|--------|------------|
| Web UI (Lab Hub) | [https://ontoiq.tech/pad/](https://ontoiq.tech/pad/) |
| Element UI (Desktop) | [Contoso Invoicing](https://github.com/MicrosoftDocs/mslearn-developer-tools-power-platform/tree/master/power-automate-desktop/contoso-invoice-app) · Lab [07](labs/07-contoso-invoice-ops/README.md) |
| Sample packs อ้างอิง | [Microsoft Learn — power-automate-desktop](https://github.com/MicrosoftDocs/mslearn-developer-tools-power-platform/tree/master/power-automate-desktop) |
| Course Outline | `Trainocate_Outline_Power Automate Desktop (2 days) ake.pdf` |
| สไลด์ประกอบ | `Power Automate Desktop.pptx` |

---

## วัตถุประสงค์

เมื่อจบหลักสูตร ผู้เรียนจะสามารถ:

- อธิบายแนวคิด RPA และบทบาทของ Power Automate Desktop ในระบบนิเวศ Power Automate
- สร้าง Desktop Flow ด้วย Recorder และ Actions Pane
- ใช้ UI Elements / Selectors กับทั้ง **Web** และ **Desktop apps (Contoso Invoicing)**
- จัดการไฟล์/โฟลเดอร์, Excel, Variables และ Data Tables
- ออกแบบ Logic: If/Else, Loop, Error Handling และ Subflows
- สร้าง Flow ธุรกิจครบวงจร: **Excel → Contoso / Web → Excel → Outlook** พร้อม **Web Scout**

---

## กลุ่มเป้าหมาย

- ผู้ใช้งานที่ต้องการ automate งานซ้ำบน Windows
- Business Analysts, Operations, Administrators
- ผู้สนใจ RPA / Power Platform ที่ต้องการ hands-on PAD

---

## Prerequisites

| รายการ | หมายเหตุ |
|--------|----------|
| Windows 10/11 | จำเป็นสำหรับ PAD |
| [Power Automate for desktop](https://learn.microsoft.com/power-automate/desktop-flows/install) | ติดตั้งด้วย MSI/Store; เวอร์ชันใหม่ต้องการ .NET 8 (installer จัดการให้) |
| Microsoft Edge หรือ Chrome | พร้อม browser extension สำหรับ PAD |
| Microsoft Excel | สำหรับ Lab 06–10 |
| Contoso Invoicing | จำเป็นสำหรับ Lab 07 — ติดตั้งจาก [ContosoInvoicingSetup.zip](https://github.com/MicrosoftDocs/mslearn-developer-tools-power-platform/raw/master/power-automate-desktop/contoso-invoice-app/ContosoInvoicingSetup.zip) |
| Microsoft Outlook (Desktop) | สำหรับ Capstone (Lab 10) — ใช้ recipient จำลอง / Draft ก่อนส่งจริง |
| สิทธิ์เครือข่าย | เข้าถึง `https://ontoiq.tech/pad/` ได้ |

---

## Selector Convention (PAD Lab Hub)

ทุก control บน Lab Hub มี `id` และ/หรือ `data-pad`

```text
#txt-name
[data-pad="btn-submit"]
```

แนวทางที่ดี:

1. ใช้ **UI element picker** ใน PAD แล้วล็อกด้วย `id` / `data-pad`
2. หลีกเลี่ยง selector ที่อ้าง index/xpath ยาวและเปราะ
3. ใส่ **Wait for web page content** ก่อน Interact กับ element แบบ dynamic (AJAX / Delay / Popup)

รายละเอียดเพิ่มเติม: [`shared/SELECTOR-CONVENTIONS.md`](shared/SELECTOR-CONVENTIONS.md) · ชื่อ Action ทางการ: [`shared/OFFICIAL-TERMINOLOGY.md`](shared/OFFICIAL-TERMINOLOGY.md)

สำหรับ **Desktop UI (Contoso)** ดู UI map ใน [`labs/07-contoso-invoice-ops/assets/ui-map.md`](labs/07-contoso-invoice-ops/assets/ui-map.md)

---

## แผนการเรียน 2 วัน

### วันที่ 1 — Fundamentals & Core Actions

| โมดูล | หัวข้อ | Lab |
|-------|--------|-----|
| What is RPA? | แนวคิด RPA, ประโยชน์, Cloud vs Desktop Flows | — |
| Getting Started | ติดตั้ง PAD, Workspace, Actions Pane, Variables, Recorder | — |
| First Automation | Desktop Recorder, Record & Replay | [01 Record & Replay](labs/01-record-replay/README.md) |
| UI Elements | Selectors, Launch/Close/Focus App | [01b Notepad/Calculator](labs/01b-desktop-ui-elements/README.md) · Contoso เต็มใน Lab 07 |
| File & Folder | Create/Copy/Move/Rename, Read/Write Text | [02 File Management](labs/02-file-management/README.md) |
| Web Automation | Launch browser, Fill form, Extract table | [03 Web Scout](labs/03-web-scout/README.md) |

### วันที่ 2 — Advanced Actions, Logic & Capstone

| โมดูล | หัวข้อ | Lab |
|-------|--------|-----|
| Conditional Logic | If / Else If / Else | [04 Conditional Automation](labs/04-conditional-automation/README.md) |
| Loops | For each, Do until, While | [05 Looping Files/Data](labs/05-looping-files-data/README.md) |
| Variables & Data Tables | Types, List, Data Table | [06 Data Table & Excel](labs/06-data-table-excel/README.md) |
| Desktop Element UI | Contoso Invoicing ครบวงจร Excel → App → Excel | [07 Contoso Invoice Ops](labs/07-contoso-invoice-ops/README.md) |
| Excel + Web | Round-trip กับ Lab Hub | [08 Excel ↔ Web Round-trip](labs/08-excel-web-roundtrip/README.md) |
| Error Handling | On block error / On error, Get last error, Logging | [09 Error Handling](labs/09-error-handling/README.md) |
| Best Practices | Subflows, Debugging, Naming | [`shared/BEST-PRACTICES.md`](shared/BEST-PRACTICES.md) |
| Capstone Workshop | Web Scout + Excel + Outlook | [10 Capstone Sales Ops](labs/10-capstone-sales-ops/README.md) |

---

## Lab Index

| # | Lab | ทักษะหลัก | UI เป้าหมาย |
|---|-----|-----------|-------------|
| 01 | [Record & Replay](labs/01-record-replay/README.md) | Recorder, กรอกฟอร์มง่าย | [01 Forms](https://ontoiq.tech/pad/01-forms.html) |
| 01b | [Desktop UI Elements](labs/01b-desktop-ui-elements/README.md) | Notepad + Calculator selectors | Windows apps |
| 02 | [File Management](labs/02-file-management/README.md) | File/Folder actions | — |
| 03 | [Web Scout](labs/03-web-scout/README.md) | Table, Controls, AJAX, Files (+ Iframe/API challenge) | [02](https://ontoiq.tech/pad/02-controls.html) · [03](https://ontoiq.tech/pad/03-table.html) · [05](https://ontoiq.tech/pad/05-files.html) · [09](https://ontoiq.tech/pad/09-ajax-table.html) |
| 04 | [Conditional Automation](labs/04-conditional-automation/README.md) | If/Else ตาม business rules | — |
| 05 | [Looping Files/Data](labs/05-looping-files-data/README.md) | For each ไฟล์/แถว | — |
| 06 | [Data Table & Excel](labs/06-data-table-excel/README.md) | อ่าน/แปลง/เขียน Excel | — |
| 07 | [Contoso Invoice Ops](labs/07-contoso-invoice-ops/README.md) | Desktop UI, validate, attachments, subflows | **Contoso Invoicing** |
| 08 | [Excel ↔ Web Round-trip](labs/08-excel-web-roundtrip/README.md) | Login + Forms + Wizard (+ Iframe/Files challenge) | [06](https://ontoiq.tech/pad/06-login.html) · [01](https://ontoiq.tech/pad/01-forms.html) · [07](https://ontoiq.tech/pad/07-wizard.html) |
| 09 | [Error Handling](labs/09-error-handling/README.md) | Retry/log + Dialog/Delay (+ OCR/Files/Iframe/API) | [04](https://ontoiq.tech/pad/04-dialogs.html) · [11](https://ontoiq.tech/pad/11-delay.html) · [01](https://ontoiq.tech/pad/01-forms.html) |
| 10 | [Capstone Sales Ops](labs/10-capstone-sales-ops/README.md) | Scout + Round-trip + Outlook · Phase 1 pack | Phase 1 missions ตามโจทย์ |

---

## Phase 1 — Core coverage (PAD Lab Hub)

อ้างอิงแผนที่: [https://ontoiq.tech/pad/](https://ontoiq.tech/pad/)

| โมดูล | การใช้ใน Lab Kit |
|-------|------------------|
| 01 Forms | Lab 01 (หลัก) · 08 · 09 · 10 |
| 02 Controls | Lab 03 Mission B |
| 03 Table | Lab 03 Mission A · 10 |
| 04 Dialogs | Lab 09 Case D |
| 05 Files | Lab 03 Mission D · 08 Challenge J · 09 Case G · 10 Mission |
| 06 Login | Lab 08 (บังคับ) · 10 |
| 07 Wizard | Lab 08 Mission W · 10 Mission |
| 08 Iframe | Lab 03 Challenge E · 08 Challenge I · 09 Case H · 10 Challenge |
| 09 AJAX Table | Lab 03 Mission C · 10 |
| 10 OCR | Lab 09 Case F · 10 Challenge |
| 11 Delay | Lab 09 Case C |
| 12 API | Lab 03 Challenge F · 09 Case I · 10 Challenge |

> ถ้าผู้เรียนทำ Core + Challenge ตาม Lab 03/08/09/10 จะครอบคลุม Phase 1 ทั้ง 12 โมดูล  
> โมดูล **19 Catalog** (pagination) พร้อมแล้ว: [19-catalog.html](https://ontoiq.tech/pad/19-catalog.html) — ใช้ใน Lab 03 Mission P และ Lab 10

---

## โครงสร้าง Repository

```text
power-automate-desktop/
├── README.md                          ← คุณอยู่ที่นี่
├── shared/                            ← แนวทางกลาง / schema อ้างอิง
├── labs/
│   ├── 01-record-replay/
│   ├── 01b-desktop-ui-elements/
│   ├── 02-file-management/
│   ├── 03-web-scout/
│   ├── 04-conditional-automation/
│   ├── 05-looping-files-data/
│   ├── 06-data-table-excel/
│   ├── 07-contoso-invoice-ops/        ← Desktop Element UI (Contoso)
│   ├── 08-excel-web-roundtrip/
│   ├── 09-error-handling/
│   └── 10-capstone-sales-ops/
├── Trainocate_Outline_...ake.pdf
└── Power Automate Desktop.pptx
```

แต่ละ Lab มี:

- `README.md` — วัตถุประสงค์, ขั้นตอน PAD, เกณฑ์ผ่าน, troubleshooting
- `assets/` — mock input / expected output (เมื่อจำเป็น)

---

## วิธีเริ่มต้น (ผู้เรียน)

1. Clone หรือ unzip repo นี้ลงเครื่อง Windows
2. ติดตั้ง PAD + browser extension + Excel (+ Contoso สำหรับ Lab 07, Outlook สำหรับ Lab 10)
3. เปิด Lab Hub: [https://ontoiq.tech/pad/](https://ontoiq.tech/pad/) เพื่อยืนยันการเข้าถึง
4. อ่าน Lab ตามลำดับ `01 → 10` (หรือตามที่วิทยากรมอบหมาย)
5. สร้าง Desktop Flow **ใหม่ต่อ Lab** ตั้งชื่อตาม convention ใน [`shared/BEST-PRACTICES.md`](shared/BEST-PRACTICES.md)
6. ใช้ไฟล์ใน `labs/<lab>/assets/` เป็น input — **อย่าแก้ต้นฉบับ**; คัดลอกไปยังโฟลเดอร์ทำงานของตัวเองถ้าจำเป็น

### โฟลเดอร์ทำงานแนะนำบนเครื่อง

```text
C:\PAD-Labs\
  ├── working\          ← สำเนา assets ที่แก้ไขได้
  ├── output\           ← ผลลัพธ์จาก Flow
  └── logs\             ← log / screenshot จาก Lab 07, 09–10
```

---

## Microsoft Sample Assets (Element UI)

ใช้เป็น **Desktop Element UI หลัก** ใน Lab 07 และชุดข้อมูลเสริม:

- [contoso-invoice-app](https://github.com/MicrosoftDocs/mslearn-developer-tools-power-platform/tree/master/power-automate-desktop/contoso-invoice-app) ← **Lab 07 บังคับใช้**
- Sample zips: `Customers.zip`, `Employees.zip`, `Orders.zip`, `SampleInvoices.zip`, `newinvoice.zip`

ใน Lab Kit นี้:

- **Web UI หลัก** = Onto-IQ PAD Lab Hub
- **Desktop Element UI หลัก** = Contoso Invoicing (Lab 07)
- **Sample packs Microsoft** = ทางเลือกเสริมใน Lab 07 / การสาธิตของวิทยากร

---

## หลักปฏิบัติสั้น ๆ

| หัวข้อ | แนวทาง |
|--------|--------|
| Naming | `LabXX_ShortName` เช่น `Lab07_ContosoInvoiceOps` |
| Variables | `%InputLeads%`, `%ScoutResults%`, `%LastError%` |
| Waits | Wait for element/content ก่อน Click/Populate |
| Excel | Close instance ทุกครั้ง; อย่าเปิดไฟล์ค้างขณะ Flow รัน |
| Contoso | Launch ครั้งเดียวต่อรัน, Focus ก่อนกรอก, Close ท้าย Flow |
| Outlook | สร้างเป็น **Draft** ก่อน — ส่งจริงเฉพาะเมื่อวิทยากรอนุญาต |
| Secrets | ห้าม hardcode password จริง — Lab Hub login demo คือ `demo` / `demo` |

---

## Troubleshooting ภาพรวม

| อาการ | ตรวจอะไร |
|-------|----------|
| Selector ไม่เจอ (Web) | รีเฟรช UI elements, ใช้ `#id` / `[data-pad=...]` |
| Selector ไม่เจอ (Contoso) | Recapture บนหน้าต่างแอป, Focus window ก่อน |
| หน้า AJAX ยังว่าง | Wait for web page content / Wait for element |
| Excel locked | ปิด Excel manual และ Close Excel instance ใน Flow |
| Outlook ไม่ส่ง | ตรวจ profile, สิทธิ์, หรือเก็บเป็น Draft แทน |
| Browser ไม่ตอบ | **Close web browser** แล้ว Launch new Edge/Chrome ใหม่; หรือ Attach to running instance ถ้าจำเป็น |
| UIPI / ส่งคลิกไม่ได้ | รัน PAD กับแอปเป้าหมายที่ elevation เดียวกัน |

รายละเอียดราย Lab อยู่ใน README ของแต่ละโฟลเดอร์

---

## License / หมายเหตุ

- PAD Lab Hub เป็นทรัพย์สินของ Onto-IQ สำหรับใช้ประกอบการฝึกอบรม
- Microsoft sample assets / Contoso Invoicing อยู่ภายใต้เงื่อนไขของ Microsoft Docs repository ต้นทาง
- Mock data ใน repo นี้เป็นข้อมูลจำลอง — ไม่ใช่ข้อมูลลูกค้าจริง
