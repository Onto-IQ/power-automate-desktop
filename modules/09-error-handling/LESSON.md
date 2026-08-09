# Lab 09 — Error Handling (ความรู้)

**หน้าปก:** [README.md](README.md) · **ลงมือทำ:** [LAB.md](LAB.md) · **พื้นฐานร่วม:** [`shared/PAD-FUNDAMENTALS.md`](../../shared/PAD-FUNDAMENTALS.md)

**วัน:** 2 · **ระดับ:** Advanced · **อ่านประมาณ:** 20–30 นาที

## 1. บทนี้เรียนอะไร / จบแล้วทำอะไรได้

เมื่อจบบทนี้ คุณจะ:

- แยกได้ชัดว่า PAD **ไม่มี Action ชื่อ Try-Catch** — ใช้ **On block error**, **On error**, **Get last error**
- ออกแบบ flow ให้ทนต่อความล้มเหลวที่ตั้งใจจำลอง (fault injection)
- Log `%LastError.Message%` / `.Location%` แล้ว **Continue** งานถัดไป
- ตั้ง **Retry** อย่างจำกัดสำหรับ wait ที่ไม่เสถียร
- Cleanup ปิด browser/Excel แม้มี error ระหว่างทาง และพิสูจน์ด้วย Case E (recovery)

## 2. เรื่องราวจากงานจริง

ในงาน RPA จริง ไฟล์หาย URL พัง หน้าโหลดช้า และมี dialog เด้ขึ้นกลางทางเป็นเรื่องปกติ  
ถ้า flow หยุดทันทีทุกครั้งที่พัง ทีม ops จะต้องรันมือใหม่ทั้งชุด  
บทนี้จำลองเคสพังทีละแบบ (A→E) แล้วบังคับให้ flow **จับ → บันทึก → ไปต่อ** จนถึง happy path ท้ายชุด — นี่คือนิยาม “ทนทาน” ที่ใช้ต่อใน Capstone

> แนวคิด “Try–Catch” ในสไลด์ **สอดคล้องกับ** On block error / On error ใน PAD — อย่าค้นหา Action ชื่อ Try-Catch ใน designer  
> อ้างอิงทางการ: [Handle errors in desktop flows](https://learn.microsoft.com/power-automate/desktop-flows/errors) และ [`shared/OFFICIAL-TERMINOLOGY.md`](../../shared/OFFICIAL-TERMINOLOGY.md)

## 3. ศัพท์ทีละคำ

| ศัพท์ | ความหมายภาษาคน | เห็นที่ไหนใน PAD |
|--------|----------------|------------------|
| **On block error** | ครอบหลาย action เป็นบล็อก — กำหนดว่าเมื่อพังจะทำอะไร | ลากเป็นโครงสร้างใน workspace |
| **On error** | นโยบายต่อ **หนึ่ง action** (Retry / Continue flow run / Throw ฯลฯ) | แท็บ/ไอคอนในหน้าต่าง action |
| **Get last error** | อ่านรายละเอียด error ล่าสุดเพื่อ log หรือตัดสินใจ | **Variables produced** = `LastError` (ชนิด Error) |
| **Retry** | ลอง action เดิมอีกครั้งตามจำนวนที่จำกัด | ภายใต้ On error ของ action |
| **Continue flow run** | ไม่หยุดทั้ง flow หลัง error ของ action/บล็อก | นโยบาย On error / On block error |
| **Fault injection** | จงใจทำให้พังเพื่อทดสอบการกู้ | [`assets/fault-injection.md`](assets/fault-injection.md) |
| **Error log** | CSV ที่เก็บ Case / Message / Location | `error-log.csv` |
| **Recovery path** | งานที่ต้องสำเร็จหลังมี error ก่อนหน้า (Case E) | Forms 01 หลัง A–D |

## 4. แนวคิดหลัก

แนวคิดสำคัญ: **จับให้ได้ → บันทึกให้ครบ → ไปต่ออย่างควบคุม**  
แยกบทบาท:

| กลไก | ใช้เมื่อ |
|------|---------|
| **On block error** | ครอบ “ชุดเคส” (เช่น Case A ทั้งก้อน) แล้วไปกู้รวม |
| **On error** (ของ action) | ตั้ง Retry/Continue เฉพาะ Wait หรือ action ที่ flaky |
| **Get last error** | ทุกครั้งที่ต้องการข้อความจริงสำหรับ log — อย่ากลืนเงียบ |

```mermaid
flowchart TD
  init[Init + header error-log]
  A[Case A: Missing file]
  B[Case B: Bad URL + screenshot]
  C[Case C: Flaky wait + Retry]
  D[Case D: Dialogs]
  E[Case E: Forms recovery]
  clean[Close browser/Excel]
  init --> A --> B --> C --> D --> E --> clean
  A -.->|On block error| logA[Get last error → log → Continue]
  B -.->|On block error| logB[log + screenshot]
  C -.->|On error Retry| logC[log RETRY / OK]
```

Pseudo-flow:

```text
เขียน header error-log.csv
Case A: On block error { อ่านไฟล์ที่ไม่มี } → Get last error → append log → Continue
Case B: On block error { เปิด Bad URL } → log + screenshot ถ้าได้ → Continue
Case C: Wait บน 11-delay + On error → Retry (สูงสุด ~3) หรือ loop นับ RetryCount
Case D: จัดการ dialog บน 04-dialogs → log DIALOG_HANDLED
Case E: กรอก 01-forms สำเร็จ → log RECOVERY_OK
Close browser / Excel
```

**อย่าทำ:** เรียกกลไกเหล่านี้ว่า “ใส่ Try-Catch action” ในรายงาน/สไลด์ส่งงาน

## 5. ตาราง Action ที่จะใช้

| Action (official) | ทำอะไร | Input สำคัญ | **Variables produced** (ชื่อตอนสร้าง — ไม่มี `%`) |
|-------------------|--------|-------------|--------------------------------------|
| **On block error** | ครอบชุดงาน + นโยบายเมื่อพัง | Exception handling / Continue | — |
| **Get last error** | อ่าน error ล่าสุด | — | `LastError` |
| **Set variable** | path, RetryCount, Fatal | Name, Value | — |
| **Write text to file** | header + append แถว log | `%ErrorLogPath%`, Text | — |
| **Read text from file** | อ่าน missing path / bad URL | file path | `MissingPath`, `BadUrl` |
| **Launch new Edge/Chrome** / **Go to web page** | เปิดเพจทดสอบ | URL | `Browser` |
| **Wait for web page content** | รอ element (+ On error Retry) | UI element | — |
| **Take screenshot of web page** | เก็บหลักฐานตอนพัง | Browser, folder | file |
| **Populate…** / **Press button…** | Case E recovery | UI elements | — |
| **Close web browser** / **Close Excel** | cleanup | instance | — |

## 6. เปรียบเทียบตัวเลือกที่มักสับสน

| หัวข้อ | ตัวเลือก A | ตัวเลือก B | เลือกเมื่อไหร่ |
|--------|------------|------------|----------------|
| ชื่อกลไก | **On block error / On error / Get last error** | “Try-Catch action” | **ไม่มี** Try-Catch ใน designer — ใช้ชื่อทางการ |
| ขอบเขต | **On block error** (หลายขั้น) | **On error** ต่อหนึ่ง action | ชุดเคส vs Retry ของ Wait |
| หลัง error | **Continue** + log | Terminate ทั้ง flow | Lab นี้ต้องการไปต่อถึง Case E |
| Retry | จำกัดครั้ง (เช่น 3) | Retry ไม่จำกัด | ป้องกันลูปไม่จบ |
| Screenshot | มี browser instance | ถ่ายทั้งที่ browser ไม่เปิด | ตรวจ `%Browser%` ก่อน |

## 7. กฎ `%` และ Variables pane

- **Variables produced** ของ Get last error = `LastError` (**ไม่มี `%`**)
- ตอน log ใช้ `%LastError.Message%`, `%LastError.Location%` (**มี `%`**)
- รายละเอียดเต็ม: [`shared/PAD-FUNDAMENTALS.md`](../../shared/PAD-FUNDAMENTALS.md)

## 8. จุดที่มือใหม่พลาดบ่อย

| อาการ | สาเหตุที่พบบ่อย | วิธีสังเกต |
|-------|-----------------|------------|
| Error ถูกกลืน ไม่มีใน log | ไม่เรียก Get last error | เปิด error-log แล้วไม่มี Message |
| Retry ไม่จบ | ไม่จำกัดครั้ง | ดูรันค้างที่ Case C |
| Case E ไม่ถึง | Terminate กลางทาง / ลำดับเคสผิด | จัด A→E ตาม fault-injection |
| Screenshot ว่าง | ไม่มี browser | ตรวจ instance ก่อน Take screenshot |
| ค้นหา “Try-Catch” ใน Actions | สับสนกับภาษาโปรแกรม | ใช้ On block error ตาม docs |

## 9. คำถามทบทวน

**1.** ใน PAD มี Action ชื่อ Try-Catch หรือไม่?

<details>
<summary>เฉลย</summary>
<strong>ไม่มี</strong> — ใช้ <strong>On block error</strong>, <strong>On error</strong>, และ <strong>Get last error</strong> ตามเอกสาร Handle errors
</details>

**2.** On block error กับ On error ต่างกันอย่างไรโดยย่อ?

<details>
<summary>เฉลย</summary>
On block error ครอบหลาย action เป็นบล็อก; On error เป็นนโยบายของ action เดี่ยว (เช่น Retry ของ Wait)
</details>

**3.** Get last error ใช้ทำอะไรใน Lab นี้?

<details>
<summary>เฉลย</summary>
ดึง Message/Location ไปเขียน error-log — อย่างน้อย Case A ต้องมีแถว log จากกลไกนี้
</details>

**4.** Case C ควรจำกัด Retry อย่างไร?

<details>
<summary>เฉลย</summary>
ใช้ On error → Retry และ/หรือ Loop กับ RetryCount รวมแล้วแนวไม่เกิน 3 ครั้ง แล้วค่อยถือว่าล้มแบบควบคุม
</details>

**5.** ทำไม Case E ต้องอยู่หลัง A–D?

<details>
<summary>เฉลย</summary>
เพื่อพิสูจน์ <strong>recovery</strong>: หลังมี error จริงแล้ว flow ยัง Populate+Submit Forms ได้ และ log <code>RECOVERY_OK</code>
</details>

## 10. อ้างอิง (Aug 2026)

| แหล่ง | URL |
|-------|-----|
| Handle errors (หลักของ Lab) | https://learn.microsoft.com/power-automate/desktop-flows/errors |
| Actions pane / On error | https://learn.microsoft.com/power-automate/desktop-flows/actions-pane |
| Official terminology (Lab Kit) | [`shared/OFFICIAL-TERMINOLOGY.md`](../../shared/OFFICIAL-TERMINOLOGY.md) |
| รายการแหล่งใน Lab Kit | [PAD version matrix](https://learn.microsoft.com/power-platform/released-versions/power-automate-desktop) |

---

**ถัดไป:** เปิด [LAB.md](LAB.md) แล้วทำ fault cases A→E (และ Challenge F–I) ทีละขั้น
