import os
from typing import List


PAGE_WIDTH = 612  # 8.5 inches * 72
PAGE_HEIGHT = 792  # 11 inches * 72
LEFT_MARGIN = 54
TOP_MARGIN = 54
LINE_HEIGHT = 14


def escape_pdf_text(text: str) -> str:
    # Sanitize to ASCII-friendly text for Latin-1 PDF stream
    replacements = {
        "\u2013": "-",  # en dash
        "\u2014": "-",  # em dash
        "\u2019": "'",  # right single quote
        "\u2018": "'",  # left single quote
        "\u201c": '"',  # left double quote
        "\u201d": '"',  # right double quote
        "—": "-",
        "–": "-",
    }
    for k, v in replacements.items():
        text = text.replace(k, v)
    # Escape PDF special characters
    return text.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")


def build_content_stream(lines: List[tuple]) -> bytes:
    """
    lines: list of tuples (text, font_tag, size, x, y)
    font_tag should be 'F1' or 'F2'.
    """
    parts: List[str] = []
    parts.append("BT")
    current_font = None
    current_size = None
    for text, font_tag, size, x, y in lines:
        if current_font != font_tag or current_size != size:
            parts.append(f"/{font_tag} {size} Tf")
            current_font, current_size = font_tag, size
        parts.append(f"{x:.2f} {y:.2f} Td")
        parts.append(f"({escape_pdf_text(text)}) Tj")
    parts.append("ET")
    return ("\n".join(parts) + "\n").encode("latin-1")


def write_pdf(path: str):
    # Prepare textual content
    y = PAGE_HEIGHT - TOP_MARGIN
    x = LEFT_MARGIN

    def add_line(buf: List[tuple], text: str, font_tag: str = "F1", size: int = 10, extra_space: int = 0):
        nonlocal y
        y -= (LINE_HEIGHT + extra_space)
        buf.append((text, font_tag, size, x, y))

    content_lines: List[tuple] = []

    # Header
    add_line(content_lines, "SINI K. SUNNY", font_tag="F2", size=18, extra_space=-6)

    # Contact
    add_line(content_lines, "Email: siniksunny98@gmail.com | Phone: +91 9961634042 | Location: Arakkulam, Kerala, India", size=10)
    add_line(content_lines, "LinkedIn: linkedin.com/in/sini-k-sunny-2b618612a", size=10)

    # Summary
    add_line(content_lines, "PROFESSIONAL SUMMARY", font_tag="F2", size=12, extra_space=6)
    summary = (
        "Accounts professional skilled in AP/AR, agent commission accounting, monthly reporting, bank and vendor "
        "ledger reconciliation, intercompany entries, month-end close, GST invoice recording, petty cash control, and "
        "expense provisioning. Strong at managing vendor payments, email correspondence, and process accuracy."
    )

    # Simple word-wrapping
    def wrap(text: str, width: int = 95) -> List[str]:
        words = text.split()
        lines = []
        cur = []
        count = 0
        for w in words:
            if count + len(w) + (1 if cur else 0) > width:
                lines.append(" ".join(cur))
                cur = [w]
                count = len(w)
            else:
                if cur:
                    count += 1
                cur.append(w)
                count += len(w)
        if cur:
            lines.append(" ".join(cur))
        return lines

    for ln in wrap(summary):
        add_line(content_lines, ln, size=10)

    # Skills
    add_line(content_lines, "CORE SKILLS", font_tag="F2", size=12, extra_space=6)
    skill_lines = [
        "Accounts Payable (AP); Accounts Receivable (AR); Bank Reconciliation; Intercompany Accounting; Month-End Close; Aging Analysis; Invoice Processing; Vendor Management",
        "GST; GCC VAT; Tax Returns; Compliance; Audit Support; Financial Statements; Reporting; Microsoft Excel; Tally Prime; Tally ERP 9; Zoho",
    ]
    for ln in skill_lines:
        for wrapped in wrap(ln):
            add_line(content_lines, wrapped, size=10)

    # Experience
    add_line(content_lines, "WORK EXPERIENCE", font_tag="F2", size=12, extra_space=6)
    add_line(content_lines, "Accounts Officer — HCI Australia", font_tag="F2", size=11)
    add_line(content_lines, "09/2023 – Present | Kochi, India", size=10)
    exp1 = [
        "- Accounts Payables & Receivables management; timely vendor payments.",
        "- Daily bank statement reconciliation; vendor ledger reconciliation.",
        "- Agent commission accounting and expense provisioning.",
        "- Preparing monthly reports and assisting month-end close/finalization.",
        "- Monitoring and replying to accounts emails; intercompany entries recorded properly.",
        "- Petty cash reconciliation and GST invoice recording with accurate posting.",
    ]
    for item in exp1:
        for wrapped in wrap(item):
            add_line(content_lines, wrapped, size=10)

    add_line(content_lines, "Tax Accountant — Bestfolio Consulting & Accounting UAE", font_tag="F2", size=11, extra_space=6)
    add_line(content_lines, "06/2022 – 11/2022 | Dubai, UAE", size=10)
    exp2 = [
        "- Handled AP, AR, intercompany accounting, reconciliations, and maintained vendor/customer files.",
        "- Prepared journal entries and supported efficient accounting operations.",
        "- Performed VAT reporting (monthly/quarterly) per FTA; assisted in audits and issue resolution across UAE and KSA.",
        "- Prepared multiple tax returns; delivered schedules and management reports on time.",
    ]
    for item in exp2:
        for wrapped in wrap(item):
            add_line(content_lines, wrapped, size=10)

    # Education
    add_line(content_lines, "EDUCATION", font_tag="F2", size=12, extra_space=6)
    education = [
        "EA Course (Pursuing) — PrepQ Educare Solutions Private Ltd, Ernakulam | 12/2022 – Present",
        "M.Com (Finance & Taxation) — St. Joseph's College Moolamattom (MG University, Kottayam) | 06/2019 – 08/2021",
        "B.Com (Finance & Taxation) — St. Joseph's Academy of Higher Education & Research, Moolamattom | 07/2016 – 04/2019",
    ]
    for entry in education:
        for wrapped in wrap(entry):
            add_line(content_lines, wrapped, size=10)

    # Certifications
    add_line(content_lines, "CERTIFICATIONS", font_tag="F2", size=12, extra_space=6)
    certs = [
        "- Tally Prime with GCC VAT & GST (12/2021 – 02/2022)",
        "- Tally ERP 9 (12/2021 – 02/2022)",
        "- GCC VAT (12/2021 – 02/2022)",
    ]
    for c in certs:
        add_line(content_lines, c, size=10)

    # Languages
    add_line(content_lines, "LANGUAGES", font_tag="F2", size=12, extra_space=6)
    add_line(content_lines, "English — Full Professional Proficiency | Malayalam — Full Professional Proficiency", size=10)

    # Achievements
    add_line(content_lines, "ACHIEVEMENTS", font_tag="F2", size=12, extra_space=6)
    achievements = [
        "- Department Topper (B.Com) — 2019",
        "- Former NSS Volunteer",
        "- Presented at National Seminar on GST — Significance & Scope",
    ]
    for a in achievements:
        add_line(content_lines, a, size=10)

    # Build the content stream
    content = build_content_stream(content_lines)

    # PDF object assembly
    objects: List[bytes] = []

    def add_object(body: str | bytes) -> int:
        if isinstance(body, str):
            body_bytes = body.encode("latin-1")
        else:
            body_bytes = body
        objects.append(body_bytes)
        return len(objects)

    # 1: Catalog
    add_object("<< /Type /Catalog /Pages 2 0 R >>")

    # 2: Pages
    add_object(f"<< /Type /Pages /Kids [3 0 R] /Count 1 /MediaBox [0 0 {PAGE_WIDTH} {PAGE_HEIGHT}] >>")

    # 3: Page
    add_object("<< /Type /Page /Parent 2 0 R /Resources << /Font << /F1 4 0 R /F2 6 0 R >> >> /Contents 5 0 R >>")

    # 4: Font Helvetica
    add_object("<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>")

    # 5: Contents (stream)
    stream = b"stream\n" + content + b"endstream"
    add_object(f"<< /Length {len(content)} >>\n".encode("latin-1") + stream)

    # 6: Font Helvetica-Bold
    add_object("<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold >>")

    # Assemble full PDF with xref
    result = bytearray()
    result.extend(b"%PDF-1.4\n")

    xref_positions = [0]
    for i, obj in enumerate(objects, start=1):
        xref_positions.append(len(result))
        result.extend(f"{i} 0 obj\n".encode("latin-1"))
        result.extend(obj)
        result.extend(b"\nendobj\n")

    xref_start = len(result)
    count = len(objects)
    result.extend(f"xref\n0 {count + 1}\n".encode("latin-1"))
    # object 0
    result.extend(b"0000000000 65535 f \n")
    for pos in xref_positions[1:]:
        result.extend(f"{pos:010d} 00000 n \n".encode("latin-1"))

    trailer = f"trailer\n<< /Size {count + 1} /Root 1 0 R >>\nstartxref\n{xref_start}\n%%EOF\n"
    result.extend(trailer.encode("latin-1"))

    with open(path, "wb") as f:
        f.write(result)


if __name__ == "__main__":
    output = "/workspace/SINI_K_SUNNY_Resume_ATS.pdf"
    write_pdf(output)
    print(f"Generated: {output} (no external dependencies)")