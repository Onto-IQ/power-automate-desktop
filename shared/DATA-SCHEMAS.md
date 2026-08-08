# Shared Data Schemas

Schema อ้างอิงสำหรับ mock Excel/CSV ใน Labs 06–09

## Contoso Invoices (Desktop — Lab 07)

| Column | Type | Example | ใช้ใน |
|--------|------|---------|--------|
| InvoiceId | Text | INV-7001 | 07 |
| Account | Text | Contoso Retail | 07 |
| Contact | Text | Maya Scout | 07 |
| Amount | Number | 15000 | 07 |
| InvoiceDate | Date/Text | 2026-08-08 | 07 |
| StatusToSet | Text | Open / Paid | 07 |
| ProcessFlag | Text | Process / Skip | 07 |
| Notes | Text | High value deal | 07 |

## Leads (Input)

| Column | Type | Example | ใช้ใน |
|--------|------|---------|--------|
| LeadId | Text | L-1001 | 06, 08, 10 |
| FullName | Text | Somchai Jai | 01, 08, 10 |
| Email | Text | somchai@example.com | 08, 10 |
| Phone | Text | 081-000-1001 | 08 |
| Company | Text | Onto Demo Co. | 08, 10 |
| Interest | Text | PAD Training | 08, 10 |
| Priority | Text | High / Medium / Low | 04, 10 |
| Status | Text | New / Ready / Done | 08, 10 |

## Orders Scout (จาก Web / AJAX)

| Column | Type | Example | ใช้ใน |
|--------|------|---------|--------|
| OrderId | Text | ORD-2001 | 03, 10 |
| Customer | Text | Contoso Retail | 03, 10 |
| Product | Text | PAD License | 03, 10 |
| Amount | Number | 15000 | 03, 06, 07, 10 |
| OrderDate | Date/Text | 2026-08-01 | 03, 10 |
| Region | Text | BKK | 03, 10 |

## Scout Results (Output)

| Column | Type | Example | ใช้ใน |
|--------|------|---------|--------|
| ScoutId | Text | S-001 | 10 |
| SourcePage | Text | 09-ajax-table | 03, 10 |
| Key | Text | ORD-2001 | 10 |
| Value | Text | 15000 | 10 |
| CapturedAt | DateTime | 2026-08-08T10:00:00 | 10 |
| Notes | Text | matched High priority | 10 |

## Outlook Recipients (Mock)

| Column | Type | Example |
|--------|------|---------|
| DisplayName | Text | Ops Team (Mock) |
| Email | Text | ops.team@mock.local |
| Role | Text | To / Cc |
| SendMode | Text | DraftOnly |

> อย่าใช้ที่อยู่อีเมลของบุคคลจริงในชั้นเรียนสาธารณะ
