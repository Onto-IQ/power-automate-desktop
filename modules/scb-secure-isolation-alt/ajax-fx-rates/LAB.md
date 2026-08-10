# Lab SCB Alt — AJAX FX Rates (Hands-on)

**อ่านก่อน:** [LESSON.md](LESSON.md) · **หน้าปก:** [README.md](README.md) · **โมดูล:** [`../README.md`](../README.md)

**Flow ชื่อ:** `LabSCB_AjaxFxRates` · **ทดแทน Lab 03 AJAX**

## Setup

```text
C:\PAD-Labs\output\lab-scb-alt\
```

อ่าน criteria: [`../assets/fx-filter.csv`](../assets/fx-filter.csv) → ค่าเริ่มต้น `CurrencyCode=USD`

เปิดด้วยมือ:

```text
https://www.scb.co.th/th/personal-banking/foreign-exchange-rates
```

รอจนเห็นแถวสกุลเงิน (เช่น USD) ก่อนเริ่ม Record/Picker

---

## Hands-on

### Step 0 — สร้าง flow + criteria

1. **New flow** → ชื่อ:

```text
LabSCB_AjaxFxRates
```

2. **Set variable** Name `CurrencyCode` ← Value:

```text
USD
```

### Step 1 — Launch

1. **Launch** Edge/Chrome · Initial URL:

```text
https://www.scb.co.th/th/personal-banking/foreign-exchange-rates
```

2. Variables produced: `Browser`

### Step 2 — Wait จนมีแถวเรท

1. **Wait for web page content** · `%Browser%` · **Contain element**
2. UI Picker ชี้ข้อความ/แถวที่มีสกุลเงิน เช่น `USD` หรือหัวตาราง BANK SELLS / BANK BUYS
3. Rename ตารางหรือคอนเทนเนอร์หลัก:

```text
Tbl_ScbFx
```

4. **อย่า** ใช้ Wait วินาทีอย่างเดียวเป็นเกณฑ์หลัก

### Step 3 — Extract

1. หน้ายังเปิดค้างและมีแถวแล้ว
2. **Extract data from web page** · `%Browser%`
3. ชี้ตารางเรท → คลิกขวา → **Extract Entire HTML Table** (ถ้ามี)
4. Variables produced: `ScbFxTable`
5. เปิด `%ScbFxTable%` จดชื่อคอลัมน์จริง
6. ถ้าหน้าไม่ใช่ `<table>` ล้วน: ใช้ live helper สร้างรายการซ้ำ (repeating data) แล้วตั้งชื่อตัวแปรเดียวกัน `ScbFxTable`

### Step 3b — สร้าง `%Hits%`

1. **Create new data table** หลัง Extract
2. ตั้งชื่อคอลัมน์**คัดลอกจาก** `%ScbFxTable%` ให้เหมือนทุกประการ
3. Variables produced: `Hits`

### Step 4 — กรองแถวที่มี CurrencyCode

1. **For each** · `%ScbFxTable%` · Store into: `FxRow`
2. ภายในลูป: **If** ข้อความในคอลัมน์สกุลเงิน **Contains** `%CurrencyCode%`  
   (เลือกคอลัมน์จากชื่อจริงใน Variables pane — อาจเป็นชื่อสกุล / currency / คอลัมน์แรก)
3. ถ้าเข้าเงื่อนไข: **Insert row into data table** · Data table: `%Hits%` · ค่าจาก `%FxRow%` ตามคอลัมน์
4. หลังลูป: แปลง `%Hits%` เป็นข้อความ CSV (หัวตาราง + แถว) เก็บใน `CsvBody`

### Step 5 — เขียนไฟล์

1. **Write text to file**

```text
C:\PAD-Labs\output\lab-scb-alt\scb-fx-rates.csv
```

2. If file exists: **Overwrite**
3. **Close web browser** · `%Browser%`
4. Replay 1–2 ครั้ง

## Acceptance

- [ ] Flow ชื่อ `LabSCB_AjaxFxRates`
- [ ] มี Wait ก่อน Extract
- [ ] มีการกรองด้วย `%CurrencyCode%` (ไม่ extract แล้วจบโดยไม่ If)
- [ ] มี `scb-fx-rates.csv` และมีอย่างน้อย 1 แถวที่เกี่ยวกับ USD (หรือสกุลที่ตั้งไว้)
- [ ] ไม่ได้ login / ทำรายการแลกเงิน

## Troubleshooting

| อาการ | แนวทาง |
|-------|--------|
| Wait timeout | เพิ่ม timeout · ชี้ element ที่โผล่ช้าจริง · ปิด popup/คุกกี้ถ้ามี |
| Extract ไม่ขึ้น “Entire HTML Table” | ใช้ repeating scrape แทน · หรือ Extract ทีละคอลัมน์ |
| `%Hits%` ว่าง | ตรวจชื่อคอลัมน์ Contains · ลอง `CurrencyCode=EUR` หรือค่าที่เห็นบนหน้า |
| หน้าเป็น English | ใช้ URL `/th/...` ตาม Step 1 หรือสลับภาษาบนหน้าแล้วจด selector ใหม่ |

## Cleanup

ปิดเบราว์เซอร์ค้าง · ลบ CSV ทดสอบถ้าไม่ต้องการเก็บเรท
