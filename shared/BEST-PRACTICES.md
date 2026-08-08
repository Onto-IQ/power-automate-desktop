# Best Practices — Power Automate for desktop Labs

เอกสารนี้รวบรวมแนวทางตั้งชื่อตัวแปร โครงสร้าง flow และจุดควรระวังเวลาทำ Lab  
อ้างอิงชื่อ Action ทางการได้จาก [`OFFICIAL-TERMINOLOGY.md`](OFFICIAL-TERMINOLOGY.md) และ [Handle errors](https://learn.microsoft.com/power-automate/desktop-flows/errors)  
แนวเขียนภาษาไทยดู [`WRITING-STYLE.md`](WRITING-STYLE.md)

## Naming

| ประเภท | Convention | ตัวอย่าง |
|--------|------------|----------|
| Flow | `LabXX_ShortName` | `Lab07_ContosoInvoiceOps` |
| Subflow | `SF_<VerbNoun>` | `SF_WriteExcelReport` |
| UI Element | `Ctrl_<Role>` | `Txt_CustomerName`, `Btn_Submit` |
| Variable | `%PascalCase%` หรือคำนำหน้าบทบาท | `%InputLeads%`, `%LastError%` |

## Variable & Data Table Contract

| ชื่อแนะนำ | ชนิด | ความหมาย |
|-----------|------|----------|
| `%WorkingRoot%` | Text | โฟลเดอร์ทำงาน เช่น `C:\PAD-Labs\working` |
| `%OutputRoot%` | Text | โฟลเดอร์เก็บผลลัพธ์ |
| `%Browser%` | Browser instance | ได้จาก Launch new Edge/Chrome |
| `%Excel%` | Excel instance | ได้จาก Launch Excel |
| `%InputTable%` | Data table | ข้อมูลที่อ่านจาก Excel/CSV |
| `%ResultTable%` | Data table | ผลที่ดึงจากเว็บหรือประมวลผลแล้ว |
| `%RowIndex%` | Numeric | ดัชนีแถวในลูป |
| `%LastError%` | Error (จาก **Get last error**) | อ้างต่อด้วย `%LastError.Message%` / `.Location%` |
| `%RetryCount%` | Numeric | นับจำนวนครั้งที่ retry |

## Flow Structure ที่แนะนำ

```text
Main
├── Init (paths, counters, empty tables)
├── On block error (ครอบงานเสี่ยง)
│   ├── Run application / Launch Excel / Launch new Edge
│   ├── Process (For each / If / Loop condition)
│   └── Write outputs
├── On error path
│   ├── Get last error → log
│   ├── Take screenshot of web page (ถ้าเป็น UI เว็บ)
│   └── Optional Run subflow / retry จำกัด
└── Cleanup
    ├── Close Excel
    ├── Close web browser
    └── Display / Notification
```

ใน PAD ให้ใช้ **On block error** ร่วมกับ **On error** ของแต่ละ action (เช่น Retry หรือ Continue flow run)  
คำว่า “Try-Catch” ใช้อธิบายแนวคิดได้ แต่ไม่ใช่ชื่อ Action ใน designer

## Subflows ที่ใช้ซ้ำได้ (Capstone)

| Subflow | หน้าที่ |
|---------|---------|
| `SF_InitPaths` | ตั้งค่า path และสร้างโฟลเดอร์หากยังไม่มี |
| `SF_OpenLabHub` | Launch new Edge/Chrome ไปยัง URL ที่กำหนด |
| `SF_ReadExcelSheet` | Read from Excel worksheet แล้วได้ Data table |
| `SF_WriteExcelSheet` | Write to Excel worksheet |
| `SF_LaunchContoso` | Run application และ Focus window ของ Contoso |
| `SF_CreateContosoInvoice` | Populate text field in window / Press button |
| `SF_ScoutCatalog` | Extract data from web page พร้อมลูปหน้า Next |
| `SF_SendOutlookDraft` | สร้างอีเมล Draft และแนบรายงาน |
| `SF_LogError` | Get last error แล้ว Write text to file |

## Excel

- เมื่อมี header ให้เปิดตัวเลือก **First line of range contains column names**
- ปิดด้วย **Close Excel** ทุกครั้ง แม้เกิด error
- แยก sheet ให้ชัด เช่น `Input`, `Results`, `Summary` / `Priced`
- ไม่ควรเขียนทับไฟล์ต้นฉบับใน `assets/` — ให้เขียนไปที่ `output/`
- หากใช้ macro ให้เรียก **Run Excel macro** บนไฟล์ `.xlsm` เท่านั้น

## Outlook

- ใช้ผู้รับจำลองจาก `recipients.csv`
- ค่าเริ่มต้นของ Lab คือสร้างเป็น **Draft**
- ตรวจเนื้อหาและไฟล์แนบให้เรียบร้อยก่อนส่งจริง
- ห้ามใส่ข้อมูลส่วนบุคคลจริงใน subject/body ตัวอย่าง

## Debugging (ใน flow designer)

1. ใช้ Breakpoints หรือ Run next action
2. ตรวจค่าใน Variables pane
3. ดู Errors pane และใช้ Get last error เมื่อต้องการรายละเอียด
4. เปรียบเทียบผลกับโฟลเดอร์ `assets/expected/` ของ Lab

## Security

- ห้าม commit password หรือ API key จริง
- บัญชี demo ของ Lab Hub คือ `demo` / `demo` (สำหรับฝึกเท่านั้น)
- เมื่อเชื่อมต่อบริการจริง ให้ใช้บัญชีองค์กรตามนโยบาย
- รัน PAD และแอปเป้าหมายด้วยสิทธิ์ elevation เดียวกัน ([UIPI guidance](https://learn.microsoft.com/troubleshoot/power-platform/power-automate/desktop-flows/ui-automation/uipi-issues))
