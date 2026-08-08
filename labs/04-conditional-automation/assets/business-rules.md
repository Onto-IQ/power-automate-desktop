# Business Rules — Lab 04

## Routing

1. **Approved** — `Priority == High` AND `Status == Ready`
2. **Rejected** — `Priority == Low` OR `Status == Invalid`
3. **Review** — ทุกกรณีอื่น (เช่น Medium, หรือ High แต่ยัง New)

## รูปแบบชื่อไฟล์ mock

```text
REQ-{LeadId}-{Priority}-{Status}.txt
```

ตัวอย่าง: `REQ-L1001-High-Ready.txt`
