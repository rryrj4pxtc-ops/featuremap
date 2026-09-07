# Restructure Plan — Dissolve Portfolio Monitoring & Wealth Visibility

**Date:** 2026-05-06 (revised)
**Author:** Auto-generated from Figma cross-check data
**Status:** PLAN ONLY — no files modified

> Note (2026-05-11): SAU-096 (was PRT-021 Preference Settings) subsequently moved to XJ-066 (Cross-Journey). See features.json for current state.
**Revision:** v2 — Correction 1 (WLT figma_file verified) + Correction 2 (Portfolios features reassigned to product journeys)

## Summary

- **Total features to reassign:** 34 (28 PRT + 6 WLT)
- **Proposed new journey distribution:**
  - Saudi Market: 26
  - US Trading: 2
  - Cross-Journey: 6
- **Features flagged for review:** 5
- **Journeys dissolved:** Portfolio Monitoring, Wealth Visibility
- **Allowed target journeys:** Onboarding, Saudi Market, US Trading, Mutual Funds, Crowd Fund, Robo Advisory, IPOs, Corporate Actions, Investor Engagement, Cross-Journey, LMS

## Corrections Applied

### Correction 1 — WLT figma_file values verified
All 6 WLT features previously showed `figma_file = "Wealth Mgmt Dashboard"` (out of scope). Searched all 10 in-scope Figma files:
- **WLT-001** Cash-In from ARB → **Home** (Deposit & Transfer section, 'Alrajhi Bank' source)
- **WLT-002** Aggregated Cash & Buying Power → **Home** (Dashboard - Main, 'Total Cash' modal + Cash section)
- **WLT-003** UCM Multi-Currency Wallet → **blank** (not found in any in-scope file)
- **WLT-004** Multi Virtual IBANs → **blank** (partial: single IBAN in Discover, not multi/virtual)
- **WLT-005** ZATCA Wallet Invoices → **blank** (partial: VAT popup in Discover, not ZATCA wallet invoices)
- **WLT-006** Apple Pay / Digital Wallet → **Home** (Web: 3 Apple Pay frames in Deposit & Withdraw)

### Correction 2 — Portfolios features → actual product sections
The Portfolios file's "Portfolio Analysis" section, "Smart Goal" section, and "Digital StoryTeller" page are NOT product-specific sections, but their content defaults to or explicitly references Saudi Market:
- **Portfolio Analysis section** (PRT-004, 005, 006, 007, 019, 023) → analytics hub that defaults to Saudi as primary portfolio → **Saudi Market**
- **Smart Goal section** (PRT-008) → frame text references "Margin Trading Available" → **Saudi Market**
- **Digital StoryTeller page** (PRT-009, 026, 027) → frame text shows "Saudi Market Profit Growth" → **Saudi Market**
- **Holdings Filter / Sector-Index-Shariah Filters** (PRT-012, 014) → primary frames in Saudi Portfolios section → **Saudi Market**
- **PRT-021** Preference Settings → found in Profile & Setting file, not Portfolios → **Saudi Market** (portfolio display defaults to Saudi)
- **PRT-024, PRT-025** → no frame found → **Saudi Market** (inferred)

**Result:** 0 features assigned to Cross-Journey from Portfolios file (was 14 in v1).

## Method

1. **figma_file set** → walked that Figma file, found the frame, identified the parent section, inferred journey from section context.
2. **figma_file = Portfolios** → used Portfolios file section mapping:
   - Saudi Portfolios section → Saudi Market
   - US Portfolios section → US Trading
   - Mutual Fund Portfolios → Mutual Funds
   - Crowdfund Portfolios → Crowd Fund
   - LMS Portfolios → LMS
   - Mashura Portfolios → Robo Advisory
   - Portfolio Analysis section → Saudi Market (primary portfolio, analytics entry point)
   - Smart Goal section → Saudi Market (references margin trading)
   - Digital StoryTeller page → Saudi Market (content shows "Saudi Market Profit Growth")
   - Saudi Portfolios - Reporting → Saudi Market
3. **figma_file = Wealth Mgmt Dashboard** → out of scope. Searched 10 in-scope files by feature name. Updated figma_file to correct file or blank.
4. **No Figma frame found** → used name/definition to assign. Flagged for review.

## Detail

| Old ID | Name | Status | Old Journey | figma_file (corrected) | Frame Found in Figma | New Journey | New ID | Confidence |
|---|---|---|---|---|---|---|---|---|
| WLT-001 | Cash-In from ARB | Live | Wealth Visibility | Home | Home file — Mobile: Deposit & Transfer section (3010:124817), 'From' screen shows 'Alrajhi Bank' chip. Web: UI Deposit & Withdraw, 'Select Source: alrajhi Bank' (3012:209993). | Cross-Journey | XJ-031 | High |
| WLT-002 | Aggregated Cash & Buying Power | Planned | Wealth Visibility | Home | Home file — Mobile: Dashboard - Main, 'Modal' frame (3010:100980) shows 'Total Cash' with portfolio chips: All, Saudi, US, MF, Crowd, Robo. Also Cash section 'Cash overview' (3010:129750+). | Cross-Journey | XJ-032 | High |
| WLT-003 | UCM Multi-Currency Wallet | Planned | Wealth Visibility | (blank) | Not found in any of the 10 in-scope Figma files. No frames for UCM, multi-currency, or wallet. | Cross-Journey | XJ-033 | Low |
| WLT-004 | Multi Virtual IBANs | Planned | Wealth Visibility | (blank) | Partial match only: Discover file has single IBAN frame (2005:158093) in Subscription Engine. Not multi/virtual IBAN routing. | Cross-Journey | XJ-034 | Low |
| WLT-005 | ZATCA Wallet Invoices | Planned | Wealth Visibility | (blank) | Partial match only: Discover file has 'popup for VAT Registration certificate' (2004:7231). Not ZATCA wallet invoices. | Cross-Journey | XJ-035 | Low |
| WLT-006 | Apple Pay / Digital Wallet | Gap | Wealth Visibility | Home | Home file — Web: UI Deposit & Withdraw, 'Apple Pay' frames (3012:213196, 3012:213464, 3012:213560). Mobile: 'Apple pay' chip in From screen. | Cross-Journey | XJ-036 | High |
| PRT-001 | Saudi Portfolio Holdings | Live | Portfolio Monitoring | Portfolios | Saudi Portfolios section — Home frames (2007:25488+) | Saudi Market | SAU-073 | High |
| PRT-002 | Holdings Letter (PDF) | Live | Portfolio Monitoring | Portfolios | Saudi Portfolios - Reporting section (2108:84728+) | Saudi Market | SAU-074 | High |
| PRT-003 | Performance Chart | Planned | Portfolio Monitoring | Portfolios | Saudi Portfolio Overview section on Perf Analysis page (2029:46047+) | Saudi Market | SAU-075 | Medium |
| PRT-010 | Analyst Ratings | Planned | Portfolio Monitoring | Watchlist | Watchlist file — LINKED (2018:58217) | Saudi Market | SAU-076 | Medium |
| PRT-013 | Saudi Portfolio Selector | Planned | Portfolio Monitoring | Portfolios | Saudi Portfolios section — Choose Portfolio (2007:29544) | Saudi Market | SAU-077 | High |
| PRT-015 | Transfer Holdings | Planned | Portfolio Monitoring | Portfolios | Saudi Portfolios section — Transfer Holdings (2007:29689+) | Saudi Market | SAU-078 | High |
| PRT-016 | Add to Watchlist | Planned | Portfolio Monitoring | Portfolios | Saudi Portfolios section — Add Holdings to watchlist (2007:35066+) | Saudi Market | SAU-079 | High |
| PRT-017 | Liquidate Holdings | Planned | Portfolio Monitoring | Portfolios | Saudi Portfolios section — Liquidate (2007:38601+) | Saudi Market | SAU-080 | High |
| PRT-020 | Downloadable Reports | Planned | Portfolio Monitoring | Portfolios | Saudi Portfolios - Reporting section (2108:84728+) | Saudi Market | SAU-081 | Medium |
| PRT-022 | Gain/Loss Tax Report | Gap | Portfolio Monitoring | Portfolios | Saudi Portfolios - Reporting section (within Reports frames) | Saudi Market | SAU-082 | Medium |
| PRT-028 | More Options Menu (Saudi) | Planned | Portfolio Monitoring | Portfolios | Saudi Portfolios section — More option (2007:28734) — LINKED | Saudi Market | SAU-083 | High |
| PRT-004 | Peer Portfolio Comparison | Planned | Portfolio Monitoring | Portfolios | Portfolio Analysis section (2106:59106) — Peers Compare. Generic analytics section on Perf Analysis page, defaults to Saudi as primary portfolio. | Saudi Market | SAU-084 | Medium |
| PRT-005 | Portfolio Insights | Planned | Portfolio Monitoring | Portfolios | Portfolio Analysis section (2050:13176-14178) — Portfolio insights frames. Generic analytics on Perf Analysis page. | Saudi Market | SAU-085 | Medium |
| PRT-006 | Portfolio Health Score | Planned | Portfolio Monitoring | Portfolios | Portfolio Analysis section (2050:14786) + Saudi Portfolio Overview (2029:45691). Health Score appears in both generic and Saudi-specific sections. | Saudi Market | SAU-086 | High |
| PRT-007 | Allocation Tracker | Planned | Portfolio Monitoring | Portfolios | Portfolio Analysis section (2106:58522) — LINKED. 'Allocation' frame with Sectors Allocations Trend. | Saudi Market | SAU-087 | Medium |
| PRT-019 | Analysis Dashboard | Planned | Portfolio Monitoring | Portfolios | Portfolio Analysis section — Home (2112:112583). Dashboard entry point for analytics. | Saudi Market | SAU-088 | Medium |
| PRT-023 | Visual Asset Allocation | Gap | Portfolio Monitoring | Portfolios | Portfolio Analysis section — Allocation (2106:58522) + Cash Allocation (2106:58654). Granular allocation breakdown. | Saudi Market | SAU-089 | Medium |
| PRT-008 | Goal Tracker | Planned | Portfolio Monitoring | Portfolios | Smart Goal section (2268:71295) on Portfolios page. Standalone section peer-level to product sections. Frame text references 'Margin Trading Available'. | Saudi Market | SAU-090 | Medium |
| PRT-009 | Storyteller (Quarterly) | Planned | Portfolio Monitoring | Portfolios | Digital StoryTeller page — ARCD-19542 section (2123:68777+). Frame text: 'Saudi Market Profit Growth'. | Saudi Market | SAU-091 | High |
| PRT-026 | Digital StoryTeller | Planned | Portfolio Monitoring | Portfolios | Digital StoryTeller page — ARCD-19542 section (2123:68777+). 45 frames of visual narratives. 'Saudi Market Profit Growth'. | Saudi Market | SAU-092 | High |
| PRT-027 | Storyteller Report | Diff | Portfolio Monitoring | Portfolios | Digital StoryTeller page — same frames as PRT-026. Exportable report version of StoryTeller. | Saudi Market | SAU-093 | High |
| PRT-012 | Holdings Filter Panel | Planned | Portfolio Monitoring | Portfolios | Saudi Portfolios section — Index - Filter (2007:25898). Also MF (2007:42621) and CF (2007:51068). | Saudi Market | SAU-094 | High |
| PRT-014 | Sector/Index/Shariah Filters | Planned | Portfolio Monitoring | Portfolios | Saudi Portfolios section — Sectors (2007:28669), Index (2007:25898), Shariah (2007:29592). Also US, LMS, Mashura. | Saudi Market | SAU-095 | High |
| PRT-021 | Preference Settings | Planned | Portfolio Monitoring | Profile & Setting | Profile & Setting file (cMRqMd2owWi3oBk5dV78TE) — Portfolio Preferences section. Not in Portfolios file. | Saudi Market | SAU-096 | Medium |
| PRT-024 | Batch Close Positions | Gap | Portfolio Monitoring | Portfolios | No standalone frame — likely within Liquidate flow in Saudi Portfolios section. | Saudi Market | SAU-097 | Low |
| PRT-025 | Auto Dividend Reinvest | Gap | Portfolio Monitoring | Portfolios | No frame found in any in-scope Figma file. Design gap. | Saudi Market | SAU-098 | Low |
| PRT-011 | Earnings Calendar (Intl) | Planned | Portfolio Monitoring | Watchlist | Watchlist file — LINKED (2018:66195) | US Trading | US-028 | High |
| PRT-018 | US Portfolio Selector | Planned | Portfolio Monitoring | Portfolios | US Portfolios section — Choose Portfolio (2007:42082) | US Trading | US-029 | High |

## Flagged for Review (5)

- **WLT-003** UCM Multi-Currency Wallet → Cross-Journey (XJ-033) — Design gap — no Figma representation. Flagged for review.
- **WLT-004** Multi Virtual IBANs → Cross-Journey (XJ-034) — No frame matching multi-virtual-IBAN routing. Flagged for review.
- **WLT-005** ZATCA Wallet Invoices → Cross-Journey (XJ-035) — No frame matching ZATCA wallet e-invoices. Flagged for review.
- **PRT-024** Batch Close Positions → Saudi Market (SAU-097) — Gap feature. No dedicated frame. Inferred from Liquidate context. Flagged.
- **PRT-025** Auto Dividend Reinvest → Saudi Market (SAU-098) — Gap feature. No Figma frame anywhere. Dividend reinvest most relevant to Saudi equities. Flagged.

## ID Reassignment Summary

- **Saudi Market:** SAU-073 through SAU-098 (26 features)
- **US Trading:** US-028 through US-029 (2 features)
- **Cross-Journey:** XJ-031 through XJ-036 (6 features)

## Post-Restructure Counts

After applying this plan, the journey distribution would be:

| Journey | Current | Added from PRT/WLT | New Total |
|---|---|---|---|
| Onboarding | 42 | -- | 42 |
| Saudi Market | 72 | +26 | **98** |
| US Trading | 27 | +2 | **29** |
| Mutual Funds | 23 | -- | 23 |
| Crowd Fund | 4 | -- | 4 |
| Robo Advisory | 12 | -- | 12 |
| LMS | 5 | -- | 5 |
| IPOs | 8 | -- | 8 |
| Corporate Actions | 5 | -- | 5 |
| Investor Engagement | 23 | -- | 23 |
| Cross-Journey | 30 | +6 | **36** |
| ~~Portfolio Monitoring~~ | 28 | dissolved | **0** |
| ~~Wealth Visibility~~ | 6 | dissolved | **0** |
| **Total** | **285** | **0 net** | **285** |

## Impact on Schema & Views

When this plan is executed, the following files will need updating:

1. **features-master.xlsx** — change journey + id on 34 rows; update figma_file on 4 WLT rows; update data validation dropdown (remove PRT/WLT journeys)
2. **SCHEMA.md** — remove Portfolio Monitoring and Wealth Visibility from journey enum, remove PRT/WLT prefixes
3. **scripts/build_template.py** — remove from JOURNEYS list
4. **scripts/xlsx-to-features-json.py** — remove from JOURNEYS set and JOURNEY_PREFIX dict
5. **views/cockpit.html, heatmap.html, atlas.html** — remove from JOURNEYS arrays
6. **data/features.json** — regenerated by export script

**This plan does not execute any of the above.** It is a report for Ahmed's review.
