PAD-Labs — โฟลเดอร์ทำงานสำหรับทุก Module (Onto-IQ PAD Lab Kit)
================================================================

ติดตั้งเร็ว (แนะนำ)
------------------
1. แตก zip นี้ไปที่ไดรฟ์ C:\
   ผลลัพธ์ที่ถูกต้อง: C:\PAD-Labs\working\ ... C:\PAD-Labs\output\ ...

2. หรือเปิด PowerShell แล้วรัน:
   Set-Location <โฟลเดอร์ที่แตก zip>
   .\Install-PAD-Labs.ps1
   (ค่าเริ่มต้นติดตั้งไปที่ C:\PAD-Labs)

โครงสร้าง
---------
C:\PAD-Labs\
  working\lab01 … lab10, lab01b, lab09b, lab-scb-alt   ← ไฟล์ input ที่ seed แล้ว
  output\labXX\                                          ← ผลลัพธ์จาก flow
  logs\lab07, lab09, lab09b, lab10                       ← log / screenshot
  downloads\                                             ← Lab 03 Files

หมายเหตุ Lab 06
---------------
working\lab06\sales-report.xlsm พร้อม macro FormatSummary แล้ว
ถ้าองค์กรบล็อก macro — ดู modules/06-data-table-excel/assets/vba/README.md

รีเซ็ต inbox / batch ก่อนสาธิตซ้ำ
---------------------------------
Lab 04 / 05 ย้ายไฟล์ตอนรัน — แตก zip ทับ หรือรัน Install อีกครั้งจากแพ็กเกจ/repo

เอกสารคอร์ส
-----------
https://github.com/Onto-IQ/power-automate-desktop
Pre-class: shared/PRECLASS-SETUP.md
Releases:  https://github.com/Onto-IQ/power-automate-desktop/releases
