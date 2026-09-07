# Journey-to-Feature Mapping
*5 core investor journeys mapped to 164 features · 2026-04-24*

> Each journey shows every feature a user touches from start to finish, ordered by the typical flow sequence. Features can appear in multiple journeys.

---

## Summary

| Journey | Features Touched | Live | Planned | Deepest Action (taps) |
|---|---|---|---|---|
| Onboarding | 23 | 5 | 18 | Complete KYC (9) |
| Saudi Market Trading | 42 | 8 | 34 | Place order (6) |
| US Market Trading | 32 | 5 | 27 | Buy/Sell US stock (7) |
| Portfolio Monitoring | 28 | 4 | 24 | Portfolio reports (5) |
| Wealth Visibility | 16 | 2 | 14 | Cash out US (6) |

**Cross-journey overlap:** 18 features appear in 2+ journeys (shared infrastructure)
**Journey-orphan features:** 23 features not part of any core journey (Corporate Actions, Engagement, Admin)

---

## Journey 1: Onboarding

*Goal: New user registers, completes KYC, and reaches the Home screen ready to invest.*

| Step | Feature # | Feature | Status | Taps from Start |
|---|---|---|---|---|
| 1 | 14 | Splash Screen & App Launch | Planned | 0 (auto) |
| 2 | 155 | Guest Mode (discovery before signup) | Planned | 1 |
| 3 | 156 | Tutorials | Planned | 1 |
| 4 | 15 | Login Screen | Planned | 1 |
| 5 | 1 | Digital Account Opening (Saudi Nationals) | Live | 2 |
| 6 | 16 | Add / Create Password | Planned | 3 |
| 7 | — | Nafath Identity Verification | Live (ext.) | 4 |
| 8 | 7 | FATCA / CRS KYC Indicia Update | Planned | 5 |
| 9 | 20 | KYC Confirmation / Message Screens | Planned | 6-9 |
| 10 | 17 | Face ID / Biometric Setup | Planned | 10 |
| 11 | 157 | First Engagement (post-signup activation) | Planned | 11 |
| 12 | 158 | Fast Onboarding (streamlined flow) | Planned | alt. path |
| | | **Variant flows:** | | |
| 13 | 2 | GCC Customer Onboarding | Planned | — |
| 14 | 3 | Family Onboarding (Non-Saudi / Non-ARB) | Planned | — |
| 15 | 4 | Expired ID Handling During Onboarding | Planned | — |
| 16 | 5 | GCC Customer ID Update (Existing Clients) | Planned | — |
| 17 | 6 | Foreign Customer Identity Verification | Planned | — |
| 18 | 8 | Minor Account Onboarding | Live | — |
| 19 | 9 | Minor Trading Restrictions | Planned | — |
| 20 | 10 | Guardian Trading on Behalf of Minor | Planned | — |
| 21 | 11 | IBKR International Brokerage Onboarding | Planned | — |
| 22 | 12 | Update National Address | Live | — |
| 23 | 13 | Session Upgrade & OTP Flow | Live | — |

**Journey health:** 5 of 23 features live (22%). Critical blocker: KYC is 9 taps with 87% drop-off. Fast Onboarding designed but not shipped.

---

## Journey 2: Saudi Market Trading

*Goal: Investor discovers a Saudi stock, researches it, places a trade, and manages the order.*

| Step | Feature # | Feature | Status | Taps from Home |
|---|---|---|---|---|
| **DISCOVER** | | | | |
| 1 | 161 | Market Home (Saudi) | Planned | 1 |
| 2 | 149 | Saudi Market Stock Profile (Enhanced) | Planned | 2 |
| 3 | 36 | Top Trending Stocks List | Planned | 2 |
| 4 | 46 | Stock Sector & Exchange Volatility | Planned | 2 |
| 5 | 150 | Stock/Sector/Exchange Liquidity | Unknown | 2 |
| 6 | 162 | Stock Stories | Planned | 2 |
| 7 | 141 | Ticker Chart Integration (TradingView) | Live | 3 |
| 8 | 77 | Analyst Ratings on Stocks | Planned | 3 |
| 9 | 140 | ARC News Screener | Planned | 3 |
| 10 | 35 | Tadawul News Push Notifications | Planned | — (push) |
| **TRADE** | | | | |
| 11 | 22 | Place Market Order (Saudi) | Live | 6 |
| 12 | 23 | Place Limit Order (Saudi) | Live | 6 |
| 13 | 24 | Market-on-Close (MOC) Order | Planned | 6 |
| 14 | 30 | Derivatives (Options) Trading | Planned | 6 |
| 15 | 56 | Basket Order — Create / Set Condition | Planned | 6 |
| 16 | 50 | Order Detail — Conditional Order | Planned | 5 |
| 17 | 51 | Order Detail — Basket Order | Planned | 5 |
| 18 | 52 | Order Detail — Slicing / Iceberg | Planned | 5 |
| 19 | 53 | Order Detail — Interval Order | Planned | 5 |
| 20 | 54 | Order Detail — Stop Loss | Planned | 5 |
| 21 | 55 | Order Detail — Take Profit | Planned | 5 |
| 22 | 57 | Order Filter Panel | Planned | 4 |
| 23 | 58 | Orders Empty State | Planned | 4 |
| 24 | 148 | View Commission Discount | Planned | 6 |
| 25 | 45 | TILA Subscription & Price Display | Live | — |
| **MARGIN & LENDING** | | | | |
| 26 | 25 | Apply for Margin Lending (Murabaha) | Live | — |
| 27 | 26 | Automated Margin Lending Approval | Planned | — |
| 28 | 27 | Margin Lending Contract Renewal | Planned | — |
| 29 | 28 | Margin Lending Early Payment | Planned | — |
| 30 | 29 | Margin Lending Full Integration (Commodities) | Planned | — |
| **SHORT SELLING & SBL** | | | | |
| 31 | 31 | Securities Borrowing & Lending | Planned | — |
| 32 | 32 | SBL Agreement & Suitability | Planned | — |
| 33 | 33 | Short Selling | Planned | — |
| **SETTLEMENT & ADMIN** | | | | |
| 34 | 44 | Instant Settlement (T+0 / T+1) | Planned | — |
| 35 | 34 | Tadawulaty Platform Access (SSO) | Planned | — |
| 36 | 42 | Block Codes Management (AML) | Live | — (admin) |
| 37 | 43 | Buying Power Swap (Local to Intl) | Planned | — |
| **FIGMA-ONLY** | | | | |
| 38 | 47 | Saudi Portfolio — Tradable Rights | Planned | — |
| 39 | 48 | Market Home — Tablet Layout | Planned | — |
| 40 | 49 | Orders — UAE Market Stocks List | Planned | — |
| 41 | 37 | Nomu (Parallel Market) Subscription | Live | — |
| 42 | 38 | Nomu IPO for Institutional Clients | Planned | — |

**Journey health:** 8 of 42 features live (19%). Most order types and market intelligence features are planned only.

---

## Journey 3: US Market Trading

*Goal: Investor discovers a US stock, researches it, places a trade, and manages the order.*

| Step | Feature # | Feature | Status | Taps from Home |
|---|---|---|---|---|
| **DISCOVER** | | | | |
| 1 | 161 | Market Home (US toggle) | Planned | 2 |
| 2 | 61 | US Market Stock Profile Page | Live | 3 |
| 3 | 66 | Trending Tickers (US Market) | Planned | 3 |
| 4 | 63 | Bulls vs. Bears Case Summary | Planned | 4 |
| 5 | 64 | Why Is It Moving — Stock Insights | Planned | 4 |
| 6 | 65 | Government Trading Data (Congress) | Planned | 4 |
| 7 | 141 | Ticker Chart Integration (TradingView) | Live | 3 |
| 8 | 77 | Analyst Ratings on Stocks | Planned | 3 |
| 9 | 140 | ARC News Screener | Planned | 3 |
| 10 | 78 | Earnings Calendar (International) | Planned | 3 |
| 11 | 139 | Economic Calendar (International) | Planned | 3 |
| 12 | 147 | International Indices Historical Data | Planned | 2 |
| **TRADE** | | | | |
| 13 | 59 | Place US Market Order | Live | 7 |
| 14 | 62 | International Options Page | Planned | 7 |
| 15 | 57 | Order Filter Panel | Planned | 4 |
| **ONBOARDING & SETUP** | | | | |
| 16 | 11 | IBKR International Brokerage Onboarding | Planned | — |
| 17 | 67 | Shariah Compliance Lists (Multi-Listing) | Live | — |
| 18 | 68 | US Market Settings | Planned | — |
| 19 | 142 | Ticker Chart — ARC Package Subscriptions | Planned | — |
| **PORTFOLIO** | | | | |
| 20 | 86 | US Portfolio — Choose Portfolio Selector | Planned | 3 |
| 21 | 39 | View Saudi Market Portfolio (P&L) | Planned | 3 |
| **FUNDING** | | | | |
| 22 | 43 | Buying Power Swap (Local to Intl) | Planned | — |
| 23 | 92 | Multi-Currency Wallet (UCM) | Planned | — |
| 24 | 93 | Multi Virtual IBANs | Planned | — |
| **CORPORATE ACTIONS** | | | | |
| 25 | 117 | Dividends Calendar (International) | Planned | 4 |
| 26 | 118 | Insider Trades Feed (International) | Planned | 4 |
| **CROSS-JOURNEY** | | | | |
| 27 | 60 | US Market Stock Search (Enhanced) | Planned | 2 |
| 28 | 163 | Fund Recommender | Planned | 3 |
| 29 | 144 | Mada / Credit Card 3D Secure | Planned | — |
| 30 | 145 | Mada / Credit Card Transaction Limits | Planned | — |
| 31 | 146 | Cash-Out Enhancements (GCC) | Planned | — |
| 32 | 164 | Saudi Options (native flow) | Planned | — |

**Journey health:** 5 of 32 features live (16%). Weakest journey — most intelligence and research features are planned.

---

## Journey 4: Portfolio Monitoring

*Goal: Investor checks portfolio value, reviews holdings, analyzes performance, and generates reports.*

| Step | Feature # | Feature | Status | Taps from Home |
|---|---|---|---|---|
| **VIEW** | | | | |
| 1 | 69 | View Saudi Market Portfolio Holdings | Live | 2 |
| 2 | 70 | View Saudi Market Portfolio Performance Chart | Planned | 3 |
| 3 | 39 | View Saudi Market Portfolio P&L | Planned | 3 |
| 4 | 40 | View Overall P&L History (Sold Stocks) | Planned | 4 |
| 5 | 41 | Update Average Cost Price | Planned | 4 |
| 6 | 81 | Saudi Portfolio — Choose Portfolio Selector | Planned | 2 |
| 7 | 82 | Sectors / Index / Shariah Filter Panels | Planned | 3 |
| 8 | 86 | US Portfolio — Choose Portfolio Selector | Planned | 2 |
| **MANAGE** | | | | |
| 9 | 83 | Saudi Portfolio — Transfer Holdings | Planned | 4 |
| 10 | 84 | Saudi Portfolio — Add Holdings to Watchlist | Planned | 3 |
| 11 | 85 | Saudi Portfolio — Liquidate Holdings Flow | Planned | 4 |
| 12 | 47 | Saudi Portfolio — Tradable Rights | Planned | 3 |
| **ANALYZE** | | | | |
| 13 | 87 | Portfolio Analysis Dashboard | Planned | 4 |
| 14 | 71 | Peer Portfolio Comparison | Planned | 5 |
| 15 | 72 | Portfolio Insights | Planned | 4 |
| 16 | 73 | Portfolio Health Score | Planned | 4 |
| 17 | 74 | Investment Allocation Tracker | Planned | 4 |
| 18 | 75 | Goal Tracker | Planned | 4 |
| 19 | 159 | Digital StoryTeller (portfolio narratives) | Planned | 4 |
| **REPORT** | | | | |
| 20 | 76 | Storyteller (Quarterly Performance Report) | Planned | 5 |
| 21 | 79 | Customer Investment Holdings Letter (PDF) | Live | 5 |
| 22 | 88 | Portfolio Reports (Downloadable) | Planned | 5 |
| **SETTINGS** | | | | |
| 23 | 89 | Portfolio Preference Settings | Planned | 3 |
| **CROSS-PRODUCT** | | | | |
| 24 | 99 | Mutual Fund Portfolio Performance Chart | Planned | 4 |
| 25 | 109 | Mashura (Robo) Reports | Planned | 4 |
| 26 | 134 | Crowdfund Portfolios Home | Planned | 3 |
| 27 | 80 | Stock Holdings Filter Panel | Planned | 3 |
| 28 | 21 | Home — Family Members Overview | Planned | 2 |

**Journey health:** 4 of 28 features live (14%). Portfolio is designed extensively in Figma but almost nothing is live beyond basic holdings view.

---

## Journey 5: Wealth Visibility

*Goal: Investor views total wealth, manages cash, funds accounts, and tracks across all products.*

| Step | Feature # | Feature | Status | Taps from Home |
|---|---|---|---|---|
| **VIEW** | | | | |
| 1 | 90 | View Total Cash & Buying Power (Aggregated) | Planned | 1 |
| 2 | 92 | Multi-Currency Wallet (UCM) | Planned | 2 |
| 3 | 93 | Multi Virtual IBANs | Planned | 3 |
| **FUND** | | | | |
| 4 | 91 | Cash-In from ARB Account | Live | 5 |
| 5 | 146 | Cash-Out Enhancements (GCC) | Planned | 5 |
| 6 | 144 | Mada / Credit Card 3D Secure | Planned | 5 |
| 7 | 145 | Mada / Credit Card Transaction Limits | Planned | — |
| 8 | 43 | Buying Power Swap (Local to Intl) | Planned | 4 |
| **INVEST PRODUCTS** | | | | |
| 9 | 95 | Subscribe to Mutual Fund (SAR) | Live | 7 |
| 10 | 96 | Subscribe to USD Mutual Fund | Planned | 7 |
| 11 | 107 | Create Robo Portfolio | Planned | 7 |
| 12 | 110 | Subscribe to Main Market IPO | Live | 6 |
| 13 | 126 | Buy Transaction Round-Up | Planned | — |
| **TRACK** | | | | |
| 14 | 94 | Wallet Transaction Invoices (ZATCA) | Planned | — |
| 15 | 74 | Investment Allocation Tracker | Planned | 4 |
| 16 | 137 | Zakat Calculator | Live | — |

**Journey health:** 4 of 16 features live (25%). Best ratio of all journeys, but aggregated wealth view (the #1 need) is still planned.

---

## Cross-Journey Feature Overlap

Features that appear in 2+ journeys (shared infrastructure):

| Feature # | Feature | Journeys |
|---|---|---|
| 11 | IBKR Onboarding | Onboarding, US Trading |
| 13 | Session Upgrade & OTP | Onboarding, All trading |
| 43 | Buying Power Swap | Saudi Trading, US Trading, Wealth |
| 57 | Order Filter Panel | Saudi Trading, US Trading |
| 74 | Investment Allocation Tracker | Portfolio, Wealth |
| 77 | Analyst Ratings | Saudi Trading, US Trading |
| 86 | US Portfolio Selector | US Trading, Portfolio |
| 92 | Multi-Currency Wallet (UCM) | US Trading, Wealth |
| 93 | Multi Virtual IBANs | US Trading, Wealth |
| 139 | Economic Calendar | US Trading, Cross |
| 140 | ARC News Screener | Saudi Trading, US Trading |
| 141 | Ticker Chart | Saudi Trading, US Trading |
| 144 | Mada 3D Secure | US Trading, Wealth |
| 145 | Mada Transaction Limits | US Trading, Wealth |
| 146 | Cash-Out GCC | US Trading, Wealth |

---

## Journey-Orphan Features (not in any core journey)

23 features that don't belong to any of the 5 core journeys:

| Feature # | Feature | Squad |
|---|---|---|
| 42 | Block Codes Management (AML) | Saudi Trading (admin) |
| 100 | MF Dividend History | Mutual Funds |
| 101 | MF Segregated by Asset Class | Mutual Funds |
| 102 | Fund Historical Performance View | Mutual Funds |
| 103 | Show MF Buy Orders as Blocked | Mutual Funds |
| 104 | Margin Lending on MF (Collateral) | Mutual Funds |
| 105 | MF Switch Funds Flow | Mutual Funds |
| 108 | Robo Portfolio Cash Withdrawal | Robo Advisory |
| 112 | Subscribe to Nomu IPO | IPOs |
| 113 | Nomu IPO for Institutional | IPOs |
| 114 | Auto-Subscribe Plan | IPOs |
| 115 | Qualified Client Verification | IPOs |
| 116 | Discover Home | IPOs |
| 119 | Purification Calculator | Corporate Actions |
| 120 | Stocks Dividend Calculator | Corporate Actions |
| 121-135 | Investor Engagement features (15) | Engagement |
| 138 | Purification ZATCA Invoice | Cross-Journey |
| 151-154 | Profile & Settings features (4) | Cross-Journey |

---

*Source: Features inventory (164 features) + Figma screen flows (8 files) + depth analysis (36 key actions).*
*Note: Feature numbers 155-164 refer to the 10 new discoveries from deep Figma extraction (see inventory update).*
