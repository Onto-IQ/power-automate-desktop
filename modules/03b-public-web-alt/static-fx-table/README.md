# Lab 03b — Static FX Table

**วัน:** 1 · **ระดับ:** Intermediate · **ทักษะเทียบ:** [Lab 03 Static Table](../../03-web-scout/static-table/README.md)  
**ทักษะ:** Wait + Extract Entire HTML Table + เขียน CSV  
**Flow ชื่อ:** `Lab03b_StaticFxTable`

## ลำดับการเรียน

| ขั้น | ไฟล์ | ทำอะไร |
|------|------|--------|
| 0 | [LESSON โมดูล](../LESSON.md) | กฎโดเมน / selector เว็บจริง |
| 1 | **[LESSON.md](LESSON.md)** | ตาราง FX ธปท. |
| 2 | **[LAB.md](LAB.md)** | Hands-on |


## Reference script (catch-up)

สำหรับนักเรียนที่ทำตามไม่ทัน — เปิด [`scripts/static-fx-table.robin`](scripts/static-fx-table.robin) แล้ว copy วางใน desktop flow ว่าง

- partial-ui
- ไม่แทนการทำ LAB หลัก; ใช้เทียบลำดับ action / กู้งานให้ทันชั้น

## วัตถุประสงค์
- เปิดตารางอัตราแลกเปลี่ยนสาธารณะของ ธปท. แล้ว Wait จนตารางพร้อม
- Extract ทั้งตารางเป็น Data table
- เขียน CSV ลงโฟลเดอร์ output

## Prerequisites

- เปิดได้: [ReportPage reportID=123](https://app.bot.or.th/BTWS_STAT/statistics/ReportPage.aspx?language=TH&reportID=123)
- แนะนำทำ [Form Search](../form-search/README.md) มาก่อนถ้ายังไม่คุ้น Populate/Wait

## Assets / Output

| | Path / ค่า |
|--|------------|
| Web UI | https://app.bot.or.th/BTWS_STAT/statistics/ReportPage.aspx?language=TH&reportID=123 |
| CSV | `C:\PAD-Labs\output\lab03b\bot-fx-table.csv` |

## บทที่เกี่ยวข้อง

- Lab มาตรฐาน: [03 Static Table](../../03-web-scout/static-table/README.md)
- ต่อ: [AJAX FX Rates](../ajax-fx-rates/README.md)
