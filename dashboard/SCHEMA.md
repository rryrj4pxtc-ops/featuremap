# Features Map — Data Schema

Version 1.5 · Updated 2026-07-18 — Added `impact` column (S). Priority is now computed: `priority = impact × pressure` (derive_status.py). Hand-typed priority in column H is ignored when impact is present.

Version 1.4 · Updated 2026-07-17 — Corrected priority direction — was documented backwards.

Version 1.3 · Updated 2026-05-11 — Added `area` (col J) and `screen` (col K) columns. Populated for Saudi Market (98 features). See saudi-market-feature-assignment-DRAFT.md.

Version 1.2 · Updated 2026-05-08 — Dissolved Investor Engagement and Corporate Actions journeys; added Cash Management. See restructure-plan-engagement-ca.md.

Version 1.1 · Updated 2026-05-07 — Dissolved Portfolio Monitoring and Wealth Visibility journeys. See restructure-plan.md.

Version 1.0 · Generated 2026-05-05

---

## Features Schema

Each row in the **Features** sheet (starting at row 4) maps to one object in `features.json → features[]`.

| # | Column | JSON key | Type | Required | Allowed values / notes |
|---|--------|----------|------|----------|------------------------|
| A | id | `id` | string | yes | Unique. Must follow `PREFIX-NNN` pattern (see prefix table below). |
| B | name | `name` | string | yes | Short feature name. |
| C | journey | `journey` | string (enum) | yes | One of the 10 journey values listed below. |
| D | status | `status` | string (enum) | yes | `Live`, `Planned`, `Gap`, `Diff` |
| E | definition | `definition` | string | no | One-sentence description of the feature. |
| F | brd | `brd` | string (CSV) → array | no | Comma-separated BRD codes, e.g. `BRD-045, BRD-046`. Each code should exist in the BRDs sheet. |
| G | competitors | `competitors` | string (CSV) → array | no | Comma-separated competitor names. Each name should exist in the Benchmarks sheet. |
| H | priority | `priority` | integer | no | **Legacy / override.** Ignored when `impact` (col S) is present — derive_status.py computes `priority = impact × pressure`. |
| I | tags | `tags` | string (CSV) → array | no | Comma-separated free-text tags, e.g. `sahm-gap, deep-discovery, cross-screen`. |
| J | area | `area` | string (enum) | no | Feature area within the journey. Currently scoped to Saudi Market only. See Area Enum below. |
| K | screen | `screen` | string | no | Specific screen within the area. Maps to the screen inventory for the journey. |
| L | figma_link | `figma_link` | string (URL) | no | Full Figma URL to the design. |
| M | figma_status | `figma_status` | string (enum) | no | `Designed`, `In Review`, `Approved`, `As-Built` |
| N | figma_file | `figma_file` | string (enum) | no | Canonical Figma file containing the design. See Figma File Enum below. Used by screen-extraction tooling to locate the source-of-truth design. |
| O | live_date | `live_date` | date | no | Target go-live date. Stored as ISO `YYYY-MM-DD` in JSON; displayed as `DD MMM YYYY` in Excel. |
| P | went_live | `went_live` | date | no | Actual go-live date. Same format convention. |
| Q | owner_pm | `owner_pm` | string | no | Product manager name. |
| R | owner_squad | `owner_squad` | string | no | Responsible squad name. |
| S | impact | `impact` | integer (1–5) | no | Does this feature move Funded & Activated Investors? 5 = blocks funding or first trade, 1 = cosmetic. Blank allowed — leave blank when unsure. |

**Derived fields (JSON only):**

| JSON key | Type | Logic |
|----------|------|-------|
| `source` | string or null | `"BRD + Figma"` if both `brd` and `figma_link` are present; `"BRD"` if only `brd`; `"Figma"` if only `figma_link`; omitted otherwise. |
| `pressure` | integer (0–5) | Competitor pressure score. Computed by derive_status.py from coverage cells. |
| `priority` | integer (1–25) or null | `impact × pressure` when both exist. Null when `impact` is blank. Higher = higher priority. |

### Journey Enum (11 values)

| Value | Description |
|-------|-------------|
| Onboarding | Account opening and KYC |
| Saudi Market | Tadawul equity trading |
| US Trading | US market equity trading |
| Mutual Funds | Fund subscription and redemption |
| Crowd Fund | Crowdfunding investment products |
| Robo Advisory | Automated portfolio management |
| LMS | Margin lending (Lending Management System) |
| IPOs | IPO subscription |
| Cash Management | Payments, wallets, funding, loyalty-to-invest |
| Investor Engagement | Rewards, referrals, gamification, community, charity |
| Platform | Cross-cutting platform layer: settings, market data, compliance, support, auth, content |

> **`Cross-Journey` retired 2026-08-02.** Its 68 features were decomposed: 11 money/wallet
> features → Cash Management (6 → 17); 10 rewards/engagement features → the new
> **Investor Engagement** journey; the remaining 47 cross-cutting features → **Platform**
> (a rename of the container). Reassigned features keep their stable `XJ-`/`SAU-` ids
> (renumbering would break repo-wide references); the export's prefix check is relaxed
> for them (`XJ` dropped from `JOURNEY_PREFIX`; `SAU-006`/`SAU-016` explicitly exempt).
> New prefixes: `IE` (Investor Engagement), `PLT` (Platform). Investor Engagement uses the
> functional 6-area model; Platform uses its own cluster-area enum (below).

### Functional area model (6 values) — the area model for all journeys except Onboarding

As of 2026-08-02 the `area` column uses a **functional** vocabulary — an area names the
*user intent* a feature serves, not a place in the app. This replaces the earlier
product-native scheme (Portfolio / Stock Page / Orders / Market / Watchlist / Trading
Actions). The six canonical values:

| Value | User intent it captures |
|-------|-------------------------|
| **Discover** | Finding and evaluating an instrument before committing: search, screen, compare, news, ratings, market data, trending, calendars |
| **Transact** | Executing or cancelling a transaction on an instrument: place/modify order, subscribe, redeem, switch, liquidate, all order types |
| **Track** | Monitoring what you already hold, watch, or have ordered: portfolio, performance, watchlist, alerts, order/holding state, history, reports |
| **Manage** | Controlling account settings, credit, and non-trade operations: margin/collateral, transfers, cost-basis edits, preferences, limits |
| **Learn** | Educational content: guides, tutorials, simulators, glossaries |
| **Onboard** | Gaining or extending access: identity, KYC, authentication, account opening, entity/family/corporate approval states |

Enforced by `VALID_AREAS_FUNCTIONAL` in `xlsx-to-features-json.py` and
`CANONICAL_SAUDI_AREAS` in `derive_status.py`. `Learn` and `Onboard` are valid areas
that a given journey may not populate (e.g. Saudi Market populates neither — see below).

#### Saudi Market — the converted reference journey

Saudi Market (92 features) is the first journey migrated to the functional model and
serves as the reference. Distribution after conversion:

| Area | Count |
|------|-------|
| Transact | 38 |
| Track | 30 |
| Discover | 15 |
| Manage | 9 |
| Learn | 0 |
| Onboard | 0 |
| **Total** | **92** · 0 null-area · 0 orphans |

#### US Trading — second converted journey (2026-08-02)

US Trading (81 features) migrated next. It had 24 null-area features beforehand, so
conversion was a strict completeness gain (24 → 0 null-area). Distribution:

| Area | Count |
|------|-------|
| Transact | 32 |
| Discover | 23 |
| Track | 23 |
| Manage | 3 |
| Learn | 0 |
| Onboard | 0 |
| **Total** | **81** · 0 null-area · 0 orphans |

4 features placed by hand (no keyword match) — the exact US twins of Saudi's 4, given
matching homes for consistency: US-016 Stock Compare & US-065 Sector & Exchange
Volatility → Discover; US-060 Liquidate Holdings & US-075 Batch Close Positions →
Transact. US Trading retains 46 null-screen features (screens were only partially
authored; see the null-screen note — the functional model does not change this).

#### Mutual Funds — third converted journey (2026-08-02)

Mutual Funds (24 features) migrated next. Like US Trading it had 24 null-area features,
so conversion was a strict completeness gain (24 → 0 null-area). Distribution:

| Area | Count |
|------|-------|
| Transact | 9 |
| Discover | 6 |
| Track | 6 |
| Manage | 3 |
| Learn | 0 |
| Onboard | 0 |
| **Total** | **24** · 0 null-area · 0 orphans |

4 features placed by hand: MF-014 Compare Funds & MF-015 Top Fund Holders & MF-016 Fund
Financial Reports → Discover (fund due-diligence/evaluation material, consistent with
SAU-041/045); MF-001 Subscribe to SAR Fund → Transact (orphaned only on a keyword-
boundary quirk — a subscription is a transaction). Mutual Funds has no authored screens
(24 null-screen), unchanged by the conversion.

#### Robo Advisory — fourth converted journey (2026-08-02)

Robo Advisory (12 features) migrated next; it had 12 null-area features, so a strict
completeness gain (12 → 0 null-area). **First converted journey to populate `Onboard`
and `Learn`** — it fills 5 of the 6 areas (only `Manage` empty), a better spread than
the trading journeys. Distribution:

| Area | Count |
|------|-------|
| Track | 7 |
| Transact | 2 |
| Onboard | 1 |
| Discover | 1 |
| Learn | 1 |
| Manage | 0 |
| **Total** | **12** · 0 null-area · 0 orphans |

2 hand placements: RBO-004 Mashura Reports → Track (portfolio reports, consistent with
SAU Portfolio Reports); RBO-003 Robo Cash Withdrawal → Transact (auto-missed on the
`withdraw\b`-before-"al" boundary quirk — a cash-out is a transaction). 12 null-screen,
unchanged by the conversion.

#### IPOs — fifth converted journey (2026-08-02)

IPOs (9 features) migrated next; 8 null-area beforehand → 0. Transact-heavy, as expected
for a subscription journey. Distribution:

| Area | Count |
|------|-------|
| Transact | 5 |
| Discover | 2 |
| Track | 1 |
| Onboard | 1 |
| Learn | 0 |
| Manage | 0 |
| **Total** | **9** · 0 null-area · 0 orphans |

5 hand placements: IPO-001/003/007 & SAU-019 (IPO subscriptions) → Transact — all
auto-missed on the `subscrib\b`-before-vowel boundary quirk; IPO-008 IPO Popup Banner →
Discover (new-IPO awareness surface). 8 null-screen, unchanged.

#### LMS — sixth converted journey (2026-08-02)

LMS (margin lending / securities borrowing & lending, 7 features) migrated next; 7
null-area → 0. Track-heavy, mirroring Robo — its portfolio screens are the structural
twins of Robo's Mashura screens. Distribution:

| Area | Count |
|------|-------|
| Track | 5 |
| Transact | 1 |
| Onboard | 1 |
| Discover | 0 |
| Learn | 0 |
| Manage | 0 |
| **Total** | **7** · 0 null-area · 0 orphans |

Placed explicitly (the keyword "lending" would otherwise pull the portfolio-view screens
into Transact): LMS-001 Portfolio Home, LMS-002 Holding Overview, LMS-003/004 Filters,
LMS-005 Choose Portfolio → Track (twins of RBO-009/010/011/012); LMS-006 SBL Program →
Transact (the securities-lending capability); LMS-007 SBL Digital Acceptance → Onboard
(enrollment/suitability). 7 null-screen, unchanged.

#### Cash Management — seventh converted journey (2026-08-02)

Cash Management (6 features) migrated; 6 null-area → 0. Distribution:

| Area | Count |
|------|-------|
| Transact | 4 |
| Manage | 2 |
| **Total** | **6** · 0 null-area · 0 orphans |

Placement: CM-001 Mokafaa Points, CM-003 Buy Round-Up, CM-005 Client Money, CM-006
Universal Funding → Transact; CM-002 ARC Debit Card, CM-004 T+2 Card → Manage.

> **Known weakness — the model has no Money area.** Every Cash Management feature is
> money-movement (wallet, card, funding, points). The functional 6-set has no `Money`
> area, so these are proxied into Transact/Manage — `Manage` here is a catch-all for
> wallet/card features rather than its intended "account settings" intent. Decision
> (2026-08-02): keep the 6-area set rather than add `Money`. **The same wall will hit
> Cross-Journey** (~14 money features: IBANs, Apple Pay, cash-in/out). Additionally
> CM-004/005/006 have no `definition`, so their placement is name-inference only. Revisit
> if a `Money` area is later adopted.

#### Crowd Fund — eighth converted journey (2026-08-02)

Crowd Fund (6 features) migrated; 6 null-area → 0. **All 6 → Track** — the feature set is
entirely the portfolio-monitoring screen family (Portfolio Home, Holding Overview,
Holdings Filter, Choose Portfolio, Portfolios, Order History), the same shape as Robo's
Mashura and LMS screens. CF-006 Crowd Funds Orders ("order history") placed in Track for
consistency with SAU-120 List of Orders, not Transact.

| Area | Count |
|------|-------|
| Track | 6 |
| **Total** | **6** · 0 null-area · 0 orphans |

> **Data-completeness note:** Crowd Fund lands 100% in Track because only its
> monitoring surface is captured in the feature map — no pledge/invest (Transact) or
> campaign-discovery (Discover) features exist yet. The single-area result reflects a
> gap in the inventory, not the real product.

> **Known limitations of the functional model, recorded honestly:**
> - **Not yet validated for other journeys.** Measured across all 423 features the 6-area
>   set orphans ~22% (notably Cross-Journey, which is largely platform/rewards/compliance
>   features). Other journeys are candidates for migration, not yet converted; a
>   `function`-as-second-attribute approach was considered as an alternative.
> - **`Transact` vs `Track` do not separate unambiguously** on order-state features
>   (e.g. "Stop Loss Detail" — an executed instruction being viewed). A written
>   tie-breaker rule is still needed.
> - **Screens no longer parent cleanly to one area.** Under the product-native scheme a
>   screen belonged to one area; functionally, `Stock Details` splits across Transact /
>   Discover / Track. Screens were retained on their features but no longer imply a
>   single area.
> - **4 features were placed by hand** (no keyword match): SAU-025 & SAU-041 → Discover,
>   SAU-080 & SAU-097 → Transact.

**Retired:** the product-native area enum and the maturity `normalize_area()` rule
(its targets were product-native names that no longer exist; `AREA_NORMALIZATION` is now
empty but the fail-fast assertion is retained for future additions).

### Area Enum — Onboarding (5 values) — DELIBERATELY EXEMPT from the functional model

| Value | Description |
|-------|-------------|
| ARB | Standard Al Rajhi Bank customer onboarding (KYC, login, authentication, guides) |
| Local | Non-ARB local individual customers (local bank accounts) |
| Global | International customers: GCC, foreign, IBKR brokerage onboarding |
| Corporate | Corporate entity onboarding: local companies, approval flows, requirements |
| Minor | Minor account onboarding and guardian controls |

> **Onboarding keeps its account-type areas — decision 2026-08-02.** These five values are
> an **account-type** axis (who is being onboarded), not the functional intent axis used
> by every other journey. Converting Onboarding to the functional model would collapse
> ~62 of its 118 features into `Onboard` and destroy the ARB/Local/Global/Corporate/Minor
> distinction the journey is organized around. It is therefore **exempt**: it stays on this
> enum, enforced by `VALID_AREAS_ONB` in `xlsx-to-features-json.py` (a separate rule from
> `VALID_AREAS_FUNCTIONAL`). Of 11 journeys: 9 are functional (the 8 trading/product
> journeys + Investor Engagement); Onboarding is exempt by design (account-type axis);
> Platform uses cluster areas. **Do not "finish" Onboarding by converting it** without an
> explicit new decision — a functional `Onboard` area exists and already holds
> full-lifecycle onboarding features from other journeys (RBO-001, IPO-005, LMS-007), so
> the account-opening intent is still represented estate-wide.

### Area Enum — Platform (7 values, cluster areas)

Platform (former Cross-Journey, 47 features) is a cross-cutting infrastructure layer, not
an investing journey, so it uses **cluster areas** (what the feature *is*), not the
functional intent axis. Enforced by `VALID_AREAS_PLATFORM` in `xlsx-to-features-json.py`.

| Value | Count | Contents |
|-------|-------|----------|
| Settings | 14 | Theme, language, navigation, session, accessibility, display prefs, widgets |
| Market Data | 13 | TradingView, live/historical index prices, liquidity, calendars, key facts, price alerts |
| Content | 6 | Tutorials, stock stories, mock trading, calculators |
| Compliance | 5 | Zakat, purification, ZATCA e-invoices, Shariah lists |
| Support | 5 | CRM cases, chatbot, WhatsApp, daily brief, investment manager |
| Auth | 3 | SSO (Tadawulaty), 3D Secure, registered devices |
| Notifications | 1 | Global notification center |

> **Placement caveat:** 15 of the 47 Platform features have no `definition`, so their area
> is name-inference (Chatbot, Daily Brief, App Widgets, Auto Zakat, Mock Trading, etc.).

#### Investor Engagement — new journey from decomposition (2026-08-02, functional areas)

10 rewards/engagement features split from Cross-Journey into a new journey aligned with the
Investor Engagement squad. Uses the functional 6-area model. Distribution: Discover 5,
Transact 4, Manage 1.

> **Fit caveat:** rewards/gamification/referral/community/charity features fit the
> functional 6-set poorly (they were the largest orphan group in the original all-journeys
> analysis). Placements are best-fit (promos → Discover, donations/bundles → Transact,
> perks → Manage); an `Engage` area would be cleaner if the model is later extended.

#### Cash Management — expanded to 17 by decomposition (2026-08-02)

The original 6 Cash Management features plus 11 money/wallet features reassigned from
Cross-Journey. Functional areas (money-movement → Transact, wallets/cards/IBANs/invoices →
Manage, aggregated view → Track): Transact 8, Manage 8, Track 1. The no-`Money`-area
weakness noted for the original 6 now applies to all 17.

### Status Enum (4 values)

| Value | Meaning |
|-------|---------|
| Live | Feature is in production. |
| Planned | Feature is approved and scheduled. |
| Gap | Feature exists in competitors but not in ARC. |
| Diff | ARC differentiator — exists in ARC but not competitors. |

### Figma File Enum (15 values)

| Value | Description |
|-------|-------------|
| CDO | Main trading & portfolio design file |
| Portfolios | Portfolio monitoring, holdings, performance |
| OnBoarding (KYC) | Account opening and KYC flows |
| Market | Market overview screens |
| Discover & Search | Discovery and search experience |
| Home | Home screen and dashboard |
| Profile & Setting | Profile and settings screens |
| LMS | Margin lending (LMS) flows |
| Wealth Mgmt Dashboard | Wealth management dashboard |
| Watchlist | Watchlist screens |
| Bain | Onboarding research/variants |
| Tradepad | Trade pad and deposit/transfer |
| Orders | Order management screens |
| Themes | Seasonal themes |
| Trader Mode | Trader mode alternative UI |

### Journey-Prefix Table

The first segment of an `id` (before the hyphen) encodes the journey.

| Prefix | Journey |
|--------|---------|
| ONB | Onboarding |
| SAU | Saudi Market |
| US | US Trading |
| MF | Mutual Funds |
| CF | Crowd Fund |
| RBO | Robo Advisory |
| LMS | LMS |
| IPO | IPOs |
| CM | Cash Management |
| IE | Investor Engagement |
| PLT | Platform |

> `XJ` (legacy Cross-Journey) is retired from the prefix map — the 68 former Cross-Journey
> features keep their existing `XJ-`/`SAU-` ids after the 2026-08-02 decomposition, so the
> prefix no longer implies the journey for those rows.

Example id: `SAU-012` → Saudi Market feature #12.

### Date Convention

- **Excel display:** `DD MMM YYYY` (e.g. `15 Mar 2026`). The cell is formatted via a custom number format in the template.
- **JSON storage:** ISO `YYYY-MM-DD` (e.g. `2026-03-15`). The export script normalises all date variants to this format.

### Worked Example (JSON)

```json
{
  "id": "SAU-012",
  "name": "Advanced Order Types",
  "journey": "Saudi Market",
  "status": "Planned",
  "definition": "Support for stop-loss, trailing-stop, and bracket orders on Tadawul.",
  "brd": ["BRD-045"],
  "competitors": ["Derayah", "Sahm"],
  "priority": 3,
  "tags": ["sahm-gap"],
  "area": "Trading Actions",
  "screen": "Options Tradepad",
  "figma_link": "https://www.figma.com/file/abc123/advanced-orders",
  "figma_status": "Designed",
  "live_date": "2026-06-15",
  "owner_pm": "Fahad",
  "owner_squad": "Saudi Market Squad",
  "source": "BRD + Figma"
}
```

---

## BRDs Schema

Each row in the **BRDs** sheet (starting at row 4) maps to one object in `brds.json → brds[]`.

| # | Column | JSON key | Type | Required | Allowed values / notes |
|---|--------|----------|------|----------|------------------------|
| A | brd_code | `brd_code` | string | yes | Unique code, e.g. `BRD-045`. Referenced by Features.brd. |
| B | title | `title` | string | no | BRD document title. |
| C | owner | `owner` | string | no | Author or owner name. |
| D | status | `status` | string (enum) | no | `Draft`, `In Review`, `Approved`, `Deprecated` |
| E | approved_date | `approved_date` | date | no | ISO `YYYY-MM-DD` in JSON. |
| F | link | `link` | string (URL) | no | URL to the BRD document. |

---

## Benchmarks Schema

Each row in the **Benchmarks** sheet (starting at row 5) maps to one object in `benchmarks.json → benchmarks[]`.

| # | Column | JSON key | Type | Required | Allowed values / notes |
|---|--------|----------|------|----------|------------------------|
| A | name | `name` | string | yes | Canonical competitor name. Used to validate Features.competitors. |
| B | region | `region` | string | no | e.g. `Saudi`, `Global`. |
| C | type | `type` | string | no | e.g. `Broker`, `Neo-Broker`, `Platform`. |
| D | primary | `primary` | boolean | no | `TRUE` if this is a primary benchmark competitor. |

---

## JSON Envelope

All three output files share a `_meta` envelope:

```json
{
  "_meta": {
    "schema_version": "1.0",
    "last_updated": "2026-05-05",
    "generated_by": "xlsx-to-features-json.py"
  },
  "features": [ ... ]
}
```

---

## Validation Rules (enforced by export script)

| Rule | Severity |
|------|----------|
| `id`, `name`, `journey`, `status` must be non-empty | Error (blocks export) |
| `id` must be unique across all features | Error |
| `journey` must be in the 10-value enum | Error |
| `status` must be in the 4-value enum | Error |
| `id` prefix should match journey per prefix table | Warning |
| `figma_status` should be in its 4-value enum | Warning |
| Each competitor name should exist in Benchmarks sheet | Warning |
| `priority` should be a whole number | Warning |

## Backend dimension (US Trading — IBKR / GTN)

US Trading runs on two brokerage backends: **IBKR** (Interactive Brokers) and **GTN** (Global Trading Network). A feature can be Live/Planned on one and a gap on the other.

- **Column:** `backends` (xlsx), format `IBKR=Live;GTN=Gap` (semicolon-separated `BACKEND=Status`).
- **Rule:** the row's own `status` must equal the **most-advanced** backend's status (Live/Diff > Planned > Gap). The converter warns on mismatch.
- **Scope:** US Trading only (warns otherwise). Leave blank when a feature is uniform across both backends.
- **Output:** `features_derived.json` carries `backends: {IBKR, GTN}` and `backend_split: true` when the two differ.
- **Views:** cockpit shows a "US Backend Split" table; atlas tree shows a `Backends:` detail line.
