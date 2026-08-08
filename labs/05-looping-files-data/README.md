# Lab 05 — Looping Files / Data

**วัน:** 2 · **ระดับ:** Intermediate  
**ทักษะ:** For each, Loop index, รวมผลจากหลายไฟล์, Do until (challenge)

## วัตถุประสงค์

- ประมวลผลไฟล์เป็นชุด (batch)
- รวมยอด Amount จากหลาย CSV
- เขียนรายงานสรุปเดียว

## Setup

1. Flow `Lab05_LoopingFilesData`
2. คัดลอก `assets/batch` → `C:\PAD-Labs\working\lab05\batch`
3. Output: `C:\PAD-Labs\output\lab05\batch-summary.csv`

## Input / Output

| | Path |
|--|------|
| Batch files | [`assets/batch/`](assets/batch/) |
| Expected summary | [`assets/expected-batch-summary.csv`](assets/expected-batch-summary.csv) |
| Processed marker folder | `C:\PAD-Labs\working\lab05\processed\` |

### ไฟล์ batch

| ไฟล์ | Orders | รวม Amount (ตรวจเองได้) |
|------|--------|-------------------------|
| `batch-01.csv` | 2 | 20000 |
| `batch-02.csv` | 2 | 17500 |
| `batch-03.csv` | 1 | 9000 |
| **Total** | **5** | **46500** |

## PAD Action Sequence (แนะนำ)

1. Get files `*.csv` จาก batch folder → `%BatchFiles%`
2. สร้าง Data table ว่าง `%SummaryTable%` (คอลัมน์: FileName, RowCount, TotalAmount)
3. **For each** `%CurrentFile%`
   - Read CSV → `%FileTable%` (หรือ Excel read ถ้าแปลงแล้ว)
   - ตั้ง `%RowCount%`, `%TotalAmount% = 0`
   - **For each** row in `%FileTable%` บวก Amount
   - Add row เข้า `%SummaryTable%`
   - Copy/Move ไฟล์ไป `processed\`
4. เขียน `%SummaryTable%` เป็น CSV/Excel ที่ output
5. (Challenge) **Do until** `%RetryCount% > 3` หรือไฟล์ปรากฏ — จำลองรอไฟล์

## Variables

| Variable | Type |
|----------|------|
| `%BatchFiles%` | File list |
| `%FileTable%` | Data table |
| `%SummaryTable%` | Data table |
| `%TotalAmount%` | Numeric |
| `%GrandTotal%` | Numeric |

## Expected Result

- Summary มี 3 แถว (หนึ่งต่อไฟล์) และยอดรวม 46500
- ไฟล์ต้นทางถูกย้าย/คัดลอกไป processed

## Acceptance Criteria

- [ ] ใช้ For each ซ้อนหรือ For each + การรวมค่า
- [ ] ไม่คัดลอก action อ่านไฟล์แบบ hardcode ทีละไฟล์ 3 ชุดโดยไม่ลูป
- [ ] ตัวเลขตรง expected

## Troubleshooting

| อาการ | แก้ |
|-------|-----|
| Amount เป็น text | Convert text to number |
| Header นับเป็นแถว | Skip first line / set column names |

## Cleanup

- กู้ batch จาก `assets/batch` ก่อนรันซ้ำ
