# Power Automate Desktop — Lab Kit (2 Days)

ชุดเอกสารและ mock assets สำหรับหลักสูตร **Power Automate Desktop (PAD) 2 วัน**  
แนวทางหลักคือ Hands-on Labs ทีละขั้นใน designer ควบคู่ Capstone Workshop เพื่อให้ผู้เรียนลงมือสร้าง desktop flow จริง

| รายการ | รายละเอียด |
|--------|------------|
| Web UI (Lab Hub) | [https://ontoiq.tech/pad/](https://ontoiq.tech/pad/) |
| Element UI (Desktop) | [Contoso Invoicing](https://github.com/MicrosoftDocs/mslearn-developer-tools-power-platform/tree/master/power-automate-desktop/contoso-invoice-app) · ดูรายละเอียดใน Lab [07](labs/07-contoso-invoice-ops/README.md) |
| Sample packs อ้างอิง | [Microsoft Learn — power-automate-desktop](https://github.com/MicrosoftDocs/mslearn-developer-tools-power-platform/tree/master/power-automate-desktop) |
| PAD baseline (Aug 2026) | **2607+** (Installer ~2.70.x) — ดู [`shared/SOURCES-AUG2026.md`](shared/SOURCES-AUG2026.md) |
| Course Outline (ไฟล์ท้องถิ่น) | `Trainocate_Outline_Power Automate Desktop (2 days) ake.pdf` |
| สไลด์ประกอบ (ไฟล์ท้องถิ่น) | `Power Automate Desktop.pptx` |

> ไฟล์ PPTX/PDF เก็บไว้ในเครื่องสำหรับสอน — ไม่ได้เผยแพร่ใน GitHub repo  
> แต่ละ Lab มีส่วน **Hands-on ทีละขั้น** (ค่าในช่อง action + ตัวแปร) ตาม [`shared/HANDS-ON-LAB-TEMPLATE.md`](shared/HANDS-ON-LAB-TEMPLATE.md)

---

## วัตถุประสงค์

เมื่อจบหลักสูตร ผู้เรียนจะสามารถ:

- อธิบายแนวคิด RPA และบทบาทของ Power Automate for desktop ในระบบนิเวศ Power Automate
- สร้าง desktop flow ด้วย **Recorder** และ **Actions Pane**
- ใช้ **UI Elements** / **Selectors** ได้ทั้งบนเว็บและแอป Desktop (รวม Contoso Invoicing)
- จัดการไฟล์/โฟลเดอร์, Excel, Variables และ Data Tables
- ออกแบบ Logic ด้วย If/Else, Loop, Error Handling และ Subflows
- สร้าง flow ธุรกิจครบวงจรแบบ **Excel → Contoso / Web → Excel → Outlook** พร้อมภารกิจ **Web Scout**

---

## กลุ่มเป้าหมาย

- ผู้ใช้งานที่ต้องการ automate งานซ้ำบน Windows
- Business Analysts, Operations และ Administrators
- ผู้สนใจ RPA / Power Platform และต้องการฝึก PAD แบบ hands-on

---

## Prerequisites

| รายการ | หมายเหตุ |
|--------|----------|
| Windows 10/11 | สภาพแวดล้อมมาตรฐานสำหรับ PAD |
| [Power Automate for desktop](https://learn.microsoft.com/power-automate/desktop-flows/install) | ติดตั้งด้วย MSI หรือ Microsoft Store — แนะนำ **2607+** สำหรับชั้นเรียนสิงหาคม 2026; เวอร์ชันใหม่ต้องการ .NET 8 (ตัว installer จัดการให้โดยทั่วไป) |
| Microsoft Edge หรือ Chrome | พร้อม browser extension สำหรับ PAD |
| Microsoft Excel | ใช้ใน Lab 06–10 |
| Contoso Invoicing | จำเป็นใน Lab 07 — ติดตั้งจาก [ContosoInvoicingSetup.zip](https://github.com/MicrosoftDocs/mslearn-developer-tools-power-platform/raw/master/power-automate-desktop/contoso-invoice-app/ContosoInvoicingSetup.zip) |
| Microsoft Outlook (Desktop) | ใช้ใน Capstone (Lab 10) — แนะนำสร้างเป็น Draft และใช้ผู้รับจำลองก่อนส่งจริง |
| สิทธิ์เครือข่าย | เข้าถึง `https://ontoiq.tech/pad/` ได้ |

---

## Selector Convention (PAD Lab Hub)

ทุก control บน Lab Hub มี `id` และ/หรือ `data-pad` เพื่อให้เลือก element ได้เสถียร

```text
#txt-name
[data-pad="btn-submit"]
```

แนวทางที่แนะนำ:

1. ใช้ **UI element picker** ใน PAD แล้วล็อกด้วย `id` หรือ `data-pad`
2. หลีกเลี่ยง selector ที่อ้าง index หรือ xpath ยาว เพราะเปราะเมื่อหน้าเว็บเปลี่ยนโครงสร้าง
3. ใส่ **Wait for web page content** ก่อน Interact กับ element แบบ dynamic เช่น AJAX, Delay หรือ Popup

รายละเอียดเพิ่มเติม: [`shared/SELECTOR-CONVENTIONS.md`](shared/SELECTOR-CONVENTIONS.md) · ชื่อ Action ทางการ: [`shared/OFFICIAL-TERMINOLOGY.md`](shared/OFFICIAL-TERMINOLOGY.md) · สไตล์ภาษา: [`shared/WRITING-STYLE.md`](shared/WRITING-STYLE.md) · อ้างอิง Aug 2026: [`shared/SOURCES-AUG2026.md`](shared/SOURCES-AUG2026.md)

> **ตัวแปรใน PAD:** ตอนสร้างชื่อ (Set variable / Store into / ชื่อ produced) **ไม่ใส่ `%`** — ตอนใช้ในช่องอื่นใช้ `%ชื่อ%` — ดู [`shared/BEST-PRACTICES.md`](shared/BEST-PRACTICES.md) และ [`shared/HANDS-ON-LAB-TEMPLATE.md`](shared/HANDS-ON-LAB-TEMPLATE.md)

สำหรับ Desktop UI ของ Contoso ดู UI map ใน [`labs/07-contoso-invoice-ops/assets/ui-map.md`](labs/07-contoso-invoice-ops/assets/ui-map.md)

---

## แผนการเรียน 2 วัน

### วันที่ 1 — Fundamentals & Core Actions

| โมดูล | หัวข้อ | Lab |
|-------|--------|-----|
| What is RPA? | แนวคิด RPA, ประโยชน์, Cloud vs Desktop Flows | — |
| Getting Started | ติดตั้ง PAD, Workspace, Actions Pane, Variables, Recorder | — |
| First Automation | Desktop Recorder, Record & Replay | [01 Record & Replay](labs/01-record-replay/README.md) |
| UI Elements | Selectors และการเปิด/ปิด/โฟกัสแอป | [01b Notepad/Calculator](labs/01b-desktop-ui-elements/README.md) · Contoso เต็มรูปแบบใน Lab 07 |
| File & Folder | Create/Copy/Move/Rename, Read/Write Text | [02 File Management](labs/02-file-management/README.md) |
| Web Automation | Launch browser, Fill form, Extract table | [03 Web Scout](labs/03-web-scout/README.md) |

### วันที่ 2 — Advanced Actions, Logic & Capstone

| โมดูล | หัวข้อ | Lab |
|-------|--------|-----|
| Conditional Logic | If / Else If / Else | [04 Conditional Automation](labs/04-conditional-automation/README.md) |
| Loops | For each, Loop condition | [05 Looping Files/Data](labs/05-looping-files-data/README.md) |
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
| 01 | [Record & Replay](labs/01-record-replay/README.md) | Recorder และการกรอกฟอร์มเบื้องต้น | [01 Forms](https://ontoiq.tech/pad/01-forms.html) |
| 01b | [Desktop UI Elements](labs/01b-desktop-ui-elements/README.md) | Selectors บน Notepad และ Calculator | Windows apps |
| 02 | [File Management](labs/02-file-management/README.md) | File/Folder actions | — |
| 03 | [Web Scout](labs/03-web-scout/README.md) | Table, Controls, AJAX, Files (+ Iframe/API challenge) | [02](https://ontoiq.tech/pad/02-controls.html) · [03](https://ontoiq.tech/pad/03-table.html) · [05](https://ontoiq.tech/pad/05-files.html) · [09](https://ontoiq.tech/pad/09-ajax-table.html) · [19](https://ontoiq.tech/pad/19-catalog.html) |
| 04 | [Conditional Automation](labs/04-conditional-automation/README.md) | If/Else ตาม business rules | — |
| 05 | [Looping Files/Data](labs/05-looping-files-data/README.md) | For each กับไฟล์และแถวข้อมูล | — |
| 06 | [Data Table & Excel](labs/06-data-table-excel/README.md) | อ่าน แปลง และเขียน Excel | — |
| 07 | [Contoso Invoice Ops](labs/07-contoso-invoice-ops/README.md) | Desktop UI, validate, attachments, subflows | **Contoso Invoicing** |
| 08 | [Excel ↔ Web Round-trip](labs/08-excel-web-roundtrip/README.md) | Login + Forms + Wizard (+ Iframe/Files challenge) | [06](https://ontoiq.tech/pad/06-login.html) · [01](https://ontoiq.tech/pad/01-forms.html) · [07](https://ontoiq.tech/pad/07-wizard.html) |
| 09 | [Error Handling](labs/09-error-handling/README.md) | Retry/log + Dialog/Delay (+ OCR/Files/Iframe/API) | [04](https://ontoiq.tech/pad/04-dialogs.html) · [11](https://ontoiq.tech/pad/11-delay.html) · [01](https://ontoiq.tech/pad/01-forms.html) |
| 10 | [Capstone Sales Ops](labs/10-capstone-sales-ops/README.md) | Scout + Round-trip + Outlook และชุด Phase 1 | ตามโจทย์ Capstone |

---

## Phase 1 — Core coverage (PAD Lab Hub)

อ้างอิงแผนที่บทเรียน: [https://ontoiq.tech/pad/](https://ontoiq.tech/pad/)

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

> หากทำทั้ง Core และ Challenge ตาม Lab 03/08/09/10 จะครอบคลุม Phase 1 ทั้ง 12 โมดูล  
> โมดูล **19 Catalog** (pagination) พร้อมแล้วที่ [19-catalog.html](https://ontoiq.tech/pad/19-catalog.html) และใช้ใน Lab 03 Mission P กับ Lab 10

---

## โครงสร้าง Repository

```text
power-automate-desktop/
├── README.md                          ← คุณอยู่ที่นี่
├── shared/                            ← แนวทางกลางและ schema อ้างอิง
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
└── (ไฟล์สไลด์/outline เก็บท้องถิ่น — ไม่ขึ้น GitHub)
```

แต่ละ Lab โดยทั่วไปมี:

- `README.md` — วัตถุประสงค์, **Hands-on ทีละขั้น**, จุดที่มักทำผิด, เกณฑ์ผ่าน และ troubleshooting (อ้างอิง docs สิงหาคม 2026)
- `assets/` — mock input / expected output เมื่อ Lab นั้นต้องการไฟล์ตัวอย่าง

---

## วิธีเริ่มต้น (ผู้เรียน)

1. Clone หรือ unzip repo นี้ลงเครื่อง Windows
2. ติดตั้ง PAD พร้อม browser extension และ Excel (เพิ่ม Contoso สำหรับ Lab 07 และ Outlook สำหรับ Lab 10)
3. เปิด Lab Hub ที่ [https://ontoiq.tech/pad/](https://ontoiq.tech/pad/) เพื่อยืนยันว่าเข้าถึงได้
4. อ่านและทำ Lab ตามลำดับ `01 → 10` หรือตามที่วิทยากรมอบหมาย
5. สร้าง desktop flow **ใหม่ต่อหนึ่ง Lab** และตั้งชื่อตาม convention ใน [`shared/BEST-PRACTICES.md`](shared/BEST-PRACTICES.md)
6. ใช้ไฟล์ใน `labs/<lab>/assets/` เป็น input — **ไม่ควรแก้ไฟล์ต้นฉบับใน repo** ให้คัดลอกไปโฟลเดอร์ทำงานของตนเองก่อน

### โฟลเดอร์ทำงานที่แนะนำบนเครื่อง

```text
C:\PAD-Labs\
  ├── working\          ← สำเนา assets ที่แก้ไขได้
  ├── output\           ← ผลลัพธ์จาก flow
  └── logs\             ← log / screenshot จาก Lab 07, 09–10
```

---

## Microsoft Sample Assets (Element UI)

ใช้เป็น Desktop Element UI หลักใน Lab 07 และเป็นชุดข้อมูลเสริมเวลาสาธิต:

- [contoso-invoice-app](https://github.com/MicrosoftDocs/mslearn-developer-tools-power-platform/tree/master/power-automate-desktop/contoso-invoice-app) ← **Lab 07 ใช้บังคับ**
- Sample zips: `Customers.zip`, `Employees.zip`, `Orders.zip`, `SampleInvoices.zip`, `newinvoice.zip`

สรุปบทบาทใน Lab Kit นี้:

- **Web UI หลัก** = Onto-IQ PAD Lab Hub
- **Desktop Element UI หลัก** = Contoso Invoicing (Lab 07)
- **Sample packs ของ Microsoft** = ทางเลือกเสริมใน Lab 07 หรือการสาธิตของวิทยากร

---

## หลักปฏิบัติสั้น ๆ

| หัวข้อ | แนวทาง |
|--------|--------|
| Naming | ใช้รูปแบบ `LabXX_ShortName` เช่น `Lab07_ContosoInvoiceOps` |
| Variables | ตอนสร้างชื่อไม่ใส่ `%` (เช่น `InputLeads`); ตอนใช้ในช่องอื่นใส่ `%InputLeads%` — ดู Hands-on ของแต่ละ Lab |
| Waits | ใช้ Wait for web page content / Wait for window content ก่อน Click หรือ Populate |
| Excel | ปิด instance ด้วย Close Excel ทุกครั้ง; ก่อน **Save document as** ชื่อคงที่ให้มีนโยบายรันซ้ำ (If exists→Delete / เปิดเดิม+Save / timestamp) — ดู [`shared/BEST-PRACTICES.md`](shared/BEST-PRACTICES.md) |
| Contoso | Run application ครั้งเดียวต่อรอบ แล้ว Focus window ก่อนกรอก จากนั้น Close window ท้าย flow |
| Outlook | สร้างเป็น **Draft** ก่อน — ส่งจริงเฉพาะเมื่อวิทยากรอนุญาต |
| Secrets | ห้าม hardcode รหัสผ่านจริง — บัญชี demo ของ Lab Hub คือ `demo` / `demo` |

---

## Troubleshooting ภาพรวม

| อาการ | สิ่งที่ควรตรวจ |
|-------|----------------|
| Selector ไม่เจอ (Web) | รีเฟรช UI elements แล้วใช้ `#id` หรือ `[data-pad=...]` |
| Selector ไม่เจอ (Contoso) | Recapture บนหน้าต่างแอป และ Focus window ก่อน Interact |
| หน้า AJAX ยังว่าง | ใช้ Wait for web page content จนแถวข้อมูลพร้อม |
| Excel locked | ปิด Excel ที่เปิดอยู่ด้วยมือ และ Close Excel ใน flow |
| Save as รอบสองล้ม (ไฟล์ซ้ำ) | If file exists → Delete ก่อน Save as หรือเปิดไฟล์เดิมแล้ว Save — Best Practices |
| Outlook ไม่ส่ง | ตรวจ profile และสิทธิ์ หรือเก็บเป็น Draft แทน |
| Browser ไม่ตอบ | Close web browser แล้ว Launch new Edge/Chrome ใหม่ หรือ Attach to running instance ถ้าจำเป็น |
| UIPI / ส่งคลิกไม่ได้ | รัน PAD กับแอปเป้าหมายที่ระดับ elevation เดียวกัน |

รายละเอียดเฉพาะ Lab อยู่ใน README ของแต่ละโฟลเดอร์

---

## License / หมายเหตุ

- PAD Lab Hub เป็นทรัพย์สินของ Onto-IQ สำหรับใช้ประกอบการฝึกอบรม
- Microsoft sample assets และ Contoso Invoicing อยู่ภายใต้เงื่อนไขของ Microsoft Docs repository ต้นทาง
- Mock data ใน repo นี้เป็นข้อมูลจำลอง ไม่ใช่ข้อมูลลูกค้าจริง
