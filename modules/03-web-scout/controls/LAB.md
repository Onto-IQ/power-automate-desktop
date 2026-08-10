# Lab 03 — Controls (Hands-on)

**อ่านก่อน:** [LESSON.md](LESSON.md) · **หน้าปก:** [README.md](README.md)

**Flow ชื่อ:** `Lab03_Controls` · **Optional**

## Setup

```text
C:\PAD-Labs\output\lab03\
```

## Hands-on

### Step 0 — สร้าง flow

```text
Lab03_Controls
```

### Step 1 — Launch

1. Initial URL:

```text
https://pad.ontoiq.tech/pad/02-controls.html
```

2. Variables produced: `Browser`

### Step 2 — ตั้งค่า control

1. ใช้ UI Picker เลือก dropdown / checkbox อย่างน้อยอย่างละหนึ่ง
2. ตั้งค่าให้ชัดเจน (เช่น เลือกตัวเลือกที่ไม่ใช่ค่าเริ่มต้น · ติ๊ก checkbox)
3. (ทางเลือก) **Get details of element on web page** อ่านค่าที่ตั้งไว้ → เก็บในตัวแปร เช่น `SelectedOption`, `CheckState`

### Step 3 — หลักฐาน

ทำอย่างน้อยหนึ่งอย่าง:

1. **Write text to file** → `C:\PAD-Labs\output\lab03\controls-result.csv`
2. ตัวอย่างเนื้อหา:

```text
SelectedOption,CheckState
(ค่าที่อ่านได้),(ค่าที่อ่านได้)
```

3. หรือ **Take screenshot** → `C:\PAD-Labs\output\lab03\controls.png`

### Step 4 — ปิด

1. **Close web browser** · `%Browser%`
2. Replay 1–2 ครั้ง

## Acceptance

- [ ] Flow ชื่อ `Lab03_Controls`
- [ ] มีหลักฐาน CSV หรือ screenshot
- [ ] ปิดเบราว์เซอร์ท้าย flow

## Cleanup

ปิดเบราว์เซอร์ค้าง

> **Catch-up:** ตามไม่ทัน → วาง [`scripts/03-controls.robin`](scripts/03-controls.robin) ใน flow **ว่าง** (partial-ui + bundled `Lab03 Controls`)
