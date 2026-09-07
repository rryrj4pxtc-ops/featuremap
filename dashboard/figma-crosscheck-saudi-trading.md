# Figma Cross-Check: Saudi Trading

> Note: feature ids updated on 2026-05-08 as part of the Investor Engagement / Corporate Actions restructure. See restructure-plan-engagement-ca.md.
>
> Note: feature ids updated on 2026-05-07 as part of the Portfolio Monitoring / Wealth Visibility restructure. See restructure-plan.md.
>
> Note (2026-05-11): SAU-013 → LMS-006, SAU-014 → LMS-007, SAU-028 [DELETED]. See below for old references.

**Date:** 2026-05-05
**Scope:** Saudi Trading journey only
**Figma files examined:** CDO, Tradepad, Market, Orders, Trader Mode
**xlsx source:** `dashboard/features-master.xlsx` (56 rows where journey = "Saudi Trading")

---

## Method

1. Walked all pages/sections/frames in the 5 relevant Figma files at depth=3
2. Identified distinct capabilities (skipping variants, error states, loading states, empty states)
3. Matched each Figma capability against the 56 Saudi Trading rows in features-master.xlsx
4. Classified into four buckets

---

## Summary

| Bucket | Count |
|--------|-------|
| MATCH-LINKED | 24 |
| MATCH-UNLINKED | 15 |
| IN-FIGMA-NOT-IN-XLSX | 12 |
| AMBIGUOUS | 5 |

---

## 1. MATCH-LINKED

Features in xlsx that have a clear corresponding Figma design AND already reference Figma as a source.

| xlsx ID | Feature Name | Figma Location | Notes |
|---------|-------------|----------------|-------|
| SAU-001 | Place Market Order | CDO > Tradepad (64 "trade" frames) | Full buy/sell flow with market order type |
| SAU-002 | Place Limit Order | CDO > Tradepad (Order type list) | Limit order type visible in order type selector |
| SAU-004 | Nomu Subscription | CDO > Tradepad (trade frames with Nomu context) | Parallel market order flow |
| SAU-012 | Derivatives (Options) Trading | CDO > buy/sell/options ("options-v3 2") | Options trading flow present |
| SAU-019 | Nomu IPO (Institutional) | CDO > Tradepad | Institutional Nomu flow frames |
| SAU-020 | Portfolio P&L View | CDO > P/L Chart (14 frames, "P&L" section) | Chart and portfolio P&L views |
| SAU-024 | Instant Settlement (T+0/T+1) | CDO > Tradepad (settlement variant frames) | Settlement options in trade confirmation |
| SAU-026 | Tradable Rights Screen | Trader Mode > Portfolio > "Tradable Rights" section | Huqooq section in portfolio |
| SAU-027 | Market Home — Tablet | CDO > IPAD (74 frames, full iPad market layout) | Complete tablet market experience |
| SAU-028 [DELETED] | UAE Market Orders | CDO > Tradepad (UAE market chips visible) | UAE market in market selector chips |
| SAU-029 | Conditional Order Detail | CDO > Tradepad ("Trading page - Conditional - Type/Criteria") | Conditional order configuration screens |
| SAU-030 | Basket Order Detail | CDO > Tradepad (Flow Section frames with basket context) | Part of advanced order flows |
| SAU-031 | Iceberg Order Detail | CDO > Tradepad (Flow Section) | Part of advanced order type list |
| SAU-032 | Interval Order Detail | CDO > Tradepad (Flow Section) | Part of advanced order type list |
| SAU-033 | Stop Loss Detail | CDO > Tradepad (Flow Section) | Stop loss in order types |
| SAU-034 | Take Profit Detail | CDO > Tradepad (Flow Section) | Take profit in order types |
| SAU-035 | Basket Order Create | CDO > Tradepad (Flow Section creation flow) | Basket creation screens |
| SAU-036 | Order Filter Panel | CDO > order view ("Customize Holding" as filter) | Order filtering/customization |
| SAU-037 | Orders Empty State | CDO > Watchlist ("Watchlist - empty") / CDO > order view | Empty state frame present |
| SAU-049 | Saudi Options (Native) | CDO > buy/sell/options + Trade Options page | Full native options trading flow |
| SAU-003 | Margin Lending (Murabaha) | CDO > LMS Renew (11 frames) | Margin/LMS lending screens |
| SAU-006 | TILA Price Display | CDO > TILA redesign (3 modal sheet frames) | TILA price modal redesign |
| SAU-009 | Margin Contract Renewal | CDO > LMS Renew (contract renewal flow) | LMS renewal screens |
| SAU-010 | Margin Early Payment | CDO > LMS Renew (payment flow) | Early payment variant in LMS |

---

## 2. MATCH-UNLINKED

Features in xlsx that have a clear Figma design but xlsx does NOT currently list "Figma" as a source (figma_link is empty).

| xlsx ID | Feature Name | Figma Location | Action |
|---------|-------------|----------------|--------|
| SAU-005 | Block Codes (AML) | CDO > Tradepad (block/restriction states in trade flow) | Add figma_link |
| SAU-007 | Market-on-Close (MOC) | CDO > Tradepad > Validity list (MOC in validity dropdown) | Add figma_link |
| SAU-008 | Auto Margin Approval | CDO > LMS Renew (approval flow frames) | Add figma_link |
| SAU-011 | Margin Phase 2 (Commodities) | CDO > LMS Renew (commodity context frames) | Add figma_link |
| LMS-006 (was SAU-013) | SBL Program | CDO > Tradepad (SBL flow in advanced sections) | Add figma_link |
| SAU-017 | Tadawul News Push | CDO > index info banner / index banner (news push frames) | Add figma_link |
| SAU-018 | Top Trending Stocks | CDO > Stock List ("Search stock" with trending) | Add figma_link |
| SAU-021 | P&L History (Sold Stocks) | CDO > P/L Chart > Section 1 (earnings/P&L history) | Add figma_link |
| SAU-022 | Update Avg Cost Price | CDO > Portfolio Analysis (cost-related analytics) | Add figma_link |
| SAU-023 | Buying Power Swap | CDO > Cash Transaction (cash overview with transfer) | Add figma_link |
| SAU-025 | Sector & Exchange Volatility | CDO > Stock Page - chips (sector/market info container) | Add figma_link |
| SAU-042 | Conditional Orders (Full BRD) | CDO > Tradepad ("Trading page - Conditional" frames) | Already in Figma — upgrade from Gap? |
| SAU-044 | Quick Reorder | CDO > Trade confirmation enhance - Reorder (8 frames) | Already in Figma — upgrade from Gap? |
| SAU-055 | Advanced Trade Button | CDO > Tradepad (buy/sell options footer with advanced entry) | Already in Figma — revisit Gap status? |
| SAU-056 | Murabaha Margin Lending | CDO > LMS Renew (full margin lending screens) | Add figma_link |

---

## 3. IN-FIGMA-NOT-IN-XLSX (Missing from features-master.xlsx)

Distinct capabilities designed in Figma that have no matching row in the Saudi Trading xlsx inventory.

### Activity assessment method

- **Page status icons** are maintained by the design team in CDO page names: ✅ = design complete, 🟡 = in review / iterating, ⏳ = queued / blocked. No icon = early or stale.
- **File-level edit frequency:** CDO had **60+ edits in the last 7 days** (May 5 back to Apr 28) by 5 designers (Mohamed, Ahmed, babdelhamid, Shahad, Sufana). The file is heavily active.
- **Per-page edit dates** are not available via Figma API. The status icons and frame counts are the strongest signals.
- **Comments:** 0 comments on the CDO file (team likely uses an external tool for review).

### Detail per feature

| # | Feature | CDO Page | Status Icon | Frames | Sections | Verdict |
|---|---------|----------|-------------|--------|----------|---------|
| 1 | **Dividend Calculator** | "Dividend Calcautor 🟡" | IN REVIEW | 27 | "Stocks Dividend Calculator" (9 fr), "other enteries" (3 fr) | **ADD** — active, substantial design |
| 2 | **Earnings Calendar (Saudi)** | "P/L Chart ✅" | COMPLETE | 22 | "Section 1" (5 fr), "P&L" (5 fr) | **ADD** — marked complete |
| 3 | **Stock Screener (Saudi)** | "Stock List ⏳ 🟡🟡" | QUEUED + REVIEW | 18 | — | **ADD** — heavy iteration (double 🟡), 5 screener frames |
| 4 | **Portfolio Reordering** | "Portflio Reodering ✅" | COMPLETE | 21 | 6 option sections (drag, custom button, settings) | **ADD** — marked complete, multiple interaction variants |
| 5 | **Holding Customization** | "Holding customaztion 🟡" | IN REVIEW | 15 | "6 data Selected (Max)", "No data selected", "draft" (7 fr) | **ADD** — active, shows data-picker with max constraint |
| 6 | **Order View Customization** | "order view 🟡" | IN REVIEW | 12 | "3 data Selected (Max)", "No data selected" | **ADD** — active, same pattern as Holding Customization |
| 7 | **Live Prices Subscription** | "Live Prices ✅" | COMPLETE | 10 | — | **ADD** — marked complete, shows pricing tiers |
| 8 | **Trading Counter (Hours)** | "Trading Counter (hours) ✅" | COMPLETE | 2 | — | **SKIP** — only 2 frames, minor UI element (market hours label on home), not a standalone feature |
| 9 | **Order Count Badge** | "order Count ✅" | COMPLETE | 7 | — | **SKIP** — 7 frames but this is a UI micro-enhancement (badge on tab), not a standalone feature |
| 10 | **Analysis & Technical Redesign** | "anaylsis rating and techncal anaysis redesign" | NO ICON | 6 | — | **SKIP** — no status icon, only 6 generic "US" frames, likely early exploration or abandoned |
| 11 | **Index Banner / Market Ticker** | "index banner ✅" + "index info banner ✅" | COMPLETE | 43 | — | **ADD** — marked complete across 2 pages, 43 frames, significant feature |
| 12 | **Trade Confirmation Enhance** | "Trade confrimation enhance - Reorder ⏳ 🟡🟡" | QUEUED + REVIEW | 19 | "Last Option" (8 fr), "Order Details" (4+4 fr) | **ADD** — active iteration, order preview redesign with reorder |

### Summary

| Verdict | Count | Features |
|---------|-------|----------|
| **ADD to xlsx** | 9 | Dividend Calculator, Earnings Calendar, Stock Screener, Portfolio Reordering, Holding Customization, Order View Customization, Live Prices Subscription, Index Banner, Trade Confirmation Enhance |
| **SKIP** | 3 | Trading Counter (micro-enhancement), Order Count Badge (micro-enhancement), Analysis Redesign (stale/abandoned) |

---

## 4. AMBIGUOUS

Items where the Figma content is unclear, overlaps multiple journeys, or cannot be confidently matched.

| # | Figma Location | Possible Match | Issue |
|---|---------------|----------------|-------|
| 1 | CDO > "Cash Transaction" page | SAU-023 (Buying Power Swap) OR WLT (Wealth Visibility) | Cash transaction could be Saudi Trading buying power or general wealth |
| 2 | CDO > "App Widget" — Portfolio Widget | SAU or PRT journey | Widget customization unclear if Saudi-specific or cross-journey |
| 3 | CDO > "Watchlist" — Sliding buy/sell | SAU-001 (market order) or new feature | Slide-to-trade from watchlist — enhancement or new capability? |
| 4 | CDO > "stock name and logo clickable" page | SAU or PRT | Holding overview with clickable names — unclear journey ownership |
| 5 | Trader Mode file (entire file) | Multiple SAU features | "Trader Mode" is an alternative UI skin — same features, different layout. Not a new capability. |

---

## Key Findings

### Gap features that already have Figma designs (status should be revisited):

| ID | Name | Current Status | Evidence |
|----|------|---------------|----------|
| SAU-039 | Stock Screener | Gap | CDO > "Stock List" has 5 "Stock screener" frames |
| SAU-042 | Conditional Orders (Full BRD) | Gap | CDO > Tradepad has full conditional order UI |
| SAU-044 | Quick Reorder | Gap | CDO > "Trade confirmation enhance - Reorder" |
| SAU-055 | Advanced Trade Button | Gap | CDO > buy/sell/options has multi-type entry |

These 4 features are marked as **Gap** (competitor-only) but have active Figma designs. They should likely be upgraded to **Planned**.

### Coverage stats:

- **56** Saudi Trading features in xlsx
- **39** have a confirmed Figma presence (24 linked + 15 unlinked)
- **12** Figma capabilities have no xlsx row at all
- **17** xlsx features have no visible Figma design (mostly BRD-only backend features like SBL Digital Acceptance, Short Selling, Tadawulaty SSO, etc.)

---

## Recommended Actions

1. **Add figma_link** to the 15 MATCH-UNLINKED rows
2. **Add 12 new rows** for IN-FIGMA-NOT-IN-XLSX features (SAU-057 through SAU-068)
3. **Upgrade 4 Gap features** to Planned (SAU-039, SAU-042, SAU-044, SAU-055) since they have active designs
4. **Resolve 5 ambiguous items** with the design team to confirm journey ownership

*Source: Figma API — files CDO, Tradepad, Market, Orders, Trader Mode · depth=3 · 2026-05-05*
