# Lab 03 — Static Table (ความรู้)

**หน้าปก:** [README.md](README.md) · **ลงมือทำ:** [LAB.md](LAB.md)

**วัน:** 1 · **Core** · อ่านประมาณ 10–15 นาที

## 1. บทนี้เรียนอะไร

- Extract ตาราง HTML ที่โหลดครบตั้งแต่เปิดหน้า (static)
- ใช้ **Wait for web page content** → **Contain element** ก่อน Extract
- แยกจาก catalog หลายหน้า ([19-catalog](https://pad.ontoiq.tech/pad/19-catalog.html)) ซึ่งมี Prev/Next

## 2. หน้าเป้าหมาย

| | |
|--|--|
| URL | https://pad.ontoiq.tech/pad/03-table.html |
| Selector | `#tbl-employees` (Hints บนหน้า) |
| Pagination | **ไม่มี** |

## 3. แนวคิดหลัก

```text
Launch → Wait Contain element (ตาราง) → Extract → For each แถว → Write CSV → Close
```

อย่าหาปุ่ม Next บนหน้านี้ — ถ้าต้องวนหลายหน้าให้ทำ [Lab 03 Catalog](../catalog/README.md)

## 4. Action หลัก

| Action | ใช้ทำ |
|--------|--------|
| **Launch** Edge/Chrome | เปิด `03-table.html` |
| **Wait for web page content** | Contain element → ตารางพนักงาน |
| **Extract data from web page** | ดึงทั้งตาราง → `StaticTable` |
| **For each** | วน `%StaticTable%` |
| **Write text to file** / CSV | เขียนผล |
| **Close web browser** | ปิดท้าย flow |

## 5. อ้างอิง

- [Web automation](https://learn.microsoft.com/power-automate/desktop-flows/automation-web)
- [UI elements / Edit selector](https://learn.microsoft.com/power-automate/desktop-flows/ui-elements)

**ถัดไป:** [LAB.md](LAB.md)
