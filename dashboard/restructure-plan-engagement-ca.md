# Restructure Plan — Investor Engagement + Corporate Actions — 2026-05-08

> Executed on 2026-05-08. IDs in this file are the original plan — see features.json for final state. Cash Management journey added during execution (ENG-005/006/007).
>
> Note (2026-05-11): Post-restructure cleanup moved SAU-101 (was ENG-019 Trading Incentive Banners) → XJ-067 (Cross-Journey). SAU-099 (was ENG-004 Prepaid Commission Bundle) was not in final features.json — actual SAU-099 is Social / Copy Trading (status → Gap).

**Author:** Auto-generated from Figma cross-check data
**Status:** EXECUTED — see Phase 2 changes below
**Reference:** Same approach as Portfolio Monitoring / Wealth Visibility restructure (restructure-plan.md)

## Summary

- **ENG features to reassign:** 23
- **CA features to reassign:** 5
- **Total:** 28
- **Proposed new journey distribution:**

| Target Journey | Count |
|---|---|
| Cross-Journey | 19 |
| Saudi Market | 6 |
| Crowd Fund | 2 |
| US Trading | 1 |
| **Total** | **28** |

- **Features flagged for review:** 6
- **Journeys dissolved:** Investor Engagement, Corporate Actions
- **Allowed target journeys:** Onboarding, Saudi Market, US Trading, Mutual Funds, Crowd Fund, Robo Advisory, IPOs, Cross-Journey, LMS

## Method

1. **figma_file set on row** — none of the 28 ENG/CA features had a figma_file set. All were blank.
2. **figma_file blank — search 10 in-scope Figma files** (OnBoarding KYC, Market, Orders, Watchlist, Portfolios, Discover & Search, Profile & Setting, LMS, Home, Tradepad). Used the Figma cross-check reports (A1–A5) to find frames matching each feature by name/function. Found 9 matches.
3. **No Figma frame found** — used name-based judgment per the rules:
   - Engagement features clearly product-specific → that product's journey
   - Engagement features genuinely cross-cutting → Cross-Journey
   - Corporate Actions: dividends/splits/rights for Saudi → Saudi Market; for US → US Trading; generic capability → Cross-Journey
4. **Did NOT walk** Wealth Mgmt Dashboard, CDO, Bain, Themes, or Trader Mode (out of scope).

## Detail

| Old ID | Name | Status | Old Journey | figma_file (current) | figma_file (proposed) | Frame Found in Figma | Proposed New Journey | Proposed New ID | Confidence | Reason |
|---|---|---|---|---|---|---|---|---|---|---|
| ENG-001 | Bundle Benefits (ARG) | Planned | Investor Engagement | (blank) | (blank) | Not found in any of the 10 in-scope Figma files. | Cross-Journey | XJ-037 | Medium | ARG group loyalty bundle — cross-cutting, not tied to one product. |
| ENG-002 | Smart Saving Plan | Planned | Investor Engagement | (blank) | (blank) | Not found in any of the 10 in-scope Figma files. | Cross-Journey | XJ-038 | Low | Automated saving/investing mechanism. Could belong to Mutual Funds or Robo Advisory. Defaulted to Cross-Journey. Flagged. |
| ENG-003 | Spin the Wheel | Planned | Investor Engagement | (blank) | Discover & Search | Discover & Search file — "Spin the wheel" section (gamification/engagement screen). Listed as MISSING in A4 cross-check. | Cross-Journey | XJ-039 | High | Gamification feature in Discover hub — not product-specific. |
| ENG-004 | Prepaid Commission Bundle | Planned | Investor Engagement | (blank) | (blank) | Not found in any of the 10 in-scope Figma files. | Saudi Market | SAU-099 | Medium | Commission bundles primarily apply to Saudi equity trading (highest volume, commission-based). |
| ENG-005 | Mokafaa Points Redemption | Planned | Investor Engagement | (blank) | (blank) | Not found in any of the 10 in-scope Figma files. | Cross-Journey | XJ-040 | Medium | Al Rajhi Bank loyalty points redemption — cross-product, not tied to one journey. |
| ENG-006 | ARC Debit Card | Planned | Investor Engagement | (blank) | (blank) | Not found in any of the 10 in-scope Figma files. | Cross-Journey | XJ-041 | Low | Entirely new product category (banking/payments). No clear journey home. Flagged. |
| ENG-007 | Buy Round-Up | Planned | Investor Engagement | (blank) | (blank) | Not found in any of the 10 in-scope Figma files. | Cross-Journey | XJ-042 | Low | Micro-investing "round-up" feature. Could be Saudi-specific or cross-product. Flagged. |
| ENG-008 | Social / Copy Trading | Planned | Investor Engagement | (blank) | (blank) | Not found in any of the 10 in-scope Figma files. | Saudi Market | SAU-100 | Medium | Copy trading primarily targets Saudi equities (largest user base). Could also serve US Trading. |
| ENG-009 | Gifting List | Planned | Investor Engagement | (blank) | (blank) | Not found in any of the 10 in-scope Figma files. | Cross-Journey | XJ-043 | Medium | Gift stock/shares feature — applies across products. |
| ENG-010 | Referral / Gift Campaigns | Planned | Investor Engagement | (blank) | Profile & Setting | Profile & Setting file — "Referral Program" section: invite, share, track referrals, reward collection, redemption. Listed as MISSING in A4 cross-check. | Cross-Journey | XJ-044 | High | Referral Program found in Profile & Setting. Cross-product growth mechanism. |
| ENG-011 | Language Preference | Planned | Investor Engagement | (blank) | (blank) | Not found as a distinct frame in any of the 10 in-scope Figma files. Logical home: Profile & Setting (App Settings). | Cross-Journey | XJ-045 | High | App-level language setting — definitionally cross-product. |
| ENG-012 | Email Templates Revamp | Planned | Investor Engagement | (blank) | (blank) | Not found in any of the 10 in-scope Figma files. Back-end/communications feature, no UI expected. | Cross-Journey | XJ-046 | Medium | Cross-product communication templates, no specific journey. |
| ENG-013 | Charity / Donation Screen | Planned | Investor Engagement | (blank) | Discover & Search | Discover & Search file — "Charity / Endowment" section: charity/donation, endowment funds, purification. Listed as MISSING in A4 cross-check. | Cross-Journey | XJ-047 | High | Charity screen found in Discover hub — cross-product. |
| ENG-014 | Crowdfund Portfolios | Planned | Investor Engagement | (blank) | Portfolios | Portfolios file — "Crowdfund Portfolio Home" section (node 2007:50528): portfolio view, holding overview, holdings filter, choose portfolio. Listed as MISSING in A1 cross-check. | Crowd Fund | CF-005 | High | Crowdfund portfolio screens clearly belong to Crowd Fund journey. |
| ENG-015 | Crowd Funds Orders | Planned | Investor Engagement | (blank) | (blank) | Not found as a distinct order flow in the 10 in-scope Figma files. Crowdfund portfolio views exist in Portfolios file but not an order/subscription flow. | Crowd Fund | CF-006 | High | Crowd fund order flow — product-specific to Crowd Fund journey. |
| ENG-016 | Social Community Feed | Planned | Investor Engagement | (blank) | Home | Home file — "Hive (Community/Social)" section: Hive info flow, app rating prompt, content modals. Listed as MISSING in A4 cross-check. | Cross-Journey | XJ-048 | High | Hive/community feed found in Home — cross-product social feature. |
| ENG-017 | Ramadan Campaign | Planned | Investor Engagement | (blank) | (blank) | Not found in any of the 10 in-scope Figma files. Seasonal marketing. | Cross-Journey | XJ-049 | Low | Seasonal campaign — no Figma, no permanent product home. Flagged. |
| ENG-018 | Social Proof Nudge | Planned | Investor Engagement | (blank) | (blank) | Not found in any of the 10 in-scope Figma files. | Cross-Journey | XJ-050 | Low | Generic cross-cutting nudge/notification mechanism. No Figma frame. Flagged. |
| ENG-019 | Trading Incentive Banners | Planned | Investor Engagement | (blank) | (blank) | Not found as distinct frames. Discover file has "Offers / Promotions" (MISSING #5) which may relate, but too vague to link. | Saudi Market | SAU-101 | Medium | Trading incentive banners primarily drive Saudi equity trading activity. |
| ENG-020 | Cashback Prediction Game | Planned | Investor Engagement | (blank) | (blank) | Not found in any of the 10 in-scope Figma files. | Cross-Journey | XJ-051 | Low | Gamification — cross-product. No Figma frame. Flagged. |
| ENG-021 | Mokafaa Loyalty to Invest | Planned | Investor Engagement | (blank) | (blank) | Not found in any of the 10 in-scope Figma files. | Cross-Journey | XJ-052 | Medium | Convert ARB loyalty points to investments — cross-product mechanism. |
| ENG-022 | ARG Group Bundle Engine | Planned | Investor Engagement | (blank) | (blank) | Not found in any of the 10 in-scope Figma files. | Cross-Journey | XJ-053 | Medium | ARG group-level bundling engine — cross-cutting infrastructure. |
| ENG-023 | Gift Campaigns | Planned | Investor Engagement | (blank) | (blank) | Not found in any of the 10 in-scope Figma files. | Cross-Journey | XJ-054 | Medium | Cross-product gift/campaign feature. |
| CA-001 | Dividends Calendar (Intl) | Planned | Corporate Actions | (blank) | Watchlist | Watchlist file — "Dividends Screen" (node 2018:63412): dividend information for watchlist stocks. Listed as MISSING in A1 cross-check. | US Trading | US-030 | High | "Intl" in name = international market. Dividends calendar for US/international stocks. |
| CA-002 | Insider Trades Feed | Planned | Corporate Actions | (blank) | Watchlist | Watchlist file — "Insider Trades Screen" (node 2018:68787): insider trading activity for stocks in watchlist. Listed as MISSING in A1 cross-check. | Saudi Market | SAU-102 | Medium | Insider trade disclosure is primarily Tadawul-regulated. Watchlist screen covers Saudi equities first. |
| CA-003 | Purification Calculator | Planned | Corporate Actions | (blank) | Discover & Search | Discover & Search file — "Calculators" section includes purification frames. XJ-004 (ZATCA Purification Invoice) already mapped to same section. Partial match — CA-003 is calculator, XJ-004 is invoice. | Cross-Journey | XJ-055 | Low | Calculator utility — cross-product. Possible overlap with existing XJ-004. Flagged. |
| CA-004 | Dividend Calculator | Planned | Corporate Actions | (blank) | Discover & Search | Discover & Search file — "Calculators — Stocks Dividend" section (MISSING #3 in A4): dividend distribution list, calendar view, stock selector. | Saudi Market | SAU-103 | High | Dividend calculator designed in Discover hub. Primary use is Saudi equities dividends. |
| CA-005 | Rights Issue (Digital) | Planned | Corporate Actions | (blank) | (blank) | Not found as a distinct frame in the 10 in-scope Figma files. SAU-026 (Tradable Rights Screen) covers tradable rights but not the full rights issue subscription flow. | Saudi Market | SAU-104 | High | Saudi market rights offerings (Tadawul). Related to SAU-026 but distinct — this is the subscription/exercise flow. |

## Flagged for Review (6)

- **ENG-002** Smart Saving Plan → Cross-Journey (XJ-038) — No Figma. Could belong to Mutual Funds (automated fund saving) or Robo Advisory (goal-based investing) instead of Cross-Journey.
- **ENG-006** ARC Debit Card → Cross-Journey (XJ-041) — No Figma. Entirely new product category (banking/payments). No clear journey home. May need its own journey or be out of scope for DX features map.
- **ENG-007** Buy Round-Up → Cross-Journey (XJ-042) — No Figma. "Round-up" purchases concept could be Saudi-specific (most trading volume) rather than cross-product.
- **ENG-017** Ramadan Campaign → Cross-Journey (XJ-049) — No Figma. Seasonal campaign — unclear if this is a permanent product feature or a temporary marketing initiative.
- **ENG-020** Cashback Prediction Game → Cross-Journey (XJ-051) — No Figma. Gamification mechanism with no design and no clear product anchor.
- **CA-003** Purification Calculator → Cross-Journey (XJ-055) — Possible overlap with existing XJ-004 (ZATCA Purification Invoice). Both live in Discover Calculators section. Needs dedup review.

## ID Reassignment Summary

- **Saudi Market:** SAU-099 through SAU-104 (6 features)
  - SAU-099: ENG-004 Prepaid Commission Bundle
  - SAU-100: ENG-008 Social / Copy Trading
  - SAU-101: ENG-019 Trading Incentive Banners
  - SAU-102: CA-002 Insider Trades Feed
  - SAU-103: CA-004 Dividend Calculator
  - SAU-104: CA-005 Rights Issue (Digital)
- **US Trading:** US-030 (1 feature)
  - US-030: CA-001 Dividends Calendar (Intl)
- **Cross-Journey:** XJ-037 through XJ-055 (19 features)
  - XJ-037: ENG-001 Bundle Benefits (ARG)
  - XJ-038: ENG-002 Smart Saving Plan
  - XJ-039: ENG-003 Spin the Wheel
  - XJ-040: ENG-005 Mokafaa Points Redemption
  - XJ-041: ENG-006 ARC Debit Card
  - XJ-042: ENG-007 Buy Round-Up
  - XJ-043: ENG-009 Gifting List
  - XJ-044: ENG-010 Referral / Gift Campaigns
  - XJ-045: ENG-011 Language Preference
  - XJ-046: ENG-012 Email Templates Revamp
  - XJ-047: ENG-013 Charity / Donation Screen
  - XJ-048: ENG-016 Social Community Feed
  - XJ-049: ENG-017 Ramadan Campaign
  - XJ-050: ENG-018 Social Proof Nudge
  - XJ-051: ENG-020 Cashback Prediction Game
  - XJ-052: ENG-021 Mokafaa Loyalty to Invest
  - XJ-053: ENG-022 ARG Group Bundle Engine
  - XJ-054: ENG-023 Gift Campaigns
  - XJ-055: CA-003 Purification Calculator
- **Crowd Fund:** CF-005 through CF-006 (2 features)
  - CF-005: ENG-014 Crowdfund Portfolios
  - CF-006: ENG-015 Crowd Funds Orders

## Post-Restructure Counts

After applying this plan (and the previous PRT/WLT restructure), the journey distribution would be:

| Journey | Before PRT/WLT | After PRT/WLT | After ENG/CA | Delta from ENG/CA |
|---|---|---|---|---|
| Onboarding | 42 | 42 | 42 | -- |
| Saudi Market | 72 | 98 | **104** | +6 |
| US Trading | 27 | 29 | **30** | +1 |
| Mutual Funds | 23 | 23 | 23 | -- |
| Crowd Fund | 4 | 4 | **6** | +2 |
| Robo Advisory | 12 | 12 | 12 | -- |
| LMS | 5 | 5 | 5 | -- |
| IPOs | 8 | 8 | 8 | -- |
| Cross-Journey | 30 | 36 | **55** | +19 |
| ~~Corporate Actions~~ | 5 | 5 | **0** | dissolved |
| ~~Investor Engagement~~ | 23 | 23 | **0** | dissolved |
| ~~Portfolio Monitoring~~ | 28 | 0 | 0 | already dissolved |
| ~~Wealth Visibility~~ | 6 | 0 | 0 | already dissolved |
| **Total** | **285** | **285** | **285** | **0 net** |

## Figma Coverage

| Category | Count |
|---|---|
| Frame found in in-scope Figma file | 9 |
| No frame found (name-based judgment) | 19 |
| **Total** | **28** |

Of the 9 Figma matches:
- Discover & Search: 4 (ENG-003, ENG-013, CA-003, CA-004)
- Watchlist: 2 (CA-001, CA-002)
- Profile & Setting: 1 (ENG-010)
- Portfolios: 1 (ENG-014)
- Home: 1 (ENG-016)

## Impact on Schema & Views

When this plan is executed, the following files will need updating:

1. **features-master.xlsx** — change journey + id on 28 rows; update figma_file on 9 rows; update data validation dropdown (remove ENG/CA journeys)
2. **SCHEMA.md** — remove Investor Engagement and Corporate Actions from journey enum, remove ENG/CA prefixes
3. **scripts/build_template.py** — remove from JOURNEYS list
4. **scripts/xlsx-to-features-json.py** — remove from JOURNEYS set and JOURNEY_PREFIX dict
5. **views/cockpit.html, heatmap.html, atlas.html** — remove from JOURNEYS arrays
6. **data/features.json** — regenerated by export script

**This plan does not execute any of the above.** It is a report for Ahmed's review.

*Source: Figma cross-check reports A1–A5 (2026-05-05 to 2026-05-06) + features.json (285 features) · 2026-05-08*
