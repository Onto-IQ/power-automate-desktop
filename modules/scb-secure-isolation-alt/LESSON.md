# SCB Secure Isolation Alt — ความรู้

**อ่านก่อนทำ Lab ย่อย** · หน้าปก: [README.md](README.md)

## ทำไมต้องมี Module นี้

Lab มาตรฐานใช้ **PAD Lab Hub** (`ontoiq.tech` / `pad.ontoiq.tech`) เพื่อให้มี `id` / `data-pad` เสถียร  
ในบางองค์กร (เช่น SCB) มี **Browser Secure Isolation** หรือ allowlist ทำให้โดเมน Lab Hub เข้าไม่ได้ — แต่ `bot.or.th` / `scb.co.th` เปิดได้

เป้าหมายของชุดนี้คือรักษาทักษะเดิมของ Lab 01 + Lab 03 Core โดยเปลี่ยนเฉพาะ “หน้าเว็บเป้าหมาย”

| ทักษะเดิม | บน Lab Hub | บนชุด SCB Alt |
|-----------|------------|----------------|
| Populate + Press button + Replay | 01-forms | ค้นหา ธปท. |
| Wait + Extract static table | 03-table | ตาราง FX ธปท. (app.bot.or.th) |
| Wait dynamic + Extract + กรอง | 09-ajax-table | อัตราแลกเปลี่ยน SCB |

## ทำไมไม่ใช้ฟอร์มสมัคร / ติดต่อธนาคาร

- สร้าง ticket / lead จริงโดยไม่ตั้งใจ
- เสี่ยงใส่ข้อมูลส่วนบุคคล
- ไม่สอดคล้องนโยบาย lab ในธนาคาร

ใช้ **ช่องค้นหา** และ **ตารางข้อมูลสาธารณะ** แทน — ได้ทักษะ Recorder / Populate / Extract เท่ากัน

## คุกกี้และแบนเนอร์

หน้า `bot.or.th` มักมีแบนเนอร์คุกกี้ก่อน Interact:

1. **Wait for web page content** ชี้ปุ่ม “จำเป็นเท่านั้น” หรือ “ยอมรับที่แนะนำ”
2. **Press button on web page**
3. ค่อย Populate / Extract

ถ้า Replay ล้มเพราะหาช่องค้นหาไม่เจอ — สงสัยแบนเนอร์ทับก่อนเสมอ

## Selector บนเว็บจริง

ไม่มี convention `#txt-name` / `data-pad` ของ Lab Hub:

1. Catch-up `scripts/*.robin` **bundle UI Elements** แล้ว (`SCB FormSearch` / `SCB StaticFx` / `SCB AjaxFx`) — paste ลง empty flow ได้ทันที
2. ถ้าทำเองในคลาส: ใช้ UI Picker แล้ว Rename เป็น `Txt_Search`, `Btn_Search`, `Tbl_BotFx`, `Tbl_ScbFx`
3. DOM เปลี่ยน → **Repair / Test selector** (custom CSS เช่น `input.serach-inputbox`, `table#dgExcel`, `table.table-rate`)

รายละเอียด: [`shared/SELECTOR-CONVENTIONS.md`](../../shared/SELECTOR-CONVENTIONS.md)

## เมื่อไหร่ที่ “เปลี่ยน URL แล้วยังทำไม่ได้”

Browser Secure Isolation บางแบบรันเว็บบน remote browser — PAD extension ที่ติดตั้งบนเครื่องผู้เรียน**คุมแท็บนั้นไม่ได้**

สัญญาณ:

- Launch เปิดได้ แต่ UI Picker ชี้ element บนหน้าไม่ได้
- Record แล้ว Replay ไม่เจอ element ทั้งที่เปิดหน้าด้วยมือได้

ทางออกด้าน IT (ไม่ใช่แก้ด้วย Lab):

- ขอโปรไฟล์ Edge/Chrome ปกติสำหรับห้องเรียน (ไม่ผ่าน isolation) หรือ
- allowlist โดเมน lab + อนุญาต PAD browser extension บน local browser

## ลำดับอ่านต่อ

1. [Form Search](form-search/LESSON.md) → [LAB](form-search/LAB.md)
2. [Static FX Table](static-fx-table/LESSON.md) → [LAB](static-fx-table/LAB.md)
3. [AJAX FX Rates](ajax-fx-rates/LESSON.md) → [LAB](ajax-fx-rates/LAB.md)
