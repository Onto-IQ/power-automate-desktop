# Selector Conventions — PAD Lab Hub

แหล่งอ้างอิง: [https://ontoiq.tech/pad/](https://ontoiq.tech/pad/)

## หลักการ

1. เลือก element ด้วย **UI element picker** ใน Power Automate Desktop
2. ตรวจ/ล็อก selector ให้ใช้ `id` หรือ `data-pad` เป็นหลัก
3. หลีกเลี่ยงตำแหน่งสัมพัทธ์ยาว ๆ และ text ที่เปลี่ยนบ่อย

## รูปแบบที่แนะนำ

| รูปแบบ | ตัวอย่าง | ใช้เมื่อ |
|--------|----------|---------|
| CSS id | `#txt-name` | มี id คงที่ |
| data attribute | `[data-pad="btn-submit"]` | Lab Hub ระบุ data-pad |
| รวม attribute | `input#txt-email` | ต้องการความเฉพาะเจาะจง |

## แผนที่โมดูล Lab Hub

| โมดูล | URL | ทักษะ |
|-------|-----|--------|
| 01 Forms | https://ontoiq.tech/pad/01-forms.html | Fill text, validate, submit |
| 02 Controls | https://ontoiq.tech/pad/02-controls.html | Click, dropdown, checkbox, radio |
| 03 Table | https://ontoiq.tech/pad/03-table.html | Extract HTML table |
| 04 Dialogs | https://ontoiq.tech/pad/04-dialogs.html | Alert / confirm / modal |
| 05 Files | https://ontoiq.tech/pad/05-files.html | Download / upload |
| 06 Login | https://ontoiq.tech/pad/06-login.html | Auth `demo` / `demo` |
| 07 Wizard | https://ontoiq.tech/pad/07-wizard.html | Multi-step |
| 08 Iframe | https://ontoiq.tech/pad/08-iframe.html | Switch iframe |
| 09 AJAX Table | https://ontoiq.tech/pad/09-ajax-table.html | Wait dynamic rows |
| 10 OCR | https://ontoiq.tech/pad/10-ocr.html | OCR compare |
| 11 Delay | https://ontoiq.tech/pad/11-delay.html | Countdown / gate |
| 12 API | https://ontoiq.tech/pad/12-api.html | HTTP mock |
| 13 Hover | https://ontoiq.tech/pad/13-hover.html | Hover / tooltip |
| 14 JavaScript | https://ontoiq.tech/pad/14-javascript.html | Execute JS |
| 15 Multi-select | https://ontoiq.tech/pad/15-multiselect.html | Multi options |
| 16 Shadow DOM | https://ontoiq.tech/pad/16-shadow.html | Shadow root |
| 17 Cross iframe | https://ontoiq.tech/pad/17-cross-iframe.html | Cross-origin |
| 18 Popup | https://ontoiq.tech/pad/18-popup.html | Popup / new tab |

## Wait Strategy

| สถานการณ์ | Action ที่แนะนำ (official) |
|-----------|------------------------------|
| โหลดหน้า / รอ element เว็บ | **Wait for web page content** |
| รอเนื้อหาในหน้าต่าง Desktop | **Wait for window content** |
| ตาราง AJAX / catalog เปลี่ยนหน้า | Wait for web page content จนแถว/ตารางพร้อม ก่อน Extract |
| Dialog / Modal | Wait for window content หรือ element ของ modal |
| Popup / Tab | สลับ tab/window แล้ว Wait ก่อน Interact |
| Delay / Captcha-like | Wait + อ่านค่าจากหน้า ตาม Lab 11 |

อ้างอิง: [Web automation actions](https://learn.microsoft.com/power-automate/desktop-flows/actions-reference/webautomation) · [UI automation](https://learn.microsoft.com/power-automate/desktop-flows/actions-reference/uiautomation) · [`OFFICIAL-TERMINOLOGY.md`](OFFICIAL-TERMINOLOGY.md)

## Validation Checklist

- [ ] Selector ยังชี้ element เดิมหลัง refresh หน้า
- [ ] ไม่พึ่งพาข้อความภาษาที่เปลี่ยนตาม locale
- [ ] มี Wait ก่อน Interact
- [ ] ตั้งชื่อ UI element ใน PAD ให้สื่อความหมาย เช่น `Btn_SubmitForm`
