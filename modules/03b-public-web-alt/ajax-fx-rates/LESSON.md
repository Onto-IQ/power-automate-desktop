# AJAX FX Rates — ความรู้

**อ่านก่อน:** [LAB.md](LAB.md) · **หน้าปก:** [README.md](README.md)

## ทำไมหน้านี้แทน 09-ajax-table

หน้าอัตราแลกเปลี่ยนสาธารณะโหลดเรทแบบ dynamic (ไม่ใช่ HTML table คงที่แบบ static ล้วน)  
จึงเหมาะฝึกทักษะเดียวกับ Lab 03 AJAX: **Wait for content → Extract → กรอง**

| Lab Hub 09-ajax | Lab 03b Ajax FX |
|-----------------|-----------------|
| ปุ่ม Refresh orders | หน้าโหลดเรทอัตโนมัติ — Wait แถวสกุลเงิน |
| `#tbl-orders` | Picker ตาราง/แถวเรท → `Tbl_FxRates` |
| กรอง Amount ≥ MinAmount | กรองข้อความสกุลเงิน เช่น มี `USD` |

## หน้าเป้าหมาย

| รายการ | ค่า |
|--------|-----|
| URL | https://www.scb.co.th/th/personal-banking/foreign-exchange-rates |
| โดเมน | `www.scb.co.th` (ตัวอย่างหน้าสาธารณะ) |
| ผลลัพธ์ที่ต้องการ | อย่างน้อยแถว USD (หรือสกุลใน `%CurrencyCode%`) ลง CSV |

## ข้อควรระวัง

- โครงสร้างหน้าอาจเปลี่ยนตามแคมเปญเว็บ — **จดชื่อคอลัมน์จาก Variables pane หลัง Extract**
- ถ้า Extract Entire HTML Table ไม่โผล่: ใช้ Extract แบบชี้เซลล์/รายการซ้ำ (PAD live web helper) แล้วเก็บเป็น Data table
- **ห้าม** เข้าสู่ระบบหรือกดไปหน้าทำธุรกรรมแลกเงินจริง

## อ้างอิง

- [Web automation](https://learn.microsoft.com/power-automate/desktop-flows/automation-web)
- [Variables / If](https://learn.microsoft.com/power-automate/desktop-flows/actions-reference/variables)
