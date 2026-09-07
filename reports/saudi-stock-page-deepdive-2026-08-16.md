# Saudi Market Deep Dive — Stock Page area
**Date:** 2026-08-16 · **Area:** Saudi Market / Stock Page · 19 features (7 Live · 4 Planned · 8 Gap)

*Source: Features Map · 2026-08-16 · Research — Analysis of Trading Features and Gaps in ARC 2025.pdf (6 Nov 2025) · data/coverage.json*

---

## 1. The 36.8% maturity figure is an artifact

**9 of 19 rows (47%) are `stock-page-dup-of:` mirrors** of features that live in the Market
or Orders areas — reused stock-detail components, deliberately tagged as duplicates during
the 2026-08-11 IA review.

| Duplicate | Mirrors |
|---|---|
| SAU-128 Government Trades | SAU-070 |
| SAU-131 Insider Trades | SAU-069 |
| SAU-133 Whale / Institutional | SAU-111 |
| SAU-134 Unusual Activity | SAU-112 |
| SAU-135 Analyst Ratings | SAU-076 |
| SAU-129 Trending Stocks | SAU-018 |
| SAU-130 Dividends Calendar | SAU-116 |
| SAU-132 News | (deep-discovery) |
| SAU-127 Options | SAU-012 |

Stock Page is "weakest area" mainly because the duplicated rows inherit their parents'
Gap status and are then counted twice. **Recommendation:** exclude `stock-page-dup-of:`
rows from area maturity, or count them at their parent's status. Until then the Stock Page
score is not comparable to the other four areas.

---

## 2. The gap backlog was entirely unsourced — 5 of 8 now sourced

Before today: all 8 Stock Page gaps had **no competitor named and no coverage cell**.
Sourced from the Nov-2025 trading gap research (matrices on pages 10–19, read from the
page images — the PDF text layer holds only the column headers):

| Feature | Local competitors with it | Global | Pressure |
|---|---|---|---|
| SAU-135 Analyst Ratings | Derayah, Awaed | none | 2 |
| SAU-133 Whale / Institutional | Derayah, Abyan (+ Moomoo, Robinhood) | OKX, Webull | 2 |
| SAU-064 Why Is It Moving | Awaed, Abyan | — | 2 |
| SAU-131 Insider Trades | Derayah | — | 1 |
| SAU-134 Unusual Activity | Sahm *(notification only)* | Webull | 1 |
| SAU-066 Bulls vs Bears | **none** | **none** | 0 |
| SAU-128 Government Trades | *not benchmarked* | — | 0 |
| XJ-058 Stocks Key Facts | *not benchmarked* | — | 0 |

Evidence also propagated to the Market-area parents (SAU-069/076/111/112) and the US twins
(US-018/019/025/125/126). **31 coverage cells added**, dated to the research (2025-11-06),
not today — so the age of the evidence stays visible.

**Unfounded gaps matrix-wide: 50 → 38.** Webull added to the Benchmarks registry (cited by
the research). OKX deliberately excluded — crypto exchange, out of scope for a Shariah equity broker.

---

## 3. ⚠️ The evidence is US-market, the rows are Saudi Market

This is the important finding. The six discovery features appear **only in the research's
US Market sections** (pages 10–19). The Saudi Market competitor section (pages 3–6) covers a
different, smaller feature set — Sell Capital, Iceberg, Repeat Order, Major Shareholder,
Stock Dividend, Gain/Loss, Stock Alert, Compare Stocks, Technical Analysis, News,
Fundamental Data, Research Hub, Bracket Order, Liquidity Tracking — and contains **none** of
these rows.

So these Saudi Market gaps are justified by what Derayah, Sahm, Awaed and Abyan offer in
their **US** trading products. Whether the same firms ship these features on **Tadawul** is
unverified. All sourced rows are tagged `benchmark:trading-gaps-2025` so the provenance
travels with the data.

**Needed:** a Saudi-market benchmark pass on these six before any of them is funded.

---

## 4. Bulls vs Bears is a differentiator, not a gap

No competitor offers it — not Sahm, Derayah, Awaed or Abyan locally; not Saxo, eToro, OKX
or Webull globally. And **US-117 Bulls vs Bears is Live**, so ARC already ships it in the US
market. SAU-066 is therefore an *internal parity gap*, and the capability itself is an
ARC differentiator that should be counted as one. Both rows tagged `no-competitor-offers-this`.

---

## 5. Parity breaks found

**US ships what Saudi lacks** — these are internal parity gaps, not competitive ones:

| Feature | US | Saudi |
|---|---|---|
| Why Is It Moving | US-118 **Live** | SAU-064 Gap |
| Bulls vs Bears | US-117 **Live** | SAU-066 Gap |
| Insider Trades | US-123 **Live** | SAU-131 Gap |
| Government Trades | US-119 / US-008 **Live** | SAU-128 / SAU-070 Gap |

**Missing US mirror:** Analyst Ratings exists only as SAU-076 / SAU-135. Every other Stock
Page feature has a US twin. This breaks the US↔Saudi symmetry established on 2026-08-11.

---

## 6. Decisions — resolved 2026-08-16

1. **SAU-045 Major Shareholder — stays `Planned`.** Ahmed's determination, upholding the
   existing 2026-08-11 record. Research p3 shows ARC ✓ in Saudi (vs ✗ for US on p16), but
   that tick is an uncorroborated ARC self-assessment and is not treated as evidence of Live.
   Note recorded against the existing `manual_status.json` entry; the original determination
   date is preserved.
2. **Impact scored — approved.** 16 Stock Page rows scored; the backlog is now rankable.
   Top gaps: Why Is It Moving, Whale / Institutional Tracking, Analyst Ratings (priority 4 each).
   Nothing scored above 3 — none of these blocks funding or a first trade.
3. **Analyst Ratings US mirrors added — approved.** Two rows, not one, to match the
   Market + Stock Page pattern every other feature in this area follows:
   **US-137** (Market) and **US-138** (Stock Page, `stock-page-dup-of:US-137`), both Gap,
   Derayah + Awaed, impact 2, priority 4.
4. **Benchmark check commissioned.** Government Trades + Stocks Key Facts, owner Strategy &
   Intelligence, due 2026-08-28. Brief: `benchmark-check-request-2026-08-16.md`.
   Scope B (Saudi-market verification of the six US-sourced gaps) remains recommended but
   not commissioned.

---

## What changed in the data

- `features-master.xlsx` — 15 rows gained competitor evidence, 2 rows tagged
  `no-competitor-offers-this`, Webull added to Benchmarks (17 → 18)
- `data/coverage.json` — 123 → 154 cells
- Features with pressure > 0: 52 → **67**
- 335 features (US-137, US-138 added) · impact scored on 16 Stock Page rows
- Backup: `features-master.xlsx.bak-2026-08-16-stockpage` · `coverage.json.bak-2026-08-16-stockpage`
- No status was changed. The 4 `Gap → Unverified` conflicts are the rows added earlier today,
  unrelated to this pass.

*Source: Ahmed Alghamdi · 2026-08-16*
