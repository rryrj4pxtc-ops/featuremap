# Saudi Market Deep Dive — Orders area
**Date:** 2026-08-16 · **Area:** Saudi Market / Orders · 21 features (13 Live · 2 Planned · 6 Gap)

*Source: Features Map · 2026-08-16 · Research — Analysis of Trading Features and Gaps in ARC 2025.pdf (6 Nov 2025), Saudi Market matrices pp.3 & 6 · data/coverage.json*

---

## 1. This area has real Saudi-market evidence — unlike Stock Page

The key difference from the Stock Page pass: the research's **Saudi Market** section (pages 3
and 6) actually benchmarks order types on Tadawul. Four Orders rows are now sourced from
Saudi-market matrices rather than US ones.

| Research row | Page | ARC | Saudi competitors with it |
|---|---|---|---|
| **IceBurg** | 3 | ✗ | Sahm, SNB Capital |
| **Bracket Order** | 6 | 🕐 planned | Sahm, Derayah |
| **Repeat Order** | 3 | ✅ | SNB Capital |
| **Liquidity Tracking (In/Out Flow)** | 6 | 🕐 planned | Sahm, Alinma, SNB Capital |

**SNB Capital** and **Riyad Bank** added to the Benchmarks registry — both appear in the
Saudi competitor set and neither was registered. Benchmarks 18 → **20**.

---

## 2. Evidence provenance is now explicit in the data

The Stock Page pass exposed that Saudi gaps were being justified with US-market evidence.
Two tags now make this visible on every sourced row:

- `evidence-market:saudi` — benchmarked against competitors' **Tadawul** products
- `evidence-market:us` — benchmarked only against their **US** products (weaker for a Saudi row)

Applied to this pass's 6 rows and retro-applied to the 10 Stock Page rows sourced earlier.
The filter is now one query, not a document archaeology exercise.

---

## 3. Ranked Orders backlog

| ID | Feature | Status | Impact | Pressure | **Priority** | Evidence |
|---|---|---|---|---|---|---|
| SAU-002 | Limit Order | Live | 5 | 1 | **5** | — |
| SAU-044 | Quick Reorder | Live | 4 | 1 | **4** | saudi |
| **SAU-047** | **Bracket Order (OCO)** | **Gap** | 2 | 2 | **4** | **saudi** |
| SAU-042 | Conditional Orders | Live | 3 | 1 | 3 | — |
| **SAU-031** | **Iceberg Order** | **Gap** | 2 | 1 | 2 | **saudi** |
| SAU-113 | Futures Trading | Gap | 2 | 1 | 2 | us |
| SAU-114 | Fast Order (No Confirm) | Gap | 2 | 1 | 2 | us |
| SAU-106 | Trailing Order | Gap | 3 | 0 | — | none |
| SAU-105 | Chain Order | Gap | 2 | 0 | — | none |

**Top gap: Bracket Order (OCO)** — and it is the best-evidenced gap found so far in this
deep dive, because two Saudi competitors ship it on Tadawul. Every Stock Page gap at the same
priority rests on US-market evidence.

Impact scored on 17 previously-blank Orders rows. Order types that gate trading at all
(Limit, Market) scored 5; risk-management and product-access types 3; refinements 2.

---

## 4. Status discrepancies vs the research

Four rows where the map and the Nov-2025 research disagree. The research is 9 months old and
ARC may have shipped since — but each needs a decision, not a silent assumption.

| Feature | Map says | Research (Nov 2025) | Question |
|---|---|---|---|
| XJ-015 Liquidity Indicators | **Live** | ARC 🕐 planned | Shipped since, or wrongly marked Live? |
| SAU-042 Conditional Orders | **Live** | ARC 🕐 planned | Shipped since? |
| SAU-047 Bracket Order (OCO) | **Gap** | ARC 🕐 planned | Gap or Planned? These are different backlog states |
| SAU-044 Quick Reorder | cites **Sahm** | Sahm ✗ for Repeat Order (Saudi) | Where did the Sahm citation come from? |

SAU-047 matters most: it is the area's top gap, and if it is actually **Planned** rather than
a Gap, it belongs in the delivery backlog rather than the gap backlog.

---

## 5. Still unbenchmarked

**SAU-105 Chain Order** and **SAU-106 Trailing Order** carry only the `ceo-assessment` tag —
no competitor evidence from any source, so pressure 0 and no priority. Same class as
Government Trades and Stocks Key Facts from the Stock Page pass.

**Recommendation:** fold both into the benchmark check already commissioned for 2026-08-28
(`benchmark-check-request-2026-08-16.md`). Trailing Order is impact 3, the highest-impact
unbenchmarked row in either area.

---

## What changed in the data

- 6 rows gained competitor evidence · 17 rows gained impact scores
- `evidence-market:saudi` / `evidence-market:us` applied to 16 rows total
- Benchmarks 18 → **20** (SNB Capital, Riyad Bank)
- `data/coverage.json` 158 → **168** cells
- Features with pressure > 0: 67 → **70**
- Unfounded gaps matrix-wide: 38 → **35** (Saudi Market 13 → 10)
- Backup: `features-master.xlsx.bak-2026-08-16-orders`
- No status changed.

---

## 6. Features added by Ahmed (2026-08-16)

Five order-management capabilities were missing from the map entirely — no row in either
market. All confirmed **Live** by the Head of DX and mirrored to US Trading as Live, keeping
the Saudi↔US symmetry intact.

| Saudi | US | Feature | Impact |
|---|---|---|---|
| SAU-145 | US-139 | Edit Order | 4 |
| SAU-146 | US-140 | Cancel Order | 4 |
| SAU-147 | US-141 | Orders History | 3 |
| SAU-148 | US-142 | Customize Orders View | 2 |
| SAU-149 | US-143 | Convert to Market Order | 3 |

Named to the house convention — identical base name across both markets (journey
distinguishes them), matching the SAU-142 / US-134 `Customize Holdings View` pair. Ahmed's
phrasing "orders customize view" was normalised to **Customize Orders View** for consistency.

Each carries a `verified_live.json` record (`manual_confirmation`, Head of DX, 2026-08-16),
so Live Rate (D4) stays evidence-based rather than hand-claimed — the same standard applied
to the other 182 Live rows.

**Edit Order and Cancel Order scored impact 4** — modifying or pulling a working order is
core trading control, second only to placing one.

**Saudi Orders: 21 → 26 features, 13 → 18 Live (61.9% → 69.2%).**
US Orders: 28 → 33, 16 → 21 Live. Matrix total 335 → **345** · Live 182 → **192**.

*Source: Ahmed Alghamdi · 2026-08-16*
