from pathlib import Path
import csv
import zipfile
from xml.sax.saxutils import escape

ROOT = Path(r"D:\dev\github\Onto-IQ\power-automate-desktop")


def col_name(n: int) -> str:
    s = ""
    while n:
        n, r = divmod(n - 1, 26)
        s = chr(65 + r) + s
    return s


def sheet_xml(rows):
    lines = [
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>',
        '<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">',
        "<sheetData>",
    ]
    for r_idx, row in enumerate(rows, start=1):
        lines.append(f'<row r="{r_idx}">')
        for c_idx, value in enumerate(row, start=1):
            ref = f"{col_name(c_idx)}{r_idx}"
            text = "" if value is None else str(value)
            lines.append(
                f'<c r="{ref}" t="inlineStr"><is><t>{escape(text)}</t></is></c>'
            )
        lines.append("</row>")
    lines.append("</sheetData></worksheet>")
    return "\n".join(lines)


CONTENT_TYPES = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/>
  <Override PartName="/xl/worksheets/sheet1.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>
</Types>"""

RELS = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="xl/workbook.xml"/>
</Relationships>"""

WB_RELS = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet1.xml"/>
</Relationships>"""


def workbook_xml(sheet_name: str = "Sheet1") -> str:
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">
  <sheets>
    <sheet name="{escape(sheet_name)}" sheetId="1" r:id="rId1"/>
  </sheets>
</workbook>"""


def write_xlsx(path: Path, rows, sheet_name: str = "Sheet1") -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml", CONTENT_TYPES)
        z.writestr("_rels/.rels", RELS)
        z.writestr("xl/workbook.xml", workbook_xml(sheet_name))
        z.writestr("xl/_rels/workbook.xml.rels", WB_RELS)
        z.writestr("xl/worksheets/sheet1.xml", sheet_xml(rows))
    print(f"Wrote {path}")


def read_csv(path: Path):
    with path.open(encoding="utf-8", newline="") as f:
        return [list(row) for row in csv.reader(f)]


def main() -> None:
    jobs = [
        (
            ROOT / "labs/06-data-table-excel/assets/orders-input.csv",
            ROOT / "labs/06-data-table-excel/assets/orders-input.xlsx",
            "Orders",
        ),
        (
            ROOT / "labs/08-excel-web-roundtrip/assets/leads-input.csv",
            ROOT / "labs/08-excel-web-roundtrip/assets/leads-input.xlsx",
            "Leads",
        ),
        (
            ROOT / "labs/07-contoso-invoice-ops/assets/invoices-batch.csv",
            ROOT / "labs/07-contoso-invoice-ops/assets/invoices-batch.xlsx",
            "Invoices",
        ),
        (
            ROOT / "labs/10-capstone-sales-ops/assets/leads.csv",
            ROOT / "labs/10-capstone-sales-ops/assets/leads.xlsx",
            "Leads",
        ),
    ]
    for csv_path, xlsx_path, sheet in jobs:
        write_xlsx(xlsx_path, read_csv(csv_path), sheet_name=sheet)
    print("done")


if __name__ == "__main__":
    main()
