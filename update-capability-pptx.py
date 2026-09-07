#!/usr/bin/env python3
"""
Add 22 missing capabilities from the PDF back into the PPTX.
- 13 rows added to Market Intelligence & Context (slide 26)
- 9 rows added to Stock Details (slide 27)
- Updates the Local Market section summary numbers
"""
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from copy import deepcopy
from lxml import etree
import os

# ── Paths ────────────────────────────────────────────────────────────────────
SRC = "/tmp/arc-19apr.pptx"
OUT_DIR = "/Users/ahmedalghamdi/Claude/ARC/projects/features-map/reports"
OUT = os.path.join(OUT_DIR, "ARC-Capability-Assessment-Updated-2026-04-22.pptx")

# ── Missing capabilities from PDF ────────────────────────────────────────────
# (row_num, capability, type, app_status, web_status, gap, jira)
# app/web: "yes"=rId3 (checkmark), "no"=rId4 (red X), "na"=text "N/A", ""=empty

MARKET_INTEL_MISSING = [
    (18, "Market display preferences", "Config", "no", "no", "", ""),
    (19, "Advance Market overview (up/Down, Net Flow)", "View", "no", "no", "", ""),
    (20, "Stock Screener (High Growth, Biggest Earnings)", "View", "no", "no", "", ""),
    (21, "Upcoming IPO", "View", "no", "no", "", ""),
    (22, "Recent IPO Performance", "View", "no", "no", "", ""),
    (23, "My position watchlist", "Config", "no", "no", "", "ARCD-91580"),
    (24, "Indices page", "Config", "no", "no", "", ""),
    (25, "Earnings Beat", "View", "no", "no", "", ""),
    (26, "Rating change list", "View", "no", "no", "", ""),
    (27, "Market Monitor", "View", "no", "no", "", ""),
    (28, "Market Liquidity", "View", "no", "no", "", "ARCD-41013"),
    (29, "Market Volatility", "View", "no", "no", "", "ARCD-58777"),
    (30, "Market alerts", "Action", "no", "no", "", ""),
]

STOCK_DETAILS_MISSING = [
    (18, "Next report estimation", "View", "no", "no", "", ""),
    (19, "Annual revenue trend", "View", "no", "no", "", ""),
    (20, "Cash flow (Annual/Quarterly)", "View", "no", "no", "", ""),
    (21, "Statements tab", "View", "no", "no", "", ""),
    (22, "Actions tab (Dividends/Splits)", "Config", "no", "no", "", ""),
    (23, "Insider Trades", "View", "no", "no", "", ""),
    (24, "Government Trades", "View", "no", "no", "", ""),
    (25, "Stock comparison", "Config", "no", "no", "", ""),
    (26, "Trade on Chart", "Action", "no", "no", "", "ARCD-72388"),
]

NS = {
    'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
    'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships',
}

def clone_row(table, template_row_idx=-1):
    """Clone a table row XML element."""
    tbl_xml = table._tbl
    template_tr = tbl_xml.findall('{http://schemas.openxmlformats.org/drawingml/2006/main}tr')[template_row_idx]
    new_tr = deepcopy(template_tr)
    tbl_xml.append(new_tr)
    return new_tr

def set_cell_text(tr, col_idx, text):
    """Set text in a specific cell of a row."""
    tcs = tr.findall('{http://schemas.openxmlformats.org/drawingml/2006/main}tc')
    tc = tcs[col_idx]
    # Find the text run and update it
    for r_elem in tc.findall('.//a:r', NS):
        t_elem = r_elem.find('a:t', NS)
        if t_elem is not None:
            t_elem.text = text
            return
    # If no run found, find paragraph and add one
    for p_elem in tc.findall('.//a:p', NS):
        # Check if there's a run
        runs = p_elem.findall('a:r', NS)
        if runs:
            runs[0].find('a:t', NS).text = text
        else:
            # Create a new run
            r = etree.SubElement(p_elem, '{http://schemas.openxmlformats.org/drawingml/2006/main}r')
            t = etree.SubElement(r, '{http://schemas.openxmlformats.org/drawingml/2006/main}t')
            t.text = text
        return

def set_cell_status(tr, col_idx, status, no_rid="rId4", yes_rid="rId3"):
    """Set App/Web cell to YES (checkmark), NO (red X), or N/A (text)."""
    tcs = tr.findall('{http://schemas.openxmlformats.org/drawingml/2006/main}tc')
    tc = tcs[col_idx]

    if status == "na":
        # Remove any blip, set text to N/A
        for blip in tc.findall('.//a:blip', NS):
            blip.getparent().getparent().getparent().remove(blip.getparent().getparent())
        set_cell_text(tr, col_idx, "N/A")
    elif status == "yes":
        # Update blip rId to checkmark
        for blip in tc.findall('.//a:blip', NS):
            blip.set('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed', yes_rid)
    elif status == "no":
        # Update blip rId to red X
        for blip in tc.findall('.//a:blip', NS):
            blip.set('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed', no_rid)

def add_rows_to_table(slide, slide_idx, missing_rows):
    """Add missing capability rows to a slide's table."""
    for shape in slide.shapes:
        if shape.has_table:
            table = shape.table
            orig_rows = len(table.rows)
            print(f"  Slide {slide_idx+1}: {orig_rows} rows → ", end="")

            for row_data in missing_rows:
                num, cap, typ, app, web, gap, jira = row_data
                tr = clone_row(table)

                set_cell_text(tr, 0, str(num))       # #
                set_cell_text(tr, 1, cap)             # Capability
                set_cell_text(tr, 2, typ + " ")       # Type (trailing space like original)
                set_cell_status(tr, 3, app)           # App
                set_cell_status(tr, 4, web)           # Web
                set_cell_text(tr, 5, gap)             # Gap
                set_cell_text(tr, 6, jira)            # Jira
                set_cell_text(tr, 7, "")              # Live Date

            new_rows = len(table.rows)
            print(f"{new_rows} rows (+{new_rows - orig_rows})")
            return new_rows - 1  # subtract header
    return 0


# ── Main ─────────────────────────────────────────────────────────────────────
p = Presentation(SRC)
print(f"Loaded: {SRC} ({len(p.slides)} slides)")

# Slide 26 (index 25) = Market Intelligence & Context
total_mi = add_rows_to_table(p.slides[25], 25, MARKET_INTEL_MISSING)

# Slide 27 (index 26) = Stock Details
total_sd = add_rows_to_table(p.slides[26], 26, STOCK_DETAILS_MISSING)

# ── Update cover slide (slide 1) date ───────────────────────────────────────
for shape in p.slides[0].shapes:
    if shape.has_text_frame:
        for para in shape.text_frame.paragraphs:
            if "3Apr2026" in para.text:
                for run in para.runs:
                    if "3Apr2026" in run.text:
                        run.text = run.text.replace("3Apr2026", "22Apr2026")
                        print(f"\n  Cover date updated: 3Apr2026 → 22Apr2026")

# ── Save ─────────────────────────────────────────────────────────────────────
os.makedirs(OUT_DIR, exist_ok=True)
p.save(OUT)
print(f"\nDone → {OUT}")
print(f"  Market Intelligence: now {total_mi} capabilities (was 17, +13)")
print(f"  Stock Details: now {total_sd} capabilities (was 17, +9)")
print(f"  Total added: 22 capabilities")
