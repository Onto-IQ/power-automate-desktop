# Lab 04 — Conditional Automation

**วัน:** 2 · **ระดับ:** Intermediate  
**ทักษะ:** If / Else If / Else, เปรียบเทียบข้อความ/ตัวเลข, จัดไฟล์ตามกฎธุรกิจ

## วัตถุประสงค์

- ใช้เงื่อนไขแยกเส้นทาง Flow
- จัดประเภทคำขอใน inbox ตาม Priority และ Status

## Prerequisites

- ผ่าน Lab 02 (แนวคิดไฟล์) จะช่วยได้
- คัดลอก `assets/inbox` → `C:\PAD-Labs\working\lab04\inbox`
- เตรียมโฟลเดอร์ `approved`, `rejected`, `review` ภายใต้ working (หรือให้ Flow สร้าง)

## Business Rules

| เงื่อนไข | Action |
|----------|--------|
| `Priority=High` และ `Status=Ready` | ย้ายไป `approved/` |
| `Priority=Low` หรือ `Status=Invalid` | ย้ายไป `rejected/` |
| อื่น ๆ | ย้ายไป `review/` |

กฎอยู่ใน [`assets/business-rules.md`](assets/business-rules.md) และสะท้อนในชื่อไฟล์ inbox

## Input / Output

| | Path |
|--|------|
| Inbox samples | [`assets/inbox/`](assets/inbox/) |
| Rules | [`assets/business-rules.md`](assets/business-rules.md) |
| Expected | [`assets/expected-routing.csv`](assets/expected-routing.csv) |
| Log | `C:\PAD-Labs\output\lab04\routing-log.csv` |

## PAD Action Sequence (แนะนำ)

1. Get files จาก inbox (`*.txt` หรือ `*.csv`)
2. For each file:
   - Read text **หรือ** parse ชื่อไฟล์ตาม pattern  
     `REQ-{id}-{Priority}-{Status}.txt`
   - **If** High **and** Ready → Move `approved`
   - **Else if** Low **or** Invalid → Move `rejected`
   - **Else** → Move `review`
   - Append แถวลง routing log
3. เขียนสรุปจำนวนแต่ละถัง

## Variables

| Variable | Type |
|----------|------|
| `%Priority%` | Text |
| `%Status%` | Text |
| `%ApprovedCount%` | Numeric |
| `%RejectedCount%` | Numeric |
| `%ReviewCount%` | Numeric |

## Expected Result

ตรงกับ `expected-routing.csv` (จำนวนและปลายทาง)

## Acceptance Criteria

- [ ] ใช้ If / Else If / Else อย่างชัดเจน
- [ ] ไม่ hardcode รายชื่อไฟล์ทีละไฟล์ในหลาย action แยก (ใช้ลูป)
- [ ] มี log ผลลัพธ์

## Troubleshooting

| อาการ | แก้ |
|-------|-----|
| เงื่อนไขไม่เข้าสาขา | ตรวจตัวพิมพ์เล็ก-ใหญ่; ใช้ Trim |
| Move ล้มเหลว | สร้างโฟลเดอร์ปลายทางก่อน |

## Cleanup

- รีเซ็ต working จาก `assets/inbox` ก่อนสาธิตซ้ำ
