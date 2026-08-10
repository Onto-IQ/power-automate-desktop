# Fault Injection Script — Lab 09b (Windows / Notepad)

ใช้เรียงลำดับ A → E (บังคับ) แล้ว F → H (Challenge) — ห้ามข้ามการ log  
กลไก PAD ทางการ: **On block error**, **On error** (Retry / Continue flow run), **Get last error** — ดู [Handle errors](https://learn.microsoft.com/power-automate/desktop-flows/errors)

> Lab นี้**ไม่ใช้ browser** — ทดแทน [Lab 09 web](../../09-error-handling/) เมื่อ Capture element บน web ถูกบล็อก

## Case A — Missing file

อ่าน path จาก `missing-file-path.txt` แล้วพยายาม **Read text from file**  
คาดหวัง: ไฟล์ไม่มีจริง → On block error → **Get last error** → เขียน log Case `A`

## Case B — Bad application path

อ่าน path จาก `bad-app-path.txt` แล้ว **Run application**  
คาดหวัง: exe ไม่มี → On block error → log Case `B` → Continue

## Case C — Flaky wait + Retry (Notepad)

1. **Run application** → `C:\Windows\System32\notepad.exe`
2. ใน Loop สูงสุด 3: **Wait for window** title ที่ตั้งใจผิด เช่น `ThisWindowDoesNotExist` (timeout สั้น)  
   → แต่ละครั้งที่ล้ม log `RETRY_WAIT` / Case `C`
3. แล้ว **Wait for window** ด้วย Window class `Notepad` (title ว่างได้) ให้สำเร็จ → log wait-success

## Case D — Save dialog (Notepad)

1. Focus Notepad ที่เปิดอยู่ (จาก Case C) หรือเปิดใหม่
2. พิมพ์ข้อความสั้น ๆ (**Populate text field in window** / **Send keys**)
3. **Close window** โดยยังไม่ Save → จัดการ dialog “Do you want to save?” → กด **Don't Save**
4. log `DIALOG_HANDLED`

## Case E — Recovery (Notepad Save As)

เปิด Notepad ใหม่ → Populate ข้อความจาก `notepad-recovery.txt` → Save As ไป:

```text
C:\PAD-Labs\output\lab09b\recovery-ok.txt
```

log `RECOVERY_OK` เมื่อสำเร็จ

## Case F — Wrong UI element · Challenge

พยายาม **Wait for window content** / **Populate** กับ element ที่จับผิด (หรือ title ผิด)  
→ log `UI_MISMATCH` แล้ว continue ด้วย element ที่ถูก

## Case G — File fault then recover · Challenge

1. **Copy file** / **Move file** จาก path ที่ไม่มี → log `FILE_MISSING`
2. Copy `recovery-upload.txt` ไป `C:\PAD-Labs\output\lab09b\` สำเร็จ → log `FILE_OK`

## Case H — Wrong window focus · Challenge

**Focus window** ด้วย title ที่ผิด → log `FOCUS_MISS`  
แล้ว **Focus window** class `Notepad` (หรือ title ที่ถูก) → log `FOCUS_OK`

## กฎคะแนนความทนทาน

- ไม่มี unhandled crash = ผ่านพื้นฐาน
- มี log ครบ A–E = ผ่านดี
- Case E สำเร็จหลัง A–D = ผ่านยอดเยี่ยม
- Challenge: ทำได้ ≥ 2 จาก F–H = resilience bonus
