# Benchmark — ARC vs Yahoo Finance

**Date:** 2026-08-30 · **Prepared by:** Digital Experience Department
**Scope:** ARC US Trading journey vs the Yahoo Finance feature set as described by a Saudi
US-market investor community account.
**Trigger:** X post by **@ypeooo** (*سترونق | السـوق الامــريكي*), read 2026-08-30.
**Method:** every Yahoo capability named in the post checked against the ARC Features Map,
baseline v2.15. Every ARC status below is a map row with an ID — nothing is estimated.

*Source: X/@ypeooo · 2026-08-30 · Features Map · features_derived.json · baseline v2.15*

---

## 1. Why this post matters

It is not a competitor announcement. It is **a Saudi investor telling other Saudi investors what
tool to use for the US market** — and recommending a free research app alongside, not instead of,
their broker. The closing line is explicit:

> *TradingView = charts and technical analysis · Yahoo Finance = financial data + news +
> fundamental analysis + portfolio tracking*

The investor has already decided their broker does not cover research. **The question this
benchmark answers is whether that assumption is true of ARC.**

Yahoo Finance is a tracked competitor in `data/compitiorlistnewv2.csv` (row 39, *Indirect ·
Global · Research and data platform*). It does not execute trades. Every comparison below is
research surface against research surface.

---

## 2. Headline

**ARC matches Yahoo on 14 of the 21 capabilities the post names, and beats it on execution.
The gaps are not depth — they are breadth of asset class, and alerting.**

| | Count |
|---|---:|
| ARC matches or exceeds | **14** |
| ARC has a Gap or no row | **7** |
| Of those, asset classes ARC does not cover at all | **4** |

*Source: Features Map · baseline v2.15 · US Trading journey, 265 rows*

---

## 3. Capability-by-capability

### 3.1 Per-stock data — ARC matches on every point

| Yahoo capability (per the post) | ARC row | Status |
|---|---|---|
| Current price | US-183 Stock change | **Live** |
| Trading volume | US-163 Key Statistics | **Live** |
| Market cap | US-163 Key Statistics | **Live** |
| 52-week high / low | US-163 Key Statistics | **Live** |
| Earnings and revenue | US-169 Earnings · US-220 Revenue | **Live** |
| Debt and cash | US-180 Balance Sheet | **Live** |
| Cash flows | US-181 Cash Flow | **Live** |
| **Valuation ratios — P/E, Forward P/E, PEG** | **no row exists** | **absent** |

### 3.2 Financial statements — ARC matches in full

| | ARC row | Status |
|---|---|---|
| Income Statement | US-179 | **Live** |
| Balance Sheet | US-180 | **Live** |
| Cash Flow | US-181 | **Live** |

All three sit under `US-168 Statements` → `US-167 Financial` on the Stock Page. Annual and
quarterly splits exist as rows (US-199…US-204) but are **unverified** — structure recorded,
status never walked.

### 3.3 News — ARC matches

| | ARC row | Status |
|---|---|---|
| Per-stock news | US-124 Stock News | **Live** |
| Market / economy / Fed news | US-066 News | **Live** |
| *(ARC extra)* Why Is It Moving | US-118 | **Live** |
| *(ARC extra)* Trending Stocks | US-120 | **Live** |
| News Screener | US-105 | Gap |

### 3.4 Watchlist and alerts — **ARC's sharpest gap**

| Yahoo capability | ARC row | Status |
|---|---|---|
| Watchlist | US-069 Watchlist · US-173 Add to Watchlist | **Live** |
| **Price alerts** | **US-182 Add Alert** | **Gap** |
| **News alerts** | **no row exists** | **absent** |
| **Earnings alerts** | **no row exists** | **absent** |

**This is the finding to act on.** The post names alerting as a reason to keep Yahoo installed,
and ARC cannot alert on a US stock at all. The asymmetry is internal, not competitive:
`SAU-227 Add Alert` is **Live** on the Saudi Stock Page and `XJ-020 Configurable Price Alerts` is
**Live** at platform level. **The capability exists in the building and has not been extended to
the US market.**

### 3.5 Portfolio tracking — ARC matches, and does more

Yahoo lets an investor *record* purchases. ARC holds the real position.

| | ARC row | Status |
|---|---|---|
| Holdings, share count, buy price | US-247 Portfolio Holdings · US-261 Holding Details | Live / Gap |
| Dividends | US-144 Portfolio Dividends | Missing evidence |
| Performance tracking | US-053 Performance Chart (IBKR) | **Live** |
| | US-111 Performance Chart (GTN) | **Gap** |

**Custodian split matters here.** The IBKR branch tracks performance; the GTN branch does not.
A GTN client gets less than a Yahoo user with a manually-typed portfolio.

### 3.6 Screener — ARC matches on the core

| | ARC row | Status |
|---|---|---|
| Stock Screener | US-012 | **Live** |
| Screener Themes | US-160 | Gap |

The post lists screening by price, market cap, growth, valuation and volume. The map records the
screener as one row and does not decompose its criteria, so **parity on the individual filters is
unverified** — worth a walk before claiming it.

### 3.7 Charts and comparison — ARC matches

| | ARC row | Status |
|---|---|---|
| Interactive chart | US-174 Stock chart | **Live** |
| Performance comparison between stocks | US-016 Compare Stock | **Live** |
| Drag-and-drop trade on chart | US-176 | Gap |

The post concedes Yahoo's charting *"does not replace TradingView for advanced technical
analysis."* ARC carries **US-039 Technical Analysis — Live**, on the same Stock Page. On the
post's own terms, **ARC covers ground Yahoo admits it does not.**

### 3.8 Asset-class coverage — **ARC's real breadth gap**

| Yahoo covers | ARC row | Status |
|---|---|---|
| US stocks | whole US Trading journey | **Live** |
| Indices (S&P 500, Nasdaq, Dow) | US-184 Indices page · US-151 Market indices chart · US-177 Indices change | **Live** |
| **ETFs** | US-017 ETF list | **Gap** |
| **Currencies** | **no row exists** | **absent** |
| **Gold and commodities** | **no row exists** | **absent** |
| **Crypto** | **no row exists** | **absent** |
| **Global markets (beyond US)** | **no row exists** | **absent** |

Four asset classes the post names are **not in the map at all** — not Gap, not Planned, simply
absent. `US-107 Intl Indices Historical Data` is Planned and is the only international row.

---

## 4. Where ARC is ahead — and it is not close

Yahoo Finance is a research app. Everything below is Live on the ARC US Stock Page and has **no
Yahoo equivalent**:

| ARC capability | Row |
|---|---|
| **Execution** — buying and selling the stock being researched | whole Orders area |
| Options Chain and option details | US-164 · US-227 |
| Analyst Ratings, Summary, Details, Bulls vs Bears | US-127 · US-165 · US-166 · US-117 |
| Market Depth | US-121 |
| Traders Summary | US-162 |
| Insider Trades · Government Trades | US-123 · US-119 |
| Technical Analysis | US-039 |
| Trade on Chart | US-077 |
| Pre/Post Market Trading · Fractional Shares | US-013 · US-014 |
| Sharia stock screening | US-003 |

**The post's own framing undersells ARC.** It positions the broker as execution-only and Yahoo as
the research layer. On the evidence, ARC's US Stock Page is the deeper research surface —
analyst ratings, market depth, insider and government trades and options data are all things
Yahoo does not provide free.

---

## 5. What I would do

1. **Ship US price alerts.** `US-182 Add Alert` is the single highest-value Gap in this
   benchmark. It is Live in Saudi (SAU-227) and Live at platform level (XJ-020) — this is
   extension work, not new build, and it is the reason the post gives for keeping a second app.
2. **Add valuation ratios to Key Statistics.** P/E, Forward P/E and PEG have no row anywhere.
   ARC already renders Income Statement, Balance Sheet and Cash Flow — the inputs are on the
   screen and the ratios are not.
3. **Decide on the four missing asset classes.** Currencies, commodities, crypto and global
   markets are absent from the map entirely. Each is a scope decision, not a gap to close
   quietly — and crypto in particular is **RED** under Decision Rights (Sharia governance).
4. **Fix GTN performance tracking.** `US-111 Performance Chart` Gap means a GTN client cannot see
   portfolio performance a Yahoo user gets by typing in trades manually.
5. **Do not treat ETF list as cosmetic.** ETFs are the second asset class the post names, and
   `US-017` is a Gap on the Market Page.

---

## Limits of this benchmark

- **The Yahoo side is the post's description, not a walk of the Yahoo app.** It is one
  well-informed investor's account and may omit or overstate features. No Yahoo screen was
  opened.
- **The ARC side is map status, not a fresh walk.** Statuses come from Features Map v2.15;
  33 US Trading rows are unverified and 10 of the Stock Page's own descendants carry no evidence.
- **Screener criteria were not compared** — ARC records the screener as a single row.
- **Free vs paid was not compared.** The post notes Yahoo gates deeper research behind a
  subscription; ARC has no equivalent tier in the map.
- Asset classes marked *absent* mean **no row in the map**, which is not the same as confirmed
  absence from the product. They have never been asked about.

*Prepared by Digital Experience · Sources: X/@ypeooo · 2026-08-30 · Features Map ·
features_derived.json · baseline v2.15 · data/compitiorlistnewv2.csv*
