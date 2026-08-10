# Lab SCB Alt — Static FX Table (Hands-on)

**อ่านก่อน:** [LESSON.md](LESSON.md) · **หน้าปก:** [README.md](README.md) · **โมดูล:** [`../README.md`](../README.md)

**Flow ชื่อ:** `LabSCB_StaticFxTable` · **ทดแทน Lab 03 Static**  
**Catch-up:** [`scripts/static-fx-table.robin`](scripts/static-fx-table.robin) — `partial-ui` + **bundled** UI Elements (`SCB StaticFx` → `Tbl_BotFx`)

## Setup

```text
C:\PAD-Labs\output\lab-scb-alt\
```

เปิดด้วยมือเพื่อยืนยันว่าตารางโหลด (มีแถว เช่น อัตราอ้างอิง USD):

```text
https://app.bot.or.th/BTWS_STAT/statistics/ReportPage.aspx?language=TH&reportID=123
```

### Input / Output (ตรง catch-up)

| | ค่า |
|---|-----|
| UI screen | `SCB StaticFx` |
| UI element | `Tbl_BotFx` · CSS `table#dgExcel` |
| Extract → | `%BotFxTable%` (8 คอลัมน์: `Seq`, `Item`, `D1`…`D6`) |
| CSV | เขียนแค่ 3 คอลัมน์แรก สูงสุด 20 แถว |
| Output | `C:\PAD-Labs\output\lab-scb-alt\bot-fx-table.csv` |

---

## Hands-on

> ทำตามลำดับเดียวกับ catch-up · หรือ paste robin ลง **empty flow** แล้วตรวจ Variables / Replay

### Step 0 — สร้าง flow + โฟลเดอร์ output

1. **New flow** → ชื่อ:

```text
LabSCB_StaticFxTable
```

2. **If folder exists** · Path:

```text
C:\PAD-Labs\output\lab-scb-alt
```

   · โหมด **Does not exist** → **Create folder** · Folder path `C:\PAD-Labs\output` · Folder name `lab-scb-alt`

### Step 1 — Launch Chrome

1. **Launch new Chrome** · Initial URL:

```text
https://app.bot.or.th/BTWS_STAT/statistics/ReportPage.aspx?language=TH&reportID=123
```

2. Wait for page to load timeout / Timeout: `90`
3. Variables produced: `Browser`

### Step 2 — Wait ตาราง + Wait ข้อความ USD

1. **Wait for web page content** · `%Browser%` · **Contain element** · UI element:

```text
Tbl_BotFx
```

   · Screen: `SCB StaticFx` · selector: `table#dgExcel` · FOR: `90`  
   · paste catch-up → UI Elements มาพร้อม ControlRepository  
   · ทำมือ → UI Picker ชี้ตาราง → Rename `Tbl_BotFx`

2. **Wait for web page content** · `%Browser%` · **Contain text** · Text:

```text
USD
```

   · FOR: `90` — ยืนยันว่าแถวข้อมูลโผล่แล้ว (ไม่ใช่แค่โครงตาราง)

3. **อย่า** ใช้ Wait วินาทีอย่างเดียวเป็นเกณฑ์หลัก

### Step 3 — Extract Entire HTML Table → `%BotFxTable%`

1. หน้ายังเปิดค้าง และ Step 2 ผ่านแล้ว
2. **Extract data from web page** · Browser: `%Browser%` · โหมด **Entire HTML table**
3. CSS ของตาราง:

```text
table#dgExcel
```

4. ตั้งชื่อคอลัมน์ Extract ให้ตรง catch-up (8 คอลัมน์ — ตาราง BOT มีลำดับ / รายการ / ค่าตามวันที่ 6 คอลัมน์):

```text
Seq
Item
D1
D2
D3
D4
D5
D6
```

5. Variables produced: `BotFxTable`
6. เปิด `%BotFxTable%` — ต้องมีหลายแถว (หน้านี้ static HTML ประมาณ 90+ แถว)

> Catch-up ใช้ `WebAutomation.ExtractData.ExtractHtmlTable` + `Control: table#dgExcel` โดยตรง  
> **ห้าม** ใช้ **Create new data table** ว่างแทน Extract — จะได้ 0 row เสมอ

### Step 4 — เขียน CSV (3 คอลัมน์แรก · สูงสุด 20 แถว)

1. **Set variable** Name `CsvBody` ← Value:

```text
ลำดับ,รายการ,ค่าล่าสุด
```

2. **Set variable** Name `RowLimit` ← `0`
3. **For each** · `%BotFxTable%` · Store into: `FxRow`
4. ภายในลูป:
   - ถ้า `%RowLimit%` >= `20` → **Exit loop**
   - ต่อบรรทัด CSV: `%FxRow[0]%,%FxRow[1]%,%FxRow[2]%` (Seq / Item / D1)
   - **Increase variable** `RowLimit` += 1
5. **Write text to file** · Text to write: `%CsvBody%`

```text
C:\PAD-Labs\output\lab-scb-alt\bot-fx-table.csv
```

   - If file exists: **Overwrite** · Encoding: UTF-8

### Step 5 — ปิด

1. **Close web browser** · `%Browser%`
2. Replay 1–2 ครั้ง — เปิด CSV แล้วต้องมีข้อมูลหลังหัวตาราง

## Acceptance

- [ ] Flow ชื่อ `LabSCB_StaticFxTable`
- [ ] มีโฟลเดอร์ `C:\PAD-Labs\output\lab-scb-alt\`
- [ ] **Launch new Chrome** ไปที่ ReportPage `reportID=123` (`language=TH`)
- [ ] Wait **Contain element** `Tbl_BotFx` แล้วตามด้วย Wait **Contain text** `USD` ก่อน Extract
- [ ] มี Extract Entire HTML Table → `%BotFxTable%` (ไม่ใช่ stub ตารางว่าง)
- [ ] มี `bot-fx-table.csv` หัว `ลำดับ,รายการ,ค่าล่าสุด` และมีข้อมูลอย่างน้อย 1 แถว (catch-up จำกัด ≤20)
- [ ] **Close web browser** · ไม่ได้ login / กรอกข้อมูลลูกค้า

## Troubleshooting

| อาการ | แนวทาง |
|-------|--------|
| `%BotFxTable%` = 0 row | ขาด Extract จริง — อย่าใช้ Create new data table ว่างแทน · paste catch-up ใหม่ |
| Extract ได้หัวแต่ไม่มีแถว | Wait **Contain text** `USD` ก่อน Extract · เลื่อนตารางให้อยู่ใน viewport |
| Designer: UI element wasn't found | paste ลง **empty** flow เพื่อให้ ControlRepository เข้า |
| ชื่อคอลัมน์ไม่ตรง | ตาม catch-up ใช้ `Seq`…`D6` · CSV ใช้ index `[0][1][2]` |
| หน้าเป็นภาษาอังกฤษ | ใช้ `language=TH` ใน URL ตาม Step 1 |
| โดเมน `app.bot.or.th` ถูกบล็อก | แจ้ง IT allowlist `*.bot.or.th` |

## Cleanup

ปิดเบราว์เซอร์ค้าง · ลบ CSV ทดสอบถ้าไม่ต้องการเก็บเรท

> **Catch-up:** ตามไม่ทัน → วาง [`scripts/static-fx-table.robin`](scripts/static-fx-table.robin) ใน flow **ว่าง** (partial-ui + bundled `SCB StaticFx` / `Tbl_BotFx`)
