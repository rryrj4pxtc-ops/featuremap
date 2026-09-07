# Benchmark — ARC vs Sahm Capital

**Date:** 2026-08-24 · **Prepared by:** Digital Experience Department
**Scope:** Al Rajhi Capital (AlRajhi Capital, iOS SA) vs Sahm Capital (Sahm – Stock Trading, iOS SA)
**Method:** live iTunes lookup + 148 most-recent App Store reviews + the 20 Sahm coverage cells
already held in the features map. Every figure below is measured, not estimated, except where
marked.

---

## 1. Headline

Sahm is one-sixteenth of ARC's installed base and is out-executing it on experience.
ARC's **lifetime** rating is healthy at 4.57; its **recent** rating is 1.78. Sahm's is 4.65.

| | **ARC** | **Sahm** |
|---|---|---|
| App | AlRajhi Capital | Sahm – Stock Trading |
| Current version | 8.2.0 · 22 Aug 2026 | 3.4.1 · 11 Aug 2026 |
| Lifetime rating | **4.57** (217,013 ratings) | **4.68** (13,498 ratings) |
| **Recent-review average** | **1.78** | **4.65** |
| 1-star share, recent | **74 of 99 (75%)** | 2 of 49 (4%) |
| UX-complaint share, recent | **29%** | **4%** |
| On the App Store since | Mar 2023 | Dec 2023 |

*Source: App Store SA · iTunes API · 2026-08-24 · 99 ARC + 49 Sahm most-recent reviews*

---

## 2. The rating split is the finding

ARC's 4.57 lifetime average is carried by 217k historical ratings. It is not describing the
app investors are using now.

**Recent ARC reviews by version — every single one below 2.7:**

| Version | Reviews | Avg |
|---|---:|---:|
| 8.1.9 | 22 | 2.64 |
| 8.0.10 | 22 | **1.27** |
| 8.0.5 | 14 | 2.07 |
| 8.0.11 | 11 | 2.09 |
| 8.0.9 | 10 | **1.00** |
| 8.1.0 | 8 | 1.62 |
| 8.0.4 | 6 | 1.33 |
| 8.0.6 | 4 | 1.25 |

This is not one bad build. It is sustained across the whole 8.0–8.1 line.

**Sahm, same window:** v3.4.1 → 4.60 (43 reviews), v3.4.0 → 5.00 (6 reviews).

### What ARC investors are actually complaining about

| Theme | Mentions in 99 reviews |
|---|---:|
| Complexity — "the app got harder" | 9 |
| Deposit / funding friction | 9 |
| Login and errors | 9 |
| Speed, hanging | 7 |
| **"Bring back the old version"** | **6** |
| Session drops / being logged out | 2 |

The regression theme is the sharpest signal: six separate reviewers asking to revert to a
previous version. One representative complaint, translated: *"the app has become more complex,
and the deposit is harder than before and not understandable."* Another reports a price-alert
bug on decimal values, *"a month old and still like this."*

*Source: App Store reviews · AlRajhi Capital · SA · 2026-08-24*

---

## 3. Feature benchmark

Twenty features in the map carry Sahm evidence. **Sahm leads on 13, matches on 5, and ARC has
2 in flight.** ARC leads on none of the twenty.

### Sahm has it · ARC gap (13)

| ID | Feature | Journey | Confidence |
|---|---|---|---|
| **SAU-221** | **Drag and Drop Trade on Chart** | Saudi Market | high |
| SAU-121 / US-015 | AI Assistant | Saudi / US | high / low |
| SAU-112 / SAU-134 / US-019 / US-126 | Unusual Activity *(market + stock, both markets)* | Saudi / US | high |
| SAU-031 | Iceberg orders | Saudi Market | high |
| SAU-051 | Auto-Watchlist on Buy | Saudi Market | low |
| US-025 | Major Shareholder | US Trading | high |
| XJ-049 | ARC Chatbot | Platform | high |
| XJ-045 | Social Community Feed | Platform | high |
| XJ-027 | Personalized Events Calendar | Platform | low |

### Parity (5)
Configurable Price Alerts · Technical Analysis · Conditional orders · Quick Reorder ·
Stock Dividend

### ARC in flight (2)
Options (SAU-012, Planned) · Bracket orders (SAU-047, Planned)

*Source: Features Map · 2026-08-24 · coverage.json*

---

## 4. Sahm's current release, read directly

Sahm v3.4.1 release notes, verbatim from the App Store:

> **[Major] Place orders directly from charts.**
> [New] Added support for the Ichimoku technical indicator.
> [Optimization] Integrated higher-frequency market data for options.
> [Optimization] The option chain now supports one-tap return to At-The-Money (ATM) contracts.
> [Optimization] AI Chat now allows sharing conversation content.

Three things worth noting:

1. **Sahm labelled drag-to-trade "[Major]" themselves.** This independently confirms SAU-221
   from a second source — the X post of 20 Aug was the first.
2. **Options depth is being tuned, not built.** Higher-frequency options data and one-tap ATM
   on the option chain are refinements of a shipped feature. ARC's Options (SAU-012) is still
   Planned, and Options Chain has no US or Saudi row beyond the contract slot.
3. **AI Chat is mature enough to be adding conveniences** (sharing conversations). ARC's AI
   Assistant is a Gap in both markets.

*Source: App Store SA · iTunes API · Sahm v3.4.1 · 11 Aug 2026*

---

## 5. Where ARC is genuinely ahead

Nothing in the twenty measured features — but the benchmark is deliberately narrow, and two
structural advantages sit outside it:

- **Scale.** 217,013 ratings to Sahm's 13,498 — roughly 16×. Distribution and trust are ARC's
  to lose, which is exactly what a 1.78 recent average threatens.
- **Breadth.** Sahm is a trading app. ARC spans onboarding, funds, robo, IPOs, corporate
  actions and cash management. None of that is in scope here because no Sahm evidence touches
  it — absence of evidence, not evidence of absence.

**Stated honestly: this benchmark measures the surfaces where the two overlap, and Sahm wins
all of them.**

---

## 6. What I would do

1. **Treat the recent-rating collapse as a P1 in its own right.** A 4.57 lifetime average is
   hiding a 1.78 current reality from every dashboard that reports it. Report both numbers,
   permanently.
2. **Run the six "bring back the old version" reviews to ground.** A regression complaint that
   specific, repeated six times, names a decision someone made. Find it.
3. **Deposit and funding friction (9 mentions) is not a UX polish item** — it sits directly on
   revenue. Worth a dedicated journey review before any feature work.
4. **On features, pick the two Sahm just proved investors notice:** drag-to-trade on the chart
   (SAU-221) and AI assistance (SAU-121 / US-015). Both are Gaps, both are visible in the
   first minute of using a competitor's app.
5. **Do not benchmark on lifetime rating again.** Sahm's 4.68 and ARC's 4.57 look like a close
   race; the reality this month is 4.65 against 1.78.

---

## Limits of this benchmark

- The review window is the **most recent ~100 per app**, which is what the App Store RSS
  exposes. It is current sentiment, not a full history.
- **Release cadence was not scored.** The iTunes API returns only the current version, and no
  version history is held locally, so the Maturity Score's cadence criterion could not be
  computed honestly. The other four criteria are reflected above.
- Feature coverage is limited to the **20 features that carry Sahm evidence**. Sahm may have
  more that ARC has never checked, and ARC has large areas Sahm does not compete in.
- Two of the 13 gap rows are `low` confidence (SAU-051, XJ-027) and one is flagged
  `journey_mismatch` (US-015).

*Prepared by Digital Experience · Sources: App Store SA (iTunes API) · App Store reviews ·
Features Map coverage.json · 2026-08-24*
