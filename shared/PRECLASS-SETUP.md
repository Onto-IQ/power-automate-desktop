# Pre-class Setup — ทำก่อนวันเรียน (ผู้เรียน)

ทำ checklist นี้ **ก่อนเข้าห้อง** จะลดเวลติดตั้งเช้าวันแรกได้มาก  
คอร์ส: Power Automate for desktop · ประมาณ 2 วัน  
เอกสารพื้นฐาน: [`PAD-FUNDAMENTALS.md`](PAD-FUNDAMENTALS.md)

> ถ้าข้อใดทำไม่ได้ ให้จดไว้แล้วยกมือหา TA เช้าวัน 1 ทันที — อย่ารอจนเริ่ม Lab

---

## 1) เครื่องและบัญชี

- [ ] Windows 10 หรือ 11 (เครื่องที่ใช้เรียนจริง)
- [ ] มีสิทธิ์ติดตั้งโปรแกรม (หรือ IT ติดตั้งให้แล้ว)
- [ ] เข้าอินเทอร์เน็ตได้ และเปิด [https://ontoiq.tech/pad/](https://ontoiq.tech/pad/) ได้
- [ ] *(SCB / Secure Isolation)* ถ้า Lab Hub เปิดไม่ได้ — ทดสอบแทน: [ค้นหา ธปท.](https://www.bot.or.th/th/search.html) · [FX ธปท.](https://app.bot.or.th/BTWS_STAT/statistics/ReportPage.aspx?language=TH&reportID=123) · [FX SCB](https://www.scb.co.th/th/personal-banking/foreign-exchange-rates) แล้วใช้ [`modules/scb-secure-isolation-alt/`](../modules/scb-secure-isolation-alt/)
- [ ] มีบัญชีที่ใช้กับ Power Automate for desktop ตามที่องค์กร/คอร์สกำหนด

## 2) ติดตั้ง Power Automate for desktop

- [ ] ติดตั้งจาก [Install Power Automate for desktop](https://learn.microsoft.com/power-automate/desktop-flows/install) (MSI หรือ Microsoft Store)
- [ ] แนะนำเวอร์ชัน **2607+** สำหรับคอร์สรอบ Aug 2026 — ดู [PAD version matrix](https://learn.microsoft.com/power-platform/released-versions/power-automate-desktop)
- [ ] เปิด PAD ได้ถึงหน้า **Console** (มีปุ่ม New flow)

## 3) Browser + Extension

- [ ] ติดตั้ง **Microsoft Edge** หรือ **Google Chrome**
- [ ] ติดตั้ง **Power Automate** browser extension ตามที่ตัวติดตั้ง PAD แนะนำ
- [ ] ทดสอบ: เปิด [01 Forms](https://ontoiq.tech/pad/01-forms.html) แล้วโหลดหน้าได้
- [ ] **ปิด Browser Autofill ในโปรไฟล์ที่ใช้กับ PAD** (สำคัญต่อ Lab 01 Record & Replay):
  - ปิดหรือปิดใช้ชั่วคราว extension **Microsoft Autofill** ถ้ามี — community ยืนยันว่าทับปุ่ม/ช่อง login แล้ว automation ไปต่อไม่ได้ ([thread](https://community.powerplatform.com/forums/thread/details/?threadid=5b9067f5-2fec-4e44-b05e-9549f05ea7bd))
  - Edge/Chrome → Settings → Autofill และ Passwords → ปิด **Save passwords** และ **Autofill forms / addresses** ขณะเรียน Lab เว็บ
  - หลังจบคอร์สเปิดกลับได้

## 4) โปรแกรมเสริมตาม Lab

| โปรแกรม | ใช้เมื่อ | ทำก่อนเรียน |
|----------|----------|-------------|
| **Microsoft Excel** | Lab 06, 07, 08, 10 | บังคับถ้าเรียนวัน 2 |
| **Contoso Invoicing** | Lab 07 (ถ้าคอร์สเลือกเส้น Contoso) | ติดตั้งเมื่อวิทยากรแจ้งเส้น A |
| **Microsoft Outlook (Desktop)** | Lab 10 Capstone | มีโปรไฟล์เปิดได้ — จะสร้าง **Draft** ไม่ส่งจริง |

ติดตั้ง Contoso (เมื่อได้รับแจ้ง):

1. ดาวน์โหลด [ContosoInvoicingSetup.zip](https://github.com/MicrosoftDocs/mslearn-developer-tools-power-platform/raw/master/power-automate-desktop/contoso-invoice-app/ContosoInvoicingSetup.zip)
2. Extract → รัน installer
3. เปิดจาก Start menu ค้นหา `Contoso Invoicing` ให้ขึ้นหน้าต่างหลักได้

## 5) สร้างโฟลเดอร์ทำงาน (บังคับ)

สร้างโครงสร้างนี้บนเครื่อง (ไดรฟ์ `C:` แนะนำ — ถ้าใช้ `D:` ต้องใช้ path นั้นให้สม่ำเสมอทั้งคอร์ส):

```text
C:\PAD-Labs\
  ├── working\
  ├── output\
  └── logs\
```

### วิธีเร็ว (PowerShell)

เปิด **PowerShell** แล้ววางทั้งก้อนนี้:

```powershell
$root = 'C:\PAD-Labs'
@(
  "$root\working",
  "$root\output",
  "$root\logs"
) | ForEach-Object {
  New-Item -ItemType Directory -Force -Path $_ | Out-Null
}
Get-ChildItem $root
```

ผลที่ควรเห็น: มีโฟลเดอร์ `working`, `output`, `logs`

## 6) เตรียมไฟล์ Lab (แนะนำทำก่อนวัน 1)

คัดลอกจาก repo ของคอร์ส (หรือ USB/zip ที่วิทยากรแจก) **อย่าแก้ไฟล์ใน `assets/` ต้นฉบับ**

| Lab | คัดลอกไปที่ |
|-----|-------------|
| 01 | `C:\PAD-Labs\working\lab01\` ← จาก `modules/01-record-replay/assets/` |
| 02 | `C:\PAD-Labs\working\lab02\inbox\` ← จาก `modules/02-file-management/assets/inbox/` |
| 03 | สร้าง `C:\PAD-Labs\output\lab03\` · (Files optional) คัดลอก `modules/03-web-scout/files/assets/upload-sample.txt` → `C:\PAD-Labs\working\lab03\` · criteria AJAX อยู่ที่ `modules/03-web-scout/ajax-table/assets/` |
| 04+ | ตาม `LAB.md` ของแต่ละบทในวันที่ 2 |

สร้างโฟลเดอร์ lab ย่อยเพิ่มได้ด้วย:

```powershell
1..10 | ForEach-Object {
  $n = '{0:D2}' -f $_
  New-Item -ItemType Directory -Force -Path "C:\PAD-Labs\working\lab$n" | Out-Null
  New-Item -ItemType Directory -Force -Path "C:\PAD-Labs\output\lab$n" | Out-Null
}
New-Item -ItemType Directory -Force -Path 'C:\PAD-Labs\working\lab01b' | Out-Null
New-Item -ItemType Directory -Force -Path 'C:\PAD-Labs\output\lab01b' | Out-Null
New-Item -ItemType Directory -Force -Path 'C:\PAD-Labs\working\lab09b','C:\PAD-Labs\output\lab09b' | Out-Null
New-Item -ItemType Directory -Force -Path 'C:\PAD-Labs\logs\lab07','C:\PAD-Labs\logs\lab09','C:\PAD-Labs\logs\lab09b','C:\PAD-Labs\logs\lab10' | Out-Null
```

## 7) ทดสอบสั้น ๆ ว่าพร้อม

- [ ] PAD → **New flow** → ตั้งชื่อทดสอบ → เปิด designer ได้
- [ ] ใน Actions Pane ค้นหาคำว่า `Set variable` แล้วเจอ
- [ ] เปิด [https://ontoiq.tech/pad/](https://ontoiq.tech/pad/) ได้
- [ ] Excel เปิดไฟล์ `.xlsx` ได้ (ถ้าเรียนวัน 2)

## 8) สิ่งที่ยังไม่ต้องทำก่อนเรียน

- ไม่ต้องสร้าง flow ของ Lab ทั้ง 10 บทล่วงหน้า  
- ไม่ต้องส่งอีเมลจริง  
- ไม่ต้องท่อง Action ทั้งชุด — อ่าน [`PAD-FUNDAMENTALS.md`](PAD-FUNDAMENTALS.md) บท “กฎ `%`” ก็พอ

## ส่งหลักฐานพรีคลาส (ถ้าวิทยากรขอ)

ถ่ายหน้าจอหรือจดสั้น ๆ:

1. เวอร์ชัน PAD (About / Settings)  
2. ผล `Get-ChildItem C:\PAD-Labs`  
3. หน้า Lab Hub โหลดได้  

---

**เช้าวันเรียน:** ถ้าข้อใดยังไม่ผ่าน → ยกมือหา **TA ประจำโซน** ทันทีตาม [`CLASSROOM-SCHEDULE-12H.md`](CLASSROOM-SCHEDULE-12H.md)
