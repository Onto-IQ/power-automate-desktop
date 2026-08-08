# Lab 03 — Web Scout

**วัน:** 1 · **ระดับ:** Intermediate  
**ทักษะ:** Launch browser, Extract HTML table, Controls, Wait for AJAX, Files download/upload, บันทึกผลลงไฟล์

## วัตถุประสงค์

- ทำ **Web Scout** แบบสนุก: เก็บข้อมูลจากหลายหน้าบน PAD Lab Hub
- Extract ตาราง static และรอตาราง dynamic (AJAX)
- ส่งออกผลเป็น CSV

## Prerequisites

- PAD + browser extension
- อ่าน [`shared/SELECTOR-CONVENTIONS.md`](../../shared/SELECTOR-CONVENTIONS.md)

## Setup

1. Flow ชื่อ `Lab03_WebScout`
2. สร้าง `C:\PAD-Labs\output\lab03\`
3. เปิด scout brief: [`assets/scout-brief.md`](assets/scout-brief.md)

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

| ขั้น | Action |
|------|--------|
| P1 | ไปที่ catalog → Wait `#tbl-products` |
| P2 | Extract ตาราง Product + Price → append เข้า `%Products%` |
| P3 | **Loop Condition** ตราบที่ Next ยังใช้ได้: Click `#btn-next-page` / `[data-pad="page-next"]` → Wait ตาราง → Extract ต่อ |
| P4 | เมื่อ Next **disabled** (หน้า 3/3) → ออกจากลูป แล้วเขียน CSV |

Selectors คงที่ทุกหน้า: `#tbl-products`, `#btn-next-page`, `#lbl-page`, `[data-pad="col-product"]`, `[data-pad="col-price"]`  
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
| Your output | `C:\PAD-Labs\output\lab03\scout-results.csv` |
| Downloads | `C:\PAD-Labs\output\lab03\downloads\` |

## PAD Action Sequence (แนะนำ)

### Mission A
1. Launch browser → Table page
2. Wait for table element
3. **Extract data from web page** (ใช้ **live web helper** เลือกตาราง) → `%StaticTable%`
4. วนแถว เขียนลงรายการผล Scout (`SourcePage=03-table`)

### Mission B
1. Go to Controls page (หรือ Launch ใหม่)
2. Select dropdown / set checkbox ตาม criteria ใน CSV
3. Extract ค่าที่เห็นบนหน้า หรือบันทึก action ที่ทำเป็น Notes

### Mission C
1. Go to AJAX Table page
2. **Wait for web page content** จนมีแถวข้อมูล
3. Extract table → `%AjaxTable%`
4. Map คอลัมน์ใกล้เคียง: OrderId, Customer, Product, Amount, Region (ชื่อจริงบนหน้าอาจต่าง — map ให้สอดคล้อง)
5. กรองตาม `scout-criteria.csv` (เช่น Amount >= MinAmount หรือ Region ตรงค่า)

### Mission D — Files (Phase 1 / 05)
1. Go to Files page
2. Download ไฟล์ตัวอย่างจากหน้า → บันทึกใต้ `output\lab03\downloads\`
3. Upload `upload-sample.txt` (ถ้าหน้ามี upload control)
4. บันทึก Scout row: `SourcePage=05-files`, `Key=DownloadOrUpload`, `Notes=path หรือผลลัพธ์`

### Mission E / F (Challenge)
- **E:** เข้า iframe page → **Set current iframe** / focus frame → กรอกฟอร์มซ้อน → กลับ parent
- **F:** จาก API playground ยิง GET health/orders แล้วเก็บ HTTP status + snippet ลง Scout

สุดท้าย: **Write text to file** / เขียน CSV รวมผลทุก Mission ที่ทำ → **Close web browser**

## Variables

| Variable | Type |
|----------|------|
| `%Browser%` | Browser |
| `%StaticTable%` / `%AjaxTable%` | Data table |
| `%ScoutResults%` | Data table / list |
| `%MinAmount%` | Numeric |
| `%TargetRegion%` | Text |

## Expected Result

- มีไฟล์ `scout-results.csv` อย่างน้อย 4 แถวข้อมูล (นอกจาก header) จาก Mission A–D
- มีแถว `SourcePage` สำหรับ `03-table`, `09-ajax-table`, และ `05-files`
- แถวที่ผ่าน criteria ถูก mark ในคอลัมน์ `Notes` หรือ `Matched`
- (Challenge) มีอย่างน้อยหนึ่งใน `08-iframe` หรือ `12-api`

## Acceptance Criteria

- [ ] มี Wait ก่อน extract หน้า AJAX
- [ ] Mission D ทำ download และ/หรือ upload สำเร็จ มีหลักฐานใน output
- [ ] ไม่ hardcode index แถวแบบเปราะบางโดยไม่จำเป็น
- [ ] Output CSV เปิดใน Excel ได้
- [ ] Browser ถูกปิด
- [ ] (Challenge) Mission E หรือ F อย่างน้อย 1 รายการ
- [ ] **Mission P:** ดึงครบ 3 หน้าจาก [19-catalog](https://ontoiq.tech/pad/19-catalog.html) (ประมาณ 24 รายการ) ด้วย Next loop

## Challenge เพิ่ม (Phase 2)

- Mission G/H ตามตารางด้านบน: Hover / Popup

## Troubleshooting

| อาการ | แก้ |
|-------|-----|
| AJAX ว่าง | เพิ่ม Wait / รอ element แถวแรก |
| Upload ไม่ติด | ตรวจ path ไฟล์ mock และ selector ของ input file |
| Iframe กรอกไม่ได้ | Set current iframe ก่อน Populate; กลับ parent หลังจบ |
| API ไม่ตอบ | ตรวจ URL `/pad/api/...` จากหน้า 12 และ timeout |
| ชื่อคอลัมน์ไม่ตรง | Rename columns ใน Data table หลัง extract |
| CSV ภาษาไทยเพี้ยน | บันทึก UTF-8 |

## Cleanup

- ปิด browser
- เก็บ output ไว้ตรวจกับวิทยากร
