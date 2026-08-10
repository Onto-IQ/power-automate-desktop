# Lab SCB Alt — Form Search (Hands-on)

**อ่านก่อน:** [LESSON.md](LESSON.md) · **หน้าปก:** [README.md](README.md) · **โมดูล:** [`../README.md`](../README.md)

**Flow ชื่อ:** `LabSCB_FormSearch` · **ทดแทน Lab 01**

## Setup บนเครื่อง

1. สร้างโฟลเดอร์:

```text
C:\PAD-Labs\output\lab-scb-alt\
```

2. เปิด URL นี้ด้วยมือหนึ่งครั้ง:

```text
https://www.bot.or.th/th/search.html
```

3. ถ้ามีแบนเนอร์คุกกี้ — กด **ยอมรับการใช้งานคุกกี้ที่จำเป็นเท่านั้น** (หรือเทียบเท่า) แล้วจำตำแหน่งปุ่มไว้

## ข้อมูลตัวอย่าง

**SearchKeyword**

```text
อัตราแลกเปลี่ยน
```

---

## Hands-on

### Step 0 — สร้าง flow

1. **New flow** → ชื่อ:

```text
LabSCB_FormSearch
```

2. **Create**

> Name / Variables produced = **ไม่มี `%`** · อ้างอิงค่า = มี `%`

### Step 1 — ตัวแปร

1. **Set variable**
   - Name: `SearchKeyword`
   - Value:

```text
อัตราแลกเปลี่ยน
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

1. **Wait for web page content** · ชี้ข้อความ/หัวข้อบนหน้าผลค้นหา (เช่น คำว่าผลลัพธ์ หรือรายการลิงก์แรก)
2. **Take screenshot** → บันทึก:

```text
C:\PAD-Labs\output\lab-scb-alt\search-proof.png
```

### Step 7 — ปิด

1. **Close web browser** · `%Browser%`
2. **Run** ทั้ง flow อย่างน้อย 2 ครั้งติดกัน

## Acceptance

- [ ] Flow ชื่อ `LabSCB_FormSearch`
- [ ] Populate จาก `%SearchKeyword%` ไม่ hardcode ใน action (มี Set variable)
- [ ] มี `search-proof.png`
- [ ] Replay ผ่านอย่างน้อย 2 ครั้ง
- [ ] **ไม่ได้** submit ฟอร์มติดต่อ/สมัครใด ๆ

## Troubleshooting

| อาการ | แนวทาง |
|-------|--------|
| หาช่องค้นหาไม่เจอ | ปิดแบนเนอร์คุกกี้ก่อน · หรือขยายหน้าต่างเบราว์เซอร์ |
| Autofill ทับช่อง | ปิด Autofill / กด `{Escape}` หลัง Populate |
| Replay ผ่านครั้งแรก ครั้งถัดไปพัง | ตรวจว่า Close browser ท้าย flow แล้ว Launch ใหม่ทุกครั้ง |
| UI Picker ชี้หน้าไม่ได้ทั้งที่เปิดเว็บได้ | Isolation remote browser — ดู [`../README.md`](../README.md) ข้อจำกัด |

## Cleanup

ปิดแท็บ/เบราว์เซอร์ค้างจาก lab
