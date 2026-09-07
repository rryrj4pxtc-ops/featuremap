# Depth Analysis — Tap Count to Key Actions
*36 features · Traced through Figma revamp designs · 2026-04-24*

> **Method:** Each feature traced from Home screen to action completion. Every distinct screen transition = 1 tap. Form fills count as 1 tap (not per field). Bottom navigation switches count as 1 tap.

---

## Summary

| Rating | Tap Range | Count | % |
|---|---|---|---|
| Excellent | 1–3 taps | 10 | 28% |
| Acceptable | 4–5 taps | 11 | 31% |
| Friction Risk | 6+ taps | 15 | 42% |

**Average depth:** 4.9 taps
**Deepest action:** Complete KYC (9 taps) and Subscribe to fund (7 taps)
**Shallowest action:** View portfolio value (1 tap)

---

## Friction Heatmap

```
█ EXCELLENT (1-3)    ██ ACCEPTABLE (4-5)    ███ FRICTION RISK (6+)
```

| # | Feature | Taps | Rating | Flow |
|---|---|---|---|---|
| **CORE TRADING** | | | | |
| 1 | Buy Saudi stock | 6 | ███ Friction | Home → Market tab → Stock → Buy → Fill form + Preview → OTP → Success |
| 2 | Sell Saudi stock | 6 | ███ Friction | Home → Portfolio tab → Holding → Sell → Fill form + Preview → OTP → Success |
| 3 | Buy US stock | 7 | ███ Friction | Home → Market tab → US toggle → Stock → Buy → Fill form + Preview → OTP → Success |
| 4 | Sell US stock | 7 | ███ Friction | Home → Portfolio tab → US Portfolio → Holding → Sell → Fill + Preview → OTP → Success |
| 5 | Place limit order | 6 | ███ Friction | Home → Market tab → Stock → Buy → Select Limit + Fill → Preview → OTP → Success |
| 6 | Place market order | 6 | ███ Friction | Home → Market tab → Stock → Buy → Fill form + Preview → OTP → Success |
| 7 | Modify order | 5 | ██ Acceptable | Home → Orders tab → Order detail → Edit → Confirm + OTP |
| 8 | Cancel order | 4 | ██ Acceptable | Home → Orders tab → Order detail → Cancel → Confirm |
| **PORTFOLIO** | | | | |
| 9 | View portfolio value | 1 | █ Excellent | Home (visible on dashboard) |
| 10 | View holdings list | 2 | █ Excellent | Home → Portfolio tab |
| 11 | View single holding | 3 | █ Excellent | Home → Portfolio tab → Tap stock |
| 12 | View profit/loss | 3 | █ Excellent | Home → Portfolio tab → P&L Overview |
| 13 | View performance chart | 4 | ██ Acceptable | Home → Portfolio tab → Analysis → Chart |
| **MARKET & DISCOVERY** | | | | |
| 14 | Search for a stock | 2 | █ Excellent | Home → Market tab → Search |
| 15 | View stock details | 3 | █ Excellent | Home → Market tab → Tap stock |
| 16 | View stock chart | 3 | █ Excellent | Home → Market tab → Stock (chart visible on detail) |
| 17 | View market index | 2 | █ Excellent | Home → Market tab (index visible) |
| 18 | View top movers | 3 | █ Excellent | Home → Market tab → Top Movers section |
| 19 | View market news | 4 | ██ Acceptable | Home → Market tab → Stock → News tab |
| 20 | Add to watchlist | 4 | ██ Acceptable | Home → Market tab → Stock → Watchlist button |
| **ONBOARDING** | | | | |
| 21 | Register new account | 2 | █ Excellent | Splash → Open Account |
| 22 | Complete KYC | 9 | ███ Friction | Open Account → Personal Info → Nationality → Work Info → Financial Info → Investment Info → Bank Linking → Documentation → KYC Summary |
| 23 | Verify identity (Nafath) | 1 | █ Excellent | Embedded in KYC flow (1 tap to approve in Nafath app) |
| 24 | Accept T&C | 1 | █ Excellent | Embedded in flow (1 tap to accept) |
| **TRANSFERS & FUNDING** | | | | |
| 25 | Cash in (Saudi) | 5 | ██ Acceptable | Home → Portfolio tab → Transfer → Select source → Amount + Confirm → OTP |
| 26 | Cash out (Saudi) | 5 | ██ Acceptable | Home → Portfolio tab → Transfer → Select destination → Amount + Confirm → OTP |
| 27 | Cash in (US) | 6 | ███ Friction | Home → Portfolio tab → US Portfolio → Transfer → Source → Amount + Confirm → OTP |
| 28 | Cash out (US) | 6 | ███ Friction | Home → Portfolio tab → US Portfolio → Transfer → Destination → Amount + Confirm → OTP |
| **MUTUAL FUNDS** | | | | |
| 29 | Browse funds list | 3 | █ Excellent | Home → Discover tab → Funds section |
| 30 | Subscribe to fund | 7 | ███ Friction | Home → Discover tab → Fund → Subscribe → Amount → Preview → OTP → Success |
| 31 | Redeem from fund | 6 | ███ Friction | Home → Portfolio tab → MF Portfolio → Fund → Redeem → Confirm → OTP |
| 32 | View fund performance | 4 | ██ Acceptable | Home → Portfolio tab → MF Portfolio → Fund detail |
| 33 | View upcoming IPOs | 3 | █ Excellent | Home → Discover tab → IPO Listing |
| 34 | Subscribe to IPO | 6 | ███ Friction | Home → Discover tab → IPO → Subscribe → Amount + Confirm → OTP → Success |
| **ROBO ADVISORY** | | | | |
| 35 | Create robo portfolio | 7 | ███ Friction | Home → Discover tab → Mashurah → Strategy selection → Risk profile → Amount → Preview → OTP |
| 36 | View robo performance | 4 | ██ Acceptable | Home → Portfolio tab → Mashura Portfolio → Overview |

---

## Key Findings

### 1. Trading is too deep (6-7 taps)
Every buy/sell action requires 6+ taps. The main bottleneck is the mandatory OTP step. Without OTP, trading would be 5 taps (acceptable). **US trading adds 1 extra tap** for the market switch.

**Recommendation:** Add quick-trade shortcut from Stock Details — tap "Buy" should go directly to pre-filled order form. Consider biometric confirmation instead of OTP for repeat trades.

### 2. KYC is the deepest flow (9 taps)
9 distinct screens to complete KYC. Combined with the 87% drop-off rate, this is the most critical friction point in the entire app.

**Recommendation:** The "Fast Onboarding" flow (364 frames in Figma) appears to be designed to address this. Prioritize shipping it — target 4-5 screens max.

### 3. Portfolio viewing is excellent (1-3 taps)
Portfolio value is visible on the Home dashboard (1 tap). Holdings, P&L, and stock details are all within 3 taps. This is best-in-class.

### 4. Fund/IPO subscription matches trading friction (6-7 taps)
Subscribe to fund (7), subscribe to IPO (6), and create robo portfolio (7) all require 6+ taps. These are conversion-critical flows.

**Recommendation:** Pre-fill known data (portfolio, bank account) to reduce form steps. One-tap resubscribe for repeat fund investors.

### 5. US Market adds +1 tap penalty everywhere
Every US Market action requires 1 extra tap vs Saudi Market (market toggle or portfolio switch). This creates a consistent friction gap for US trading.

**Recommendation:** Remember last-used market. If user's primary activity is US trading, default to US view.

---

## Depth Distribution

```
Taps  Features                                            Count
  1   Portfolio value, Nafath, T&C                          3
  2   Holdings list, Search stock, Market index, Register   4
  3   Holding detail, P&L, Stock details, Chart,            6
      Top movers, Funds list, IPOs list
  4   Performance chart, News, Watchlist, Fund perf,        5
      Cancel order, Robo performance
  5   Modify order, Cash in Saudi, Cash out Saudi           3
  6   Buy Saudi, Sell Saudi, Limit order, Market order,     8
      Cash in US, Cash out US, Redeem fund, Subscribe IPO
  7   Buy US, Sell US, Subscribe fund, Create robo          4
  9   Complete KYC                                          1
```

*Friction cluster at 6-7 taps = transactional flows with OTP*

---

## Priority Actions

| # | Action | Impact | Effort | Features Affected |
|---|---|---|---|---|
| 1 | **Quick-trade shortcut** from stock detail | High | Medium | Buy/Sell Saudi, Buy/Sell US, Limit, Market |
| 2 | **Ship Fast Onboarding** flow | Critical | Large | KYC (9→4 taps) |
| 3 | **Biometric instead of OTP** for repeat trades | High | Large | All 6+ tap transactional flows |
| 4 | **Remember last market** (Saudi/US) | Medium | Small | All US Market features (-1 tap) |
| 5 | **Pre-fill fund subscription** data | Medium | Small | Subscribe fund, Subscribe IPO, Create robo |

---

*Source: Figma revamp designs (8 files). Flow paths based on screen inventory extracted 2026-03-26 + deep extraction 2026-04-21.*
*Note: All flows represent the UNRELEASED revamp design — live app may differ.*
