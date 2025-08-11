from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, ListFlowable, ListItem, HRFlowable
from reportlab.lib.units import inch


def section_title(text: str):
    return Paragraph(text.upper(), ParagraphStyle(
        name="SectionTitle",
        parent=styles["Heading2"],
        fontName="Helvetica-Bold",
        fontSize=12,
        leading=14,
        spaceBefore=10,
        spaceAfter=6,
        alignment=TA_LEFT,
        textColor=colors.black,
    ))


def bullet_list(items):
    return ListFlowable([
        ListItem(Paragraph(item, styles["BodyText"]), leftIndent=6, value='-') for item in items
    ], bulletType='bullet', start='-', leftIndent=12)


styles = getSampleStyleSheet()
styles["Normal"].fontName = "Helvetica"
styles["BodyText"].fontName = "Helvetica"
styles["BodyText"].fontSize = 10
styles["BodyText"].leading = 13

header_style = ParagraphStyle(
    name="Header",
    parent=styles["Heading1"],
    fontName="Helvetica-Bold",
    fontSize=18,
    leading=22,
    textColor=colors.black,
    spaceAfter=6,
)
subheader_style = ParagraphStyle(
    name="SubHeader",
    parent=styles["BodyText"],
    fontName="Helvetica",
    fontSize=10,
    leading=13,
    textColor=colors.black,
)


def build_pdf(path: str):
    doc = SimpleDocTemplate(
        path,
        pagesize=A4,
        rightMargin=36,
        leftMargin=36,
        topMargin=36,
        bottomMargin=36,
        title="Resume - ATS Friendly",
        author="SINI K. SUNNY",
    )

    story = []

    # Header: Name
    story.append(Paragraph("SINI K. SUNNY", header_style))

    # Contact block (single-line, ATS-friendly keywords)
    contact_lines = [
        "Email: siniksunny98@gmail.com | Phone: +91 9961634042 | Location: Arakkulam, Kerala, India",
        "LinkedIn: linkedin.com/in/sini-k-sunny-2b618612a",
    ]
    for line in contact_lines:
        story.append(Paragraph(line, subheader_style))
    story.append(Spacer(1, 8))
    story.append(HRFlowable(width='100%', thickness=0.8, color=colors.black, spaceBefore=4, spaceAfter=8))

    # Professional summary with targeted keywords for ATS
    story.append(section_title("Professional Summary"))
    summary_text = (
        "Detail-oriented Accounts and Tax Professional with hands-on experience across Accounts Payable, "
        "Accounts Receivable, Bank Reconciliation, Intercompany, Month-End Closing, and VAT/GST compliance. "
        "Proficient in Tally Prime/ERP 9, Microsoft Excel, and Zoho Books. Adept at stakeholder communication, "
        "reporting, and process improvement to strengthen internal controls and ensure accurate financial statements."
    )
    story.append(Paragraph(summary_text, styles["BodyText"]))

    # Core skills / keywords
    story.append(section_title("Core Skills"))
    skills_line_1 = (
        "Accounts Payable (AP); Accounts Receivable (AR); Bank Reconciliation; Intercompany Accounting; Month-End Close; "
        "Aging Analysis; Invoice Processing; Vendor Management"
    )
    skills_line_2 = (
        "GST; GCC VAT; Tax Returns; Compliance; Audit Support; Financial Statements; Reporting; "
        "Microsoft Excel; Tally Prime; Tally ERP 9; Zoho"
    )
    story.append(Paragraph(skills_line_1, styles["BodyText"]))
    story.append(Paragraph(skills_line_2, styles["BodyText"]))

    # Work Experience
    story.append(section_title("Work Experience"))

    # Role 1
    story.append(Paragraph("Accounts Officer — HCI Australia", ParagraphStyle(name="JobTitle", parent=styles["BodyText"], fontName="Helvetica-Bold")))
    story.append(Paragraph("09/2023 – Present | Kochi, India", styles["BodyText"]))
    items_role1 = [
        "Managed end-to-end Accounts Payable and Accounts Receivable with on-time payments and collections.",
        "Performed weekly reconciliation of bank statements to the general ledger and financial records.",
        "Reconciled vendor and customer ledgers; investigated discrepancies and processed adjustments.",
        "Monitored Birds portal invoicing and recorded documents in the business control system.",
        "Generated and reconciled intercompany transactions; validated intercompany GL balances monthly.",
        "Prepared age-wise debtor/creditor statements and supported disbursement/collection with plan monitoring.",
        "Participated in month-end closing activities and account finalization; prepared schedules and reports.",
        "Collaborated with stakeholders to improve payment plans and resolve account queries via email."
    ]
    story.append(bullet_list(items_role1))

    story.append(Spacer(1, 6))

    # Role 2
    story.append(Paragraph("Tax Accountant — Bestfolio Consulting & Accounting UAE", ParagraphStyle(name="JobTitle2", parent=styles["BodyText"], fontName="Helvetica-Bold")))
    story.append(Paragraph("06/2022 – 11/2022 | Dubai, UAE", styles["BodyText"]))
    items_role2 = [
        "Handled AP, AR, intercompany accounting, reconciliations, and maintained vendor/customer files.",
        "Prepared journal entries and supported smooth and efficient accounting operations.",
        "Performed VAT reporting (monthly/quarterly) aligned with FTA and other tax authorities.",
        "Assisted in tax audits, research, and resolution of accounting issues across geographies (UAE, KSA).",
        "Prepared multiple tax returns and supported management with timely reports and schedules."
    ]
    story.append(bullet_list(items_role2))

    # Education
    story.append(section_title("Education"))
    education_lines = [
        "EA Course (Pursuing) — PrepQ Educare Solutions Private Ltd, Ernakulam | 12/2022 – Present",
        "M.Com (Finance & Taxation) — St. Joseph's College Moolamattom (MG University, Kottayam) | 06/2019 – 08/2021",
        "B.Com (Finance & Taxation) — St. Joseph's Academy of Higher Education & Research, Moolamattom | 07/2016 – 04/2019",
    ]
    for line in education_lines:
        story.append(Paragraph(line, styles["BodyText"]))

    # Certifications
    story.append(section_title("Certifications"))
    certs = [
        "Tally Prime with GCC VAT & GST (12/2021 – 02/2022)",
        "Tally ERP 9 (12/2021 – 02/2022)",
        "GCC VAT (12/2021 – 02/2022)",
    ]
    story.append(bullet_list(certs))

    # Languages
    story.append(section_title("Languages"))
    story.append(Paragraph("English — Full Professional Proficiency | Malayalam — Full Professional Proficiency", styles["BodyText"]))

    # Achievements
    story.append(section_title("Achievements"))
    achievements = [
        "Department Topper (B.Com) — 2019",
        "Former NSS Volunteer",
        "Presented at National Seminar on GST — Significance & Scope",
    ]
    story.append(bullet_list(achievements))

    # Interests
    story.append(section_title("Interests"))
    story.append(Paragraph("Baking; Craft Work; Designing", styles["BodyText"]))

    # Footer note (ATS friendly: no graphics)
    story.append(Spacer(1, 12))
    story.append(HRFlowable(width='100%', thickness=0.6, color=colors.grey))
    story.append(Paragraph("References available upon request", ParagraphStyle(name="Footer", parent=styles["BodyText"], alignment=TA_LEFT, textColor=colors.grey)))

    doc.build(story)


if __name__ == "__main__":
    output_path = "/workspace/SINI_K_SUNNY_Resume_ATS.pdf"
    build_pdf(output_path)
    print(f"Generated: {output_path}")