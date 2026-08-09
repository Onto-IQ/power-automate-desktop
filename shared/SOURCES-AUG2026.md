# แหล่งอ้างอิง — สิงหาคม 2026 เท่านั้น

ใช้เมื่อเขียนหรือทบทวน Lab Kit ให้สอดคล้องกับ **Power Automate for desktop** ช่วงสิงหาคม 2026  
(เวอร์ชันหลักในสนาม: **2607 / 2607-update**; **2608** ทยอย mid-August 2026)

## Official — Microsoft Learn / Release notes

| หัวข้อ | URL | ใช้กับ Lab |
|--------|-----|------------|
| PAD version matrix | https://learn.microsoft.com/power-platform/released-versions/power-automate-desktop | ทุกบท (baseline) |
| 2607 release notes | https://learn.microsoft.com/power-platform/released-versions/power-automate-desktop/2607 | Tips / preview features |
| 2606 release notes | https://learn.microsoft.com/power-platform/released-versions/power-automate-desktop/2606 | Default variable values, Get UI/web control |
| Coding guidelines (desktop flows) | https://learn.microsoft.com/power-automate/guidance/desktop-flow-coding-guidelines/ | โครงสร้าง flow, performance |
| Getting started (free org) — file backup pattern | https://learn.microsoft.com/power-automate/desktop-flows/getting-started-freeorg | **Lab 02** (Get files → For each → Get file path part → Copy) |
| Folder actions | https://learn.microsoft.com/power-automate/desktop-flows/actions-reference/folder | Lab 02, 04, 05 |
| File actions | https://learn.microsoft.com/power-automate/desktop-flows/actions-reference/file | Lab 02, 04, 05 |
| Handle errors | https://learn.microsoft.com/power-automate/desktop-flows/errors | Lab 07, 09, 10 |
| Web automation | https://learn.microsoft.com/power-automate/desktop-flows/automation-web | Lab 01, 03, 08, 10 |
| Web actions reference | https://learn.microsoft.com/power-automate/desktop-flows/actions-reference/webautomation | Lab 01, 03, 08–10 |
| UI automation actions | https://learn.microsoft.com/power-automate/desktop-flows/actions-reference/uiautomation | Lab 01b, 07 |
| Excel actions | https://learn.microsoft.com/power-automate/desktop-flows/actions-reference/excel | Lab 06–08, 10 |
| Actions pane / On error | https://learn.microsoft.com/power-automate/desktop-flows/actions-pane | ทุกบท |
| Install PAD | https://learn.microsoft.com/power-automate/desktop-flows/install | Prerequisites |
| Contoso setup (Learn) | https://learn.microsoft.com/training/modules/input-parameters/2-set-up | Lab 07 |
| Contoso sample app | https://github.com/MicrosoftDocs/mslearn-developer-tools-power-platform/tree/master/power-automate-desktop/contoso-invoice-app | Lab 07 |
| Excel troubleshooting | https://learn.microsoft.com/troubleshoot/power-platform/power-automate/desktop-flows/office-automation/excel/troubleshoot-excel-errors | Lab 06+ |
| UIPI issues | https://learn.microsoft.com/troubleshoot/power-platform/power-automate/desktop-flows/ui-automation/uipi-issues | Lab 01b, 07 |

## Official — Blog (July/August 2026 window)

| หัวข้อ | URL |
|--------|-----|
| What’s new in Power Platform: July/August 2026 | https://www.microsoft.com/en-us/power-platform/blog/2026/08/06/whats-new-in-power-platform-july-august-2026-feature-update/ |

ประเด็นที่เกี่ยวกับ PAD ในช่วงนี้ (อ้างอิง blog + release notes): AI-assisted UI automation repair (preview), Self-healing, PGP cryptography reference, Flowchart designer (preview ใน 2607)

## Community (สิงหาคม 2026 / ใกล้เคียง)

| แหล่ง | URL | หมายเหตุ |
|-------|-----|----------|
| Agnius Bartninkas — สรุป PAD 2607 (July 2026) | https://www.linkedin.com/posts/agnius-bartninkas_the-release-notes-for-the-power-automate-activity-7485244071339311107-SXgZ | Flowchart, UI repair agent, static analysis — ใช้เป็น Tips ไม่บังคับในเกณฑ์ผ่าน |
| Power Users / Learn Q&A Contoso | https://learn.microsoft.com/answers/questions/2244882/how-to-resolve-contoso-invoicing-app-issue | Lab 07 troubleshooting |

> Community อื่นนอกช่วง Jul–Aug 2026 ไม่ใช้เป็นเกณฑ์หลักของ Lab Kit รอบนี้

## สิ่งที่ Lab Kit **บังคับ** vs **Tips (preview)**

| ใช้เป็นขั้นตอนบังคับ | ใส่เป็น Tips / Challenge เท่านั้น |
|----------------------|----------------------------------|
| Actions เสถียร: Folder/File, For each, If, Web, Excel, On block error | Flowchart designer view (preview) |
| Wait for web/window content (ไม่พึ่ง Wait วินาทีอย่างเดียว) | AI-assisted UI repair (preview) |
| Get last error + log | Get UI control / Get web control (dynamic selectors) |
| Close Excel / Close web browser / Close window | Default values ของตัวแปร (2606) — ใช้ได้ถ้ามีใน designer |

## Baseline เวอร์ชันสำหรับชั้นเรียน (Aug 2026)

แนะนำให้ผู้เรียนอัปเดต PAD เป็นอย่างน้อย **2607** (Installer ~2.70.x / Store 11.2607.x)  
ตรวจเวอร์ชันที่ Console → Settings / About ตามผลิตภัณฑ์
