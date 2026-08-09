# Lab 03 — Static Table (Hands-on)

**อ่านก่อน:** [LESSON.md](LESSON.md) · **หน้าปก:** [README.md](README.md) · **พื้นฐาน:** [`shared/PAD-FUNDAMENTALS.md`](../../../shared/PAD-FUNDAMENTALS.md)

**Flow ชื่อ:** `Lab03_StaticTable` · **Core**

## Setup

```text
C:\PAD-Labs\output\lab03\
```

## Hands-on

### Step 0 — สร้าง flow

1. **New flow** → ชื่อ:

```text
Lab03_StaticTable
```

2. **Create**

> Name / Variables produced = ไม่มี `%` · อ้างอิงค่า = มี `%`

### Step 1 — Launch

1. **Launch new Microsoft Edge** หรือ **Chrome**
2. Initial URL:

```text
https://pad.ontoiq.tech/pad/03-table.html
```

3. Variables produced: `Browser`

### Step 2 — Wait ตาราง

1. **Wait for web page content**
2. Web browser instance: `%Browser%`
3. Wait for web page to: **Contain element**
4. UI element: picker ชี้ตาราง Emp ID / Name / Department / Salary
5. ชื่ออัตโนมัติอาจเป็น `Table 'Emp …'` — ปกติ
6. **Save**
7. แผง **UI Elements** → Rename เป็น:

```text
Tbl_Employees
```

8. ไม่มีช่องใน Wait ให้พิมพ์ `#tbl-employees`
9. Tips: คลิกขวา `Tbl_Employees` → **Edit** = Selector builder · ตรวจว่ามี `id` / `#tbl-employees` (Hints บนหน้า)

### Step 3 — Extract

1. ให้เบราว์เซอร์ของ flow เปิดค้างที่ URL ด้านล่าง (ถ้ายังไม่เปิด — รันถึง Launch ก่อน หรือเปิด URL นี้ใน instance ที่ `%Browser%` ชี้)

```text
https://pad.ontoiq.tech/pad/03-table.html
```

2. **Extract data from web page** · Browser: `%Browser%`
3. PAD จะเปิด **live web helper** บนหน้านั้น
4. ชี้ตารางพนักงาน (`#tbl-employees` · คอลัมน์ Emp ID / Name / Department / Salary)
5. **คลิกขวา** บนตาราง/เซลล์ในตาราง
6. เลือก **Extract Entire HTML Table**
7. Variables produced: `StaticTable`

### Step 4 — เขียน CSV จากแถวตาราง

1. แปลง `%StaticTable%` เป็นข้อความ CSV (วน **For each** Store into `StaticRow` แล้วประกอบข้อความ หรือใช้ action เขียน CSV ที่มีใน designer)
2. **Write text to file** (หรือเทียบเท่า) ไปที่:

```text
C:\PAD-Labs\output\lab03\static-table.csv
```

3. If file exists: Overwrite · แนะนำ UTF-8
4. ตัวอย่างคอลัมน์ผล: Emp ID, Name, Department, Salary (ตามที่ extract ได้)

### Step 5 — ปิดเบราว์เซอร์

1. **Close web browser** · `%Browser%`

### Step 6 — Replay

รันอย่างน้อย 2 ครั้ง · เปิด CSV ตรวจแถวพนักงาน (ประมาณ 5 แถวบนหน้า)

## Acceptance

- [ ] Flow ชื่อ `Lab03_StaticTable`
- [ ] Wait = Contain element + ตารางพนักงาน
- [ ] มีไฟล์ `static-table.csv`
- [ ] ปิดเบราว์เซอร์ท้าย flow
- [ ] ไม่ใช้ปุ่ม Next (หน้านี้ไม่มี pagination)

## Troubleshooting

| อาการ | แก้ |
|-------|-----|
| หา Next ไม่เจอ | ถูกแล้ว — ใช้ [Lab 03 Catalog](../catalog/README.md) ถ้าต้องการหลายหน้า |
| หา Edit selector ไม่เจอ | แผง UI Elements → คลิกขวา element → **Edit** (ไม่อยู่ในฟอร์ม Wait) |

## Cleanup

ปิดเบราว์เซอร์ค้าง · เก็บ CSV ไว้ตรวจ
