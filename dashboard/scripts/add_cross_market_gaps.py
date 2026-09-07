#!/usr/bin/env python3
"""
add_cross_market_gaps.py
Adds cross-market gap features to features-master.xlsx:
- Saudi Live/Planned features missing from US Trading → new US Gap rows
- US Live/Planned features missing from Saudi Market → new Saudi Gap rows

Skips features that already exist as gaps in the target journey.
"""
import os, shutil
from datetime import date
from openpyxl import load_workbook

here = os.path.dirname(os.path.abspath(__file__))
dashboard_dir = os.path.join(here, "..")
xlsx_path = os.path.join(dashboard_dir, "features-master.xlsx")
backup_path = xlsx_path + f".bak-{date.today().isoformat()}-crossgap"

# Backup first
shutil.copy2(xlsx_path, backup_path)
print(f"Backup: {backup_path}")

wb = load_workbook(xlsx_path)
ws = wb["Features"]

# Read all existing features
existing = []
for row in ws.iter_rows(min_row=4, values_only=True):
    if not any(row[:4]):
        continue
    fid = str(row[0]).strip() if row[0] else None
    name = str(row[1]).strip() if row[1] else None
    journey = str(row[2]).strip() if row[2] else None
    status = str(row[3]).strip() if row[3] else None
    existing.append({"id": fid, "name": name, "journey": journey, "status": status})

# Get max IDs
us_ids = [int(f["id"].split("-")[1]) for f in existing if f["id"] and f["id"].startswith("US-")]
sau_ids = [int(f["id"].split("-")[1]) for f in existing if f["id"] and f["id"].startswith("SAU-")]
next_us = max(us_ids) + 1  # 032
next_sau = max(sau_ids) + 1  # 107

# Existing US feature names (lowercase for matching)
us_names = {f["name"].lower() for f in existing if f["journey"] == "US Trading"}
sau_names = {f["name"].lower() for f in existing if f["journey"] == "Saudi Market"}

# --- New US Gap features (from Saudi Live/Planned, not already in US) ---
# These are Saudi trading capabilities that don't exist in US Trading yet
# Excluding: Level 2 (US-011 Gap), Stock Comparison (US-016 Gap) — already exist
new_us_gaps = [
    {
        "name": "Conditional Orders (US)",
        "definition": "Support for conditional order types (if-then logic) on US market orders.",
    },
    {
        "name": "Stop Loss (US)",
        "definition": "Stop loss order type for US market positions to limit downside risk.",
    },
    {
        "name": "Take Profit (US)",
        "definition": "Take profit order type for US market positions to lock in gains at target price.",
    },
    {
        "name": "Basket Orders (US)",
        "definition": "Create and execute multiple US stock orders simultaneously as a basket.",
    },
    {
        "name": "Quick Reorder (US)",
        "definition": "One-tap reorder of previous US market trades from order history.",
    },
    {
        "name": "Bracket Order / OCO (US)",
        "definition": "One-cancels-other bracket orders combining stop loss and take profit for US trades.",
    },
    {
        "name": "Order Filter Panel (US)",
        "definition": "Advanced filtering panel for US market order history by status, date, and type.",
    },
    {
        "name": "Advanced Technical Analysis (US)",
        "definition": "Full technical analysis charting with indicators and drawing tools for US stocks.",
    },
]

# --- New Saudi Gap features (from US Live/Planned, not already in Saudi) ---
# US-028 Earnings Calendar — Saudi doesn't have this
new_sau_gaps = [
    {
        "name": "Earnings Calendar",
        "definition": "Calendar view of upcoming and past company earnings announcements for Saudi-listed stocks.",
    },
]

# Check for duplicates before adding
def name_exists(name, journey_names):
    return name.lower() in journey_names

# Filter out any that already exist
us_gaps_to_add = [g for g in new_us_gaps if not name_exists(g["name"], us_names)]
sau_gaps_to_add = [g for g in new_sau_gaps if not name_exists(g["name"], sau_names)]

print(f"\nAdding {len(us_gaps_to_add)} new US Trading Gap features (IDs US-{next_us:03d} to US-{next_us + len(us_gaps_to_add) - 1:03d})")
print(f"Adding {len(sau_gaps_to_add)} new Saudi Market Gap features (IDs SAU-{next_sau:03d} to SAU-{next_sau + len(sau_gaps_to_add) - 1:03d})")

# Find the last row with data
last_row = ws.max_row
# Find actual last used row
for r in range(ws.max_row, 3, -1):
    if any(ws.cell(row=r, column=c).value for c in range(1, 5)):
        last_row = r
        break

next_row = last_row + 1

# Write US Gap features
for i, gap in enumerate(us_gaps_to_add):
    fid = f"US-{next_us + i:03d}"
    row_idx = next_row + i
    ws.cell(row=row_idx, column=1, value=fid)        # A: id
    ws.cell(row=row_idx, column=2, value=gap["name"]) # B: name
    ws.cell(row=row_idx, column=3, value="US Trading") # C: journey
    ws.cell(row=row_idx, column=4, value="Gap")        # D: status
    ws.cell(row=row_idx, column=5, value=gap["definition"])  # E: definition
    print(f"  + {fid}: {gap['name']}")

next_row += len(us_gaps_to_add)

# Write Saudi Gap features
for i, gap in enumerate(sau_gaps_to_add):
    fid = f"SAU-{next_sau + i:03d}"
    row_idx = next_row + i
    ws.cell(row=row_idx, column=1, value=fid)           # A: id
    ws.cell(row=row_idx, column=2, value=gap["name"])    # B: name
    ws.cell(row=row_idx, column=3, value="Saudi Market") # C: journey
    ws.cell(row=row_idx, column=4, value="Gap")          # D: status
    ws.cell(row=row_idx, column=5, value=gap["definition"])  # E: definition
    print(f"  + {fid}: {gap['name']}")

wb.save(xlsx_path)
wb.close()

print(f"\nSaved: {xlsx_path}")
print(f"Total new features added: {len(us_gaps_to_add) + len(sau_gaps_to_add)}")
