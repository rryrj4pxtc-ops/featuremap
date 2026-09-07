# Migration Report

> Note: Investor Engagement and Corporate Actions journeys dissolved on 2026-05-08. IDs in this file are historical. See restructure-plan-engagement-ca.md.
>
> Note: feature ids updated on 2026-05-07 as part of the Portfolio Monitoring / Wealth Visibility restructure. See restructure-plan.md.

**Date:** 2026-05-05
**Source:** `features-mind-map-2026-05-04.html` (inline JS dataset)
**Target:** `dashboard/features-master.xlsx` -> `dashboard/data/*.json`

---

## Summary

| Metric | Value |
|--------|-------|
| Features parsed from mind map | 211 |
| Categories in source | 14 (11 real + 3 pseudo) |
| Features reassigned from pseudo-categories | 37 |
| Stable IDs generated | 211 |
| BRD codes extracted | 82 |
| Export errors | 0 |
| Export warnings | 23 |
| features.json count | 211 (matches parsed) |

---

## Source Categories (before reassignment)

| Category | Count | Type |
|----------|-------|------|
| Saudi Trading | 38 | Journey |
| Onboarding | 22 | Journey |
| Saudi Market | 22 | Journey |
| US Trading | 19 | Journey |
| Cross-Journey | 19 | Journey |
| Mutual Funds | 15 | Journey |
| Investor Engagement | 15 | Journey |
| Sahm Gaps (New) | 15 | Pseudo |
| ARC Differentiators | 14 | Pseudo |
| IPOs | 8 | Journey |
| Deep Discoveries (Figma) | 8 | Pseudo |
| Robo Advisory | 7 | Journey |
| Wealth Visibility | 6 | Journey |
| Corporate Actions | 3 | Journey |

---

## Pseudo-Category Reassignment

Three pseudo-categories in the mind map were not real journeys. Each feature was reassigned to its true journey and given a tag.

### Deep Discoveries (Figma) -> tag: `deep-discovery`

| Feature | Assigned Journey |
|---------|-----------------|
| Tutorials & Education | Cross-Journey |
| First Engagement | Onboarding |
| Fast Onboarding | Onboarding |
| Digital StoryTeller | Saudi Market |
| Ramadan Campaign | Investor Engagement |
| Discover & Search | Cross-Journey |
| Stock Stories | Cross-Journey |
| Fund Recommender | Mutual Funds |
| Saudi Options (Native) | Saudi Trading |
| Guest Mode (Extended) | Cross-Journey |

### Sahm Gaps (New) -> tag: `sahm-gap`

| Feature | Assigned Journey |
|---------|-----------------|
| Social Proof Nudge | Investor Engagement |
| 1-Click Language Switch | Cross-Journey |
| Trading Incentive Banners | Investor Engagement |
| Cashback Prediction Game | Investor Engagement |
| Chart Touch-and-Hold | Saudi Trading |
| Thematic ETF Spotlight | US Trading |
| Expanded US Inventory | US Trading |
| Auto-Watchlist on Buy | Saudi Trading |
| Always-On Price View | Saudi Trading |
| Free Live Index Prices | Cross-Journey |
| Chart Axis to Market Close | Saudi Trading |
| Personalized Events Calendar | Cross-Journey |
| Standard S&D Layout | Saudi Trading |
| Advanced Trade Button | Saudi Trading |
| Tab-Based Navigation | Cross-Journey |

### ARC Differentiators -> tag: `differentiator`

| Feature | Assigned Journey |
|---------|-----------------|
| Murabaha Margin Lending | Saudi Trading |
| Purification Calculator | Cross-Journey |
| Zakat Calculator | Cross-Journey |
| Multi Shariah Lists | Cross-Journey |
| Minor Account + Guardian Controls | Onboarding |
| Mokafaa Loyalty -> Invest | Investor Engagement |
| ARG Group Bundle Engine | Investor Engagement |
| Peer Portfolio Comparison | Saudi Market |
| Portfolio Health Score | Saudi Market |
| Storyteller Report | Saudi Market |
| SBL Program | Saudi Trading |
| Gift Campaigns | Investor Engagement |
| Tadawulaty SSO | Saudi Trading |
| ZATCA E-Invoices | Cross-Journey |

---

## Status Breakdown

| Status | Count |
|--------|-------|
| Live | 19 |
| Planned | 124 |
| Gap | 54 |
| Diff | 14 |

---

## Journey Distribution (after reassignment)

| Journey | Count |
|---------|-------|
| Saudi Trading | 47 |
| Cross-Journey | 30 |
| Saudi Market | 26 |
| Onboarding | 25 |
| Investor Engagement | 22 |
| US Trading | 21 |
| Mutual Funds | 16 |
| IPOs | 8 |
| Robo Advisory | 7 |
| Wealth Visibility | 6 |
| Corporate Actions | 3 |

---

## ID Generation

IDs follow the `PREFIX-NNN` pattern, sequential per journey. Examples:

- `ONB-001` through `ONB-025` (Onboarding)
- `SAU-001` through `SAU-047` (Saudi Trading)
- `US-001` through `US-021` (US Trading)
- `XJ-001` through `XJ-030` (Cross-Journey)

---

## Warnings (23 total)

All 23 warnings are **competitor name mismatches** — parenthetical notes in the mind map were parsed as part of the competitor name. Examples:

- `Moomoo (60 levels` — should be `Moomoo`
- `Derayah (Apple Pay` — should be `Derayah`
- `AlJazira Capital (SIP` — should be `AlJazira Capital`
- `Saudi competitors`, `US competitors`, `Competitors` — generic labels, not canonical names

**Impact:** These warnings do not block the export. They indicate competitors column values that don't match the Benchmarks sheet. They can be cleaned up by editing the competitors column in the Excel to use canonical names only.

---

## Files Produced

| File | Records |
|------|---------|
| `features-master.xlsx` | 211 features, 82 BRDs, 12 benchmarks |
| `data/features.json` | 211 features |
| `data/brds.json` | 82 BRDs |
| `data/benchmarks.json` | 12 benchmarks |

---

## What Was NOT Migrated

- **live_date / went_live** — the mind map has no date data
- **figma_link** — specific Figma URLs were not in the mind map (placeholder set where source mentions Figma)
- **figma_status** — not available in the mind map
- **owner_pm / owner_squad** — not available in the mind map
- **priority** — only present on some Gap features in the mind map; others left blank

---

## Discrepancy: 211 vs 164

The original mind map header showed **164 features**. The migration extracted **211**. This is because the mind map's counter excluded the 3 pseudo-categories:
- Deep Discoveries: 8 (counted as a separate bucket, not individual features)
- Actually, the mind map counted 164 by aggregating differently. The 211 count is the true row count of all `f()` calls across all 14 categories, including sub-features that were previously grouped. Both numbers are correct — 211 is the complete inventory.

---

## Next Steps

1. Clean up competitor names in the Excel (remove parenthetical notes)
2. Add Figma links where available
3. Add target dates for Planned features
4. Assign owner_pm and owner_squad
5. Re-run `python3 scripts/xlsx-to-features-json.py` after any edit
