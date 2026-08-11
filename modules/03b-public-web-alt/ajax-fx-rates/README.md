# Lab 03b — AJAX FX Rates

**วัน:** 1 · **ระดับ:** Intermediate · **ทักษะเทียบ:** [Lab 03 AJAX Table](../../03-web-scout/ajax-table/README.md)  
**ทักษะ:** Wait แถว dynamic + Extract + กรองด้วย If + CSV  
**Flow ชื่อ:** `Lab03b_AjaxFxRates`

## ลำดับการเรียน

| ขั้น | ไฟล์ | ทำอะไร |
|------|------|--------|
| 0 | [LESSON โมดูล](../LESSON.md) | dynamic wait / กฎความปลอดภัย |
| 1 | **[LESSON.md](LESSON.md)** | หน้า FX สาธารณะ (dynamic) |
| 2 | **[LAB.md](LAB.md)** | Hands-on |


## Reference script (catch-up)

สำหรับนักเรียนที่ทำตามไม่ทัน — เปิด [`scripts/ajax-fx-rates.robin`](scripts/ajax-fx-rates.robin) แล้ว copy วางใน desktop flow ว่าง

- partial-ui
- ไม่แทนการทำ LAB หลัก; ใช้เทียบลำดับ action / กู้งานให้ทันชั้น

## วัตถุประสงค์
- เปิดหน้าอัตราแลกเปลี่ยนสาธารณะแล้ว **Wait จนแถวสกุลเงินโผล่** (ไม่ใช้ Wait วินาทีอย่างเดียว)
- Extract ตาราง/รายการเรท
- กรองแถวที่สนใจ (เช่น มีคำว่า USD) แล้วเขียน CSV

## Prerequisites

- เปิดได้: [อัตราแลกเปลี่ยน (สาธารณะ)](https://www.scb.co.th/th/personal-banking/foreign-exchange-rates)
- แนะนำทำ [Static FX Table](../static-fx-table/README.md) มาก่อน

## Assets / Output

| | Path / ค่า |
|--|------------|
| Web UI | https://www.scb.co.th/th/personal-banking/foreign-exchange-rates |
| Criteria | [`../assets/fx-filter.csv`](../assets/fx-filter.csv) |
| CSV | `C:\PAD-Labs\output\lab03b\bank-fx-rates.csv` |

## บทที่เกี่ยวข้อง

- Lab มาตรฐาน: [03 AJAX Table](../../03-web-scout/ajax-table/README.md)
- ก่อนหน้า: [Static FX Table](../static-fx-table/README.md)
