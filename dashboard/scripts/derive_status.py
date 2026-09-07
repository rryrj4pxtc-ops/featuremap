#!/usr/bin/env python3
"""
derive_status.py
Compute derived_status for every feature from evidence files.
Reads:  features-master.xlsx  (via features.json)
        data/coverage.json    (competitor coverage cells)
        data/verified_live.json (ARC App Store evidence)
Writes: data/features_derived.json

Does NOT modify the xlsx or features.json.
"""
import json, re, sys
from collections import defaultdict
from datetime import date, datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent.parent  # → ARC/
FEATURES_JSON = Path(__file__).resolve().parent.parent / "data" / "features.json"
BENCHMARKS_JSON = Path(__file__).resolve().parent.parent / "data" / "benchmarks.json"
COVERAGE_JSON = BASE_DIR / "data" / "coverage.json"
VERIFIED_LIVE_JSON = BASE_DIR / "data" / "verified_live.json"
MANUAL_STATUS_JSON = BASE_DIR / "data" / "manual_status.json"
OUTPUT_JSON = BASE_DIR / "data" / "features_derived.json"
MASTER_XLSX = Path(__file__).resolve().parent.parent / "features-master.xlsx"
BASELINE_MD = Path(__file__).resolve().parent.parent / "ARC-STRUCTURE-BASELINE.md"


def _workbook_md5():
    """md5 of the workbook this generation read. The dashboard compares it against the
    live master to detect a regenerate that never happened."""
    import hashlib
    try:
        return hashlib.md5(MASTER_XLSX.read_bytes()).hexdigest()
    except Exception:
        return None


def _baseline_version():
    """Parse the '**Version:** vX.Y.Z' line out of the baseline document."""
    try:
        m = re.search(r"\*\*Version:\*\*\s*(v[\d.]+)", BASELINE_MD.read_text())
        return m.group(1) if m else None
    except Exception:
        return None

TODAY = date.today()
STALE_DAYS = 90

# ── Area normalization (Saudi Market) ────────────────────────────────────────
# Collapse maturity-encoding area labels onto their canonical place-name.
# Keys are matched case-insensitively (after strip); values are the canonical
# Title-Case area. Idempotent: canonical names map to themselves. Documented in
# SCHEMA.md § "Area normalization". Portfolio Analytics and Market Data are
# deliberately NOT merged — they stay distinct areas.
# Functional area model (see SCHEMA.md § "Functional area model"). Saudi Market
# is the converted reference journey. Learn/Onboard are valid areas that Saudi
# happens not to populate.
CANONICAL_SAUDI_AREAS = {
    "Discover", "Transact", "Manage", "Track", "Learn", "Onboard",
}

# Normalization retired at the functional-area conversion (2026-08-02): its old
# targets were product-native area names that no longer exist. Kept empty so the
# fail-fast assertion below still guards any future additions.
AREA_NORMALIZATION = {}

# Every normalization target must be an existing canonical area (fail fast if a
# future edit introduces a target that isn't a real place).
_bad_targets = set(AREA_NORMALIZATION.values()) - CANONICAL_SAUDI_AREAS
assert not _bad_targets, f"AREA_NORMALIZATION targets not in canonical areas: {_bad_targets}"


def normalize_area(area, journey):
    """Return the canonical Title-Case area for Saudi Market features.
    Non-Saudi journeys and blank areas are returned unchanged."""
    if journey != "Saudi Market" or not area:
        return area
    mapped = AREA_NORMALIZATION.get(area.strip().lower())
    return mapped if mapped else area.title()


# ── Load inputs ──────────────────────────────────────────────────────────────

def load_json(path):
    if not path.exists():
        return {}
    return json.loads(path.read_text())


def load_features():
    data = load_json(FEATURES_JSON)
    return data.get("features", [])


def load_benchmarks():
    data = load_json(BENCHMARKS_JSON)
    return [b["name"] for b in data.get("benchmarks", [])]


def load_coverage():
    """Return coverage dict keyed by feature_id::competitor."""
    return load_json(COVERAGE_JSON)


def load_verified_live():
    """Return dict keyed by feature ID."""
    return load_json(VERIFIED_LIVE_JSON)


def load_manual_status():
    """Ahmed's authoritative status determinations (Gap/Planned/Live) keyed by
    feature ID — the evidence store for hand-reviewed features with no competitor
    or BRD signal. Same role for Gap/Planned as verified_live.json plays for Live."""
    return load_json(MANUAL_STATUS_JSON)


# ── Evidence helpers ─────────────────────────────────────────────────────────

def verified_live_age(entry):
    """Return age in days of a verified_live entry, or None if no date."""
    vd = entry.get("verified_date", "")
    if not vd:
        return None
    try:
        d = datetime.strptime(vd[:10], "%Y-%m-%d").date()
        return (TODAY - d).days
    except Exception:
        return None


def _non_mismatched_cells(feature_id, coverage):
    """Return coverage cells that are supports=yes and not journey-mismatched,
    split into (high, low) lists."""
    high, low = [], []
    for cell in coverage.values():
        if cell.get("feature_id") != feature_id:
            continue
        if cell.get("supports") != "yes":
            continue
        if cell.get("journey_mismatch"):
            continue
        if cell.get("confidence") == "high":
            high.append(cell)
        else:
            low.append(cell)
    return high, low


def all_cells_for_feature(feature_id, coverage):
    """Return ALL coverage cells for this feature (any confidence)."""
    return [c for c in coverage.values() if c.get("feature_id") == feature_id]


def pressure_score(feature_id, coverage, benchmark_names):
    """Share of the 13 benchmark competitors with a non-mismatched yes cell (1–5).
    High-confidence cells count as 1.0, low as 0.5."""
    high_cells, low_cells = _non_mismatched_cells(feature_id, coverage)
    high_comps = {c["competitor"] for c in high_cells if c["competitor"] in benchmark_names}
    low_comps = {c["competitor"] for c in low_cells if c["competitor"] in benchmark_names}
    low_only = low_comps - high_comps  # don't double-count
    n = len(benchmark_names)
    if n == 0:
        return 0
    weighted = len(high_comps) + len(low_only) * 0.5
    if weighted == 0:
        return 0
    ratio = weighted / n
    if ratio <= 0.1:
        return 1
    if ratio <= 0.25:
        return 2
    if ratio <= 0.5:
        return 3
    if ratio <= 0.75:
        return 4
    return 5


# ── Cross-market parity gaps ─────────────────────────────────────────────────
# Saudi Market and US Trading are reconciled to mirror each other (parity work,
# 2026-08-11). When one market SHIPS a feature (substantiated) and the sibling
# market lacks it, that sibling row is a real *internal* gap — not "Unverified".
# derive() otherwise can't tell, because a Saudi/US twin isn't a competitor.
MARKET_JOURNEYS = {"Saudi Market", "US Trading"}
_PAREN = re.compile(r"\([^)]*\)")


def base_name(name):
    """Normalized base name for cross-market twin matching: drop parenthetical
    qualifiers like (US)/(Saudi)/(OCO), collapse whitespace, lowercase. Keeps
    'Watchlist — Edit' distinct from 'Watchlist' (no split on the em dash)."""
    return re.sub(r"\s+", " ", _PAREN.sub("", name or "")).strip().lower()


def _substantiated(f, coverage, verified_live):
    """A market feature the org actually ships or is building: App-Store verified,
    hand-typed Live, has a BRD/Figma, or has competitor coverage evidence."""
    if verified_live.get(f["id"]):
        return True
    if f.get("status") == "Live":
        return True
    if f.get("brd") or f.get("figma_link"):
        return True
    return any(c.get("feature_id") == f["id"] and c.get("supports") == "yes"
               and not c.get("journey_mismatch") for c in coverage.values())


def compute_parity_gaps(features, coverage, verified_live):
    """IDs of market features whose same-base-name twin in the SIBLING market is
    substantiated — i.e. confirmed internal (non-competitor) parity gaps."""
    idx = defaultdict(lambda: defaultdict(list))
    for f in features:
        if f.get("journey") in MARKET_JOURNEYS:
            idx[base_name(f.get("name"))][f["journey"]].append(f)
    parity = set()
    for f in features:
        j = f.get("journey")
        if j not in MARKET_JOURNEYS:
            continue
        other = (MARKET_JOURNEYS - {j}).pop()
        twins = idx[base_name(f.get("name"))].get(other, [])
        if any(_substantiated(t, coverage, verified_live) for t in twins):
            parity.add(f["id"])
    return parity


# ── Derive status ────────────────────────────────────────────────────────────

# Populated by main() before deriving: container id -> derived status from its children.
_CONTAINER_STATUS = {}


def _container_status(fid):
    return _CONTAINER_STATUS.get(fid, "Planned")


def build_container_status(features):
    """Roll a container's status up from its children — three states, best-first.

        any child Live      -> Live
        else any Planned    -> Planned
        else all Gap        -> Gap
        no children         -> Planned

    The Gap outcome exists because the original two-state rule (Live / else
    Planned) reported a container with nothing but Gap children as *Planned*,
    which reads as "being built" when the truth is "we have none of it".
    Caught on US-150 / US-246 Portfolio Analysis, v2.2.2.

    Children are found by the `sub-of:<id>` tag — keyed by ID, never by name
    (baseline standing rule: names repeat across journeys).
    """
    kids = {}
    for f in features:
        for t in f.get("tags") or []:
            if str(t).startswith("sub-of:"):
                kids.setdefault(str(t).split(":", 1)[1].strip(), []).append(f)
    out = {}
    for f in features:
        if not f.get("is_container"):
            continue
        statuses = [k.get("status") for k in kids.get(f["id"], [])]
        if "Live" in statuses:
            out[f["id"]] = "Live"
        elif "Planned" in statuses:
            out[f["id"]] = "Planned"
        elif statuses and all(s == "Gap" for s in statuses):
            out[f["id"]] = "Gap"
        else:
            out[f["id"]] = "Planned"
    return out


def derive(feature, coverage, verified_live, benchmark_names, parity_gap_ids=frozenset(),
           manual_status=None):
    fid = feature["id"]
    hand_typed = feature.get("status", "")
    has_brd = bool(feature.get("brd"))
    has_figma = bool(feature.get("figma_link"))

    vl = verified_live.get(fid)
    high_cells, low_cells = _non_mismatched_cells(fid, coverage)
    all_ev = all_cells_for_feature(fid, coverage)
    p = pressure_score(fid, coverage, benchmark_names)

    result = dict(feature)  # copy all original fields (incl. `backends` if present)
    result["area"] = normalize_area(result.get("area"), result.get("journey"))
    result["pressure"] = p
    result["evidence_count"] = len(all_ev)
    # Backend split (IBKR/GTN): flag when a feature's status differs by backend so
    # views can render it. derived_status still reflects the more-advanced backend.
    if feature.get("backends") and len(set(feature["backends"].values())) > 1:
        result["backend_split"] = True

    # Compute priority = impact × pressure (null when impact is missing)
    impact = feature.get("impact")
    if impact is not None and p > 0:
        result["priority"] = impact * p
    else:
        result["priority"] = None

    # Rule 0: containers are scaffolding. Their status is DERIVED from their children
    # (Live if any child is Live, else Planned) and never typed. They carry no evidence
    # of their own, so they can never be "Missing evidence" and never raise a conflict —
    # a ↻ marker on a container would be noise, not a signal.
    if feature.get("is_container"):
        result["derived_status"] = _container_status(fid)
        result["status_conflict"] = False
        result["evidence_count"] = 0
        result["pressure"] = 0
        result["priority"] = None
        return result

    # Rule 0.5: Ahmed's manual determination is authoritative (Head-of-DX review).
    # Used for hand-reviewed features that carry no competitor or BRD signal.
    ms = (manual_status or {}).get(fid)
    if ms and ms.get("status"):
        result["derived_status"] = ms["status"]
        result["manual_status"] = True
        result["status_conflict"] = (ms["status"] != hand_typed)
        return result

    # Rule 1: verified_live present and < 90 days old → Live
    if vl:
        age = verified_live_age(vl)
        if age is not None and age < STALE_DAYS:
            derived = "Live"
        elif age is not None:
            derived = "Unverified"
        else:
            # verified_date is empty string — treat as stale
            derived = "Unverified"
        result["derived_status"] = derived
        result["status_conflict"] = (derived != hand_typed)
        return result

    # Rule 3: no verified_live, competitor evidence → Gap
    if high_cells:
        result["derived_status"] = "Gap"
        result["status_conflict"] = ("Gap" != hand_typed)
        return result
    if low_cells:
        result["derived_status"] = "Gap (unconfirmed)"
        result["status_conflict"] = (hand_typed not in ("Gap", "Gap (unconfirmed)"))
        return result

    # Rule 4: no verified_live, no competitor evidence, has BRD or Figma → Planned
    if has_brd or has_figma:
        result["derived_status"] = "Planned"
        result["status_conflict"] = ("Planned" != hand_typed)
        return result

    # Rule 4.5: cross-market parity gap — the sibling market (Saudi↔US) ships or
    # is building this, but this row is bare → a real internal Gap, not Unverified.
    if fid in parity_gap_ids:
        result["derived_status"] = "Gap"
        result["parity_gap"] = True
        result["status_conflict"] = (hand_typed not in ("Gap", "Gap (unconfirmed)"))
        return result

    # Rule 5: nothing at all → Unverified
    result["derived_status"] = "Unverified"
    result["status_conflict"] = ("Unverified" != hand_typed)
    return result


# ── Main ─────────────────────────────────────────────────────────────────────

def main():
    features = load_features()
    if not features:
        print(f"No features loaded from {FEATURES_JSON}")
        sys.exit(1)

    coverage = load_coverage()
    verified_live = load_verified_live()
    manual_status = load_manual_status()
    benchmark_names = set(load_benchmarks())
    parity_gap_ids = compute_parity_gaps(features, coverage, verified_live)
    _CONTAINER_STATUS.update(build_container_status(features))
    print(f"  Containers (status derived from children): {len(_CONTAINER_STATUS)}")

    print(f"  Inputs: {len(features)} features, "
          f"{len(coverage)} coverage cells, "
          f"{len(verified_live)} verified_live entries, "
          f"{len(benchmark_names)} benchmark competitors")

    derived = []
    for f in features:
        derived.append(derive(f, coverage, verified_live, benchmark_names, parity_gap_ids,
                              manual_status))
    n_parity = sum(1 for f in derived if f.get("parity_gap"))
    n_manual = sum(1 for f in derived if f.get("manual_status"))
    print(f"  Cross-market parity gaps flagged: {n_parity}")
    print(f"  Manual (Head-of-DX) determinations: {n_manual}")

    # Write output.
    # generated_at / source_md5 / baseline_version let the dashboard prove what it is
    # showing: source_md5 is the workbook this generation actually read, so a header
    # can compare it against the live master and flag STALE instead of quietly
    # rendering yesterday's data.
    output = {
        "_meta": {
            "schema_version": "1.1",
            "generated_by": "derive_status.py",
            "last_updated": TODAY.isoformat(),
            "generated_at": datetime.now().astimezone().isoformat(timespec="seconds"),
            "source_md5": _workbook_md5(),
            "baseline_version": _baseline_version(),
            "inputs": {
                "features_json": str(FEATURES_JSON),
                "coverage_json": str(COVERAGE_JSON),
                "verified_live_json": str(VERIFIED_LIVE_JSON),
            },
        },
        "features": derived,
    }
    OUTPUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_JSON.write_text(json.dumps(output, indent=2, ensure_ascii=False))
    print(f"  Output: {OUTPUT_JSON}")

    # Summary
    from collections import Counter
    status_counts = Counter(f["derived_status"] for f in derived)
    conflicts = sum(1 for f in derived if f.get("status_conflict"))
    unverified_diffs = sum(1 for f in derived if f.get("unverified_diff"))

    print(f"\n  Derived status distribution:")
    for s in ["Live", "Gap", "Gap (unconfirmed)", "Planned", "Unverified"]:
        print(f"    {s:14s} {status_counts.get(s, 0):>4}")

    print(f"\n  Status conflicts (derived ≠ hand-typed): {conflicts}")

    # Pressure summary
    with_pressure = [f for f in derived if f["pressure"] > 0]
    print(f"  Features with pressure > 0:              {len(with_pressure)}")

    # Show conflicts
    if conflicts:
        print(f"\n  Conflict detail (first 20):")
        shown = 0
        for f in derived:
            if f.get("status_conflict") and shown < 20:
                print(f"    {f['id']:10s} {f['status']:10s} → {f['derived_status']:12s}  "
                      f"({f['name'][:40]})")
                shown += 1


if __name__ == "__main__":
    main()
