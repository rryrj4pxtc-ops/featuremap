#!/usr/bin/env python3
"""
xlsx-to-features-json.py
Reads features-master.xlsx and writes:
  data/features.json
  data/brds.json
  data/benchmarks.json

Usage:
  python3 scripts/xlsx-to-features-json.py [--input FILE] [--out-dir DIR]
"""
import argparse, json, os, sys
from datetime import date, datetime
from openpyxl import load_workbook

JOURNEYS = {
    "Onboarding", "Saudi Market", "US Trading",
    "Mutual Funds", "Crowd Fund", "Robo Advisory",
    "LMS/SBL", "IPOs", "Cash Management",
    # Cross-Journey decomposed 2026-08-02 -> Platform (cross-cutting layer) +
    # Investor Engagement (new journey); money features reassigned to Cash Management.
    "Platform",
}
# Diff was retired 2026-08-26 (baseline v2.3.4). Typing it is now a hard error:
# a status must assert Live, Planned or Gap. "Not yet walked" is expressed by the
# absence of evidence, which derives Unverified, not by a fourth label.
STATUSES = {"Live", "Planned", "Gap"}
# US Trading runs on two brokerage backends. A feature may be Live/Planned on one
# and a gap on the other. The `backends` column encodes this as "IBKR=Live;GTN=Gap".
# When set, the row's own `status` must equal the more-advanced backend's status.
BACKENDS = {"IBKR", "GTN"}
STATUS_RANK = {"Live": 3, "Planned": 2, "Gap": 1}


def parse_backends(val, row_label, journey, status, warnings):
    """Parse "IBKR=Live;GTN=Gap" into {"IBKR": "Live", "GTN": "Gap"}. Validates
    backend names/statuses, that it's a US Trading row, and that the row `status`
    matches the most-advanced backend."""
    if not val:
        return None
    out = {}
    for part in str(val).split(";"):
        part = part.strip()
        if not part:
            continue
        if "=" not in part:
            warnings.append(f"{row_label}: malformed backends entry '{part}' (want BACKEND=Status)")
            continue
        b, st = (x.strip() for x in part.split("=", 1))
        if b not in BACKENDS:
            warnings.append(f"{row_label}: unknown backend '{b}' (allowed: {', '.join(sorted(BACKENDS))})")
            continue
        if st not in STATUSES:
            warnings.append(f"{row_label}: invalid backend status '{st}' for {b}")
            continue
        out[b] = st
    if not out:
        return None
    if journey != "US Trading":
        warnings.append(f"{row_label}: backends set on non-US-Trading journey '{journey}'")
    best = max(out.values(), key=lambda s: STATUS_RANK.get(s, 0))
    if status and STATUS_RANK.get(status, 0) != STATUS_RANK.get(best, 0):
        warnings.append(f"{row_label}: status '{status}' != most-advanced backend '{best}' ({out})")
    return out
FIGMA_STATUSES = {"Designed", "In Review", "Approved", "As-Built"}
FIGMA_FILES = {
    "CDO", "Portfolios", "OnBoarding (KYC)", "Market", "Discover & Search",
    "Home", "Profile & Setting", "LMS", "Wealth Mgmt Dashboard", "Watchlist",
    "Bain", "Tradepad", "Orders", "Themes", "Trader Mode",
}
BRD_STATUSES = {"Draft", "In Review", "Approved", "Deprecated"}

JOURNEY_PREFIX = {
    "ONB": "Onboarding",
    "SAU": "Saudi Market",
    "US":  "US Trading",
    "MF":  "Mutual Funds",
    "CF":  "Crowd Fund",
    "RBO": "Robo Advisory",
    "LMS": "LMS/SBL",
    "IPO": "IPOs",
    "CM":  "Cash Management",
    "PLT": "Platform",             # new-Platform features going forward
}
# NOTE: "XJ" (legacy Cross-Journey) intentionally NOT in the prefix map. The 68
# former Cross-Journey features keep their stable XJ-/SAU- ids after the 2026-08-02
# decomposition, so their prefix no longer implies their journey; leaving XJ out
# suppresses spurious prefix-mismatch warnings for reassigned features.
PREFIX_FOR_JOURNEY = {v: k for k, v in JOURNEY_PREFIX.items()}


def split_csv(val, respect_parens=False):
    if not val:
        return []
    s = str(val)
    if not respect_parens:
        return [t.strip() for t in s.split(",") if t.strip()]
    # Split on commas that are NOT inside parentheses
    parts, current, depth = [], [], 0
    for ch in s:
        if ch == '(':
            depth += 1
        elif ch == ')':
            depth = max(0, depth - 1)
        if ch == ',' and depth == 0:
            parts.append(''.join(current).strip())
            current = []
        else:
            current.append(ch)
    parts.append(''.join(current).strip())
    return [p for p in parts if p]


# ── Competitor name normalization ──
COMPETITOR_MERGES = {
    "Alinma Tadawul": "Alinma",
    "AlJazira": "AlJazira Capital",
    "Moomoo AI": "Moomoo",
}

COMPETITOR_PLACEHOLDERS = {
    "US competitors", "Saudi competitors", "Competitors",
    "US local competitors", "Competitors with US access",
}

import re
_PAREN_RE = re.compile(r'^(.+?)\s*\((.+)\)$')

def clean_competitors(raw_list):
    """Return (cleaned_names, notes_list, placeholder_list)."""
    names, notes, placeholders = [], [], []
    for raw in raw_list:
        # Check placeholder first
        if raw in COMPETITOR_PLACEHOLDERS:
            placeholders.append(raw)
            continue
        # Strip parenthetical detail
        m = _PAREN_RE.match(raw)
        if m:
            base, note = m.group(1).strip(), m.group(2).strip()
            notes.append(note)
        else:
            base = raw
        # Apply merges
        base = COMPETITOR_MERGES.get(base, base)
        if base not in names:
            names.append(base)
    return names, notes, placeholders


def normalize_date(val):
    if val is None:
        return None
    if isinstance(val, datetime):
        return val.strftime("%Y-%m-%d")
    if isinstance(val, date):
        return val.strftime("%Y-%m-%d")
    s = str(val).strip()
    if not s:
        return None
    for fmt in ("%Y-%m-%d", "%d %b %Y", "%d %B %Y", "%d/%m/%Y", "%m/%d/%Y"):
        try:
            return datetime.strptime(s, fmt).strftime("%Y-%m-%d")
        except ValueError:
            continue
    return s  # return raw if unparseable


def derive_source(brd_list, figma_link):
    has_brd = len(brd_list) > 0
    has_figma = bool(figma_link)
    if has_brd and has_figma:
        return "BRD + Figma"
    if has_brd:
        return "BRD"
    if has_figma:
        return "Figma"
    return None


def main():
    parser = argparse.ArgumentParser(description="Export features-master.xlsx to JSON")
    parser.add_argument("--input", default=None, help="Path to xlsx (default: features-master.xlsx)")
    parser.add_argument("--out-dir", default=None, help="Output directory (default: data)")
    args = parser.parse_args()

    here = os.path.dirname(os.path.abspath(__file__))
    dashboard_dir = os.path.join(here, "..")

    input_path = args.input or os.path.join(dashboard_dir, "features-master.xlsx")
    out_dir = args.out_dir or os.path.join(dashboard_dir, "data")
    os.makedirs(out_dir, exist_ok=True)

    if not os.path.exists(input_path):
        print(f"ERROR: {input_path} not found")
        sys.exit(1)

    wb = load_workbook(input_path, read_only=True, data_only=True)

    errors = []
    warnings = []

    # ── Read Benchmarks ──
    benchmarks = []
    canonical_competitors = set()
    if "Benchmarks" in wb.sheetnames:
        ws = wb["Benchmarks"]
        for row in ws.iter_rows(min_row=5, values_only=True):
            name = row[0]
            if not name:
                continue
            canonical_competitors.add(str(name).strip())
            entry = {"name": str(name).strip()}
            if row[1]:
                entry["region"] = str(row[1]).strip()
            if row[2]:
                entry["type"] = str(row[2]).strip()
            if row[3] is not None:
                entry["primary"] = bool(row[3])
            benchmarks.append(entry)

    # ── Read BRDs ──
    brds = []
    brd_codes_registered = set()
    if "BRDs" in wb.sheetnames:
        ws = wb["BRDs"]
        for row in ws.iter_rows(min_row=4, values_only=True):
            code = row[0]
            if not code:
                continue
            code = str(code).strip()
            brd_codes_registered.add(code)
            entry = {"brd_code": code}
            if row[1]:
                entry["title"] = str(row[1]).strip()
            if row[2]:
                entry["owner"] = str(row[2]).strip()
            if row[3]:
                entry["status"] = str(row[3]).strip()
            d = normalize_date(row[4])
            if d:
                entry["approved_date"] = d
            if row[5]:
                entry["link"] = str(row[5]).strip()
            brds.append(entry)

    # ── Read Features ──
    features = []
    seen_ids = set()
    brd_codes_referenced = set()
    stats = {"total": 0, "by_status": {}, "by_journey": {}, "missing_figma": 0, "undated_planned": 0, "slipped": 0, "has_figma_file": 0, "has_area_screen": 0}
    today = date.today()

    if "Features" not in wb.sheetnames:
        print("ERROR: No 'Features' sheet found")
        sys.exit(1)

    ws = wb["Features"]
    for row in ws.iter_rows(min_row=4, values_only=True):
        # skip completely blank rows
        if not any(row[:4]):
            continue

        fid = str(row[0]).strip() if row[0] else None
        name = str(row[1]).strip() if row[1] else None
        journey = str(row[2]).strip() if row[2] else None
        status = str(row[3]).strip() if row[3] else None

        row_label = fid or name or f"row {stats['total'] + 4}"

        # Required field checks
        if not fid:
            errors.append(f"{row_label}: missing id")
        if not name:
            errors.append(f"{row_label}: missing name")
        if not journey:
            errors.append(f"{row_label}: missing journey")
        elif journey not in JOURNEYS:
            errors.append(f"{row_label}: invalid journey '{journey}'")
        if not status:
            errors.append(f"{row_label}: missing status")
        elif status not in STATUSES:
            errors.append(f"{row_label}: invalid status '{status}'")

        if fid:
            if fid in seen_ids:
                errors.append(f"{row_label}: duplicate id")
            seen_ids.add(fid)

            # Prefix check (warn only). Features reassigned in the 2026-08-02
            # Cross-Journey decomposition keep their stable ids, so exempt them.
            PREFIX_CHECK_EXEMPT = {"SAU-006", "SAU-016"}  # moved to Platform, keep SAU- id
            prefix = fid.split("-")[0] if "-" in fid else fid
            expected_journey = JOURNEY_PREFIX.get(prefix)
            if expected_journey and journey and expected_journey != journey and fid not in PREFIX_CHECK_EXEMPT:
                warnings.append(f"{fid}: prefix {prefix} suggests '{expected_journey}' but journey is '{journey}'")

        # Parse fields
        definition = str(row[4]).strip() if row[4] else None
        brd_list = split_csv(row[5])
        raw_competitors = split_csv(row[6], respect_parens=True)
        competitors, competitor_notes, competitor_placeholders = clean_competitors(raw_competitors)
        priority = None
        if row[7] is not None:
            try:
                priority = int(row[7])
            except (ValueError, TypeError):
                warnings.append(f"{row_label}: non-integer priority '{row[7]}'")
        tags = split_csv(row[8])
        area = str(row[9]).strip() if len(row) > 9 and row[9] else None
        screen = str(row[10]).strip() if len(row) > 10 and row[10] else None
        # display_order (col AB): the contract sequence for a screen, depth-first.
        # The renderer sorts on it, so ordering lives in the data, not in view code.
        try:
            display_order = int(row[27]) if len(row) > 27 and row[27] is not None else None
        except (TypeError, ValueError):
            display_order = None
        # is_container (col AC): the row exists only to group children. Its status is
        # DERIVED from its children by derive_status.py, and it is excluded from every
        # KPI and maturity count — containers are scaffolding, not delivered features.
        is_container = bool(row[28]) if len(row) > 28 else False
        # row_type (col AG): 'detail' marks a field/period leaf. Rendered in the tree but
        # EXCLUDED from feature counts, maturity KPIs and gap metrics — it is a data field
        # promoted to a row for navigation, not a feature ARC can ship or fail to ship.
        row_type = str(row[31]).strip() if len(row) > 31 and row[31] else None
        figma_link = str(row[11]).strip() if len(row) > 11 and row[11] else None
        figma_status = str(row[12]).strip() if len(row) > 12 and row[12] else None
        figma_file = str(row[13]).strip() if len(row) > 13 and row[13] else None
        live_date = normalize_date(row[14]) if len(row) > 14 else None
        went_live = normalize_date(row[15]) if len(row) > 15 else None
        owner_pm = str(row[16]).strip() if len(row) > 16 and row[16] else None
        owner_squad = str(row[17]).strip() if len(row) > 17 and row[17] else None
        impact = None
        if len(row) > 18 and row[18] is not None:
            try:
                impact = int(row[18])
                if impact < 1 or impact > 5:
                    warnings.append(f"{row_label}: impact {impact} out of range 1-5")
                    impact = None
            except (ValueError, TypeError):
                warnings.append(f"{row_label}: non-integer impact '{row[18]}'")
        backends = parse_backends(row[19] if len(row) > 19 else None,
                                  row_label, journey, status, warnings)

        # Validate area
        # Functional area model (SCHEMA.md § "Functional area model"). Saudi Market
        # is the converted reference journey; other journeys migrate over time.
        VALID_AREAS_FUNCTIONAL = {"Discover", "Transact", "Manage", "Track", "Learn", "Onboard"}
        VALID_AREAS_MPO = {"Market", "Stock Page", "Watchlist", "Portfolio", "Orders", "Market Data"}
        VALID_AREAS_SAUDI = VALID_AREAS_MPO
        VALID_AREAS_ONB = {"ARB", "Local", "Global", "Corporate", "Minor", "All account types", "Saudi"}
        # Platform (former Cross-Journey) uses cluster areas, not the functional set,
        # because its features are cross-cutting infrastructure, not investing intents.
        VALID_AREAS_PLATFORM = {"Settings", "Market Data", "Compliance", "Support",
                                "Auth", "Content", "Notifications", "Calculator",
                                "Services", "Family", "Education", "Alert and Notification",
                                "Subscription", "Customization", "App Widgets", "Investment",
                                "Engagement", "Charity"}
        if area and journey == "Saudi Market" and area not in VALID_AREAS_SAUDI:
            warnings.append(f"{row_label}: unknown area '{area}' for Saudi Market")
        if area and journey == "Onboarding" and area not in VALID_AREAS_ONB:
            warnings.append(f"{row_label}: unknown area '{area}' for Onboarding")
        if area and journey == "Platform" and area not in VALID_AREAS_PLATFORM:
            warnings.append(f"{row_label}: unknown area '{area}' for Platform")
        if area and journey == "Investor Engagement" and area not in VALID_AREAS_FUNCTIONAL:
            warnings.append(f"{row_label}: unknown area '{area}' for Investor Engagement")
        if journey == "Saudi Market" and status != "Gap" and not screen and area:
            warnings.append(f"{row_label}: area set but screen is empty")
        if journey == "Saudi Market" and status != "Gap" and not area and not screen:
            warnings.append(f"{row_label}: Saudi Market feature missing area/screen")
        if journey == "Onboarding" and not area:
            warnings.append(f"{row_label}: Onboarding feature missing area (ARB/Non-ARB/Minor)")

        # Validate figma_status
        if figma_status and figma_status not in FIGMA_STATUSES:
            warnings.append(f"{row_label}: invalid figma_status '{figma_status}'")

        # Validate figma_file
        if figma_file and figma_file not in FIGMA_FILES:
            warnings.append(f"{row_label}: unknown figma_file '{figma_file}'")

        # Track BRD references
        for code in brd_list:
            brd_codes_referenced.add(code)

        # Validate competitors against canonical list (error, not warning)
        for comp in competitors:
            if comp not in canonical_competitors:
                errors.append(f"{row_label}: competitor '{comp}' not in Benchmarks sheet")

        # Flag placeholder competitors
        for ph in competitor_placeholders:
            warnings.append(f"{row_label}: placeholder competitor '{ph}' — replace with real names")

        # Derive source
        source = derive_source(brd_list, figma_link)

        # Build feature dict — drop empty optional fields
        feat = {"id": fid, "name": name, "journey": journey, "status": status}
        if definition:
            feat["definition"] = definition
        if brd_list:
            feat["brd"] = brd_list
        if competitors:
            feat["competitors"] = competitors
        if competitor_notes:
            feat["competitor_notes"] = competitor_notes
        if priority is not None:
            feat["priority"] = priority
        if tags:
            feat["tags"] = tags
        if area:
            feat["area"] = area
        if screen:
            feat["screen"] = screen
        if display_order is not None:
            feat["display_order"] = display_order
        if is_container:
            feat["is_container"] = True
        if row_type:
            feat["row_type"] = row_type
        if figma_link:
            feat["figma_link"] = figma_link
        if figma_status:
            feat["figma_status"] = figma_status
        if figma_file:
            feat["figma_file"] = figma_file
        if live_date:
            feat["live_date"] = live_date
        if went_live:
            feat["went_live"] = went_live
        if owner_pm:
            feat["owner_pm"] = owner_pm
        if owner_squad:
            feat["owner_squad"] = owner_squad
        if impact is not None:
            feat["impact"] = impact
        if backends:
            feat["backends"] = backends
        if source:
            feat["source"] = source

        features.append(feat)

        # Stats
        stats["total"] += 1
        stats["by_status"][status] = stats["by_status"].get(status, 0) + 1
        if journey:
            stats["by_journey"][journey] = stats["by_journey"].get(journey, 0) + 1
        if figma_file:
            stats["has_figma_file"] += 1
        if area and screen:
            stats["has_area_screen"] += 1
        if status in ("Live", "Planned") and not figma_link:
            stats["missing_figma"] += 1
        if status == "Planned" and not live_date:
            stats["undated_planned"] += 1
        if status == "Planned" and live_date:
            try:
                ld = datetime.strptime(live_date, "%Y-%m-%d").date()
                if ld < today:
                    stats["slipped"] += 1
            except ValueError:
                pass

    wb.close()

    # BRDs referenced but not documented
    undocumented_brds = brd_codes_referenced - brd_codes_registered

    # ── Write JSON ──
    meta = {
        "schema_version": "1.5",
        "last_updated": today.strftime("%Y-%m-%d"),
        "generated_by": "xlsx-to-features-json.py",
    }

    features_out = {"_meta": meta, "features": features}
    brds_out = {"_meta": meta, "brds": brds}
    benchmarks_out = {"_meta": meta, "benchmarks": benchmarks}

    for fname, data in [
        ("features.json", features_out),
        ("brds.json", brds_out),
        ("benchmarks.json", benchmarks_out),
    ]:
        path = os.path.join(out_dir, fname)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    # ── Print summary ──
    print("=" * 60)
    print("  FEATURES EXPORT SUMMARY")
    print("=" * 60)
    print(f"  Total features:     {stats['total']}")
    print(f"  By status:")
    for s in ["Live", "Planned", "Gap"]:
        print(f"    {s:10s}  {stats['by_status'].get(s, 0)}")
    print(f"  By journey:")
    for j in sorted(stats["by_journey"].keys()):
        print(f"    {j:25s}  {stats['by_journey'][j]}")
    print(f"  Figma file set:     {stats['has_figma_file']}")
    print(f"  Area+Screen set:    {stats['has_area_screen']}")
    print(f"  Missing Figma link: {stats['missing_figma']}")
    print(f"  Undated Planned:    {stats['undated_planned']}")
    print(f"  Slipped:            {stats['slipped']}")
    print(f"  BRDs referenced:    {len(brd_codes_referenced)}")
    print(f"  BRDs documented:    {len(brd_codes_registered)}")
    if undocumented_brds:
        print(f"  BRDs undocumented:  {len(undocumented_brds)}")

    # Errors
    print(f"\n  Errors:   {len(errors)}")
    if errors:
        for e in errors[:20]:
            print(f"    ERROR: {e}")
        if len(errors) > 20:
            print(f"    ... and {len(errors) - 20} more")

    # Warnings
    print(f"  Warnings: {len(warnings)}")
    if warnings:
        for w in warnings[:20]:
            print(f"    WARN:  {w}")
        if len(warnings) > 20:
            print(f"    ... and {len(warnings) - 20} more")

    print(f"\n  Output:")
    print(f"    {os.path.join(out_dir, 'features.json')}")
    print(f"    {os.path.join(out_dir, 'brds.json')}")
    print(f"    {os.path.join(out_dir, 'benchmarks.json')}")
    print("=" * 60)

    if errors:
        print(f"\nFAILED — {len(errors)} hard error(s). Fix the xlsx and re-run.")
        sys.exit(1)
    else:
        print("\nSUCCESS")


if __name__ == "__main__":
    main()
