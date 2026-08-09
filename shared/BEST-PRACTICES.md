# Best Practices — Power Automate for desktop Labs

เอกสารนี้รวบรวมแนวทางตั้งชื่อตัวแปร โครงสร้าง flow และจุดควรระวังเวลาทำ Lab  
อ้างอิงชื่อ Action ทางการได้จาก [`OFFICIAL-TERMINOLOGY.md`](OFFICIAL-TERMINOLOGY.md) และ [Handle errors](https://learn.microsoft.com/power-automate/desktop-flows/errors)  
แหล่งอ้างอิงช่วงสิงหาคม 2026: [`SOURCES-AUG2026.md`](SOURCES-AUG2026.md) · Coding guidelines: [desktop-flow-coding-guidelines](https://learn.microsoft.com/power-automate/guidance/desktop-flow-coding-guidelines/)

## Aug 2026 notes (ไม่บังคับในเกณฑ์ผ่าน)

- **Wait ที่ถูกต้อง:** ใช้ **Wait for web page content** / **Wait for window content** แทนการพึ่ง **Wait** เป็นวินาทีอย่างเดียว ([optimize flow performance](https://learn.microsoft.com/power-automate/guidance/desktop-flow-coding-guidelines/optimize-flow-performance))
- **Flowchart designer (preview, 2607):** สลับ Sequence ↔ Flowchart ได้ — Lab ยังเขียนตาม Sequence เป็นหลัก
- **AI-assisted UI repair (preview):** ใช้เมื่อ selector หลุดตอน debug — ไม่แทนที่การ capture ด้วย `id` / `data-pad` / AutomationId
- **Default variable values (2606+):** ตั้งค่า fallback ใน Variables pane ได้ถ้า designer รองรับ

## Naming

| ประเภท | Convention | ตัวอย่าง |
|--------|------------|----------|
| Flow | `LabXX_ShortName` | `Lab07_ContosoInvoiceOps` |
| Subflow | `SF_<VerbNoun>` | `SF_WriteExcelReport` |
| UI Element | `Ctrl_<Role>` | `Txt_CustomerName`, `Btn_Submit` |
| Variable (ชื่อตอนสร้าง) | `PascalCase` **ไม่มี `%`** | `InputLeads`, `LastError` |
| Variable (ตอนอ้างอิงในช่องค่า) | `%PascalCase%` | `%InputLeads%`, `%LastError%` |

### กฎ `%` ใน designer (ผู้เรียนทั่วไป)

| ทำอะไร | ใส่ `%` หรือไม่ |
|--------|----------------|
| **Set variable** → ช่อง Name | ไม่ใส่ — พิมพ์ `WorkingRoot` |
| เปลี่ยนชื่อ produced variable / Store into | ไม่ใส่ — พิมพ์ `InboxFiles`, `CurrentFile` |
| พิมพ์ค่าในช่อง Folder / path / text ที่ต้องการดึงตัวแปร | ใส่ — `%WorkingRoot%\inbox` |
| Variables pane แสดงชื่อ | มักเห็นเป็น `%WorkingRoot%` หลังสร้างแล้ว — เป็นเรื่องปกติ |

รายละเอียดการเขียนกฎ `%` ใน Lab: [`PAD-FUNDAMENTALS.md`](PAD-FUNDAMENTALS.md)

## Variable & Data Table Contract

ตารางด้านล่างใช้รูปแบบ `%Name%` เพื่อสื่อว่า **ตอนอ้างอิงในช่องค่า** ต้องมี `%` — ตอนตั้งชื่อใน **Set variable** ใช้คอลัมน์ “ชื่อตอนสร้าง”

| ชื่อตอนสร้าง | ตอนอ้างอิง | ชนิด | ความหมาย |
|--------------|------------|------|----------|
| `WorkingRoot` | `%WorkingRoot%` | Text | โฟลเดอร์ทำงาน เช่น `C:\PAD-Labs\working` |
| `OutputRoot` | `%OutputRoot%` | Text | โฟลเดอร์เก็บผลลัพธ์ |
| `Browser` | `%Browser%` | Browser instance | ได้จาก Launch new Edge/Chrome |
| `Excel` | `%Excel%` | Excel instance | ได้จาก Launch Excel |
| `InputTable` | `%InputTable%` | Data table | ข้อมูลที่อ่านจาก Excel/CSV |
| `ResultTable` | `%ResultTable%` | Data table | ผลที่ดึงจากเว็บหรือประมวลผลแล้ว |
| `RowIndex` | `%RowIndex%` | Numeric | ดัชนีแถวในลูป |
| `LastError` | `%LastError%` | Error (จาก **Get last error**) | อ้างต่อด้วย `%LastError.Message%` / `.Location%` |
| `RetryCount` | `%RetryCount%` | Numeric | นับจำนวนครั้งที่ retry |

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

### รันซ้ำแล้วชื่อไฟล์ซ้ำ (Create / Save as)

**Save Excel** / **Close Excel** โหมด **Save document as** ไม่มีพารามิเตอร์ Overwrite แบบ **Write text to file**  
ถ้า path เป้าหมายมีไฟล์อยู่แล้ว (รอบสองของ Lab) มักล้มด้วย *Failed to save Excel document* / file-related error  
อ้างอิงแนวทางจาก [Close Excel (Kaizen)](https://www.samurai-emblem.com/2023/02/02/power-automate-desktop-action-close-excel/) ที่แนะนำให้เช็กว่าไฟล์มีอยู่ก่อน Save as

เลือกนโยบายหนึ่งให้ชัด:

| นโยบาย | ลำดับ Action | เมื่อไหร่ใช้ |
|--------|--------------|-------------|
| **Overwrite** | **If file exists** → **Delete file** → แล้วค่อย **Save document as** | Lab ที่ต้องการไฟล์ output ชื่อคงที่ |
| **Open existing** | รอบแรก Create+Save as; รอบถัดไป **Launch Excel** → *Open the following document* แล้ว **Save document** | อัปเดต workbook เดิม |
| **Unique name** | ใส่ timestamp ในชื่อ เช่น `report-%CurrentDateTime%.xlsx` | เก็บประวัติทุกรอบ |

อย่าสับสนกับ error อื่นที่เจอบ่อยเมื่อรัน Excel ซ้ำ:

- ไฟล์ถูกล็อกจากรอบก่อน → ตรวจว่า **Close Excel** ครบ และปิดหน้าต่าง Excel ที่เปิดด้วยมือ
- COM / RPC → ลอง Advanced ของ **Launch Excel** → **Nest under a New Excel process** ([Excel troubleshooting](https://learn.microsoft.com/troubleshoot/power-platform/power-automate/desktop-flows/office-automation/excel/troubleshoot-excel-errors))
- ลูปโฟลเดอร์แล้วเจอ `~$...` → ข้าม temp file ของ Excel ที่กำลังเปิด

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
