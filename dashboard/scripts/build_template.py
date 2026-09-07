#!/usr/bin/env python3
"""
build_template.py
Creates a blank features-master.xlsx with four sheets:
  Features, BRDs, Benchmarks, README
Run: python3 scripts/build_template.py
Output: dashboard/features-master.xlsx
"""
import os, sys
from datetime import date
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side, numbers
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.formatting.rule import CellIsRule, FormulaRule
from openpyxl.comments import Comment

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "features-master.xlsx")

FONT = Font(name="Arial", size=10)
FONT_BOLD = Font(name="Arial", size=10, bold=True)
FONT_HEADER = Font(name="Arial", size=11, bold=True, color="FFFFFF")
FONT_TITLE = Font(name="Arial", size=14, bold=True, color="000045")
FILL_HEADER = PatternFill(start_color="000045", end_color="000045", fill_type="solid")
THIN_BORDER = Border(
    left=Side(style="thin", color="DCDCDC"),
    right=Side(style="thin", color="DCDCDC"),
    top=Side(style="thin", color="DCDCDC"),
    bottom=Side(style="thin", color="DCDCDC"),
)
ALIGN_WRAP = Alignment(wrap_text=True, vertical="top")
ALIGN_CENTER = Alignment(horizontal="center", vertical="center")

# Conditional formatting fills
FILL_LIVE = PatternFill(start_color="E8F5E9", end_color="E8F5E9", fill_type="solid")
FILL_PLANNED = PatternFill(start_color="E3F2FD", end_color="E3F2FD", fill_type="solid")
FILL_GAP = PatternFill(start_color="FFEBEE", end_color="FFEBEE", fill_type="solid")
FILL_RED = PatternFill(start_color="F44336", end_color="F44336", fill_type="solid")
FILL_AMBER = PatternFill(start_color="FFB300", end_color="FFB300", fill_type="solid")
FONT_RED = Font(name="Arial", size=10, color="FFFFFF")
FONT_AMBER = Font(name="Arial", size=10, color="000000")

LAST_ROW = 1003

# ── Features sheet ──────────────────────────────────────────────────────
FEATURES_COLS = [
    ("id",            12, "Stable identifier. Prefix = journey (ONB/SAU/US/MF/CF/RBO/LMS/IPO/CM/XJ) + 3-digit seq."),
    ("name",          35, "Short human-readable feature name."),
    ("journey",       20, "Which investor journey this belongs to. Use the dropdown."),
    ("status",        10, "Current lifecycle status. Use the dropdown."),
    ("definition",    50, "One-sentence description of what the feature does."),
    ("brd",           20, "Comma-separated BRD codes (e.g. ARCD-1234, ARCD-5678). Must match BRDs sheet."),
    ("competitors",   30, "Comma-separated competitor names that have this feature. Must match Benchmarks sheet."),
    ("priority",      10, "Gap priority score 0-25 (Competitive Pressure x Investor Demand). Gaps only."),
    ("tags",          25, "Comma-separated tags: differentiator, sahm-gap, deep-discovery, parity, cross-screen, etc."),
    ("area",          18, "Feature area within the journey. Saudi Market areas: Portfolio, Watchlist, Trading Actions, Stock Page, Orders, Market."),
    ("screen",        25, "Specific screen within the area. Maps to the screen inventory."),
    ("figma_link",    35, "URL to the Figma frame/page for this feature."),
    ("figma_status",  14, "Design maturity. Use the dropdown."),
    ("figma_file",    22, "Canonical Figma file containing the design for this feature. Use the dropdown."),
    ("live_date",     14, "Target go-live date (Planned) or actual go-live date (Live). DD MMM YYYY."),
    ("went_live",     14, "Actual date the feature shipped to production. DD MMM YYYY."),
    ("owner_pm",      20, "Product Manager responsible."),
    ("owner_squad",   20, "Squad that owns delivery."),
]

AREAS = [
    "Portfolio", "Watchlist", "Trading Actions",
    "Stock Page", "Orders", "Market",
    "ARB", "Local", "Global", "Corporate", "Minor",
]

JOURNEYS = [
    "Onboarding", "Saudi Market", "US Trading",
    "Mutual Funds", "Crowd Fund", "Robo Advisory",
    "LMS", "IPOs", "Cash Management", "Investor Engagement", "Platform",
]
STATUSES = ["Live", "Planned", "Gap"]
FIGMA_STATUSES = ["Designed", "In Review", "Approved", "As-Built"]
FIGMA_FILES = [
    "CDO", "Portfolios", "OnBoarding (KYC)", "Market", "Discover & Search",
    "Home", "Profile & Setting", "LMS", "Wealth Mgmt Dashboard", "Watchlist",
    "Bain", "Tradepad", "Orders", "Themes", "Trader Mode",
]

BRD_COLS = [
    ("brd_code",      15, "Unique BRD identifier (e.g. ARCD-1234)."),
    ("title",         45, "Full BRD title."),
    ("owner",         20, "Author / owner of the BRD."),
    ("status",        12, "Document status. Use the dropdown."),
    ("approved_date", 14, "Date the BRD was approved. DD MMM YYYY."),
    ("link",          40, "URL or file path to the BRD document."),
]
BRD_STATUSES = ["Draft", "In Review", "Approved", "Deprecated"]

BENCH_COLS = [
    ("name",    25, "Competitor or benchmark app name."),
    ("region",  12, "Market region: Saudi, GCC, Global, US."),
    ("type",    15, "Category: Broker, Fintech, Platform, Data."),
    ("primary", 10, "TRUE if this is a primary benchmark (tracked weekly)."),
]
BENCH_DATA = [
    ("Derayah",         "Saudi",  "Broker",   True),
    ("Derayah Smart",   "Saudi",  "Fintech",  True),
    ("Sahm",            "Saudi",  "Broker",   True),
    ("AlJazira Capital","Saudi",  "Broker",   True),
    ("Alinma Tadawul",  "Saudi",  "Broker",   True),
    ("Abyan",           "Saudi",  "Broker",   False),
    ("Moomoo",          "Global", "Broker",   True),
    ("Robinhood",       "US",     "Broker",   True),
    ("IBKR",            "Global", "Broker",   True),
    ("TradingView",     "Global", "Platform", False),
    ("thinkorswim",     "US",     "Platform", False),
    ("Investing.com",   "Global", "Data",     False),
]


def build_features_sheet(wb: Workbook):
    ws = wb.active
    ws.title = "Features"

    # Title row
    ws.merge_cells("A1:R1")
    c = ws["A1"]
    c.value = "ARC Features Master"
    c.font = FONT_TITLE

    ws.merge_cells("A2:R2")
    c2 = ws["A2"]
    c2.value = f"Last updated: {date.today().strftime('%d %b %Y')}  |  Schema v1.0  |  Do NOT edit JSON files directly — run xlsx-to-features-json.py"
    c2.font = Font(name="Arial", size=9, italic=True, color="808080")

    # Header row at row 3
    for ci, (col_name, width, comment_text) in enumerate(FEATURES_COLS, 1):
        cell = ws.cell(row=3, column=ci, value=col_name)
        cell.font = FONT_HEADER
        cell.fill = FILL_HEADER
        cell.alignment = ALIGN_CENTER
        cell.border = THIN_BORDER
        cell.comment = Comment(comment_text, "build_template.py")
        ws.column_dimensions[get_column_letter(ci)].width = width

    # Style data area
    for r in range(4, LAST_ROW + 1):
        for ci in range(1, len(FEATURES_COLS) + 1):
            cell = ws.cell(row=r, column=ci)
            cell.font = FONT
            cell.border = THIN_BORDER
            cell.alignment = ALIGN_WRAP

    # Freeze header
    ws.freeze_panes = "A4"

    # ── Data validations ──
    # journey (col C)
    dv_journey = DataValidation(
        type="list",
        formula1='"' + ",".join(JOURNEYS) + '"',
        allow_blank=True,
        showErrorMessage=True,
        errorTitle="Invalid journey",
        error="Pick from the dropdown.",
    )
    dv_journey.sqref = f"C4:C{LAST_ROW}"
    ws.add_data_validation(dv_journey)

    # status (col D)
    dv_status = DataValidation(
        type="list",
        formula1='"' + ",".join(STATUSES) + '"',
        allow_blank=True,
        showErrorMessage=True,
        errorTitle="Invalid status",
        error="Pick from the dropdown.",
    )
    dv_status.sqref = f"D4:D{LAST_ROW}"
    ws.add_data_validation(dv_status)

    # area (col J)
    dv_area = DataValidation(
        type="list",
        formula1='"' + ",".join(AREAS) + '"',
        allow_blank=True,
        showErrorMessage=True,
        errorTitle="Invalid area",
        error="Pick from the dropdown.",
    )
    dv_area.sqref = f"J4:J{LAST_ROW}"
    ws.add_data_validation(dv_area)

    # figma_status (col M)
    dv_figma = DataValidation(
        type="list",
        formula1='"' + ",".join(FIGMA_STATUSES) + '"',
        allow_blank=True,
    )
    dv_figma.sqref = f"M4:M{LAST_ROW}"
    ws.add_data_validation(dv_figma)

    # figma_file (col N)
    dv_figma_file = DataValidation(
        type="list",
        formula1='"' + ",".join(FIGMA_FILES) + '"',
        allow_blank=True,
        showErrorMessage=True,
        errorTitle="Invalid Figma file",
        error="Pick from the dropdown.",
    )
    dv_figma_file.sqref = f"N4:N{LAST_ROW}"
    ws.add_data_validation(dv_figma_file)

    # priority (col H) — whole number 0-25
    dv_priority = DataValidation(
        type="whole",
        operator="between",
        formula1="0",
        formula2="25",
        allow_blank=True,
        showErrorMessage=True,
        errorTitle="Invalid priority",
        error="Must be a whole number 0-25.",
    )
    dv_priority.sqref = f"H4:H{LAST_ROW}"
    ws.add_data_validation(dv_priority)

    # Date format on live_date (col O=15) and went_live (col P=16)
    for r in range(4, LAST_ROW + 1):
        ws.cell(row=r, column=15).number_format = "DD MMM YYYY"
        ws.cell(row=r, column=16).number_format = "DD MMM YYYY"

    # ── Conditional formatting ──
    range_str = f"A4:R{LAST_ROW}"

    # Row tint by status (col D)
    ws.conditional_formatting.add(range_str,
        FormulaRule(formula=['$D4="Live"'], fill=FILL_LIVE))
    ws.conditional_formatting.add(range_str,
        FormulaRule(formula=['$D4="Planned"'], fill=FILL_PLANNED))
    ws.conditional_formatting.add(range_str,
        FormulaRule(formula=['$D4="Gap"'], fill=FILL_GAP))

    # Slipped: live_date (col O) RED when Planned AND date < TODAY
    ws.conditional_formatting.add(f"O4:O{LAST_ROW}",
        FormulaRule(
            formula=['AND($D4="Planned", $O4<>"", $O4<TODAY())'],
            fill=FILL_RED, font=FONT_RED,
        ))

    # Undated: live_date (col O) AMBER when Planned AND date is empty
    ws.conditional_formatting.add(f"O4:O{LAST_ROW}",
        FormulaRule(
            formula=['AND($D4="Planned", $O4="")'],
            fill=FILL_AMBER, font=FONT_AMBER,
        ))

    # No Figma: figma_link (col L) AMBER when (Live or Planned) AND empty
    ws.conditional_formatting.add(f"L4:L{LAST_ROW}",
        FormulaRule(
            formula=['AND(OR($D4="Live",$D4="Planned"), $L4="")'],
            fill=FILL_AMBER, font=FONT_AMBER,
        ))


def build_brds_sheet(wb: Workbook):
    ws = wb.create_sheet("BRDs")

    ws.merge_cells("A1:F1")
    ws["A1"].value = "BRD Registry"
    ws["A1"].font = FONT_TITLE
    ws.merge_cells("A2:F2")
    ws["A2"].value = "Every BRD code referenced in the Features sheet should have an entry here."
    ws["A2"].font = Font(name="Arial", size=9, italic=True, color="808080")

    for ci, (col_name, width, comment_text) in enumerate(BRD_COLS, 1):
        cell = ws.cell(row=3, column=ci, value=col_name)
        cell.font = FONT_HEADER
        cell.fill = FILL_HEADER
        cell.alignment = ALIGN_CENTER
        cell.border = THIN_BORDER
        cell.comment = Comment(comment_text, "build_template.py")
        ws.column_dimensions[get_column_letter(ci)].width = width

    ws.freeze_panes = "A4"

    dv_brd_status = DataValidation(
        type="list",
        formula1='"' + ",".join(BRD_STATUSES) + '"',
        allow_blank=True,
    )
    dv_brd_status.sqref = f"D4:D{LAST_ROW}"
    ws.add_data_validation(dv_brd_status)

    for r in range(4, LAST_ROW + 1):
        ws.cell(row=r, column=5).number_format = "DD MMM YYYY"


def build_benchmarks_sheet(wb: Workbook):
    ws = wb.create_sheet("Benchmarks")

    ws.merge_cells("A1:D1")
    ws["A1"].value = "Competitor & Benchmark Registry"
    ws["A1"].font = FONT_TITLE
    ws.merge_cells("A2:D2")
    ws["A2"].value = "Canonical list. Competitor names in the Features sheet must match these exactly."
    ws["A2"].font = Font(name="Arial", size=9, italic=True, color="808080")
    ws.merge_cells("A3:D3")
    ws["A3"].value = "Add new competitors here first, then reference in Features."
    ws["A3"].font = Font(name="Arial", size=9, italic=True, color="808080")

    for ci, (col_name, width, comment_text) in enumerate(BENCH_COLS, 1):
        cell = ws.cell(row=4, column=ci, value=col_name)
        cell.font = FONT_HEADER
        cell.fill = FILL_HEADER
        cell.alignment = ALIGN_CENTER
        cell.border = THIN_BORDER
        cell.comment = Comment(comment_text, "build_template.py")
        ws.column_dimensions[get_column_letter(ci)].width = width

    for ri, (name, region, typ, primary) in enumerate(BENCH_DATA, 5):
        ws.cell(row=ri, column=1, value=name).font = FONT
        ws.cell(row=ri, column=2, value=region).font = FONT
        ws.cell(row=ri, column=3, value=typ).font = FONT
        ws.cell(row=ri, column=4, value=primary).font = FONT

    ws.freeze_panes = "A5"


def build_readme_sheet(wb: Workbook):
    ws = wb.create_sheet("README")
    ws.column_dimensions["A"].width = 100
    ws.sheet_properties.tabColor = "221AFB"

    lines = [
        ("ARC Features Master — Editor Guide", FONT_TITLE),
        ("", FONT),
        ("PURPOSE", FONT_BOLD),
        ("This workbook is the single source of truth for ARC platform features.", FONT),
        ("JSON files consumed by the dashboard views are GENERATED from this file.", FONT),
        ("Never edit the JSON files directly.", FONT),
        ("", FONT),
        ("UPDATE FLOW", FONT_BOLD),
        ("1. Open this file in Excel / Numbers / Google Sheets.", FONT),
        ("2. Add or edit rows in the Features, BRDs, or Benchmarks sheets.", FONT),
        ("3. Save the file.", FONT),
        ("4. Run:  python3 scripts/xlsx-to-features-json.py", FONT),
        ("5. Review the validation summary printed to the terminal.", FONT),
        ("6. Refresh the dashboard views in your browser.", FONT),
        ("", FONT),
        ("REQUIRED FIELDS (Features sheet)", FONT_BOLD),
        ("id — Must be unique. Use journey prefix + 3-digit number (e.g. SAU-001).", FONT),
        ("name — Short feature name.", FONT),
        ("journey — Must be from the dropdown list.", FONT),
        ("status — Must be Live, Planned or Gap.", FONT),
        ("", FONT),
        ("CONDITIONAL FIELDS", FONT_BOLD),
        ("definition — Strongly recommended for every feature.", FONT),
        ("brd — Required for Live and Planned. Comma-separated if multiple.", FONT),
        ("competitors — Required for Gap. Comma-separated; must match Benchmarks sheet.", FONT),
        ("priority — Required for Gap (0-25 score).", FONT),
        ("figma_link — Expected for Live and Planned.", FONT),
        ("live_date, went_live — Dates in DD MMM YYYY format.", FONT),
        ("", FONT),
        ("COMMA-SEPARATED FIELDS", FONT_BOLD),
        ("brd, competitors, and tags accept multiple values separated by commas.", FONT),
        ("Example:  ARCD-1234, ARCD-5678", FONT),
        ("Example:  Moomoo, Derayah, IBKR", FONT),
        ("Spaces around commas are trimmed automatically by the export script.", FONT),
        ("", FONT),
        ("JOURNEY PREFIXES FOR NEW IDs", FONT_BOLD),
        ("ONB = Onboarding          SAU = Saudi Market", FONT),
        ("US  = US Trading           MF  = Mutual Funds", FONT),
        ("CF  = Crowd Fund           RBO = Robo Advisory", FONT),
        ("LMS = LMS                  IPO = IPOs", FONT),
        ("CM  = Cash Management      IE  = Investor Engagement   PLT = Platform", FONT),
        ("", FONT),
        ("COMMON MISTAKES TO AVOID", FONT_BOLD),
        ("- Editing the JSON files directly (they get overwritten on export).", FONT),
        ("- Using a competitor name not in the Benchmarks sheet (generates a warning).", FONT),
        ("- Leaving id blank or duplicating an existing id (export will fail).", FONT),
        ("- Typing free-text in dropdown columns (use the dropdown).", FONT),
        ("- Entering dates in non-DD-MMM-YYYY format (export may misparse).", FONT),
        ("- Forgetting to run the export script after editing.", FONT),
    ]

    for ri, (text, font) in enumerate(lines, 1):
        cell = ws.cell(row=ri, column=1, value=text)
        cell.font = font
        cell.alignment = Alignment(wrap_text=True)


def main():
    wb = Workbook()
    build_features_sheet(wb)
    build_brds_sheet(wb)
    build_benchmarks_sheet(wb)
    build_readme_sheet(wb)
    wb.save(OUT)
    print(f"Created {os.path.abspath(OUT)}")


if __name__ == "__main__":
    main()
