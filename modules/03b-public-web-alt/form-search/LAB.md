# Lab 03b — Form Search (Hands-on)

**อ่านก่อน:** [LESSON.md](LESSON.md) · **หน้าปก:** [README.md](README.md) · **โมดูล:** [`../README.md`](../README.md)

**Flow ชื่อ:** `Lab03b_FormSearch` · **ทดแทน Lab 01**

## Setup บนเครื่อง

1. สร้างโฟลเดอร์:

```text
C:\PAD-Labs\output\lab03b\
```

2. เปิด URL นี้ด้วยมือหนึ่งครั้ง:

```text
https://www.bot.or.th/th/search.html
```

3. ถ้ามีแบนเนอร์คุกกี้ — กด **ยอมรับการใช้งานคุกกี้ที่จำเป็นเท่านั้น** (หรือเทียบเท่า) แล้วจำตำแหน่งปุ่มไว้

## ข้อมูลตัวอย่าง

**SearchKeyword** (ค่าเริ่มต้นใน catch-up — เป็นแท็กยอดนิยมบนหน้าค้นหา ธปท. ให้ผลค้นหาเดโมชัดกว่า `อัตราแลกเปลี่ยน`)

```text
แก้หนี้ยั่งยืน
```

ทางเลือกจาก [`../assets/search-keywords.csv`](../assets/search-keywords.csv): `ภาวะเศรษฐกิจ` · `คุณสู้เราช่วย` · `เงินเฟ้อ` · `นโยบายการเงิน`
---

## Hands-on

### Step 0 — สร้าง flow

1. **New flow** → ชื่อ:

```text
Lab03b_FormSearch
```

2. **Create**

> Name / Variables produced = **ไม่มี `%`** · อ้างอิงค่า = มี `%`

### Step 1 — ตัวแปร

1. **Set variable**
   - Name: `SearchKeyword`
   - Value:

```text
แก้หนี้ยั่งยืน
```

### Step 2 — Launch

1. **Launch new Microsoft Edge** หรือ **Chrome**
2. Initial URL:

```text
https://www.bot.or.th/th/search.html
```

3. Variables produced: `Browser`

### Step 3 — (ถ้ามี) ปิดแบนเนอร์คุกกี้

1. **Wait for web page content** · `%Browser%` · Contain element
2. UI Picker ชี้ปุ่มคุกกี้ “จำเป็นเท่านั้น” → Rename:

```text
Btn_CookieNecessary
```

3. **Press button on web page** · UI element: `Btn_CookieNecessary`
4. ถ้าไม่มีแบนเนอร์ — ข้าม Step นี้ได้

### Step 4 — กรอกค้นหา

1. **Wait for web page content** · ชี้ช่องค้นหา
2. Rename UI element:

```text
Txt_Search
```

3. **Populate text field on web page**
   - UI element: `Txt_Search`
   - Text: `%SearchKeyword%`
   - แนะนำปิด **Emulate typing** ถ้า Autofill รบกวน

### Step 5 — กดค้นหา

1. UI Picker ชี้ปุ่มค้นหา (หรือไอคอนแว่น) → Rename:

```text
Btn_Search
```

2. **Press button on web page** · `Btn_Search`  
   (ทางเลือก: **Send keys** `{Enter}` หลัง Populate ถ้าปุ่มหายาก)

### Step 6 — Wait ผลลัพธ์ + หลักฐาน

1. **Wait for web page content** · `%Browser%` · **Contain text** · Text: `%SearchKeyword%`  
   (catch-up รอให้ผลค้นหาโผล่ก่อนถ่ายภาพ — อย่า screenshot ทันทีหลัง Click)
2. **Take screenshot of web page** → บันทึก:

```text
C:\PAD-Labs\output\lab03b\search-proof.png
```

### Step 7 — ปิด

1. **Close web browser** · `%Browser%`
2. **Run** ทั้ง flow อย่างน้อย 2 ครั้งติดกัน

## Acceptance

- [ ] Flow ชื่อ `Lab03b_FormSearch`
- [ ] `SearchKeyword` = `แก้หนี้ยั่งยืน` (หรือค่าจาก `search-keywords.csv`) ผ่าน **Set variable** แล้ว Populate จาก `%SearchKeyword%`
- [ ] หลัง Click มี Wait **Contain text** `%SearchKeyword%` ก่อน screenshot
- [ ] มี `search-proof.png` ที่เห็นผลค้นหา (ไม่ใช่หน้าเปล่า)
- [ ] Replay ผ่านอย่างน้อย 2 ครั้ง
- [ ] **ไม่ได้** submit ฟอร์มติดต่อ/สมัครใด ๆ

## Troubleshooting

| อาการ | แนวทาง |
|-------|--------|
| ผลค้นหาไม่น่าสนใจ / ว่าง | เปลี่ยน `SearchKeyword` เป็นแท็กยอดนิยมบนหน้า เช่น `แก้หนี้ยั่งยืน` · `ภาวะเศรษฐกิจ` · `คุณสู้เราช่วย` |
| Screenshot ไม่มีผลลัพธ์ | เพิ่ม Wait **Contain text** หลัง Click ก่อน Take screenshot |
| หาช่องค้นหาไม่เจอ | ปิดแบนเนอร์คุกกี้ก่อน · หรือขยายหน้าต่างเบราว์เซอร์ |
| Autofill ทับช่อง | ปิด Autofill / กด `{Escape}` หลัง Populate |
| Replay ผ่านครั้งแรก ครั้งถัดไปพัง | ตรวจว่า Close browser ท้าย flow แล้ว Launch ใหม่ทุกครั้ง |
| UI Picker ชี้หน้าไม่ได้ทั้งที่เปิดเว็บได้ | Isolation remote browser — ดู [`../README.md`](../README.md) ข้อจำกัด |

## Cleanup

ปิดแท็บ/เบราว์เซอร์ค้างจาก lab

> **Catch-up:** ตามไม่ทัน → วาง [`scripts/form-search.robin`](scripts/form-search.robin) ใน flow **ว่าง** (partial-ui + bundled `Lab03b FormSearch`)
