# ARC Response — International Brokerage App Gap Analysis
*Document: 20260325 - International brokerage app gap analysis vShared.pdf*
*Response prepared by: Digital Experience Department*
*Date: 2026-03-27*

---

## Section 1 — Feature Gaps: ARC vs. Sahm

---

### Point 1 — App Store Display
**Finding:** Sahm uses incentivizing graphics on the App Store download page. ARC uses basic graphics.

**ARC Response:**
This is a marketing and App Store optimization (ASO) decision, not a product feature. ARC's App Store presence is managed by the Marketing team. The Digital Experience team will flag this to Marketing as a recommended improvement to the App Store listing graphics, screenshots, and preview video to better reflect the revamp experience once it launches.

**Owner:** Marketing
**Action:** Flag to Marketing team — App Store listing refresh to coincide with revamp launch.

---

### Point 2 — Subscription Options
**Finding:** Sahm clearly displays subscription options with Apple Pay integration. ARC only allows payment after wallet is funded.

**ARC Response:**
ARC has a Prepaid Commission Bundle (Feature #122, Planned — BRD: ARCD-17031) in the roadmap. This covers commission-free trading subscription bundles. The gap is in (a) the clarity of the subscription display and (b) Apple Pay as a payment method. Apple Pay funding is also captured separately as Gap G-34 (Wealth Visibility squad). Both are in the roadmap pipeline.

**Owner:** Investor Engagement Squad (#122) + Wealth Visibility Squad (Apple Pay)
**Action:** Confirm delivery timeline for #122. Ensure the subscription UI clearly surfaces options at the right moment in the user journey, not only after wallet funding.

---

### Point 3 — Social Proof / Behavioral Nudge on US Trading
**Finding:** Sahm shows "98% of users invest in the US market" to encourage activation. ARC only uses behavioral nudges on the Murabaha product.

**ARC Response:**
This gap is confirmed and logged as G-48 in the gap matrix. ARC does not currently have a systematic behavioral nudge framework for US trading activation. The Investor Engagement squad's existing features (#121 Spin the Wheel, #126 Round-Up, #127 Social Trading) focus on engagement mechanics but not social proof messaging at the journey entry point.

**Owner:** Investor Engagement Squad + US Trading Squad
**Action:** Add a social proof / behavioral nudge feature to the US Trading journey BRD backlog. Priority Score: 12/25.

---

### Point 4 — Login with Face Recognition (Direct Activation)
**Finding:** Sahm activates Face ID directly from the first screen. ARC shows the login screen first, then signs in.

**ARC Response:**
ARC has Face ID / Biometric Setup (Feature #17, Planned — Figma-only). The planned revamp includes biometric login, but the specific UX flow — skipping the login screen entirely and going directly to Face ID — is not confirmed in the current Figma designs. This is a UX flow decision for the Onboarding squad to review.

**Owner:** Onboarding Squad
**Action:** Review the Face ID login flow in the revamp Figma. Confirm whether the flow matches Sahm's direct-to-Face-ID pattern or still shows the login screen first. Adjust if needed — this is a 1–2 day Figma change.

---

### Point 5 — Account Funding via Apple Pay
**Finding:** Sahm offers instant Apple Pay funding. ARC uses traditional funding only.

**ARC Response:**
Confirmed gap — logged as G-34 (Wealth Visibility squad, Priority Score: not yet scored in original matrix — equivalent to Medium-High). ARC currently supports ARB bank transfer (#91, Live), Mada/credit card (#144, #145, Planned), and UCM wallet enhancements (#92, Planned). Apple Pay is not in the current BRD pipeline.

**Owner:** Wealth Visibility Squad
**Action:** Write BRD for Apple Pay funding integration. Requires coordination with the Payments/Banking team and Apple Pay provisioning. This is a commercially important gap — Sahm uses it as a key differentiator for instant funding.

---

### Point 6 — Instant In-App Language Switch (1-Click)
**Finding:** Sahm offers instant Arabic/English switching with one click from anywhere in the app. ARC's behavior was marked "to be checked."

**ARC Response:**
Language switching is a Cross-Journey setting function. ARC's current app has language settings in the Profile section but it is not a persistent, instant 1-click toggle. The revamp Figma does not have a dedicated instant language switch feature. This is logged as G-49.

**Owner:** Cross-Journey (Design System & Governance)
**Action:** Confirm the current language switching behavior in the live app. If it requires more than 1 tap, add an instant language toggle to the revamp. This is a low-effort, high-polish improvement.

---

### Point 7 — In-App Trading Incentive Banners on Home Page
**Finding:** Sahm shows banners on the home page to incentivize account funding and trading. ARC has none.

**ARC Response:**
ARC's home page in the revamp (Figma: Home file) does not include a promotional banner system. The note in the gap analysis ("to be added once marketing starts") is a marketing readiness issue, not a product feature gap. However, the underlying capability — a configurable home page banner/promotional slot — does not have a BRD. Logged as G-50.

**Owner:** Investor Engagement Squad + Marketing
**Action:** Add a home page promotional banner/notification system to the BRD backlog. This is a platform capability that Marketing needs before launch. Priority: Medium.

---

### Point 8 — Market Prediction Competition (Cashback)
**Finding:** Sahm runs a cashback competition tied to market prediction accuracy. ARC has this in the marketing plan but not built.

**ARC Response:**
ARC has Spin the Wheel for Discounts (#121, Planned — BRD: ARCD-16056) as a gamified reward mechanic. However, a market prediction competition with cashback on commission is a distinct product — it requires a prediction engine, scoring logic, and campaign management. This is logged as G-51. The gap analysis note says "promotion to be included in marketing plan" — this should be elevated from a marketing item to a product backlog item.

**Owner:** Investor Engagement Squad
**Action:** Separate the prediction competition from general marketing planning. Write a BRD if ARC wants this as a product feature. Priority Score: 12/25.

---

### Point 9 — Chart Screen Functionality (Trade on Chart, Share, Scroll Between Watchlist)
**Finding:** Sahm has: (1) trade button directly on chart screen, (2) chart sharing with contacts, (3) direct scroll between watchlist securities on the chart. ARC's chart functionality was "to be confirmed by Digital."

**ARC Response:**
- **Trade button on chart:** Already in the gap matrix as G-14 (Chart Trading, Priority Score: not yet formally scored — confirmed high priority from Chart Trading Feature Benchmark PDF). ARC has TradingView integration (#141, Live) but chart-native order placement is not in the inventory.
- **Chart sharing:** Not in ARC's inventory. New gap — add to the gap matrix.
- **Scroll between watchlist securities:** Not in ARC's inventory. New gap — add to the gap matrix.

**Owner:** Saudi Trading / US Trading Squad
**Action:** (1) Chart trading BRD is a strategic priority — already identified. (2) Chart share and watchlist scroll are lower-effort improvements to add to the TradingView/Ticker Chart enhancement BRD (#142). Confirm with the Digital team what is feasible within the current TradingView integration scope.

---

### Point 10 — Hover / Touch-and-Hold for Intra-Day Prices on Chart
**Finding:** Sahm allows touch-and-hold on the chart to view intra-day prices at any point. ARC shows daily performance but not granular intra-day exploration.

**ARC Response:**
Logged as G-52 (Priority Score: 16/25). This is a standard advanced chart interaction that most serious trading apps support. ARC's TradingView integration (#141) may already support this within TradingView's native controls — the Digital team needs to confirm whether the current TradingView embed exposes this interaction. If it does, this may be a configuration fix, not a development item.

**Owner:** Saudi Trading / US Trading Squad
**Action:** Confirm with the Digital team whether TradingView's touch-and-hold intra-day hover is enabled in ARC's current integration. If not, this should be in the TradingView package configuration (#142).

---

### Point 11 — Thematic ETF Spotlight (Oil, Gold, etc.)
**Finding:** Sahm groups ETFs into thematic spotlights. ARC shows a single flat ETF list.

**ARC Response:**
Logged as G-53 (Priority Score: 12/25). ARC's US Trading journey (#59–#68) does not include ETF discovery or thematic filtering. This is a product discovery gap — investors looking for thematic exposure (oil, tech, gold) have no guided path in ARC's current or planned experience.

**Owner:** US Trading Squad
**Action:** Add ETF thematic grouping to the US Trading product backlog. This pairs well with G-21 (Related ETF Exposure View) already in the gap matrix.

---

### Point 12 — Expanded US Stock Inventory (7.2K vs. 12.8K Stocks)
**Finding:** Sahm offers 12,800 US stocks including 2,000 Shariah-compliant. ARC offers 7,200 Shariah stocks only.

**ARC Response:**
Logged as G-54 (Priority Score: 16/25). ARC's current US stock list is limited to Shariah-compliant securities. This is a deliberate product decision — but it means ARC excludes non-Shariah investors from the full US market universe. With IBKR as the new backend provider (#11, Planned), expanding the available instrument list is technically possible and commercially important.

**Owner:** US Trading Squad + Technology / IBKR Integration
**Action:** Confirm with the Technology team what stock inventory is available through IBKR. Determine whether a non-Shariah US stock tier can be offered alongside the Shariah list. This is a commercial and compliance decision as much as a product one — flag to CPO.

---

### Point 13 — Owned Stocks Auto-Added to Watchlist
**Finding:** Sahm automatically adds purchased stocks to the watchlist. ARC requires manual watchlist management.

**ARC Response:**
Logged as G-55 (Priority Score: 12/25). ARC's Watchlist feature is in the revamp (Figma file: Watchlist — currently empty). Auto-adding holdings to the watchlist is a logical and low-effort behavioral improvement. It is not in any current BRD.

**Owner:** Saudi Trading / US Trading Squad (with Portfolio Monitoring)
**Action:** Add auto-watchlist behavior to the Watchlist BRD when it is written. This is a low-effort feature with high UX impact. Feature #84 (Add Holdings to Watchlist, Planned — Figma-only) covers the manual add flow; auto-add is the missing complement.

---

### Point 14 — Always-On Live Price Detail View in Portrait Mode
**Finding:** Sahm shows the full detailed price view (bid, ask, spread, volume) in portrait mode at all times. ARC only shows this in landscape mode.

**ARC Response:**
Logged as G-56 (Priority Score: 16/25). Requiring investors to rotate their phone to see live price detail is a significant UX friction point for active traders. This appears to be a layout constraint in the current app rather than a deliberate design decision. The revamp Figma should confirm whether the stock detail page shows full bid/ask data in portrait — if not, it must be corrected before launch.

**Owner:** Saudi Trading / US Trading Squad
**Action:** Audit the revamp Figma stock detail screens for portrait-mode bid/ask/volume display. Confirm this data is always visible without requiring landscape mode. Flag as a P0 UX fix if missing.

---

### Point 15 — Live Prices for Options (vs. Delayed + Limited)
**Finding:** Sahm provides live pricing and detailed depth of market data for options. ARC has delayed pricing and limited depth.

**ARC Response:**
ARC has International Options Page (#62, Planned — BRD: ARCD-72350) which includes Greeks, theoretical values, and market data. However, whether this delivers live or delayed pricing depends on the IBKR data subscription tier. Delayed pricing for options is a commercial constraint, not a design gap.

**Owner:** US Trading Squad + Technology
**Action:** Confirm with the Technology/IBKR team what options data tier ARC will subscribe to at launch. If delayed, assess the commercial cost of upgrading to live options pricing — active options traders will not accept delayed data.

---

### Point 16 — Free Live Index Prices (Sahm and Abyan Free; Derayah and Awaed Paid)
**Finding:** Sahm and Abyan offer live index prices for free. Derayah and Awaed charge a subscription.

**ARC Response:**
Logged as G-57 (Priority Score: 16/25). ARC has Stock Sector & Exchange Liquidity Indicators (#150, Unknown status — BRD: ARCD-41013). The live vs. delayed index pricing decision is tied to TILA (Tadawul Information License Agreement — Feature #45, Live). ARC's current status for US index data is unconfirmed.

**Owner:** Saudi Trading Squad / US Trading Squad + Technology
**Action:** Confirm current pricing tier for: (1) Saudi index data (Tadawul), (2) US index data (S&P, Nasdaq, Dow). If either is delayed, assess the cost of upgrading to free live indices — this is a competitive disadvantage vs. Sahm and Abyan.

---

### Point 17 — Market Hours Chart Axis Extended to Close Time
**Finding:** Sahm's chart x-axis extends to market close even during live trading, giving traders full-session context. ARC's axis only goes up to the current time.

**ARC Response:**
Logged as G-58 (Priority Score: 9/25). This is a chart configuration decision — likely within the TradingView/Ticker Chart integration scope. Showing the full session axis (from open to close) regardless of current time is a standard expectation for intra-day trading charts.

**Owner:** Saudi Trading / US Trading Squad
**Action:** Confirm with the Digital team whether the TradingView/Ticker Chart integration can be configured to extend the x-axis to market close. If yes, this is a configuration change — ship with the revamp.

---

### Point 18 — Personalized Events Calendar (Filtered by Watchlist / Holdings)
**Finding:** Sahm's events calendar surfaces only events relevant to the user's watchlist and owned stocks. ARC shows a static full-market calendar.

**ARC Response:**
This is the highest-priority new gap identified in this document (G-59, Priority Score: 20/25). ARC has three calendar features planned: Dividends Calendar (#117), Earnings Calendar (#78), and Economic Calendar (#139) — but all are global/market-wide, not personalized. A personalized events calendar filtered by the investor's actual holdings dramatically increases relevance.

**Owner:** Corporate Actions Squad (#117) + Portfolio Monitoring Squad (#78) + US Trading Squad (#139)
**Action:** Add personalization to the events calendar BRDs. When writing #117, #78, and #139, include a "My Stocks" filter that shows only events relevant to the investor's holdings and watchlist. This should be a standard feature, not an add-on.

---

### Point 19 — Supply & Demand Layout (Demand Right / Supply Left Convention)
**Finding:** Sahm follows market convention: demand (buy) on right, supply (sell) on left. ARC's layout is reversed.

**ARC Response:**
This is both a UX convention gap (G-60) and potentially a bug in the current live app. The bid/ask layout inconsistency is also flagged in Section 2 (Bug B-02). The reversed supply/demand display creates serious confusion for traders switching between ARC and any other platform.

**Owner:** Saudi Trading Squad + US Trading Squad (Design System & Governance to review)
**Action:** Treat this as a P0 UX correction — fix in the revamp Figma immediately. Also resolve as part of Bug B-02 in the live app. This is not a new feature — it is a correction to an existing incorrect layout.

---

### Point 20 — Advanced Trade Button (Multiple Order Types + Most Traded Stocks)
**Finding:** Sahm's trade button surfaces multiple order types and most-traded stocks directly in the trade flow. ARC only allows normal orders from the trade entry point.

**ARC Response:**
Logged as G-61 (Priority Score: 16/25). ARC has multiple order type screens designed in the revamp Figma (Stop Loss #54, Take Profit #55, Conditional #50, Basket #51, Iceberg #52, Interval #53) but these are Figma-only with no BRDs. The gap is that all these order types are not accessible from the main trade entry button. Additionally, a "most traded stocks" surface at the trade entry point is not in ARC's inventory.

**Owner:** Saudi Trading Squad
**Action:** (1) Write BRDs for the advanced order type screens (#50–#55) — these are currently Figma-only with no business requirements. (2) Add a contextual "most traded / top movers" module to the trade entry screen in the BRD.

---

### Point 21 — Tab-Based Navigation vs. Long Vertical Scroll
**Finding:** Sahm uses a tab-based navigation architecture. ARC uses a long vertical scroll layout which reduces navigation efficiency.

**ARC Response:**
Logged as G-62 (Priority Score: 16/25). The current ARC revamp Figma appears to maintain a scroll-heavy navigation pattern. Tab-based navigation is the standard pattern for trading apps globally (Moomoo, Robinhood, eToro, Sahm). A vertical scroll architecture increases the number of gestures needed to reach key features and negatively impacts D4 (discoverability) in the platform maturity framework.

**Owner:** Product Experience Design (Design System & Governance)
**Action:** This is a fundamental UX architecture decision that must be resolved before the revamp launches. If the revamp Figma uses vertical scroll, the design team must assess the feasibility and effort of switching to a tab-based bottom navigation pattern. Recommend an urgent design review with the Head of DX and squad leads.

---

## Section 2 — ARC Live App Bugs

> All bugs below are in the **current live production app** — not the revamp. Each must be assigned to a squad lead with a resolution timeline before or alongside the revamp launch.

---

### Bug B-01 — SMS Notifications for Deposits/Transfers
**Finding:** SMS messages for transfers and deposits lack clarity and structure — hard to parse.
**Severity:** Medium
**Owner:** Wealth Visibility Squad + Notifications Team
**Action:** Rewrite SMS notification templates for all wallet deposit, transfer, and cash-in events. BRD: ARCD-20124 (Email Notification Templates Revamp, #132) covers email — extend scope to include SMS. Target: fix before revamp launch.

---

### Bug B-02 — Bid & Ask Layout Inconsistency
**Finding:** Arabic interface shows Bid/Ask on opposite sides between header and price table. English shows labels on wrong sides.
**Severity:** High
**Owner:** Saudi Trading Squad / US Trading Squad
**Action:** This is a data display bug causing incorrect trading decisions. Must be fixed in the live app immediately — do not wait for the revamp. Raise a P1 ticket with Engineering. Also correct in the revamp Figma to ensure the issue is not carried forward.

---

### Bug B-03 — Insufficient Funds Redirect Shows Wrong Currency
**Finding:** USD order rejected for insufficient funds → app redirects user to fund SAR amount instead of USD amount.
**Severity:** High
**Owner:** US Trading Squad + Wealth Visibility Squad
**Action:** Fix the currency detection logic in the insufficient-funds redirect flow. When a USD order is rejected, the redirect must show the correct USD shortfall amount and link to the USD wallet funding flow. Raise a P1 Engineering ticket.

---

### Bug B-04 — Order Status Mismatch Between SMS and App
**Finding:** After execution, SMS says "completed" but app shows "active" in Today's Orders and "completed" in Last Month's Transactions — inconsistent across 3 surfaces.
**Severity:** High
**Owner:** Saudi Trading Squad / US Trading Squad + Notifications Team
**Action:** This is a data state synchronization bug. The order status must be consistent across: (1) SMS confirmation, (2) Today's Orders view, (3) Order history. Raise a P1 Engineering ticket. Root cause is likely a timing/cache issue in order state propagation.

---

### Bug B-05 — US Portfolio Value Incorrect on Home Screen
**Finding:** Home page shows wrong US portfolio value (e.g., $2 instead of $48,000).
**Severity:** Critical
**Owner:** Portfolio Monitoring Squad + US Trading Squad
**Action:** This is a critical data accuracy issue that directly undermines client trust. Raise an immediate P0 Engineering ticket. Investigate whether this is a currency conversion error, a data feed issue, or a display rendering bug. Must be resolved in the live app before any marketing activity around US trading.

---

### Bug B-06 — Portfolio Performance Discrepancy
**Finding:** Total portfolio performance on home screen does not match the sum of individual market performances.
**Severity:** Critical
**Owner:** Portfolio Monitoring Squad
**Action:** P0 Engineering ticket. Portfolio performance is a core trust metric — any inconsistency will cause clients to doubt their data. Investigate whether the discrepancy is in the calculation logic (weighted vs. simple sum) or a display issue. If it is a known calculation methodology difference, add a tooltip explaining how total performance is calculated.

---

### Bug B-07 — Earnings Announcements Shown During Trading Hours
**Finding:** Earnings announcements appear in-app at 11 AM during active trading hours. These should appear before market open or after market close.
**Severity:** Medium
**Owner:** US Trading Squad + Corporate Actions Squad
**Action:** Review the timing logic for earnings announcement notifications and in-app banners. Set the display window to: pre-market (6–9:30 AM ET) or post-market (4–8 PM ET) only. This prevents announcements from appearing as misleading signals during live trading sessions.

---

### Bug B-08 — Swipe-to-Cancel Available on Executed Orders
**Finding:** Swipe-to-cancel is active on already-executed orders. Triggering it shows the order as "rejected."
**Severity:** High
**Owner:** Saudi Trading Squad / US Trading Squad
**Action:** The swipe-to-cancel gesture must be disabled for orders with status "Executed" or "Filled." Only orders in "Pending" or "Open" state should be cancellable. Raise a P1 Engineering ticket. This is a UI state management bug.

---

### Bug B-09 — Rejected Order Blocks Cash + SMS Confirms Non-Existent Order
**Finding:** Rejected order incorrectly blocks cash balance. SMS confirms execution of a new order that never appears in the app.
**Severity:** Critical — Two compounding failures
**Owner:** US Trading Squad + Technology (Order Management System)
**Action:** This is the most severe bug in this document — it involves financial data integrity. Two separate issues must be fixed:
1. Rejected orders must release blocked cash immediately. Raise a P0 Engineering ticket for cash release logic.
2. SMS execution confirmations must only fire after the order is confirmed as executed in the order management system. Raise a P0 ticket for SMS/notification trigger logic.
Both fixes require coordination between the Digital Experience team and the core Technology/OMS team.

---

### Bug B-10 — Visual Price Indicator Misalignment on Range Scale
**Finding:** The price indicator marker on the stock's price range scale does not visually align with the actual current price.
**Severity:** Low
**Owner:** Saudi Trading Squad / US Trading Squad
**Action:** This is a rendering/scaling bug in the price range widget. Raise a low-priority Engineering ticket. Fix in the revamp — confirm the correct calculation for indicator position is: `(current_price - range_low) / (range_high - range_low) × scale_width`.

---

## Section 3 — Onboarding Comparison

### Finding: Derayah Global provides a dedicated human onboarding specialist after account activation. Verification as fast as 1 hour for some customers.

**ARC Response:**
ARC's onboarding time (5–7 minutes) is competitive with Sahm and faster than Derayah Global (10–12 minutes). However, Derayah's human-assisted onboarding specialist is a differentiated service for the international brokerage product — it addresses the anxiety of first-time US market investors who want guidance before they start trading.

ARC does not currently have an assisted onboarding service for the international brokerage product. Feature #11 (IBKR International Brokerage Onboarding, Planned) focuses on the digital flow, not a human-assisted layer.

**Owner:** Onboarding Squad + Customer Experience Team
**Action:** Assess whether ARC should offer an optional "speak to a specialist" onboarding path for international brokerage clients, matching Derayah's differentiator. This is particularly important for high-value clients who are new to US market investing.

---

## Section 4 — Live Prices for Indices

### Finding: Sahm and Abyan provide free live index prices. Derayah and Awaed charge subscriptions.

**ARC Response:**
See Point 16 above (G-57). ARC should confirm its current index pricing tier for both Saudi and US markets and benchmark against the free-tier competitors. This is a data licensing cost decision — but offering free live index prices positions ARC with Sahm and Abyan rather than the paid-subscription tier.

**Owner:** Saudi Trading Squad + US Trading Squad + Technology
**Action:** Get commercial terms from the data providers for free live index pricing. Present cost/benefit to CPO — the competitive pressure from free-tier peers makes this a commercially necessary investment.

---

## Summary — Action Priority Matrix

| # | Item | Type | Severity/Priority | Owner | Action |
|---|---|---|---|---|---|
| B-05 | US portfolio value wrong | Bug | **Critical P0** | Portfolio Monitoring | Raise P0 ticket immediately |
| B-06 | Portfolio performance discrepancy | Bug | **Critical P0** | Portfolio Monitoring | Raise P0 ticket immediately |
| B-09 | Cash block + false SMS | Bug | **Critical P0** | US Trading + Technology | Raise P0 ticket immediately |
| B-02 | Bid/Ask layout reversed | Bug | **High P1** | Saudi/US Trading | Fix in live app now; correct in Figma |
| B-03 | Wrong currency in funding redirect | Bug | **High P1** | US Trading | Raise P1 Engineering ticket |
| B-04 | Order status mismatch | Bug | **High P1** | US Trading | Raise P1 Engineering ticket |
| B-08 | Swipe-cancel on executed orders | Bug | **High P1** | Saudi/US Trading | Raise P1 Engineering ticket |
| 19 | Supply & demand layout reversed | UX Bug | **High P1** | Saudi/US Trading | Fix in revamp Figma immediately |
| 14 | Portrait mode price detail | UX Fix | **High** | Saudi/US Trading | Audit revamp Figma — fix before launch |
| 21 | Tab-based navigation | Architecture | **High** | Design System | Urgent design review required |
| 18 | Personalized events calendar | Gap G-59 | **Score 20** | Corporate Actions + Portfolio | Add personalization to calendar BRDs |
| 5 | Apple Pay funding | Gap G-34 | **High** | Wealth Visibility | Write BRD |
| 12 | Expanded stock inventory | Gap G-54 | **Score 16** | US Trading + Technology | Confirm IBKR inventory scope |
| 9 | Chart trading / share / scroll | Gap G-14 | **Score 16** | Saudi/US Trading | Already in gap matrix — prioritize BRD |
| 15 | Live options pricing | Data | **High** | US Trading + Technology | Confirm IBKR data subscription tier |
| 16 | Free live index prices | Data | **Score 16** | Saudi/US Trading + Technology | Commercial decision — flag to CPO |
| B-01 | SMS notification wording | Bug | Medium | Wealth Visibility + Notifications | Fix before launch |
| B-07 | Earnings timing during market hours | Bug | Medium | US Trading | Fix notification timing logic |
| B-10 | Price indicator misalignment | Bug | Low | Saudi/US Trading | Fix in revamp |

---

*Response prepared by: Ahmed Alghamdi, Head of Digital Experience*
*For distribution to: US Trading Squad Lead, Saudi Trading Squad Lead, Portfolio Monitoring Squad Lead, Wealth Visibility Squad Lead, Investor Engagement Squad Lead, Technology Team*
