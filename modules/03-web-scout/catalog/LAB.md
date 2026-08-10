# Lab 03 — Catalog (Hands-on)

**อ่านก่อน:** [LESSON.md](LESSON.md) · **หน้าปก:** [README.md](README.md)

**Flow ชื่อ:** `Lab03_Catalog` · **Optional**

## Setup

```text
C:\PAD-Labs\output\lab03\
```

## Hands-on

### Step 0 — สร้าง flow + ตัวแปรช่วย

1. **New flow** → ชื่อ:

```text
Lab03_Catalog
```

2. **Create new data table** → `CatalogHits` · คอลัมน์: SKU, Product, Price, Category
3. **Set variable** `MaxPages` ← `10` (safety)
4. **Set variable** `PageCount` ← `0`

### Step 1 — Launch

1. **Launch** Edge/Chrome · Initial URL:

```text
https://pad.ontoiq.tech/pad/19-catalog.html
```

2. Variables produced: `Browser`

### Step 1b — เก็บ UI element ปุ่ม Next (ทำก่อนลูป)

1. เปิดแผง **UI Elements** → **Add UI element** (หรือ Add element) ด้วย UI Picker
2. ชี้ปุ่ม **Next** บนหน้า (`#btn-next-page`)
3. **Save** แล้ว Rename เป็น:

```text
Btn_NextPage
```

4. (ทางเลือก) เก็บตาราง `#tbl-products` แล้ว Rename เป็น `Tbl_Products` — ใช้กับ Wait ในลูปได้

อย่าข้ามขั้นนี้ — ในลูปต้องอ้าง `Btn_NextPage` ไม่ใช่ไปหาปุ่มใหม่ทุกครั้ง

### Step 2 — Loop หน้า + Extract

> **Tip:** มีลูปซ้อนกัน — **Loop condition** = วน **หน้า** · **For each** (ข้างใน) = วน **แถว** ของหน้าปัจจุบัน อย่าสลับบทบาท

1. **Loop condition** (First operand / Operator / Second operand — เช่น `%PageCount%` · **Less than (<)** · `%MaxPages%`)
2. ในลูป: **Wait for web page content** · Contain element · ตาราง `#tbl-products` / `Tbl_Products`
3. ให้หน้ายังอยู่ที่ [19-catalog](https://pad.ontoiq.tech/pad/19-catalog.html) (หลังกด Next แล้วยังต้องเป็นหน้านี้)
4. **Extract data from web page** · Browser: `%Browser%`
5. PAD จะเปิด **live web helper** บนหน้านั้น
6. ชี้ `#tbl-products`
7. **คลิกขวา** บนตาราง/เซลล์ในตาราง
8. เลือก **Extract Entire HTML Table** · Variables produced: `PageTable`
9. รอบแรกตั้งค่า helper · รอบถัดไปใช้ extract เดิมบนตารางหน้าปัจจุบัน
10. ลาก **For each** · Value to iterate: (คัดลอก)

```text
%PageTable%
```

11. Store into: `ProductRow` ← **ไม่ใส่ `%`**
12. **ภายใน For each** ลาก **Insert row into data table**
13. ตั้งค่า 3 ช่องให้ตรงนี้เท่านั้น:

| ช่องใน UI | ใส่ค่า |
|-----------|--------|
| **Data table** | `%CatalogHits%` (กด `{x}` เลือก `CatalogHits`) |
| **Into location** | **End of data table** |
| **New value(s)** | `%ProductRow%` (กด `{x}` เลือก `ProductRow`) ถ้าคอลัมน์ตรงกัน |

คัดลอกวาง Data table:

```text
%CatalogHits%
```

คัดลอกวาง New value(s):

```text
%ProductRow%
```

หรือใส่เป็น list (**ห้ามซ้อน `%` ข้างใน**) — คัดลอก:

```text
%[ProductRow['SKU'], ProductRow['Product'], ProductRow['Price'], ProductRow['Category']]%
```
14. **End** For each
15. **Increase variable** — **Variable name:** `%PageCount%` · **Increase by:** `1`
   (ตาม [Variables actions](https://learn.microsoft.com/power-automate/desktop-flows/actions-reference/variables#increase-variable))
16. **สำคัญ:** หลังหน้า 3 ปุ่ม Next จะ **disabled** — ถ้าไม่ตรวจแล้ว **Exit loop** ลูปจะ Extract **หน้า 3 ซ้ำ** จนครบ `MaxPages` (รอบ 4–10)  
   `MaxPages` เป็น safety เท่านั้น · hub มีจริง **3 หน้า** (~24 แถว)
17. **Get details of element on web page**
    - Web browser instance: `%Browser%`
    - UI element: `Btn_NextPage`
    - Attribute name: **Disabled** (เลือกจากรายการ หรือพิมพ์ `Disabled`)
    - Variables produced: `AttributeValue` (หรือ Rename เป็น `NextDisabled`)
18. ลาก **If**
    - First operand: `%AttributeValue%` (หรือ `%NextDisabled%`)
    - Operator: **Equal to (=)**
    - Second operand: `True` (ถ้าไม่เข้า ให้ลอง `true`)
19. **ภายใน If (disabled = True):** ลาก **Exit loop** → แล้ว **End** If
20. **หลัง End If** (แปลว่า Next ยังกดได้): **Press button on web page** (หรือ **Click link on web page**) · UI element: `Btn_NextPage` · Browser: `%Browser%`
21. **End** loop

โครงท้ายลูปที่ถูกต้อง:

```text
End For each
Increase PageCount
Get details … Attribute=Disabled → AttributeValue
If AttributeValue = True
  Exit loop
End
Press button Btn_NextPage
End  (Loop condition)
```

เป้าหมาย: รวมแถวประมาณ **24** รายการ (3 หน้า × ~8) — **ไม่ใช่** วน 10 รอบ

### Step 3 — เขียน CSV + ปิด

ทำ**หลัง** End ของ Loop condition ใน Step 2

เป้าหมาย: เขียนหัวตารางก่อนหนึ่งครั้ง แล้ว**วนแถว** `%CatalogHits%` เพื่อ Append ลงไฟล์ทีละบรรทัด  
(อย่าต่อข้อความด้วยการขึ้นบรรทัดใหม่ใน Set variable — ใน PAD มักเกิด Syntax error)

กำหนด path ไว้ใช้ซ้ำ (คัดลอก):

```text
C:\PAD-Labs\output\lab03\catalog-products.csv
```

#### 3.1 เขียนหัวตาราง (สร้าง/ทับไฟล์ใหม่)

1. ลาก **Write text to file** (ค้นคำว่า `Write text to file`)
2. **File path:** วาง path ด้านบน
3. **Text to write:**

```text
SKU,Product,Price,Category
```

4. **If file exists:** **Overwrite**
5. Encoding: แนะนำ **UTF-8** (ถ้ามี)
6. กด **Save**

#### 3.2 วน `%CatalogHits%` แล้ว Append ทีละแถว

ใช้**ลำดับคอลัมน์ (index)** จะชัวร์กว่าชื่อ

1. ลาก **For each**
2. Value to iterate: (คัดลอก)

```text
%CatalogHits%
```

3. Store into: `CatalogRow` ← **ไม่ใส่ `%`**
4. **ภายใน For each** ลาก **Set variable** · Name: `CsvLine` ← Value: (คัดลอก)

```text
%CatalogRow[0]%
```

5. ลาก **Set variable** · Name: `CsvLine` · Value: (คัดลอก)

```text
%CsvLine + ',' + CatalogRow[1]%
```

6. ลาก **Set variable** · Name: `CsvLine` · Value: (คัดลอก)

```text
%CsvLine + ',' + CatalogRow[2]%
```

7. ลาก **Set variable** · Name: `CsvLine` · Value: (คัดลอก)

```text
%CsvLine + ',' + CatalogRow[3]%
```

ความหมาย: SKU→`[0]`, Product→`[1]`, Price→`[2]`, Category→`[3]`

8. **ภายใน For each เดิม** ลาก **Write text to file** เพิ่มอีกหนึ่ง action
9. **File path:** path เดิม (`...\catalog-products.csv`)
10. **Text to write:** (คัดลอก)

```text
%CsvLine%
```

11. หลังวาง `%CsvLine%` ในช่อง Text ให้กด Enter หนึ่งครั้งท้ายข้อความ (หรือใช้ **Append line to text file** ถ้ามีใน Actions Pane)
12. **If file exists:** **Append** ← ต้องเป็น Append ไม่ใช่ Overwrite
13. Encoding: UTF-8 (ให้ตรงกับข้อ 3.1)
14. กด **Save**
15. **End** For each

หลังรัน เปิดไฟล์ตรวจ: บรรทัดแรกเป็นหัวตาราง · ถัดไปประมาณ **24** แถวข้อมูล (ไม่ใช่แถวหน้า 3 ซ้ำยาว)

#### 3.3 ปิดเบราว์เซอร์

1. ลาก **Close web browser** · Web browser instance: (คัดลอก)

```text
%Browser%
```

### Step 4 — Replay

รัน 2 ครั้ง · ตรวจจำนวนแถวใน CSV (~24 + หัวตาราง)

## Acceptance

- [ ] Flow ชื่อ `Lab03_Catalog`
- [ ] มี UI element `Btn_NextPage` (เก็บก่อนเข้าลูป)
- [ ] มีการกด Next อย่างน้อยหนึ่งครั้ง (ถ้ามีหลายหน้า)
- [ ] CSV มีแถวรวมหลายหน้า (~24)
- [ ] มี MaxPages เป็น safety **และ** Exit เมื่อ Next Disabled = True
- [ ] ไม่ Extract หน้าสุดท้ายซ้ำ (CSV ~24 ไม่ใช่แถวซ้ำยาว)
- [ ] ปิดเบราว์เซอร์ท้าย flow

## Troubleshooting

| อาการ | แก้ |
|-------|-----|
| กด Next ไม่ได้ / หาปุ่มไม่เจอ | ทำ Step 1b ก่อน — Add UI element แล้ว Rename `Btn_NextPage` |
| ได้แค่หน้าแรก | ตรวจว่ามี Press/Click `Btn_NextPage` + Wait หลังเปลี่ยนหน้า |
| หน้า 3 ซ้ำในรอบ 4–10 / CSV แถวซ้ำเกิน ~24 | ขาด **Exit loop** เมื่อ Next disabled — ใช้ Get details · Attribute **Disabled** แล้ว If = True → Exit (อย่าพึ่งแค่ MaxPages) |
| วนไม่จบ | ใช้ MaxPages เป็น safety + Exit เมื่อ Disabled = True |
| If Disabled ไม่เข้า | ลองเทียบ `True` / `true` · ตรวจว่า Attribute name เป็น **Disabled** |
| หาคอลัมน์ Product ในรายการตัวแปรไม่เจอ | พิมพ์/วาง `%ProductRow['Product']%` เอง |
| หา Write CSV / เขียนไฟล์ไม่เจอ | ค้น **Write text to file** · หัวตารางใช้ Overwrite · แถวในลูปใช้ **Append** |
| CSV มีแค่แถวสุดท้าย | ในลูปต้องเลือก **Append** ไม่ใช่ Overwrite |
| Syntax error ตอนสร้าง CsvLine | ใช้ index `%CatalogRow[0]%` … `%CatalogRow[3]%` ตาม Step 3.2 · อย่าต่อ 4 คอลัมน์ในสูตรเดียว |
| สับสนกับ 03-table | 03-table ไม่มี Next — Lab นี้อยู่บน 19-catalog |

## Cleanup

ปิดเบราว์เซอร์ค้าง

> **Catch-up:** ตามไม่ทัน → วาง [`scripts/03-catalog.robin`](scripts/03-catalog.robin) ใน flow **ว่าง** (partial-ui + bundled `Lab03 Catalog`)
