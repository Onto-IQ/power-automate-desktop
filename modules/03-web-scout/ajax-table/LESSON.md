# Lab 03 — AJAX Table (ความรู้)

**หน้าปก:** [README.md](README.md) · **ลงมือทำ:** [LAB.md](LAB.md)

**วัน:** 1 · **Core** · อ่านประมาณ 10–15 นาที

## 1. บทนี้เรียนอะไร

- ตารางที่แถวโผล่หลังเรียก API (AJAX) — ต้อง **Wait for web page content** จนมีแถวก่อน Extract
- กรองแถวด้วย **If** ตาม criteria
- หน้านี้**ไม่มี** pagination แบบ catalog

## 2. เปรียบเทียบสั้น ๆ

| หน้า | ต่างจาก AJAX อย่างไร |
|------|---------------------|
| [03-table](https://pad.ontoiq.tech/pad/03-table.html) | Static — แถวพร้อมทันที |
| [09-ajax-table](https://pad.ontoiq.tech/pad/09-ajax-table.html) | ต้อง Wait / Refresh จนมีแถว |
| [19-catalog](https://pad.ontoiq.tech/pad/19-catalog.html) | มี Next หลายหน้า — ไม่ใช่ Lab นี้ |

## 3. หน้าเป้าหมาย

| | |
|--|--|
| URL | https://pad.ontoiq.tech/pad/09-ajax-table.html |
| Hints | `#tbl-orders`, `#btn-refresh-orders`, `#lbl-loading` |
| Criteria | `MinAmount=10000`, `TargetRegion=BKK` |

## 4. แนวคิดหลัก

```text
Launch 09-ajax → (Refresh ถ้าต้อง) → Wait แถว/ตาราง → Extract AjaxTable
For each → If ผ่าน criteria → เก็บแถว → Write CSV → Close
```

## 5. อ้างอิง

- [Web automation](https://learn.microsoft.com/power-automate/desktop-flows/automation-web)

**ถัดไป:** [LAB.md](LAB.md)
