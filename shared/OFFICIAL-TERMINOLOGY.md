# Official terminology — Power Automate for desktop

เอกสารนี้ช่วยให้ชื่อ Action และศัพท์ใน Lab Kit สอดคล้องกับ Microsoft Learn  
(ตรวจอ้างอิงล่าสุดปี 2026) และยังคง keyphrase ภาษาอังกฤษตามทางการ โดยไม่แปลชื่อ Action

| หัวข้อ | URL |
|--------|-----|
| Install | https://learn.microsoft.com/power-automate/desktop-flows/install |
| Handle errors | https://learn.microsoft.com/power-automate/desktop-flows/errors |
| Web automation | https://learn.microsoft.com/power-automate/desktop-flows/automation-web |
| Web actions | https://learn.microsoft.com/power-automate/desktop-flows/actions-reference/webautomation |
| UI automation | https://learn.microsoft.com/power-automate/desktop-flows/actions-reference/uiautomation |
| Excel actions | https://learn.microsoft.com/power-automate/desktop-flows/actions-reference/excel |
| System actions | https://learn.microsoft.com/power-automate/desktop-flows/actions-reference/system |

## Product naming

| ใช้ใน Lab Kit | ความหมาย |
|---------------|----------|
| **Power Automate for desktop** | ชื่อผลิตภัณฑ์ทางการ (ย่อ PAD ได้) |
| **desktop flow** | Flow ที่สร้าง/รันบน PAD |
| **Cloud flow** | Flow บน Power Automate cloud (คู่กันในระบบนิเวศ) |

หลีกเลี่ยงการใช้คำว่า “Try-Catch” เป็นชื่อ Action เพราะใน PAD ใช้กลไกตามตารางด้านล่างแทน

## Error handling (ทางการ)

| กลไก | ใช้เมื่อ |
|------|---------|
| **On error** (ในแต่ละ action) | Retry / Continue flow run / Set variable / Run subflow |
| **On block error** | ครอบหลาย action ด้วยนโยบายเดียวกัน |
| **Get last error** | ดึง error object ล่าสุด (มี message, location, subflow, …) |
| **Terminate process** / จบ flow ตามสถานการณ์ | หยุด process หรือออกแบบให้ flow จบอย่างควบคุม |

ตัวแปรแนะนำหลัง Get last error คือ `%LastError%` (ชนิด Error) จากนั้นอ้าง `%LastError.Message%` และ `%LastError.Location%` ตาม properties จริงใน designer

## Action names ที่ Lab Kit ใช้ (สะกดตาม docs)

### Browser / Web

| Action (official) |
|-------------------|
| Launch new Microsoft Edge |
| Launch new Chrome |
| Go to web page |
| Wait for web page content |
| Populate text field on web page |
| Press button on web page |
| Click link on web page |
| Set drop-down list value on web page |
| Set check box state on web page |
| Select radio button on web page |
| Extract data from web page *(เปิด **live web helper**)* |
| Take screenshot of web page |
| Close web browser |

### Desktop UI

| Action (official) |
|-------------------|
| Run application |
| Focus window |
| Populate text field in window |
| Click UI element in window |
| Press button in window |
| Wait for window content |
| Close window |
| Terminate process |

### Excel

| Action (official) |
|-------------------|
| Launch Excel |
| Read from Excel worksheet |
| Write to Excel worksheet |
| Run Excel macro |
| Get first free row on column from Excel worksheet |
| Close Excel |

### Files / Logic (ชื่อที่พบบ่อยใน designer)

| Action |
|--------|
| If folder exists / If file exists |
| Get files in folder |
| Copy file(s) / Move file(s) |
| Write text to file / Read text from file |
| For each |
| Loop / Loop condition |
| If / Else / Else if |
| Create new data table / Insert row into data table |

## Consistency rules สำหรับผู้เขียน Lab

1. เขียนชื่อ Action **ตรงตัว** ตามตารางด้านบน (ภาษาอังกฤษ) ครั้งแรกในลำดับขั้นตอน  
2. คำอธิบายภาษาไทยวางหลังหรือในวงเล็บได้ เช่น `Wait for web page content` (รอเนื้อหาหน้าเว็บ)  
3. อย่าใช้ `Launch application` → ใช้ **Run application**  
4. อย่าใช้ `Try-Catch` เป็นชื่อ Action → ใช้ **On block error** / **On error**  
5. ตัวช่วยดึงข้อมูลเว็บเรียกว่า **live web helper** (ไม่ใช่ Live Helper อย่างเดียวโดยไม่มีบริบท)  
6. Browser instance / Excel instance มาจาก Launch action ก่อน แล้วส่งต่อใน action ถัดไป  

## หมายเหตุจากหลักสูตรสไลด์ vs docs

| ในสไลด์ Trainocate | ใน Lab Kit / official |
|--------------------|------------------------|
| Activate Phone Number Input | ไม่ใช้เป็นเกณฑ์บังคับ — เป็นเคสเฉพาะในบางโมดูล Learn; Lab 09 ใช้ Wait/Focus/On error แทน |
| Try-Catch | อธิบายแนวคิดได้ แต่ลงมือด้วย On block error |
| Live Web Helper | **live web helper** ของ Extract data from web page |
