# ARC Features Inventory
*Extracted from BRDs + Figma (Unreleased Revamp) — Updated 2026-04-24*
*Total features: 164 (112 from BRDs, 42 Figma-only, 10 deep-extraction discoveries)*

---

## Summary by Squad

| Squad | Live | Planned | Unknown | Figma Confirmed | Figma-Only | Total |
|---|---|---|---|---|---|---|
| Onboarding | 4 | 9 | 0 | 12 | 8 | 21 |
| Saudi Trading | 6 | 19 | 0 | 7 | 12 | 37 |
| US Trading | 3 | 6 | 0 | 3 | 1 | 10 |
| Portfolio Monitoring | 2 | 9 | 0 | 7 | 10 | 21 |
| Wealth Visibility | 1 | 4 | 0 | 1 | 0 | 5 |
| Mutual Funds | 1 | 9 | 0 | 4 | 1 | 11 |
| Robo Advisory | 1 | 2 | 0 | 3 | 1 | 4 |
| IPOs | 2 | 4 | 0 | 3 | 1 | 7 |
| Corporate Actions | 0 | 3 | 0 | 1 | 1 | 4 |
| Investor Engagement | 2 | 10 | 0 | 1 | 3 | 15 |
| Cross-Journey | 2 | 12 | 1 | 2 | 4 | 19 |
| Deep Extraction Discoveries | 0 | 10 | 0 | 0 | 10 | 10 |
| **Total** | **24** | **97** | **1** | **44** | **52** | **164** |

---

## Feature List

---

### Onboarding

| # | Feature | Description | Status | Source | BRD Ref |
|---|---|---|---|---|---|
| 1 | Digital Account Opening (Saudi Nationals) | Standard onboarding journey for Saudi nationals to create an ARC investment account via SuperApp or SuperWeb. | Live | BRD + Figma (OnBoarding KYC) | ARCD-47480 |
| 2 | GCC Customer Onboarding | Onboarding flow for GCC clients (non-Saudi Gulf nationals) with real-time identity document verification and face verification via third-party integration. | Planned | BRD + Figma (OnBoarding KYC) | ARCD-47480 |
| 3 | Family Onboarding (Non-Saudi / Non-ARB) | Enables ARC customers to digitally onboard non-Saudi and non-ARB family members, with integrated KYC and identity verification. | Planned | BRD + Figma (OnBoarding KYC) | ARCD-26191 |
| 4 | Expired ID Handling During Onboarding | Automated workflow that detects expired national IDs at onboarding initiation and routes clients through a document renewal sub-flow instead of blocking them. | Planned | BRD + Figma (OnBoarding KYC) | ARCD-73474 |
| 5 | GCC Customer ID Update (Existing Clients) | Dedicated workflow for existing GCC clients to update or renew their expired identification documents through digital channels. | Planned | BRD + Figma (OnBoarding KYC) | ARCD-47480 |
| 6 | Foreign Customer Identity Verification | Real-time identity document verification and face scan for non-Saudi, non-GCC (foreign) customers during onboarding, with third-party provider integration. | Planned | BRD + Figma (OnBoarding KYC) | ARCD-79680 |
| 7 | FATCA / CRS KYC Indicia Update | Allows existing clients to update their FATCA and CRS tax indicia, including TIN validation, to maintain regulatory compliance. | Planned | BRD + Figma (OnBoarding KYC) | ARCD-58762, ARCD 58733 |
| 8 | Minor Account Onboarding | Guardian-initiated onboarding flow to create investment accounts for minor children under the guardian's supervision. | Live | BRD + Figma (OnBoarding KYC) | ARCD 45978 |
| 9 | Minor Trading Restrictions (Custodian Controls) | Empowers guardians to configure trade amount limits, trade count caps, withdrawal limits, product access, and sector restrictions on minor accounts. | Planned | BRD | ARCD 45978 |
| 10 | Guardian Trading on Behalf of Minor | Enables a guardian customer to execute trades on behalf of their linked minor's portfolio directly from the SuperApp. | Planned | BRD + Figma (OnBoarding KYC) | Business Requirements for Guardian Trade |
| 11 | IBKR International Brokerage Onboarding | Onboarding flow to create and activate an International Brokerage account backed by Interactive Brokers (IBKR) as the new backend provider. | Planned | BRD + Figma (OnBoarding KYC) | ARCD-70106 |
| 12 | Update National Address | Self-service flow for clients to update their registered national address through SuperApp or SuperWeb. | Live | BRD + Figma (OnBoarding KYC) | ARCD-14242 |
| 13 | Session Upgrade & OTP Flow Enhancement | One-time session upgrade that allows clients to perform multiple high-value actions without repeated verification prompts in a single session. | Live | BRD + Figma (OnBoarding KYC) | ARCD-84906 |
| 14 | Splash Screen & App Launch | Initial app splash screen shown on launch before authentication. | Planned | Figma (OnBoarding KYC) | — |
| 15 | Login Screen | Username/password login entry screen for existing clients. | Planned | Figma (OnBoarding KYC) | — |
| 16 | Add / Create Password | Screen for new clients to set up their account password during onboarding. | Planned | Figma (OnBoarding KYC) | — |
| 17 | Face ID / Biometric Setup | Setup screens for Face ID authentication (3-step flow). | Planned | Figma (OnBoarding KYC) | — |
| 18 | Change Password | Self-service flow for clients to update their account password. | Planned | Figma (OnBoarding KYC) | — |
| 19 | Non-ARB Bank Account Info Entry | Screen to capture external bank account details for clients without an ARB account. | Planned | Figma (OnBoarding KYC) | — |
| 20 | KYC Confirmation / Message Screens | Success, error, and informational modal screens across the KYC and onboarding flow. | Planned | Figma (OnBoarding KYC) | — |
| 21 | Home — Family Members Overview | Screen showing all linked family member accounts accessible from the home screen. | Planned | Figma (Home) | — |

---

### Saudi Trading

| # | Feature | Description | Status | Source | BRD Ref |
|---|---|---|---|---|---|
| 22 | Place Market Order (Saudi Market) | Enables clients to place a buy or sell market order for Saudi Exchange (Tadawul) listed stocks via SuperApp or SuperWeb. | Live | BRD + Figma (Tradepad) | ARCD-14312, ARCD-1553 |
| 23 | Place Limit Order (Saudi Market) | Enables clients to place a limit buy or sell order at a specified price for Saudi market stocks. | Live | BRD + Figma (Tradepad) | ARCD-1553 |
| 24 | Market-on-Close (MOC) Order | Conditional order type that executes at the Saudi market's official closing price during the Trade at Last session. | Planned | BRD | ARCD_9245 |
| 25 | Apply for Margin Lending (Murabaha) via SuperApp | Digital application flow for Murabaha margin lending (financing for share purchases) directly through the SuperApp. | Live | BRD | ARCD-1634 |
| 26 | Automated Margin Lending Approval | Automates Compliance and Risk department approvals for margin lending applications based on pre-defined eligibility conditions. | Planned | BRD | ARCD 1923 |
| 27 | Margin Lending Contract Renewal | Digital flow for renewing an existing Murabaha margin lending contract at maturity, triggered by push notification and in-app prompts. | Planned | BRD | ARCD-2367 |
| 28 | Margin Lending Early Payment | Allows clients to make early partial or full repayment on an active Murabaha margin lending contract through digital channels. | Planned | BRD | ARCD-2367 |
| 29 | Margin Lending Full Integration Phase 2 (Commodities) | Integrates commodity contractor buy/sell execution and digital promissory notes into the Murabaha lending process. | Planned | BRD | ARCD-2424 |
| 30 | Derivatives (Options) Trading | Full options trading capability on Saudi Exchange (DOTS system), including order placement, suitability, lifecycle management, and invoicing. | Planned | BRD + Figma (Orders) | ARCD-1983 |
| 31 | Securities Borrowing & Lending (SBL) Program | Enables eligible clients to lend their listed shares to earn yield or borrow shares to short sell. | Planned | BRD | ARCD-53753 |
| 32 | SBL Agreement & Suitability Digital Acceptance | Digital enrollment flow for whitelisted clients to accept the Securities Lending agreement and complete suitability questions. | Planned | BRD | ARCD-86486 |
| 33 | Short Selling | Allows eligible clients to sell borrowed securities short in the Saudi market, with integrated SBL framework and margin controls. | Planned | BRD | ARCD-53753 |
| 34 | Tadawulaty Platform Access (Single Sign-On) | Enables clients to access Edaa's Tadawulaty platform directly from within the SuperApp without a separate login. | Planned | BRD | ARCD-22970 |
| 35 | Tadawul News Push Notifications | Sends real-time Tadawul market news as push notifications to clients via the SuperApp. | Planned | BRD | ARCD-39221 |
| 36 | Top Trending (Heated) Stocks List | Displays a dynamic, hourly-updated list of the top 20–30 most-searched and most-viewed stocks in the Saudi market. | Planned | BRD | ARCD-41012 |
| 37 | Nomu (Parallel Market) Subscription | Enables eligible clients to apply for parallel market (Nomu) subscriptions directly through the SuperApp. | Live | BRD + Figma (Discover (IPO, Subscription Engine)) | ARCD-1922 |
| 38 | Nomu IPO Subscription for Institutional Clients | Allows institutional ARC customers to subscribe to Nomu market IPOs via the SuperApp. | Planned | BRD + Figma (Discover (IPO, Subscription Engine)) | ARCD-47866 |
| 39 | View Saudi Market Portfolio Performance (P&L) | Shows clients a historical P&L performance chart for their Saudi market portfolio and individual holdings. | Planned | BRD + Figma (Portfolios) | ARCD-2654 |
| 40 | View Overall P&L History for Local Stocks (Sold) | Provides a comprehensive historical profit and loss report for all Saudi market stocks sold by the client. | Planned | BRD | ARCD 60444 |
| 41 | Update Average Cost Price | Allows clients to manually update the average cost price of a Saudi market holding to reflect accurate valuation and P&L calculations. | Planned | BRD | ARCD-2650 |
| 42 | Block Codes Management (AML) | Back-office and admin tool to create, assign, update, and remove AML-related trading block codes on customer accounts. | Live | BRD | ARCD-2792 |
| 43 | Buying Power Swap (Local to International) | Allows clients to use their Saudi market buying power to fund international brokerage orders, and vice versa. | Planned | BRD | ARCD-2644 |
| 44 | Instant Settlement (T+0 / T+1) | Gives clients the option to receive sale proceeds from Saudi market securities instantly (T+0) or next business day (T+1) rather than waiting for standard T+2 settlement. | Planned | BRD + Figma (Portfolios) | ARCD-14352 |
| 45 | TILA Subscription & Price Display | Manages the Tadawul Information License Agreement subscription for clients and controls whether real-time or delayed prices are displayed. | Live | BRD | ARCD-2933 |
| 46 | View Stock Sector & Exchange Volatility | Displays historical volatility indicators for individual stocks, sectors, and the exchange across daily, weekly, monthly, and yearly timeframes. | Planned | BRD | ARCD-58777 |
| 47 | Saudi Portfolio — Tradable Rights Screen | Screen displaying tradable rights (huqooq) available for the client's portfolio. | Planned | Figma (Portfolios) | — |
| 48 | Market Home — Tablet Layout | Tablet-optimised market overview layout. | Planned | Figma (Market) | — |
| 49 | Orders — UAE Market Stocks List | Order history and active orders for UAE market stock orders. | Planned | Figma (Orders) | — |
| 50 | Order Detail — Conditional Order | Full detail view of an active or executed conditional (stop/trigger) order. | Planned | Figma (Orders) | — |
| 51 | Order Detail — Basket Order | Full detail and management screen for basket orders (group of stocks). | Planned | Figma (Orders) | — |
| 52 | Order Detail — Slicing / Iceberg Order | Full detail view for iceberg/slicing order type. | Planned | Figma (Orders) | — |
| 53 | Order Detail — Interval Order | Full detail view for interval (scheduled) order type. | Planned | Figma (Orders) | — |
| 54 | Order Detail — Stop Loss Order | Full detail view of an active stop loss order. | Planned | Figma (Orders) | — |
| 55 | Order Detail — Take Profit Order | Full detail view of an active take profit order. | Planned | Figma (Orders) | — |
| 56 | Basket Order — Create / Set Condition Screen | Screen for creating a new basket order and defining its execution conditions. | Planned | Figma (Orders) | — |
| 57 | Order Filter Panel | Filter and sort panel for the orders list (by status, type, market). | Planned | Figma (Orders) | — |
| 58 | Orders Empty State Screen | Empty state screen shown when no orders exist. | Planned | Figma (Orders) | — |

---

### US Trading

| # | Feature | Description | Status | Source | BRD Ref |
|---|---|---|---|---|---|
| 59 | Place US Market Order | Enables clients to place buy or sell orders for US-listed stocks (NYSE, NASDAQ, etc.) through the SuperApp or SuperWeb. | Live | BRD + Figma (Orders) | ARCD-70106, ARCD-14312 |
| 60 | US Market Stock Search & Listing (Enhanced) | Improved search experience for US stocks across all indices — clients can search by ticker symbol or company name in Arabic or English. | Planned | BRD | ARCD-50707 |
| 61 | US Market Stock Profile Page | Detailed stock information page for US-listed stocks including financials, key metrics, news, and analyst data. | Live | BRD + Figma (Market) | ARCD-14312 |
| 62 | International Options Page (US Stocks) | Consolidated options chain view for US market stocks, showing Greeks, theoretical values, and market data. | Planned | BRD + Figma (Orders) | ARCD-72350 |
| 63 | Bulls vs. Bears Case Summary (US Stocks) | Displays concise bullish and bearish case summaries for each US stock, sourced from Benzinga. | Planned | BRD | ARCD-61067 |
| 64 | Why Is It Moving — Stock Insights | Provides real-time AI-driven explanations of why a US stock price is moving up or down. | Planned | BRD | ARCD-60875 |
| 65 | Government Trading Data (US Congress Disclosures) | Shows clients real-time US congressional stock trading disclosures via Benzinga. | Planned | BRD | ARCD-72957 |
| 66 | Trending Tickers (US Market) | Displays a list of US stocks gaining or losing retail investor attention based on high-frequency Benzinga page-view data. | Planned | BRD | ARCD-72979 |
| 67 | Shariah Compliance Lists (Multi-Listing) | Allows clients to select and apply either the General Shariah list or the ARC-specific Shariah list to filter stocks. | Live | BRD | ARCD-2067 |
| 68 | US Market Settings | Configuration screen for US market-specific settings and preferences. | Planned | Figma (Profile & Setting) | — |

---

### Portfolio Monitoring

| # | Feature | Description | Status | Source | BRD Ref |
|---|---|---|---|---|---|
| 69 | View Saudi Market Portfolio Holdings | Displays current Saudi market portfolio holdings, quantities, average cost, current value, and unrealized P&L for each stock. | Live | BRD + Figma (Portfolios) | ARCD-2654 |
| 70 | View Saudi Market Portfolio Performance Chart | Shows a graphical performance chart of the Saudi market portfolio over selectable time periods. | Planned | BRD + Figma (Portfolios) | ARCD-2654 |
| 71 | Peer Portfolio Comparison | Benchmarks the client's Saudi market portfolio P&L percentage against anonymized peers in the same investor segment. | Planned | BRD + Figma (Portfolios) | ARCD-60816 |
| 72 | Portfolio Insights | Provides clients with insights into their own portfolio including diversification analysis, concentration alerts, sector breakdown, and performance relative to market. | Planned | BRD + Figma (Portfolios) | ARCD-60816 |
| 73 | Portfolio Health Score | Calculates and displays an overall health score for the client's portfolio based on diversification, risk, and performance metrics. | Planned | BRD + Figma (Portfolios) | ARCD 52378 |
| 74 | Investment Allocation Tracker | Enables clients to define and monitor target allocation percentages across Saudi Market, US Market, Investment Funds, and Cash. | Planned | BRD | ARCD-61176 |
| 75 | Goal Tracker | Allows clients to define financial investment goals, link specific assets from their portfolios, and monitor real-time progress toward each goal. | Planned | BRD | ARCD 55733 |
| 76 | Storyteller (Quarterly Performance Report) | Generates a personalized, narrative-driven quarterly investment performance overview for the client. | Planned | BRD + Figma (Portfolios) | ARCD 19542 |
| 77 | Analyst Ratings on Stocks | Shows clients real-time stock ratings from verified analyst firms, including recommendation type, price target, date, and action. | Planned | BRD | ARCD-60979 |
| 78 | Earnings Calendar (International) | Provides a centralized view of upcoming and past company earnings announcements within the International product section. | Planned | BRD | ARCD - Earnings Calendar |
| 79 | Customer Investment Holdings Letter (Authenticated PDF) | Enables clients to generate and download an authenticated PDF report of all their current ARC holdings across products. | Live | BRD + Figma (Portfolios) | Customer Investment Holdings Letter BRD |
| 80 | Stock Holdings Filter Panel | Filter panel for sorting and filtering stock holdings by various criteria. | Planned | Figma (Discover (IPO, Subscription Engine)) | — |
| 81 | Saudi Portfolio — Choose Portfolio Selector | Portfolio selector screen when client has multiple Saudi market portfolios. | Planned | Figma (Portfolios) | — |
| 82 | Saudi Portfolio — Sectors / Index / Shariah Filter Panels | Filter panels for sorting portfolio holdings by sector, index membership, or Shariah compliance. | Planned | Figma (Portfolios) | — |
| 83 | Saudi Portfolio — Transfer Holdings | Screen to initiate an in-specie transfer of holdings between portfolios. | Planned | Figma (Portfolios) | — |
| 84 | Saudi Portfolio — Add Holdings to Watchlist | Quick-add flow to add a held stock to the client's watchlist from the portfolio. | Planned | Figma (Portfolios) | — |
| 85 | Saudi Portfolio — Liquidate Holdings Flow | Bulk liquidation flow for closing out positions in the Saudi portfolio. | Planned | Figma (Portfolios) | — |
| 86 | US Portfolio — Choose Portfolio Selector | Portfolio selector screen when client has multiple US market portfolios. | Planned | Figma (Portfolios) | — |
| 87 | Portfolio Analysis Dashboard | Analytics hub showing top stocks, gains/losses, allocation, and trading activity. | Planned | Figma (Portfolios) | — |
| 88 | Portfolio Reports (Downloadable) | Downloadable and viewable portfolio performance reports with filter controls. | Planned | Figma (Portfolios) | — |
| 89 | Portfolio Preference Settings | Display preference settings for portfolio view (grouping, default sort, etc.). | Planned | Figma (Profile & Setting) | — |

---

### Wealth Visibility

| # | Feature | Description | Status | Source | BRD Ref |
|---|---|---|---|---|---|
| 90 | View Total Cash & Buying Power (Aggregated) | Displays a consolidated view of total available cash and buying power across all ARC portfolios and wallets. | Planned | BRD | ARCD-72218 |
| 91 | Cash-In from ARB Account to Portfolio | Allows clients to transfer funds from any linked Al Rajhi Bank current account to their local brokerage, mutual fund, or UCM wallet. | Live | BRD + Figma (Tradepad) | ARCD-2651 |
| 92 | Multi-Currency Wallet (UCM) Enhancements | Enhances the UCM multi-currency wallet to support additional currencies, improved balance display, and streamlined transfer flows. | Planned | BRD | ARCD-72195 |
| 93 | Multi Virtual IBANs | Assigns unique Virtual IBANs to each client portfolio and UCM wallet so that incoming wire transfers are automatically routed to the correct destination. | Planned | BRD | ARCD-72196 |
| 94 | Wallet Transaction Invoices (ZATCA-Compliant) | Automatically generates ZATCA-compliant electronic invoices for all wallet transactions. | Planned | BRD | ARCD - ARC UCM Wallet Transactions Invoices |

---

### Mutual Funds

| # | Feature | Description | Status | Source | BRD Ref |
|---|---|---|---|---|---|
| 95 | Subscribe to Mutual Fund (SAR Portfolio) | Allows clients to subscribe to ARC's SAR-denominated mutual funds through the SuperApp, including portfolio creation and cash-in. | Live | BRD + Figma (Portfolios) | ARCD-47782 |
| 96 | Subscribe to USD Mutual Fund Using SAR Account | Enables clients to subscribe to USD-denominated mutual funds using their SAR current accounts, with an automated FX conversion. | Planned | BRD + Figma (Portfolios) | ARCD-32980 |
| 97 | Redeem / Cancel Mutual Fund Subscription Order | Allows clients to cancel a pending mutual fund subscription or redemption order before it is processed. | Planned | BRD + Figma (Orders) | Cancel Subscription Redemption Order BRD |
| 98 | Cancel Mutual Fund Portfolio (SAR/USD) | Enables clients to fully cancel and close an active SAR or USD mutual fund portfolio. | Planned | BRD | Cancel Portfolio Investment Funds BRD |
| 99 | Mutual Fund Portfolio Performance Chart | Displays an investment performance chart for the client's mutual fund portfolio over selectable time periods. | Planned | BRD + Figma (Portfolios) | ARCD-47782 |
| 100 | Mutual Fund Dividend History & Total Dividends | Shows clients a complete dividend history and cumulative total dividends received for each fund held in their portfolio. | Planned | BRD | ARCD-47782 |
| 101 | Mutual Funds Segregated by Asset Class | Organizes the mutual fund catalog by asset class (equity, money market, sukuk, etc.) to improve fund discovery and selection. | Planned | BRD | ARCD-47782 |
| 102 | Fund Historical Performance View | Displays the historical performance chart of a mutual fund available for subscription, allowing comparison across time periods. | Planned | BRD | ARCD-47782 |
| 103 | Show Mutual Fund Buy Orders as Blocked Amounts | Displays the cash value of pending mutual fund buy orders as blocked amounts in the portfolio cash overview. | Planned | BRD | ARCD-48329 |
| 104 | Margin Lending on Mutual Funds (Collateral) | Allows clients to include their mutual fund units as eligible collateral when applying for a Murabaha margin lending product. | Planned | BRD | ARCD-8609 |
| 105 | Mutual Fund Portfolio — Switch Funds Flow | Multi-step flow for switching between mutual fund products within the portfolio. | Planned | Figma (Portfolios) | — |

---

### Robo Advisory

| # | Feature | Description | Status | Source | BRD Ref |
|---|---|---|---|---|---|
| 106 | Robo Advisory Onboarding | New-client onboarding flow for the Robo Advisory product, including suitability questions and risk profile assessment. | Live | BRD + Figma (Portfolios) | ARCD-74031 |
| 107 | Create Robo Portfolio & Investment Risk Profile | Allows clients to create a new Robo Advisory portfolio and assign or update their investment risk profile. | Planned | BRD + Figma (Portfolios) | ARCD-74031 |
| 108 | Robo Portfolio Cash Withdrawal | Enables Robo Advisory clients to withdraw cash from their Robo portfolio through a native digital flow. | Planned | BRD + Figma (Portfolios) | ARCD-74031 |
| 109 | Mashura (Robo Advisory) Reports | Reporting screens specific to the Robo Advisory (Mashura) product. | Planned | Figma (Portfolios) | — |

---

### IPOs

| # | Feature | Description | Status | Source | BRD Ref |
|---|---|---|---|---|---|
| 110 | Subscribe to Main Market IPO | Allows clients to apply for an IPO subscription on the Saudi Exchange main market directly through the SuperApp or SuperWeb. | Live | BRD + Figma (Discover (IPO, Subscription Engine)) | ARCD-1594 |
| 111 | View IPO Details & Subscription Status | Displays upcoming and active IPO listings with details and shows the client's current subscription status. | Live | BRD + Figma (Discover (IPO, Subscription Engine)) | ARCD-1594 |
| 112 | Subscribe to Nomu (Parallel Market) IPO | Enables eligible clients to subscribe to IPOs listed on the Nomu parallel market from within the SuperApp. | Planned | BRD | ARCD-1922 |
| 113 | Nomu IPO Subscription for Institutional Clients | Allows ARC institutional customers to submit IPO subscription requests for Nomu market listings via the SuperApp. | Planned | BRD | ARCD-47866 |
| 114 | Auto-Subscribe Plan (Subscription Engine) | Enables clients to create recurring automated subscription plans across mutual funds, Saudi market stocks, and Robo portfolios. | Planned | BRD + Figma (Discover (IPO, Subscription Engine)) | ARCD-2632 |
| 115 | Qualified Client Verification for Private Fund IPOs | Enforces CMA-mandated eligibility checks for qualified clients subscribing to restricted funds during IPO periods. | Planned | BRD | ARCD-22937 |
| 116 | Discover Home | Main Discover section landing page showing IPOs, subscriptions, and investment opportunities. | Planned | Figma (Discover (IPO, Subscription Engine)) | — |

---

### Corporate Actions

| # | Feature | Description | Status | Source | BRD Ref |
|---|---|---|---|---|---|
| 117 | Dividends Calendar (International) | Provides a financial calendar view of upcoming and past dividend announcements and payment amounts for international stocks. | Planned | BRD + Figma (Discover (IPO, Subscription Engine)) | ARCD- 72987 |
| 118 | Insider Trades Feed (International) | Displays executive-level insider trading disclosures for international companies. | Planned | BRD | ARCD-68490 |
| 119 | Purification Calculator | Allows clients to subscribe to the Purification Calculator service and calculate their Sharia-required purification amount. | Planned | BRD | ARCD-1096 |
| 120 | Stocks Dividend Calculator | Interactive calculator allowing clients to estimate dividend income from their stock holdings. | Planned | Figma (Discover (IPO, Subscription Engine)) | — |

---

### Investor Engagement

| # | Feature | Description | Status | Source | BRD Ref |
|---|---|---|---|---|---|
| 121 | Spin the Wheel for Discounts | Gamified reward feature that gives clients a chance to win commission discounts or investment bonuses after reaching trading milestones. | Planned | BRD | ARCD-16056 |
| 122 | Prepaid Commission Bundle (Commission-Free Trading) | Allows clients to subscribe to a prepaid commission-free trading bundle for a defined period. | Planned | BRD | ARCD-17031 |
| 123 | Bundle Benefits (ARG Group Bundle Engine) | Displays and activates Al Rajhi Group bundle benefits — including brokerage fee discounts — that clients are eligible for. | Live | BRD | ARCD 18697 |
| 124 | Mokafaa Loyalty Points Redemption | Allows clients to redeem their Al Rajhi Mokafaa loyalty points as cash and directly fund any supported ARC investment portfolio. | Planned | BRD | ARCD 67739 |
| 125 | ARC Debit Card | Provides clients with an ARC-branded debit card linked to their UCM wallet. | Planned | BRD | ARCD 72647 |
| 126 | Buy Transaction Round-Up | Automatically rounds up the value of each buy transaction to the nearest defined amount and invests the spare change. | Planned | BRD | ARCD 73671 |
| 127 | Social Trading (Follow & Copy Traders) | Enables clients to discover, follow, and manually replicate trading strategies of selected professional traders. | Planned | BRD | ARCD-72352 |
| 128 | Smart Saving Plan (Bulk Orders via ARB) | Processes bulk deposit and subscription orders received from ARB into ARC mutual fund portfolios in a batch/offline execution mode. | Live | BRD | BRD - Smart Saving Plan |
| 129 | Gifting List with Date Selection | Back-office tool for the operations team to generate a gifting list within the UCM system with a selectable date range. | Planned | BRD | ARCD-42865 |
| 130 | Investment Referral / Date-Based Gift Campaigns | Allows the UCM operations team to configure and deliver date-specific gift campaigns to targeted client segments. | Planned | BRD | ARCD-42865 |
| 131 | Preferred Language for Notifications | Allows clients to select their preferred language (Arabic or English) for all notifications related to Asset Management, International Brokerage, and Crowd Investing products. | Planned | BRD + Figma (Profile & Setting) | ARCD - 37611 |
| 132 | Email Notification Templates Revamp | Redesigned email notification templates for all SuperApp/SuperWeb-triggered events. | Planned | BRD | ARCD 20124 |
| 133 | Charity Investment / Donation Screen | Screen for charity donation or investment product offerings within the Discover section. | Planned | Figma (Discover (IPO, Subscription Engine)) | — |
| 134 | Crowdfund Portfolios Home | Portfolio view for crowd investment (crowdfunding) products. | Planned | Figma (Portfolios) | — |
| 135 | Orders — Crowd Funds List | Order history for crowd investment fund orders. | Planned | Figma (Orders) | — |

---

### Cross-Journey

| # | Feature | Description | Status | Source | BRD Ref |
|---|---|---|---|---|---|
| 136 | Guest Mode (Discovery Mode) | Allows non-registered users to explore the SuperApp without KYC, viewing markets and products in a read-only mode. | Planned | BRD + Figma (Home) | ARCD - 75522 |
| 137 | Zakat Calculator | Enables clients to calculate the Zakat due on their investment holdings directly within the SuperApp or SuperWeb. | Live | BRD | ARCD-1283 |
| 138 | Purification ZATCA-Compliant Invoice | Automatically generates ZATCA-compliant electronic invoices for the Purification Calculator service. | Planned | BRD | ARCD-14553 |
| 139 | Economic Calendar (International) | Provides clients with a real-time global economic calendar showing key economic indicators, events, forecasts, and their expected market impact. | Planned | BRD | ARCD 61046 |
| 140 | ARC News Screener (Personalized News Dashboard) | Enables clients to configure a personalized news dashboard with custom widgets, tag-based content filters, and alert rules. | Planned | BRD | ARCD-82616 |
| 141 | Ticker Chart Integration (Trading View) | Integrates advanced interactive price charts (TradingView/Ticker Chart) into the Saudi and International market stock pages. | Live | BRD + Figma (Market) | ARCD-1553, ARCD-2627 |
| 142 | Ticker Chart — ARC Package Subscriptions | Allows ARC clients to access premium TradingView/TickerChart package features via an ARC-subsidized subscription. | Planned | BRD | ARCD-2627 |
| 143 | CRM Case Management (End-to-End Digital) | Digital CRM system enabling clients to raise, track, and resolve service cases fully online. | Planned | BRD | ARCD-85537 |
| 144 | Mada / Credit Card 3D Secure Authentication | Adds 3D Secure (OTP) verification when a client links a new credit or Mada card to their ARC account. | Planned | BRD | ARCD-68518 |
| 145 | Mada / Credit Card Transaction Limits | Enables daily transaction limit controls per client for linked Mada and credit cards used to fund investment accounts. | Planned | BRD | ARCD-68518 |
| 146 | Cash-Out Enhancements (GCC to External Bank) | Allows GCC clients to initiate and complete cash withdrawals from ARC accounts to linked local or international bank accounts. | Planned | BRD | ARCD-34470 |
| 147 | International Indices Historical Data (ODS) | Provides clients with accurate, pre-aggregated historical data for major international market indices. | Planned | BRD | ARCD-68581 |
| 148 | View Commission Discount on Saudi Market Trades | Displays the applicable commission discount rate to clients on Saudi market trade execution screens. | Planned | BRD | ARCD-60436 |
| 149 | Saudi Market Stock Profile Information (Enhanced) | Enhances the stock information page for Saudi market stocks with additional data fields including financial metrics, sector data, and company overview. | Planned | BRD | ARCD-14312 |
| 150 | Stock Sector & Exchange Liquidity Indicators | Displays liquidity indicators (volume, bid-ask spread, turnover) for individual stocks, sectors, and the exchange. | Unknown | BRD | ARCD - 41013 |
| 151 | Session Timeout Settings | Settings screen to configure automatic session timeout duration. | Planned | Figma (Profile & Setting) | — |
| 152 | Always On Display Setting | Toggle to keep the device screen on while using the app. | Planned | Figma (Profile & Setting) | — |
| 153 | Index Feed Bar Settings | Setting to show/hide or configure the live market index ticker bar. | Planned | Figma (Profile & Setting) | — |
| 154 | Registered Devices Management | List of devices registered for this account with option to revoke access. | Planned | Figma (Profile & Setting) | — |

---

### New Discoveries (Deep Figma Extraction — 2026-04-21)

*10 features discovered during deep tree extraction of 2.27M nodes across 8 Figma files.*

| # | Feature | Description | Status | Source | BRD Ref |
|---|---|---|---|---|---|
| 155 | Guest Mode (Discovery Mode) | Allows non-registered users to explore the app in read-only mode before signing up — market prices, stock pages, and product discovery without KYC. 8,012 screens designed. | Planned | Figma (OnBoarding KYC — Guest Mode page) | ARCD-75522 |
| 156 | Tutorials & Onboarding Education | Interactive tutorial screens guiding new users through app features and investing basics during first-time use. | Planned | Figma (OnBoarding KYC — Tutorials page) | — |
| 157 | First Engagement (Post-Signup Activation) | Guided first-trade experience shown immediately after onboarding completion — amount entry, stock selection, and first investment prompt. 3,766 screens designed. | Planned | Figma (OnBoarding KYC — First Engagement page) | — |
| 158 | Fast Onboarding (Streamlined KYC) | Reduced-step onboarding flow targeting faster completion — condensed KYC with progressive disclosure. 364 screens designed. | Planned | Figma (OnBoarding KYC — Fast Onboarding page) | — |
| 159 | Digital StoryTeller (Portfolio Narratives) | Visual storytelling format for portfolio performance — total profit cards, multi-wallet views, and narrative quarterly summaries. 1,845 screens designed. | Planned | Figma (Portfolios — Digital StoryTeller page) | — |
| 160 | Ramadan Campaign / Theme | Seasonal Ramadan-themed home screen experience with special promotions and religious investment features. | Planned | Figma (Home — Ramadan page) | — |
| 161 | Discover & Search (Unified Discovery) | Unified search and discovery experience across all product types — stocks, funds, IPOs, and robo products from a single entry point. | Planned | Figma (Discover — Discover & Search page) | — |
| 162 | Stock Stories | Swipeable story-format cards for key stock events — price movements, bulls/bears, analyst ratings, news, dividends, earnings, insider trades, government trades. | Planned | Figma (Market — Stock Stories section) | — |
| 163 | Fund Recommender | Suitability-based fund recommendation engine — risk profile quiz, dashboard view, and one-tap invest flow. 17+ dashboard variants designed. | Planned | Figma (Market — Fund Recommender section) | — |
| 164 | Saudi Options (Native Trading Flow) | Full native options trading flow for Saudi Exchange — options list, expiration date selection, put/call/strike views, order preview, portfolio integration. | Planned | Figma (Market — Saudi Options section) | — |

---

*Notes:*
- *Status "Live" = feature is active in the current production app (BRD confirmed)*
- *Status "Planned" = BRD-approved but not yet live, OR Figma-only screen in the unreleased revamp*
- *Status "Unknown" = BRD file could not be fully read or status was unclear*
- *Source "BRD + Figma" = feature exists in both a BRD and a Figma screen in the unreleased revamp*
- *Source "Figma" = screen found only in Figma revamp files — no corresponding BRD located*
- *All Figma files represent the UNRELEASED APP REVAMP — not the current live app*
- *Some features appear in multiple BRDs — the most relevant/authoritative source is cited*

---

## Competitor Gap Analysis
Gap analysis complete — see `competitor-gap-matrix.md` for full results.
