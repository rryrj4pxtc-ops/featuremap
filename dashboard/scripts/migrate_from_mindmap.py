#!/usr/bin/env python3
"""
migrate_from_mindmap.py
Parses the inline JS dataset from features-mind-map-2026-05-04.html,
generates stable IDs, reassigns pseudo-categories to real journeys,
populates features-master.xlsx, and runs the export.

Usage:
  python3 scripts/migrate_from_mindmap.py
"""
import json, os, re, sys
from copy import copy
from datetime import date
from openpyxl import load_workbook

HERE = os.path.dirname(os.path.abspath(__file__))
DASHBOARD = os.path.join(HERE, "..")
MINDMAP = os.path.join(DASHBOARD, "..", "features-mind-map-2026-05-04.html")
XLSX = os.path.join(DASHBOARD, "features-master.xlsx")

# Journey prefix map
PREFIX_FOR_JOURNEY = {
    "Onboarding": "ONB",
    "Saudi Trading": "SAU",
    "US Trading": "US",
    "Portfolio Monitoring": "PRT",
    "Wealth Visibility": "WLT",
    "Mutual Funds": "MF",
    "Robo Advisory": "RBO",
    "IPOs": "IPO",
    "Corporate Actions": "CA",
    "Investor Engagement": "ENG",
    "Cross-Journey": "XJ",
}

# Pseudo-category → reassignment rules
# Features in these categories get assigned a real journey + a tag
PSEUDO_CATEGORIES = {
    "Deep Discoveries (Figma)": {"tag": "deep-discovery"},
    "Sahm Gaps (New)": {"tag": "sahm-gap"},
    "ARC Differentiators": {"tag": "differentiator"},
}

# Best-guess journey assignment for pseudo-category features
# Based on feature content analysis from the mind map
PSEUDO_JOURNEY_MAP = {
    # Deep Discoveries (Figma)
    "Tutorials & Education": "Cross-Journey",
    "First Engagement": "Onboarding",
    "Fast Onboarding": "Onboarding",
    "Digital StoryTeller": "Portfolio Monitoring",
    "Ramadan Campaign": "Investor Engagement",
    "Discover & Search": "Cross-Journey",
    "Stock Stories": "Cross-Journey",
    "Fund Recommender": "Mutual Funds",
    "Saudi Options (Native)": "Saudi Trading",
    "Guest Mode (Extended)": "Cross-Journey",
    # Sahm Gaps (New)
    "Social Proof Nudge": "Investor Engagement",
    "1-Click Language Switch": "Cross-Journey",
    "Trading Incentive Banners": "Investor Engagement",
    "Cashback Prediction Game": "Investor Engagement",
    "Chart Touch-and-Hold": "Saudi Trading",
    "Thematic ETF Spotlight": "US Trading",
    "Expanded US Inventory": "US Trading",
    "Auto-Watchlist on Buy": "Saudi Trading",
    "Always-On Price View": "Saudi Trading",
    "Free Live Index Prices": "Cross-Journey",
    "Chart Axis to Market Close": "Saudi Trading",
    "Personalized Events Calendar": "Cross-Journey",
    "Standard S&D Layout": "Saudi Trading",
    "Advanced Trade Button": "Saudi Trading",
    "Tab-Based Navigation": "Cross-Journey",
    # ARC Differentiators
    "Murabaha Margin Lending": "Saudi Trading",
    "Purification Calculator": "Cross-Journey",
    "Zakat Calculator": "Cross-Journey",
    "Multi Shariah Lists": "Cross-Journey",
    "Minor Account + Guardian Controls": "Onboarding",
    "Mokafaa Loyalty → Invest": "Investor Engagement",
    "ARG Group Bundle Engine": "Investor Engagement",
    "Peer Portfolio Comparison": "Portfolio Monitoring",
    "Portfolio Health Score": "Portfolio Monitoring",
    "Storyteller Report": "Portfolio Monitoring",
    "SBL Program": "Saudi Trading",
    "Gift Campaigns": "Investor Engagement",
    "Tadawulaty SSO": "Saudi Trading",
    "ZATCA E-Invoices": "Cross-Journey",
}


def extract_f_call_body(text, start):
    """Starting after 'f(' at position start, return the full argument string
    up to the matching ')' — correctly skipping parentheses inside quotes."""
    i = start
    depth = 1
    in_quote = None
    buf = []
    while i < len(text) and depth > 0:
        c = text[i]
        if in_quote:
            buf.append(c)
            if c == '\\' and i + 1 < len(text):
                buf.append(text[i + 1])
                i += 2
                continue
            if c == in_quote:
                in_quote = None
        else:
            if c == '(':
                depth += 1
                buf.append(c)
            elif c == ')':
                depth -= 1
                if depth > 0:
                    buf.append(c)
            elif c in ('"', "'"):
                in_quote = c
                buf.append(c)
            else:
                buf.append(c)
        i += 1
    return "".join(buf), i


def parse_mindmap(html_path):
    """Extract features from the mind map HTML by parsing the f() calls."""
    with open(html_path, "r", encoding="utf-8") as fh:
        html = fh.read()

    m = re.search(r'const data = \{', html)
    if not m:
        print("ERROR: Could not find 'const data =' in mind map HTML")
        sys.exit(1)

    features = []
    current_category = None
    lines = html.split("\n")

    for line in lines:
        cat_m = re.search(r'\{name:"([^"]+)",color:"[^"]*",children:\[', line)
        if cat_m:
            current_category = cat_m.group(1)
            continue

        if current_category is None:
            continue

        # Find every 'f(' on this line using parentheses-aware extraction
        search_start = 0
        while True:
            idx = line.find('f(', search_start)
            if idx == -1:
                break
            # Make sure this is a standalone f( call, not part of another word
            if idx > 0 and (line[idx - 1].isalnum() or line[idx - 1] == '_'):
                search_start = idx + 2
                continue
            args_str, end_pos = extract_f_call_body(line, idx + 2)
            search_start = end_pos
            args = parse_f_args(args_str)
            if len(args) >= 2:
                feat = {
                    "category": current_category,
                    "name": args[0],
                    "status": args[1],
                    "definition": args[2] if len(args) > 2 else None,
                    "source": args[3] if len(args) > 3 else None,
                    "brd": args[4] if len(args) > 4 else None,
                    "competitors": args[5] if len(args) > 5 else None,
                    "priority": args[6] if len(args) > 6 else None,
                }
                features.append(feat)

    return features


def parse_f_args(s):
    """Parse the arguments of f(...) handling quoted strings and bare values."""
    args = []
    i = 0
    while i < len(s):
        c = s[i]
        if c in ('"', "'"):
            # Quoted string
            quote = c
            j = i + 1
            val = ""
            while j < len(s):
                if s[j] == '\\' and j + 1 < len(s):
                    val += s[j + 1]
                    j += 2
                elif s[j] == quote:
                    j += 1
                    break
                else:
                    val += s[j]
                    j += 1
            args.append(val)
            i = j
        elif c == ',':
            i += 1
        elif c in (' ', '\t', '\n'):
            i += 1
        else:
            # Bare value (number or null/undefined)
            j = i
            while j < len(s) and s[j] not in (',', ')'):
                j += 1
            val = s[i:j].strip()
            if val in ("null", "undefined", ""):
                args.append(None)
            else:
                try:
                    args.append(int(val))
                except ValueError:
                    try:
                        args.append(float(val))
                    except ValueError:
                        args.append(val)
            i = j
    return args


def assign_journey_and_tags(feat):
    """Assign real journey and tags for pseudo-category features."""
    cat = feat["category"]
    tags = []

    if cat in PSEUDO_CATEGORIES:
        tags.append(PSEUDO_CATEGORIES[cat]["tag"])
        journey = PSEUDO_JOURNEY_MAP.get(feat["name"], "Cross-Journey")
    elif cat in PREFIX_FOR_JOURNEY:
        journey = cat
    else:
        journey = "Cross-Journey"
        tags.append("uncategorized")

    return journey, tags


def generate_ids(features):
    """Generate stable IDs: PREFIX-NNN, sequential per journey."""
    counters = {}
    for feat in features:
        journey = feat["_journey"]
        prefix = PREFIX_FOR_JOURNEY.get(journey, "XJ")
        if prefix not in counters:
            counters[prefix] = 0
        counters[prefix] += 1
        feat["_id"] = f"{prefix}-{counters[prefix]:03d}"


def populate_xlsx(features, xlsx_path):
    """Write features into the existing xlsx template."""
    wb = load_workbook(xlsx_path)
    ws = wb["Features"]

    for i, feat in enumerate(features):
        row = i + 4  # data starts at row 4

        ws.cell(row=row, column=1, value=feat["_id"])
        ws.cell(row=row, column=2, value=feat["name"])
        ws.cell(row=row, column=3, value=feat["_journey"])
        ws.cell(row=row, column=4, value=feat["status"])

        if feat.get("definition"):
            ws.cell(row=row, column=5, value=feat["definition"])
        if feat.get("brd"):
            ws.cell(row=row, column=6, value=feat["brd"])
        if feat.get("competitors"):
            ws.cell(row=row, column=7, value=feat["competitors"])
        if feat.get("priority") is not None:
            ws.cell(row=row, column=8, value=int(feat["priority"]))
        if feat.get("_tags"):
            ws.cell(row=row, column=9, value=", ".join(feat["_tags"]))
        # source → derive from brd + figma; set figma_link for Figma sources
        source = feat.get("source")
        if source and "Figma" in source:
            ws.cell(row=row, column=10, value="(Figma link pending)")
        # figma_status: leave blank
        # live_date, went_live, owner_pm, owner_squad: leave blank

    # Populate BRDs sheet with all referenced BRD codes
    brd_codes = set()
    for feat in features:
        if feat.get("brd"):
            for code in [c.strip() for c in feat["brd"].split(",") if c.strip()]:
                brd_codes.add(code)

    if "BRDs" in wb.sheetnames:
        ws_brd = wb["BRDs"]
        for i, code in enumerate(sorted(brd_codes)):
            row = i + 4
            ws_brd.cell(row=row, column=1, value=code)
            ws_brd.cell(row=row, column=4, value="Draft")

    wb.save(xlsx_path)
    wb.close()
    return len(brd_codes)


def main():
    print("=" * 60)
    print("  MIGRATION: Mind Map → Dashboard")
    print("=" * 60)

    # Verify files exist
    if not os.path.exists(MINDMAP):
        print(f"ERROR: Mind map not found at {MINDMAP}")
        sys.exit(1)
    if not os.path.exists(XLSX):
        print(f"ERROR: Template xlsx not found at {XLSX}")
        print("Run: python3 scripts/build_template.py first")
        sys.exit(1)

    # Step 1: Parse
    print("\n  [1/5] Parsing mind map HTML...")
    raw_features = parse_mindmap(MINDMAP)
    print(f"        Extracted {len(raw_features)} features from {len(set(f['category'] for f in raw_features))} categories")

    # Category breakdown
    cats = {}
    for f in raw_features:
        cats[f["category"]] = cats.get(f["category"], 0) + 1
    for cat, count in sorted(cats.items(), key=lambda x: -x[1]):
        marker = " (pseudo)" if cat in PSEUDO_CATEGORIES else ""
        print(f"          {cat}: {count}{marker}")

    # Step 2: Assign journeys and tags
    print("\n  [2/6] Assigning journeys and tags...")
    reassigned = 0
    for feat in raw_features:
        journey, tags = assign_journey_and_tags(feat)
        feat["_journey"] = journey
        feat["_tags"] = tags
        if feat["category"] in PSEUDO_CATEGORIES:
            reassigned += 1
    print(f"        Reassigned {reassigned} features from pseudo-categories to real journeys")

    # Step 3: Deduplicate — merge pseudo-category duplicates into real-journey rows
    print("\n  [3/6] Deduplicating...")
    # Index real-journey features by name
    real_by_name = {}
    for feat in raw_features:
        if feat["category"] not in PSEUDO_CATEGORIES:
            real_by_name[feat["name"]] = feat

    deduped = []
    merged_count = 0
    for feat in raw_features:
        if feat["category"] in PSEUDO_CATEGORIES and feat["name"] in real_by_name:
            # Merge: add the pseudo tag to the real-journey feature
            target = real_by_name[feat["name"]]
            for tag in feat["_tags"]:
                if tag not in target["_tags"]:
                    target["_tags"].append(tag)
            # Carry over priority if the real row lacks one
            if feat.get("priority") is not None and target.get("priority") is None:
                target["priority"] = feat["priority"]
            # Carry over competitors if the real row lacks them
            if feat.get("competitors") and not target.get("competitors"):
                target["competitors"] = feat["competitors"]
            merged_count += 1
        else:
            deduped.append(feat)

    raw_features = deduped
    print(f"        Merged {merged_count} pseudo-category duplicates into existing real-journey rows")

    # Also deduplicate identical names across real journeys (genuine source dupes)
    seen_names = set()
    deduped2 = []
    cross_dupes = 0
    for feat in raw_features:
        key = feat["name"]
        if key in seen_names:
            cross_dupes += 1
            print(f"          Dropped cross-journey duplicate: \"{key}\" (category: {feat['category']})")
        else:
            seen_names.add(key)
            deduped2.append(feat)
    raw_features = deduped2
    if cross_dupes:
        print(f"        Dropped {cross_dupes} cross-journey duplicate(s)")
    print(f"        Features after dedup: {len(raw_features)}")

    # Step 4: Generate IDs
    print("\n  [4/6] Generating stable IDs...")
    generate_ids(raw_features)
    print(f"        Generated {len(raw_features)} IDs across {len(PREFIX_FOR_JOURNEY)} prefixes")

    # Status breakdown
    by_status = {}
    for f in raw_features:
        by_status[f["status"]] = by_status.get(f["status"], 0) + 1
    for s in ["Live", "Planned", "Gap", "Diff"]:
        print(f"          {s}: {by_status.get(s, 0)}")

    # Journey breakdown
    by_journey = {}
    for f in raw_features:
        by_journey[f["_journey"]] = by_journey.get(f["_journey"], 0) + 1
    print(f"\n        Journey distribution (after reassignment):")
    for j in sorted(by_journey.keys()):
        print(f"          {j}: {by_journey[j]}")

    # Step 4: Populate xlsx
    print("\n  [5/6] Populating features-master.xlsx...")
    brd_count = populate_xlsx(raw_features, XLSX)
    print(f"        Wrote {len(raw_features)} features to Features sheet")
    print(f"        Wrote {brd_count} BRD codes to BRDs sheet")

    # Step 5: Run export
    print("\n  [6/6] Running xlsx-to-features-json.py...")
    export_script = os.path.join(HERE, "xlsx-to-features-json.py")
    exit_code = os.system(f"python3 \"{export_script}\" --input \"{XLSX}\" --out-dir \"{os.path.join(DASHBOARD, 'data')}\"")

    print("\n" + "=" * 60)
    if exit_code == 0:
        print("  MIGRATION COMPLETE")
    else:
        print("  MIGRATION COMPLETE (export had errors — see above)")
    print("=" * 60)

    # Spot-check
    data_dir = os.path.join(DASHBOARD, "data")
    fj = os.path.join(data_dir, "features.json")
    if os.path.exists(fj):
        import json
        with open(fj) as fh:
            d = json.load(fh)
        exported = len(d.get("features", []))
        print(f"\n  Spot-check: features.json contains {exported} features")
        if exported == len(raw_features):
            print("  ✓ Count matches parsed features")
        else:
            print(f"  ✗ Mismatch: parsed {len(raw_features)}, exported {exported}")
    else:
        print(f"\n  WARNING: {fj} not found")

    # Write migration report data for the report generator
    report = {
        "date": date.today().strftime("%Y-%m-%d"),
        "parsed": len(raw_features),
        "categories": dict(sorted(cats.items(), key=lambda x: -x[1])),
        "reassigned": reassigned,
        "by_status": by_status,
        "by_journey": dict(sorted(by_journey.items())),
        "brd_codes": brd_count,
        "pseudo_mappings": {k: v for k, v in PSEUDO_JOURNEY_MAP.items()},
    }
    report_path = os.path.join(DASHBOARD, "migration-data.json")
    with open(report_path, "w") as fh:
        json.dump(report, fh, indent=2)
    print(f"\n  Migration data saved to: {report_path}")


if __name__ == "__main__":
    main()
