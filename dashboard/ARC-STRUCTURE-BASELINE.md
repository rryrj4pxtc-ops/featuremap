# ARC Structure Baseline — Saudi + US

**Version:** v2.21 · **Locked:** 2026-08-31 · **Owner:** Ahmed Alghamdi, Head of Digital Experience
**Snapshot:** `structure-BASELINE-v2.2.1-2026-08-26.xlsx` (read-only)
**Filename note:** `derive_status.py` parses this filename for `baseline_version` — renaming it requires updating `BASELINE_MD` in the same commit.
**Prior:** v1.3, v1.2, v1.1 (same folder)
**Note:** v1.2.1 was cut *after* v1.3, so this snapshot also contains the v1.3 Level1–Level7 columns.
**Working file:** `features-master.xlsx`

*Source: Features Map · 2026-08-17 · approved spec v3 + Portfolio Analysis amendment + baseline v1.1 + v1.2*

---

## 0. Standing rule — no lock without an evidence bundle (2026-08-25)

**Effective immediately. Applies to every campaign, and to any sub-agent or session this work
is delegated to.**

No completion or lock may be reported without its EVIDENCE BUNDLE, produced **after** the run
and printed in the **same output** as the lock line:

| # | Evidence | Read from |
|---|---|---|
| a | Per-screen row counts | the **saved** workbook, re-opened from disk |
| b | Structural-diff acceptance result | the rendered trees |
| c | Workbook md5 | the file on disk |
| d | JSON `generated_at` + `baseline_version` | `features_derived.json` `_meta` |
| e | Three spot-check rows printed from disk | the saved workbook |

**A lock line without the bundle is invalid and must be treated as NOT RUN.**

A true FAILED beats a false LOCKED every time. If a check fails, report the failure with its
evidence rather than the lock.

### The failure mode this guards against — version-label collision

On 2026-08-25 the dashboard was found rendering a Market structure that a "BASELINE v1.8
LOCKED" report appeared to contradict. Diagnosis showed **no drift and no staleness**: the
workbook, the derived JSON, `status.json` and the manifest all carried the same md5, and the
dashboard was rendering the truth.

The cause was that **two different campaigns were both called v1.8**:

1. **v1.8 — Trade on Chart split.** Executed 2026-08-23. Verified on disk: 430 → 432 rows,
   `SAU-221` and `US-176` created as Gap children on Stock Page #32. Backup, snapshot and
   commit `ce987d8` all exist. This campaign's lock line was real.
2. **"v1.8" — Unified Market Contract.** Never executed. It stopped at the mapping pause
   awaiting the ordered contract outline, so it produced no writes at all.

Reading (1)'s lock line as (2)'s completion is what created the appearance of a phantom
report. The Market structure looked untouched because it *was* untouched — v1.8 only changed
Stock Page.

**Two rules follow:**

- **A version number is consumed the moment it is locked.** It may never be reused for a
  different campaign. When a brief reuses a locked number, say so and renumber before starting.
- **The evidence bundle above makes this self-correcting**: bundle (e) prints rows specific to
  the campaign being claimed, so a lock line can no longer be matched to the wrong campaign.

*Source: Ahmed Alghamdi · 2026-08-25*

---

## 1. Locked structure

Sub-items are rows carrying a `sub-of:<parent-id>` tag. "Top-level" = rows on the screen with
no `sub-of:` tag. Counts below are the contract — any edit that changes them needs a new
baseline version.

### All Portfolios View — 9 top-level · 12 rows total

| # | ID | Status | Feature |
|---|---|---|---|
| 1 | SAU-151 | Live | Today Gain |
| 2 | SAU-152 | Live | Market Value |
| 3 | SAU-153 | Live | Total Cash |
| 4 | SAU-154 | Live | Total Gain |
| 5 | SAU-155 | Live | **All Holdings List** |
| | └ SAU-156 | Live | Holding Details |
| | ⠀⠀└ SAU-178 | Live | Update Avg Cost Price |
| 6 | SAU-157 | Live | **Orders Across All Portfolios** |
| | └ SAU-158 | Live | Order Details |
| 7 | SAU-159 | Live | Holdings Distribution Across All Portfolios |
| 8 | SAU-187 | Live | Share |
| 9 | SAU-189 | Live | Hide Balance |

### One Portfolio View — 23 top-level · 47 rows total

| # | ID | Status | Feature |
|---|---|---|---|
| 1 | SAU-075 | Live | Performance Chart — *last 3 months* |
| 2 | SAU-020 | Live | Portfolio P/L View |
| 3 | SAU-160 | Live | Today Gain |
| 4 | SAU-161 | Live | Market Value |
| 5 | SAU-162 | Live | Total Cash |
| 6 | SAU-163 | Live | Total Gain |
| 7 | SAU-177 | Live | **Holdings List** |
| | └ SAU-141 | Live | Holding Details |
| | ⠀⠀└ SAU-022 | Live | Update Avg Cost Price |
| | ⠀⠀└ SAU-098 | **Gap** | Auto Dividend Reinvest |
| 8 | SAU-120 | Live | **Orders** |
| | └ SAU-164 | Live | Order Details |
| 9 | SAU-137 | Live | Transactions |
| 10 | SAU-143 | Live | Holdings Distribution |
| 11 | SAU-026 | Live | Tradable Rights |
| 12 | SAU-102 | Live | Rights Issue |
| 13 | SAU-150 | **Planned** | Dividends List |
| 14 | SAU-175 | Live | **Customizations** |
| | └ SAU-142 | Live | Holdings |
| | └ SAU-172 | Live | Orders |
| 15 | SAU-081 | Live | **Reports** |
| | └ SAU-179 … SAU-185 | Live | Overview · Gain/Loss · Statement · Orders · Transfer · Market · Finance |
| 16 | SAU-165 | Live | Disable Portfolio |
| 17 | SAU-080 | Live | **Liquidate Portfolio** |
| | └ SAU-176 | Live | All Stocks |
| | └ SAU-169 | Live | Select Stocks |
| 18 | SAU-078 | Live | Transfer Stocks |
| 19 | SAU-166 | Live | Rename Portfolio |
| 20 | SAU-167 | Live | Copy Portfolio Number |
| 21 | SAU-168 | Live | Hide Balance |
| 22 | SAU-186 | **Planned** | **Portfolio Analysis** |
| | └ SAU-084 | Planned | Peer Portfolio Comparison |
| | └ SAU-086 | Planned | Portfolio Health Score |
| | └ SAU-087 | Planned | Allocation Tracker |
| | └ SAU-090 | Planned | Goal Tracker |
| | └ SAU-092 | Planned | StoryTeller |
| | └ SAU-140 | Planned | Portfolio Backtesting |
| | └ XJ-050 | Planned | Daily Brief |
| | └ XJ-055 | Planned | Custom Index Against Benchmark |
| | └ XJ-063 | Planned | Personal Investment Manager |
| 23 | SAU-188 | Live | Share |

**Count derivation.** All Portfolios View: 9 top-level + 3 nested = **12**.
One Portfolio View: 23 top-level + 24 nested = **47**.
Nested = Holdings List 3 · Orders 1 · Customizations 2 · Reports 7 · Liquidate Portfolio 2 ·
Portfolio Analysis 9. *(The v1.1 document originally stated 48; corrected to 47 on 2026-08-17.)*

---

## 1a. Level1–Level7 hierarchy columns (v1.3)

Columns **U–AA** (`Level1`…`Level7`) carry the explicit path for every Saudi Portfolio row.
They are a *derived projection* of `screen` + `sub-of:` parentage — the tree remains the
source of truth; the columns exist so the path is readable without traversing tags.

| Level | Value |
|---|---|
| Level1 | `ARC Platform` — every row |
| Level2 | `Saudi Market` |
| Level3 | `Portfolio` |
| Level4 | `All Portfolios View` or `One Portfolio View`; **empty for backlog rows** |
| Level5 | group — `Holdings`, `Orders`, `Customizations`, `Reports`, `Liquidate`, `Analysis`; empty for direct features |
| Level6 | feature name; **empty on the group container rows themselves** (they stop at Level5) |
| Level7 | only `Update Avg Cost Price` and `Auto Dividend Reinvest`, under `… > Holdings > Holding Details` |

**Group containers** (Level5 filled, Level6 empty): SAU-155 / SAU-177 → Holdings ·
SAU-157 / SAU-120 → Orders · SAU-175 → Customizations · SAU-081 → Reports ·
SAU-080 → Liquidate · SAU-186 → Analysis.

**Reference path:**
`ARC Platform > Saudi Market > Portfolio > One Portfolio View > Analysis > Peer Portfolio Comparison`

### Consistency rules (verified on every edit)
1. Level1–Level3 filled on every in-scope row
2. Level4 filled **iff** the row has a screen
3. No skipped levels — a filled Level6 requires a filled Level4; a filled Level7 requires Level5 **and** Level6
4. The Level path must agree with `sub-of:` parentage
5. Level7 restricted to the two designated rows (three rows total — SAU-022, SAU-098 on One Portfolio View; SAU-178 on All Portfolios View)

**Scope:** journey `Saudi Market` **and** area `Portfolio` — 59 rows (12 + 47 on-screen).
Out of scope and deliberately unpopulated: SAU-095 Sectors (area Market), SAU-036 Order
Filter Panel (area Orders), SAU-024 Instant Settlement (journey Cash Management), and all
US Trading / Mutual Funds / Robo Advisory / Onboarding rows.

---

## 1b. Market area IA (v1.4)

The Market area carries **two screens**. `Level3 = Market` for both; `Level4` separates them.

### Design decisions
1. **Stock Page is its own Level4 screen.** Market Page item 10 is a **navigation link** to it —
   no feature row exists for the link.
2. **Dual placements are intentional**, one row per screen, same pattern as Share / Hide Balance
   in Portfolio: **Earnings Calendar** (market + stock), **Whale/Institutional Trades**
   (market + stock, the latter under Analyst Ratings), **Unusual Activity** (market + stock).
3. **Statuses come from the workbook by ID.** This campaign changed structure and Level paths,
   never statuses. The 8 known gaps stayed Gap. Genuinely new rows were created **Planned**.
4. **Level paths:** L1 `ARC Platform` · L2 `Saudi Market` · L3 `Market` ·
   L4 `Market Page` | `Stock Page` · L5 group · L6 feature · L7 sub.

### Market Page — 15 top-level + nav link · 26 rows
Market Chart · Market Hours · Market Summary · **Stock Search** · **Market Sectors** ↳Sector
Details ↳Volatility · **Stocks** ↳Trending ↳Top Gainers ↳Top Losers ↳Most Active by Quantity
↳Most Active by Value ↳Top Traders ↳Sharia Stock · Economic Calendar · Earnings Calendar *(gap)*
· Dividend Calendar · **News** ↳News Screener *(gap)* · **Stock Screener** *(gap)* ↳Saved Themes
*(gap)* · Analysis Changes *(gap)* · ETF View · Whale/Institutional Trades *(gap)* ·
Unusual Activity *(gap)* · → *nav link to Stock Page (item 10, not a row)*

### Stock Page — 19 top-level · 35 rows
Why Is It Moving *(gap)* · Earnings Calendar · Trending Tag · **Stock Details** ↳Market Depth
↳Traders Summary ↳Key Statistics · Stock News · **Options** ↳Options Chain · **Analyst Ratings**
↳**Analyst Ratings Summary** ↳↳Analyst Ratings Details ↳Bulls vs Bears *(gap)* ↳Technical
Analysis ↳Whale/Institutional Trades *(gap)* · **Financial** ↳Statements ↳Earnings ↳Actions ·
**Profile** ↳Major Shareholder · Holding · **Traders** ↳Insider Traders *(gap)* ↳Government
Traders *(gap)* · Share Stock · Add to Watchlist · **Stock Performance Chart** ↳Historical Data ·
Compare Stock · AI Assistant *(gap — SAU-121, initiative: ai-guided-investing)* · Stock Key Fact
*(gap)* · Stock Dividend · Unusual Activity *(gap)*

### Backlog — none (v1.4.1)
The three rows held off-screen in v1.4 were **removed on 2026-08-17** at Ahmed's instruction:
`XJ-015` Liquidity Indicators · `SAU-139` Price Chart Corporate Actions Adjustment ·
`XJ-012` Intl Indices Historical Data. All were Planned; none was on a screen.

**Every Saudi Market row now sits on Market Page or Stock Page — the area has no backlog.**

Their US Trading twins were **kept**, since the instruction was scoped to Saudi:
`US-106` Liquidity Indicators (Live) · `US-107` Intl Indices Historical Data (Planned) ·
`US-131` Price Chart Corporate Actions Adjustment (Planned). Saudi↔US parity is broken for
these three by design — revisit in the US campaign.

### Renames (v1.4) — canonical workbook names
Each row carries a `renamed-from:<old>, v1.4` note so evidence citations in reports and
`coverage.json` stay traceable.

| Was | Now |
|---|---|
| Sectors | Market Sectors |
| Sector & Exchange Volatility | Volatility |
| Trending Stocks | Trending |
| Shariah Compliance Lists | Sharia Stock |
| Dividends Calendar | Dividend Calendar |
| Market News | News |
| ETF Exposure View | ETF View |
| Level 2 Order Book | Market Depth |
| Stock Profile | Profile |
| Stock Comparison | Compare Stock |
| Stocks Key Facts | Stock Key Fact |

---

## 1c. Orders area IA (v1.5)

`Level3 = Orders` · `Level4 = Orders Page` · L5 group · L6 feature. Order comes from
**`display_order`** (col AB), written by `scripts/converge-contract.py`.

### Orders Page — 5 top-level · 25 rows
**Order Types** ↳Market ↳Limit ↳Stop Loss ↳Take Profit ↳MOC (Market On Close) ↳Iceberg *(gap)*
↳Bracket ↳Conditional ↳Attached ↳Slicing ↳Trailing *(gap)* ↳Chain *(gap)* ↳Basket ↳Options ·
**Order Details** ↳Quick Reorder ↳Cancel ↳Edit ↳Convert to Market Price ↳Partial Execution ·
**Order Filter** ↳Orders History · Fast Order (No Confirmation) *(gap)* · Customize Orders View

### Rows relocated out of Orders (Ahmed, 2026-08-17)
| Row | To | Why |
|---|---|---|
| SAU-046 Sukuk Trading | **Market Page** | instrument access, not an order type. Priority 6 — the highest-ranked row in Saudi Market |
| SAU-113 Futures Trading | **Market Page** | instrument access |
| SAU-048 Trade on Chart | **Stock Page** | a chart action, belongs with the stock chart |
| SAU-035 Basket Order | Orders Page → **Order Types** | |
| SAU-126 Options Order | Orders Page → **Order Types** | |
| SAU-147 Orders History | Orders Page → **Order Filter** | |

Market Page becomes **17 top-level / 28 rows**; Stock Page **20 top-level / 36 rows**.
Sukuk and Futures were placed immediately after **ETF View**, grouping instrument access
together; Trade on Chart follows **Stock Performance Chart**.

### Customize Orders View — the dual placement already existed
`SAU-148` (Orders area, previously unplaced) now sits on **Orders Page**.
`SAU-172` remains the **One Portfolio View → Customizations → Orders** child. No third row was
created; Portfolio is unchanged at 12 + 47.

*(The v1.5 brief assumed SAU-148 was the Portfolio-placed row. It was not — SAU-172 is, having
been renamed to "Orders" in v1.2.1. Mapping SAU-148 here placed an orphan rather than adding a
duplicate.)*

### Rename caution
16 rows were shortened to bare type names — `Market`, `Limit`, `Edit`, `Cancel`, `Chain`,
`Options`, `Basket`. Several now collide: **`Market`** with the Reports child `SAU-184` and with
Level5 values; **`Options`** with `SAU-012` on Stock Page. Structurally safe under the key-by-ID
rule, ambiguous in prose. Each row carries `renamed-from:<old>, v1.5`.

---

## 1d. US Trading structure mirror (v1.6, 2026-08-18)

The Saudi Market / Stock Page / Orders / Portfolio **structure** was mirrored onto US Trading.
**Structure only** — no feature row was invented, and **no status was written to any existing
row** (verified: 0 status changes, 0 name changes, 0 Saudi rows touched across 115 modified rows).

### What mirrored

| Saudi screen | US rows placed | of Saudi contract |
|---|---:|---:|
| Orders Page | 25 | 25 |
| Market Page | 17 | 28 |
| Stock Page | 21 | 36 |
| One Portfolio View / All Portfolios View | 31 | — |

US Trading areas now match Saudi: **Market** (Market Page + Stock Page screens) · **Portfolio**
(All Portfolios View + One Portfolio View) · **Orders** (Orders Page) · **Watchlist**.

### Six structural containers created

These exist in the Saudi contract, had mapped children in US, and without them the children
have nothing to hang from — which is exactly why the earlier Portfolio mirror rendered flat.

| ID | Container | Screen | Mirrors |
|---|---|---|---|
| US-145 | Stocks | Market Page | SAU-194 |
| US-146 | Profile | Stock Page | SAU-122 |
| US-147 | Traders | Stock Page | SAU-214 |
| US-148 | Order Types | Orders Page | SAU-219 |
| US-149 | Order Details | Orders Page | SAU-220 |
| US-150 | Portfolio Analysis | One Portfolio View | SAU-186 |

All six were created **Planned**, matching the v1.4/v1.5 precedent for new rows. Tagged
`structural-container, mirrors:<saudi-id>`.

**Open question for Ahmed:** a container's status is scaffolding, not a delivery claim.
`Order Types` reads Planned while thirteen of its fourteen children are Live. Six Planned rows
also inflate the US Planned count. The alternative is to derive a container's status from its
children. Saudi has the same issue (SAU-219/220), so any change should apply to both.

### Mapping method

An explicit **Saudi-ID → US-ID table**, curated pair by pair — never fuzzy, never by name
(standing rule §2a). A first attempt at normalised name matching scored 39/106 on US and
**0/20 on Mutual Funds**, which is what exposed the finding below.

### Screens deleted by the mirror

`Market Data` · `Order Page` · `Order Customisation` · `Orders on Portfolio` · `Charting` ·
`Intelligence` — ad-hoc US screen names with no Saudi equivalent. Rows on them kept their
status and moved to backlog, tagged `backlog:mirror-v1.6`. The US **area** named `Stock Page`
was folded into `Market` to end the area/screen name collision.

### Rows deliberately left in backlog (13)

No unambiguous Saudi counterpart, so placing them would have been invention:
US-005 Options *(duplicate of US-116)* · US-008 Government Trades *(duplicate of US-119)* ·
US-013 Pre/Post Market Trading · US-014 / US-113 Fractional Shares (IBKR / GTN) ·
US-020 Bonds Trading · US-031 Insider Trades *(duplicate of US-123)* · US-106 Liquidity
Indicators · US-107 Intl Indices Historical Data · US-114 Trailing Order (GTN) ·
US-131 Price Chart Corporate Actions Adjustment · US-136 Quick Trade Ticket ·
US-128 Multi Views.

Three of these are the **US twins retained when the Saudi equivalents were removed in v1.4.1**
(US-106, US-107, US-131) — parity was deliberately broken there, and the mirror preserves that.
Three others are same-name duplicates across the old Market / Stock Page areas.

### Mutual Funds and Robo Advisory — the Saudi contract does not apply

Their rows are product-specific (`Subscribe to SAR/USD Fund`, `Mashura Reports`,
`Fund Recommender`). There is no counterpart to Market Chart, Order Types or Stop Loss —
**zero of 31 rows matched anything in the Saudi contract**, and that is a true finding, not a
matching failure. Mirroring Saudi's Market/Orders IA onto them would have created empty
scaffolding.

What they received instead: Level1–7 paths completed on every row that has a screen, and
`display_order` populated so their screens render deterministically. Their own IA remains
undefined — it needs its own contract, not a mirror.

*Source: Ahmed Alghamdi · 2026-08-18*

---

## 1e. Container status rule (v1.6.1, 2026-08-18)

A **container** is a row whose only role is holding children. It is scaffolding, not a
delivered feature.

### The rule
1. Containers carry `is_container = TRUE` in column **AC**.
2. **Container status is derived, never typed:** `Live` if any child is Live, else `Planned`.
   `derive_status.py` computes it at generation from `sub-of:` parentage — keyed by ID, never
   by name. The derived value is written back to the workbook status cell (tagged
   `derived, v1.6.1`) so the sheet and the JSON always agree. Verified: 0 disagreements.
3. **Every KPI and maturity count excludes containers** — features only. Applied in
   `cockpit.html`, `heatmap.html`, `screens.html` and the atlas stat bar.
4. Containers render their glyph from the derived value and **never carry the ↻ evidence
   marker** — they hold no evidence of their own, so `evidence_count`, `pressure` and
   `priority` are all forced to 0/null and `status_conflict` to false. A ↻ on a container
   would be noise, not signal.

### The 12 containers

| ID | Container | Journey | Typed was | Derived |
|---|---|---|---|---|
| SAU-194 | Stocks | Saudi Market | Planned | **Live** |
| SAU-203 | Stock Details | Saudi Market | Planned | **Live** |
| SAU-209 | Financial | Saudi Market | Planned | Planned |
| SAU-214 | Traders | Saudi Market | Planned | Planned |
| SAU-219 | Order Types | Saudi Market | Planned | **Live** |
| SAU-220 | Order Details | Saudi Market | Planned | **Live** |
| US-145 | Stocks | US Trading | Planned | **Live** |
| US-146 | Profile | US Trading | Planned | Planned |
| US-147 | Traders | US Trading | Planned | **Live** |
| US-148 | Order Types | US Trading | Planned | **Live** |
| US-149 | Order Details | US Trading | Planned | **Live** |
| US-150 | Portfolio Analysis | US Trading | Planned | Planned |

8 of 12 flipped Planned → Live. No non-container row changed status.

### How a container was identified
Three signals had to agree: the row **has children**, its **Level5 is set with Level6 empty**
(the grouping signature from §1a), and it carries **no evidence of its own** — no definition,
no BRD, no competitor coverage. The third test is what separates scaffolding from a real
feature that happens to have children.

**Parents deliberately NOT flagged** — they have children but are real, evidenced features:
SAU-012 Options · SAU-036 Order Filter · SAU-039 Stock Screener · SAU-067 News ·
SAU-095 Market Sectors · SAU-122 Profile · SAU-135 Analyst Ratings · SAU-217 Stock
Performance Chart · SAU-207 Analyst Ratings Summary · US-002 Stock Profile Page ·
US-038 Order Filter Panel · US-064 Sectors · US-066 Market News · US-127 Analyst Ratings.

### Effect on counts

| Market | Planned typed | Planned derived | Planned features-only |
|---|---:|---:|---:|
| Saudi Market | 49 | 45 | **43** |
| US Trading | 25 | 21 | **19** |
| Mutual Funds | 5 | 5 | 5 |
| Robo Advisory | 0 | 0 | 0 |

US Planned drops 25 → 19: four containers flipped to Live, two more are excluded as
scaffolding. Atlas feature count reads **393**, not 405 — the 12 containers still render as
grouping nodes but no longer count as features.

### ⚠ Open asymmetry — the eight Saudi Portfolio group containers

§1a already documents these as **group containers**: SAU-155 All Holdings List ·
SAU-177 Holdings List · SAU-157 Orders Across All Portfolios · SAU-120 Orders ·
SAU-175 Customizations · SAU-081 Reports · SAU-080 Liquidate Portfolio ·
**SAU-186 Portfolio Analysis**.

They were **not** flagged, because the approved scope named "the Saudi group containers from
v1.4/v1.5" and these come from v1.2.1/v1.3. Consequences:

- **SAU-186 Portfolio Analysis is not a container while its direct US twin US-150 is** — the
  mirror created US-150 explicitly to mirror SAU-186. In the atlas today, Saudi's shows a ↻
  and US's does not.
- All eight carry real definitions and read as genuine features (a holdings list *is* a
  feature), so flagging them is not obviously right.
- Flagging them would remove roughly 8 more rows from Saudi's counts, most of them Live —
  a visible drop in Saudi Live.

**Decision needed from Ahmed:** flag all eight for symmetry, flag SAU-186 only (closing the
twin asymmetry), or leave as is.

*Source: Ahmed Alghamdi · 2026-08-18*

---

## 1f. US Market completion (v1.7, 2026-08-18)

The full Saudi Market Page + Stock Page contract **as it stands today (post-v1.4.1)** now
applies to US Trading. The converge script **reads the contract out of the Saudi rows in the
workbook** rather than restating it, so US can only converge to what Saudi actually is.

### Acceptance — structural tree diff, Saudi Market vs US Market

**PASS.** All **67 Saudi Market nodes are present in US, in identical nesting and identical
display order.** Zero missing. Eleven extra US nodes, every one classified:

| Class | Nodes |
|---|---|
| `us-only` | US-013 Pre/Post Market Trading · US-014 / US-113 Fractional Shares (IBKR/GTN) · US-020 Bonds Trading |
| Backlog group node | render-layer container, holds nothing of its own |
| `deliberate-break:v1.4.1` | US-106 Liquidity Indicators · US-107 Intl Indices Historical Data · US-131 Price Chart Corporate Actions Adjustment |
| `duplicate-of:` | US-005 (→US-116) · US-008 (→US-119) · US-031 (→US-123) |

**Unclassified differences: 0.** Statuses are excluded from the diff by design.

### Counts

| Screen | Rows | Top-level |
|---|---:|---:|
| Saudi Market Page | 28 | 17 |
| **US Market Page** | **32** (28 shared + 4 us-only) | **21** |
| Saudi Stock Page | 36 | 20 |
| **US Stock Page** | **36** | **20** |

Saudi and Portfolio counts unchanged. 405 → 430 rows, **25 created, 0 deleted, 0 statuses
changed, 0 Saudi rows modified, 0 US Portfolio rows modified.**

### Canonical vocabulary (decision A)

Every US row occupying a contract slot now carries the Saudi canonical name — **19 renames**,
each with a `renamed-from:<old>, v1.7` note. The `(US)` suffixes are retired: journey + ID
distinguish rows, and the suffixes date from the pre-Level-column name-collision era.

Two renames also stripped **trailing whitespace** that had been sitting in the sheet:
`Earnings Calendar ` and `Dividends Calendar `.

**US-002 needed more than a rename — the markets were inverted.** Saudi has `Stock Details` as
a *container* and `Profile` as a real Live feature; US had US-002 Stock Profile Page as the
real feature and a container holding Profile. Resolved by **US-002 → `Profile`** (with US-025
Major Shareholder beneath it) and **US-146 → `Stock Details`** as the position-4 container.
Both rows reused; nothing deleted.

### Sukuk and Futures are shared, not us-only

The campaign brief listed them as us-only. They are not: Saudi carries SAU-046 Sukuk Trading
(Live) and SAU-113 Futures Trading (Gap) on Market Page, both already mapped to US-098 /
US-021. Tagging them `us-only` would have misclassified them in the parity report.

### Backlog rendering (decision C) — the fix was in the renderer

The workbook was correct: `screen`, all Level columns and `display_order` were empty on every
backlog row. The **renderer** placed screenless rows as direct children of the area node, so
they rendered as *peers of Market Page and Stock Page* — indistinguishable from being on a
screen. Saudi never exposed this because no Saudi Market row is screenless.

Screenless rows now group under an explicit **Backlog** node — but only when the area also has
screens. Where an area has none (Watchlist), rows stay direct, so §2b's single-screen work is
not regressed.

### Node IDs now reach the renderer

`makeFeatureNode` attaches `o.id`. The first run of this acceptance test reported a false
failure on `Options` because the classifier looked tags up **by name**, and `Options` exists in
both journeys — the §2a trap, hit inside the verification code itself. Carrying the ID makes
name-keyed checks unnecessary.

### Housekeeping — baseline file renamed (done 2026-08-18)

`ARC-SAUDI-PORTFOLIO-BASELINE.md` was wrong twice over — no longer Portfolio-only, no longer
Saudi-only. Renamed to **`ARC-STRUCTURE-BASELINE.md`**, with `BASELINE_MD` in
`scripts/derive_status.py` updated in the same commit so `baseline_version` never resolved
against a missing file.

Snapshots covering **both** markets were renamed `saudi-structure-BASELINE-v*` →
**`structure-BASELINE-v*`**: v1.6, v1.6.1, v1.7.

Earlier snapshots **keep their original names**, because those names are accurate for what
they contain: `saudi-portfolio-BASELINE-v1.1…v1.3` really are Saudi Portfolio only, and
`saudi-structure-BASELINE-v1.4…v1.5` really are Saudi structure only. Renaming them would
make the archive claim a coverage those files never had.

**Convention going forward:** `structure-BASELINE-v<version>-<date>.xlsx`.

*Source: Ahmed Alghamdi · 2026-08-18*

---

## 1g. Trade on Chart split (v1.8, 2026-08-23)

`Trade on Chart` was carrying two claims at once: the capability is **Live** (verified by Ahmed
2026-08-11) while the *depth* a competitor shipped is not. One row cannot be both, and each
week's answer was overwriting the other.

Split instead of overwritten:

| ID | Row | Status |
|---|---|---|
| SAU-048 / US-077 | **Trade on Chart** — place orders directly on the price chart | Live |
| **SAU-221 / US-176** | └ **Drag and Drop Trade on Chart** — drag a line to set the target price and send the order from the chart, then edit stop-loss and watch P/L without leaving it | **Gap** |

Created at Stock Page position **32** in both markets; the five rows below shifted down one.
Per §1a the parent now stops at Level5 (`Trade on Chart`) with Level6 cleared, because it has a
child. Same canonical name in both markets per §1d — no suffixes.

**The Sahm evidence moved with the depth**, from `SAU-048::Sahm` to `SAU-221::Sahm`. That is the
point of the split: SAU-048 keeps its Live verification, and the competitive pressure attaches
to the row that is actually behind.

Counts: Saudi and US Stock Page **36 → 37 rows**, top-level unchanged at 20. 430 → 432 rows,
2 created, 0 deleted, **0 statuses changed on existing rows**.

### Benchmarks are canonical in the workbook, not in JSON

`Raseed` was added to `benchmarks.json` by hand and silently wiped on the next run:
`xlsx-to-features-json.py` regenerates that file from the **Benchmarks sheet** in the workbook,
which states it plainly — *"Canonical list. Competitor names in the Features sheet must match
these exactly. Add new competitors here first."* Raseed is now on the sheet and survives
regeneration.

**Open hygiene item:** 14 competitor names used in the Features sheet are not in the registry —
mostly qualified variants (`Derayah (2 stocks)`, `Moomoo (6 stocks)`) and comma-split artifacts
(`Moomoo (comments`, `polls)`). Each one is evidence the pressure score cannot see.

*Source: Ahmed Alghamdi · 2026-08-23*

---

## 1h. Unified Market Contract (v1.9, 2026-08-25)

One contract, applied to **both** market journeys in a single atomic converge. Ahmed's rulings
were a **delta on the locked v1.8 structure — unnamed rows stay**; nothing disappeared that was
not explicitly ruled absorbed or backlogged.

### Counts

| Screen | Rows | Top-level |
|---|---:|---:|
| Market Page — Saudi | 24 | 16 |
| Market Page — US | 28 (24 shared + 4 us-only) | 20 |
| Stock Page — both | 34 | 18 |

444 features. Portfolio and Orders untouched (12 / 47 / 25 unchanged).

### Feature boundary (`content_spec`, column AD)

Data fields, table columns, period toggles and session variants are **not rows**. They are
stored verbatim on the owning feature. Session variants: `trading` applies to both markets,
`pre/post` is marked us-only inside the spec text.

### Renames — spec vocabulary, both markets

Market Chart → **Market indices chart** · Trending Tag → **Trending stocks** ·
Holding → **Holdings** · Traders → **Trades** · Insider Traders → **Insider Trades** ·
Government Traders → **Government Trades** · Stock Performance Chart → **Stock chart**.

`Traders Summary` (under Stock Details) deliberately **keeps its name**, so the old
Traders/Trades collision stays dead.

### Absorbed (7 per market, retired with lineage)

Market Summary → Indices change · Saved Themes → Stock Screener · News Screener → News ·
Stock-Page Earnings Calendar → Earnings · Analyst Ratings Summary + Details → Analyst Ratings ·
Historical Data → Stock chart.

Each keeps its row and status, loses its placement, and carries `absorbed-into:<id>`. The
absorbed description is appended to the target's `content_spec`.

### Backlogged (6 per market, `gap-unplaced`)

Analysis Changes · Whale/Institutional Trades (both placements) · Unusual Activity (both
placements) · Stock Key Fact. Screens cleared, Gap status kept, for roadmap review.

### New rows (6 per market, Planned)

Indices change · Stock list · Income Statement · Balance Sheet · Cash Flow · Add Alert.
`Add Alert` is tagged `related-to:XJ-020` — the capability stays in Platform, this is the
surface entry point.

### Financial (rule 3 as amended)

`Financial` → **Statements** (Income Statement, Balance Sheet, Cash Flow, Earnings) **+ Actions**.

### Backlog rendering — deterministic order

The Saudi-vs-US diff initially FAILED on the Backlog node: backlogged rows carry no
`display_order` by design, so the renderer fell back to workbook row order, which differs
between markets. The residue, not the contract, was failing the test. Loose rows are now sorted
by name, and the diff passes.

*Source: Ahmed Alghamdi · 2026-08-25*

---

### v1.9.1 patch — two contract misses, two accepted deviations

**Fixed.** Checked by ID first; no existing row mapped to either, so both were created Planned.

- **Stock change** — Stock Page top-level, position 1, both markets.
  `content_spec`: *Price change per session: pre-market (us-only), post-market (us-only), trading.*
- **Indices page · Indices stocks · Indices options** — children of Indices change, both
  markets. **Indices change becomes a container** (`is_container`, status derived from children).

Counts after the patch: **Market Page 27 (Saudi) / 31 (US, incl. 4 us-only) · Stock Page 35
both markets** · 452 features.

**Accepted deviations from the spec — recorded, no data change.**

1. **Stocks and Analyst Ratings remain containers.** The spec lists items 5–9 and 9–11 flat;
   they are grouped here for IA hygiene. Approved 2026-08-25.
2. **`Sharia Stock` stands** for the spec's *Sharia stock list*; the `renamed-from` lineage
   covers the mapping. **The `Options` half of this deviation was RETIRED in v1.9.9** — the row
   is now `Stock options`, matching the spec.

*Source: Ahmed Alghamdi · 2026-08-25*

---

### v1.9.2 — backlog resolution

Element-by-element rulings, both markets symmetric. **Supersedes the earlier
archive/absorb/consolidate proposal, which was not applied.**

**Market Page → 32 rows / 19 top-level (Saudi), 36 / 23 (US).**
Analysis Changes restored top-level, **Gap → Planned** (*prioritized to Planned per backlog
review*) · News Screener → child of News · Saved Themes → **Screener Themes**, child of Stock
Screener · Unusual Activity and Whale/Institutional Trades restored top-level.

**Stock Page → 41 rows / 22 top-level, both markets.**
Analyst Ratings Summary + Details un-retired in their **pre-absorb shape** — Summary under
Analyst Ratings, Details under Summary · Historical Data un-retired as **Historical Data
(Corporate Action)**, child of Stock chart · Stock Key Fact, Unusual Activity and
Whale/Institutional Trades restored top-level.

**Deleted:** the backlog duplicate Earnings Calendar (SAU-201 / US-161) — *removed, Market Page
row is the sole placement*. `SAU-107` / `US-028` are now the only Earnings Calendar rows.

**Un-retire lineage:** `absorbed-into:X` becomes `restored:v1.9.2` + `was-absorbed-into:X`, so
the history survives the reversal. The absorbed text was stripped from the four targets;
curated spec lines stay — Stock chart keeps *"Ranges: max. Chart types: candle."*

### v1.9.3 — ruling 12

`Market Summary` un-retired to **Market Page top-level, position 3, after Market Hours**, both
markets, status Planned unchanged. Lineage kept: `restored:v1.9.3` + `was-absorbed-into:`.
`Indices change` content_spec drops the absorbed text and keeps its curated line —
*"Market summary figures: index level, change, % change."*

Market Page → **33 rows / 20 top-level (Saudi), 37 / 24 (US)**.

**Saudi Backlog fan: EMPTY.** ✅

### ⚠ US Backlog is not empty — 6 rows, all prior recorded decisions

The rulings covered 12 of 13 Saudi backlog rows. What remains:

| Row | Tag | Origin |
|---|---|---|
| US-005 Options · US-008 Government Trades · US-031 Insider Trades | `duplicate-of:` | v1.6 mirror — same-name twins of rows already placed |
| US-106 Liquidity Indicators · US-107 Intl Indices Historical Data · US-131 Price Chart Corporate Actions Adjustment | `deliberate-break:v1.4.1` | US twins deliberately kept when the Saudi equivalents were removed |

Emptying the US fan means reversing those two recorded decisions. **Not done without a ruling.**

*Source: Ahmed Alghamdi · 2026-08-25*

---

### v1.9.4 — session variants promoted to rows

**Supersedes the `content_spec` treatment for four features only.** Under **Top Gainers, Top
Losers, Most Active by Quantity, Most Active by Value**, the session views are now rows:
**Trading · Pre · Post**, in that order. 12 new rows per market, **24 total**, all Planned —
no existing row mapped by ID.

- **Parents keep their typed statuses and are NOT containers.** They are features with session
  views, so `is_container` stays FALSE and their status is typed, not derived.
- **Trending and Top Traders get no session children**, per the spec.
- Level path: `… > Stocks > <parent> > <variant>` at L7.
- Parents carry the lineage note `session-variants promoted to rows, v1.9.4`.

Market Page → **45 rows / 20 top-level (Saudi), 49 / 24 (US)**. Top-level unchanged — every new
row is a child. Stocks subtree: **6 features + 12 variant rows** per market. 474 features.

**Ruling 3 was a no-op on content_spec.** Those four rows never carried session text: the v1.9
`CONTENT_SPEC` map wrote session variants only to **Top Traders** (*"Session variants n/a"*) and
**Trade on Chart**. Both are correct as they stand — Top Traders takes no session children by
ruling 4, and Trade on Chart is outside this ruling's scope. The lineage note was added to all
four parents regardless, so the decision is legible on the row.

**⚠ Name-collision load.** `Trading`, `Pre` and `Post` now name **24 rows** across the two
markets. This is safe under §2a — everything keys by ID, and the Level path disambiguates — but
it is the largest single increase in duplicate names in the map, and any prose reference to
"Pre" or "Post" is now ambiguous without its parent.

*Source: Ahmed Alghamdi · 2026-08-25*

---

### v1.9.5 — ETF restructure

`ETF View` → **`ETF list`**, same row and ID in both markets, `renamed-from:ETF View, v1.9.5`.
Market Page position unchanged (#41, top-level #16). **Statuses unchanged: SAU-110 Live,
US-017 Gap** — the US twin has always been a Gap, so "status Live unchanged" holds for Saudi
only, and statuses stay keyed by ID.

**`ETF Page` registered as a screen** in `data/screen-nav.json`: own Level4,
`nav_parent: Market Page`, `nav_position: 17` — immediately after ETF list. Same mechanism as
Stock Page.

**Amended same day — ETF Page anchors to the ETF list ROW, not a sibling slot.** The tree reads
`Market Page → ETF list → ETF Page ▸`, the list → detail-page pattern. See §2c.

The amendment also resolved the empty-screen limitation: **`screen-nav.json` is now the screen
registry**, so a screen named there renders with zero feature rows. ETF Page is visible today
and will fill as rows are added.

Only two cells changed in the whole workbook: the two name fields. 474 features, all counts
unchanged.

*Source: Ahmed Alghamdi · 2026-08-25*

---

### v1.9.6 — Sukuk restructure

`Sukuk Trading` → **`Sukuk list`**, same row and ID in both markets, `renamed-from:Sukuk
Trading, v1.9.6`. Position unchanged (#42, top-level #17). **Statuses unchanged: SAU-046 Live,
US-098 Gap** — as with ETF, the US twin has always been a Gap, so "status Live unchanged" holds
for Saudi only.

**`Sukuk Page` registered** with `nav_anchor: SAU-046 / US-098` — the same mechanism as ETF
Page, so the tree reads `Market Page → Sukuk list → Sukuk Page ▸`. **Awaits its outline**: it
renders as an empty screen node today and fills as rows are added.

Only two cells changed in the whole workbook. 474 features, all counts unchanged. Six nav rules
now load: Stock Page ×2 (by position), ETF Page ×2 and Sukuk Page ×2 (by anchor).

**Pattern note:** ETF and Sukuk are now the same shape — a list feature on Market Page with a
detail page hanging off it. `Futures Trading` (SAU-113 / US-021) is the remaining sibling in
that group with no detail page registered.

*Source: Ahmed Alghamdi · 2026-08-25*

---

### v1.9.7 → v1.9.8 — Financial subtree (revised shape, max depth L8)

**Schema v2.0.** Two columns appended: **AE `Level8` · AF `row_type`**. v1.9.7 briefly carried a
`Level9`; the revised outline caps depth at **L8**, so Level9 was removed and `row_type` slid
from AG into AF.

**Renderer depth limit: none found.** Nesting is entirely parent-driven — `orderedScreenNodes`
recurses through `sub-of:` tags with no cap, and the Level columns never reach the JSON. L8
needed **no renderer change**.

### Shape — `Financial (3)`

```
Financial
  Statements
    Income Statement  → Annual · Quarterly
    Balance Sheet     → Annual · Quarterly
    Cash Flow         → Annual · Quarterly
  Earnings
    Next report estimation → Revenue · EPS · Date · Period
    Quarterly              → Period · Estimated · Actual · Surprise
    Annual                 → Period · Estimated · Actual · Surprise
    Revenue                → Period · Estimated · Actual · Surprise
  Actions
    Dividends · Split
```

**35 nodes per market, max rendered depth d6.** Financial's direct children are **Statements,
Earnings, Actions** — Earnings re-parented Statements → Financial, Actions returned Earnings →
Financial, both carrying `re-parented:…, v1.9.8`.

### `row_type: detail` — rendered, never counted

24 field/period leaves per market carry `row_type: detail`: the Annual/Quarterly toggles under
Statements, and Revenue · EPS · Date · Period · Estimated · Actual · Surprise · Dividends ·
Split. They render in the tree and are **excluded from feature counts, maturity KPIs and gap
metrics** in all four views.

**Verified:** 530 rows, 48 detail, **KPI feature count 465**. Against the pre-Financial baseline
of 457 that is a delta of **+8 — the four mid-level nodes per market and nothing else**. The
atlas stat bar reads **465 Features**, not 530.

Stock Page **69 rows** each market. Market Page, Portfolio and Orders untouched; no status
changed.

**Deviation on casing (unchanged from v1.9.7).** The outline writes *Income statement · Balance
sheet · Cash flow*; the map keeps canonical **Income Statement · Balance Sheet · Cash Flow**,
per §1h's precedent of not churning rows for casing alone.

*Source: Ahmed Alghamdi · 2026-08-25*

---

### v1.9.9 — Options branch

`Options` → **`Stock options`** on Stock Page, same row and ID in both markets
(`renamed-from:Options, v1.9.9`), statuses unchanged: SAU-012 Planned, US-116 Live. This
**retires the "Options stays" vocabulary deviation** recorded at v1.9.1 — see §1h.

`Options Chain` keeps its name and status. **`Options details` created** as its child at L7,
Planned, both markets — no existing row mapped.

```
Stock options
  Options Chain
    Options details
```

Stock Page → **70 rows** each market. 532 rows, KPI feature count **467** (+2, both new rows are
normal features, not detail). No status changed.

**The rename reduces a name collision rather than adding one.** Three rows were literally named
`Options`; two remain and they are genuinely different features — `SAU-126 Options` (Orders Page,
an order type) and `US-005 Options` (backlog duplicate of US-116). The Stock Page row is now
distinct from both.

*Source: Ahmed Alghamdi · 2026-08-25*

---

## 2. Status contract

Every on-screen row is **Live** except:

| Row | Status |
|---|---|
| SAU-150 Dividends List | Planned |
| SAU-186 Portfolio Analysis **+ its 9 children** | Planned |
| SAU-098 Auto Dividend Reinvest | Gap |

All Portfolios View carries **no Planned and no Gap rows**.

**Paired rows.** `Share` and `Hide Balance` each exist as exactly **two** rows — one per
screen, both Live, both top-level. Any workbook-wide search must find precisely two of each.

Every Live row must have a matching record in `data/verified_live.json`. A row that leaves
Live must have its record removed in the same edit, or hygiene will report a
verified-but-not-Live orphan.

---

## 2a. Status display principle (2026-08-17)

> **The dashboard displays the contract status; derived evidence annotates, never overrides.**

The glyph and colour on every row come from the **typed status in the workbook** — the value
this baseline locks. `derive_status.py` may compute a different state from the evidence on
file, but that is an annotation, not a correction.

| Typed status | Glyph | Colour |
|---|---|---|
| Live | ● filled | `#20C992` |
| Planned | ○ hollow | `#A2E3FF` |
| Gap | ✕ | `#F43653` |

An evidence conflict renders as a small **↻ after the child count** — `Portfolio Analysis (9) ▾ ↻`
— with a tooltip reading *"<status> — no verification evidence yet"* and, below it, what the
evidence would have classified it as and why.

**Why:** a row marked Planned in the locked baseline must read Planned on the page. Showing
`◌ Unverified` because no verification record exists yet contradicts the contract and invites
someone to "fix" a row that is already correct.

**Currently 7 conflicted rows:** SAU-144, US-136, MF-026, RBO-011 (typed Gap) · SAU-150,
US-144, SAU-186 (typed Planned) — all show their typed glyph plus the marker.

### Two vocabularies, kept apart
| Concept | Values | Source | Where it appears |
|---|---|---|---|
| **Status** (the contract) | Live · Planned · Gap | the workbook's typed column | glyphs, colours, tooltip status chip |
| **Evidence state** | Verified · **Missing evidence** | `derive_status.py` | filters, KPI counters, the ↻ marker |

`derive_status.py` still emits `Unverified` internally — that is the data value and it has not
changed. **"Unverified" no longer appears anywhere in the interface**; it renders as
**"Missing evidence"** in the filter button, the KPI tile, the journey-health column and the
↻ tooltip. The rename exists so an evidence state can never be misread as a status.

**Scope:** glyph, colour and the tooltip status chip follow the typed value. Filters and KPI
counters operate on evidence state, since that is what they are for — surfacing where evidence
is missing.

### Standing rule — key by ID, never by name
**Any check, join, lookup or diff on this dataset keys by feature ID. Never by name.**

Names repeat across journeys and across levels. This trap has bitten twice:

1. **Analyst Ratings** — an exact-name search missed `US-067`/`US-127` because they were named
   `Analyst Ratings (US)`, so two duplicate rows were created and had to be reverted.
2. **Status verification** — a name-keyed sweep reported 22 false glyph mismatches, because
   `Why Is It Moving` is Gap in Saudi Market and Live in US Trading, and the map kept only one.

Within Saudi Portfolio alone, `Orders` names three rows, and `Holding Details`, `Update Avg
Cost Price`, `Market` and `Transfer` each repeat. A name is not a key here.

**Lived example, v1.4:** the Market IA needed a `Traders` row in two places — under Stock
Details and as a top-level container. Rather than ship two identically-named siblings, the
child was named **Traders Summary** and the container kept **Traders**. Disambiguating at
design time is cheaper than defending every lookup afterwards; where a duplicate name is
unavoidable, the ID is the only safe key.

---

## 2b. Single-screen collapse (display rule, 2026-08-17)

**When an area has exactly one screen, the atlas renders that screen's rows directly off the
area node — no intermediate screen hop.** Areas with two or more screens are unchanged.

A lone screen node carries no information the area node doesn't already carry: every row
beneath it has the same screen, so the hop costs a click and a level of indentation and
returns nothing. Areas with 2+ screens keep their screen nodes, because there the screen is
the thing that distinguishes one branch from another.

**The collapsed screen's name is never visible.** The node reads `Orders` — no subtitle, no
suffix, nothing appended. The Level4 identity lives on in the data (the node carries
`screenLabel`, and every row keeps its own screen column and Level4 value in the workbook) and
surfaces only on hover, as a native tooltip. Nothing about the collapse is legible in the
label, which is the point: the nav reads **Market · Portfolio · Orders · Watchlist**, exactly
as the areas are named.

**Renderer only. The workbook, the Level1–7 columns and the screen assignments are untouched** —
every row still carries its Level4 screen exactly as locked. Turning the rule off restores the
old shape with no data change. It is generic: any area that has exactly one screen collapses,
today and in future, with no per-area configuration.

Where it fires today:

| Journey | Area | Collapsed screen (tooltip only) |
|---|---|---|
| Saudi Market | Orders | Orders Page |
| Saudi Market | Watchlist | *(none — no screen assigned; unaffected)* |
| US Trading | Stock Page | Market Data |
| Mutual Funds | Market / Portfolio / Orders | One Portfolio View |
| LMS/SBL | SBL | Order Page |
| IPOs | Subscriptions | IPO Details |
| Cash Management | Cash Management | All Portfolios View |
| Platform | Compliance | Market Home |
| Platform | Content | Copy Trading |

Saudi Portfolio and Saudi Market are unaffected — each has two screens (All Portfolios View /
One Portfolio View, Market Page / Stock Page). Verified node-for-node identical before and
after the change.

**Consequence to watch (2):** because the screen name is invisible, an area's Level4 is no
longer readable off the atlas at all. It remains in the workbook, in the Level4 column and in
the hover tooltip — but the atlas is no longer the place to check it. Use the workbook or the
derived JSON when the screen assignment is the question.

**Consequence to watch (1):** an area drops its screen hop the moment its second screen leaves, and
regains it the moment a second screen is added. That is intended, but it means a screen node
appearing or disappearing in the atlas is *not* on its own evidence of a workbook change.

*Source: Ahmed Alghamdi · 2026-08-17*

---

## 2c. Screen nav nesting (display rule, 2026-08-25)

**A screen with a `nav_parent` renders as a child NODE of that parent screen, instead of
hanging off the journey.** Collapsible, showing its own child count — `Stock Page (19) ▸`.
Expanding it fans the subtree exactly as before.

**Renderer + metadata only.** Levels, screen assignments, counts and contracts are untouched;
the workbook md5 is byte-identical across this change. Turning the rule off restores the old
shape with no data change.

The rule is **generic and config-driven** — `data/screen-nav.json`, view layer only, never
written back to the workbook. No screen is named in the renderer code. A missing or unreadable
config renders exactly as before.

| Field | Meaning |
|---|---|
| `journey` / `area` / `screen` | which screen the rule applies to |
| `nav_parent` | the screen it nests under, in the same area |
| `nav_position` | 1-based among the parent's children; `null` appends last |

Today: **Stock Page → Market Page** in both markets, appended last (spec item 16 — after the
last Market Page feature).

**Interactions with the other display rules:**

- **Single-screen collapse (§2b) is decided on the TOTAL screen count**, before nesting. Nesting
  Stock Page leaves Market Page as the only top-level screen in the area, and without this the
  area would collapse and destroy the very parent the child nests into.
- If the `nav_parent` screen is absent, the child is left top-level rather than dropped.

**Count note:** Saudi Market Page shows **(17)** — 16 features plus the Stock Page node. The
spec numbers the nav link as item 16 because it counts the link, not the features; the map
carries 16 real feature rows, so the node lands 17th. No row was added.

*Source: Ahmed Alghamdi · 2026-08-25*

---

### Amendment — anchoring a screen to a feature row (2026-08-25)

`nav_parent` now supports two anchoring modes:

| Field | Behaviour |
|---|---|
| `nav_anchor` | a **feature row ID** — the screen becomes a **child of that row**. The list → detail-page pattern. |
| `nav_position` | 1-based among the parent screen's children; omit to append last. |

Today: **Stock Page** uses `nav_position` (appended last under Market Page); **ETF Page** uses
`nav_anchor: SAU-110 / US-017`, so it renders beneath ETF list. Any future list → detail-page
pair works the same way with no code change.

**The config is now the screen registry.** A screen named in `screen-nav.json` renders even with
**zero feature rows** — previously impossible, because `buildHierarchy` derives screens purely
from `f.screen` on the rows. This is what lets a screen be registered and visible before it has
content. Anchor rows are found by **ID**, depth-first inside the parent screen's subtree, per §2a.

Verified: `Market Page → ETF list → ETF Page` in both markets; Stock Page still nests as before;
structural diff 90/90 with zero unclassified differences. Workbook byte-identical.

*Source: Ahmed Alghamdi · 2026-08-25*

---

## 2d. Archive display rule (2026-08-25, v2.0.2)

**A row tagged `archived:<version>` is retired with lineage, not deleted, and is hidden from the
tree by default.** A `Show Archived` toggle in the atlas brings the archived set back for audit.

The rule is generic and tag-driven — no ID appears in the renderer. An archived row keeps its
status, its history and its `duplicate-of:` / `merged-into:` lineage; it simply stops competing
for attention in the backlog.

| Tag | Meaning |
|---|---|
| `archived:<version>` | hidden by default; the version records when it was retired |
| `archive-note:<text>` | why it was retired, in prose |
| `merged-into:<id>` / `merged-from:<id>` | lineage written on **both** rows so the merge is legible from either end |

### v2.0.2 — backlog final resolution

**Archived (4 rows, all US):**

| Row | Lineage |
|---|---|
| US-005 Options | `duplicate-of:US-116` — superseded by placed canonical row, app-verified Live 2026-08-25 |
| US-008 Government Trades | `duplicate-of:US-119` — same |
| US-031 Insider Trades | `duplicate-of:US-123` — same |
| US-131 Price Chart Corporate Actions Adjustment | `merged-into:US-175`, with `merged-from:US-131` written back on US-175 |

**Nothing deleted.** 532 rows before and after; 5 rows modified; **0 statuses changed**.

**SAU-139 does not exist** — the Saudi twin of Price Chart Corporate Actions Adjustment was
removed in v1.4.1, so that half of the merge was a no-op.

### v2.0.3 — final placements · Backlog EMPTY, both markets

| Row | Placement | Status |
|---|---|---|
| US-106 Liquidity Indicators | child of **Indices change** (US-177), Market Page #9 | **Live** — unchanged |
| US-107 Intl Indices Historical Data | child of **Market indices chart** (US-151), Market Page #2 | Planned — unchanged |

**US-only. No Saudi twins created** — the v1.4.1 deliberate break is preserved, and both rows
keep their `deliberate-break:v1.4.1` tag alongside `placed:v2.0.3`.

**The Backlog fan is now EMPTY in both markets.** Four archived rows remain behind the
`Show Archived` toggle (§2d): US-005, US-008, US-031, US-131.

Three points were referred back before applying, because the brief as written conflicted with
the record:

1. **"Both markets"** would have created Saudi rows deliberately removed in v1.4.1 — recorded
   three times in this document. Ruled US-only.
2. **XJ-012**, offered as the comparison point, **does not exist** — removed in v1.4.1.
3. **"Status Planned"** would have demoted US-106, which is Live on an 11 Aug `verified_live`
   confirmation. Ruled: keep Live.

The Saudi chart → historical-data precedent (`Stock chart → Historical Data (Corporate
Action)`) sits on **Stock Page**; this placement is on **Market Page** under a different chart.
Analogous shape, not the same precedent — placed on Ahmed's explicit ruling.

*Source: Ahmed Alghamdi · 2026-08-25*

---

## 2e. Structural identity certification — `scripts/check-parity.sh`

**One command, ~1 second, exit 0 = identical.** Certifies that the Saudi and US Market journeys
are the same structure.

```
projects/features-map/dashboard/scripts/check-parity.sh
```

**This runs inside every future §0 bundle** as evidence item (b). It supersedes the ad-hoc
tree-diff snippet each campaign used to re-write.

### What it checks

Counterparts are keyed by **(screen, parent-chain, name)** — deliberately *not* by
`display_order`. A us-only row legitimately shifts positions on one side, so a position-keyed
match reports every subsequent row as missing. **That exact bug produced a false 88-difference
failure on the first certification run**; order is instead verified separately, over the shared
set only.

Per shared node it compares **name · parent · depth · display_order · is_container · row_type**.

### Six gates

| Gate | Meaning |
|---|---|
| unclassified differences = 0 | every difference has a recorded reason |
| us-only set matches the expected list | no silent additions |
| deliberate-break class empty | all historic breaks resolved |
| backlog empty both sides | nothing unplaced |
| structural attributes identical | shape, nesting and row kinds match |
| shared-set order identical | display order agrees where both markets have the row |

*Source: Ahmed Alghamdi · 2026-08-25*

---

## 2f. Product Dimensions — and the promote-before-strip rule (2026-08-25)

### The dimensions the product genuinely has

The model must represent these. A row's identity is a **feature × its position on these axes** —
not a name.

| Dimension | Values | Modelled as | State |
|---|---|---|---|
| **Market** | Saudi · US | `journey` column | ✅ modelled |
| **Custodian** (US only) | GTN · IBKR | `backends` column (T), format `IBKR=Live;GTN=Gap` | ⚠️ **column exists, populated on 0 rows** |
| **Session** (US only) | pre · post · trading | rows under the parent feature | ✅ modelled — v1.9.4 |

*Ahmed extends this list — the brief's `[Ahmed extends]` placeholder is still open.*

**Candidates surfaced by the 2026-08-25 inventory, not yet confirmed as dimensions:**
**vendor/provider** (Nomu, Mashura, Benzinga, Trading Central, Drahim) · **account type**
(Institutional, Corporate, Minor).

### STANDING RULE — a suffix is DATA until proven noise

**Before any rename, merge or dedup campaign, check whether the repeated qualifier encodes a
dimension from this section, or a candidate for one. If it does, promote it to modelled
structure FIRST and strip second.**

**Stripping a dimension-carrying suffix without promoting it is a defect** — it destroys the
only record of the axis and silently merges rows that are not the same thing.

Test: *if two rows differ only by this qualifier, do they have different statuses?* If yes, the
qualifier is load-bearing. `Fractional Shares (IBKR)` is Live and `Fractional Shares (GTN)` is
Gap — merging them on the grounds that the names "duplicate" would have deleted a real gap.

### Origin — the five-step chain

1. **v1.7** stripped `(US)` suffixes across the contracted Market screens as canonical
   vocabulary, on the reasoning that journey + ID already distinguish rows. Correct there —
   market *is* modelled, so the suffix was genuinely redundant.
2. **A hygiene item was then logged** proposing the same treatment for the 24 remaining
   `(US)`/`(Saudi)` rows — suffix-stripping generalised from a specific case to a policy.
3. **v1.9.4 moved in the opposite direction**: session variants were *promoted* out of
   `content_spec` into rows, because pre/post/trading is a real axis. Two campaigns, opposite
   instincts, no rule to arbitrate.
4. **The custodian inventory** found four `(IBKR)`/`(GTN)` pairs — Fractional Shares,
   Performance Chart, Portfolio P&L View, Trailing Order — **every one Live on IBKR and Gap on
   GTN**. Not four coincidences: one fact, that GTN trails IBKR, stated four times.
5. **The `backends` column already existed** — specified in `xlsx-to-features-json.py` with a
   parser and a consistency validator, documented as *"US Trading runs on two brokerage
   backends… encodes as `IBKR=Live;GTN=Gap`"* — and **populated on zero rows**. The dimension had
   a modelled home built for it and unused, while the map duplicated rows with suffixes instead.

Had step 2's policy been applied to those four pairs, the merge would have looked like tidy
dedup and would have erased the GTN shortfall from the map entirely.

**Open consequence:** the four custodian pairs are still eight rows. Collapsing them onto
`backends` would remove four rows and four false Gap entries from the metrics, and surface the
GTN shortfall as one line. Not done — it needs a ruling, and it is exactly the kind of change
this rule exists to sequence correctly.

*Source: Ahmed Alghamdi · 2026-08-25*

---

## 2g. Custodian branching — US Portfolio (v2.2, 2026-08-26)

**US Portfolio branches by custodian.** One Portfolio View is replaced by two Level4 screens;
All Portfolios View stays as the shared list.

```
US Trading / Portfolio
  ├── All Portfolios View    7 rows — the list showing both portfolios
  ├── GTN Portfolio         21 rows · 12 top-level
  └── IBKR Portfolio        22 rows · 13 top-level     (Open IBKR Portfolio lives here only)
```

31 → **50 rows**, 19 created, 0 deleted. The `(IBKR)`/`(GTN)` suffixes are gone from Portfolio:
the **branch carries the custodian**, so `Portfolio P&L View` is Live in IBKR and Gap in GTN as
two placements of one feature name.

### Mixed model, deliberately

Custodian is expressed **two ways**, because the rows sit in different places:

| Where | Mechanism |
|---|---|
| Inside Portfolio | **branch** — GTN / IBKR screens |
| Outside Portfolio (Market Page, Orders Page) | **`backends` column**, sparse |

`Fractional Shares` and `Trailing Order` are on Market Page and Orders Page, which do not branch,
so they collapsed onto `backends=IBKR=Live;GTN=Gap` and their GTN twins were archived with
`merged-into:` lineage.

**Sparse population rule:** `backends` is set **only where custodians differ**. Empty means the
capability applies equally to both. A fully populated column would bury the signal in
boilerplate.

### Instances never become tree rows

**Accounts, portfolios and customers are instances, not structure.** Dimensions live in columns
and specs. The two branches are not "the customer's two portfolios" — they are the two
*capability sets*; a customer may hold many portfolios on either custodian.

### `custodian-branch` classification

`check-parity` gained a scope flag (`check-parity.sh <area>`) and a `custodian-branch` class, so
branch-only rows are classified rather than reported as unexplained. `EXPECTED_US_ONLY` dropped
from 4 to 3 — the `(GTN)` row is archived and the `(IBKR)` row lost its suffix.

### ⚠ US Portfolio is NOT identity-certified — by design

Saudi 59 rows against US 50, **0 shared**: the journeys are now deliberately different shapes.
Saudi has one portfolio view, US has two custodian branches, so a node-for-node identity check
can never pass. **Portfolio identity certification is therefore not applicable**, and the
COVERAGE line in every §0 bundle must say so rather than leaving it looking untested.

### v2.21 — the Saudi sweep closes, and the map has no unknowns left

Ahmed ruled all 44 unwalked Saudi Market rows: `SAU-150 Portfolio Dividends` **Live**, the other
**43 Planned**. 865 rows, none created or deleted, 44 modified. Saudi Market 197 · Live 111 ·
Planned 61 · Gap 25.

**Every row in the map now has a determined status. `Unverified` is empty for the first time —
865 rows, zero unknowns.** Totals: Live 524 · Planned 129 · Gap 212.

**The eighteen parity Gaps are gone, and gone the right way.** They read Gap only because
evidencing their US twins fired Rule 4.5; nothing had been observed in the Saudi app. A
`manual_status` Planned (**Rule 0.5**) now overrides the parity inference on each of them. Rule
0.5 outranking Rule 4.5 is the whole point of the ordering: **a human ruling beats an inference
drawn from the other market.** Saudi Gap 65 → 25.

**Planned here means on the roadmap, not shipped**, and it is a much larger claim than the map
carried this morning — 61 of Saudi Market's 197 rows. The Stock Page *Financial* subtree is now
almost entirely Planned: statements, earnings, revenue, actions and their leaves. This is the
opposite of the US result, where the same screen came back Live. **The two markets genuinely
differ here, and the map now says so on a ruling rather than on silence.**

**`SAU-214 Trades` would not take the ruling, and was left alone deliberately.** It is a
container over `SAU-069 Insider Trades` and `SAU-070 Government Trades`, both Gap, so container
roll-up (**Rule 0**) sets it Gap before Rule 0.5 is consulted. The override was **removed rather
than left in place**, on the same principle as `US-175` in v2.20.1: an evidence store must never
assert what the map denies. Ruling a container is really a ruling about its children — if Trades
is Planned, Insider Trades and Government Trades need to be Planned, and they were not named.

The deck at `projects/features-map/reports/features-map-2026-08-31.pptx` was built against
v2.19.3 and is now stale on every count. Its builder reads the data live, so re-running it
restates it.

*Source: Ahmed Alghamdi · 2026-08-31 · features-master.xlsx · verified_live.json ·
manual_status.json · structure-BASELINE-v2.21*

### v2.20.1 — US-175 corrected to Gap, and Rule 4.5 lets go of its twin

`US-175 Historical Data (Corporate Action)` **Live → Gap**. The v2.20 walk recorded it Live with
the other 25 Financial rows; Ahmed corrected it the same day. Its `verified_live` entry is
**removed**, not left beside a contradicting status, and a `manual_status` Gap written in its
place stating that it supersedes the walk. 865 rows, one row modified. US Trading 272 · Live 150
· Planned 15 · Gap 107 · still zero unverified.

**A batch walk can carry a wrong row, and the fix is to delete the evidence, not to overtype the
status.** Leaving the Live evidence in place while typing Gap would have left the store asserting
something the map denies, and Rule 1 would have fought Rule 0.5 on every rebuild.

**Rule 4.5 released `SAU-218` on its own.** The Saudi twin — also *Historical Data (Corporate
Action)* — was one of the nineteen that flipped Unverified → Gap in v2.20 when the US side gained
evidence. With that evidence gone, it returned to **Unverified**. Saudi Gap 66 → 65,
Unverified 2 → 3.

**This is the v2.20 warning demonstrated in a single row.** Those nineteen Saudi Gaps are not
observations; they are a shadow cast by the US walk, and they move when the US side moves. Any
of them can be released the same way. **A parity Gap is a statement about evidence, not about
the Saudi app**, and it should never be read to a stakeholder as a missing feature.

*Source: Ahmed Alghamdi · 2026-08-31 · features-master.xlsx · verified_live.json ·
manual_status.json · structure-BASELINE-v2.20.1*

### v2.20 — US Trading is fully determined, and Saudi pays for it

Ahmed walked all 33 unwalked US Trading rows. 864 → **865 rows**. US Trading 272 ·
Live 151 · Planned 15 · Gap 106 · **zero unverified — the journey is fully determined for the
first time.**

**26 Financial leaves → Live.** The whole Stock Page *Financial* subtree — annual/quarterly on
Income Statement, Balance Sheet and Cash Flow; period/estimated/actual/surprise on Earnings,
Quarterly, Annual and Revenue; next-report estimation; Actions with Dividends and Split; and
Historical Data on the chart. **The parents were already Live and the children had simply never
been opened** — one screen closed 26 rows.

**Order Types resolved.** `US-046 Iceberg Order`, `US-035 Basket Order` and
`US-136 Quick Trade Ticket` → **Gap** by manual_status (Rule 0.5): they were typed Gap but
derived Unverified, because a typed Gap needs competitor evidence to stand and none existed.

**Bracket Order split by custodian.** `US-037 Bracket Order (OCO)` → **Live** on IBKR, and
`US-315 Bracket Order (OCO) (GTN)` created as **Gap**. This follows the convention already in
this area — `US-045 Trailing Order` Live beside `US-114 Trailing Order (GTN)` Gap — where the
unsuffixed row is the default branch and the GTN variant carries its own row. **A single row
cannot hold two statuses**, and inventing a per-row custodian column for one case would have
been worse than reusing the pattern.

`US-228 Instant Settlement` and both `Portfolio Dividends` rows → **Planned**.

**Nineteen Saudi rows flipped Unverified → Gap as a side effect, and nobody looked at the Saudi
app.** Writing evidence onto the 26 US Financial rows substantiated them, which fired **Rule 4.5
cross-market parity** against their unevidenced Saudi twins: `SAU-212`, `SAU-218`, `SAU-252`,
`SAU-253`, `SAU-254`, `SAU-256`–`SAU-259`, `SAU-261`–`SAU-264`, `SAU-266`–`SAU-271`. Saudi Market
Gap 47 → 66, Unverified 21 → 2.

This was isolated and confirmed, not assumed: replaying the pre-turn workbook with only the new
`manual_status` produced no Saudi change, while the full new state produced all nineteen.

**The rule is behaving as designed and the result is probably wrong.** Rule 4.5 exists to stop a
verified capability in one market silently implying absence in the other. But the Saudi Stock
Page carries the same Financial section, so the likeliest truth is that these nineteen are Live
too — and the map now asserts nineteen Saudi Gaps on the strength of a **US** walk. **Rule 4.5
should be read as "unproven in this market", never as "confirmed missing."** Walking the Saudi
stock page's Financial section is now the single highest-value walk left in the map: two rows
of genuine unknown remain (`SAU-150 Portfolio Dividends`, `SAU-230 Indices stocks`), and
nineteen rows are one screen away from being right.

**`US-245` and `US-144` are both named Portfolio Dividends.** Both were ruled Planned, so both
were kept, but they are a duplicate pair and have been flagged twice now.

*Source: Ahmed Alghamdi · 2026-08-31 · features-master.xlsx · verified_live.json ·
manual_status.json · structure-BASELINE-v2.20*

### v2.19.3 — Support dissolves, ARC Chatbot stays

`XJ-049 ARC Chatbot` loses its **Support** area and hangs straight off Platform. Status unchanged
at **Gap**. 864 rows, nothing created or deleted, one row modified. Platform 71 · Live 49 ·
Planned 13 · Gap 9 · zero unverified. `Support` no longer exists as an area anywhere in the map.

Fourth application of the same rule, after Compliance, Content and Market Data in v2.19:
**an area that groups one row is not grouping.** Platform's journey-level set is now four rows —
TILA, ARC Chatbot, Cross-Product Gain-Loss Chart, Social / Copy Trading.

**One single-row area survives on purpose.** `Sharia List Management` holds only
`XJ-101 View Only Shariah Compliant Stocks (On/Off)`, and Ahmed named it explicitly in the v2.19
two-level ruling. **A named ruling outranks the pattern** — it was not dissolved on consistency,
and should not be without an instruction.

**ARC Chatbot being a Gap now shows at journey level, and that is the point.** Customer support
has no other representation in the map: the Figma *Customer Care* section — message centre, help
centre, tutorials — has no rows at all, and `XJ-008 CRM Case Management` disappeared in an
earlier restructure. The map currently says ARC has no support surface beyond a chatbot that
does not exist.

`views/atlas.html` area order updated — `Support` removed from the Platform list.

*Source: Ahmed Alghamdi · 2026-08-31 · features-master.xlsx · views/atlas.html ·
figma-crosscheck-home-discover-profile-lms.md · structure-BASELINE-v2.19.3*

### v2.19.2 — Cash Management stops rendering its own name twice

Display fix only. **No data change** — 864 rows, no row touched, `features-master.xlsx`
unmodified. `views/atlas.html` §2k extended.

Cash Management was rendering **Cash Management → Cash Management → rows**: 81 of its 82 rows
sit in an area named after the journey, so the area node repeated the journey label. §2k already
existed to kill exactly this hop, but its guard was `one area **and no loose rows**` — and
v2.19.1 gave the journey its first loose row (`XJ-069`), which silently switched the collapse
off. **The duplication is a regression I introduced one version earlier, not old debt.**

§2k now collapses on either of two shapes:

| Shape | Collapses | Why |
|---|---|---|
| One area, no loose rows | yes *(original rule)* | area node adds nothing |
| One area **named after the journey**, loose rows present | yes *(new)* | the discarded label repeats the journey name, so loose rows lose nothing by joining the area's children as siblings |

The name test is what makes the second case safe. Collapsing *any* single area beside loose rows
would flatten a real label — `Crowd Fund → Portfolio` and `IPOs → Subscriptions` both collapse
today only because they have no loose rows, and if either gained one its area name would still
carry information worth keeping. **Only a label that repeats the journey name is free to
discard.**

Verified against every journey: Cash Management is the sole behaviour change. Crowd Fund and
IPOs collapse as before; the eight multi-area journeys are untouched.

*Source: Ahmed Alghamdi · 2026-08-31 · views/atlas.html · structure-BASELINE-v2.19.2*

### v2.19.1 — the last Market Data area dissolves

`XJ-069 Global Last Transaction View` loses its **Market Data** area label and hangs straight off
Cash Management. Status unchanged at **Planned**. 864 rows, nothing created or deleted; one row
modified. Cash Management 82 · Live 61 · Gap 9 · Planned 12 · zero unverified.

**This closes a hole v2.18 opened.** That version moved the row from Platform to Cash Management
carrying its area label with it, which created a one-row *Market Data* area inside a journey that
had never had one — every other Cash Management row sits in the *Cash Management* area. v2.19
dissolved the Platform copy of the same area on the same reasoning and left this one standing
because the ruling named Platform. **Moving a row across journeys must re-home its area, not
import the old journey's vocabulary.**

`Market Data` now appears nowhere in the map as an area.

**Cash Management is the first journey with a row at journey level.** XJ-069 has no area and no
parent, so it renders as a direct child of the journey beside the *Cash Management* area node.
That is the intended shape for a capability that belongs to the journey rather than to any
cluster inside it — the same treatment TILA, Cross-Product Gain-Loss Chart and Social / Copy
Trading now get in Platform.

Its Planned status is still BRD-only (`ARCD-60858`) and has never been walked.

*Source: Ahmed Alghamdi · 2026-08-31 · features-master.xlsx · BRD ARCD-60858 ·
structure-BASELINE-v2.19.1*

### v2.19 — Platform collapses to two levels

Ahmed's ruling of 2026-08-31: *"does not have to be 3 levels, 2 is enough"*, repeated for ten
groups. **All twelve group containers created or promoted in v2.18 are deleted.** 876 → **864
rows**; Platform 83 → **71** (Live 49 · Planned 13 · Gap 9 · zero unverified).

**What the third level actually was.** v2.18 gave every group both an `area` label and a
container row of the same name. The atlas renders *journey → area → screen → rows*, and the
single-screen collapse (§2b) already removed the screen hop — so the chain read
**Platform → Auth → Auth → Set password**. The container carried no information the area did not
already carry. Deleting it leaves **Platform → Auth → Set password**.

**The lesson is worth stating in general terms: a grouping node and an area label are the same
mechanism.** v2.18 used both at once for every group and produced twelve redundant hops in one
version. Grouping in this map is done with `area` where a flat set of siblings is wanted, and
with `sub-of` only where a row genuinely owns others.

Removed: `XJ-071 Auth`, `XJ-043 Language`, `XJ-077 Family`, `XJ-065 Subscription`, `XJ-086 KYC`,
`XJ-016 Session Duration`, `XJ-093 Customization`, `XJ-066 Portfolio Preference`,
`XJ-100 Sharia List Management`, `XJ-020 Alerts`, `XJ-107 Calculators`, `XJ-062 App Widgets`.
Six of those were pre-existing rows promoted one version earlier; the promotion is fully undone
and their content survives as the children.

**`XJ-020` is gone.** *"Alert remove."* It was the row the Yahoo Finance benchmark
(2026-08-30) cited as `XJ-020 Configurable Price Alerts` — the Live platform-level alerting that
the US market has not inherited. **The capability is not gone**; it is now the five category rows
under Alert and Notification. But that benchmark's citation no longer resolves to anything, and
any future reference must point at the category rows instead.

**Alert and Notification is now one cluster.** `XJ-059 Global Notification Center` — one of the
unparented BRD-only rows — was renamed **Global Notification** and pulled in as **Planned**
alongside News, Orders, Cash, Portfolio, Market. `Cash Transfer` → **Cash** and `Portfolios` →
**Portfolio** per the ruling.

**Three single-row areas dissolved.** *Compliance*, *Content* and *Market Data* each held exactly
one live row after earlier moves. `SAU-006 TILA`, `SAU-099 Social / Copy Trading` and
`XJ-068 Cross-Product Gain-Loss Chart` keep their rows and now hang straight off the journey with
no area. **An area that groups one thing is not grouping.**

**Two departures from the letter of the ruling, both deliberate.**

**Family was not named** in the ten, but has the identical shape, so the same collapse was
applied. Leaving it as the only three-level group would have been a worse outcome than the small
inference. Say the word and the container returns.

**Subscription is still three deep in one branch.** Collapsing the container leaves
`XJ-082 US Live Price` owning `XJ-083 Options and Live Prices` and `XJ-084 Market Depth` — a
nesting Ahmed drew himself in the v2.18 ruling. That is a row genuinely owning others, not a
redundant hop, so it was kept. It is the one place Platform still reads three levels deep, and
it was not flattened on inference.

`views/atlas.html` area order updated to the ruling's order; the three dissolved areas removed
from the list.

*Source: Ahmed Alghamdi · 2026-08-31 · features-master.xlsx · verified_live.json ·
views/atlas.html · structure-BASELINE-v2.19*

### v2.18.1 — Minor Trading Restrictions joins Family

`ONB-011 Minor Trading Restrictions` re-parented under `XJ-077 Family`, **status unchanged at
Planned**. 876 rows, no creations, no deletions. Platform 83 · Live 61 · Planned 13 · Gap 9 ·
zero unverified.

**This is the first mixed-status group in Platform.** Family now reads Live with a Planned child:
the minor account itself is live end to end — onboarding, switching in, switching back — while
the guardian's control panel over it is not. `Family` still rolls up **Live** because the roll-up
takes Live if any child has it, which is right here: the group is usable, one capability inside
it is not.

**Planned is still resting on the BRD alone** (`ARCD 45978`), and that has not been tested. A
Figma section named *Minor Trading Restriction* exists in the Profile & Setting file with four
controls — max trade amount, max trades per day, max withdrawal, sector filter — so designs are
done. Under the SBL precedent a BRD-and-Figma row with three Live siblings is a strong candidate
to already be shipped. **Placing it did not verify it**, and the §0 bundle must not read as if
it did.

`ONB-012 Guardian Trading for Minor` and `ONB-027 Minor Account + Guardian Controls` remain in
Onboarding and were not touched. Whether the guardian capability belongs in one journey or two
is still unruled.

*Source: Ahmed Alghamdi · 2026-08-31 · features-master.xlsx · BRD ARCD 45978 ·
structure-BASELINE-v2.18.1*

### v2.18 — Platform gets a structure, and stops being a list

Platform was the last journey with **zero parentage** — 39 rows, 17 area labels, no screen model.
Ahmed's ruling of 2026-08-31 imposes **12 groups**. 831 → **876 rows**; Platform 39 → **83**
(Live 61 · Planned 13 · Gap 9 · zero unverified).

47 rows created, 13 existing rows re-parented, **2 removed** (`XJ-060 Investment Customisation`,
`XJ-027 Personalized Events Calendar`), 1 moved out of the journey.

**Six group nodes are existing rows promoted, not new containers.** `XJ-043 Language Preference`
→ **Language**, `XJ-065 Live Prices Subscription` → **Subscription**, `XJ-016 Session Timeout
Settings` → **Session Duration**, `XJ-020 Configurable Price Alerts` → **Alerts**, plus
`XJ-066 Portfolio Preference` and `XJ-062 App Widgets` kept in place. Promoting beat creating:
a new container next to the old row would have left twins, which is the failure v2.4.x spent
four versions undoing. Every rename is recorded in the row's own tags.

**`XJ-020` deserves a note of its own.** It was cited in the Yahoo Finance benchmark
(2026-08-30) as the Live platform-level alert capability that the US market has not inherited.
It is now named **Alerts** and carries five category children. The benchmark claim still holds —
the row is the same row — but anything citing "XJ-020 Configurable Price Alerts" by name will no
longer match.

**Three overlaps with Onboarding are live and unresolved.** `XJ-073 Face ID` sits under Platform
Auth while `ONB-017 Face ID / Biometric Setup` is Live in Onboarding. `XJ-087 Update KYC` /
`XJ-088 Edit KYC` sit beside `ONB-020 KYC Confirmation Screens` and `ONB-023 Pre-filled KYC`.
**These were created, not moved** — moving an Onboarding row on a Platform ruling would silently
change another journey's counts. Setup-versus-management is a defensible split, but it has not
been ruled on and should not be assumed deliberate.

**Twenty-five Platform rows the ruling did not mention are untouched.** Ahmed named two rows to
remove explicitly, so silence is not removal — **§2i holds: absence from an instruction is not
an instruction.** The untouched set still contains the BRD-only Planned rows (Spin the Wheel,
Auto Zakat, Tadawulaty SSO, Prepaid Commission Bundle, ZATCA Invoice, Bundle Benefits, Global
Notification Center, Subscription Engine, Minor Trading Restrictions, How-To Guides,
Portfolio-to-Mobile Linking) that the SBL precedent says are systematically wrong.

**`ONB-011 Minor Trading Restrictions` is now stranded beside Family.** The Family group has
three named children and it is not one of them, so it sits unparented in the same area. Either
it belongs under Family or it does not, and the ruling did not say.

**`XJ-069 Global Last Transaction View` left the journey** — Platform → **Cash Management**,
Planned, top level, no parent given. Cash Management 81 → 82.

**Name reuse is now heavy inside Platform and is legitimate.** *Orders* appears twice
(`XJ-103` an alert category, `XJ-115` a widget); *Market*, *Portfolio*, *Saudi Market*,
*Watchlist*, *Stock*, *Fund* all repeat across the Alerts, Customization, Portfolio Preference
and App Widgets groups. **§2a: never key on name** — parentage is the only identity.

`XJ-116 Top Movers` and `XJ-117 US News` are Gap by **manual_status (Rule 0.5)**, not by
competitor evidence — Ahmed's ruling is the authority. Every Live row created here carries
`app_walk` evidence dated 2026-08-31 in `verified_live.json`; the two Gap widgets, the Planned
Purification Calculator and the Gap Cross-Product Chart carry none, by design.

**The instruction arrived duplicated verbatim** — the same paste artefact as v2.4.3. Both blocks
were identical, so there was nothing to reconcile.

*Source: Ahmed Alghamdi · 2026-08-31 · features-master.xlsx · verified_live.json ·
manual_status.json · structure-BASELINE-v2.18*

### v2.17.3 — Accounts joins Cards, and CM-009 becomes a real pair

`CM-071 Accounts` created as a **structural container** under `CM-009 Cards and Accounts`,
carrying `CM-072 Add Account`, `CM-073 Delete Account`, `CM-074 Edit Account` — all three
**Live** on the app walk of 2026-08-31, evidence written to `verified_live.json` as `app_walk` /
high confidence. 827 → **831 rows**. Cash Management 81 · Live 61 · Gap 9 · Planned 11 ·
**zero unverified**.

**The single-child redundancy flagged in v2.17.2 is closed.** CM-009 now has exactly the two
children its name promises — Cards and Accounts — and the container reads as designed rather
than as an artefact. This is the case for having made Cards a node in the first place: the
sibling arrived one version later and had somewhere to land.

**The two branches are deliberately asymmetric.** Accounts carries three actions, Cards carries
two — there is no `Edit Card` row. That is **§2i**: an unasked capability is recorded as row
*absence*, not as a Gap. Whether card editing exists in the product has never been put to the
walk, and the map must not imply it was and failed. The same applies to any account capability
beyond add/delete/edit.

*Source: Ahmed Alghamdi · 2026-08-31 · features-master.xlsx · verified_live.json ·
structure-BASELINE-v2.17.3*

### v2.17.2 — the two card actions are grouped under Cards

`CM-070 Cards` created as a **structural container** under `CM-009 Cards and Accounts`, and
`CM-068 Add Card` / `CM-069 Delete Card` re-parented beneath it. Both stay **Live**; CM-070 and
CM-009 both roll up **Live**. 826 → **827 rows**. Cash Management 77 · Live 57 · Gap 9 ·
Planned 11 · **zero unverified**.

**Two things about this shape are worth stating rather than discovering later.**

**CM-009 now has exactly one child.** Everything under Cards and Accounts is the Cards node —
there is no Accounts branch yet. The atlas single-area collapse (§2k) works at *area* level and
does not reach this depth, so the tree renders the full chain *Cards and Accounts → Cards → Add
Card / Delete Card*. That is correct as a container-for-future-siblings — Accounts, and any card
capability beyond add/delete, land next to Cards, not next to the two actions. It reads as
redundant only for as long as CM-009 has one child.

**The name `Cards` is now used twice.** `CM-015 Cards` under Cash In is a *funding method* — the
card you pay with. `CM-070 Cards` under Cards and Accounts is *card management* — the card you
hold. Both Live, both in Cash Management, different parents. **§2a holds: never key on name.**
Anything matching rows by label across this journey will collide on these two, and the collision
is legitimate structure, not a duplicate to clean up.

*Source: Ahmed Alghamdi · 2026-08-31 · features-master.xlsx · structure-BASELINE-v2.17.2*

### v2.17.1 — card management is live

`CM-068 Add Card` and `CM-069 Delete Card` **Gap → Live** on the app walk. `CM-009 Cards and
Accounts` rolls up to **Live** with them.

Cash Management returns to **zero unverified rows**: 76 rows · Live 56 · Gap 9 · Planned 11.

**The roll-up inconsistency logged in v2.17 has resolved itself here, but the rule has not
changed.** CM-009 read `Gap` for one version because the roll-up takes the child's *typed*
status while the children derived `Missing evidence`. Now that both children are typed and
evidenced `Live`, typed and derived agree and the container is right for the right reason. The
underlying mismatch — `build_container_status()` reading the typed cell rather than
`derived_status` — is still there and will resurface on the next container whose children are
typed but unwalked.

**Cash Management is the second journey to be fully determined twice.** It reached zero
unverified at v2.14.4, lost it at v2.17 when two named-but-unwalked rows were added, and regained
it here. That cycle is the normal shape of the work: naming a capability creates an unknown, and
the walk closes it.

### v2.17 — Cards and Accounts gets its contents

`CM-068 Add Card` and `CM-069 Delete Card` created under **Cards and Accounts**, which had been
an empty container since v2.14.6 stripped both its rows. Neither carries evidence, so both
derive **Missing evidence** pending a walk.

Cash Management: **76 rows · Live 53 · Gap 10 · Planned 11 · Missing evidence 2.** The journey
loses its fully-determined status, which is the honest outcome — two named capabilities nobody
has checked.

**A roll-up inconsistency this exposed, recorded not fixed.** `CM-009` moved from **Planned**
(empty-container fallback) to **Gap** — because `build_container_status()` reads the child's
**typed** status, and both children are typed `Gap`. But those children *derive* `Missing
evidence`, because they carry no evidence at all.

So the container asserts `Gap` above two rows the map says it does not know about. The parent is
more confident than its children, which is backwards. Fixing it means having the roll-up read
`derived_status` rather than the typed cell — a change that would ripple through every container
in the map, so it is logged here rather than made in passing.

### v2.16 — the Yahoo benchmark rulings land in the map

The ARC vs Yahoo Finance benchmark surfaced five capabilities where Ahmed's ruling and the map
disagreed. The map was the stale side. Six rows created, one status changed.

| Capability | Map said | Now |
|---|---|---|
| US price alerts | US-182 **Gap** | **Planned** |
| News and earnings alerts | no row | **US-309 Live** |
| Valuation ratios (P/E, PEG) | no row | **US-310 Planned** (under Financial) |
| TradingView chart | no row | **US-311 Live** (under Stock chart) |
| Commodities | no row | **US-312 Live** |
| Currencies | no row | **US-313 Gap** |
| Crypto | no row | **US-314 Gap** — tagged `sharia-governance:RED` |

**Four of these were recorded as "absent from the map" in the benchmark, and three of them
ship.** Commodities is Live. TradingView charting is Live. News and earnings alerts are Live.
The benchmark's own "four asset classes ARC does not cover" finding was wrong on two counts —
written from the map, and the map had no rows to be wrong with.

**The lesson is about what an empty map means.** A capability with no row is not a capability
that does not exist; it is one nobody has asked about. The benchmark stated that caveat
explicitly and it still read as a gap in the summary. Absence of a row should be reported as
*unknown*, never as *absent* — the same distinction drawn for the empty Cash Out container in
v2.14, and it was got wrong here two versions later.

**`US-314 Crypto` carries the RED tag.** Digital assets route through
`compliance-and-sharia-governance` before scoping, not after.

US Trading: **271 rows** · Live 124 · Gap 102 · Planned 12 · Missing evidence 33.

### v2.15 — the cash flow map

Ahmed's flow-by-flow walk, 2026-08-27. **55 rows created**, Cash Management goes 19 → **74**.
Cash In, Cash Out and Transfer now name every source and every destination.

**Cash In (7)** — ARB Linked Account Live · ARB Account **Gap** · Local Bank Transfer Live ·
Apple Pay Live · Cards Live · Mokafaa Live · Samsung Pay Planned.

**Cash Out (15)** — five sources, each to ARB Account and to Local Bank Account:

| From | To ARB | To Local Bank |
|---|---|---|
| ARC Wallet | Live | Live |
| Saudi Portfolio | Live | Live |
| **US GTN Portfolio** | **Gap** | **Gap** |
| US IBKR Portfolio | Live | **Gap** |
| Fund Portfolio | Live | Live |

**Transfer (37)** — five sources against seven destinations. Everything moves except four cells:
**US IBKR ↔ US GTN is Gap in both directions**, and **neither US custodian can reach the Robo
portfolio**.

**Cash Out is no longer empty — it is the second-largest group in the journey.** The v2.14
finding that ARC had no cash-out row at all was a mapping hole, not a product hole: money leaves
in eight of ten ways. The two BRDs still unreferenced (`ARCD-34470`, `ARCD-83428`) describe
enhancements to something that already ships.

**The nine Gaps form two clusters, not nine problems:**

1. **GTN cash-out does not work at all** — both destinations Gap, and the source row with them.
   IBKR can reach ARB but not a local bank. Cash out is custodian-dependent in a way nothing else
   in the map is.
2. **The two US custodians are islands.** They cannot transfer to each other, and neither can
   reach Robo. Every other portfolio pair moves freely.

**`Mokafaa` moved from Yield & Rewards to Cash In** and was renamed from *Mokafaa Points
Redemption* — redeeming points into a portfolio is a funding rail. Yield & Rewards is left with
`Buy Round-Up` alone and now derives Planned; **Cards and Accounts is still empty**.

**Repeated names are load-bearing here.** `To ARB Account` appears five times, `To Saudi
Portfolio` four, `To Robo Portfolio` four — each meaningful only through its parent. This is the
largest name-collision surface in the map and the sharpest reason §2a exists.

### v2.14.6 — three empty groups

`SAU-023 Buying Power Swap` moved under **ARC Wallet**. `CM-004 T+2 Card` and
`XJ-032 Aggregated Cash & Buying Power` deleted.

```
Cash Management   (19)
  ARC Wallet                  Live
    UCM Multi-Currency Wallet   Planned
    Multi Virtual IBANs         Planned
    ARC Debit Card              Planned
    Client Money (Overnight)    Planned
    Buying Power Swap           Planned
  Cash In                     Live      (3)
  Cash Out                    Planned   — EMPTY
  Transfer                    Planned   — EMPTY
  Cards and Accounts          Planned   — EMPTY
  Yield & Rewards             Live      (2)
  Instant Settlement          Planned   (1)
  ZATCA E-Invoices            Planned
```

**Three of the six function groups are now empty.** Cash Out was never populated; Transfer was
emptied by moving its only row to the wallet; Cards and Accounts was emptied by deleting both of
its remaining rows. Each renders as a Planned node with nothing beneath it — and as recorded in
v2.14, an empty container derives Planned by roll-up fallback, which overstates all three. They
should read as *unmapped*, not *roadmap*.

**The six-group structure ruled in v2.14 no longer fits what is in it.** Half the groups are
shells and the wallet holds five of the journey's thirteen Planned rows. Either the empty groups
go, or they are placeholders someone intends to fill.

**Two more BRDs lost their only row.** `ARCD-72218` (All Total Cash Buying Power) and
`ARCD-72391` (T+2 Card) are now referenced by nothing — the same effect as ARCD-22937 in v2.13.1.
Three BRDs have now been orphaned by deletions in this session.

**`XJ-032` was Live with app-walk evidence** — a second shipped capability removed from the map
today, after the three IPO rows. Removals of Live rows are worth tracking separately from
removals of Planned ones: the map is being narrowed to what should be *managed*, not to what
exists.

### v2.14.5 — the wallet gathers its capabilities

Three rows moved under **ARC Wallet**, each from a different group:

| Row | From |
|---|---|
| XJ-034 Multi Virtual IBANs | Cash In |
| CM-002 ARC Debit Card | Cards and Accounts |
| CM-005 Client Money (Overnight Investment) | Yield & Rewards |

```
Cash Management   (21)
  ARC Wallet                  Live
    UCM Multi-Currency Wallet   Planned
    Multi Virtual IBANs         Planned
    ARC Debit Card              Planned
    Client Money (Overnight)    Planned
  Cash In                     Live      (3)
  Cash Out                    Planned   — empty
  Transfer                    Planned   (1)
  Cards and Accounts          Live      (2)
  Yield & Rewards             Live      (2)
  Instant Settlement          Planned   (1)
  ZATCA E-Invoices            Planned
```

**The wallet is now the roadmap and the groups are the shipped product.** All four rows under
ARC Wallet are Planned beneath a Live parent; every other group's Live rows stayed where they
were. Cash Management reads as: the wallet exists, and everything it is meant to become —
currencies, IBANs, a card, overnight yield — is still ahead.

**Three groups were drained by one move each**, which changes what they mean:

- **Cards and Accounts** is now T+2 Card and Aggregated Cash & Buying Power. With the debit card
  gone it is barely a card group.
- **Yield & Rewards** is Mokafaa Points and Buy Round-Up — both rewards, no yield. Client Money
  was the only yield row.
- **Cash In** loses its IBAN routing but keeps its three funding rails.

Whether those three groups still earn their names is worth a look; **Cash Out remains empty**.

### v2.14.4 — ARC Wallet is live

`CM-012 ARC Wallet` Gap → **Live**. Cash Management now has **zero unverified rows**:
21 rows · Live 8 · Planned 13 · Gap 0.

**The wallet ships and everything hanging off it is roadmap.** UCM Multi-Currency Wallet is
Planned beneath a Live parent — the wallet exists, multi-currency does not yet. Same shape across
the journey: Cash In is Live through ARB transfer and Apple Pay, with Samsung Pay and Multi
Virtual IBANs Planned behind them.

**Cash Management still has no Gaps** — and that remains a statement about *looking*, not about
the product. 13 of 21 rows are Planned, nine of them on BRD-only evidence, the profile that
proved wrong four times in SBL. Nothing here has been walked except the eight Live rows.

**Map-wide, only two journeys carry unverified rows:** Saudi Market 21, US Trading 33. Eight of
ten journeys are fully determined.

### v2.14.3 — UCM is a capability of ARC Wallet

`XJ-033 UCM Multi-Currency Wallet` moved out of **Cards and Accounts** to sit under
**ARC Wallet**. The two-wallet ambiguity raised in v2.14.1 and v2.14.2 is closed: there is one
wallet, and multi-currency is something it does.

```
Cash Management   (21)
  ARC Wallet                  Missing evidence
    UCM Multi-Currency Wallet   Planned
  Cash In                     Live      (4)
  Cash Out                    Planned   — empty
  Transfer                    Planned   (1)
  Cards and Accounts          Live      (3)
  Yield & Rewards             Live      (3)
  Instant Settlement          Planned   (1)
  ZATCA E-Invoices            Planned
```

**Cards and Accounts is now cards and one balance row** — ARC Debit Card, T+2 Card and Aggregated
Cash & Buying Power. With both wallets gone from it the group is closer to its name, though
`Aggregated Cash & Buying Power` is a *view* across accounts rather than an account, and may
belong under ARC Wallet too.

**The parent is less determined than its child.** ARC Wallet derives Missing evidence while UCM
below it is Planned on a BRD. Nothing is wrong — a row nobody has walked can legitimately parent
one that is documented — but it means the wallet's own status is the least-known thing in a
journey now organised around it.

### v2.14.2 — ARC Wallet sits under Cash Management

`CM-012 ARC Wallet` moved out of **Cards and Accounts** to top level, first position. It is a
peer of the six function groups, not an item inside one.

```
Cash Management   (21)
  ARC Wallet                Missing evidence
  Cash In                   Live      (4)
  Cash Out                  Planned   — empty
  Transfer                  Planned   (1)
  Cards and Accounts        Live      (4)
  Yield & Rewards           Live      (3)
  Instant Settlement        Planned   (1)
  ZATCA E-Invoices          Planned
```

Every Cash Management row shifted +1 so the wallet leads. Position one was a judgment call, not a
ruling: the wallet is the thing money moves *into*, out of and through, so the groups read as
what you can do with it.

**The two-wallet question is unresolved and now more visible.** `XJ-033 UCM Multi-Currency Wallet`
still sits inside Cards and Accounts while ARC Wallet sits above it. If UCM is a capability *of*
ARC Wallet it should be its child; if they are separate products, the naming needs to say so.

### v2.14.1 — ARC Wallet added

`CM-012 ARC Wallet` created under **Cards and Accounts**, carrying no evidence and deriving
**Missing evidence** — the only undetermined row in the journey.

**Two placement calls, both flagged rather than assumed:**

1. **It went under Cards and Accounts**, beside UCM Multi-Currency Wallet, ARC Debit Card, T+2
   Card and Aggregated Cash. That is where wallet-and-account rows already live. It could equally
   deserve its own group — a wallet that funds, holds and pays is arguably the spine of the
   journey rather than one item in it.
2. **It sits alongside `XJ-033 UCM Multi-Currency Wallet`**, and the map now holds two wallet
   rows. Either ARC Wallet is the product and UCM is its multi-currency capability — in which
   case UCM should be its child — or they are separate things. Not resolved here.

No status was invented: Ahmed named the row, not its state.

### v2.14 — Cash Management grouped by function

Ahmed's six groups, 2026-08-27. Six containers created (CM-006…CM-011); all 14 existing rows
placed. **The Cash Management backlog is empty.**

```
Cash In              Cash-In from ARB Live · Apple Pay Live · Samsung Pay · Multi Virtual IBANs
Cash Out             — EMPTY —
Transfer             Buying Power Swap
Cards and Accounts   ARC Debit Card · T+2 Card · UCM Multi-Currency Wallet · Aggregated Cash Live
Yield & Rewards      Mokafaa Points Live · Buy Round-Up · Client Money (Overnight)
Instant Settlement   Instant Settlement
ZATCA E-Invoices     (top level — fits none of the six)
```

**`Cash Out` is an empty container, and that is the finding.** ARC funds three ways in and the
map has no row for getting money out. Two BRDs on disk describe it — `ARCD-34470` (Cash out from
ARC to external) and `ARCD-83428` (Cash-out Enhancements) — and neither is referenced by any row
in the map. The empty group makes the hole visible instead of leaving it as an absence nobody
notices.

**Caveat on that node:** an empty container derives `Planned` by the roll-up fallback, which
overstates it — nothing is planned, nothing is even recorded. It should be read as "unmapped",
not "roadmap", until the two BRDs are turned into rows.

**`XJ-030 ZATCA E-Invoices` sits top-level**, outside all six groups — it is a compliance
artefact rather than a cash function. Left visible rather than forced into a group it does not
belong to.

**The risk this journey carries:** 13 of 20 rows are `Planned`, and nine of those rest on
**BRD-only evidence** — the exact profile that proved wrong four times running in SBL (v2.9,
v2.9.2), where every BRD-only Planned row turned out to be shipping. Cash Management is now the
largest remaining pool of that risk in the map, and **nothing here has been walked**: the journey
has zero Gaps, not because nothing is missing but because nobody has looked.

<!-- RECONSTRUCTION NOTE ---------------------------------------------------
The sections from v2.3.1 to v2.13.2 below were reconstructed on 2026-08-30.
They were missing because the edit scripts that wrote them used a silent
string replace against an anchor that did not match; the scripts reported
success without verifying, so 45 versions locked with a correct workbook,
snapshot and commit but no baseline narrative. The text below comes from the
commit messages written at lock time, not from later recollection. Every
version's workbook, snapshot, evidence stores and integrity check were
verified independently at the time and are unaffected.
Since v2.14 every baseline write is re-read and asserted before commit.
------------------------------------------------------------------------- -->

### v2.13.2 — IPOs fully determined

IPO-006 IPO Details & Status (Nomu) Gap -> Live. That was the last undetermined row: IPOs is 9 rows, Live 6, Gap 3, Missing evidence 0.

The journey reduces to one sentence - individuals can subscribe on both Saudi markets, institutions on neither, and the US not at all. Both markets are otherwise identical: details and status Live, individual subscription Live, institutional subscription Gap.

IPOs joins Mutual Funds, Robo Advisory and LMS/SBL as journeys with zero unverified rows. Four of ten are now fully determined.

758 rows unchanged, 1 modified.

*Reconstructed 2026-08-30 from commit `0222468`, written at lock time.*

### v2.13.1 — remove three IPO rows

IPO-011 Apply for Nomu, IPO-005 Qualified Client Verification and IPO-008 IPO Popup Banner deleted - all three Live, all three leaves, all three with their verified_live entries removed.

A BRD lost its only row: ARCD-22937 (Restricted Fund for Qualified Customer) was referenced solely by IPO-005 and is now referenced by nothing. That is a consequence of the delete rather than an error - the capability left the map, so its requirement document has no home. Recorded because BRD coverage was one of the reasons IPOs looked well-sourced, and the count just fell.

All three were Live: capabilities that ship, deliberately removed. The map now describes IPO subscription by market and nothing else. IPO-011 had been created two versions earlier in the same session, a reminder that a structure ruling and a scope ruling are different decisions and can reverse each other quickly.

IPOs: 9 rows, Live 5, Gap 3, Missing evidence 1.

761 -> 758 rows.

*Reconstructed 2026-08-30 from commit `ee6efab`, written at lock time.*

### v2.13 — group IPOs by market

Main Market and Nomu Market containers over per-market rows, plus US IPO standalone. 5 rows created, 7 modified.

Institutional subscription is a Gap in both Saudi markets: individuals can subscribe on Main Market and Nomu, institutions on neither. SAU-019 was demoted Planned -> Gap in the process; it had been the journey's only Planned row, reading as roadmap.

Main Market and Nomu Market are containers, not typed rows. They are structural groupings - a market classification, not a surface - so status derives from children and no verdict was invented. Both roll up to Live. This is the opposite call from the Fund Page sections, which were ruled Live directly because a tab is something the investor sees; a market grouping is not.

Names now repeat across groups by design - IPO Details & Status, Individuals Subscription and Institutions Subscription each appear twice, disambiguated only by parent.

The ID sequence is whole again: IPO-004 and IPO-006, the two holes noted in v2.11, were reused, so IPOs runs IPO-001..IPO-011 with no gaps.

Two rows were not in the structure and were left top-level rather than deleted: IPO-005 Qualified Client Verification and IPO-008 IPO Popup Banner, both Live. IPO-006 carries no verdict and is the journey's only undetermined row.

756 -> 761 rows.

*Reconstructed 2026-08-30 from commit `4595445`, written at lock time.*

### v2.12 — single-area collapse

The mirror of the single-screen rule, one level up: a journey with exactly one area and no un-areaed features drops the area node, and its rows hang straight off the journey.

Renderer change only. No workbook row was touched - area and screen still hold Subscriptions in the data, and the names survive as areaLabel / screenLabel on the node for tooltips. Nothing about the contract, the Level columns or any count changes.

The rule is generic, not an IPO special case. Three journeys collapse under it today - IPOs (Subscriptions), Cash Management, Crowd Fund (Portfolio) - and any future single-area journey will too. The other seven journeys have two or more areas and are untouched.

Why both collapses exist: a node earns its place by distinguishing its siblings. With one screen the screen node distinguishes nothing from the area; with one area the area node distinguishes nothing from the journey. Both are hops, and the tree should show structure that exists rather than structure the schema permits.

Workbook md5 unchanged from v2.11.

*Reconstructed 2026-08-30 from commit `e7e5172`, written at lock time.*

### v2.11 — IPOs is one category

All seven IPO rows placed on a single Subscriptions category. The IPOs backlog is empty and the single-screen collapse fires, so IPOs renders as one node with seven rows and no sub-level - the third journey to take this shape after SBL and LMS.

The backlog here was inverted from every other journey. Elsewhere unplaced rows were the unbuilt ones; in IPOs the five Live rows sat in backlog while the single placed row was Planned on a screen called IPO Details - with IPO-002 IPO Details & Status, the row that is that screen, unplaced beside it. Placement had drifted entirely out of step with reality.

IPO-008 IPO Popup Banner changed area, not just screen: it was the journey's only Market-area row, an awareness surface rather than a subscription. Folding it into Subscriptions keeps area and screen in agreement, which the map now requires map-wide. The semantic cost is recorded - a popup announcing an IPO is not a subscription capability, and if IPOs earns a second category that row is the one that leaves.

Two IPO BRDs still have no row (IPO Enhancements Ver. 1.1 and Ver. 1.8, neither carrying an ARCD number), and the IPO- ID sequence has holes at IPO-004 and IPO-006 with no record of their removal.

756 rows unchanged, 7 modified.

*Reconstructed 2026-08-30 from commit `4f7363a`, written at lock time.*

### v2.10 — group LMS by lending type

LMS now mirrors SBL's shape: one category, three lending types, each with its capabilities beneath it. The two screens (Margin Activation Process, Margin Account Home) and the backlog are gone; everything sits on a single LMS screen so the single-screen collapse fires.

Saudi Margin Lending (Live) parents Renewal, Early Payment, Phase 2 and Auto Approval. Two new parents with native LMS- IDs: LMS-008 Mutual Fund Lending over MF-010, LMS-009 US Lending over US-092.

SAU-011 Phase 2 (Commodities) demoted Live -> Planned; it carried an app-walk verified_live entry that a manual_status determination now overrides. Every other correction in this journey went the other way.

US-092 US Margin Lending promoted Gap -> Planned: US lending is on the roadmap, not absent.

The journey's existing rows are prefixed SAU-, US- and MF- because they were created inside other journeys; the type parents are the first rows created as LMS. The mismatch on inherited rows is cosmetic and left as is, since renaming IDs breaks every reference.

LMS/SBL: 13 rows, Live 8, Planned 5, Gap 0, backlog empty - the only journey in the map with no Gaps at all.

754 -> 756 rows.

*Reconstructed 2026-08-30 from commit `5f37b30`, written at lock time.*

### v2.9.2 — US Short Selling is live

US-041 Short Selling (US) Gap -> Live. The contradicting manual_status Gap determination was removed so the promotion holds.

SBL is now entirely Live - all four rows. Short selling works in both markets.

All four SBL rows were wrong yesterday: three read Planned on BRD evidence, one read Gap on a Head-of-DX determination, and every one of them ships. The whole securities-borrowing programme was being reported as unbuilt. Two different failure modes produced the same wrong answer, which is why the fix is walking rather than tightening any single rule.

LMS/SBL: 11 rows, Live 9, Planned 1, Gap 1. The two remaining are the backlog pair - MF-010 Mutual Fund Margin Lending (Planned, BRD-only, the same profile that just proved wrong four times) and US-092 US Margin Lending (Gap). Given SBL's record MF-010 should be walked before it is trusted, and US-092 is now the only genuine Gap in the journey.

754 rows unchanged, 1 modified.

*Reconstructed 2026-08-30 from commit `616d871`, written at lock time.*

### v2.9.1 — SBL is one category

US-041 Short Selling (US) moved from Order Page to SBL. The SBL area now has exactly one screen, so the single-screen collapse fires and the screen node disappears: SBL renders as one category holding four rows, with no sub-level.

No renderer change was needed. The rule that produces this already existed - an area with one screen drops the screen hop. SBL was nesting only because US-041 sat on a second screen. The fix was a data change, not a display change: if the tree renders an unwanted level, look for the row that forced it before touching the renderer.

Both Short Selling rows now sit side by side (SAU-015 Live, US-041 Gap), so the market divergence is visible in one place rather than split across two screens.

754 rows unchanged, 1 modified.

*Reconstructed 2026-08-30 from commit `bd5ba93`, written at lock time.*

### v2.9 — SBL out of backlog and live

The three unplaced SBL rows are placed on a new SBL screen and all three walked to Live: SAU-015 Short Selling, LMS-006 SBL Program, LMS-007 SBL Digital Acceptance.

Securities borrowing and lending ships. All three were carried as Planned on BRD evidence alone - the strongest case yet of the trap recorded in v2.5.7: a BRD makes a row read Planned, and Planned then reads as 'not built yet'. Three shipped capabilities were being reported as roadmap because nobody had walked them. Any row whose only evidence is a BRD is a candidate for the same error.

Short Selling now diverges by market: SAU-015 Live on the SBL screen, US-041 Gap on the Order Page.

LMS/SBL: 11 rows, Live 8, Planned 1, Gap 2. Two rows remain in backlog - MF-010 Mutual Fund Margin Lending and US-092 US Margin Lending - both LMS-area with no LMS screen to sit on.

Still unrecorded: ARCD-1590 and ARCD-2219 describe capability with no row in the map.

754 rows unchanged, 3 modified.

*Reconstructed 2026-08-30 from commit `4f80d47`, written at lock time.*

### v2.8.2 — remove Liquidate Portfolio from Robo

RBO-085 Liquidate Portfolio deleted. Its two equity modes had already gone in v2.8.1, leaving a Live leaf; the capability itself does not exist for a robo plan - a plan is exited through Withdraw, not liquidated position by position.

RBO-004 Mashura Reports stays as a Gap. The proposal to delete it as a duplicate of RBO-076 Reports was declined; recorded so it is not re-raised. The two coexist, both Gap, on different screens - RBO-004 carrying BRD ARCD-85842 on One Portfolio View, RBO-076 carrying the seven report sub-types on Mashura Portfolio.

Liquidate Portfolio now exists in four journeys and is Live in exactly one: Saudi. US (both custodians) and Mutual Funds are Gap; Robo is absent by design. Same shape as Reports and Portfolio Analysis, except the robo answer is 'not applicable' rather than 'missing' - the managed products are not behind on liquidation, they simply do not work that way.

755 -> 754 rows. Robo 68: Live 37, Gap 26, Planned 5.

*Reconstructed 2026-08-30 from commit `8df0760`, written at lock time.*

### v2.8.1 — walk the Robo portfolio

Verdicts on all 39 mirrored rows: 10 Live, 22 Gap, 7 removed. Mashura Portfolio is 44 rows, Live 21 and Gap 23, zero unverified. Robo Advisory now has no unverified rows at all: 69 rows, Live 38, Gap 26, Planned 5.

Removed as having no robo equivalent: Order List, Order Details, Orders (customization scope), All Stocks, Select Stocks, Transfer Stocks, Daily Brief.

The Reports subtree is Gap in all three products. Saudi has all seven Live; Mutual Funds walked it to Gap in v2.4.3 and Robo does here. That is a platform pattern rather than three findings: reporting exists only for Saudi equity. Portfolio Analysis is likewise Gap in both managed products where Saudi carries it as Planned.

RBO-085 Liquidate Portfolio is Live with both modes removed - the third time the equity liquidation modes have been deleted after a mirror. Any future mirror should exclude All Stocks / Select Stocks up front, alongside Tradable Rights and Rights Issue.

RBO-064 Portfolio P/L View is Gap while Today Gain, Total Gain, Total Cash and Market Value are all Live: the components exist, the combined view does not.

762 -> 755 rows.

*Reconstructed 2026-08-30 from commit `703ba97`, written at lock time.*

### v2.8 — mirror the Saudi Portfolio contract onto the Robo portfolio

The third journey to take the Saudi One Portfolio View contract, after the US branches and Mutual Funds. 39 rows created with the nesting preserved: Portfolio Holdings -> Holding Details -> (Update Avg Cost Price, Auto Dividend Reinvest); Order List -> Order Details; Reports -> 7 types; Liquidate Portfolio -> 2 modes; Customize Holdings View -> 2 scopes; Portfolio Analysis -> 9. Mashura Portfolio goes 12 to 51 rows.

Excluded: Tradable Rights and Rights Issue, the same ruling made for the US branches and for funds. A robo plan holds funds and ETFs, not rights.

Six existing rows matched rather than duplicated: Performance Chart, Market Value, Holdings Table (= Portfolio Holdings), Transactions (= Transaction List), Dividends (= Portfolio Dividends), and Allocation (= Holdings Distribution). The last is lower confidence - Saudi's row is the breakdown of what you hold, Robo's is the target asset allocation of the plan. Matched and flagged.

The mirrored rows derive Missing evidence, not Planned, because they carry no Figma link - unlike the v2.7 import which is why that one derived Planned. The two Robo imports now sit at different confidence levels by rule rather than by choice.

723 -> 762 rows. Robo 76: Live 28, Gap 4, Planned 5, Missing evidence 39.

*Reconstructed 2026-08-30 from commit `237737d`, written at lock time.*

### v2.7.1 — walk Robo against the Figma import

Ahmed's row-by-row verdicts: 28 rows removed, 22 to Live, 3 to Gap, 1 moved. Robo goes 65 to 37 rows: Live 28, Gap 4, Planned 5.

Two whole screens were deleted. Orders Page (5 rows) and Invest Flow (8 of 9) came from Figma frames - order lists, filters, Pay With, Order Preview, commission, VAT, Execution Tracker - and none of them exist. Only RBO-001 Risk Confirmation survives on Invest Flow.

Almost half the import was wrong: 28 of the 54 Figma-sourced rows were removed. That is the cost of reading a design file as a feature list - a Figma frame proves something was drawn, not that it was kept. The import was still worth doing, since it produced 22 confirmed-Live capabilities the map had no rows for, but the correct default for a Figma import is Planned pending a walk and this campaign is the evidence for why.

Re-parenting after deletion: removing RBO-009 and RBO-036 orphaned four rows, and removing RBO-055 left RBO-001 pointing at a deleted parent. All five re-parented to top level; the map now has zero dangling sub-of tags. Recorded as a rule - deleting a row means checking what pointed at it, since the tag is a reference and nothing validates it at write time.

RBO-011 In-line Allocation Editing moved to One Portfolio View, staying Gap, joining Mashura Reports and Goal-Based Portfolio, both demoted Live to Gap.

751 -> 723 rows.

*Reconstructed 2026-08-30 from commit `41f40fe`, written at lock time.*

### v2.7 — rebuild Robo Advisory from Figma

Source: CDO / 'Mashura New Journey', node 12288-27975, read live via the Figma REST API. Twenty screens. The journey goes 11 rows to 65, across seven screens where it had two.

Market Page 8, Plan Details Page 16, Mashura Portfolio 17, Holding Overview 4, Orders Page 5, Invest Flow 9, Transaction Details 3.

Every new row carries the Figma URL and derives Planned by rule, not by assertion: Rule 4 turns a Figma link with no verification evidence into Planned, which is the right claim for a design - drawn, not confirmed shipped. No status was typed by hand and no walk was implied.

Every row is traceable: each carries figma-sourced:v2.7 plus the literal text it came from. Nothing was inferred from a frame name alone.

Eight existing rows were re-homed rather than duplicated - RBO-001 became Risk Confirmation, RBO-008 Investment Strategies, RBO-002 Create Investment, RBO-006 the simulator inside the Overview tab, RBO-011 In-line Allocation Editing under Plan Distribution. Statuses and evidence survive.

Plan Details Page is anchored to the strategy list (nav_anchor RBO-008) - a plan opens from the catalogue, the same list -> detail pattern as Stock Page, ETF Page and Fund Page.

Three old rows have no Figma counterpart and are left on One Portfolio View: RBO-004 Mashura Reports, RBO-005 Goal-Based Portfolio, RBO-007 Robo Calculator. Either the new journey drops them or the export did not cover them; not resolved here.

Robo previously showed 10 of 11 Live and looked like the most complete journey in the map. Against its own design it is 10 Live, 54 Planned, 1 Gap - roughly 15% built. The old number measured how little had been asked of it.

697 -> 751 rows.

*Reconstructed 2026-08-30 from commit `5196dc0`, written at lock time.*

### v2.6 — mirror the Watchlist contract to Mutual Funds

Five rows MF-121..MF-125, all Gap: Watchlist, Watchlist Story, Auto-Watchlist on Buy, Watchlist - Edit/Reorder, Multi Views. Mutual Funds now has a fourth area and matches the Saudi/US Watchlist contract row for row.

The US rows were the donor, not Saudi: Saudi's five are still unplaced in backlog while US's five sit on a Watchlist screen, so mirroring from the placed side carried the screen assignment for free. A mirror inherits its donor's completeness - choose the donor by how well-formed it is, not by which market came first.

Fund watchlisting does not exist at all, five for five, where Saudi and US are identical to each other and both largely Live. That makes it the sharpest single-product divergence in the map: an investor can watch a stock in either market but cannot watch a fund.

Auto-Watchlist on Buy kept its name though for funds the trigger is a subscription; flagged rather than renamed, unlike Transfer Stocks -> Transfer Funds where the object itself differed.

692 -> 697 rows. Mutual Funds 115, Live 78, Gap 33, Planned 4.

*Reconstructed 2026-08-30 from commit `cb91d3f`, written at lock time.*

### v2.5.12 — three rows onto the fund Orders Page

MF-118 Edit Order (Gap), MF-119 Orders History (Live), MF-120 Customize Orders View (Live). The fund Orders Page is now 7 rows: Live 4, Gap 2, Planned 1.

Against the Saudi Orders Page the two order-management basics diverge. Orders History and Customize Orders View match Live-to-Live, but Edit (SAU-145 Live vs MF-118 Gap) and Cancel (SAU-146 Live vs MF-003 Gap) do not.

A fund order can be placed but not changed or cancelled - both mutation actions are Gaps where the equity equivalents are Live. Whether that is a limitation of the fund operating model (orders execute at end-of-day NAV, so there may be no window to edit) or a genuine product gap is a question for the Mutual Funds squad, but the map now states it plainly instead of leaving Cancel filed under a portfolio screen where nobody would compare it.

689 -> 692 rows. Mutual Funds 110, Live 78, Gap 28, Planned 4, Missing evidence 0.

*Reconstructed 2026-08-30 from commit `61a61d5`, written at lock time.*

### v2.5.11 — close the last area/screen mismatch

MF-003 Cancel Subscription Order moves from One Portfolio View to the Orders Page, and Live -> Gap on the app walk. The contradicting verified_live entry was removed.

There are now zero area/screen mismatches in the entire 689-row map. Every row's area agrees with its screen, so no screen renders twice under two branches. The defect existed in exactly two rows - MF-016 (closed in v2.4.9) and MF-003 - both in Mutual Funds, both from the same habit of parking a row on whichever screen it was first seen.

The move changed the answer, not just the address. On the portfolio screen the row read Live; walked on the Orders Page it is a Gap. Cancelling a subscription was recorded as working because nobody had looked for it where it belongs. Placement errors hide status errors.

Mutual Funds: 107 rows, Live 76, Gap 27, Planned 4, Missing evidence 0.

689 rows unchanged, 1 modified.

*Reconstructed 2026-08-30 from commit `924e549`, written at lock time.*

### v2.5.10 — Mutual Funds fully determined

MF-089 Asset Allocation Gap -> Live. That was the last row: every one of the 107 Mutual Funds rows now carries a determination, Missing evidence zero. It is the first journey in the map with no unverified rows.

Market Page 8 (Live 7), Fund Page 34 (Live 30), Orders Page 3 (Live 2), One Portfolio View 48 (Live 25), All Portfolios View 14 (Live 13). Total 107: Live 77, Gap 26, Planned 4.

The Gaps are not spread evenly - 23 of 26 sit on One Portfolio View, and 18 of those are two blocks: the Reports subtree (8) and Portfolio Analysis (10). Every other surface is 88-100% Live. A fund investor can discover, subscribe and see holdings; what they cannot do is pull a report or analyse the portfolio.

Three caveats on completeness: MF-003 Cancel Subscription Order still carries area=Orders on a portfolio screen, the last area/screen mismatch in the map; the Orders Page statuses were inherited before the screen existed rather than observed on it; and Holdings and Documents are Live with no contents enumerated, so the journey is determined, not exhaustively described.

689 rows unchanged, 1 modified.

*Reconstructed 2026-08-30 from commit `2cc2e8d`, written at lock time.*

### v2.5.9 — walk the Fund Page

Eleven rows to Live - six section headers (Overview, Performance, Dividends, Holdings, Zakat, Documents) and five contents (Performance vs Benchmark, Annual Return, Cumulative Return, Fund Strategy, Geographic Split). MF-016 Fund Financial Reports moved under Performance, staying Gap.

The section headers were ruled Live directly rather than made containers, so the is_container proposal is closed as unnecessary: Ahmed walked the sections as real surfaces, which they are - a tab that renders is something the investor sees, not pure scaffolding.

Holdings and Documents are Live with no children. That is coherent: the section exists and renders, its contents have simply not been enumerated. A Live parent with no children means 'we looked and it is there', not 'it is empty'.

Mutual Funds Market: 42 rows, Live 36, Gap 2, Planned 3, Missing evidence 1. The journey overall: 107 rows with one unverified row left - MF-089 Asset Allocation, the only section not ruled.

689 rows unchanged, 12 modified.

*Reconstructed 2026-08-30 from commit `1de3eec`, written at lock time.*

### v2.5.8 — the Asset Allocation section gets its contents

MF-015 Top Fund Holders moved from Fund Page top level into MF-089 Asset Allocation - what a fund holds is allocation, so it belongs inside the section rather than beside it. Planned status unchanged. Added MF-116 Fund Strategy and MF-117 Geographic Split, both Missing evidence pending a walk.

Five of seven sections now filled; Holdings and Documents remain flat. Fund Page is 34 rows.

The Fund Page top level has thinned to four rows - Compare Funds, Fund Financial Reports, Fund Performance Chart and the seven sections. That is the shape a tabbed detail page should have: a chart, a few page-level actions, and sections holding the substance.

687 -> 689 rows. Mutual Funds 107.

*Reconstructed 2026-08-30 from commit `aa26b3c`, written at lock time.*

### v2.5.7 — the Zakat section gets its contents

MF-114 Previous Years Zakat per Unit (Live) and MF-115 Calculate Your Zakat (Planned) under MF-092 Zakat.

Planned needed an authoritative determination to survive: with no BRD and no Figma link, Rule 4 does not fire and the derive chain falls through to Rule 5 -> Unverified, silently discarding the ruling. MF-115 carries a manual_status entry. Recorded as a general trap - typing Planned on a bare row does not produce Planned.

Zakat is now the fourth Zakat surface in the map and the first outside Platform, alongside XJ-001 Zakat Calculator (Live), XJ-051 Auto Zakat and XJ-048 Purification Calculator. Calculate Your Zakat and Zakat Calculator are the same verb on different scopes. Both rows carry sharia-governance:RED; under Decision Rights this routes through compliance-and-sharia-governance before scoping - a per-fund Zakat figure is a Sharia calculation ARC publishes, and two calculators that disagree is a governance failure, not a design inconsistency.

685 -> 687 rows. Mutual Funds 105.

*Reconstructed 2026-08-30 from commit `3ef6e07`, written at lock time.*

### v2.5.6 — the Dividends section gets its contents

Five rows under MF-090 Dividends (MF-109..MF-113), all Live: Frequency, YTD, Past 12 Months, Yield, Avg Distribution.

Three of seven Fund Page sections now filled; four remain flat.

A name now appears twice on the same screen: MF-095 Dividend Yield under Overview and MF-112 Yield under Dividends, both Live. Plausibly the same number in two places - the Overview fact-sheet quoting what the Dividends section details. Recorded rather than merged: it is the shape that produced MF-024/MF-034, but unlike that case the two sit under different sections and may genuinely both render.

680 -> 685 rows. Mutual Funds 103, Live 64, Planned 3, Gap 26, Missing evidence 10.

*Reconstructed 2026-08-30 from commit `52591bf`, written at lock time.*

### v2.5.5 — the Performance section gets its contents

MF-106 Performance vs Benchmark under MF-088 Performance, with MF-107 Annual Return and MF-108 Cumulative Return beneath it - three levels deep, the deepest structure on the Fund Page. All three carry no evidence and derive Missing evidence pending a walk. Typo normalised: 'perforamnce vs Benchmark' -> Performance vs Benchmark.

Two of the seven Fund Page sections now have contents; five remain flat.

The Overview parent problem is now a pattern rather than an instance: MF-087 reads Missing evidence above eleven Live children and MF-088 will read the same once walked. Section rows are structural headers holding no capability of their own, which is what is_container is for - mark them and status derives from children. Left unmarked pending a ruling, but it is one ruling covering all seven sections, not seven.

677 -> 680 rows. Mutual Funds 98.

*Reconstructed 2026-08-30 from commit `3e7dc54`, written at lock time.*

### v2.5.4 — Fund Performance Chart page-level; Compare Funds is a Gap

MF-094 Fund Performance Chart moves out of Overview to sit on the Fund Page itself - it is not a fact-sheet field, it belongs to the page above the sections. Resolves the placement question left open in v2.5.3; Overview keeps its eleven fact-sheet rows.

MF-014 Compare Funds Live -> Gap (app walk, Head of DX). The contradicting verified_live entry was removed so the demotion holds.

This also moots the flag raised in v2.5.1 and repeated in v2.5.3: Compare Funds failed the detail-page test as a cross-fund action on a single-fund page, but it turns out not to exist at all. A row in the wrong place is sometimes a row that was never built.

677 rows unchanged, 2 modified. Mutual Funds 95 rows, Live 59, Planned 3, Gap 26, Missing evidence 7.

*Reconstructed 2026-08-30 from commit `a009f72`, written at lock time.*

### v2.5.3 — the Overview section gets its contents

Twelve rows under MF-087 Overview (MF-094..MF-105), all Live: Fund Performance Chart, Dividend Yield, Price Update Frequency, Fund Category, Risk Level, Min Subscription, Inception Date, Inception Price, Since Inception Change, Redeem, Potential Returns, Fund Currency.

Fund Performance Chart was placed under Overview, not Performance. The instruction line ran into the 'Under MF-087:' heading so both readings were open; Overview was chosen because the other eleven rows are a fact-sheet and a chart at the head of that block is the standard shape. One-row move if wrong.

Two contradictions recorded rather than resolved: MF-087 Overview still derives Missing evidence above twelve Live children because it is not marked is_container, so the roll-up never runs - 'All live' named the contents, not the section. And MF-094 Fund Performance Chart duplicates MF-005 Fund Performance Chart on One Portfolio View by name.

665 -> 677 rows. Mutual Funds 95 rows.

*Reconstructed 2026-08-30 from commit `3dea2e3`, written at lock time.*

### v2.5.2 — add seven Fund Page sections

MF-087..MF-093 on the Mutual Funds Fund Page, positions 4-10: Overview, Performance, Asset Allocation, Dividends, Holdings, Zakat, Documents. All carry no evidence and derive Missing evidence pending a walk - the standing rule since Diff was retired.

Two spellings normalised and flagged rather than assumed: 'Assest allocation' -> Asset Allocation, 'Divided' -> Dividends.

Zakat is the row to notice. No other product surface in the map carries a Zakat section - the platform has XJ-001 Zakat Calculator and XJ-051 Auto Zakat, both journey-level. A per-fund Zakat section is a Sharia governance surface, RED under Decision Rights, and should route through compliance-and-sharia-governance before it is scoped.

658 -> 665 rows. Fund Page now 10 rows; Mutual Funds 83 across five screens.

*Reconstructed 2026-08-30 from commit `6ba2026`, written at lock time.*

### v2.5.1 — Fund Recommender belongs to the market, not to a fund

MF-017 Fund Recommender moves from Fund Page to Market Page (position 8, Planned unchanged). Fund Page renumbers 1-3.

The test this settles: a capability belongs on the detail page only if it acts on the thing the page is about. Being recommended a fund happens before you have one in view, so it sits at market level next to All Fund List. Top Fund Holders and Fund Financial Reports do act on a specific fund and stay.

Compare Funds remains on Fund Page and still fails the same test - comparing funds is a cross-fund action. Left as ruled, flagged a second time rather than moved.

658 rows unchanged, 2 modified.

*Reconstructed 2026-08-30 from commit `63ea540`, written at lock time.*

### v2.5 — the fund market gets a list and a detail page

The Mutual Funds Market area now follows the list -> detail-page pattern the Market journey already uses.

Funds by Asset Class renamed to All Fund List - the old name described a filter, the new one names the surface. Six fund types hang off it as rows: Private, Saving, Dividend, Growth, Smart, Endowment, all Live (MF-082..MF-086 created).

New Fund Page holds Compare Funds, Top Fund Holders, Fund Recommender and Fund Financial Reports. It is registered in screen-nav.json with nav_anchor MF-007, so it renders as a child of the All Fund List row rather than a sibling screen - identical to ETF Page hanging off the ETF list row. A fund detail page is reached through the list and the tree now says so.

MF-026 Saudi SME Equity Fund deleted: it was the journey's last row with no evidence, and a single named fund is an instance, not a capability.

Mutual Funds now has zero unverified rows - 76 rows, Live 48, Planned 3, Gap 25, across five screens, no backlog.

Flagged not re-homed: Compare Funds and Fund Recommender operate across funds rather than on one, so a fund detail page is an odd home for them.

654 -> 658 rows.

*Reconstructed 2026-08-30 from commit `cf2fd5c`, written at lock time.*

### v2.4.9 — a screen belongs to one area

One Portfolio View was rendering under Market as well as Portfolio, because MF-016 Fund Financial Reports carried area=Market while sitting on a portfolio screen. Moved to the Mutual Funds Market Page, position 7, status Gap unchanged.

The rule: area and screen must agree. The tree groups screens under areas, so a single row with a mismatched area makes its whole screen appear a second time under the wrong branch - a structural artefact created by one cell, not by the tree.

Flagged not fixed: MF-003 Cancel Subscription Order carries area=Orders on One Portfolio View, so the same duplicate node still renders under Orders. The instruction named Market; the Orders case awaits a ruling - move it to the Orders Page, or re-area it to Portfolio since cancelling a subscription is reached from the holding.

These two were the only area/screen mismatches in the entire map.

654 rows unchanged, 1 modified.

*Reconstructed 2026-08-30 from commit `fbe4df7`, written at lock time.*

### v2.4.8 — clear the Mutual Funds backlog onto Market and Orders screens

The nine unplaced rows are placed by area: 6 onto a new Market Page (Funds by Asset Class, Private Fund, Compare Funds, Top Fund Holders, Fund Recommender, Saudi SME Equity Fund) and 3 onto a new Orders Page (Subscribe to SAR/USD Fund, USD Fund via SAR Account, Switch Funds Flow).

Two screens created by placement rather than declaration - a screen exists in this map when rows name it. Names follow the cross-journey convention: screens are keyed by (journey, area, screen), so reusing Market Page and Orders Page is safe and carries meaning - the same name in two journeys asserts the same kind of surface.

The Mutual Funds backlog is empty. The journey now has the same Market -> Orders -> Portfolio spine as Saudi and US, at 72 rows across four screens.

What placement does not settle: both new screens are flat, neither has been walked, and MF-026 Saudi SME Equity Fund remains the journey's only row with no evidence.

654 rows unchanged, 9 modified.

*Reconstructed 2026-08-30 from commit `e46e39e`, written at lock time.*

### v2.4.7 — Holding Details identical on both MF portfolio screens

Ahmed: Holding Details should be the same on All Portfolios and on One Portfolio. The All Portfolios copy held only Update Avg Cost Price; added MF-080 Investment Breakdown and MF-081 Auto Dividend Reinvest. Name set and status set now identical on both screens.

The principle: a detail view reached from two places is one contract, not two. Which screen the investor arrived from does not change what a holding can do. The mirror had treated the two Holding Details as independent because it copied each Saudi screen separately - and Saudi has the same asymmetry today (SAU-141 carries Auto Dividend Reinvest, SAU-156 does not), so Saudi is now out of step with its own rule.

Statuses were carried from the One Portfolio View rows already walked rather than re-asserted; the verified_live evidence names that provenance.

652 -> 654 rows; 5 display_order shifts.

*Reconstructed 2026-08-30 from commit `c02cad8`, written at lock time.*

### v2.4.6 — remove MF-051 All Stocks; Liquidate Portfolio becomes a leaf

With MF-052 Select Stocks gone in v2.4.5 and MF-051 All Stocks gone here, Liquidate Portfolio has no children. Both were equity liquidation modes - 'liquidate every holding' and 'liquidate selected holdings' - with no fund equivalent: a fund is redeemed by units or amount, not by picking stocks. MF-050 carries a modes-removed note recording why.

MF-051 held a verified_live entry from the 27 Aug walk, removed with it.

The mirror's cost, stated plainly: copying the Saudi contract wholesale gave Mutual Funds 41 rows in one pass, but three of them (MF-024, MF-051, MF-052) were capabilities that cannot exist for a fund and had to be deleted afterwards - one only after being walked and marked Live. Mirroring is the right way to get shape fast; it imports the source product's assumptions with it, and those surface only on a row-by-row read.

MF One Portfolio View: 49 rows, 25 Live and 24 Gap, zero unverified.

653 -> 652 rows.

*Reconstructed 2026-08-30 from commit `755e905`, written at lock time.*

### v2.4.5 — remove MF-052 Select Stocks

MF-052 Select Stocks - 'liquidate selected holdings rather than the whole portfolio' - deleted. It carried no evidence in either store, so nothing was orphaned.

Mutual Funds One Portfolio View is now fully determined: 50 rows, 26 Live and 24 Gap, zero unverified. Both fund portfolio screens are walked end to end.

Liquidate Portfolio is left with one child and a contradiction: MF-050 is Gap while its only remaining child MF-051 All Stocks is Live. Left as found - whether the parent should still be Gap, and whether All Stocks should keep equity vocabulary in a fund portfolio, are both open.

654 -> 653 rows.

*Reconstructed 2026-08-30 from commit `112182a`, written at lock time.*

### v2.4.4 — remove MF-024 as a duplicate of MF-034

MF-024 Reinvest Dividends (MF) and MF-034 Auto Dividend Reinvest were the same capability under two names, sitting as Live siblings under Holding Details after v2.4.3. MF-024 deleted.

The ceo-assessment tag was carried onto MF-034 first: MF-024 was one of the original twenty MF rows and the only carrier of that signal, so deleting it silently would have dropped a provenance marker nothing else recorded. MF-034 also gains absorbed:MF-024.

Rule recorded: when a duplicate is removed, its tags are the part most easily lost - status and definition live on the survivor by definition, provenance and assessment tags do not. Check the loser's tags first.

655 -> 654 rows.

*Reconstructed 2026-08-30 from commit `87fd2bf`, written at lock time.*

### v2.4.3 — walk the Mutual Funds One Portfolio View

Ahmed's row-by-row walk 2026-08-27: 42 status rulings (18 Live, 24 Gap), two renames, two re-parentings. Screen now 27 Live, 24 Gap, 1 outstanding.

Renames: MF-004 Cancel Fund Portfolio -> Disable Portfolio (adopts the Saudi canon, the capability is shared); MF-053 Transfer Stocks -> Transfer Funds (a fund transfers units, not stocks). Opposite directions on purpose - vocabulary unifies where the capability is the same, not where the product differs.

Re-parented under Holding Details: MF-024 Reinvest Dividends and MF-025 Investment Breakdown are reached from a holding, not the portfolio root.

The whole Reports subtree is Gap (8 rows) where Saudi has all seven Live - the largest coherent gap in the fund portfolio.

Three inconsistencies recorded rather than silently resolved: MF-050 Liquidate Portfolio is Gap while its child MF-051 All Stocks is Live; MF-052 Select Stocks carries no verdict and stays Missing evidence; MF-024 and MF-034 are now Live siblings that may be the same capability under two names.

A duplicated block in the instruction with conflicting values (MF-016 Planned vs Gap, MF-025 Planned vs Live) was read as a paste artefact - the first, fully-annotated block was taken as authoritative.

655 rows unchanged, 44 modified, all MF.

*Reconstructed 2026-08-30 from commit `00f6118`, written at lock time.*

### v2.4.2 — walk the Mutual Funds All Portfolios View

Ahmed 2026-08-27: everything Live except Update Avg Cost Price, which is Gap. 11 rows to Live with app_walk evidence, MF-074 to Gap with a manual_status determination. The screen is now 11 Live, 1 Gap, 0 unverified - the first Mutual Funds surface fully walked.

The aggregate view reaches parity with Saudi on the first pass, one row apart. That divergence is coherent with the product: a mutual fund prices at NAV, so there is no average cost for an investor to correct. Worth checking whether the row should exist for funds at all rather than stand as a permanent Gap - the section 2i 'no need' test applies.

655 rows unchanged, 12 modified, all MF.

*Reconstructed 2026-08-30 from commit `bd399e2`, written at lock time.*

### v2.4.1 — mirror All Portfolios View onto Mutual Funds

The aggregate view completes the Portfolio contract for funds: 12 rows created, name set identical to Saudi, nesting preserved - All Holdings List -> Holding Details -> Update Avg Cost Price, and Orders Across All Portfolios -> Order Details.

Nothing was matched here: Mutual Funds had no All Portfolios View rows at all, so every row is new and derives Missing evidence pending a walk.

Mutual Funds now stands at 73 rows across two portfolio screens (One Portfolio View 52, All Portfolios View 12) with 9 still in backlog.

643 -> 655 rows. No non-MF row touched.

*Reconstructed 2026-08-30 from commit `6b58ddb`, written at lock time.*

### v2.4 — mirror the Saudi Portfolio contract onto Mutual Funds

Mutual Funds had 20 rows, no tree, and 9 in backlog. The Saudi One Portfolio View contract is now its structure: 41 rows created with the nesting preserved - Portfolio Holdings -> Holding Details -> (Update Avg Cost Price, Auto Dividend Reinvest); Order List -> Order Details; Reports -> 7 types; Liquidate Portfolio -> 2 modes; Customize Holdings View -> 2 scopes; Portfolio Analysis -> 9. Screen went 11 rows to 52.

Excluded: Tradable Rights and Rights Issue - equity corporate actions, funds have none. Same ruling as the US branches.

Four existing MF rows matched rather than duplicated: MF-005 Fund Performance Chart, MF-020 Mutual Fund - Holding Overview, MF-006 Dividend History, MF-004 Cancel Fund Portfolio. Matching counterparts before creating is what stops a mirror duplicating rows it should re-parent - MF-032 Holding Details nests under the pre-existing MF-020.

All 41 mirrored rows carry no evidence and derive Missing evidence. Structure may be copied; status may never be. With Diff retired this is the only representation of 'not yet walked' and needs no special label.

602 -> 643 rows. No non-MF row touched.

*Reconstructed 2026-08-30 from commit `18789f1`, written at lock time.*

### v2.3.7 — Saudi Fast Order into Order Types

SAU-114 Fast Order (No Confirmation) moved from top-level on the Saudi Orders Page into Order Types at position 16, mirroring US-024. Eight rows shifted +1; the Saudi Orders Page renumbers cleanly 1-25.

Order Types is now symmetric in shape: Saudi 15 children, US 16. The one remaining difference is US-136 Quick Trade Ticket, which has no Saudi counterpart row at all.

Still out of step: SAU-060 Watchlist - Edit/Reorder and SAU-136 Multi Views remain in the Saudi backlog while US-091 and US-128 are placed on the Watchlist screen.

602 rows unchanged, 9 modified.

*Reconstructed 2026-08-30 from commit `c9b6e8f`, written at lock time.*

### v2.3.6 — Fast Order into Order Types

US-024 Fast Order (No Confirm) moved from top-level on the Orders Page into Order Types at position 17, immediately after Quick Trade Ticket. Eight rows shifted +1; Order Types now holds 16 children and the Orders Page renumbers cleanly 1-26.

Flagged, not fixed: SAU-114 Fast Order (No Confirmation) is still top-level on the Saudi Orders Page. With SAU-060 and SAU-136 still in the Watchlist backlog, three Saudi rows now sit where their US counterparts have been moved. Orders and Watchlist have no parity certification, so nothing enforces this until check-parity is extended past Market.

602 rows unchanged, 9 modified.

*Reconstructed 2026-08-30 from commit `bb08bbf`, written at lock time.*

### v2.3.5 — three US rows out of backlog

Ahmed 2026-08-26: US-136 Quick Trade Ticket into Orders Page / Order Types at position 16; US-128 Multi Views and US-091 Watchlist - Edit/Reorder onto the Watchlist screen.

Quick Trade Ticket was inserted inside Order Types rather than appended after it, so ten following rows shifted +1 (US-149 Order Details 16->17 and its subtree, Order Filter Panel, Fast Order, Customize Orders View). 13 rows modified, 0 created, 0 deleted.

The US Trading backlog now holds no live rows - only the four archived tombstones the renderer already hides.

Flagged, not fixed: the Saudi twins SAU-060 Watchlist - Edit/Reorder and SAU-136 Multi Views are still unplaced. The ruling was US-only, so the Watchlist area is now asymmetric between markets.

*Reconstructed 2026-08-30 from commit `e66f028`, written at lock time.*

### v2.3.4 — retire Diff permanently

Ahmed: 'remove all diff label do not put that label any more.'

Diff is not merely cleared - it is removed from the pipeline, the workbook template and the dashboard, and typing it is now a hard validation error: ERROR: SAU-006: invalid status 'Diff' FAILED - 1 hard error(s). Fix the xlsx and re-run.

Removed from xlsx-to-features-json.py (STATUSES, STATUS_RANK, summary), derive_status.py (the short-circuit rule, _substantiated, summary), build_template.py (author dropdown, help text, conditional format, fill), hygiene_check.py, and atlas.html (filter button, stat box, star glyph, legend swatch, colour map). Zero references remain.

Why it had to go rather than just be emptied: a status must assert something - Live, Planned or Gap. Diff asserted nothing; it meant 'not decided', which is the absence of a determination, and absence already derives Unverified. Carrying both gave the map two ways to say unknown and let one short-circuit real classification - which is exactly what happened in v2.3, where Diff sat in front of Rule 4.5 and suppressed 36 legitimate parity classifications until removed.

Workbook unchanged - code and baseline only.

*Reconstructed 2026-08-30 from commit `89444df`, written at lock time.*

### v2.3.3 — rule the 13 Market gaps cell by cell

Ahmed ruled each observed Market gap by capability x market x screen, using 'no need' for cells where the capability does not belong.

'No need' is recorded as the ABSENCE of a row, never as a status. There is no Not Applicable value and there should not be one: a row that exists asserts the capability belongs there. This keeps KPI denominators honest - a screen is never penalised for lacking something it was never meant to have. Confirmation the reading was right: every cell marked 'no need' was already an absent row, so nothing had to be deleted.

Changes: SAU-273 and US-308 created (Analyst Ratings at market level, Gap on Saudi / Planned on US). US-008 Government Trades and US-031 Insider Trades un-archived and placed on the US Market Page at Planned - they had been archived as 'superseded by the Stock Page row', which conflated capability with placement. Archived rows 6 -> 4.

SAU-202 Trending Stocks Gap -> Live, superseding the 25 Aug walk verdict; the verified_live note names the supersession rather than silently overwriting it.

New parity class product-decision for rows one market carries by choice rather than market structure, gated at exactly 2 IDs. Market now passes 8 of 9 gates, 0 unclassified differences.

600 -> 602 rows.

*Reconstructed 2026-08-30 from commit `933ad80`, written at lock time.*

### v2.3.2 — market structure decides what rows may exist

Tadawul has no extended-hours session, so the eight Saudi Pre/Post rows under Top Gainers, Top Losers, Most Active by Quantity and Most Active by Value were counted as Saudi failures against a capability the market structure forbids. Deleted: SAU-233/234/236/237/239/240/242/243, with their manual_status entries removed.

Deleted rather than archived: archived rows still count in KPI aggregation, so archiving would have kept eight phantom Gaps in every published number. The symmetric precedent is Rights Issue / Tradable Rights, never created on the US side at all.

New parity class market-structure: the eight US twins are tagged and check-parity gains a gate asserting the class holds exactly those IDs. Market now passes 7 of 8 gates, only the recorded US-106/US-107 break remains, 0 unclassified differences.

Ahmed's ruling recorded: the ten Rule 4.5 Gaps in the Saudi Financials and Options Chain subtree stay Gap, carried as a walk backlog.

608 -> 600 rows.

*Reconstructed 2026-08-30 from commit `ed3985b`, written at lock time.*

### v2.3.1 — remove the Diff label map-wide

Ahmed: 'remove all diff label.'

The 36 v2.3 mirrored rows were parked on Diff (star, amber) as a 'preserved, unverified' marker. They are now typed Gap and derive Gap through Rule 4.5 - cross-market parity gap: the sibling market ships this and the row is bare. Diff appears nowhere in the map now, typed or derived.

Diff had been short-circuiting Rule 4.5 before it could run, which is why it read as a fourth state rather than a classification. Rule 4.5 is the honest reading: Saudi ships these Live and the US rows are bare, so an internal gap is what they are - a hypothesis the walk confirms or overturns, not an observation.

The walk list survives the relabel: all 36 carry awaiting-app-walk:v2.3.1 and are flagged parity_gap in the derived JSON, so they remain recoverable as a set even though they no longer render distinctly.

608 rows unchanged, 0 created, 0 deleted, 36 modified. KPI: Live 310, Gap 160, Planned 76, Missing evidence 14, Diff 0.

*Reconstructed 2026-08-30 from commit `210b319`, written at lock time.*

### v2.2.1 — US Portfolio app walk (2026-08-26)

Ahmed walked both branches. **26 rows flipped to Gap — 13 per branch, symmetric**: Official
Letter · Liquidate Holdings · Transfer Holdings · the entire **Portfolio Analysis cluster**
(container + 9 children).

**Six were demotions from Live** — US-052, US-060, US-090 (IBKR) and their GTN twins US-230,
US-235, US-240. Three contradicting `verified_live` entries were removed so the demotions hold.

The effect on maturity is severe and worth stating plainly:

| Branch | Live | Gap | Planned | Missing ev. | |
|---|---:|---:|---:|---:|---|
| All Portfolios View | 7 | 0 | 0 | 0 | 100% Live |
| **IBKR Portfolio** | 5 | 14 | 2 | 1 | **23% Live** |
| **GTN Portfolio** | **0** | 15 | 3 | 3 | **0% Live** |

**The GTN branch has no verified Live capability at all.** Before the walk it inherited the
shared originals' statuses and appeared at parity; observed, it is empty. That is the single
clearest argument that branching was the right call — under a merged model this would have been
invisible.

### v2.3 — Saudi Portfolio contract mirrored onto both US branches

Ahmed's instruction: *"Copy the Saudi portfolio then we will verify the status."* The Saudi
One Portfolio View tree is now the contract for **IBKR Portfolio** and **GTN Portfolio**.

**47 rows created**, symmetric across both branches, carrying the Saudi nesting: Portfolio
Holdings → Holding Details → (Update Avg Cost Price · Auto Dividend Reinvest) · Order List →
Order Details · Reports → 7 report types · Liquidate Portfolio → 2 modes · Customize Holdings
View → 2 scopes. Excluded per ruling: **Tradable Rights** and **Rights Issue** — Tadawul
mechanics with no US equivalent.

**Status of mirrored rows: never inherited.** v2.2 recorded that the GTN branch *inherited* its
statuses and falsely read at parity. Structure may be copied; **status may never be**.

v2.3 first parked the 36 mirrored rows on `Diff` (★ amber). **v2.3.1 removed that label at
Ahmed's instruction** — the rows are now typed `Gap` and derive **Gap via Rule 4.5**
(cross-market parity gap: the sibling market ships it, this row is bare). Diff now appears
nowhere in the map, typed or derived.

`Diff` had been short-circuiting Rule 4.5 before it could run, which is why the label looked
like a fourth state rather than a classification. Rule 4.5 is the honest reading here: Saudi
ships these Live and the US rows are bare, so an internal gap is exactly what they are — a
hypothesis the walk will confirm or overturn, not an observation.

**The walk list survives the relabel.** All 36 carry `awaiting-app-walk:v2.3.1` and are flagged
`parity_gap` in the derived JSON, so they stay recoverable as a set even though they no longer
render distinctly. Anyone reading a Gap on these rows is reading a parity inference, not an
app walk.

**Re-parenting, not duplication.** `Update Avg Cost Price` and `Auto Dividend Reinvest` already
existed flat on each branch. The first pass created depth-2 twins of them; that was caught in
verification and reversed — the four twins were deleted and the **originals re-parented** under
Holding Details, preserving their IDs and evidence. Recorded because the mirror keyed rows by
canonical *path*, and a row at a different depth is a different path — a mirror will duplicate
rather than move unless it matches on name-within-branch first.

**Ahmed's status rulings, app walk 2026-08-26:**

| Capability | IBKR | GTN | |
|---|---|---|---|
| Copy Portfolio Number | Live | Live | |
| Hide Balance | Live | Live | also Live on All Portfolios View (US-307, added) |
| Visual Asset Allocation | Live | Live | GTN promoted from missing-evidence |
| Disable Portfolio | Gap | Gap | |
| Rename Portfolio | Gap | Gap | |
| Share | Gap | Gap | |
| Update Avg Cost Price | Gap | Gap | GTN demoted from Planned |

### §2h — Unified Portfolio vocabulary (v2.3)

One name per capability across both markets. Applied to Saudi and US simultaneously; 34 rows
renamed. The `(US)` suffix is dropped throughout the Portfolio area — the `journey` column and
the branch already carry the market.

| Canonical | Was (Saudi) | Was (US) |
|---|---|---|
| Portfolio P/L View | — | Portfolio P&L View |
| Portfolio Holdings | Holdings List | — |
| Transaction List | Transactions | — |
| Order List | Orders | List of Orders |
| Holding Details | — | View Holdings Details |
| Liquidate Portfolio | — | Liquidate Holdings (US) |
| Portfolio Dividends | Dividends List | — |
| Customize Holdings View | Customizations | — |
| Reports | — | Downloadable Reports (US) |

`Portfolio P/L View` vs `Portfolio P&L View` is the reason to care: a one-character divergence
defeated every name-keyed comparison we ran and inflated the Saudi/US gap report by 15 rows.

**Known name collision, accepted:** `Orders` appears twice per branch — once under Customize
Holdings View (a customization scope) and once under Reports (a report type). This mirrors Saudi
exactly (SAU-172, SAU-182). Safe only because nesting and IDs disambiguate; it is a live example
of why §2a forbids name-keyed lookups.

### v2.2.3 — per-portfolio capabilities move onto the branches

Ahmed's walk found five capabilities modelled **only on All Portfolios View** that in fact live on
each individual portfolio: Portfolio Holdings · Holdings Filter Panel · List of Orders ·
Transaction List · Customize Holdings View. Ten rows added, **five per branch, symmetric**
(US-247…US-256), all Live with app-walk evidence.

Three of them are **Gap at the aggregate level** — US-059 Holdings Filter Panel, US-129
Transaction List, US-134 Customize Holdings View. You can see holdings and orders across all
portfolios; you cannot filter them, see their transactions, or customize the view there.

| Screen | Rows | Live | Gap | Planned | Missing ev. | |
|---|---:|---:|---:|---:|---:|---|
| All Portfolios View | 7 | 4 | 3 | 0 | 0 | 57% Live |
| IBKR Portfolio | 27 | 10 | 15 | 1 | 1 | 37% Live |
| GTN Portfolio | 26 | 5 | 16 | 2 | 3 | **19% Live** |

GTN moves off zero for the first time — these five are the only verified Live capability it has.

**The modelling principle this establishes:** a capability that operates *on one portfolio* belongs
on the portfolio branch, not on the aggregate view, even when the aggregate screen happens to
render something similar. The aggregate view answers "what do I own in total"; the branch answers
"what can I do with this account". Both rows can exist with different statuses — that is not
duplication, it is two different questions. Compare §2f: instances never become rows, but
*capabilities scoped to an instance* do.

**Store-schema note:** `verified_live.json` entries require `verified_date` / `method` /
`evidence` / `confidence`. A `date`/`note` shape parses without error but yields no age, so
`verified_live_age()` returns None and the row silently derives **Unverified** despite being typed
Live. Caught here on all ten new rows. Valid `method` values in use: `manual_confirmation`,
`app_walk`, `appstore_release_notes`.

### v2.2.2 — container roll-up gains a Gap state (rule fix)

Ahmed re-flagged Portfolio Analysis as Gap after v2.2.1 had already written it. The rows were
correct on disk; the **derivation rule was wrong**.

`build_container_status()` was binary — *Live if any child is Live, else Planned*. It had no Gap
outcome, so a container with nothing but Gap children rendered **Planned**: "we're building it",
when the truth was "we have none of it". The rule predates Gap being common on containers.

The roll-up is now three-state, best-first:

| Children | Container |
|---|---|
| any Live | **Live** |
| else any Planned | **Planned** |
| else all Gap | **Gap** |
| none | Planned |

Three containers changed, all genuinely all-Gap: **SAU-214 Trades** (Saudi Stock Page, 2 children),
**US-150** and **US-246 Portfolio Analysis** (both custodian branches, 9 children each).
Distribution: Gap 111 → 114, Planned 80 → 77. **Workbook untouched** — md5 identical to v2.2.1;
this is a derivation change only.

**The lesson, recorded:** a container status that can never be Gap will always understate. Any
roll-up rule with fewer states than the thing it summarises hides the worst case by construction.

**Still not app-verified:** the remaining GTN rows inherited from the originals rather than being
observed. Only the rows above and the four custodian-split rows carry evidence.

*Source: Ahmed Alghamdi · 2026-08-26*

---

## 3. Out of scope / deliberately absent

| Row | Disposition |
|---|---|
| Holdings Filter Panel · Visual Asset Allocation · Portfolio Insights | **Deleted** per spec v3 |
| Instant Settlement (SAU-024) | **Moved** to journey/area Cash Management, no screen, Planned |
| Sectors (SAU-095) · Order Filter Panel (SAU-036) | Detached — in backlog, no screen |

**Zero Saudi Portfolio rows sit outside the two screens** apart from those listed above.

---

## 4. Guardrail — mandatory for every structural edit

Applies to any change to rows, screens, nesting, names or statuses in this area.

1. **Backup** — copy `features-master.xlsx` to a dated `.bak-YYYY-MM-DD-<reason>` first
2. **Apply** the change
3. **Save** the workbook
4. **Re-open fresh** — never verify from the in-memory object that made the change
5. **Re-verify** every count and status rule in sections 1–2 above
6. **Diff** against the backup — list created / deleted / modified rows
7. **Change note** — record the reason on each affected row or in this file

8. **Regenerate** — `xlsx-to-features-json.py` then `derive_status.py`
9. **Verify the JSON** — screen counts match this baseline (currently APV 12 / OPV 47) and
   `dashboard/data/features_derived.json` resolves to the regenerated file
10. **Re-record** `data/master-integrity.json` so the next integrity check has a clean fingerprint

**An edit is not done until step 10.** A workbook change that never reaches the JSON is
invisible to the dashboard and is treated as unfinished work.

**Requests to make a structural edit without this sequence are to be refused.** Report what
would be skipped and offer the guarded version instead.

---

## 4a. Numbers editing workflow (IMPORT)

Edit in Numbers, export to **`staging/features-edit.xlsx`**, then ask for **IMPORT**.
`scripts/import-staging.py` runs it. **The staging file never replaces the master** — only
differing cell values are copied, so Numbers formatting, fonts and column widths are ignored.

**a. VALIDATE** — sheet `Features` exists · header row 2 matches the master exactly · every
data row has an id · status ∈ {Live, Planned, Gap} · Level paths have no skipped levels
(Level6 needs Level4; Level7 needs Level5 **and** Level6; Levels 1–4 must not skip).
Level5 is group-only, so a direct feature legitimately has Level5 empty with Level6 filled.
**Any failure prints the exact problems and STOPS.**

**b. DIFF** — cell-by-cell on `name`, `status`, `Level1`–`Level7`, printed as
`id · column · before -> after`. Values only.

**c. CONFIRM then APPLY** — the default run is read-only and writes nothing. Only after
Ahmed confirms the diff is it re-run with `--apply`, which routes the changes through the
full guardrail above. Ids in staging that the master lacks are **reported, not auto-created**.
Ids in the master absent from staging are **ignored, never deleted**.

**d. FINISH** — regenerate JSON, verify counts, re-record the integrity manifest, delete the
staging file, print the result.

```
cd projects/features-map/dashboard/scripts
python3 import-staging.py            # validate + diff, writes nothing
python3 import-staging.py --apply    # only after Ahmed confirms
```

### Direct-overwrite protection
**A file exported over `features-master.xlsx` is never accepted.** `data/master-integrity.json`
holds the md5, byte size, row count, headers and screen counts recorded at the last guardrail
run. `scripts/check-integrity.py` compares the master against it:

```
python3 check-integrity.py     # exit 0 = clean, 1 = drift
```

On drift — the master was written outside the guardrail (a Numbers export saved over it, a
sync client, a manual save). **Restore from the latest snapshot and alert Ahmed before doing
anything else. Do not regenerate JSON from a drifted master**, or the bad state propagates to
the dashboard. Run this check before starting any edit.

### Known traps
- `ws.cell(r, c, None)` in openpyxl **does not clear a cell** — it returns it. Use
  `ws.cell(r, c).value = None`. This silently no-opped a detach on 2026-08-17.
- **Name collisions are live in this area.** `Orders` names three rows (SAU-120, SAU-172,
  SAU-182); `Holding Details`, `Update Avg Cost Price`, `Market` and `Transfer` also repeat.
  Match on **ID or `sub-of:` parentage — never on name**.
- Base-name matching must strip parenthetical suffixes; 24 rows elsewhere still carry
  `(US)` / `(Saudi)` suffixes that hide twins from exact-name lookups.
- The dashboard must be served via `scripts/serve.py` (no-store headers). A plain
  `python3 -m http.server` lets browsers cache `features_derived.json` and show stale counts.

---

## 4b. Single-writer topology (locked 2026-08-17)

The repo is a **Syncthing** folder (`id="arc"`, `/Users/ahmedalghamdi/Claude/ARC`) shared
between two devices:

| Device ID | Name | Role |
|---|---|---|
| `6BJPRS4` | **Ahmeds-iMac.local — this host** | **WRITER** — folder type `sendonly` |
| `ULOLWJR` | MacBook | consumer — must be set `receiveonly` **on that machine** |

**All workbook writes happen on this host, through the guardrail. Other devices are
read-only consumers.** A second writer is what produced the unattributed 23:01 restructure on
2026-08-16 — a script using openpyxl ran on the MacBook and Syncthing pulled the result here,
bypassing every check.

### Applied here
`folder arc: sendreceive → sendonly` (via the Syncthing REST API). This host no longer accepts
inbound file changes for the folder; remote edits surface as out-of-sync on the sender instead
of silently overwriting the master.

### Must be applied on the MacBook (ULOLWJR) — cannot be pushed remotely
Syncthing folder type is a per-device setting. On that machine:
1. Open the Syncthing GUI (`http://127.0.0.1:8384`)
2. Folder **ARC** → **Edit** → **Advanced** → **Folder Type** → **Receive Only**
3. Save. Any local edits there will show as "Local Additions" and must be reverted, not synced.

Equivalent REST call on that host:
`curl -X PATCH -H "X-API-Key: <key>" -d '{"type":"receiveonly"}' http://127.0.0.1:8384/rest/config/folders/arc`

Until step 3 is done on the MacBook, the lockdown is **one-sided**: this host is protected from
inbound overwrites, but the MacBook can still diverge locally.

### Syncthing process note
Two `syncthing serve` processes are **expected** — PID pairs are the supervisor and its worker
(`ppid` of the second is the first; only the worker binds `:8384` and `:22000`). One launchd
agent, `net.syncthing.arc`, manages them. This is not a duplicate instance and must not be
"fixed" by killing one.

### Inbound-overwrite alarm
`~/Library/LaunchAgents/com.arc.master-integrity.plist` watches `features-master.xlsx`
(`WatchPaths`, 30 s throttle) and runs `scripts/master-integrity-watch.sh`, which calls
`check-integrity.py`:

- clean → appends `OK` to `data/integrity-watch.log`, clears any stale alert
- drift → writes **`data/INTEGRITY-ALERT.txt`** and logs the detail

The watcher is read-only: it never repairs and never regenerates JSON. A guarded edit trips it
briefly until guardrail step 10 re-records the manifest, at which point the alert self-clears
and is archived as `INTEGRITY-ALERT.txt.cleared-<timestamp>`.

**If `INTEGRITY-ALERT.txt` exists at the start of a session, stop and read it before any edit.**

### Conflict-file policy
`*.sync-conflict-*` files are quarantined, never deleted — see
`quarantine/sync-conflicts-2026-08-17/`. 42 were archived on 2026-08-17; none contained work
missing from the locked state.

---

## 4c. One-name policy (2026-08-17)

**Exactly one file in the repo may bear the master's name.**

```
projects/features-map/dashboard/features-master.xlsx
```

Any other file named `features-master.xlsx`, or matching `features-master*.xlsx`, is a
name collision and must be quarantined — not deleted. The risk is not that a duplicate is
wrong, but that a glob, a name-based lookup or a stray script resolves to it instead of the
master and silently operates on stale data.

### Permitted neighbours (no collision)
| Pattern | Why it is safe |
|---|---|
| `features-master.xlsx.bak-<date>-<label>` | 49 guarded backups. Extension is `.bak-*`, not `.xlsx`, so `*.xlsx` globs never match them. |
| `saudi-portfolio-BASELINE-v*.xlsx` | 4 read-only locked snapshots. Distinct name, `chmod 444`. |

### Sweep result — 2026-08-17
11 `.xlsx` files in the repo. One master, 4 baseline snapshots, 5 unrelated workbooks
(segmentation, nationality analysis, the 2026-05-04 per-journey mind-map export, 2 validation
exports — all different sheet structures, no `Features` sheet or no id overlap), and **2
collisions quarantined**:

| File | Rows | Issue |
|---|---|---|
| `projects/features-map/reports/features-master.xlsx` | 296 | **Identical filename** in a second location. May 2026, Schema v1.0, three versions behind. |
| `dashboard/features-master-backup-2026-05-11.xlsx` | 308 | Name begins `features-master` and ends `.xlsx` — matches a `features-master*.xlsx` glob. |

Both in `quarantine/stale-copies/` with provenance. Neither was referenced by any script.

### Enforcement
Re-run the sweep after any bulk file operation, restore, or sync event:

```
find . -name "features-master*.xlsx" -not -path "./.git/*" -not -path "./quarantine/*"
```

**Expected output: exactly one line.** More than one means a duplicate has appeared — quarantine
it before running any pipeline script.

---

## 5. Regeneration after any edit

```
cd projects/features-map/dashboard/scripts
python3 xlsx-to-features-json.py     # workbook -> features.json / benchmarks.json / brds.json
python3 derive_status.py             # -> data/features_derived.json (dashboard source)
python3 hygiene_check.py             # competitor names · unfounded gaps · Live decay
```

---

## 6. Version history

| Version | Date | Change |
|---|---|---|
| v1 | 2026-08-17 | First reconciliation to the approved spec — 9 / 21 top-level |
| v1 amend | 2026-08-17 | Portfolio Analysis attached as top-level 22 with 9 children |
| spec v3 | 2026-08-17 | 3 rows deleted · Instant Settlement moved to Cash Management · Reports and Liquidate normalised to parent + subs · 7 / 21 |
| v1.1 | 2026-08-17 | Share reinstated Live on both screens · Hide Balance merged to SAU-168 · totals corrected to 8/11 and 23/47 · LOCKED |
| v1.2 | 2026-08-17 | Hide Balance reinstated on All Portfolios View (SAU-189, Live, top-level 9) · totals 9/12 and 23/47 · LOCKED |
| v1.3 | 2026-08-17 | Level1–Level7 hierarchy columns added and populated for 59 Saudi Portfolio rows · no structural change, columns only · LOCKED |
| **v1.2.1** | **2026-08-17** | **Liquidate child renamed `All` → `All Stocks` (SAU-176), Level6 updated to match · verified verbatim against approved spec, 0 differences · LOCKED** |
| **v1.5** | **2026-08-17** | **Orders area IA: Orders Page 25 rows/5 top-level. 6 rows relocated (Sukuk + Futures → Market Page, Trade on Chart → Stock Page, Basket + Options → Order Types, Orders History → Order Filter). Market Page 28/17, Stock Page 36/20. 16 renames.** |
| v1.4.1 | 2026-08-17 | **Removed XJ-012, XJ-015, SAU-139 (Planned, off-screen). Saudi Market backlog now empty; US twins retained.** |
| v1.4 | 2026-08-17 | **Market area IA approved; Stock Page confirmed as its own screen, linked from Market Page item 10. Market Page 26 rows/15 top-level, Stock Page 35/19. 29 rows created Planned, 11 renames, 2 area moves.** |
| display | 2026-08-25 | nav_anchor added: a screen can anchor to a feature ROW, rendering as its child (ETF list -> ETF Page). screen-nav.json becomes the screen registry, so a registered screen renders with zero rows. Workbook byte-identical |
| **v1.9.9** | **2026-08-25** | **Options branch: Options renamed Stock options (retires the v1.9.1 vocab deviation); Options details created under Options Chain at L7. Stock Page 70 both markets; KPI count 467.** |
| **v1.9.8** | **2026-08-25** | **Financial revised: direct children Statements, Earnings, Actions; Earnings re-parented up, Actions returned. Level9 removed, max depth L8. 35 nodes/market, KPI count unchanged at 465.** |
| **v1.9.7** | **2026-08-25** | **Financial subtree to L9. Schema v2.0: Level8, Level9, row_type columns. 56 rows created (48 detail, 8 mid-level); Actions re-parented to Earnings. Stock Page 69 both markets. KPI count 457 -> 465 — detail rows excluded from all metrics.** |
| **v1.9.6** | **2026-08-25** | **Sukuk Trading renamed Sukuk list (both markets, statuses unchanged). Sukuk Page registered with nav_anchor, awaits its outline. Two cells changed; counts unchanged.** |
| **v1.9.5** | **2026-08-25** | **ETF View renamed ETF list (both markets, statuses unchanged). ETF Page registered as a nav-nested screen at position 17, pending rows — the renderer derives screens from feature rows, so an empty screen cannot render.** |
| **v1.9.4** | **2026-08-25** | **Session variants as rows: Trading/Pre/Post under Top Gainers, Top Losers, Most Active by Quantity, Most Active by Value. 24 rows created, all Planned. Market Page 45/20 Saudi, 49/24 US. Parents stay typed features, not containers.** |
| **v1.9.3** | **2026-08-25** | **Ruling 12: Market Summary un-retired to Market Page #3 both markets. Market Page 33/20 Saudi, 37/24 US. Saudi Backlog now EMPTY; US retains 6 duplicate/deliberate-break rows.** |
| **v1.9.2** | **2026-08-25** | **Backlog resolution: 11 element rulings applied both markets. Market Page 32/19 Saudi, 36/23 US; Stock Page 41/22 both. Earnings Calendar duplicate deleted; Screener Themes and Historical Data (Corporate Action) renamed. Backlog fan NOT empty — 1 Saudi / 7 US rows remain, all prior recorded decisions.** |
| display | 2026-08-25 | Screen nav nesting (S2c): a screen with a nav_parent renders as a collapsible child node of that parent. Stock Page nests under Market Page in both markets. Config-driven, workbook byte-identical |
| **v1.9.1** | **2026-08-25** | **Patch: Stock change created (Stock Page #1, both markets); Indices change gains Indices page/stocks/options and becomes a container. Market Page 27/31, Stock Page 35. Two spec deviations recorded as accepted.** |
| **v1.9** | **2026-08-25** | **Unified Market Contract (S1h): one contract, both markets, one converge. Market Page 24/16 Saudi + 4 us-only; Stock Page 34/18 both. 12 rows created, 14 absorbed, 12 backlogged, 14 renamed. content_spec column AD added. Structural diff PASS.** |
| **v1.8** | **2026-08-23** | **Trade on Chart split (S1g): SAU-221 / US-176 Drag and Drop Trade on Chart created Gap under the Live parent; Sahm evidence moved to the new rows. Stock Page 36 -> 37 both markets. Raseed added to the Benchmarks sheet.** |
| **v1.7** | **2026-08-18** | **US Market completion (S1f): full Saudi Market/Stock Page contract applied to US. 25 rows created, 19 renames + US-002/US-146 re-resolution, 4 us-only placed. Structural tree diff Saudi vs US = PASS, 0 unclassified differences. US MP 32/21, SP 36/20. Renderer: Backlog grouping node, node IDs exposed.** |
| **v1.6.1** | **2026-08-18** | **Container status rule (§1e): 12 rows flagged `is_container` (col AC). Status derived from children, never typed; written back so sheet and JSON agree. KPIs exclude containers; no marker on containers. 8 of 12 flipped Planned to Live. US Planned 25->19, Saudi 49->43. Schema v1.8.** |
| **v1.6** | **2026-08-18** | **US Trading structure mirrored from Saudi (§1d): Orders Page 25/25, Market Page 17/28, Stock Page 21/36. 6 structural containers created, 6 ad-hoc screens deleted, 13 rows to backlog. No status or name changed. MF/Robo: Level paths + display_order only — Saudi contract does not apply.** |
| display | 2026-08-17 | Single-screen collapse rule (§2b) — areas with exactly one screen render rows straight off the area; the screen name is not visible anywhere, tooltip only. Renderer only, workbook untouched |
| infra | 2026-08-17 | Evidence vocabulary split from status: "Unverified" → "Missing evidence" in all UI; key-by-ID rule recorded |
| infra | 2026-08-17 | Status display principle recorded (§2a): contract status shown, evidence annotates |
| infra | 2026-08-17 | One-name policy added; 2 duplicate workbooks quarantined |
| infra | 2026-08-17 | Single-writer topology locked — this host `sendonly`, MacBook to be set `receiveonly`; 42 conflict files quarantined; integrity watcher installed |
