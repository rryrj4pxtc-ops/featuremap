# Benchmark Check Request — Stock Page unbenchmarked features
**Commissioned:** 2026-08-16 by Ahmed Alghamdi (Head of DX)
**Owner:** Strategy & Intelligence
**Due:** 2026-08-28 (aligns with Squad Validation Cycle 2 responses)
**Trigger:** Saudi Market deep dive — Stock Page pass (`saudi-stock-page-deepdive-2026-08-16.md`)

---

## Scope A — Unbenchmarked features (the commission)

Two Stock Page gaps carry **no competitor evidence from any source** — not the Nov-2025
trading gap research, not `coverage.json`, not the weekly competitor report. They are Gaps
on assertion alone, and cannot be ranked (`priority` is null because pressure = 0).

| Feature | Also as | Journey / Area | Impact | Current evidence |
|---|---|---|---|---|
| **Government Trades** | SAU-128 (Stock Page dup) · SAU-070 (Market) · US-119, US-008 (**Live** in US) | Saudi Market | 2 | none |
| **Stocks Key Facts** | XJ-058 (Stock Page) · US-103 (US Trading) | Saudi Market | 3 | none |

### What to determine, per feature

1. **Does each benchmark competitor offer it — in their Saudi (Tadawul) product?**
   Check set: Sahm · Derayah · Derayah Smart · Alinma · AlJazira Capital · Abyan · Awaed
   Secondary (global, for reference only): Moomoo · Robinhood · Webull · IBKR
2. **If yes — where does it live** (stock page, market page, separate screen) and what is shown?
3. **If no competitor offers it** — say so explicitly. That is a valid and useful outcome; it
   makes the row a differentiator candidate rather than a gap (see Bulls vs Bears, which turned
   out this way).
4. **Government Trades specifically:** US-119 and US-008 are marked **Live in ARC's US product**.
   Confirm whether the Saudi absence is a genuine gap or simply an unmirrored capability.

### How to record the outcome

- Add a cell per competitor to `data/coverage.json` in the standard shape
  (`FEATURE::Competitor` → `feature_id, competitor, supports, checked_date, source, evidence, confidence`)
- Use the **real check date** as `checked_date` — do not backdate or use today's date for old evidence
- Re-run `derive_status.py` so pressure and priority recompute
- A "no competitor has it" result should be recorded as a `no-competitor-offers-this` tag on the row

---

## Scope B — Recommended extension (not commissioned; needs Ahmed's go-ahead)

The Stock Page pass surfaced a larger evidence problem. **Six Saudi Market gaps are sourced
entirely from the research's US Market matrices** — the Saudi Market section of the same
document contains none of these rows. So we are justifying Tadawul gaps with what these
firms ship in their *US* products.

| Feature | Saudi row(s) | Sourced from | Pressure |
|---|---|---|---|
| Why Is It Moving | SAU-064 | US matrix (Awaed, Abyan) | 2 |
| Whale / Institutional Tracking | SAU-133, SAU-111 | US matrix (Derayah, Abyan, Moomoo, Robinhood) | 2 |
| Analyst Ratings | SAU-135, SAU-076 | US matrix (Derayah, Awaed) | 2 |
| Insider Trades | SAU-131, SAU-069 | US matrix (Derayah) | 1 |
| Unusual Activity | SAU-134, SAU-112 | US matrix (Sahm, notification-only) | 1 |
| Bulls vs Bears | SAU-066 | US matrix — **nobody has it** | 0 |

All are tagged `benchmark:trading-gaps-2025` so the provenance is visible in the data.
**These three currently rank joint-top of the Stock Page backlog (priority 4)** — Why Is It
Moving, Whale / Institutional Tracking, Analyst Ratings. If the Saudi-market reality differs,
the top of the backlog is wrong.

**Recommendation:** run the same Saudi-product check across these six while the analyst is
already in the competitor apps. Marginal cost is low; it either confirms the ranking or
corrects it before anything is funded.

---

## Related open item

**SAU-045 Major Shareholder** is marked `Planned`, but research page 3 (Saudi Market
Competitors) shows **ARC ✓ has it** while page 16 shows ARC ✗ for US — a deliberate
Saudi/US split matching US-025's Gap. Evidence is ARC's own self-assessment from 6 Nov 2025
with no corroboration. Awaiting Ahmed's determination; if confirmed it goes to
`data/manual_status.json`, not a hand edit.

*Source: Features Map · 2026-08-16 · Research — Analysis of Trading Features and Gaps in ARC 2025.pdf (6 Nov 2025) · Ahmed Alghamdi · 2026-08-16*
