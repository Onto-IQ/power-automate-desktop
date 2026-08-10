# Lab SCB Alt — AJAX FX Rates

**วัน:** 1 · **ระดับ:** Intermediate · **ทดแทน:** [Lab 03 AJAX Table](../../03-web-scout/ajax-table/README.md)  
**ทักษะ:** Wait แถว dynamic + Extract + กรองด้วย If + CSV  
**Flow ชื่อ:** `LabSCB_AjaxFxRates`

## ลำดับการเรียน

| ขั้น | ไฟล์ | ทำอะไร |
|------|------|--------|
| 0 | [LESSON โมดูล](../LESSON.md) | dynamic wait / กฎความปลอดภัย |
| 1 | **[LESSON.md](LESSON.md)** | หน้า FX ของ SCB |
| 2 | **[LAB.md](LAB.md)** | Hands-on |

## วัตถุประสงค์

- เปิดหน้าอัตราแลกเปลี่ยน SCB แล้ว **Wait จนแถวสกุลเงินโผล่** (ไม่ใช้ Wait วินาทีอย่างเดียว)
- Extract ตาราง/รายการเรท
- กรองแถวที่สนใจ (เช่น มีคำว่า USD) แล้วเขียน CSV

## Prerequisites

- เปิดได้: [อัตราแลกเปลี่ยน SCB](https://www.scb.co.th/th/personal-banking/foreign-exchange-rates)
- แนะนำทำ [Static FX Table](../static-fx-table/README.md) มาก่อน

## Assets / Output

| | Path / ค่า |
|--|------------|
| Web UI | https://www.scb.co.th/th/personal-banking/foreign-exchange-rates |
| Criteria | [`../assets/fx-filter.csv`](../assets/fx-filter.csv) |
| CSV | `C:\PAD-Labs\output\lab-scb-alt\scb-fx-rates.csv` |

## บทที่เกี่ยวข้อง

- Lab มาตรฐาน: [03 AJAX Table](../../03-web-scout/ajax-table/README.md)
- ก่อนหน้า: [Static FX Table](../static-fx-table/README.md)
