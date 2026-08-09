# Lab 03 — Files (Hands-on)

**อ่านก่อน:** [LESSON.md](LESSON.md) · **หน้าปก:** [README.md](README.md)

**Flow ชื่อ:** `Lab03_Files` · **Optional**

## Setup

```text
C:\PAD-Labs\downloads\
C:\PAD-Labs\output\lab03\
```

คัดลอก [`assets/upload-sample.txt`](assets/upload-sample.txt) ไปที่ทำงานได้ เช่น:

```text
C:\PAD-Labs\working\lab03\upload-sample.txt
```

## Hands-on

### Step 0 — สร้าง flow

```text
Lab03_Files
```

### Step 1 — Launch

```text
https://pad.ontoiq.tech/pad/05-files.html
```

Variables produced: `Browser`

### Step 2 — Download

1. คลิกลิงก์/ปุ่ม download บนหน้า (UI Picker)
2. **Wait** จนไฟล์ปรากฏใน `C:\PAD-Labs\downloads\` (หรือโฟลเดอร์ download ของเบราว์เซอร์ที่ตั้งไว้)
3. (ทางเลือก) **If file exists** แล้วเขียนโน้ตสั้นลง `C:\PAD-Labs\output\lab03\files-evidence.txt`

### Step 3 — Upload

1. หา input อัปโหลดบนหน้า
2. ส่ง path:

```text
C:\PAD-Labs\working\lab03\upload-sample.txt
```

   (หรือ path ที่คุณคัดลอก sample ไว้)

3. Submit / Confirm ตาม UI หน้า

### Step 4 — ปิด

**Close web browser** · `%Browser%`

## Acceptance

- [ ] Flow ชื่อ `Lab03_Files`
- [ ] มีหลักฐาน download และ/หรือ upload สำเร็จ
- [ ] ปิดเบราว์เซอร์ท้าย flow

## Cleanup

ไฟล์ใน `downloads\` เก็บไว้ตรวจได้
