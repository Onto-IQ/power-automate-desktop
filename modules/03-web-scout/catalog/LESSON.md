# Lab 03 — Catalog (ความรู้)

**หน้าปก:** [README.md](README.md) · **ลงมือทำ:** [LAB.md](LAB.md)

**Optional (pagination)** · อ่านประมาณ 10–15 นาที

## 1. บทนี้เรียนอะไร

- ตารางที่มี **Prev / Next** — ต้องวนหน้าแล้ว Extract ทีละหน้า
- ต่างจาก [03-table](https://pad.ontoiq.tech/pad/03-table.html) ที่เป็น static หน้าเดียว

## 2. เปรียบเทียบสั้น ๆ

| หน้า | Pagination |
|------|------------|
| 03-table | ไม่มี |
| 09-ajax-table | ไม่มี (แต่ต้อง Wait แถว) |
| **19-catalog** | **มี Next** |

## 3. หน้าเป้าหมาย

| | |
|--|--|
| URL | https://pad.ontoiq.tech/pad/19-catalog.html |
| Table | `#tbl-products` |
| เป้า | รวมประมาณ 24 รายการ (หลายหน้า) |

## 4. แนวคิดหลัก

Lab นี้ใช้ **ลูปซ้อนลูป** เพราะงานมีสองระดับที่ต่างกัน:

| ชั้น | Action | วนอะไร |
|------|--------|--------|
| นอก | **Loop condition** | ทีละ **หน้า** (กด Next จนครบ / disabled) |
| ใน | **For each** | ทีละ **แถว** ของตารางหน้าปัจจุบัน → Insert เข้า `CatalogHits` |

หน้าหนึ่งได้ตารางหนึ่งชุด (`PageTable`) — ต้องวนแถวในหน้านั้นก่อน แล้วค่อยพลิกหน้า วนหน้าถัดไป ไม่ใช่ลูปเดียวที่ทำทั้งสองอย่าง

```text
Launch → เก็บ Btn_NextPage → Loop condition (หน้า · safety MaxPages):
  Wait ตาราง → Extract #tbl-products → PageTable
  For each แถวใน PageTable → Insert เข้า CatalogHits
  Increase variable · Variable name=%PageCount% · Increase by=1
  Get details of element · Btn_NextPage · Attribute=Disabled → AttributeValue
  If AttributeValue = True → Exit loop
  Else → Press button Btn_NextPage
Write CSV → Close
```

ใส่ **MaxPages** เป็น safety เท่านั้น — เงื่อนไขหยุดจริงคือ **Next disabled** (hub มี 3 หน้า; ถ้าไม่ Exit จะอ่านหน้า 3 ซ้ำจนครบ MaxPages)

## 5. อ้างอิง

- [Web automation](https://learn.microsoft.com/power-automate/desktop-flows/automation-web)
- [`shared/SELECTOR-CONVENTIONS.md`](../../../shared/SELECTOR-CONVENTIONS.md)

**ถัดไป:** [LAB.md](LAB.md)
