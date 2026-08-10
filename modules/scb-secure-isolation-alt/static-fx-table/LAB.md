# Lab SCB Alt — Static FX Table (Hands-on)

**อ่านก่อน:** [LESSON.md](LESSON.md) · **หน้าปก:** [README.md](README.md) · **โมดูล:** [`../README.md`](../README.md)

**Flow ชื่อ:** `LabSCB_StaticFxTable` · **ทดแทน Lab 03 Static**

## Setup

```text
C:\PAD-Labs\output\lab-scb-alt\
```

เปิดด้วยมือเพื่อยืนยันว่าตารางโหลด:

```text
https://app.bot.or.th/BTWS_STAT/statistics/ReportPage.aspx?language=TH&reportID=123
```

---

## Hands-on

### Step 0 — สร้าง flow

```text
LabSCB_StaticFxTable
```

### Step 1 — Launch

1. **Launch new Microsoft Edge** / **Chrome**
2. Initial URL:

```text
https://app.bot.or.th/BTWS_STAT/statistics/ReportPage.aspx?language=TH&reportID=123
```

3. Variables produced: `Browser`

### Step 2 — Wait ตาราง

1. **Wait for web page content** · `%Browser%` · **Contain element**
2. UI Picker ชี้ตารางที่มีแถว เช่น “อัตราอ้างอิง : ดอลลาร์สหรัฐ (USD)”
3. Rename:

```text
Tbl_BotFx
```

4. อย่าใช้ Wait วินาทีอย่างเดียวเป็นเกณฑ์หลัก

### Step 3 — Extract

1. ให้เบราว์เซอร์ของ flow เปิดค้างที่ URL ด้านบน
2. **Extract data from web page** · Browser: `%Browser%`
3. ชี้ตาราง → **คลิกขวา** → **Extract Entire HTML Table**
4. Variables produced: `BotFxTable`
5. เปิด `%BotFxTable%` ใน Variables pane แล้วจดชื่อคอลัมน์จริง

### Step 4 — เขียน CSV

1. **ก่อนลูป** ตั้งหัวตารางด้วย **Set variable** Name `CsvBody` ตามคอลัมน์ที่เห็นจริง (ตัวอย่างแนวทาง — ปรับให้ตรง Variables pane):

```text
ลำดับ,รายการ,ค่าล่าสุด
```

2. **For each** · Value to iterate: `%BotFxTable%` · Store into: `FxRow`
3. ภายในลูป ต่อสตริงแถว CSV จากคอลัมน์จริง เช่น `%FxRow['Column1']%` (ชื่อต้องตรง Variables pane)
4. จำกัดแถวก็ได้ (เช่น เก็บแค่ 20 แถวแรกด้วยตัวนับ) ถ้าตารางยาวมาก
5. **Write text to file**

```text
C:\PAD-Labs\output\lab-scb-alt\bot-fx-table.csv
```

   - Text to write: `%CsvBody%`
   - If file exists: **Overwrite**

### Step 5 — ปิด

1. **Close web browser** · `%Browser%`
2. Replay 1–2 ครั้ง

## Acceptance

- [ ] Flow ชื่อ `LabSCB_StaticFxTable`
- [ ] มี Wait + Extract ทั้งตาราง
- [ ] มีไฟล์ `bot-fx-table.csv` และเปิดใน Excel/Notepad แล้วมีข้อมูล
- [ ] ไม่ได้ login / กรอกข้อมูลลูกค้า

## Troubleshooting

| อาการ | แนวทาง |
|-------|--------|
| Extract ได้หัวแต่ไม่มีแถว | Wait ให้ตารางโผล่ก่อน · เลื่อนหน้าให้ตารางอยู่ใน viewport |
| ชื่อคอลัมน์ว่าง / Column1 | ใช้ชื่อจาก Variables pane เป็นแหล่งจริง |
| หน้าเป็นภาษาอังกฤษ | ใช้ `language=TH` ใน URL ตาม Step 1 |
| โดเมน `app.bot.or.th` ถูกบล็อก | แจ้ง IT allowlist `*.bot.or.th` |

## Cleanup

ปิดเบราว์เซอร์ค้าง
