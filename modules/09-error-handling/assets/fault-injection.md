# Fault Injection Script — Lab 09

ใช้เรียงลำดับ A → E (บังคับ) แล้ว F → I (Challenge Phase 1) — ห้ามข้ามการ log  
กลไก PAD ทางการ: **On block error**, **On error** (Retry / Continue flow run), **Get last error** — ดู [Handle errors](https://learn.microsoft.com/power-automate/desktop-flows/errors)

## Case A — Missing file

อ่าน path จาก `missing-file-path.txt` แล้วพยายาม **Read text from file**  
คาดหวัง: ไฟล์ไม่มีจริง → on error → เขียน log `MISSING_FILE`

## Case B — Bad URL

อ่าน URL จาก `bad-url.txt` แล้ว Launch browser  
คาดหวัง: ล้มหรือหน้า error → log `BAD_URL`

## Case C — Delay / flaky wait (Phase 1 / 11)

เปิด https://ontoiq.tech/pad/11-delay.html  
รอ element ผลลัพธ์ด้วย timeout สั้น + retry สูงสุด 3  
log แต่ละครั้งที่ timeout: `RETRY_WAIT`

## Case D — Dialogs (Phase 1 / 04)

เปิด https://ontoiq.tech/pad/04-dialogs.html  
สั่ง action ที่ทำให้เกิด alert/confirm แล้ว handle  
log `DIALOG_HANDLED` เมื่อผ่าน

## Case E — Recovery (Phase 1 / 01)

เปิด https://ontoiq.tech/pad/01-forms.html  
กรอก Name = `Recovery Scout` แล้ว submit  
log `RECOVERY_OK` เมื่อสำเร็จ

## Case F — OCR mismatch (Phase 1 / 10) · Challenge

เปิด https://ontoiq.tech/pad/10-ocr.html  
อ่านค่าจากภาพ/ช่องคำตอบ แล้วเปรียบเทียบกับค่าที่ตั้งใจให้ผิดพลาดครั้งแรก  
ถ้าไม่ตรง → log `OCR_MISMATCH` แล้วลองกรอกค่าที่อ่านได้จริง (recovery) → log `OCR_RECOVERED`

## Case G — Files fault then recover (Phase 1 / 05) · Challenge

เปิด https://ontoiq.tech/pad/05-files.html  
1. พยายาม upload path ที่ไม่มีจริง → log `UPLOAD_MISSING`  
2. Upload `recovery-upload.txt` ให้สำเร็จ → log `UPLOAD_OK`

## Case H — Iframe trap (Phase 1 / 08) · Challenge

เปิด https://ontoiq.tech/pad/08-iframe.html  
พยายามกรอกโดยยังไม่ switch iframe (คาดว่า fail หรือกรอกผิดที่) → log `IFRAME_MISS`  
แล้ว set current iframe ถูกต้อง กรอกใหม่ → log `IFRAME_OK`

## Case I — API bad then good (Phase 1 / 12) · Challenge

เปิด https://ontoiq.tech/pad/12-api.html หรือเรียก HTTP โดยตรง  
1. ยิง URL ผิด / path ไม่มี → log `API_BAD`  
2. ยิง health (หรือ endpoint ที่หน้าแนะนำ) ให้ได้สำเร็จ → log `API_OK`

## กฎคะแนนความทนทาน

- ไม่มี unhandled crash = ผ่านพื้นฐาน
- มี log ครบ A–E = ผ่านดี
- Case E สำเร็จหลัง A–D = ผ่านยอดเยี่ยม
- Challenge: ทำได้ ≥ 2 จาก F–I = Phase 1 resilience bonus
