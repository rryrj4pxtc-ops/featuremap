# Progress — Features Map

## Final Goal
Maintain a comprehensive, always-current map of every feature in the ARC app — catalogued by journey, squad, live status, and competitive gap — used as the input for roadmap prioritization and platform maturity scoring.

---

## Required Steps

- [x] 1. Extract all features currently live in the ARC app — screen by screen, flow by flow
- [x] 2. Review all BRDs in `assets/BRDs/` — 112 features extracted from 95+ BRDs
- [x] 3. Map each feature to its squad and journey — done in features-inventory.md. 154 total features: 44 BRD+Figma confirmed, 68 BRD-only, 42 Figma-only (no BRD exists).
- [x] 4. Identify features present in competitor apps but absent in ARC — mark as gap. 47 gaps identified, saved to `competitor-gap-matrix.md`.
- [x] 5. Identify ARC features not found in any competitor — mark as differentiator. 14 differentiators identified in `competitor-gap-matrix.md`.
- [x] 6. Score each gap feature: investor demand × competitive pressure = priority score. Top 20 gaps scored (max 25). Highest: Level 2 Order Book, Stock Screener, Pre/Post Market Trading (all score 25).
- [x] 7. Validate feature list with squad leads — `squad-validation-checklist.md` created and ready to share. Deadline: April 7, 2026.
- [x] 8. Publish features map as living document — `features-map-published.md` created.
- [x] 9. Cross-reference with product-clarity-map — `clarity-map.md` created in product-clarity-map project. Covers ownership, documentation debt, discoverability, and competitor gap column.
- [x] 10. Feed gap features into platform-maturity scoring — maturity framework defined, baseline scoring running.
- [x] 11. Visual Features Map PPTX deck — 16-slide presentation using pptxgenjs design system. Built 2026-04-21.
- [x] 12. Deep Figma extraction — 2.27M nodes, 262K text layers, 246K instances across 8 files. 10 new features discovered. Built 2026-04-21.
- [x] 13. Platform parity matrix — CONFIRMED: All 8 modules have Mobile + Web + Tablet designs (3/3 coverage).
- [x] 14. Deep Features Map deck — 20-slide enhanced presentation with extraction findings, gap status updates, terminology map, design activity timeline. Built 2026-04-21.
- [x] 15. Excel validation export — 164 features exported to `reports/features-map-validation-2026-04-22.xlsx` with 3 sheets (All Features, Summary by Squad, Instructions). Color-coded status, validation columns for squad leads. Built 2026-04-22.
- [x] 16. Depth analysis — 36 features traced, avg 4.9 taps. 42% at friction risk (6+ taps). Saved to `depth-analysis.md`. Built 2026-04-24.
- [x] 17. Journey-to-feature mapping — 5 core journeys mapped to 141 features (23 orphans). Cross-journey overlap: 18 shared features. Saved to `journey-to-feature-mapping.md`. Built 2026-04-24.
- [x] 18. Update inventory from 154 → 164 features — 10 deep-extraction discoveries added (#155-164). Inventory, published map, and summary counts updated. Built 2026-04-24.
- [x] 19. Knowledge Bank integration — features-master.xlsx `brd` codes joined to `brd-index.md` via `knowledge_bank.py`. Feature↔BRD cross-reference published to `knowledge-bank/feature-brd-crossref.md`, read by all 22 projects + 9 reports. Built 2026-08-06.
- [x] 20. BRD refresh — knowledge bank grown from 100 → 196 BRDs across recent batches. All new BRDs scanned, indexed, and joined to features. Underscore-named codes (`ARCD_2647`, `ARCD_9245`) fixed in the code parser. Built 2026-08-06.
- [x] 21. Cancellation handling — ARCD-74031 and ARCD-73474 marked cancelled (`cancelled-brds.txt`). ONB-007 (Expired ID Handling) re-pointed to its correct replacement BRD ARCD-99958. RBO-001/002/003 flagged as needing a replacement Robo BRD. Built 2026-08-06.
- [x] 22. Code-collision cleanup — resolved two duplicate ARCD codes: 60887 (kept Custom Index Against Benchmark per feature XJ-055; corrected Portfolio Backtesting's filename) and 2647 (archived a stray Client Money copy, kept Phase 1). Each code now resolves to exactly one BRD. Built 2026-08-06.
- [x] 23. BRD→feature mapping drive — worked every unlinked BRD into a feature by domain (exact-concept, order-types, FATCA, LMS/margin, mutual funds, robo/Mashura, news/notifications). **44 BRDs mapped**; with-BRD 137 → 166 (152 resolve to KB), no-BRD 286 → 257. Closed all cancelled-BRD gaps (ONB-007→99958, RBO-001→22648, RBO-002/003→85842) and the entire LMS journey (0→7/7). Remaining unlinked BRDs classified in `knowledge-bank/brd-mapping-review.md` as BACKEND (10) or NEW-FEATURE candidates (7). Built 2026-08-10.
- [x] 24. US Trading gap analysis — tiered the 67 US no-BRD features (`us-trading-brd-gap.md`): 11 US parallels linked to their existing cross-market BRD (US gap 67 → 56, with-BRD 166 → 177). Remaining 56 = 9 Saudi-specific twins (US needs own BRD) + 27 undocumented in both markets (dual-market BRD) + 20 US-unique (net-new). Backlog handed to the US Trading squad. Built 2026-08-10.
- [x] 25. Saudi Market gap analysis — as the source market, only 1 linkable duplicate (SAU-118 Performance Chart → ARCD-2654; gap 58 → 57). Grouped the remaining 57 into 5 capability families (`saudi-market-brd-gap.md`): Order management (16), Discovery & market data (14), Portfolio & holdings (13), Charting & technical analysis (9), Products & trading (5). Flagged duplicate feature rows (Dividends ×3, Earnings ×2) for consolidation. Priority: SAU-040 Advanced Technical Analysis (indicators/Ichimoku — active competitor gap). Built 2026-08-10.
- [x] 26. Onboarding gap analysis — the 83 gap is inflated by **account-type duplication** (same screen ×5 per ARB/Local/Global/Corporate/Minor). Linked 19 documented variants (10 Corporate sub-screens→2958, 4 Login→89063, 5 Guest Mode→75522); gap 83 → 64. Grouped remaining 64 into 12 screen-families + 4 singletons (`onboarding-brd-gap.md`) — collapses to **~16 BRDs, not 64**. Recommended consolidating the 5×-duplicated rows in the map. Onboarding with-BRD 35 → 54; overall 178 → 197. Built 2026-08-10.
- [x] 27. Onboarding duplicate consolidation — merged the 5×-per-account-type screen rows: 18 screen-families × 4 empty variants = **72 rows removed** (variants differed only by `area`; account types preserved in an `account-types` tag on the canonical). Total features **423 → 351**, Onboarding **118 → 46**, onboarding gap **64 → 16** (the true BRD count). Remapped 16 orphaned competitor findings in `coverage.json` to their canonical feature. Atlas tree + all 4 dashboard views verified. Built 2026-08-10.
- [x] 28. US↔Saudi market parity — reconciled the two markets to mirror each other. Matched pairs 48 → 88: renamed ~23 naming-artifact pairs to identical base names (Saudi = base, US = base; journey distinguishes them), mirrored 18 shared features as Gaps into the market that lacked them (Margin/Murabaha, Sukuk, Shariah, Options, Limit/Market Order, AI Assistant, Stock Profile/Search, order screens…), and deleted 6 non-features/duplicates (Nomu, Arabic ×2, Portfolio Selector, dividends + options dups). Genuine market exceptions kept: Pre-Auction, Rights Issue, Tradable Rights (Saudi); Bonds, Pre/Post-Market (US). Features 351 → 365; Saudi 93 / US 94 (now symmetric). Built 2026-08-11.
- [x] 29. Manual live-status verification — Ahmed reviewed all 63 Live-but-unverified features. **55 now evidence-verified Live** in `data/verified_live.json` (`method: manual_confirmation`, was 6). **11 corrected off Live:** US-017/XJ-037/XJ-038 → Gap; SAU-029/037/044/067/068/075/119 → Planned. **4 duplicate rows removed** (US-082/083/084 Dividends/Earnings dups, SAU-118 Performance Chart dup) — features 365 → 361. Live Rate (D4) is now evidence-based; maturity recomputed = 38.6 (was 40.0 on hand-claimed Live). See `live-verification-checklist.md`. Built 2026-08-11.
- [x] 30. Cross-market parity rule + Unverified cleanup — added **Rule 4.5** to `derive_status.py`: a bare Gap (no competitor, no BRD/Figma) whose same-base-name twin in the *sibling market* (Saudi↔US) is substantiated (Live/BRD/verified) is a confirmed *internal* parity gap → derived **Gap** with `parity_gap: true`, not "Unverified". This pulled **Unverified 84 → 23** (60 features reclassified as real internal gaps). Removed 1 more duplicate (SAU-117 = SAU-107 Earnings Calendar) → 360 features. Maturity unchanged (38.6 — parity gaps carry no competitor pressure, so D5/critical counts are unaffected). Confirmed the 23 residual have **no BRD anywhere in the KB** — they are genuine documentation debt for squad triage. Built 2026-08-11.
- [x] 31. Residual Unverified triage — Ahmed hand-adjudicated the final 23. Added **Rule 0.5** to `derive_status.py` (authoritative Head-of-DX determinations via `data/manual_status.json`, the Gap/Planned analogue of `verified_live.json`). Outcome: **7 → Live** (incl. P/L History pair SAU-021+US-074 renamed from "P/L History (Sold Stocks)"; MF-024, XJ-054, XJ-062, XJ-064, ONB-043), **13 → Gap** (Chain Order, Unusual Activity, Fast Order, Minichart, Pre-Auction, Bonds, US IPO, Cancel Fund Portfolio, Smart Saving Plan…), **2 → Planned** (MF-015 Top Fund Holders, MF-016 Fund Financial Reports), **1 removed** (XJ-035 ZATCA Wallet Invoices). **Unverified 23 → 0** (359 features). verified_live 62 · manual_status 15. Maturity 38.6 → **39.4**. Built 2026-08-11.
- [x] 32. Planned-backlog verification pass — Ahmed reviewed all **158 Planned** features across 11 journeys, one journey at a time. Net result: **+56 confirmed Live** (verified_live 62 → 118), many → Gap (via manual_status), **27 removed** (non-features/dupes/deprecated: 359 → 332 features), and several reclassified/moved: XJ-005 → US Trading; XJ-055/058/063 moved to Saudi Market with new **US mirrors US-102/103/104**; renames (Tutorials & Education → **Education**, Preference Settings → **Portfolio Preference**); SAU-075 flagged Live-but-limited-to-3-months; SAU-008 partly shipped (ARCD-1923 live, 85843/86236 planned phases). **Planned 158 → 51** (the residual true delivery backlog). Maturity **39.4 → 47.7** (LMS 76, Crowd Fund/Onboarding 72; US Trading still weakest at 20.9). Built 2026-08-11.

- [x] 33. Saudi Market deep dive — **Stock Page** area (19 features). Sourced the gap backlog against the Nov-2025 trading gap research: **5 of 8 gaps now carry competitor evidence** (Analyst Ratings, Whale/Institutional, Why Is It Moving, Insider Trades, Unusual Activity); 31 coverage cells added dated to the research, not today. Unfounded gaps matrix-wide **50 → 38**; features with pressure > 0 **52 → 65**. Webull added to Benchmarks (OKX excluded — crypto). Four findings: (a) **47% of Stock Page rows are `stock-page-dup-of:` mirrors**, so the 36.8% maturity figure is an artifact and isn't comparable to other areas; (b) ⚠️ the evidence is **US-market** — the research's Saudi section contains none of these rows, so Saudi gaps are justified by competitors' US products (tagged `benchmark:trading-gaps-2025`); (c) **Bulls vs Bears is a differentiator, not a gap** — no competitor local or global has it and US-117 is Live; (d) parity breaks — US ships Why Is It Moving / Bulls vs Bears / Insider Trades / Government Trades that Saudi lacks, and **Analyst Ratings has no US mirror**. Ahmed adjudicated the four open items same day: SAU-045 **stays Planned** (research tick is an uncorroborated ARC self-assessment; upholds the 2026-08-11 determination), **impact scored** on 16 rows (backlog now rankable — top gaps Why Is It Moving / Whale / Analyst Ratings at priority 4), **Analyst Ratings US mirrors added** (US-137 Market + US-138 Stock Page, restoring the Market+Stock Page pattern), and a **benchmark check commissioned** for the two unbenchmarked rows (Strategy & Intelligence, due 2026-08-28 — `reports/benchmark-check-request-2026-08-16.md`). Features 333 → 335; pressure > 0: 52 → 67. See `reports/saudi-stock-page-deepdive-2026-08-16.md`. Built 2026-08-16.

- [x] 34. Saudi Market deep dive — **Orders** area (21 features). First area with **genuine Saudi-market evidence**: the research's Saudi matrices (pp.3, 6) benchmark order types on Tadawul, unlike the Stock Page set. Sourced 6 rows — **Bracket Order (OCO)** ← Sahm + Derayah and **Iceberg Order** ← Sahm + SNB Capital are real Tadawul gaps; Futures and Fast Order sourced from US matrices only. **SNB Capital + Riyad Bank added to Benchmarks** (18 → 20). Introduced **`evidence-market:saudi` / `evidence-market:us` tags**, retro-applied to the 10 Stock Page rows, so US-sourced justification for Saudi rows is now one query instead of document archaeology. Impact scored on 17 rows (Limit/Market Order 5; risk-management 3). **Top gap: SAU-047 Bracket Order (OCO), priority 4 on Saudi evidence** — better evidenced than any Stock Page gap. Four map-vs-research status discrepancies flagged (XJ-015 + SAU-042 marked Live but research shows planned; SAU-047 Gap vs planned; SAU-044 cites Sahm but Saudi research shows Sahm ✗). SAU-105 Chain Order + SAU-106 Trailing Order remain unbenchmarked — folded into the 2026-08-28 check. Unfounded gaps 38 → 35; pressure > 0: 67 → 70. **Ahmed then added 5 missing order-management capabilities**, all Live and mirrored to US as Live: Edit Order (SAU-145/US-139), Cancel Order (SAU-146/US-140), Orders History (SAU-147/US-141), Customize Orders View (SAU-148/US-142), Convert to Market Order (SAU-149/US-143) — each with a `verified_live.json` manual-confirmation record so D4 stays evidence-based. **Saudi Orders 21 → 26 features, 61.9% → 69.2% mature**; matrix 335 → 345, Live 182 → 192. See `reports/saudi-orders-deepdive-2026-08-16.md`. Built 2026-08-16.

- [x] 35. Saudi Market — status determinations + duplicate collapse (Ahmed, 2026-08-16). **SAU-047 Bracket Order Gap → Planned** and **XJ-015 Liquidity Indicators Live → Planned** (both supersede the 2026-08-11 records; XJ-015's `verified_live` entry removed since it can no longer be Live-verified; typed column reconciled). SAU-042 + SAU-044 re-confirmed Live. **SAU-044's Sahm citation removed** — traced to a low-confidence `legacy_xlsx` carry-over contradicted by the Saudi matrix (coverage cell kept as `supports:no` for audit). **Analyst Ratings duplication corrected**: US-137/US-138 (added earlier the same day on a faulty "no US mirror" finding) deleted — US-067/US-127 already existed as "Analyst Ratings (US)"; the `(US)` suffix had hidden them from name matching. Both renamed to the parity convention and given the evidence; **24 rows still carry a (US)/(Saudi) suffix** and remain collision-prone. **Impact propagated to the 9 Market parents** of the Stock Page duplicates. **Government Trades and Insider Trades collapsed**: SAU-069 + SAU-070 moved Market → Stock Page and the duplicates SAU-131 + SAU-128 deleted, determinations and coverage migrated to the canonical ids. Saudi rows 99 → 97, 7 duplicates remain. Stock Page now 19 rows / 31.6%; Market 18 / 44.4%. Built 2026-08-16.

- [x] 36. Features Map deck + companion workbook at v2.21 — 6-slide deck (`reports/features-map-2026-08-31.pptx`) and a 4-sheet Excel companion (`reports/features-map-2026-08-31.xlsx`: Summary · Coverage · Cross-Product · Capabilities) built by `scripts/build-features-map-deck.py` and `scripts/build-features-map-xlsx.py`. Both read the same `features_derived.json` and `verified_live.json` at build time, so deck and workbook cannot drift. Method and Action Items sections removed from the deck at Ahmed's request (still present in the builder). Built 2026-09-06.

- [x] 37. Unassigned rows filed + Education widened (Ahmed, 2026-09-06). The deck's Platform & Managed Products slide surfaced 5 of 865 rows rendering as "Unassigned" — rows whose `area` was null. Ahmed's ruling: **SAU-006 TILA**, **XJ-049 ARC Chatbot** and **XJ-068 Cross-Product Gain-Loss Chart** → `Platform`; **XJ-069 Global Last Transaction View** → `Cash Management`; **SAU-099 Social / Copy Trading** → `Education/Social`, with the existing `Education` area renamed to carry it. Applied to the master via `dashboard/scripts/assign_platform_areas.py` (integrity checked clean before the edit, backup taken, JSON regenerated, manifest re-recorded at v2.21 — row count, headers and Saudi screen counts unchanged). New areas: **Platform 3 rows / 66% gap** — the highest gap concentration of any Platform area — and **Education/Social 4 rows / 50% gap**. Cash Management is now a single clean area of 82 rows. **Unassigned 5 → 0.** Built 2026-09-06.

---

## Current Feature Inventory (as of 2026-09-06)

- **865 capability rows** at baseline **v2.21** — **524 Live** · 129 Planned · 212 Gap · **0 Unverified** · 1 status conflict (US-236 Reports: hand-typed Live, derives Planned — needs a ruling)
- **504 of the 524 Live rows carry dated evidence** — 317 app walks, 185 manual confirmations by the Head of DX, 5 App Store release notes. `verified_live.json` 507 entries · `manual_status.json` 238 entries.
- **10 investor journeys**, every row placed in a reviewed area structure and resolved to exactly one of Live / Planned / Gap.

| Journey | Rows | Live | Planned | Gap | Gap % |
|---|---|---|---|---|---|
| US Trading | 272 | 150 | 15 | 107 | 39% |
| Saudi Market | 197 | 111 | 61 | 25 | 12% |
| Mutual Funds | 115 | 78 | 4 | 33 | 28% |
| Cash Management | 82 | 61 | 12 | 9 | 10% |
| Platform | 71 | 49 | 13 | 9 | 12% |
| Robo Advisory | 68 | 37 | 5 | 26 | 38% |
| Onboarding | 34 | 20 | 14 | 0 | 0% |
| LMS/SBL | 13 | 8 | 5 | 0 | 0% |
| IPOs | 9 | 6 | 0 | 3 | 33% |
| Crowd Fund | 4 | 4 | 0 | 0 | 0% |

- **Maturity (2026-09-06): platform average 51.9** — Onboarding 81.6 (High), Crowd Fund 72.2 (Advancing), LMS/SBL 53.3, Cash Management 51.5, Robo Advisory 48.9, Mutual Funds 48.7, Platform 46.4, Saudi Market 44.3, IPOs 36.0 (Early), **US Trading 35.5 (Early — still the weakest)**.
- **BRD coverage:** 165 rows carry a BRD · 700 do not. The no-BRD count is dominated by US Trading and Saudi Market — see `us-trading-brd-gap.md` and `saudi-market-brd-gap.md`.
- **The finding (unchanged and still open):** 18 named capabilities are a Gap in Mutual Funds, Robo Advisory and US Trading simultaneously, and 9 of them are Live in Saudi Market today. Portfolio depth was built for Saudi equity and never extended to anything else ARC sells. Gap concentration: US Trading · Portfolio 77 · Robo Advisory · Portfolio 26 · Mutual Funds · Portfolio 24 · US Trading · Market 22 · Saudi Market · Market 19.
- **Every row is filed.** As of 2026-09-06 no row renders as "Unassigned" — see step 37.

> ⚠️ **Gap in this log.** The step list below stops at 35 (2026-08-16), when the map held 345 rows. The map advanced to v2.21 / 865 rows between 2026-08-16 and 2026-08-31 and that work was never written up here. The numbers above are read live from `features_derived.json`; the missing narrative is worth reconstructing before the next baseline.

*Source: Features Map · baseline v2.21 · features_derived.json · verified_live.json · manual_status.json · 06 September 2026*

---

## Current Step

> **Nothing is in flight.** The map is complete end to end — all 865 rows walked or ruled, zero Unverified, zero Unassigned.
> Two commitments are overdue and both are waiting on other people:
> - **Squad Validation Cycle 2** — deadline was **1 September**, now 5 days past, all 10 squad responses outstanding.
> - **Benchmark check** (Strategy & Intelligence) — due **28 August**, now 9 days past. Covers Government Trades, Stocks Key Facts, Chain Order, Trailing Order. See `reports/benchmark-check-request-2026-08-16.md`.
>
> Saudi Market deep dive remains part-done: Portfolio ✅ · Stock Page ✅ · Orders ✅ · **Market (108 rows) and Watchlist (5 rows) not started**.

---

## Next Step

> **1. Chase or drop the two overdue items.** Both have been sitting past their dates with no movement.
>
> **2. Re-verify the 129 Planned rows.** This is the least-evidenced part of an otherwise evidence-backed map, and it is the part competitor reports read to generate gaps. On 2026-09-06 two features recorded as Planned turned out to be live in the product — the returns calculator and calendar filtering by holdings and watchlist — and both produced false gaps in the CEO brief before Ahmed caught them. Saudi Market alone holds 61 Planned rows; US Trading 15; Onboarding 14.
>
> **3. Finish the Saudi Market deep dive with Market (108 rows, 47 of them Planned), then Watchlist (5).** Doing Market next closes the deep dive and clears the largest single cluster of unverified Planned rows in one pass.
>
> **4. Rule on US-236 (Reports)** — the map's only remaining status conflict.
>
> **5. Housekeeping:** `build-features-map-deck.py` still regenerates the Method and Action Items sections removed from the deck on 2026-09-06; the deck's percentage column is unlabelled and reads as Live when it is Gap share.

---

## Last Updated

2026-09-06

## Confirmed Answers
- FIGMA_TOKEN: set in `.env` and `~/.zshrc` ✅
- Feature inventory: 154 features saved to `features-inventory.md` ✅
- Raw Figma screens: 157 screens saved to `figma-screens.md` ✅
- 42 Figma-only features (designed but no BRD) — flag for squad leads to write BRDs ✅
- 68 BRD-only features (requirements written but not yet in Figma revamp) — flag for design team ✅

---

## Confirmed Answers
- Research files available: 43 research PDFs indexed in knowledge-bank/research-index.md ✅
- BRDs available: 182 BRDs (deduped) indexed and joined to features via `knowledge_bank.py` — 166 features linked (was 100 BRDs / 137 links at project start). ✅

- Scope: all ARC products from day one — not limited to 5 core journeys ✅
- Competitor gap analysis: use the same list as the weekly competitor report (56 apps in CSV) ✅
- Product backlog: none currently — BRDs are the source of truth. Ahmed will update BRDs as vision becomes clearer. Feature extraction starts from Figma + BRDs only. ✅
- Figma files (all 8): PgN7nzg8CcueY12mu6TIVe (Onboarding), KbRt2JimFFINSFPqe1t5sZ (Home), PXgN11AxL6KevGVTGocbrI (Tradepad), p7TSYYTNeEGFPwHYhhy56q (Market), 4ybkyLURbOhzauw8ugkHGp (Portfolios), PEMRwaRLpQaSD7rBxnQ4zF (Discover), cMRqMd2owWi3oBk5dV78TE (Profile & Setting), BhwWZvTq5ZxP0YmhgrkpWN (Orders), muzIamMJ7ycvstbVnWbXvi (Watchlist — empty) ✅

## Pending Questions for Ahmed

- **Squad Validation Cycle 2 — 5 days overdue.** Deadline was 1 September; no responses in from any of the 10 squads. Chase, extend, or close the cycle without them?
- **Benchmark check — 9 days overdue.** Commissioned from Strategy & Intelligence on 2026-08-16, due 2026-08-28, covering 4 unbenchmarked rows.
- **US-236 (Reports)** — hand-typed Live, derives Planned. Needs a determination to clear the last status conflict.
- **The Planned list needs a verification pass** — two Planned rows were found live in the product on 2026-09-06. How many more? Ahmed's ruling is the only way to close them.

---

## Knowledge Bank References
*Auto-linked from the DX Knowledge Bank (`projects/knowledge-bank/`). DX Knowledge Bank · 182 BRDs · 45 research · projects/knowledge-bank/*

**Relevant BRDs** (`assets/BRDs/`):
- ARCD 18697- BRD New Bundle Feature and Product fulfillment- Version 1.5.docx — BRD New Bundle Feature and Product fulfillment- Version
- ARCD 19542 -Story Teller_BRD_V0.1.docx — Storyteller feature
- ARCD -75525 - Global Notification - BRD_V0.8.docx — Global Notification - BRD
- ARCD 20124- BRD Revamp of Email notifications sent to the Customers- Version 1.0.docx — BRD Revamp of Email notifications sent to the Customers- Version
- ARCD-101056_Benzinga Content Translation and Caching Optimization_BRD_V0.1.docx — Benzinga Content Translation and Caching Optimization BRD

**Relevant research** (`assets/research/`):
- Analysis Features and Gaps 2025 - NEW (Copy).pdf — Analysis Features and Gaps 2025 - NEW (Copy)
- Analysis Features and Gaps 2025 - NEW.pdf — Analysis Features and Gaps 2025 - NEW
- Bain Features List.pdf — Bain consulting feature recommendations
- Analysis of Trading Features and Gaps in ARC 2025.pdf — Full trading feature gap analysis — ARC vs market

**Competitor signals** (`competitor-intelligence-index.md`):
- Drahim · SAU-020 — Hello! We’re thrilled to share the latest updates in Drahim: See a list of your  (2026-08-09)
- Drahim · MF-019 — Hello! We’re thrilled to share the latest updates in Drahim: See a list of your  (2026-08-09)
- hyssa · SAU-073 — Brand-new Portfolio design with improved navigation More insights into your inve (2026-07-21)
- hyssa · XJ-028 — Brand-new Portfolio design with improved navigation More insights into your inve (2026-07-21)

> Indexes: `brd-index.md` · `research-index.md` · `regulations-index.md` · `figma-index.md` · `project-outputs-index.md` · `feature-brd-crossref.md` · `competitor-intelligence-index.md`

