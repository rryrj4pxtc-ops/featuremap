# Features Matrix Hygiene Check — 2026-08-16

**Scope:** 329 feature rows · 182 Live · 85 Planned · 62 Gap · 13 benchmarks
**Script:** `dashboard/scripts/hygiene_check.py` (reusable, run as `python3 hygiene_check.py [YYYY-MM-DD]`)

*Source: Features Map · 2026-08-16 (features.json, last_updated 2026-08-15) · benchmarks.json · data/verified_live.json*

---

## Check 1 — Competitor names resolve to Benchmarks

**Result: PASS — 0 unresolved names.**

Every competitor named in the matrix maps to an entry in the Benchmarks sheet.

**Caveat:** only **35 of 329 rows (11%)** name a competitor at all. The check is clean because
the field is largely empty, not because coverage is good.

*Source: Features Map · 2026-08-16*

---

## Check 2 — Gaps with no competitor named

**Result: FAIL — 50 of 62 Gap rows (81%) have no competitor named.**

A Gap with no competitor is an unfounded gap: nothing in the matrix says who has it or why
it matters. None of the 50 carry a tag pointing to a competitor source either.

| Journey | Unfounded gaps | Feature IDs |
|---|---|---|
| Saudi Market | 22 | SAU-031, SAU-064, SAU-066, SAU-069, SAU-070, SAU-076, SAU-085, SAU-105, SAU-106, SAU-107, SAU-111, SAU-112, SAU-113, SAU-114, SAU-121, SAU-128, SAU-131, SAU-133, SAU-134, SAU-135, XJ-006, XJ-058 |
| US Trading | 20 | US-019, US-020, US-021, US-024, US-025, US-035, US-037, US-044, US-046, US-050, US-064, US-076, US-081, US-098, US-103, US-105, US-110, US-111, US-114, US-126 |
| Platform | 5 | XJ-021, XJ-038, XJ-042, XJ-049, XJ-052 |
| LMS/SBL | 2 | US-041, US-092 |
| IPOs | 1 | IPO-007 |

### Sub-findings

**a) 6 of the 50 are duplicate rows, not distinct gaps.** Tagged `stock-page-dup-of:` —
they mirror an existing gap onto the Stock Page area and should inherit the parent's
competitor evidence rather than being sourced independently:
`US-126→US-019`, `SAU-128→SAU-070`, `SAU-131→SAU-069`, `SAU-133→SAU-111`,
`SAU-134→SAU-112`, `SAU-135→SAU-076`. (18 rows carry this tag matrix-wide.)

**b) 8 carry a provenance tag that is not competitor evidence.**
`ceo-assessment` (SAU-105, SAU-106, XJ-049, XJ-052, XJ-058, US-103) and
`parity-mirror` (SAU-121, US-092, US-098). These have a known origin — CEO input or
Saudi↔US parity mirroring — so they are defensible, but the origin should be recorded in
the competitors/tags field so they stop reading as unfounded.

**c) 50 of 62 Gap rows have no `impact` score**, so `priority = impact × pressure` cannot be
computed. Only 22 of 329 rows matrix-wide have a computed priority. The gap backlog is
currently unrankable.

*Source: Features Map · 2026-08-16*

---

## Check 3 — Live decay (Live rows unverified > 90 days)

**Result: PASS on the letter — 0 stale, 0 never verified. All 182 Live rows have a verification record.**

**But the evidence quality is weak and the clock was effectively reset in bulk:**

| Verified date | Rows | Method |
|---|---|---|
| 2026-08-11 | 168 | `manual_confirmation` |
| 2026-08-15 | 8 | `manual_confirmation` |
| 2026-08-01 | 3 | `appstore_release_notes` |
| 2026-07-16 | 3 | `appstore_release_notes` |

- **176 of 182 (97%)** are `manual_confirmation` — self-attested, no external evidence.
- Only **6 of 182 (3%)** are backed by App Store release notes.
- All 182 are marked `confidence: high`, which is not distinguishable by method.
- 168 were stamped on a single day (2026-08-11), five days ago. The 90-day window will not
  flag anything until **2026-11-09**, so this check will pass trivially for the next three months.

The `live-verification-checklist.md` (2026-08-11, 63 features flagged as Live without App
Store evidence) appears to have been closed out by bulk manual confirmation rather than
per-feature verification.

*Source: Features Map · 2026-08-16 · data/verified_live.json*

---

## Recommended actions

| # | Action | Effort |
|---|---|---|
| 1 | Attach competitor evidence to the 36 genuinely unsourced gaps — or downgrade them out of Gap status | M |
| 2 | Make the 6 `stock-page-dup-of:` rows inherit their parent's competitor field automatically in `derive_status.py` | S |
| 3 | Record `ceo-assessment` / `parity-mirror` as an explicit provenance field so non-competitor gaps stop failing this check | S |
| 4 | Score `impact` on the 50 unscored Gap rows so the backlog becomes rankable | M |
| 5 | Split `confidence` by method — `manual_confirmation` should not read as `high` alongside App Store evidence | S |
| 6 | Add a fourth hygiene check: Live rows whose only evidence is `manual_confirmation` older than 30 days | S |

*Source: Ahmed Alghamdi · 2026-08-16 — recommendations pending review*
