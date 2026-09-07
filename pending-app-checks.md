# Pending App Checks — ARC App Verification Queue

Open questions that can only be resolved by checking what the ARC app actually does
today. Each item names the features in conflict, the question to answer in-app, and
what the answer resolves.

Confirmed results graduate to `data/verified_live.json` (with `verified_date`,
`method`, `evidence`, `confidence`). This file holds only what is still **unverified**.

*Source: Features Map · 2026-07-22*

---

## Open

### 1. Level 2 Order Book — does ARC's US app show order-book depth today?

**Status:** OPEN — needs in-app verification
**Raised:** 2026-07-22
**Features in conflict:** `SAU-038` ↔ `US-011`

| id | name | journey | hand-typed | derived | competitors |
|---|---|---|---|---|---|
| SAU-038 | Level 2 Order Book | Saudi Market | **Live** | Gap (unconfirmed) ↻ | — |
| US-011 | Level 2 Order Book (US) | US Trading | **Planned** | Gap (unconfirmed) ↻ | Moomoo, IBKR |

**The conflict:** the two markets carry contradicting hand-typed statuses — Saudi says
`Live`, US says `Planned` — yet **both derive to `Gap (unconfirmed)`**. Saudi claims
`Live` with no verified-live record backing it, which is the same false-Live pattern
corrected in commit `39f32a4` for six other Saudi features.

**Question to answer in-app:**
1. Does the ARC **US** app display order-book depth (bid/ask ladder) today? → resolves US-011.
2. Does the ARC **Saudi** app display market depth today? → resolves whether SAU-038's `Live` is a false-Live claim.

**Do not resolve by guessing.** Both rows stay as-is until verified.

**On resolution:** add a `verified_live.json` entry for whichever side is confirmed live,
then re-run `scripts/derive_status.py`.

> **Note on a mis-paired duplicate.** This item has been raised as a "US-011 / US-025
> duplicate". It is not one. Verified against `features-master.xlsx` on 2026-07-22:
> row 120 = `US-011` *Level 2 Order Book (US)* ("Market depth for US stocks"); row 134 =
> `US-025` *Major Shareholder* ("Institutional ownership breakdown"). Two different
> features. `US-025` pairs with `SAU-045` Major Shareholder Data. A search for "level 2"
> across the whole dataset returns exactly two rows — `SAU-038` and `US-011` — which is
> the correct one-per-market pairing, **not** a duplicate. There is nothing to merge or
> delete.

---

### 2. Five US Trading features — confirm live, then stamp `verified_live`

**Status:** OPEN — needs in-app verification
**Raised:** 2026-07-22
**Features:** `US-002`, `US-003`, `US-004`, `US-006`, `US-047`

**Question for all five:** *confirm live in ARC US app, then stamp `verified_live`.*

These are core US trading features judged almost certainly live, but carrying no
`verified_live` record — so the pipeline cannot confirm them. **The fix is evidence,
not a status flip. Do NOT change their hand-typed status.**

| id | name | definition | hand-typed | derived | backed by |
|---|---|---|---|---|---|
| US-002 | US Stock Profile Page | Detailed US stock info with financials | Live | Planned ↻ | BRD ARCD-14312 + Figma |
| US-003 | Shariah Compliance Lists | General + ARC-specific Shariah filter | Live | Planned ↻ | BRD ARCD-2067 |
| US-004 | US Stock Search | Search by ticker/name in Arabic/English | Live | Planned ↻ | BRD ARCD-50707 |
| US-006 | Bulls vs Bears | Bullish/bearish case via Benzinga | Live | Planned ↻ | BRD ARCD-61067 |
| US-047 | Buying Power Swap (US) | Swap buying power between US portfolios or accounts | **Gap** | Unverified ↻ | — nothing |

> ⚠️ **`US-047` differs from the other four.** It is hand-typed **`Gap`**, not `Live`, and has
> no BRD, no Figma, and no competitor evidence (derived `Unverified`). It is included here
> on the product owner's judgement that it is in fact live. If the app check confirms it,
> that resolves a mis-typed `Gap` — a larger correction than the other four, which only
> need their existing `Live` claim substantiated.
>
> *Source: Ahmed Alghamdi · 2026-07-22*

**On resolution:** for each confirmed feature add a `data/verified_live.json` entry
(`verified_date`, `method`, `evidence`, `confidence`), then re-run
`scripts/derive_status.py`. A verified-live record dated within 90 days derives `Live`
and clears the ↻ automatically — no manual status edit required.

**Not included in this item** — the three US features where the derived status is
`Gap (unconfirmed)` *because competitors demonstrably ship the feature*, which is a
stronger contradiction than a missing record: `US-013` Pre/Post Market Trading
(Moomoo, Robinhood, IBKR), `US-016` Stock Compare (Moomoo, Investing.com), `US-017`
ETF Exposure View (Moomoo, Investing.com). All three are hand-typed `Live`. These
remain open and unassigned.

---

## Resolved

_(none yet)_
