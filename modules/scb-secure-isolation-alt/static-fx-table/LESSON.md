# Static FX Table — ความรู้

**อ่านก่อน:** [LAB.md](LAB.md) · **หน้าปก:** [README.md](README.md)

## ทำไมใช้ตารางนี้

Lab 03 Static ใช้ `#tbl-employees` บน Lab Hub  
ชุดนี้ใช้ตารางสถิติอัตราแลกเปลี่ยนของ ธปท. ซึ่ง:

- อยู่ในโดเมน `app.bot.or.th` (อนุญาตใน SCB ได้โดยทั่วไป)
- เป็น HTML table ที่ Extract ได้ด้วย **Extract Entire HTML Table**
- ข้อมูลสาธารณะ — ไม่อ่านข้อมูลลูกค้า

## หน้าเป้าหมาย

| รายการ | ค่า |
|--------|-----|
| URL | https://app.bot.or.th/BTWS_STAT/statistics/ReportPage.aspx?language=TH&reportID=123 |
| ชื่อรายงาน | FM_FX_001_S3 อัตราแลกเปลี่ยนเฉลี่ยของธนาคารพาณิชย์… |
| UI element | Rename เป็น `Tbl_BotFx` |

## ต่างจาก Lab Hub

| Lab Hub 03-table | ธปท. ReportPage |
|------------------|-----------------|
| มี `#tbl-employees` | ต้อง Picker เอง — ไม่มี `data-pad` |
| แถวน้อย คอลัมน์คงที่ | แถว/คอลัมน์วันที่เปลี่ยนตามวันเผยแพร่ |
| ไม่มี dropdown ช่วงเวลา | มีตัวกรองช่วงเวลา (ใช้เป็น Controls optional ได้) |

หลัง Extract ให้เปิด `%BotFxTable%` ใน Variables pane แล้ว**จดชื่อคอลัมน์จริง**ก่อนเขียน CSV

## อ้างอิง

- [Web automation](https://learn.microsoft.com/power-automate/desktop-flows/automation-web)
- [UI elements](https://learn.microsoft.com/power-automate/desktop-flows/ui-elements)
