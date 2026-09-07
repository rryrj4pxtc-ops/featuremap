# Saudi Market — BRD Gap Analysis
**Saudi features with no BRD:** 57  |  **Generated:** 2026-08-10

> Saudi Market is the source market — features aren't parallels of another market, so almost nothing can be linked (SAU-118 Performance Chart was the one exact duplicate, now linked to ARCD-2654). The rest are genuinely undocumented capabilities. Grouped into families below so the squad can scope BRDs per cluster rather than per feature.

---

## Charting & technical analysis (9)
| Feature | Definition |
|---|---|
| SAU-039 Stock Screener | Filter stocks by fundamentals, technicals, s |
| SAU-040 Advanced Technical Analysis | Native drawing tools, 60+ indicators, patter |
| SAU-041 Stock Comparison | Side-by-side multi-stock comparison with ove |
| SAU-043 Money Flow Tracking | Inflow/outflow breakdown by trade size |
| SAU-050 Chart Touch-and-Hold | Press-and-hold to reveal intra-day price at  |
| SAU-053 Chart Axis to Market Close | X-axis extends to close time for full sessio |
| SAU-054 Standard S&D Layout | Demand right / Supply left — market conventi |
| SAU-057 Watchlist Stocks | Main watchlist screen showing user's saved s |
| SAU-119 Minichart Component | Mini price chart component used in watchlist |

## Order management (16)
| Feature | Definition |
|---|---|
| SAU-029 Conditional Order Detail | Stop/trigger order view |
| SAU-030 Basket Order Detail | Group stock order management |
| SAU-031 Iceberg Order Detail | Slicing order view |
| SAU-035 Basket Order Create | Create basket with conditions |
| SAU-036 Order Filter Panel | Filter by status/type/market |
| SAU-037 Orders Empty State | Empty state when no orders |
| SAU-038 Level 2 Order Book | Market depth — active traders consider non-n |
| SAU-042 Conditional Orders | ARC has Figma only — competitors have full p |
| SAU-044 Quick Reorder | One-tap repeat previous trade — reduces fric |
| SAU-047 Bracket Order (OCO) | Combined stop-loss + take-profit in one orde |
| SAU-048 Chart Trading | Place orders directly on the price chart |
| SAU-060 Watchlist — Edit / Reorder | Edit watchlist: reorder, remove, or rename w |
| SAU-094 Holdings Filter Panel | Filter/sort holdings by criteria |
| SAU-105 Chain Order |  |
| SAU-114 Fast Order (No Confirm) | Quick order execution without confirmation d |
| SAU-120 List of Orders | Full list of all submitted orders with statu |

## Portfolio & holdings (13)
| Feature | Definition |
|---|---|
| SAU-021 P&L History (Sold Stocks) | Complete sold stocks P&L report |
| SAU-026 Tradable Rights | Huqooq available in portfolio |
| SAU-051 Auto-Watchlist on Buy | Owned stocks automatically added to watchlis |
| SAU-058 Watchlist — Story View | Story-style card view of watchlist stocks wi |
| SAU-074 Holdings Letter (PDF) | Authenticated PDF holdings report download |
| SAU-077 Saudi Portfolio Selector | Choose between multiple portfolios |
| SAU-078 Transfer Holdings | In-specie transfer between portfolios |
| SAU-080 Liquidate Holdings | Bulk liquidation flow |
| SAU-088 Analysis Dashboard | Top stocks, gains/losses, allocation analyti |
| SAU-089 Visual Asset Allocation | Granular live allocation breakdown by class |
| SAU-092 StoryTeller | Visual portfolio narratives (1,845 screens) |
| SAU-095 Sector/Index/Shariah Filters | Filter holdings by sector/index/Shariah |
| SAU-097 Batch Close Positions | Close multiple positions at once |

## Discovery & market data (14)
| Feature | Definition |
|---|---|
| SAU-045 Major Shareholder Data | Top shareholders of listed companies |
| SAU-064 Why Is It Moving | Screen highlighting stocks moving up in pric |
| SAU-066 Bulls vs Bears Screen | Market sentiment view: bulls vs bears for wa |
| SAU-068 Dividends Screen | Dividend information for stocks |
| SAU-069 Insider Trades Screen | Insider trading activity for stocks in watch |
| SAU-070 Government Trades Screen | Government/sovereign fund trading activity f |
| SAU-098 Auto Dividend Reinvest | Automatic dividend reinvestment option |
| SAU-107 Earnings Calendar | Calendar view of upcoming and past company e |
| SAU-110 ETF Exposure View | Detailed ETF profile page showing holdings,  |
| SAU-111 Whale / Institutional Tracking | Track large institutional and whale trades o |
| SAU-112 Unusual Activity Alerts | Alerts for unusual trading volume or price a |
| SAU-115 Dividends Screen | Dividend history, yield, and upcoming ex-dat |
| SAU-116 Dividends Screen | Dividend history, yield, and upcoming ex-dat |
| SAU-117 Earnings Calendar | Calendar view of upcoming and past company e |

## Products & trading (5)
| Feature | Definition |
|---|---|
| SAU-049 Saudi Options | Full native options trading flow |
| SAU-102 Rights Issue (Digital) | End-to-end digital rights subscription flow |
| SAU-108 Pre-Auction Trading | Trading during Tadawul opening and closing a |
| SAU-109 Fractional Shares | Buy fractional shares of Saudi-listed stocks |
| SAU-113 Futures Trading | Trading Saudi market futures and derivatives |

---

## Data-quality: duplicate feature rows (consolidate)
> Same feature entered multiple times — inflates the count and the gap. Merge to one row each.

- **Performance Chart** — SAU-075, SAU-118
- **Dividends Screen** — SAU-068, SAU-115, SAU-116
- **Earnings Calendar** — SAU-107, SAU-117

---

## Recommendation
- The 57 gaps cluster into ~5 families — scope **one BRD per capability cluster**, not per screen.
- **Priority:** Charting & technical analysis includes SAU-040 Advanced Technical Analysis (indicators/Ichimoku) — the same charting gap competitors (Sahm) are actively shipping. Highest competitive urgency.
- Consolidate the duplicate rows (Dividends x3, Earnings x2) before writing BRDs.

*Source: Features Map · 2026-08-10 · features_derived.json*
