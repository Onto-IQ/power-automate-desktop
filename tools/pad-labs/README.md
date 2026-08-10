# PAD-Labs pack tools

สร้างและติดตั้งโฟลเดอร์ `C:\PAD-Labs` สำหรับทุก Module ของ Lab Kit

| สคริปต์ | หน้าที่ |
|---------|---------|
| [`Build-PAD-LabsZip.ps1`](Build-PAD-LabsZip.ps1) | สร้าง `dist/PAD-Labs.zip` (seed assets ครบ) |
| [`Install-PAD-Labs.ps1`](Install-PAD-Labs.ps1) | ติดตั้งไป `C:\PAD-Labs` จาก repo หรือจากแพ็กเกจ |
| [`New-Lab06SalesReport.ps1`](New-Lab06SalesReport.ps1) | สร้าง `sales-report.xlsm` ด้วย Excel COM |
| [`PAD-Labs-README.txt`](PAD-Labs-README.txt) | คู่มือสั้นใน zip |

## ผู้เรียน (ดาวน์โหลดจาก GitHub)

1. เปิด [Releases](https://github.com/Onto-IQ/power-automate-desktop/releases)
2. ดาวน์โหลด **`PAD-Labs.zip`**
3. แตกไปที่ `C:\` → ได้ `C:\PAD-Labs\`

หรือรันจาก clone:

```powershell
cd <repo>
.\tools\pad-labs\Install-PAD-Labs.ps1 -FromRepo -Force
```

## ผู้ดูแล (build ใหม่)

ต้องมี Excel (สำหรับ Lab 06 `.xlsm`) ครั้งแรก:

```powershell
.\tools\pad-labs\Build-PAD-LabsZip.ps1
# → dist\PAD-Labs.zip
```

อัปโหลดเป็น asset ของ GitHub Release (หรือให้ workflow `pad-labs-zip` ทำให้อัตโนมัติ)
