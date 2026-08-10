# Lab SCB Alt — AJAX FX Rates (Hands-on)

**อ่านก่อน:** [LESSON.md](LESSON.md) · **หน้าปก:** [README.md](README.md) · **โมดูล:** [`../README.md`](../README.md)

**Flow ชื่อ:** `LabSCB_AjaxFxRates` · **ทดแทน Lab 03 AJAX**  
**Catch-up:** [`scripts/ajax-fx-rates.robin`](scripts/ajax-fx-rates.robin) — `partial-ui` + **bundled** UI Elements (`SCB AjaxFx` → `Tbl_ScbFx`)

## Setup

```text
C:\PAD-Labs\output\lab-scb-alt\
```

อ่าน criteria: [`../assets/fx-filter.csv`](../assets/fx-filter.csv) → ค่าเริ่มต้น `CurrencyCode=USD`

เปิดด้วยมือแล้วรอจนเห็นแถวสกุลเงิน (เช่น `USD`) ก่อนออกแบบ Wait:

```text
https://www.scb.co.th/th/personal-banking/foreign-exchange-rates
```

### Input / Output (ตรง catch-up)

| | ค่า |
|---|-----|
| Input | `CurrencyCode` = `USD` |
| UI screen | `SCB AjaxFx` |
| UI element | `Tbl_ScbFx` · CSS `table.table-rate` |
| Extract → | `%ScbFxTable%` (7 คอลัมน์) |
| Filter → | `%Hits%` คอลัมน์ `Currency`, `BankBuys`, `BankSells` |
| Output | `C:\PAD-Labs\output\lab-scb-alt\scb-fx-rates.csv` |

---

## Hands-on

> ทำตามลำดับเดียวกับ catch-up · หรือ paste robin ลง **empty flow** แล้วตรวจ Variables / Replay

### Step 0 — สร้าง flow + criteria + โฟลเดอร์ output

1. **New flow** → ชื่อ:

```text
LabSCB_AjaxFxRates
```

2. **Set variable** · Name `CurrencyCode` ← Value:

```text
USD
```

3. **If folder exists** · Path:

```text
C:\PAD-Labs\output\lab-scb-alt
```

   · โหมด **Does not exist** → ภายใน: **Create folder** · Folder path `C:\PAD-Labs\output` · Folder name `lab-scb-alt`

### Step 1 — Launch Chrome

1. **Launch new Chrome** · Initial URL:

```text
https://www.scb.co.th/th/personal-banking/foreign-exchange-rates
```

2. Wait for page to load timeout / Timeout: `90`
3. Variables produced: `Browser`

### Step 2 — Wait ตาราง (shell) แล้ว Wait ข้อความเรท (AJAX)

ตาราง `table.table-rate` มีใน DOM ตั้งแต่โหลด แต่แถวเรทมาทีหลัง — ต้อง Wait สองชั้นตาม catch-up

1. **Wait for web page content** · `%Browser%` · **Contain element** · UI element:

```text
Tbl_ScbFx
```

   · Screen ใน catch-up: `SCB AjaxFx` · selector: `table.table-rate` · Timeout / FOR: `90`  
   · ถ้าทำมือ: UI Picker ชี้ตารางเรท → Rename เป็น `Tbl_ScbFx` ภายใต้ screen `SCB AjaxFx`  
   · ถ้า paste catch-up: UI Elements มาพร้อม ControlRepository — ไม่ต้อง Capture ใหม่

2. **Wait for web page content** · `%Browser%` · **Contain text** · Text: `%CurrencyCode%` (ตัวแปร `CurrencyCode`) · FOR: `90`

3. **อย่า** ใช้ Wait วินาทีอย่างเดียวเป็นเกณฑ์หลัก

### Step 3 — Extract Entire HTML Table → `%ScbFxTable%`

1. หน้ายังเปิดค้าง และ Step 2 ผ่านแล้ว (เห็นข้อความสกุลเงินบนหน้า)
2. **Extract data from web page** · Browser: `%Browser%` · โหมด **Entire HTML table**
3. ชี้ / ใส่ CSS ของตาราง:

```text
table.table-rate
```

4. ตั้งชื่อคอลัมน์ Extract ให้ตรง catch-up (7 คอลัมน์):

```text
Currency
SellDDTT
SellNotes
BuyTT
BuyExport
BuyTCHQ
BuyNotes
```

5. Variables produced: `ScbFxTable`
6. เปิด `%ScbFxTable%` ใน Variables pane — ต้องมีแถวข้อมูล (ไม่ใช่แค่ header / `{{curCode}}`)

> Catch-up ใช้ `WebAutomation.ExtractData.ExtractHtmlTable` + `Control: table.table-rate` โดยตรง (ไม่ผ่าน appmask ในบรรทัด Extract)

### Step 3b — สร้าง `%Hits%` (3 คอลัมน์ผลกรอง)

ไม่คัดลอกทั้ง 7 คอลัมน์จาก `%ScbFxTable%` — catch-up สร้างตารางผลลัพธ์แคบ:

1. **Create new data table** หลัง Extract
2. คอลัมน์:

```text
Currency
BankBuys
BankSells
```

3. 0 rows ก็ได้ → Variables produced: `Hits`

### Step 4 — กรอง `%CurrencyCode%` แล้ว map คอลัมน์เข้า `%Hits%`

1. **For each** · `%ScbFxTable%` · Store into: `FxRow`
2. ภายในลูป: **If** · `Contains(%FxRow[0]%, %CurrencyCode%)` (คอลัมน์แรก = สกุลเงิน)
3. ถ้าเข้าเงื่อนไข: **Insert row into data table** · Data table: `%Hits%` · ค่า:

| Hits | มาจาก |
|------|--------|
| `Currency` | `%FxRow[0]%` |
| `BankBuys` | `%FxRow[3]%` (= `BuyTT`) |
| `BankSells` | `%FxRow[1]%` (= `SellDDTT`) |

4. หลังลูป: สร้างข้อความ CSV ในตัวแปร `CsvBody`
   - บรรทัดหัว: `Currency,BankBuys,BankSells`
   - วน `%Hits%` ต่อบรรทัด: `%HitRow[0]%,%HitRow[1]%,%HitRow[2]%`

### Step 5 — เขียนไฟล์ + ปิดเบราว์เซอร์

1. **Write text to file** · Text to write: `%CsvBody%`

```text
C:\PAD-Labs\output\lab-scb-alt\scb-fx-rates.csv
```

2. If file exists: **Overwrite** · Encoding: UTF-8
3. **Close web browser** · `%Browser%`
4. Replay 1–2 ครั้ง — เปิด CSV ตรวจว่ามีอย่างน้อย 1 แถว USD

## Acceptance

- [ ] Flow ชื่อ `LabSCB_AjaxFxRates`
- [ ] มีโฟลเดอร์ `C:\PAD-Labs\output\lab-scb-alt\` (สร้างอัตโนมัติถ้ายังไม่มี)
- [ ] **Launch new Chrome** ไปที่ URL `/th/.../foreign-exchange-rates`
- [ ] Wait **Contain element** `Tbl_ScbFx` แล้วตามด้วย Wait **Contain text** `%CurrencyCode%` ก่อน Extract
- [ ] มี Extract Entire HTML Table → `%ScbFxTable%` (ไม่ใช้ stub ตารางว่างแทน Extract)
- [ ] มี `%Hits%` คอลัมน์ `Currency`, `BankBuys`, `BankSells` และกรองด้วย Contains บนคอลัมน์แรก
- [ ] map แถว: `[0]→Currency`, `[3]→BankBuys`, `[1]→BankSells`
- [ ] มี `scb-fx-rates.csv` และมีอย่างน้อย 1 แถวที่เกี่ยวกับ USD (หรือสกุลที่ตั้งไว้)
- [ ] **Close web browser** · ไม่ได้ login / ทำรายการแลกเงิน

## Troubleshooting

| อาการ | แนวทาง |
|-------|--------|
| Wait element ผ่านเร็ว แต่ `%Hits%` = 0 | ขาด Wait **Contain text** — ตาราง shell ว่างก่อน AJAX · ดู Step 2 |
| Wait text timeout | ปิดคุกกี้/popup · เพิ่ม FOR · เปิดหน้าด้วยมือยืนยันว่ามี `USD` · ลอง `CurrencyCode=EUR` |
| Designer: UI element wasn't found | paste catch-up ลง **empty** flow เพื่อให้ ControlRepository เข้า · หรือ Capture `Tbl_ScbFx` เองใต้ `SCB AjaxFx` |
| Extract ได้แค่ placeholder / 0 แถวข้อมูล | Extract ก่อน AJAX เสร็จ — ย้าย Extract ไปหลัง Wait text |
| `%Hits%` ว่างหลังมีแถวใน `%ScbFxTable%` | ตรวจ Contains ที่ `%FxRow[0]%` · เปิด Variables ดูว่าสกุลเงินอยู่คอลัมน์ไหน · ปรับ index map `[0]/[3]/[1]` ถ้า DOM เปลี่ยน |
| CSV คอลัมน์เรทสลับ Buys/Sells | ตาม catch-up: Buys = col3 (`BuyTT`), Sells = col1 (`SellDDTT`) — อย่าสลับ |
| หน้าเป็น English | ใช้ URL `/th/...` ตาม Step 1 |

## Cleanup

ปิดเบราว์เซอร์ค้าง · ลบ CSV ทดสอบถ้าไม่ต้องการเก็บเรท

> **Catch-up:** ตามไม่ทัน → วาง [`scripts/ajax-fx-rates.robin`](scripts/ajax-fx-rates.robin) ใน flow **ว่าง** (partial-ui + bundled `SCB AjaxFx` / `Tbl_ScbFx`)
