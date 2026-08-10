# Form Search — ความรู้

**อ่านก่อน:** [LAB.md](LAB.md) · **หน้าปก:** [README.md](README.md)

## ทำไมใช้หน้าค้นหาแทน 01-forms

Lab 01 สอน Populate หลายช่องแล้ว Submit  
บนโดเมนที่อนุญาตใน SCB **ไม่มีฟอร์มฝึกที่ปลอดภัยเทียบเท่า Lab Hub**  
หน้าค้นหา ธปท. ให้ทักษะเดียวกันในแกนหลัก: Launch → Populate → Press button → Wait → Replay โดยไม่สร้างธุรกรรม/ticket

## หน้าเป้าหมาย

| รายการ | ค่า |
|--------|-----|
| URL | https://www.bot.or.th/th/search.html |
| โดเมน | `www.bot.or.th` |
| Input หลัก | ช่องค้นหา (UI Picker → Rename `Txt_Search`) |
| Action หลัก | ปุ่มค้นหา / Enter (`Btn_Search`) |
| ผลลัพธ์ | หน้ารายการผลค้นหา — เก็บ screenshot เป็นหลักฐาน |

## Pattern ที่ต้องได้

```text
Browser = Launch Edge/Chrome → https://www.bot.or.th/th/search.html
(optional) กดคุกกี้ “จำเป็นเท่านั้น”
Populate Txt_Search = %SearchKeyword%
Press Btn_Search
Wait for web page content (ผลค้นหา / หัวข้อผลลัพธ์)
Take screenshot → C:\PAD-Labs\output\lab-scb-alt\search-proof.png
Close browser
```

## อ้างอิง

- [Web automation](https://learn.microsoft.com/power-automate/desktop-flows/automation-web)
- [Populate text field](https://learn.microsoft.com/power-automate/desktop-flows/actions-reference/webautomation)
