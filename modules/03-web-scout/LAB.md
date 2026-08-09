# Lab 03 — Web Scout (Hands-on)

**อ่านก่อน:** [LESSON.md](LESSON.md) · **หน้าปกบท:** [README.md](README.md) · **พื้นฐาน:** [`shared/PAD-FUNDAMENTALS.md`](../../shared/PAD-FUNDAMENTALS.md)

**วัน:** 1 · **ระดับ:** Intermediate  
**ทักษะ:** Launch browser, Extract HTML table, Controls, Wait for AJAX, Files download/upload, บันทึกผลลงไฟล์

## อ้างอิง (Aug 2026)

| แหล่ง | URL |
|-------|-----|
| Web automation | [automation-web](https://learn.microsoft.com/power-automate/desktop-flows/automation-web) |
| Web actions | [actions-reference/webautomation](https://learn.microsoft.com/power-automate/desktop-flows/actions-reference/webautomation) |
| Coding guidelines | [desktop-flow-coding-guidelines](https://learn.microsoft.com/power-automate/guidance/desktop-flow-coding-guidelines/) |

## Setup บนเครื่อง (ทำก่อนเปิด designer)

1. สร้างโฟลเดอร์ output และ downloads (คัดลอก path):

```text
C:\PAD-Labs\output\lab03\
```

```text
C:\PAD-Labs\output\lab03\downloads\
```

2. คัดลอก [`assets/upload-sample.txt`](assets/upload-sample.txt) ไปที่ที่เข้าถึงง่าย เช่น:

```text
C:\PAD-Labs\working\lab03\upload-sample.txt
```

3. เปิด scout brief: [`assets/scout-brief.md`](assets/scout-brief.md) อ่านกฎการเล่น
4. เปิด criteria: [`assets/scout-criteria.csv`](assets/scout-criteria.csv) — ค่าหลัก: `MinAmount=10000`, `TargetRegion=BKK`

## Web Targets

### Core missions (ต้องทำ)

| Mission | Phase 1 | URL | เก็บอะไร |
|---------|---------|-----|----------|
| A — Static table | 03 | https://ontoiq.tech/pad/03-table.html | แถวตารางทั้งหมด |
| B — Controls sniff | 02 | https://ontoiq.tech/pad/02-controls.html | ค่า dropdown/checkbox ที่เลือกได้ |
| C — AJAX orders | 09 | https://ontoiq.tech/pad/09-ajax-table.html | แถวที่โหลดหลัง wait |
| D — Files raid | 05 | https://ontoiq.tech/pad/05-files.html | Download อย่างน้อย 1 ไฟล์ และ/หรือ Upload ไฟล์ mock |

### Challenge missions (Phase 1 ที่ยังขาด — เลือกอย่างน้อย 1)

| Mission | Phase 1 | URL | เก็บอะไร |
|---------|---------|-----|----------|
| E — Iframe nest | 08 | https://ontoiq.tech/pad/08-iframe.html | Switch iframe แล้วกรอก/อ่านค่าใน nested form |
| F — API pulse | 12 | https://ontoiq.tech/pad/12-api.html | เรียก health หรือ orders (Web หรือ **Invoke web service**/HTTP) แล้วบันทึก status |

### Mission P — Multi-page catalog (ตรงสไลด์ Web Scraping)

หน้าพร้อมแล้ว: [19 Catalog](https://ontoiq.tech/pad/19-catalog.html)

Selectors คงที่ทุกหน้า (คัดลอกด้านล่างวางในช่องเมื่อ capture / Wait):

```text
#tbl-products
```

```text
#btn-next-page
```

```text
#lbl-page
```

```text
[data-pad="col-product"]
```

```text
[data-pad="col-price"]
```

API คู่กัน: `GET /pad/api/products?page=1&pageSize=8` (challenge)

**Fallback** ถ้า catalog ล่มชั่วคราว: รวม 03-table + 09-ajax ตามเดิม

### Challenge missions (Phase 2 — โบนัส)

| Mission | URL | เก็บอะไร |
|---------|-----|----------|
| G — Hover | https://ontoiq.tech/pad/13-hover.html | tooltip หลัง hover |
| H — Popup | https://ontoiq.tech/pad/18-popup.html | ค่าจาก popup/new tab แล้วกลับแท็บหลัก |

## Input / Output

| | Path |
|--|------|
| Criteria | [`assets/scout-criteria.csv`](assets/scout-criteria.csv) |
| Upload mock (Mission D) | [`assets/upload-sample.txt`](assets/upload-sample.txt) |
| Output template | [`assets/scout-results-template.csv`](assets/scout-results-template.csv) |
| Expected shape | [`assets/expected-scout-results.csv`](assets/expected-scout-results.csv) |
| Your output | ดู code block ใน Step 9 |
| Downloads | ดู code block ใน Setup |

---

## Hands-on ทีละขั้น

### Step 0 — สร้าง flow และโครงผล Scout

1. เปิด Power Automate for desktop → **New flow**
2. ชื่อ flow (คัดลอกได้):

```text
Lab03_WebScout
```

3. กด **Create**

> **กฎตัวแปรใน PAD (อ่านก่อนทำ Step ถัดไป)**  
> - ช่อง **Name** ของ **Set variable**, ส่วน **Variables produced**, และ **Store into** = พิมพ์ชื่ออย่างเดียว **ไม่มี `%`** เช่น `WorkingRoot`  
> - ช่องอื่นที่ต้องดึงค่าตัวแปร (Folder, File path, Text, …) = ใช้ `%WorkingRoot%` (**มี `%` ครบสองด้าน**)  
> - หลังสร้างแล้ว Variables pane อาจแสดงเป็น `%WorkingRoot%` — เป็นเรื่องปกติ

4. ลาก **Set variable**:
   - Name: `MinAmount` ← **ไม่ใส่ `%`**
   - Value: (คัดลอกด้านล่างวางในช่อง Value)

```text
10000
```

5. ลาก **Set variable**:
   - Name: `TargetRegion` ← **ไม่ใส่ `%`**
   - Value: (คัดลอกด้านล่างวางในช่อง Value)

```text
BKK
```

6. ลาก **Create new data table** (หรือเทียบเท่าใน designer)
7. ตั้งคอลัมน์ให้ตรง template: `ScoutId`, `SourcePage`, `Key`, `Value`, `CapturedAt`, `Matched`, `Notes`
8. **Variables produced:** `ScoutResults` ← **ไม่ใส่ `%`**  
   (อ้างอิงด้วย `%ScoutResults%`)

### Step 1 — เปิดเบราว์เซอร์

1. ลาก **Launch new Microsoft Edge** (หรือ **Launch new Chrome**)
2. Initial URL: (คัดลอกด้านล่างวางในช่อง — เริ่ม Mission A)

```text
https://ontoiq.tech/pad/03-table.html
```

3. **Variables produced:** `Browser` ← **ไม่ใส่ `%`**  
   (อ้างอิงด้วย `%Browser%`)
4. กด Save

---

### Mission A — Static table (`03-table`)

### Step A1 — Wait ตาราง

1. ลาก **Wait for web page content**
2. Browser instance: (คัดลอกด้านล่างวางในช่อง)

```text
%Browser%
```

3. รอ element ตารางบนหน้า (เช่น table / `#tbl-...` ตามที่หน้ามี)
4. กด Save

### Step A2 — Extract ตาราง

1. ลาก **Extract data from web page**
2. Browser instance: (คัดลอกด้านล่างวางในช่อง)

```text
%Browser%
```

3. เปิด **live web helper** เลือกตารางทั้งตาราง
4. **Variables produced:** `StaticTable` ← **ไม่ใส่ `%`**  
   (อ้างอิงด้วย `%StaticTable%`)
5. กด Save

### Step A3 — บันทึกลง ScoutResults

1. ลาก **For each** → Value to iterate: (คัดลอกด้านล่างวางในช่อง)

```text
%StaticTable%
```

   Store into: `StaticRow` ← **ไม่ใส่ `%`**
2. **ภายใน For each** ลาก **Insert row into data table** (หรือ Add row) เข้า (คัดลอกด้านล่างวางในช่อง)

```text
%ScoutResults%
```

3. ใส่ค่าอย่างน้อย:
   - SourcePage = (คัดลอกด้านล่างวางในช่อง)

```text
03-table
```

   - Key / Value = จากคอลัมน์ของ `%StaticRow%` (หรือสรุปแถว)
   - CapturedAt = เวลาเครื่อง (ใช้ action วันที่/เวลาที่มีใน designer)
   - Matched / Notes ตามที่เห็นสมควร
4. ปิด **End** ของ For each

> ไม่ต้อง hardcode index แถวแบบเปราะบาง — วนจาก Data table ที่ extract ได้

---

### Mission B — Controls sniff (`02-controls`)

### Step B1 — ไปหน้า Controls

1. ลาก **Go to web page** วางหลัง Mission A
2. Browser instance: (คัดลอกด้านล่างวางในช่อง)

```text
%Browser%
```

3. URL: (คัดลอกด้านล่างวางในช่อง)

```text
https://ontoiq.tech/pad/02-controls.html
```

4. กด Save
5. ลาก **Wait for web page content** รอ control หลักบนหน้า

### Step B2 — เลือก dropdown / checkbox

1. ลาก **Set drop-down list value on web page**
2. Browser instance: (คัดลอกด้านล่างวางในช่อง)

```text
%Browser%
```

3. เลือกตัวเลือกที่หน้าอนุญาต (ตามที่เห็นบน UI)
4. ลาก **Set check box state on web page** (และ/หรือ **Select radio button on web page** ถ้ามี)
5. ตั้งสถานะตามที่ต้องการบันทึกเป็นหลักฐาน

### Step B3 — บันทึก Notes ลง ScoutResults

1. ลาก **Insert row into data table** เข้า (คัดลอกด้านล่างวางในช่อง)

```text
%ScoutResults%
```

2. ค่าตัวอย่าง:
   - SourcePage = (คัดลอกด้านล่างวางในช่อง)

```text
02-controls
```

   - Key = (คัดลอกด้านล่างวางในช่อง — หรือชื่อ control จริง)

```text
dropdown
```

   - Value = ค่าที่เลือกได้
   - Notes = สั้น ๆ ว่าทำอะไรบนหน้า

---

### Mission C — AJAX orders (`09-ajax-table`)

### Step C1 — ไปหน้า AJAX แล้ว Wait จริงจัง

1. ลาก **Go to web page**
2. URL: (คัดลอกด้านล่างวางในช่อง)

```text
https://ontoiq.tech/pad/09-ajax-table.html
```

3. Browser: (คัดลอกด้านล่างวางในช่อง)

```text
%Browser%
```

4. ลาก **Wait for web page content** จนมีแถวข้อมูล (ไม่ใช้ Wait วินาทีอย่างเดียวเป็นเกณฑ์หลัก)
5. กด Save

### Step C2 — Extract ตาราง AJAX

1. ลาก **Extract data from web page** + **live web helper**
2. **Variables produced:** `AjaxTable` ← **ไม่ใส่ `%`**  
   (อ้างอิงด้วย `%AjaxTable%`)
3. Map คอลัมน์ใกล้เคียง: OrderId, Customer, Product, Amount, Region  
   (ชื่อจริงบนหน้าอาจต่าง — map ให้สอดคล้องใน Data table / ตอนอ่านแถว)

### Step C3 — กรองตาม criteria แล้วบันทึก

1. ลาก **For each** → Value to iterate: (คัดลอกด้านล่างวางในช่อง)

```text
%AjaxTable%
```

   Store into: `AjaxRow` ← **ไม่ใส่ `%`**
2. **ภายในลูป** ลาก **If** ตามเกณฑ์จาก `scout-criteria.csv` เช่น:
   - Amount >= (คัดลอกด้านล่างวางในช่องเมื่ออ้างอิงเกณฑ์)

```text
%MinAmount%
```

   **หรือ**
   - Region ตรง (คัดลอกด้านล่างวางในช่อง)

```text
%TargetRegion%
```

   (ถ้ามีคอลัมน์)
3. เมื่อเข้าเงื่อนไข: **Insert row into data table** เข้า (คัดลอกด้านล่างวางในช่อง)

```text
%ScoutResults%
```

   - SourcePage = (คัดลอกด้านล่างวางในช่อง)

```text
09-ajax-table
```

   - Notes = (คัดลอกด้านล่างเมื่อ Amount ≥ MinAmount ตาม scout-brief)

```text
PRIORITY HIT
```

   - Matched = (คัดลอกด้านล่างเมื่อผ่านเงื่อนไข)

```text
Yes
```

4. ปิด End ของ If และ For each

---

### Mission D — Files raid (`05-files`)

### Step D1 — ไปหน้า Files

1. ลาก **Go to web page**
2. URL: (คัดลอกด้านล่างวางในช่อง)

```text
https://ontoiq.tech/pad/05-files.html
```

3. Browser: (คัดลอกด้านล่างวางในช่อง)

```text
%Browser%
```

4. **Wait for web page content** รอ control download/upload

### Step D2 — Download อย่างน้อย 1 ไฟล์

1. ใช้ **Click link on web page** / **Press button on web page** ตาม control ดาวน์โหลดบนหน้า
2. บันทึกไฟล์ใต้โฟลเดอร์นี้ (คัดลอก path):

```text
C:\PAD-Labs\output\lab03\downloads\
```

   (ตั้งค่า download folder ของเบราว์เซอร์/PAD ให้ชี้โฟลเดอร์นี้ หรือย้ายไฟล์หลังดาวน์โหลดด้วย File actions)
3. เก็บ path จริงไว้ในตัวแปร เช่น Name: `DownloadedPath` ← **ไม่ใส่ `%`** (อ้างอิงด้วย `%DownloadedPath%`)

### Step D3 — Upload ไฟล์ mock (ถ้าหน้ามี upload)

1. Capture input file / ปุ่ม upload ด้วย UI picker
2. Upload จาก path นี้ (คัดลอกด้านล่างวางในช่อง — หรือ path ที่คุณคัดลอกไว้):

```text
C:\PAD-Labs\working\lab03\upload-sample.txt
```

3. Wait ผลลัพธ์บนหน้าถ้ามีข้อความยืนยัน

### Step D4 — บันทึก Scout row

1. **Insert row into data table** เข้า (คัดลอกด้านล่างวางในช่อง)

```text
%ScoutResults%
```

2. ค่า:
   - SourcePage = (คัดลอกด้านล่างวางในช่อง)

```text
05-files
```

   - Key = (คัดลอกด้านล่างวางในช่อง)

```text
DownloadOrUpload
```

   - Value / Notes = path หรือผลลัพธ์
   - Matched = (คัดลอกด้านล่างเมื่อทำ download และ/หรือ upload สำเร็จ)

```text
Yes
```

---

### Challenge — Mission E หรือ F (อย่างน้อย 1)

### Step E — Iframe nest (`08-iframe`) — เลือกทำ

1. **Go to web page** → URL: (คัดลอกด้านล่างวางในช่อง)

```text
https://ontoiq.tech/pad/08-iframe.html
```

2. **Wait for web page content**
3. ใช้ action สลับ iframe ในกลุ่ม Web (**Set current iframe** / เทียบเท่าใน designer) เข้า nested form
4. **Populate text field on web page** กรอกค่าในฟอร์มซ้อน
5. อ่านค่า / บันทึกแถว Scout: SourcePage = (คัดลอกด้านล่างวางในช่อง)

```text
08-iframe
```

6. กลับ parent frame ก่อนไปหน้าถัดไป

### Step F — API pulse (`12-api`) — เลือกทำ

1. **Go to web page** → URL: (คัดลอกด้านล่างวางในช่อง)

```text
https://ontoiq.tech/pad/12-api.html
```

   หรือใช้ **Invoke web service** ยิง GET health/orders ตาม URL บนหน้า
2. เก็บ HTTP status + snippet
3. บันทึกแถว Scout:
   - SourcePage = (คัดลอกด้านล่างวางในช่อง)

```text
12-api
```

   - Key = (คัดลอกด้านล่างวางในช่อง — หรือ orders)

```text
health
```

   - Value = status เช่น (คัดลอกด้านล่างวางในช่อง)

```text
200
```

---

### Mission P — Multi-page catalog (`19-catalog`)

### Step P1 — ไป catalog แล้ว Wait ตาราง

1. ลาก **Go to web page**
2. URL: (คัดลอกด้านล่างวางในช่อง)

```text
https://ontoiq.tech/pad/19-catalog.html
```

3. Browser: (คัดลอกด้านล่างวางในช่อง)

```text
%Browser%
```

4. ลาก **Wait for web page content** รอ selector (คัดลอกด้านล่างวางในช่อง):

```text
#tbl-products
```

5. (ถ้ายังไม่มีตัวสะสม) เตรียม Data table — **Variables produced:** `Products` ← **ไม่ใส่ `%`** คอลัมน์ Product + Price (อ้างอิงด้วย `%Products%`)

### Step P2 — Extract หน้าปัจจุบัน

1. ลาก **Extract data from web page** ชี้ตารางสินค้า (Product + Price)
2. Append / รวมแถวเข้า (คัดลอกด้านล่างวางในช่อง)

```text
%Products%
```

   (For each แล้ว Insert row หรือรวมตารางตามที่ designer รองรับ)

### Step P3 — Loop หน้าถัดไปตราบที่ Next ยังใช้ได้

1. ลาก **Loop condition** (หรือ Loop ตามเงื่อนไขที่ designer มี)
2. เงื่อนไขแนวคิด: ปุ่ม Next ยังไม่ disabled — ตรวจจาก UI element (คัดลอกด้านล่างวางในช่องเมื่อ capture):

```text
#btn-next-page
```

   หรือ

```text
[data-pad="page-next"]
```

   หรือข้อความ

```text
#lbl-page
```

3. **ภายในลูป:**
   - **Click link on web page** หรือ **Press button on web page** ที่ `#btn-next-page`
   - **Wait for web page content** รอ `#tbl-products` พร้อมอีกครั้ง
   - **Extract data from web page** แล้ว append เข้า `%Products%`
4. เมื่อ Next **disabled** (หน้า 3/3) → ออกจากลูป

เป้าหมาย: ครบประมาณ **24 รายการ** จาก 3 หน้า

### Step P4 — เขียนผล catalog (และรวม Scout)

1. เขียน `%Products%` เป็นไฟล์ช่วยได้ (เช่น CSV ภายใต้ `output\lab03\`) — ทางเลือก
2. ใส่แถวสรุปลง `%ScoutResults%` ว่า Mission P ดึงครบกี่รายการก็ได้

---

### Step 9 — เขียน scout-results.csv และปิดเบราว์เซอร์

1. **หลัง** Mission A–D (และ Challenge / P ที่ทำ) แปลง `%ScoutResults%` เป็นข้อความ CSV  
   (ใช้ Write CSV / วนแถวสร้างข้อความ — ให้เปิดใน Excel ได้ และแนะนำ UTF-8)
2. ลาก **Write text to file** (หรือ action เขียน CSV ที่มี)
3. ตั้งค่า:
   - File path: (คัดลอกด้านล่างวางในช่อง)

```text
C:\PAD-Labs\output\lab03\scout-results.csv
```

   - If file exists: Overwrite
4. โครงคอลัมน์ให้สอดคล้อง [`assets/scout-results-template.csv`](assets/scout-results-template.csv)
5. ลาก **Close web browser** → Browser instance: (คัดลอกด้านล่างวางในช่อง)

```text
%Browser%
```

### Step 10 — รันและตรวจ

1. กด **Run**
2. เปิด `scout-results.csv` — ต้องมีอย่างน้อย 4 แถวข้อมูล (นอกจาก header) จาก Mission A–D
3. ตรวจว่ามี `SourcePage` สำหรับ `03-table`, `09-ajax-table`, และ `05-files`
4. ตรวจโฟลเดอร์ `downloads\` และ/หรือหลักฐาน upload
5. (เกณฑ์ผ่าน) Mission P: นับรายการจาก catalog ประมาณ 24 รายการจาก 3 หน้า

### Challenge เพิ่ม (Phase 2)

- Mission G — Hover — URL: (คัดลอกได้)

```text
https://ontoiq.tech/pad/13-hover.html
```

  เก็บ tooltip หลัง hover
- Mission H — Popup — URL: (คัดลอกได้)

```text
https://ontoiq.tech/pad/18-popup.html
```

  อ่านค่าจาก popup/new tab แล้วกลับแท็บหลัก

---

## จุดที่มักทำผิด

| ผิด | ถูก |
|-----|-----|
| พิมพ์ `%Name%` ในช่อง Name / Store into / **Variables produced** | ใช้ชื่อเปล่าไม่มี `%` เช่น `ScoutResults`, `StaticRow` |
| Extract หน้า AJAX ทันทีหลัง Go to | มี **Wait for web page content** จนมีแถวก่อน Extract |
| Hardcode แถวที่ 1–2 แบบตายตัว | วนจาก Data table ที่ extract ได้ |
| Mission D ไม่มีหลักฐานไฟล์ | ต้องมีไฟล์ใน `downloads\` และ/หรือ Notes path ใน CSV |
| ลืมปิดเบราว์เซอร์ | ท้าย flow มี **Close web browser** |
| Mission P หยุดที่หน้า 1 | ใช้ Loop + Click Next จน disabled แล้วก็นับรวม ~24 รายการ |
| Iframe กรอกที่ parent | **Set current iframe** ก่อน Populate แล้วกลับ parent |

---

## Variables

| ชื่อตอนสร้าง (ไม่มี `%`) | ตอนอ้างอิง | Type |
|--------------------------|------------|------|
| `Browser` | `%Browser%` | Browser |
| `StaticTable` / `AjaxTable` | `%StaticTable%` / `%AjaxTable%` | Data table |
| `ScoutResults` | `%ScoutResults%` | Data table / list |
| `Products` | `%Products%` | Data table (Mission P) |
| `MinAmount` | `%MinAmount%` | Numeric |
| `TargetRegion` | `%TargetRegion%` | Text |
| `StaticRow` / `AjaxRow` | `%StaticRow%` / `%AjaxRow%` | Data row |

## Expected Result

- มีไฟล์ `scout-results.csv` อย่างน้อย 4 แถวข้อมูล (นอกจาก header) จาก Mission A–D
- มีแถว `SourcePage` สำหรับ `03-table`, `09-ajax-table`, และ `05-files`
- แถวที่ผ่าน criteria ถูก mark ในคอลัมน์ `Notes` หรือ `Matched`
- (Challenge) มีอย่างน้อยหนึ่งใน `08-iframe` หรือ `12-api`
- Mission P: ดึงครบ 3 หน้าจาก catalog (ประมาณ 24 รายการ)

## Acceptance Criteria

- [ ] มี Wait ก่อน extract หน้า AJAX
- [ ] Mission D ทำ download และ/หรือ upload สำเร็จ มีหลักฐานใน output
- [ ] ไม่ hardcode index แถวแบบเปราะบางโดยไม่จำเป็น
- [ ] Output CSV เปิดใน Excel ได้
- [ ] Browser ถูกปิด
- [ ] (Challenge) Mission E หรือ F อย่างน้อย 1 รายการ
- [ ] **Mission P:** ดึงครบ 3 หน้าจาก [19-catalog](https://ontoiq.tech/pad/19-catalog.html) (ประมาณ 24 รายการ) ด้วย Next loop

## Troubleshooting

| อาการ | แก้ |
|-------|-----|
| AJAX ว่าง | เพิ่ม Wait / รอ element แถวแรก |
| Upload ไม่ติด | ตรวจ path ไฟล์ mock และ selector ของ input file |
| Iframe กรอกไม่ได้ | Set current iframe ก่อน Populate; กลับ parent หลังจบ |
| API ไม่ตอบ | ตรวจ URL `/pad/api/...` จากหน้า 12 และ timeout |
| ชื่อคอลัมน์ไม่ตรง | Rename columns ใน Data table หลัง extract |
| CSV ภาษาไทยเพี้ยน | บันทึก UTF-8 |
| Catalog Next ไม่เดิน | ตรวจ `#btn-next-page` / `[data-pad="page-next"]` และ Wait ตารางทุกหน้า |

## Cleanup

- ปิด browser
- เก็บ output ไว้ตรวจกับวิทยากร
