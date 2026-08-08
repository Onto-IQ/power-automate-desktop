# Best Practices — Power Automate for desktop Labs

อ้างอิงชื่อ Action ทางการ: [`OFFICIAL-TERMINOLOGY.md`](OFFICIAL-TERMINOLOGY.md) · [Handle errors](https://learn.microsoft.com/power-automate/desktop-flows/errors)

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
| `%OutputRoot%` | Text | โฟลเดอร์ผลลัพธ์ |
| `%Browser%` | Browser instance | จาก Launch new Edge/Chrome |
| `%Excel%` | Excel instance | จาก Launch Excel |
| `%InputTable%` | Data table | ข้อมูลอ่านจาก Excel/CSV |
| `%ResultTable%` | Data table | ผลที่ดึงจาก Web หรือประมวลผลแล้ว |
| `%RowIndex%` | Numeric | index ในลูป |
| `%LastError%` | Error (จาก **Get last error**) | ใช้ `%LastError.Message%` / `.Location%` |
| `%RetryCount%` | Numeric | นับครั้ง retry |

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

ใน PAD ใช้ **On block error** + **On error** ของแต่ละ action (Retry / Continue flow run)  
อย่าเรียกชื่อ Action ว่า “Try-Catch” — เป็นได้แค่คำอธิบายแนวคิด

## Subflows ที่ใช้ซ้ำได้ (Capstone)

| Subflow | หน้าที่ |
|---------|---------|
| `SF_InitPaths` | ตั้งค่า path / สร้างโฟลเดอร์ถ้าไม่มี |
| `SF_OpenLabHub` | Launch new Edge/Chrome ไปยัง URL ที่กำหนด |
| `SF_ReadExcelSheet` | Read from Excel worksheet → Data table |
| `SF_WriteExcelSheet` | Write to Excel worksheet |
| `SF_LaunchContoso` | Run application + Focus window Contoso |
| `SF_CreateContosoInvoice` | Populate text field in window / Press button |
| `SF_ScoutCatalog` | Extract data from web page + Next page loop |
| `SF_SendOutlookDraft` | สร้างอีเมล Draft + attach report |
| `SF_LogError` | Get last error → Write text to file |

## Excel

- อ่านด้วย **First line of range contains column names** เมื่อมี header
- ปิดด้วย **Close Excel** ทุกครั้งแม้ error
- แยก sheet: `Input`, `Results`, `Summary` / `Priced`
- อย่าเขียนทับไฟล์ต้นฉบับใน `assets/` — เขียนไปที่ `output/`
- Macro: **Run Excel macro** บนไฟล์ `.xlsm` เท่านั้น

## Outlook

- ใช้ recipient จำลองจาก assets (`recipients.csv`)
- สร้างเป็น **Draft** เป็นค่าเริ่มต้นของ Lab
- ตรวจเนื้อหาและไฟล์แนบก่อนส่งจริง
- ห้ามใส่ข้อมูลส่วนบุคคลจริงใน subject/body ตัวอย่าง

## Debugging (ใน flow designer)

1. Breakpoints / Run next action
2. Inspect Variables pane
3. Errors pane + Get last error
4. เปรียบเทียบผลกับ `assets/expected/` ของ Lab

## Security

- ห้าม commit password / API key จริง
- Lab Hub demo login: `demo` / `demo` (สาธารณะสำหรับฝึก)
- ใช้บัญชีองค์กรตามนโยบายเมื่อเชื่อมต่อบริการจริง
- รัน PAD และแอปเป้าหมายด้วยสิทธิ์ elevation เดียวกัน ([UIPI guidance](https://learn.microsoft.com/troubleshoot/power-platform/power-automate/desktop-flows/ui-automation/uipi-issues))
