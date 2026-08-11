# Lab 09 — Error Handling (ความรู้)

**หน้าปก:** [README.md](README.md) · **ลงมือทำ:** [LAB.md](LAB.md) · **พื้นฐานร่วม:** [`shared/PAD-FUNDAMENTALS.md`](../../shared/PAD-FUNDAMENTALS.md)

**วัน:** 2 · **ระดับ:** Advanced · **อ่านประมาณ:** 20–30 นาที

## 1. บทนี้เรียนอะไร / จบแล้วทำอะไรได้

เมื่อจบบทนี้ คุณจะ:

- แยกได้ชัดว่า PAD **ไม่มี Action ชื่อ Try-Catch** — ใช้ **On block error**, **On error**, **Get last error**
- อธิบายนโยบาย **On error** สามแบบหลักได้: **Stop flow** (ค่าเริ่มต้น / throw ไป caller), **Continue flow run**, **Retry / Repeat action**
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
| **On error** | นโยบายต่อ **หนึ่ง action** | แท็บ/ไอคอน **On error** ในหน้าต่าง action |
| **Stop flow** (ค่าเริ่มต้น) | ไม่ตั้ง On error เพิ่ม → โฟลว์หยุดเมื่อพัง และถ้าถูกเรียกจาก parent/cloud จะเห็นว่าโฟลว์ล้ม (throw ไป caller) | พฤติกรรม default ตาม [Handle errors](https://learn.microsoft.com/power-automate/desktop-flows/errors) |
| **Continue flow run** | ไม่หยุดทั้ง flow — ข้าม error แล้วไปต่อ (เช่น **Go to next action**) | checkbox / ตัวเลือกใต้ On error |
| **Retry action** | ลอง action เดิมซ้ำตามจำนวนครั้ง + หน่วงวินาทีที่กำหนด | **Retry action if an error occurs** |
| **Repeat action** | ภายใต้ Continue flow run — ทำซ้ำจนกว่าจะสำเร็จ (ระวังลูปไม่จบ) | dropdown ของ Continue flow run |
| **Get last error** | อ่านรายละเอียด error ล่าสุดเพื่อ log หรือตัดสินใจ | **Variables produced** = `LastError` (ชนิด Error) |
| **Fault injection** | จงใจทำให้พังเพื่อทดสอบการกู้ | [`assets/fault-injection.md`](assets/fault-injection.md) |
| **Error log** | CSV ที่เก็บ Case / Message / Location | `error-log.csv` |
| **Recovery path** | งานที่ต้องสำเร็จหลังมี error ก่อนหน้า (Case E) | Forms 01 หลัง A–D |

## 4. แนวคิดหลัก

แนวคิดสำคัญ: **จับให้ได้ → บันทึกให้ครบ → ไปต่ออย่างควบคุม**  
ทบทวนโครงจาก Lab 07 R6 (Contoso): ใน handler = SET flag อย่างเดียว → นอกบล็อก = Get last error + log  

### นโยบาย On error สามแบบ (ต้องพูดในชั้น)

| นโยบาย | พฤติกรรม | ใช้เมื่อ | ใน Lab 09 |
|--------|----------|---------|-----------|
| **Stop flow** (default) | หยุดรันทันทีเมื่อพัง — แจ้งว่าโฟลว์ล้ม / throw ไป caller | error ที่ไม่ควรกลืน (ข้อมูลสำคัญเสีย, ไม่มีทางกู้) | **สาธิตสั้น** ก่อน Case A: รัน Read ไฟล์ที่ไม่มีโดยไม่ครอบ On block error → โฟลว์แดงแล้วหยุด |
| **Continue flow run** | ข้าม error แล้วไป action ถัดไป (หรือ label / ท้ายบล็อก) | จับ → log → ไปเคสถัดไปได้ | Case A / B / D / E — เป้าหมายหลักของบท |
| **Retry action** (+ จำกัดครั้ง) | ลอง action เดิมอีกครั้งตามครั้ง/วินาที | wait/flaky ที่มักสำเร็จในรอบถัดไป | Case C — หรือใช้ Loop นับ `RetryCount` แทน/คู่กัน |

> **Repeat action** ใต้ Continue flow run ≠ Retry แบบจำกัดครั้ง — Repeat จะวนจนกว่าจะสำเร็จ ห้ามใช้โดยไม่จำกัดในห้องเรียน  
> อ้างอิง UI: [Handle errors — Configure error-handling](https://learn.microsoft.com/power-automate/desktop-flows/errors#configure-error-handling-functionality)

แยกบทบาทโครงสร้าง:

| กลไก | ใช้เมื่อ |
|------|---------|
| **On block error** | ครอบ “ชุดเคส” (เช่น Case A ทั้งก้อน) แล้วไปกู้รวม |
| **On error** (ของ action) | ตั้ง Retry / Continue เฉพาะ Wait หรือ action ที่ flaky |
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
| หลัง error | **Continue flow run** + log | **Stop flow** (default) | Lab หลัก A→E ต้อง Continue ถึง Case E; Stop ใช้สาธิต “โฟลว์พัง” เท่านั้น |
| ลองซ้ำ | **Retry action** จำกัดครั้ง (เช่น 3) | **Repeat action** ไม่จำกัด / Retry ไม่จำกัด | Case C ใช้ Retry หรือ Loop `RetryCount` — ห้าม Repeat ไม่จำกัด |
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

**4.** Stop flow / Continue flow run / Retry ต่างกันอย่างไร?

<details>
<summary>เฉลย</summary>
<strong>Stop flow</strong> = ค่าเริ่มต้น โฟลว์หยุดและแจ้งว่าพัง (throw ไป caller ถ้ารันจาก parent)<br>
<strong>Continue flow run</strong> = ข้าม error แล้วไป action ถัดไปได้<br>
<strong>Retry action</strong> = ลอง action เดิมซ้ำตามจำนวนครั้ง/หน่วงที่ตั้ง — ไม่ใช่ Repeat ไม่จำกัด
</details>

**5.** Case C ควรจำกัด Retry อย่างไร?

<details>
<summary>เฉลย</summary>
ใช้ On error → Retry และ/หรือ Loop กับ RetryCount รวมแล้วแนวไม่เกิน 3 ครั้ง แล้วค่อยถือว่าล้มแบบควบคุม — อย่าใช้ Repeat action โดยไม่จำกัด
</details>

**6.** ทำไม Case E ต้องอยู่หลัง A–D?

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
