# US Market Page — Deep Dive

**Date:** 2026-08-18 · **Scope:** US Trading / Market area / Market Page (18 rows)
**Method:** workbook state → BRD sourcing → competitor coverage → parity check against Saudi
**Status:** findings only — no workbook change applied. Decisions for Ahmed at the end.

*Source: Features Map · 2026-08-18 · baseline v1.6.1*

---

## 1. Current state

18 rows. Evidence is thin: **14 of 18 carry zero competitor evidence, and only 4 have impact
scored**, so `priority = impact × pressure` is uncomputable for two-thirds of the page.

| # | ID | Feature | Status | Impact | Pressure | Priority | Evidence |
|---|---|---|---|---|---:|---:|---:|
| 1 | US-004 | Stock Search | Live | — | 0 | — | 0 |
| 2 | US-064 | Sectors | **Gap** | — | 0 | — | 0 |
| 3 | US-065 | Sector & Exchange Volatility | Planned | — | 0 | — | 0 |
| 4 | US-145 | Stocks *(container)* | Live | — | — | — | — |
| 5 | US-009 | Trending Stocks | Live | — | 0 | — | 0 |
| 6 | US-003 | Shariah Compliance Lists | Live | — | 0 | — | 0 |
| 7 | XJ-005 | Economic Calendar | Live | — | 0 | — | 0 |
| 8 | US-028 | Earnings Calendar | Live | — | 0 | — | 0 |
| 9 | US-030 | Dividends Calendar | Live | — | 0 | — | 0 |
| 10 | US-066 | Market News | Live | — | 0 | — | 0 |
| 11 | US-105 | News Screener | **Gap** | — | 0 | — | 0 |
| 12 | US-012 | Stock Screener (US) | Live | 3 | 1 | 3 | 2 |
| 13 | US-067 | Analysis Changes | Planned | 2 | 1 | 2 | 2 |
| 14 | US-017 | ETF Exposure View | **Gap** | 1 | 1 | 1 | 3 |
| 15 | US-098 | Sukuk Trading | **Gap** | — | 0 | — | 0 |
| 16 | US-021 | Futures Trading | **Gap** | — | 0 | — | 1 |
| 17 | US-018 | **Whale / Institutional Tracking** | **Gap** | **5** | **2** | **10** | **4** |
| 18 | US-019 | Unusual Activity | **Gap** | — | 1 | — | 2 |

**Top-ranked gap: US-018 Whale / Institutional Tracking** — impact 5, priority 10, four
benchmarks confirmed (Abyan, Derayah, Moomoo, Webull). Highest-scoring row on the page.
Saudi carries the identical gap (SAU-111), so this is a both-markets gap, not a parity break.

*Source: Features Map · 2026-08-18 · App Store / competitor coverage cells*

---

## 2. What the BRDs add — five documents, none fully reflected in the map

### ARCD-50707 — Improve Listing & Search Functionality in US Market
**AS-IS (per BRD):** the customer must first pick an index (NASDAQ), and can search **only by
ticker symbol**. List shows Title = ticker, Sub-title = index.

**TO-BE requirements not represented as rows:**
- **"All" stocks list** aggregating NASDAQ + AMEX + NYSE, no index pre-selection, no duplicates
- **Search by stock name in English *and* Arabic**, case-insensitive, **partial match / auto-suggest**
- **Arabic name localisation** driven by app language, with fallback to English when absent
- List UI change: Title → symbol, Sub-title → **stock name** (currently index)
- Retain Sharia / General filters on the new list

US-004 Stock Search is marked **Live** and was verified by you on 2026-08-11. That is not in
conflict with the BRD — the *parent* search is live. What is unverified is whether the
above **sub-requirements** shipped. The BRD's own AS-IS says they had not.

### ARCD-61082 — International Stocks Screener
**AS-IS (per BRD):** "there is no advanced screener that allows them to filter."

**TO-BE requirements not represented as rows:**
- **Save screener criteria — up to 10 named filter sets** (this is the direct US twin of
  Saudi's SAU-144 Saved Themes)
- **Export results to Excel / CSV**
- Multi-select industry and sector; all filters optional
- Defined empty-state, timeout and duplicate-name messages

US-012 Stock Screener (US) is **Live**, verified 2026-08-11. Again the parent is live; the
save-criteria and export sub-features have no row and no verification.

### International Reports / Corporate Actions / Market Details / News BRD
Requirements with **no row anywhere in the map**:
- **Market Trading Hours** per exchange (US twin of Saudi SAU-191 Market Hours)
- **Market Settlement Holidays** per exchange — **no Saudi equivalent exists**; US-only
- Symbols list per market; latest ticker detail list
- **Market-level Corporate Actions** (by market/symbol/date range)
- Market & Symbol News — sources US-066 Market News, which currently carries **no BRD at all**

### International Market Data Feeder Subscription Packages BRD
**"Default subscription is delayed unsubscribed."** US market data is **delayed unless the
customer buys a real-time package**, and the entry point is a *"Delayed" button below the
stock*. This is a first-order US market experience constraint and it appears nowhere on the
Market Page.

It is **not** missing from the map — it lives as **XJ-065 Live Prices Subscription**
(Platform / Subscription area, Live, BRD ARCD-91702), with **XJ-057 Subscription Engine**
(Platform, Planned) alongside. So this is a **placement** finding, not a gap.

### ARCD-68581 — Fetch International Indices Historical Data
Sources **US-107 Intl Indices Historical Data** (Planned), currently sitting in backlog with
no screen after the v1.6 mirror.

*Source: BRD — ARCD-50707, ARCD-61082, ARCD-68581, International Reports Corporate Actions
Market Details News v1.3, International Market Data Feeder Subscription Packages v1.5*

---

## 3. Parity against Saudi — the "10 missing rows" claim does not hold

Ten Saudi Market Page rows have no US counterpart. But **all ten are themselves unverified in
Saudi** — created as contract scaffolding in v1.4 with no evidence:

Market Chart · Market Hours · Market Summary · Sector Details · Top Gainers · Top Losers ·
Most Active by Quantity · Most Active by Value · Top Traders · Saved Themes

Calling US "10 behind Saudi" would be comparing against rows Saudi cannot itself substantiate.

**Two of the ten are exceptions** — they now have independent US evidence from the BRDs, so
they are real US gaps regardless of Saudi's state:
- **Market Hours** → International Reports BRD
- **Saved Themes / Saved Screener Criteria** → ARCD-61082 requirement 3

---

## 4. Pipeline defect found — 30 competitor cells are silently discarded

`pressure_score()` counts a coverage cell only when the competitor name is in the registered
benchmark list. **30 cells across 22 feature rows are dropped**, leaving 9 rows at pressure 0
— and therefore priority `null` — despite having real evidence.

| Competitor | Cells | Why dropped |
|---|---:|---|
| Drahim, Thndr, hyssa, gate, Tarmeez, Wahed Invest, Anb capital, Raseed, Tiger Brokers, rain, ICAP, eo broker, Dinar, Manafa, TradeStation, eToro | 26 | not registered as benchmarks |
| **Tradingview** | 3 | **casing** — registered as `TradingView` |
| **Interactive Brokers** | 1 | **alias** — registered as `IBKR` |

The last two rows are pure data hygiene: 4 cells lost to a lowercase `v` and an unmapped alias.

**On this page it hides one row:** US-021 Futures Trading has a TradeStation cell, but
TradeStation is unregistered, so the row reads as unevidenced with pressure 0. US-017 ETF
Exposure View loses its eToro cell the same way.

*Source: derive_status.py `pressure_score()` · data/coverage.json · benchmarks.json*

---

## 5. Proposed rows — checked against the whole map first, no duplicates

| Proposed | Placement | Source | Note |
|---|---|---|---|
| All Stocks List | under US-004 Stock Search | ARCD-50707 | absent |
| Search by Name (EN/AR) + partial match | under US-004 | ARCD-50707 | absent |
| Saved Screener Criteria | under US-012 Stock Screener | ARCD-61082 | US twin of SAU-144 |
| Export Screener Results (Excel/CSV) | under US-012 | ARCD-61082 | Saudi has none either — US-ahead |
| Market Trading Hours | Market Page top-level | Intl Reports BRD | US twin of SAU-191 |
| Market Settlement Holidays | Market Page top-level | Intl Reports BRD | **no Saudi twin** |
| Market Corporate Actions | Market Page top-level | Intl Reports BRD | market-level, distinct from US-131 |

**Not proposed — already exists:** real-time/delayed market data (XJ-065 Live Prices
Subscription, Platform). Export of *reports* also already exists as US-062 Downloadable
Reports, but that is portfolio reports, not screener results — distinct.

---

## 6. Decisions for Ahmed

1. **Create the 7 proposed rows?** All are BRD-sourced. Statuses would be left blank for you
   to set, or defaulted to Gap pending verification — your call.
2. **US-004 and US-012 are Live by your 2026-08-11 confirmation, but their BRD
   sub-requirements are unverified.** Should the parent stay Live with the sub-features
   tracked separately (my recommendation), or should the parent be re-reviewed?
3. **XJ-065 Live Prices Subscription** — should the delayed/real-time data constraint surface
   on the US Market Page, or stay a Platform row? It shapes the US market experience more
   than most rows on this page.
4. **Register the missing benchmarks** (or at minimum fix `Tradingview` → `TradingView` and
   `Interactive Brokers` → `IBKR`) so 30 evidence cells stop being discarded.
5. **US-018 Whale / Institutional Tracking** is the top-ranked gap here (priority 10) and is
   also a Saudi gap (SAU-111). Treat as one cross-market initiative?
6. **Impact is unscored on 14 of 18 rows.** Score them now, as we did for Saudi?

---

*Prepared by Digital Experience · Source: Features Map · 2026-08-18*
