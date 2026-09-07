# Saudi Market — Feature Assignment (DRAFT)

> Generated 2026-05-11. Maps 101 Saudi Market features to screens in saudi-market-screen-inventory.md.
> **Status:** DRAFT — for Ahmed's review before updating features-master.xlsx.
> **Updated 2026-05-11:** 5 features removed from Saudi Market (SAU-013 → LMS-006, SAU-014 → LMS-007, SAU-096 → XJ-066, SAU-101 → XJ-067, SAU-028 deleted). 3 features changed to Gap status (SAU-005, SAU-016, SAU-099).

## Summary

- **Total features:** 101
- **Assigned to a screen:** 98
- **Flagged for review (no screen match):** 3 (SAU-005, SAU-016, SAU-099 — kept in Saudi Market as Gap)
- **Distribution by area:**

| Area | Assigned | % |
|---|---|---|
| Portfolio | 37 | 37.8% |
| Watchlist | 18 | 18.4% |
| Trading Actions | 15 | 15.3% |
| Stock Page | 10 | 10.2% |
| Orders | 9 | 9.2% |
| Market | 9 | 9.2% |
| **Total assigned** | **98** | **100%** |

---

## Assignments

| id | name | proposed area | proposed screen | confidence | reason |
|---|---|---|---|---|---|
| SAU-001 | Place Market Order | Trading Actions | Tradepad | High | Market order is one of the Tradepad's order type modes. |
| SAU-002 | Place Limit Order | Trading Actions | Tradepad | High | Limit order is the default Tradepad mode (Normal Buy/Sell). |
| SAU-003 | Margin Lending (Murabaha) | Portfolio | Margin Activation Process | High | figma_link node 2277-16009 maps to Margin Activation section (node 2277-16013). Multi-step application flow. |
| SAU-004 | Nomu Subscription | Market | IPO Details | Medium | Nomu IPO subscription is an IPO-type flow; IPO Details screen covers subscription dates, pricing, and subscribe CTA. |
| SAU-006 | TILA Price Display | Market | Market Home | Medium | Real-time vs delayed price toggle. Affects many screens but Market Home is the primary landing where price mode matters most. Cross-screen note. |
| SAU-007 | Market-on-Close (MOC) | Trading Actions | Tradepad | High | MOC is an order type executed via the Tradepad. |
| SAU-008 | Auto Margin Approval | Portfolio | Margin Activation Process | High | Automated approval is part of the margin activation flow (eligibility check step). |
| SAU-009 | Margin Contract Renewal | Portfolio | Margin Account Home | High | Renewal is a portfolio-level margin action surfaced on the Margin Account Home. |
| SAU-010 | Margin Early Payment | Portfolio | Margin Account Home | High | Early repayment action on the margin portfolio. |
| SAU-011 | Margin Phase 2 (Commodities) | Portfolio | Margin Account Home | Medium | Commodity margin extension of the existing margin portfolio view. |
| SAU-012 | Derivatives (Options) Trading | Trading Actions | Options Tradepad | High | Full options trading flow lives on the Options Tradepad. |
| SAU-015 | Short Selling | Trading Actions | Tradepad | Medium | Short sell is an order action placed via the Tradepad. Requires SBL program (LMS-006, moved to LMS journey) as prerequisite. |
| SAU-017 | Tadawul News Push | Market | News | Medium | Push notifications for market news. Canonical screen is the News feed. Note: also a notification/system capability beyond this screen. |
| SAU-018 | Top Trending Stocks | Market | Trending Tickers | High | Direct match — Trending Tickers screen shows top 20-30 most-searched stocks. |
| SAU-019 | Nomu IPO (Institutional) | Market | IPO Details | Medium | Institutional Nomu subscription uses the IPO Details screen (variant for institutional investors). |
| SAU-020 | Portfolio P&L View | Portfolio | P/L Overview | High | figma_link node 2029-45173 maps to the P/L Overview section (node 2029-48806). Performance chart with date range. |
| SAU-021 | P&L History (Sold Stocks) | Portfolio | P/L Overview | High | Sold stocks P&L report is part of the P/L history within P/L Overview. |
| SAU-022 | Update Avg Cost Price | Portfolio | Holding Details | High | Manual cost price correction is a per-holding action on the Holding Details screen. |
| SAU-023 | Buying Power Swap | Portfolio | All Portfolios View | Medium | Buying power transfer shown on All Portfolios View where total cash/buying power is displayed. May need its own modal. |
| SAU-024 | Instant Settlement (T+0/T+1) | Portfolio | Instant Settlement Home | High | Direct match — Instant Settlement Home is the landing for settlement options. |
| SAU-025 | Sector & Exchange Volatility | Market | Sectors Page | Medium | Sector-level volatility indicators belong on the Sectors Page heatmap. |
| SAU-026 | Tradable Rights Screen | Portfolio | One Portfolio View | High | figma_link node 2007-35148 is in the Portfolios file. One Portfolio View explicitly mentions tradable rights display. |
| SAU-027 | Market Home — Tablet | Market | Market Home | High | Tablet-optimized layout variant of Market Home. Same screen, different viewport. |
| SAU-029 | Conditional Order Detail | Orders | Order Details | High | Order Details screen covers all order types including conditional orders. |
| SAU-030 | Basket Order Detail | Orders | Basket Details | High | Direct match — Basket Details shows basket contents, value, and per-stock status. |
| SAU-031 | Iceberg Order Detail | Orders | Order Details | High | Order Details screen covers iceberg/slicing order view. |
| SAU-032 | Interval Order Detail | Orders | Order Details | High | Order Details screen covers interval/scheduled order view. |
| SAU-033 | Stop Loss Detail | Orders | Order Details | High | Order Details screen covers stop loss order view. |
| SAU-034 | Take Profit Detail | Orders | Order Details | High | Order Details screen covers take profit order view. |
| SAU-035 | Basket Order Create | Trading Actions | Create Basket | High | Direct match — Create Basket screen covers basket creation with stock selection and conditions. |
| SAU-036 | Order Filter Panel | Orders | Stock Order Filter | High | Direct match — Stock Order Filter screen is the full-screen filter for orders. |
| SAU-037 | Orders Empty State | Orders | Orders List | High | Empty state is a state variant of the Orders List screen. |
| SAU-038 | Level 2 Order Book | Stock Page | Stock Details | High | Market depth / order book is shown within the Stock Details page. Also visible in Tradepad, but Stock Details is the canonical view. |
| SAU-039 | Stock Screener | Market | Stock Screener | High | Direct match — Stock Screener screen covers filtering by fundamentals, technicals, sector. |
| SAU-040 | Advanced Technical Analysis | Stock Page | Stock Details | High | Chart with indicators, drawing tools, and pattern detection lives on the Stock Details interactive chart. |
| SAU-041 | Stock Comparison Tool | Stock Page | Compare Stocks | High | Direct match — Compare Stocks screen provides side-by-side multi-stock comparison. |
| SAU-042 | Conditional Orders (Full BRD) | Trading Actions | Tradepad | High | Conditional order entry is a Tradepad mode (market index/sector/share price triggers). |
| SAU-043 | Money Flow Tracking | Stock Page | Stock Details | Medium | Inflow/outflow by trade size is a per-stock metric best shown on Stock Details. |
| SAU-044 | Quick Reorder | Orders | Orders List | Medium | One-tap reorder from order history. Orders List is where past orders are visible. |
| SAU-045 | Major Shareholder Data | Stock Page | Stock Details | High | Top shareholders is a data section within the Stock Details page. |
| SAU-046 | Sukuk Trading | Trading Actions | Sukuk Tradepad | High | Direct match — Sukuk Tradepad is the sukuk-specific order entry screen. |
| SAU-047 | Bracket Order (OCO) | Trading Actions | Tradepad | High | Bracket (stop-loss + take-profit) is an advanced order type placed via the Tradepad. |
| SAU-048 | Chart Trading | Stock Page | Stock Details | High | Placing orders directly on the price chart — the chart lives on Stock Details. |
| SAU-049 | Saudi Options (Native) | Trading Actions | Options Tradepad | High | Full native options trading flow on the Options Tradepad. |
| SAU-050 | Chart Touch-and-Hold | Stock Page | Stock Details | High | Press-and-hold intra-day price interaction on the Stock Details chart. |
| SAU-051 | Auto-Watchlist on Buy | Watchlist | Watchlist | Medium | Automatic addition of purchased stocks to watchlist. Canonical screen is Watchlist itself. Note: cross-screen automation triggered from trading flow. |
| SAU-052 | Always-On Price View | Stock Page | Stock Details | High | Bid/ask/spread always visible in portrait — Stock Details is the canonical price view. |
| SAU-053 | Chart Axis to Market Close | Stock Page | Stock Details | High | X-axis chart behavior on the Stock Details intra-day chart. |
| SAU-054 | Standard S&D Layout | Stock Page | Stock Details | High | Supply/demand (order book) layout convention on the Stock Details page. |
| SAU-055 | Advanced Trade Button | Trading Actions | Tradepad | High | Multi-order-type entry button and most-traded shortcut at Tradepad entry point. |
| SAU-056 | Murabaha Margin Lending | Portfolio | Margin Account Home | High | Full Sharia-compliant digital margin — the ongoing margin portfolio view. |
| SAU-057 | Watchlist Home | Watchlist | Watchlist | High | figma_link node 2015-17180 pointed to the Home widget (dropped from inventory as out-of-scope). Feature maps to the Watchlist main screen. |
| SAU-058 | Watchlist — Story View | Watchlist | Watchlist | High | figma_link node 2012-14669. Story card layout is a view mode of the Watchlist screen (consolidated during cleanup). |
| SAU-059 | Watchlist — Add Stock | Watchlist | Add Stocks to Watchlist | High | figma_link node 2012-31313 is an exact match to Add Stocks to Watchlist screen. |
| SAU-060 | Watchlist — Edit / Reorder | Watchlist | Watchlist | Medium | figma_link node 2012-31364. No separate edit screen in inventory — likely an overlay/mode on Watchlist. Possible missing screen. |
| SAU-061 | Watchlist — Empty State | Watchlist | Watchlist | High | figma_link node 2012-35864. Empty state was merged into the Watchlist screen entry during cleanup. |
| SAU-062 | Watchlist — Main View (Full List) | Watchlist | Watchlist | High | figma_link node 2012-35887 is an exact match to the Watchlist screen. |
| SAU-063 | Watchlist — Menu / Actions | Watchlist | Watchlist | Medium | figma_link node 2012-39946. Context menu is an overlay within the Watchlist screen, not a separate destination. |
| SAU-064 | Moving Up Screen | Watchlist | Moving Up Story | High | figma_link node 2018-50473 is an exact match. |
| SAU-065 | Moving Down Screen | Watchlist | Moving Down Story | High | figma_link node 2018-53055 is an exact match. |
| SAU-066 | Bulls vs Bears Screen | Watchlist | Bulls vs Bears Story | High | figma_link node 2018-55635 is an exact match. |
| SAU-067 | News Screen | Watchlist | News Story | High | figma_link node 2018-60820 is an exact match. |
| SAU-068 | Dividends Screen | Watchlist | Dividends Story | High | figma_link node 2018-63412 is an exact match. |
| SAU-069 | Insider Trades Screen | Watchlist | Insider Trades Story | High | figma_link node 2018-68787 is an exact match. |
| SAU-070 | Government Trades Screen | Watchlist | Government Trades Story | High | figma_link node 2018-71425 is an exact match. |
| SAU-071 | Story Wishlist Detail | Watchlist | Story Wishlist | High | figma_link node 2018-76715 is an exact match. |
| SAU-072 | Minichart Component | Watchlist | Watchlist | Low | figma_link node 2012-72580. This is a UI component (mini chart in stock rows), not a screen. Assigned to Watchlist as its primary surface. See flagged notes. |
| SAU-073 | Saudi Portfolio Holdings | Portfolio | All Portfolios View | High | Holdings with quantities, cost, P&L — the All Portfolios View shows aggregated holdings. |
| SAU-074 | Holdings Letter (PDF) | Portfolio | Portfolio Reports | High | PDF report download is a report type within the Portfolio Reports screen. |
| SAU-075 | Performance Chart | Portfolio | One Portfolio View | High | One Portfolio View includes performance chart (1W/1M/2M/3M). |
| SAU-076 | Analyst Ratings | Watchlist | Analyst Ratings Story | High | figma_link node 2018-58217 is an exact match to Analyst Ratings Story. Note: Stock Page > Analyst Ratings also exists — this feature was explicitly linked to the watchlist story version. |
| SAU-077 | Saudi Portfolio Selector | Portfolio | Choose Portfolio | High | Direct match — Choose Portfolio is the portfolio picker/selector. |
| SAU-078 | Transfer Holdings | Portfolio | Transfer Holdings | High | Direct match — Transfer Holdings screen covers stock transfer between portfolios. |
| SAU-079 | Add to Watchlist | Portfolio | Add Holdings to Watchlist | High | Direct match — Add Holdings to Watchlist covers selecting holdings to add. |
| SAU-080 | Liquidate Holdings | Portfolio | Liquidate Holdings | High | Direct match — Liquidate Holdings screen covers bulk sell flow. |
| SAU-081 | Downloadable Reports | Portfolio | Portfolio Reports | High | Portfolio Reports screen includes report list with filters and download. |
| SAU-082 | Gain/Loss Tax Report | Portfolio | Portfolio Reports | High | Tax report is a report type within the Portfolio Reports screen. |
| SAU-083 | More Options Menu (Saudi) | Portfolio | One Portfolio View | High | figma_link node 2007-28734 is in the Portfolios file near One Portfolio View. Contextual menu for portfolio actions. |
| SAU-084 | Peer Portfolio Comparison | Portfolio | Portfolio Performance Analysis | High | Portfolio Performance Analysis includes a Peers Comparison tab. |
| SAU-085 | Portfolio Insights | Portfolio | Portfolio Performance Analysis | High | Portfolio Performance Analysis includes the Portfolio Insights card view (gains, trading activity, overview). |
| SAU-086 | Portfolio Health Score | Portfolio | Portfolio Health Score | High | Direct match — Portfolio Health Score screen with 0-100 score and factor breakdown. |
| SAU-087 | Allocation Tracker | Portfolio | Portfolio Performance Analysis | High | figma_link node 2106-58522 was Asset Allocation View, consolidated into Portfolio Performance Analysis. |
| SAU-088 | Analysis Dashboard | Portfolio | Portfolio Performance Analysis | High | Top stocks, gains/losses, allocation analytics — all tabs within Portfolio Performance Analysis. |
| SAU-089 | Visual Asset Allocation | Portfolio | Portfolio Performance Analysis | High | Granular allocation breakdown is covered by the Allocation tab in Portfolio Performance Analysis. |
| SAU-090 | Goal Tracker | Portfolio | Smart Goal Setup & Tracking | High | Direct match — Smart Goal Setup & Tracking covers goal-based investing with progress tracking. |
| SAU-091 | Storyteller (Quarterly) | Portfolio | Digital StoryTeller | High | Quarterly narrative report maps to the Digital StoryTeller screen. |
| SAU-092 | Digital StoryTeller | Portfolio | Digital StoryTeller | High | Direct match — Digital StoryTeller is the interactive year-in-review story. |
| SAU-093 | Storyteller Report | Portfolio | Digital StoryTeller | High | Narrative performance report is delivered via the Digital StoryTeller screen. |
| SAU-094 | Holdings Filter Panel | Portfolio | Portfolio Filters | High | Direct match — Portfolio Filters screen covers full-screen filter overlays for holdings. |
| SAU-095 | Sector/Index/Shariah Filters | Portfolio | Portfolio Filters | High | Portfolio Filters includes tabs for Index, Sectors, Shariah, Research, Tradable Rights. |
| SAU-097 | Batch Close Positions | Portfolio | Liquidate Holdings | High | Batch close is functionally the same as the Liquidate Holdings flow (sell multiple positions). |
| SAU-098 | Auto Dividend Reinvest | Portfolio | Holding Details | Low | Dividend reinvestment toggle would logically live on the per-holding detail screen. No Figma frame found. |
| SAU-100 | Trading Incentive Banners | Market | Market Home | Medium | Promotional banners for trading offers. Market Home is the highest-traffic landing. Note: could also appear on other screens as a cross-screen promotional surface. |
| SAU-102 | Rights Issue (Digital) | Portfolio | One Portfolio View | Medium | Digital rights subscription flow. One Portfolio View mentions tradable rights. Related to SAU-026. May need its own screen for the full subscription flow. |
| SAU-103 | Attached Order | Trading Actions | Tradepad | Medium | Attached order type — placed via the Tradepad order type picker. No definition in features.json. |
| SAU-104 | Slicing Order | Trading Actions | Tradepad | Medium | Slicing (iceberg) order type — placed via the Tradepad. No definition in features.json. |
| SAU-105 | Chain Order | Trading Actions | Tradepad | Medium | Chain order type — placed via the Tradepad. No definition in features.json. |
| SAU-106 | Trailing Order | Trading Actions | Tradepad | Medium | Trailing stop order type — placed via the Tradepad. No definition in features.json. |

---

## Flagged for Review (3)

> 5 features previously flagged here were resolved on 2026-05-11: SAU-013 → LMS-006, SAU-014 → LMS-007, SAU-096 → XJ-066, SAU-101 → XJ-067, SAU-028 deleted.

| id | name | status | reason | suggestion |
|---|---|---|---|---|
| SAU-005 | Block Codes (AML) | Gap | Backend compliance feature (AML block code management). No UI screen in the 5 Saudi Market Figma files. | Backend/admin capability. No screen needed — tag as infrastructure or cross-screen. |
| SAU-016 | Tadawulaty SSO | Gap | Single sign-on to external Edaa/Tadawulaty platform. No screen in inventory — cross-app integration. | Cross-screen capability. May surface via a button/link on Profile or Portfolio screens. |
| SAU-099 | Social / Copy Trading | Gap | Follow & replicate professional traders. No screen in any of the 5 Saudi Market Figma files. Entirely new capability. | New screen(s) needed: "Copy Trading Home", "Trader Profiles", "Copy Settings". Major new feature requiring its own screen set. |

---

## Assignment Notes

### High-concentration screens

Some screens attract many features. This is expected — they are primary destinations.

| Screen | Area | Features assigned | IDs |
|---|---|---|---|
| Tradepad | Trading Actions | 11 | SAU-001, 002, 007, 015, 042, 047, 055, 103, 104, 105, 106 |
| Stock Details | Stock Page | 9 | SAU-038, 040, 043, 045, 048, 050, 052, 053, 054 |
| Watchlist | Watchlist | 8 | SAU-051, 057, 058, 060, 061, 062, 063, 072 |
| Portfolio Performance Analysis | Portfolio | 5 | SAU-084, 085, 087, 088, 089 |
| Order Details | Orders | 5 | SAU-029, 031, 032, 033, 034 |
| One Portfolio View | Portfolio | 4 | SAU-026, 075, 083, 102 |
| Margin Account Home | Portfolio | 4 | SAU-009, 010, 011, 056 |
| Digital StoryTeller | Portfolio | 3 | SAU-091, 092, 093 |
| Portfolio Reports | Portfolio | 3 | SAU-074, 081, 082 |
| Portfolio Filters | Portfolio | 2 | SAU-094, 095 |

### Screens with zero features assigned

| Screen | Area | Notes |
|---|---|---|
| Switch Funds | Portfolio | Mutual fund action — may belong to Mutual Funds journey, not Saudi Market. |
| Asset Selection | Portfolio | Sub-step screen used within Transfer/Liquidate flows — features assigned to those parent screens. |
| Share / Export | Portfolio | Utility screen — no feature explicitly covers sharing/export as a standalone capability. |
| Instant Cash Withdrawal | Portfolio | Sub-flow of Instant Settlement. SAU-024 assigned to the Home screen. |
| Margin Monitor Dashboard | Portfolio | Margin monitoring — no feature explicitly covers the monitoring dashboard vs. the account home. |
| ETF List Page | Market | No Saudi Market feature covers ETF browsing specifically. |
| ETF Detail Page | Market | No Saudi Market feature covers individual ETF details. |
| Events & Calendars | Market | No feature covers the aggregated calendar. Dividends/earnings stories exist but are Watchlist-based. |
| Research & Reports | Market | No feature covers the research reports listing. |
| News Article Detail | Market | SAU-017 (Tadawul News Push) assigned to News home, not the article detail. |
| Index Customization | Market | No feature covers index widget customization. |
| Trade Log | Market | No feature explicitly covers the trade log/history screen. |
| Market Filters | Market | Market-level filter panel — no standalone feature. |
| Stock Financials | Stock Page | No feature covers financial statements (income, balance sheet, cash flow) as a capability. |
| Liquidity Analytics | Stock Page | No feature covers liquidity metrics. |
| Options Chain | Stock Page | SAU-012/049 (options trading) assigned to Options Tradepad; no feature for the chain browse screen. |
| Option Contract Details | Stock Page | No feature covers viewing individual option contract details. |
| Stock Order Filter | Orders | SAU-036 assigned here. |
| Basket Details | Orders | SAU-030 assigned here. |
| Order Preview | Orders | No feature covers the order confirmation preview step. |
| ARC Story | Watchlist | No feature explicitly covers the ARC Story format screen. |
| Earnings Story | Watchlist | No feature covers the earnings story screen. |
| Search Stock / Fund | Trading Actions | No feature covers the search-before-trade screen. |
| Basket Management | Trading Actions | SAU-035 assigned to Create Basket; no feature for the basket list/management screen. |
| OTP Verification | Trading Actions | Shared OTP screen — cross-flow utility, no standalone feature. |
| Order Type Helper | Trading Actions | Educational content — no feature covers order type education. |
| Sukuk Tradepad | Trading Actions | SAU-046 assigned here. |

### Cross-screen features (assigned but flagged)

These features are assigned to one canonical screen but affect multiple screens:

| id | name | assigned screen | also affects |
|---|---|---|---|
| SAU-006 | TILA Price Display | Market Home | Stock Details, Watchlist, Tradepad — price display mode is app-wide. |
| SAU-017 | Tadawul News Push | News | System-level push notifications, not just the News screen. |
| SAU-051 | Auto-Watchlist on Buy | Watchlist | Triggered from trading flow (Tradepad → Watchlist). |
| SAU-072 | Minichart Component | Watchlist | Also used in Market Home, Stock Screener, and Portfolio views. |
| SAU-100 | Trading Incentive Banners | Market Home | Could appear on Home, Portfolio, or other high-traffic screens. |

### Features that may need new screens

| id | name | why |
|---|---|---|
| SAU-099 | Social / Copy Trading | Major new feature (Gap). Needs trader profiles, copy settings, leaderboard screens. |
| SAU-102 | Rights Issue (Digital) | Assigned to One Portfolio View but the subscription flow likely needs its own screen. |

> SBL Program and SBL Digital Acceptance moved to LMS journey (LMS-006, LMS-007) on 2026-05-11.

---

## Confidence Distribution

| Confidence | Count | % |
|---|---|---|
| High | 76 | 77.6% |
| Medium | 18 | 18.4% |
| Low | 4 | 4.1% |
| **Total assigned** | **98** | **100%** |

---

*Source: features.json (101 Saudi Market features after cleanup) + saudi-market-screen-inventory.md (69 screens) · 2026-05-11*
