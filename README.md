# Power Automate Desktop — Lab Kit (2 Days)

[![Release](https://img.shields.io/github/v/release/Onto-IQ/power-automate-desktop?display_name=tag&sort=semver)](https://github.com/Onto-IQ/power-automate-desktop/releases/latest)
[![PAD baseline](https://img.shields.io/badge/PAD-2607%2B-0078D4?logo=microsoft&logoColor=white)](https://learn.microsoft.com/power-platform/released-versions/power-automate-desktop)
[![Lab Hub](https://img.shields.io/badge/Lab%20Hub-ontoiq.tech%2Fpad-0B5FFF)](https://ontoiq.tech/pad/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Changelog](https://img.shields.io/badge/changelog-Keep%20a%20Changelog-E05735)](CHANGELOG.md)

ชุดเอกสาร จับมือทำ (LESSON + LAB) และ mock assets สำหรับหลักสูตร **Power Automate for desktop (PAD) 2 วัน**  
แนวทางหลักคือ Hands-on Labs ทีละขั้นใน designer ควบคู่ Capstone Workshop เพื่อให้ผู้เรียนลงมือสร้าง desktop flow จริง

| รายการ | รายละเอียด |
|--------|------------|
| Web UI (Lab Hub) | [https://ontoiq.tech/pad/](https://ontoiq.tech/pad/) |
| Element UI (Desktop) | [Contoso Invoicing](https://github.com/MicrosoftDocs/mslearn-developer-tools-power-platform/tree/master/power-automate-desktop/contoso-invoice-app) · ดู Lab [07](modules/07-contoso-invoice-ops/README.md) |
| Sample packs อ้างอิง | [Microsoft Learn — power-automate-desktop](https://github.com/MicrosoftDocs/mslearn-developer-tools-power-platform/tree/master/power-automate-desktop) |
| PAD baseline (Aug 2026) | **2607+** (Installer ~2.70.x) — [PAD version matrix](https://learn.microsoft.com/power-platform/released-versions/power-automate-desktop) |
| GitHub Release | [Releases](https://github.com/Onto-IQ/power-automate-desktop/releases) · ดาวน์โหลด **`PAD-Labs.zip`** → แตกที่ `C:\` · [`CHANGELOG.md`](CHANGELOG.md) |
| Course Outline (local) | `slides/Trainocate_Outline_Power Automate Desktop (2 days) ake.pdf` |
| สไลด์ประกอบ (local) | `slides/Power Automate Desktop.pptx` |

> ไฟล์ PPTX/PDF อยู่ที่ [`slides/`](slides/) บนเครื่องทีมสอน — ไม่ได้เผยแพร่ใน GitHub repo

> แต่ละบทแยกเป็น **LESSON.md** (ความรู้) + **LAB.md** (จับมือทำ) · หน้าปกอยู่ที่ `README.md` ของโฟลเดอร์ Lab · พื้นฐานร่วม: [`shared/PAD-FUNDAMENTALS.md`](shared/PAD-FUNDAMENTALS.md)

---

## สารบัญ

- [วัตถุประสงค์](#วัตถุประสงค์)
- [กลุ่มเป้าหมาย](#กลุ่มเป้าหมาย)
- [Prerequisites](#prerequisites)
- [วิธีเริ่มต้น (ผู้เรียน)](#วิธีเริ่มต้น-ผู้เรียน)
- [Selector Convention (PAD Lab Hub)](#selector-convention-pad-lab-hub)
- [แผนการเรียน 2 วัน](#แผนการเรียน-2-วัน)
- [Module Index](#module-index)
- [Phase 1 — Core coverage](#phase-1--core-coverage-pad-lab-hub)
- [โครงสร้าง Repository](#โครงสร้าง-repository)
- [Microsoft Sample Assets](#microsoft-sample-assets-element-ui)
- [หลักปฏิบัติสั้น ๆ](#หลักปฏิบัติสั้น-ๆ)
- [Troubleshooting](#troubleshooting-ภาพรวม)
- [Contributing](#contributing)
- [Changelog](#changelog)
- [Acknowledgments](#acknowledgments)
- [License](#license)
- [Disclaimer](#disclaimer)

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
| สิทธิ์เครือข่าย | เข้าถึง `https://ontoiq.tech/pad/` ได้ · ถ้า Browser Secure Isolation กั้น Lab Hub ใช้ [`modules/03b-public-web-alt/`](modules/03b-public-web-alt/) (ทักษะเทียบ 01 form + 03 table) บน `bot.or.th` / `scb.co.th` |
| **`PAD-Labs.zip`** | โฟลเดอร์ทำงาน `C:\PAD-Labs` seed ครบทุก Module — ดาวน์โหลดจาก [Releases](https://github.com/Onto-IQ/power-automate-desktop/releases) (ดู [`shared/PRECLASS-SETUP.md`](shared/PRECLASS-SETUP.md)) |

---

## วิธีเริ่มต้น (ผู้เรียน)

1. Clone หรือ unzip repo นี้ลงเครื่อง Windows
2. ทำ [`shared/PRECLASS-SETUP.md`](shared/PRECLASS-SETUP.md) ให้ครบ **ก่อนวันเรียน**
3. อ่าน [`shared/PAD-FUNDAMENTALS.md`](shared/PAD-FUNDAMENTALS.md) ให้คุ้น designer และกฎตัวแปร `%`
4. เปิด Lab Hub ที่ [https://ontoiq.tech/pad/](https://ontoiq.tech/pad/) เพื่อยืนยันว่าเข้าถึงได้
5. ในห้องเรียนทำตาม [`shared/CLASSROOM-SCHEDULE-12H.md`](shared/CLASSROOM-SCHEDULE-12H.md) (Core ก่อน Challenge)
6. ต่อหนึ่งบท: เปิด `README.md` → อ่าน **LESSON.md** → ทำ **LAB.md**
7. สร้าง desktop flow **ใหม่ต่อหนึ่ง Lab** และตั้งชื่อตาม convention ใน [`shared/BEST-PRACTICES.md`](shared/BEST-PRACTICES.md)
8. ใช้ไฟล์ใน `modules/<module>/assets/` เป็น input — **ไม่ควรแก้ไฟล์ต้นฉบับใน repo** ให้คัดลอกไปโฟลเดอร์ทำงานของตนเองก่อน

### โฟลเดอร์ทำงานที่แนะนำบนเครื่อง

```text
C:\PAD-Labs\
  ├── working\          ← สำเนา assets ที่แก้ไขได้
  ├── output\           ← ผลลัพธ์จาก flow
  └── logs\             ← log / screenshot จาก Lab 07, 09–10
```

ดาวน์โหลดแพ็กเกจจาก [Releases → `PAD-Labs.zip`](https://github.com/Onto-IQ/power-automate-desktop/releases) แล้วแตกที่ `C:\`  
หรือจาก clone: `.\tools\pad-labs\Install-PAD-Labs.ps1 -FromRepo -Force`  
รายละเอียด: [`shared/PRECLASS-SETUP.md`](shared/PRECLASS-SETUP.md) · [`tools/pad-labs/README.md`](tools/pad-labs/README.md)

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

รายละเอียดเพิ่มเติม: [`shared/SELECTOR-CONVENTIONS.md`](shared/SELECTOR-CONVENTIONS.md) · ชื่อ Action ทางการ: [`shared/OFFICIAL-TERMINOLOGY.md`](shared/OFFICIAL-TERMINOLOGY.md) · เวอร์ชัน PAD: [PAD version matrix](https://learn.microsoft.com/power-platform/released-versions/power-automate-desktop)

> **ตัวแปรใน PAD:** ตอนสร้างชื่อ (Set variable / Store into / **Variables produced**) **ไม่ใส่ `%`** — ตอนใช้ในช่องอื่นใช้ `%ชื่อ%` — ดู [`shared/BEST-PRACTICES.md`](shared/BEST-PRACTICES.md) และ [`shared/PAD-FUNDAMENTALS.md`](shared/PAD-FUNDAMENTALS.md)

สำหรับ Desktop UI ของ Contoso ดู UI map ใน [`modules/07-contoso-invoice-ops/assets/ui-map.md`](modules/07-contoso-invoice-ops/assets/ui-map.md)

---

## แผนการเรียน 2 วัน

> **สอนในห้อง 12 ชม.:** ใช้ตาราง Core/Optional และหน้าที่ TA ใน [`shared/CLASSROOM-SCHEDULE-12H.md`](shared/CLASSROOM-SCHEDULE-12H.md)  
> **ผู้เรียนก่อนวันเรียน:** [`shared/PRECLASS-SETUP.md`](shared/PRECLASS-SETUP.md) · **ทีมสอน (local):** `ops/` (TA cheat sheet, Lab Hub status)

### วันที่ 1 — Fundamentals & Core Actions

| โมดูล | หัวข้อ | Lab |
|-------|--------|-----|
| What is RPA? | แนวคิด RPA, ประโยชน์, Cloud vs Desktop Flows | — |
| Getting Started | ติดตั้ง PAD, Workspace, Actions Pane, Variables, Recorder | [`PAD-FUNDAMENTALS`](shared/PAD-FUNDAMENTALS.md) |
| First Automation | Desktop Recorder, Record & Replay | [01 Record & Replay](modules/01-record-replay/README.md) |
| UI Elements | Selectors และการเปิด/ปิด/โฟกัสแอป | [01b Notepad](modules/01b-notepad/README.md) · [01b Calculator](modules/01b-calculator/README.md) *(optional)* · Contoso เต็มรูปแบบใน Lab 07 |
| File & Folder | Create/Copy/Move/Rename, Read/Write Text | [02 File Management](modules/02-file-management/README.md) |
| Web Automation | Launch browser, Extract table (static / AJAX) | [03 Web Scout](modules/03-web-scout/README.md) · [Static](modules/03-web-scout/static-table/README.md) · [AJAX](modules/03-web-scout/ajax-table/README.md) |

### วันที่ 2 — Advanced Actions, Logic & Capstone

| โมดูล | หัวข้อ | Lab |
|-------|--------|-----|
| Conditional Logic | If / Else If / Else | [04 Conditional Automation](modules/04-conditional-automation/README.md) |
| Loops | For each, Loop condition | [05 Looping Files/Data](modules/05-looping-files-data/README.md) |
| Variables & Data Tables | Types, List, Data Table | [06 Data Table & Excel](modules/06-data-table-excel/README.md) |
| Desktop Element UI | Contoso Invoicing ครบวงจร Excel → App → Excel | [07 Contoso Invoice Ops](modules/07-contoso-invoice-ops/README.md) |
| Excel + Web | Round-trip กับ Lab Hub | [08 Excel ↔ Web Round-trip](modules/08-excel-web-roundtrip/README.md) |
| Error Handling | On block error / On error, Get last error, Logging | [09 Error Handling](modules/09-error-handling/README.md) |
| Best Practices | Subflows, Debugging, Naming | [`shared/BEST-PRACTICES.md`](shared/BEST-PRACTICES.md) |
| Capstone Workshop | Web Scout + Excel + Outlook | [10 Capstone Sales Ops](modules/10-capstone-sales-ops/README.md) |

---

## Module Index

ลำดับต่อบท: อ่าน **ความรู้ (LESSON)** ก่อน → แล้วทำ **Lab (LAB)** ทีละขั้น · พื้นฐานร่วม: [`shared/PAD-FUNDAMENTALS.md`](shared/PAD-FUNDAMENTALS.md)

| # | หน้าปก | ความรู้ | Lab | ทักษะหลัก | UI เป้าหมาย |
|---|--------|--------|-----|-----------|-------------|
| 01 | [Record & Replay](modules/01-record-replay/README.md) | [LESSON](modules/01-record-replay/LESSON.md) | [LAB](modules/01-record-replay/LAB.md) | Recorder และการกรอกฟอร์มเบื้องต้น | [01 Forms](https://ontoiq.tech/pad/01-forms.html) |
| 01b | [Notepad](modules/01b-notepad/README.md) | [LESSON](modules/01b-notepad/LESSON.md) | [LAB](modules/01b-notepad/LAB.md) | UI Elements + Populate Notepad | Windows Notepad |
| 01b | [Calculator](modules/01b-calculator/README.md) *(optional)* | [LESSON](modules/01b-calculator/LESSON.md) | [LAB](modules/01b-calculator/LAB.md) | Click ปุ่ม + อ่าน display | Windows Calculator |
| 02 | [File Management](modules/02-file-management/README.md) | [LESSON](modules/02-file-management/LESSON.md) | [LAB](modules/02-file-management/LAB.md) | File/Folder actions | — |
| 03 | [Web Scout](modules/03-web-scout/README.md) | — | — | แผนที่ + lab ย่อยในโฟลเดอร์เดียวกัน | [pad.ontoiq.tech/pad](https://pad.ontoiq.tech/pad/) |
| 03 | [Static Table](modules/03-web-scout/static-table/README.md) **Core** | [LESSON](modules/03-web-scout/static-table/LESSON.md) | [LAB](modules/03-web-scout/static-table/LAB.md) | Wait + Extract `#tbl-employees` | [03-table](https://pad.ontoiq.tech/pad/03-table.html) |
| 03 | [AJAX Table](modules/03-web-scout/ajax-table/README.md) **Core** | [LESSON](modules/03-web-scout/ajax-table/LESSON.md) | [LAB](modules/03-web-scout/ajax-table/LAB.md) | Wait แถว + กรอง criteria | [09-ajax-table](https://pad.ontoiq.tech/pad/09-ajax-table.html) |
| 03 | [Catalog](modules/03-web-scout/catalog/README.md) *(optional)* | [LESSON](modules/03-web-scout/catalog/LESSON.md) | [LAB](modules/03-web-scout/catalog/LAB.md) | Next loop + Extract products | [19-catalog](https://pad.ontoiq.tech/pad/19-catalog.html) |
| 03 | [Controls](modules/03-web-scout/controls/README.md) *(optional)* | [LESSON](modules/03-web-scout/controls/LESSON.md) | [LAB](modules/03-web-scout/controls/LAB.md) | Dropdown / checkbox | [02-controls](https://pad.ontoiq.tech/pad/02-controls.html) |
| 03 | [Files](modules/03-web-scout/files/README.md) *(optional)* | [LESSON](modules/03-web-scout/files/LESSON.md) | [LAB](modules/03-web-scout/files/LAB.md) | Download / upload | [05-files](https://pad.ontoiq.tech/pad/05-files.html) |
| 03b | [Public Web Alt](modules/03b-public-web-alt/README.md) *(เมื่อ Lab Hub ถูกกั้น)* | [LESSON](modules/03b-public-web-alt/LESSON.md) | Form / Static FX / AJAX FX | ทักษะเทียบ Lab 01 form + Lab 03 table | `bot.or.th` · `scb.co.th` |
| 04 | [Conditional Automation](modules/04-conditional-automation/README.md) | [LESSON](modules/04-conditional-automation/LESSON.md) | [LAB](modules/04-conditional-automation/LAB.md) | If/Else ตาม business rules | — |
| 05 | [Looping Files/Data](modules/05-looping-files-data/README.md) | [LESSON](modules/05-looping-files-data/LESSON.md) | [LAB](modules/05-looping-files-data/LAB.md) | For each กับไฟล์และแถวข้อมูล | — |
| 06 | [Data Table & Excel](modules/06-data-table-excel/README.md) | [LESSON](modules/06-data-table-excel/LESSON.md) | [LAB](modules/06-data-table-excel/LAB.md) | อ่าน แปลง และเขียน Excel | — |
| 07 | [Contoso Invoice Ops](modules/07-contoso-invoice-ops/README.md) | [LESSON](modules/07-contoso-invoice-ops/LESSON.md) | [LAB](modules/07-contoso-invoice-ops/LAB.md) | Desktop UI, validate, attachments, subflows | **Contoso Invoicing** |
| 08 | [Excel ↔ Web Round-trip](modules/08-excel-web-roundtrip/README.md) | [LESSON](modules/08-excel-web-roundtrip/LESSON.md) | [LAB](modules/08-excel-web-roundtrip/LAB.md) | Login + Forms + Wizard (+ Iframe/Files challenge) | [06](https://ontoiq.tech/pad/06-login.html) · [01](https://ontoiq.tech/pad/01-forms.html) · [07](https://ontoiq.tech/pad/07-wizard.html) |
| 09 | [Error Handling](modules/09-error-handling/README.md) | [LESSON](modules/09-error-handling/LESSON.md) | [LAB](modules/09-error-handling/LAB.md) | Retry/log + Dialog/Delay (+ OCR/Files/Iframe/API) | [04](https://ontoiq.tech/pad/04-dialogs.html) · [11](https://ontoiq.tech/pad/11-delay.html) · [01](https://ontoiq.tech/pad/01-forms.html) |
| 10 | [Capstone Sales Ops](modules/10-capstone-sales-ops/README.md) | [LESSON](modules/10-capstone-sales-ops/LESSON.md) | [LAB](modules/10-capstone-sales-ops/LAB.md) | Scout + Round-trip + Outlook และชุด Phase 1 | ตามโจทย์ Capstone |

---

## Phase 1 — Core coverage (PAD Lab Hub)

อ้างอิงแผนที่บทเรียน: [https://ontoiq.tech/pad/](https://ontoiq.tech/pad/)

| โมดูล | การใช้ใน Lab Kit |
|-------|------------------|
| 01 Forms | Lab 01 (หลัก) · 08 · 09 · 10 |
| 02 Controls | [Lab 03 Controls](modules/03-web-scout/controls/README.md) *(optional)* |
| 03 Table | [Lab 03 Static Table](modules/03-web-scout/static-table/README.md) · 10 |
| 04 Dialogs | Lab 09 Case D |
| 05 Files | [Lab 03 Files](modules/03-web-scout/files/README.md) *(optional)* · 08 Challenge J · 09 Case G · 10 Mission |
| 06 Login | Lab 08 (บังคับ) · 10 |
| 07 Wizard | Lab 08 Mission W · 10 Mission |
| 08 Iframe | Lab 03 โบนัส (hub) · 08 Challenge I · 09 Case H · 10 Challenge |
| 09 AJAX Table | [Lab 03 AJAX Table](modules/03-web-scout/ajax-table/README.md) · 10 |
| 10 OCR | Lab 09 Case F · 10 Challenge |
| 11 Delay | Lab 09 Case C |
| 12 API | Lab 03 โบนัส (hub) · 09 Case I · 10 Challenge |

> Lab 03 แยกเป็นหลาย flow ใต้ [03-web-scout](modules/03-web-scout/README.md)  
> **19 Catalog** (pagination): [Lab 03 Catalog](modules/03-web-scout/catalog/README.md) *(optional)* และ Lab 10

---

## โครงสร้าง Repository

```text
power-automate-desktop/
├── README.md                          ← คุณอยู่ที่นี่
├── LICENSE                            ← MIT
├── CHANGELOG.md                       ← Keep a Changelog / SemVer
├── tools/pad-labs/                    ← Build/Install PAD-Labs.zip
├── shared/                            ← พื้นฐาน + เอกสารผู้เรียน
│   ├── PAD-FUNDAMENTALS.md            ← อ่านก่อน Module แรก
│   ├── PRECLASS-SETUP.md              ← รวมลิงก์ดาวน์โหลด PAD-Labs.zip
│   └── CLASSROOM-SCHEDULE-12H.md
├── authoring/                         ← คู่มือผู้เขียน (local)
├── ops/                               ← ทีมสอน / Lab Hub (local)
├── slides/                            ← PPTX/PDF หลักสูตร (local)
├── modules/
│   ├── 01-record-replay/
│   │   ├── README.md                  ← หน้าปก / สารบัญบท
│   │   ├── LESSON.md                  ← ความรู้ (อ่านก่อน)
│   │   ├── LAB.md                     ← จับมือทำทีละขั้น
│   │   └── assets/
│   ├── 01b-notepad/
│   ├── 01b-calculator/
│   ├── 02-file-management/            ← ตัวอย่างมาตรฐานโครงสร้าง 3 ไฟล์
│   ├── 03-web-scout/                  ← Lab 03 index + static-table / ajax-table / …
│   ├── 03b-public-web-alt/            ← เส้นทดแทนเมื่อ Lab Hub ถูกกั้น (ทักษะเทียบ 01 form + 03 table)
│   ├── …
│   └── 10-capstone-sales-ops/
└── …
```

แต่ละ **Module** มี 3 เอกสารหลัก:

- `README.md` — หน้าปกบท: meta, ลำดับเรียน, prerequisites, ลิงก์ LESSON/LAB
- `LESSON.md` — เอกสารความรู้เต็ม (ศัพท์ แนวคิด คำถามทบทวน)
- `LAB.md` — Setup + Hands-on ทีละขั้นใน designer
- `assets/` — mock input / expected output เมื่อ Module นั้นต้องการไฟล์ตัวอย่าง

> โฟลเดอร์รากของบทเรียนคือ **`modules/`** — คำว่า **Lab** ยังใช้กับไฟล์ `LAB.md` และการอ้างอิงแบบ Lab 01, Lab 02 ตามเดิม  
> คู่มือทีมอยู่ที่ [`authoring/`](authoring/) · [`ops/`](ops/) · [`slides/`](slides/) บนเครื่องทีมพัฒนา (ไม่เผยแพร่ใน GitHub สำหรับผู้เรียน)

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

## Contributing

ยินดีรับ feedback จากวิทยากร / TA ที่ใช้ชุดนี้ในห้องจริง

1. เปิด [Issue](https://github.com/Onto-IQ/power-automate-desktop/issues) อธิบายปัญหา Lab, selector ที่พัง หรือข้อเสนอแนะหลักสูตร
2. สำหรับ Pull Request: แก้เฉพาะ Module ที่เกี่ยวข้อง ให้ LESSON / LAB / catch-up `scripts/*.robin` สอดคล้องกัน
3. อย่า commit โฟลเดอร์ส่วนตัว `C:\PAD-Labs\`, `working/`, `output/`, `logs/` หรือสไลด์ภายใต้ `slides/`

ถ้าต้องการช่วยจัดตารางห้องหรือ catch-up ดูแนวทางใน [`shared/CLASSROOM-SCHEDULE-12H.md`](shared/CLASSROOM-SCHEDULE-12H.md)

---

## Changelog

ดูประวัติเวอร์ชันแบบ SemVer ใน [`CHANGELOG.md`](CHANGELOG.md)  
แพ็กเกจผู้เรียนล่าสุด: [GitHub Releases](https://github.com/Onto-IQ/power-automate-desktop/releases) (`PAD-Labs.zip`)

---

## Acknowledgments

- [Microsoft Learn — Power Automate Desktop samples](https://github.com/MicrosoftDocs/mslearn-developer-tools-power-platform/tree/master/power-automate-desktop) และ **Contoso Invoicing**
- [Power Automate for desktop documentation](https://learn.microsoft.com/power-automate/desktop-flows/)
- Onto-IQ PAD Lab Hub ที่ [ontoiq.tech/pad](https://ontoiq.tech/pad/)

---

## License

เอกสาร Lab Kit, scripts (`.robin`), mock assets และเครื่องมือใน repo นี้เผยแพร่ภายใต้ [**MIT License**](LICENSE) — Copyright © 2026 Onto-IQ

| ส่วนประกอบ | สิทธิ์ / เงื่อนไข |
|------------|-------------------|
| เนื้อหาใน repo นี้ (docs, scripts, tools, mock data) | [MIT](LICENSE) |
| PAD Lab Hub (`ontoiq.tech/pad`) | ทรัพย์สินของ Onto-IQ สำหรับใช้ประกอบการฝึกอบรม — ไม่รวมใน LICENSE ของ repo |
| Contoso Invoicing / Microsoft sample packs | อยู่ภายใต้เงื่อนไขของ [Microsoft Docs repository](https://github.com/MicrosoftDocs/mslearn-developer-tools-power-platform) ต้นทาง |
| Power Automate for desktop | ผลิตภัณฑ์ของ Microsoft — ติดตั้งและใช้ตามข้อกำหนดสิทธิ์ขององค์กรผู้เรียน |

---

## Disclaimer

- Mock data ใน repo นี้เป็นข้อมูลจำลอง ไม่ใช่ข้อมูลลูกค้าจริง
- Lab Kit นี้ไม่ใช่เอกสารทางการของ Microsoft และไม่รับประกันความเข้ากันได้กับทุกเวอร์ชันของ PAD นอกเหนือจาก baseline ที่ระบุใน Release
- การส่งอีเมลจริง การรันบนเครื่อง production หรือการเชื่อมระบบองค์กรอยู่นอกขอบเขตหลักสูตร — ใช้เฉพาะสภาพแวดล้อมฝึกตามที่วิทยากรกำหนด
