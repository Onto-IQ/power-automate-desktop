# Shared resources

เอกสารกลางที่ใช้ร่วมหลาย Lab

| ไฟล์ | คำอธิบาย |
|------|----------|
| [OFFICIAL-TERMINOLOGY.md](OFFICIAL-TERMINOLOGY.md) | ชื่อ Action / ศัพท์ตาม Microsoft Learn ล่าสุด |
| [SELECTOR-CONVENTIONS.md](SELECTOR-CONVENTIONS.md) | CSS / data-pad / wait strategy สำหรับ PAD Lab Hub |
| [BEST-PRACTICES.md](BEST-PRACTICES.md) | Naming, variables, subflows, Outlook/Excel safety |
| [DATA-SCHEMAS.md](DATA-SCHEMAS.md) | Schema ของ mock leads / orders / scout / recipients |
| [WEB-HUB-REQUESTS.md](WEB-HUB-REQUESTS.md) | สถานะหน้า Lab Hub (รวม 19 Catalog) |
| [generate_mock_xlsx.py](generate_mock_xlsx.py) | สร้างไฟล์ `.xlsx` จาก CSV ใน Labs 06, 07, 08, 10 |

## Regenerating Excel mocks

จากราก repo:

```powershell
python shared\generate_mock_xlsx.py
```
