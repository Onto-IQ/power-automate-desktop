# Lab 09 — Error Handling

**วัน:** 2 · **ระดับ:** Advanced  
**ทักษะ:** **On block error**, **On error** (Retry / Continue flow run), **Get last error**, การบันทึก log, screenshot และการปิดแอปอย่างปลอดภัย  
อ้างอิง: [Handle errors in desktop flows](https://learn.microsoft.com/power-automate/desktop-flows/errors) · [`shared/OFFICIAL-TERMINOLOGY.md`](../../shared/OFFICIAL-TERMINOLOGY.md)

## วัตถุประสงค์

- ทำให้ desktop flow ทนต่อความล้มเหลวที่ตั้งใจจำลองขึ้นมา
- บันทึก log ให้ตรวจสอบย้อนหลังได้ และไม่ทิ้ง Excel หรือเบราว์เซอร์ค้าง
- แยกได้ว่า error ใดควร retry และ error ใดควรถือว่าจบงานอย่างควบคุม

> แนวคิด “Try–Catch” ในสไลด์ สอดคล้องกับ **On block error** และ **On error** ใน PAD — ไม่มี Action ชื่อ Try-Catch ใน designer

## Setup

1. Flow `Lab09_ErrorHandling`
2. คัดลอก assets ไป `C:\PAD-Labs\working\lab09\`
3. สร้าง `C:\PAD-Labs\logs\lab09\`

## Test Cases (เจตนาให้พัง / กู้)

### Core cases

| Case | Phase 1 | ไฟล์/URL | พฤติกรรมที่คาด |
|------|---------|----------|----------------|
| A Missing file | — | path ใน [`assets/missing-file-path.txt`](assets/missing-file-path.txt) | On block error → **Get last error** → log → ไปต่อ |
| B Bad URL | — | [`assets/bad-url.txt`](assets/bad-url.txt) | จับ error เปิดเพจ → **Take screenshot of web page** (ถ้าได้) → continue |
| C Flaky wait | 11 | https://ontoiq.tech/pad/11-delay.html | **On error → Retry** และ/หรือ Loop + **Wait for web page content** สูงสุด 3 ครั้ง |
| D Dialog | 04 | https://ontoiq.tech/pad/04-dialogs.html | จัดการ alert/confirm โดยไม่ให้ flow ตายเงียบ |
| E Recover happy path | 01 | https://ontoiq.tech/pad/01-forms.html | หลัง error ก่อนหน้า ยัง Populate + Press button ได้ |

### Challenge cases (Phase 1 ที่เสริม)

| Case | Phase 1 | URL / ไฟล์ | พฤติกรรมที่คาด |
|------|---------|------------|----------------|
| F OCR mismatch | 10 | https://ontoiq.tech/pad/10-ocr.html | อ่านค่า OCR/hidden answer — ถ้าไม่ตรง log `OCR_MISMATCH` แล้ว continue |
| G Files fault | 05 | https://ontoiq.tech/pad/05-files.html | upload path ที่ไม่มี → จับ error แล้ว upload [`assets/recovery-upload.txt`](assets/recovery-upload.txt) |
| H Iframe trap | 08 | https://ontoiq.tech/pad/08-iframe.html | miss-frame แล้วกู้ด้วย set iframe ถูกต้อง |
| I API bad then good | 12 | https://ontoiq.tech/pad/12-api.html | endpoint ผิด → log → health ได้ 2xx |

รายละเอียดสคริปต์: [`assets/fault-injection.md`](assets/fault-injection.md)

## Input / Output

| | Path |
|--|------|
| Fault script | [`assets/fault-injection.md`](assets/fault-injection.md) |
| Log template | [`assets/error-log-template.csv`](assets/error-log-template.csv) |
| Your log | `C:\PAD-Labs\logs\lab09\error-log.csv` |

## PAD Action Sequence (แนะนำ)

1. Init `%RetryCount% = 0`, เขียน header log
2. **On block error** — Case A: อ่านไฟล์ที่ไม่มี → **Get last error** → append `%LastError.Message%` → Continue
3. Case B: **Launch new Microsoft Edge/Chrome** ไป URL ผิด → On error: log + **Take screenshot of web page**
4. Case C: **Go to web page** Delay → **Wait for web page content** พร้อม **On error → Retry action** (หรือ Loop condition จำกัด 3)
5. Case D: Dialogs — handle แล้ว log `DIALOG_HANDLED`
6. Case E: Forms — **Populate text field on web page** + **Press button on web page** → log `RECOVERY_OK`
7. (Challenge) Cases F–I
8. Cleanup: **Close web browser** / **Close Excel** แม้เกิด error

## Variables

| Variable | Type |
|----------|------|
| `%LastError%` | Error (จาก **Get last error**) |
| `%RetryCount%` | Numeric |
| `%ErrorLogPath%` | Text |
| `%Fatal%` | Boolean |

## Expected Result

- มี error-log อย่างน้อย 1 แถวสำหรับ Case A
- Flow ไม่หยุดแบบ unmanaged ก่อนจบชุดทดสอบ
- Case E สำเร็จหลังมี error ก่อนหน้า

## Acceptance Criteria

- [ ] ใช้ **On block error** อย่างน้อย 2 จุด
- [ ] ใช้ **Get last error** อย่างน้อย 1 ครั้งเมื่อ log
- [ ] มีไฟล์ log
- [ ] มีนโยบาย retry ชัดเจนสำหรับ Case C (**On error → Retry** และ/หรือ max loop)
- [ ] Cleanup ด้วย **Close web browser** / **Close Excel**
- [ ] (Challenge) ทำอย่างน้อย 2 จาก Cases F–I

## Troubleshooting

| อาการ | แก้ |
|-------|-----|
| Error ถูกกลืน ไม่รู้สาเหตุ | **Get last error** แล้ว log `%LastError.Message%` / `.Location%` |
| Retry ไม่จบ | จำกัดจำนวน retry ใน On error; หลีกเลี่ยง Repeat action ไม่จำกัด |
| Screenshot ว่าง | ตรวจว่ามี browser instance เปิดอยู่ |
| Selector ไม่เจอ | เพิ่ม Wait for web page content / recapture ([docs](https://learn.microsoft.com/troubleshoot/power-platform/power-automate/desktop-flows/ui-automation/failed-get-ui-element)) |

## Cleanup

- ล้าง logs เก่าก่อน demo รอบใหม่ถ้าต้องการไฟล์สะอาด

## หมายเหตุสไลด์ vs official

สไลด์อาจกล่าวถึง “Activate Phone Number Input” — **ไม่ใช่เกณฑ์บังคับของ Lab นี้** ให้ใช้ Wait for window content / Focus window / On error ตาม [official error handling](https://learn.microsoft.com/power-automate/desktop-flows/errors)
