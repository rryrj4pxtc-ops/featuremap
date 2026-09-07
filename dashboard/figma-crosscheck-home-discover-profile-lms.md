# Figma Cross-Check: Home + Discover & Search + Profile & Setting + LMS

> Note: feature ids updated on 2026-05-08 as part of the Investor Engagement / Corporate Actions restructure. See restructure-plan-engagement-ca.md.
>
> Note: feature ids updated on 2026-05-07 as part of the Portfolio Monitoring / Wealth Visibility restructure. See restructure-plan.md.
>
> Note (2026-05-11): SAU-096 → XJ-066 (moved to Cross-Journey). See below for old reference.

**Date:** 2026-05-06
**Source files:** Home, Discover & Search, Profile & Setting, LMS (Figma)
**Target:** `features-master.xlsx` (285 features)
**Methodology:** Same as A1-A3 -- one capability = one user-facing function

---

## Summary

| File | MATCH-LINKED | MATCH-UNLINKED | MISSING | AMBIGUOUS | Total Caps |
|---|---|---|---|---|---|
| Home | 0 | 5 | 6 | 0 | 11 |
| Discover & Search | 3 | 11 | 12 | 0 | 26 |
| Profile & Setting | 0 | 9 | 9 | 0 | 18 |
| LMS | 1 | 2 | 13 | 0 | 16 |
| **Total** | **4** | **27** | **40** | **0** | **71** |

### Cross-Product Flag

All four files contain designs spanning multiple journeys:

| File | Journeys Touched |
|---|---|
| **Home** | Cross-Journey, Saudi Market, US Trading, Mutual Funds |
| **Discover & Search** | Cross-Journey, IPOs, Saudi Market, US Trading, Robo Advisory, LMS |
| **Profile & Setting** | Cross-Journey, Saudi Market, US Trading |
| **LMS** | LMS (single journey -- but references Saudi Market for margin features) |

---

## Home

**File key:** `KbRt2JimFFINSFPqe1t5sZ`

| Bucket | Count |
|---|---|
| MATCH-LINKED | 0 |
| MATCH-UNLINKED | 5 |
| MISSING | 6 |
| AMBIGUOUS | 0 |
| _Skipped (duplicates/informational)_ | _3_ |
| **Total unique capabilities** | **11** |

### MATCH-LINKED (0)

_None_

### MATCH-UNLINKED (5)

Features exist in xlsx but have no `figma_link` set. Figma frames found in this file.

| Feature ID | Feature Name | Status | Journey | Section | Figma Caps |
|---|---|---|---|---|---|
| SAU-094 | Holdings Filter Panel | Planned | Saudi Market | Holdings Filter (Mobile) | Holdings List & Filter |
| SAU-023 | Buying Power Swap | Planned | Saudi Market | Buying Power Swap (Mobile) | Buying Power Swap; Web Buying Power Swap |
| SAU-024 | Instant Settlement (T+0/T+1) | Planned | Saudi Market | Web > Instant Settlement | Instant Settlement (Web) |
| XJ-011 | GCC Cash-Out | Planned | Cross-Journey | Deposit & Transfer (Mobile) | Deposit & Transfer; Web Deposit & Withdraw |
| XJ-022 | Discover & Search | Planned | Cross-Journey | Search (Mobile) | In-App Search; Web Search (Stock Detail) |

### MISSING (6)

Capabilities visible in Figma with no matching feature in xlsx.

| # | Capability | Section | Notes | Suggested Journey | Suggested ID |
|---|---|---|---|---|---|
| 1 | Home Dashboard (Portfolio Overview) | Dashboard - Main (Mobile) | Main home screen with portfolio value, widgets, holding mood view, pagination | Cross-Journey | XJ-0XX |
| 2 | Customize Home Widgets | Customize Widget (Mobile) | Select and arrange widgets: Holdings, Pending alerts, Events, Research & Reports | Cross-Journey | XJ-0XX |
| 3 | Cash Overview | Cash (Mobile) | Cash balance display, breakdown, expiration date selection | Cross-Journey | XJ-0XX |
| 4 | Notifications Centre | Notification (Mobile) | Notification inbox, empty state, filter, date picker (web) | Cross-Journey | XJ-0XX |
| 5 | Hive (Community/Social) | Hive (Mobile) | Hive info flow, app rating prompt, content modals | Cross-Journey | XJ-0XX |
| 6 | Family Members / Account Switching | Standalone | Family members list, account switching between family members | Cross-Journey | XJ-0XX |

### AMBIGUOUS (0)

_None_

---

## Discover & Search

**File key:** `PEMRwaRLpQaSD7rBxnQ4zF`

| Bucket | Count |
|---|---|
| MATCH-LINKED | 3 |
| MATCH-UNLINKED | 11 |
| MISSING | 12 |
| AMBIGUOUS | 0 |
| _Skipped (duplicates/informational)_ | _1_ |
| **Total unique capabilities** | **26** |

### MATCH-LINKED (3)

| Feature ID | Feature Name | Status | Journey | Figma File | Figma Caps |
|---|---|---|---|---|---|
| SAU-087 | Allocation Tracker | Planned | Saudi Market | Portfolios | Investment Allocation & Rebalancing |
| SAU-003 | Margin Lending (Murabaha) | Live | Saudi Market | Portfolios | Murabaha (from Discover) |
| SAU-026 | Tradable Rights Screen | Planned | Saudi Market | Portfolios | Tradable Rights |

### MATCH-UNLINKED (11)

Features exist in xlsx but have no `figma_link` set. Figma frames found in this file.

| Feature ID | Feature Name | Status | Journey | Section | Figma Caps |
|---|---|---|---|---|---|
| IPO-001 | Main Market IPO Subscribe | Live | IPOs | Mobile > IPO / Mobile > Discover | IPO Subscription |
| SAU-078 | Transfer Holdings | Planned | Saudi Market | Web > UI Discover | Holding Transfer |
| SAU-081 | Downloadable Reports | Planned | Saudi Market | Mobile > Reports | Reports — Transactions; Reports — Orders |
| SAU-082 | Gain/Loss Tax Report | Gap | Saudi Market | Mobile > Reports | Reports — Gain/Loss; Gain/Loss Report (Web) |
| SAU-004 | Nomu Subscription | Live | Saudi Market | Mobile > Nomuc | Nomuc Subscription |
| SAU-039 | Stock Screener | Gap | Saudi Market | Web > UI Discover | Stock Screener (Web) |
| US-003 | Shariah Compliance Lists | Live | US Trading | Web > UI Discover | Shariah Compliant List |
| XJ-001 | Zakat Calculator | Live | Cross-Journey | Mobile > Calculators | Calculators — Zakat |
| XJ-004 | ZATCA Purification Invoice | Planned | Cross-Journey | Mobile > Calculators | Calculators — Purification |
| XJ-008 | CRM Case Management | Planned | Cross-Journey | Mobile > Help Center | Help Center |
| XJ-022 | Discover & Search | Planned | Cross-Journey | Web > UI Discover / Mobile > Discover | Discover Hub |

### MISSING (12)

Capabilities visible in Figma with no matching feature in xlsx.

| # | Capability | Section | Notes | Suggested Journey | Suggested ID |
|---|---|---|---|---|---|
| 1 | Subscription Engine | Web > Subscription Engine / Mobile > Subscription Engine | Create/edit/cancel plans, ready-made plans, asset selection, allocation, execution history | Cross-Journey | XJ-0XX |
| 2 | Power of Attorney (PoA) | Web > POA / Mobile > PoA Request | Full PoA request flow, procedure type, products, list, status | Cross-Journey | XJ-0XX |
| 3 | Calculators — Stocks Dividend | Mobile > Calculators > sub-section | Dividend distribution list, calendar view, stock selector | Cross-Journey | XJ-0XX |
| 4 | Calculators — Smart Goal | Mobile > Calculators | Smart goal calculator entry | Cross-Journey | XJ-0XX |
| 5 | Offers / Promotions | Mobile > Offers | Three design variants for offers/promotions screen | Cross-Journey | XJ-0XX |
| 6 | Charity / Endowment | Mobile > Discover | Charity/donation, endowment funds, purification | Cross-Journey | XJ-0XX |
| 7 | Spin the Wheel | Mobile > Spin the wheel | Gamification — engagement/loyalty | Cross-Journey | XJ-039 |
| 8 | Client Money | Mobile > Discover | Client money balance, zero state, create/cancel request | Cross-Journey | XJ-0XX |
| 9 | My Suitability | Web > UI Discover | Full 12-step suitability questionnaire | Cross-Journey | XJ-0XX |
| 10 | Daily Market Reports Subscription | Web > UI Discover | Subscribe to daily market reports | Cross-Journey | XJ-0XX |
| 11 | Dividend List | Web > UI Discover | List of dividend distributions | Cross-Journey | XJ-0XX |
| 12 | Smart Investment | Web > UI Discover | Smart investment feature entry | Cross-Journey | XJ-0XX |

### AMBIGUOUS (0)

_None_

---

## Profile & Setting

**File key:** `cMRqMd2owWi3oBk5dV78TE`

| Bucket | Count |
|---|---|
| MATCH-LINKED | 0 |
| MATCH-UNLINKED | 9 |
| MISSING | 9 |
| AMBIGUOUS | 0 |
| _Skipped (duplicates/informational)_ | _8_ |
| **Total unique capabilities** | **18** |

### MATCH-LINKED (0)

_None_

### MATCH-UNLINKED (9)

Features exist in xlsx but have no `figma_link` set. Figma frames found in this file.

| Feature ID | Feature Name | Status | Journey | Section | Figma Caps |
|---|---|---|---|---|---|
| XJ-066 (was SAU-096) | Preference Settings | Planned | Cross-Journey | App Settings | Portfolio Preferences |
| US-003 | Shariah Compliance Lists | Live | US Trading | App Settings | Shariah Filter Toggle |
| XJ-008 | CRM Case Management | Planned | Cross-Journey | Customer Care | Customer Care / Message Centre; Web — Help Center |
| XJ-013 | Commission Discount Display | Planned | Cross-Journey | Commission Discount | Commission Discount Display |
| XJ-016 | Session Timeout Settings | Planned | Cross-Journey | Security & Access / App Settings | Session Timeout Settings |
| XJ-017 | Always On Display | Planned | Cross-Journey | App Settings | Always On Display |
| XJ-018 | Index Feed Bar Settings | Planned | Cross-Journey | App Settings | Index Feed Bar Settings |
| XJ-019 | Registered Devices | Planned | Cross-Journey | App Settings / Device Management | Registered Devices |
| XJ-021 | Tutorials & Education | Planned | Cross-Journey | Customer Care | Tutorials |

### MISSING (9)

Capabilities visible in Figma with no matching feature in xlsx.

| # | Capability | Section | Notes | Suggested Journey | Suggested ID |
|---|---|---|---|---|---|
| 1 | Password / MPIN Management | Security & Access | Change password, set/change MPIN | Cross-Journey | XJ-0XX |
| 2 | Face ID Setup | Profile and Setting (main) | Biometric authentication setup — 6 states | Cross-Journey | XJ-0XX |
| 3 | Theme Selection | Profile and Setting (main) | Light/dark theme toggle | Cross-Journey | XJ-0XX |
| 4 | Notification Settings | App Settings | Category-based notification toggles (orders, cash, portfolio, market, US) | Cross-Journey | XJ-0XX |
| 5 | Referral Program | Referral Program | Invite, share, track referrals, reward collection, redemption | Cross-Journey | XJ-042 |
| 6 | Personal Information | Personal Information | Profile dashboard, KYC, account details, bank cards management | Cross-Journey | XJ-0XX |
| 7 | Minor Trading Restrictions | Minor Trading Restriction | Max trade amount, max trades per day, max withdrawal, sector filter for minor | Cross-Journey | XJ-0XX |
| 8 | What's New | What's New | In-app release notes / feature announcements | Cross-Journey | XJ-0XX |
| 9 | National Address Update | Update National Address | Address update flow tied to NOMUC/account opening | Cross-Journey | XJ-0XX |

### AMBIGUOUS (0)

_None_

---

## LMS

**File key:** `DlJXkWsI2jb9MiRJrMpDwc`

| Bucket | Count |
|---|---|
| MATCH-LINKED | 1 |
| MATCH-UNLINKED | 2 |
| MISSING | 13 |
| AMBIGUOUS | 0 |
| _Skipped (duplicates/informational)_ | _1_ |
| **Total unique capabilities** | **16** |

### MATCH-LINKED (1)

| Feature ID | Feature Name | Status | Journey | Figma File | Figma Caps |
|---|---|---|---|---|---|
| LMS-001 | LMS Portfolio Home | Planned | LMS | Portfolios | LMS Home (Post-Activation) |

### MATCH-UNLINKED (2)

Features exist in xlsx but have no `figma_link` set. Figma frames found in this file.

| Feature ID | Feature Name | Status | Journey | Section | Figma Caps |
|---|---|---|---|---|---|
| SAU-009 | Margin Contract Renewal | Planned | Saudi Market | Section 1 > Renew | Loan Renewal |
| SAU-010 | Margin Early Payment | Planned | Saudi Market | Section 1 > Early Payment | Early Payment (Settlement) |

### MISSING (13)

Capabilities visible in Figma with no matching feature in xlsx.

| # | Capability | Section | Notes | Suggested Journey | Suggested ID |
|---|---|---|---|---|---|
| 1 | LMS Suitability Assessment | Web > Suitability / Section 1 > Suitability | 12-step suitability questionnaire for margin/lending account opening | LMS | LMS-0XX |
| 2 | LMS Application / Open Account | Web > 1 / Section 1 > STEP 1 | Apply for LMS, initial request, source account selection | LMS | LMS-0XX |
| 3 | Finance Allocation | Web > 2 | Enter/review finance amount, select purchase type | LMS | LMS-0XX |
| 4 | Continue Application Post-Approval | Section 1 > Continue Application | Complete fields post-approval, amount entry, portfolio selection, error states | LMS | LMS-0XX |
| 5 | Purchase Order — Commodity (Murabaha) | Section 1 > PO Commodity | Commodity-based Murabaha purchase order | LMS | LMS-0XX |
| 6 | Purchase Order — Stocks (Collateral) | Section 1 > PO Stocks | Stock collateral selection with percentage allocation — 4 states | LMS | LMS-0XX |
| 7 | Promissory Note & Contract Acceptance | Section 1 > Promissory Note | Review and sign Murabaha contract, order preview, success | LMS | LMS-0XX |
| 8 | New Profit Rate | Section 1 > New Profit Rate | Review/accept/decline new profit rate offer — 4 screens | LMS | LMS-0XX |
| 9 | Cancel Application | Section 1 > Cancel Application | Cancel LMS application mid-process | LMS | LMS-0XX |
| 10 | Fund / Collateral Changes | Section 1 > Fund Changes | Modify collateral fund/portfolio linked to LMS account | LMS | LMS-0XX |
| 11 | Expire Contract | Expire contract / Section 1 | Contract expiry notification/acknowledgment | LMS | LMS-0XX |
| 12 | Request Phone Call | Section 1 > Request Phone Call | Request callback from advisor | LMS | LMS-0XX |
| 13 | LMS Notifications & Alerts | Top-level | In-app notifications and push alert for LMS | LMS | LMS-0XX |

### AMBIGUOUS (0)

_None_

---

## Notes

1. **Deduplication across files:** Some capabilities appear in multiple files (e.g., Hive appears in both Home and Profile, Subscription Engine in Discover and Profile, Family Members in Home and Profile). Each is counted once in the first file where it appears; duplicates in later files are marked as "Skipped."
2. **Informational pages excluded:** "About Us," "About Brokerage," FAQ, and Rate Us are informational/engagement screens, not product features. They are not counted as MISSING.
3. **LMS is the most gap-heavy file:** The LMS Figma file shows a complete Murabaha lending lifecycle (17 capabilities), but the xlsx only has 5 LMS features (LMS-001 through LMS-005) plus 2 Saudi Market features (SAU-009, SAU-010) for margin. 12 new features are needed.
4. **Discover & Search is the largest cross-product file:** 560+ frames spanning IPO, subscriptions, reports, PoA, calculators, help center, investment allocation, charity, and more.
5. **Home contains Instant Settlement:** Maps to SAU-024 (Instant Settlement T+0/T+1) — this is a web-only flow currently.
6. **Subscription Engine is a major gap:** Full recurring investment plan feature designed across Discover (web + mobile) and Profile, with no matching xlsx feature.
7. **No xlsx or view changes made** -- this is a report-only cross-check.
