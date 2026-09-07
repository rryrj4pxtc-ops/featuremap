# Saudi / US Cross-Market Parity Analysis

**Date:** 22 July 2026
**Owner:** Head of Digital Experience
**Scope:** Saudi Market (92 features) vs US Trading (81 features)
**Purpose:** Establish which feature concepts are genuinely shared across the two markets, which are market-specific, and where real cross-market gaps exist.

*Source: Features Map · 2026-07-22 · `features-master.xlsx` → `features_derived.json`*

---

## Summary

| Measure | Count |
|---|---|
| Saudi Market features | 92 |
| US Trading features | 81 |
| **Shared concepts (total)** | **~70** |
| — matched on identical name (`(US)` suffix only) | 52 |
| — **requiring cross-market reconciliation** | **22** |
| Saudi-only (market-specific) | ~20 |
| US-only | ~10 |

US Trading was clearly built as a mirror of the Saudi set: 52 features carry the same
name with a `(US)` suffix. The remaining 22 concepts are shared but need judgment —
they are renamed, split at different granularity, merely analogous, or blocked by
market structure. **Those 22 are the deliverable below.**

---

## The 22 concepts requiring reconciliation

Format is `hand-typed / derived`. **↻** = evidence-refined (the two disagree).

| Concept | Type | Saudi ID | SAU hand/derived | US ID | US hand/derived | Note |
|---|---|---|---|---|---|---|
| Iceberg Order | renamed | SAU-031 | Gap / Planned ↻ | US-046 | Gap / Unverified ↻ |  |
| Stop Loss | renamed | SAU-033 | Live / Planned ↻ | US-033 | Gap / Unverified ↻ |  |
| Take Profit | renamed | SAU-034 | Live / Planned ↻ | US-034 | Gap / Unverified ↻ |  |
| Options Trading | renamed | SAU-049 | Planned / Planned | US-005 | Planned / Planned | only clean row |
| Bulls vs Bears | renamed | SAU-066 | Gap / Planned ↻ | US-006 | Live / Planned ↻ |  |
| Sector / Index Filters | renamed | SAU-095 | Live / Planned ↻ | US-064 | Gap / Unverified ↻ | SAU adds Shariah filter |
| P&L History (Sold) | renamed | SAU-021 | Gap / Planned ↻ | US-074 | Gap / Unverified ↻ |  |
| Holdings Letter (PDF) | renamed | SAU-074 | Live / Planned ↻ | US-052 | Gap / Unverified ↻ |  |
| Major Shareholder | renamed | SAU-045 | Gap / Unverified ↻ | US-025 | Gap / Unverified ↻ |  |
| Bracket Order (OCO) | renamed | SAU-047 | Planned / Gap (unconfirmed) ↻ | US-037 | Gap / Unverified ↻ |  |
| Insider Trades | renamed | SAU-069 | Gap / Planned ↻ | US-031 | Live / Planned ↻ | US ahead |
| Place Order | renamed | SAU-002 | Live / Planned ↻ | US-001 | Live / Planned ↻ | SAU=Limit, US=Market |
| Watchlist | renamed | SAU-057 | Live / Planned ↻ | US-069 | Gap / Unverified ↻ |  |
| Dividends | renamed + dup | SAU-068 | Live / Planned ↻ | US-030 | Live / Planned ↻ | "Screen" vs "Calendar"; ×3 both sides |
|  |  | SAU-115 | Live / Unverified ↻ | US-082 | Live / Unverified ↻ |  |
|  |  | SAU-116 | Live / Unverified ↻ | US-083 | Live / Unverified ↻ |  |
| Portfolio Holdings | renamed | SAU-073 | Live / Gap ↻ | US-051 | Gap / Unverified ↻ |  |
| Trending Stocks | renamed | SAU-018 | Live / Planned ↻ | US-009 | Live / Planned ↻ | "Stocks" vs "Tickers" |
| Stock Comparison | renamed | SAU-041 | Live / Gap (unconfirmed) ↻ | US-016 | Live / Gap (unconfirmed) ↻ | "Comparison" vs "Compare" |
| **Government Trades** | renamed | SAU-070 | **Gap** / Planned ↻ | US-008 | **Live** / Planned ↻ | **US ahead — real SAU gap** |
| Basket Orders | granularity | SAU-035 | Live / Planned ↻ | US-035 | Gap / Unverified ↻ | SAU split Create/Detail |
|  |  | SAU-030 | Live / Planned ↻ | — | — |  |
| Extended Hours | analogous | SAU-108 | Gap / Unverified ↻ | US-013 | Live / Gap (unconfirmed) ↻ | **DO NOT MERGE** — different microstructure |
| Fixed Income | analogous | SAU-046 | Gap / Unverified ↻ | US-020 | Gap / Unverified ↻ | **DO NOT MERGE** — Sukuk is the Sharia-compliant instrument |
| **Fractional Shares** | market-specific | SAU-109 | Gap / Unverified ↻ | US-014 | Gap / Gap (unconfirmed) | **SAU: 0 competitors → Pile 3** |

*Source: Features Map · 2026-07-22*

---

## Key finding — Fractional Shares is NOT a Saudi gap

| | SAU-109 | US-014 |
|---|---|---|
| Definition | "Buy fractional shares of **Saudi-listed** stocks" | "Buy partial shares of expensive stocks" |
| Competitors offering it | **none** | Moomoo, Robinhood, IBKR |
| evidence_count | **0** | 3 |
| pressure | **0** | 2 |

**Not one app in the 56-competitor benchmark offers fractional Saudi-listed shares**,
while the same concept has three confirmed providers on the US side. Zero coverage
across an entire market is the signature of a market-structure constraint, not a
competitive gap.

**Recommendation:** classify SAU-109 as **Pile 3 / market-specific**. US-014 remains
a real gap.

> ⚠️ **Regulatory basis unconfirmed.** Public sources (CMA, Saudi Exchange) returned no
> authoritative statement on whether Tadawul permits fractional trading. The Pile 3
> classification currently rests on competitor-coverage inference, not a regulatory
> citation. **Route to `compliance-and-sharia-governance` for the definitive CMA/Tadawul
> position before locking this classification.**
>
> *Source: unverified — do not present to stakeholders*

---

## Real cross-market gaps (evidence-backed)

**Caveat: no feature in the reconciliation set derives to `Live` on either side.** Every
"Live in one market, Gap in the other" is a *hand-typed claim* the pipeline cannot
confirm. The derived column shows Saudi rows landing on `Planned` and US rows on
`Unverified` — that is a **documentation gap on the US side** (US features have no BRD,
no Figma, no competitor evidence), not a proven capability difference.

Claimed gaps worth verifying:

| Direction | Concepts |
|---|---|
| **Saudi ahead** | Stop Loss, Take Profit, Sector/Index Filters, Holdings Letter, Watchlist, Basket Orders |
| **US ahead** | Bulls vs Bears, Insider Trades, **Government Trades**, Extended Hours |

**`Government Trades` (SAU-070 Gap ↔ US-008 Live) is the single clearest actionable
item** — the US app ships the equivalent; check whether the implementation is portable.

---

## Data quality issues surfaced

1. **Intra-market duplicates** — same concept, multiple rows in the same journey:
   - Saudi: `Dividends Screen` ×3 (SAU-068/115/116), `Performance Chart` ×2 (SAU-075/118), `Earnings Calendar` ×2 (SAU-107/117)
   - US: `Dividends Calendar` ×3 (US-030/082/083), `Performance Chart` ×2 (US-053/085), `Earnings Calendar` ×2 (US-028/084)
   - These inflate any cross-match count and should be de-duped before the next parity run.

2. **Granularity mismatch** — Saudi splits order types into Create/Detail/Empty-State/List
   screens (SAU-029/030/035/037/120); US uses one feature per order type. Decide whether
   parity is measured at *feature* or *concept* granularity.

3. **Evidence coverage** — 27 of 28 rows in the reconciliation set carry ↻. Only
   `Options Trading` is clean on both sides.

4. **Open conflict pending app verification** — `SAU-038` / `US-011` Level 2 Order Book.
   See `projects/features-map/pending-app-checks.md`.

---

## Method

- Matching pass 1: exact name after normalization (strip `(US)`, parentheticals, market qualifiers).
- Matching pass 2: token-set Jaccard ≥ 0.5 → 14 renamed concepts.
- Matching pass 3: synonym-collapsed semantic matching (screener≈filter, P&L≈profit,
  compare≈comparison, sukuk≈bonds, trending≈top, ticker≈stock) → 4 further genuine matches
  (Trending, Stock Comparison, Government Trades, Extended Hours) plus Basket Orders and
  Fixed Income identified by manual review.
- ~20 candidate pairs discarded as false positives where the only shared token was generic
  (`HOLDINGS`, `WATCHLIST`, `orders`) — e.g. "Transfer Holdings" ⟷ "Portfolio Holdings".

*Source: Features Map · 2026-07-22 · derived via `scripts/derive_status.py`*
