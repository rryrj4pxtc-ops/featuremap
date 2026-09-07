# Competitive Gap Brief — ARC Digital Experience
### 36 features rivals ship that ARC does not · 2026-08-11

*Distribution: Product squads, CPO, DX. Scope: **competitive** gaps only — features where a benchmarked competitor has the capability and ARC does not. Excludes the 120 internal Saudi↔US parity gaps (tracked separately in the parity build lists).*

*Source: Features Map · 2026-08-11 · competitor benchmarking via `coverage.json` + Competitor Intelligence Index. Priority = Investor Demand (impact) × Competitive Pressure (# rivals), 1–25.*

---

## Executive Summary

Of ARC's 156 feature gaps, only **36 are competitive** — a rival actually ships the feature. The other 120 are internal Saudi↔US parity gaps. Two rivals define the competitive frontier, and they are opposite in nature:

| Rival | Our gaps they cover | Character |
|---|---:|---|
| **Moomoo** | 13 | **High-value capability** — smart-money analytics, screener, social, fractional |
| **Sahm** | 13 | **Low-value polish** — chart touch, navigation, layout, language |
| Derayah + Derayah Smart | 14 | Robo, onboarding, screener, dividends |
| Investing.com | 5 | Screener, AI, allocation |
| AlJazira Capital | 4 | Private funds, SIP, IPO |
| IBKR / thinkorswim / TradingView / NinjaTrader | — | Pro-grade charting |

**The strategic read:** *Moomoo threatens with capability; Sahm threatens with polish.* Treat them differently — Moomoo's gaps are coherent product bets worth roadmapping; Sahm's are a single polish sprint.

---

## The Three Roadmap Bets

**1. Stock Screener — both markets (highest priority).** The single most-benchmarked gap: 3 rivals in Saudi, 2 in US. Discrete, high-demand, no dependency.

| ID | Feature | Priority | Competitors |
|---|---|---|---|
| SAU-039 | Stock Screener | 10 | Derayah, Investing.com, Moomoo |
| US-012 | Stock Screener | 3 | Moomoo, Investing.com |

Owner: **Saudi Trading + US Trading Squads** · Effort: M (one build, two markets)

**2. Smart-Money Analytics — neutralize Moomoo.** Five gaps form one coherent theme Moomoo owns end-to-end and ARC has none of. Building them as a workstream (not one-offs) closes Moomoo's clearest advantage.

| ID | Feature | Priority | Competitors |
|---|---|---|---|
| SAU-043 | Money Flow Tracking | 5 | Moomoo, Sahm |
| US-018 | Whale / Institutional Tracking | 5 | Moomoo, Robinhood |
| US-015 | AI-Powered Assistant | 5 | Investing.com, Moomoo |
| SAU-045 | Major Shareholder | 4 | Derayah, Moomoo |
| SAU-089 | Visual Asset Allocation | 2 | Moomoo, Investing.com |

Owner: **Product Experience Design** (cross-squad theme: Saudi + US Trading) · Effort: L

**3. Robo parity — close Derayah Smart.** All four robo competitive gaps are vs Derayah Smart alone — they out-execute ARC on the robo journey specifically. Close them as a bundle.

| ID | Feature | Priority | Competitors |
|---|---|---|---|
| RBO-005 | Goal-Based Portfolio (Full) | 4 | Derayah Smart, AlJazira Capital |
| RBO-006 | Try-Before-Invest Simulator | 5 | Derayah Smart, Moomoo, Sahm |
| RBO-007 | Robo Calculator | 3 | Derayah Smart |
| RBO-008 | Strategy Comparison | 3 | Derayah Smart |

Owner: **Robo Advisory Squad** · Effort: M

---

## Secondary Clusters

**Charting depth (a bigger bet — needs feasibility).** ARC's charting trails the pro-tool tier. SAU-048 is the widest single gap on the board — 4 pro platforms benchmark it.

| ID | Feature | Priority | Competitors |
|---|---|---|---|
| SAU-048 | Chart Trading | 4 | TradingView, thinkorswim, NinjaTrader, IBKR |
| SAU-047 | Bracket Order (OCO) | 2 | thinkorswim |
| SAU-050 | Chart Touch-and-Hold | 1 | Sahm |
| SAU-053 | Chart Axis to Market Close | 1 | Sahm |

Owner: **Saudi Trading Squad** · Effort: L–XL · *Recommend a build-vs-embed (TradingView) feasibility review first.*

**Onboarding conversion polish (Derayah).**

| ID | Feature | Priority | Competitors |
|---|---|---|---|
| ONB-023 | Pre-filled KYC from National ID | 5 | Derayah |
| ONB-024 | Onboarding Checklist / Guide | 5 | Sahm, Derayah Smart |
| ONB-022 | Progress Indicator / Stepper | 4 | Derayah, Derayah Smart |

Owner: **Onboarding Squad** · Effort: S–M

**Managed-product access (AlJazira / Derayah).**

| ID | Feature | Priority | Competitors |
|---|---|---|---|
| MF-012 | Private Funds / PE Access | 5 | AlJazira Capital, Derayah |
| MF-013 | SIP for Mutual Funds | 5 | AlJazira Capital, Derayah Smart |

Owner: **Mutual Funds Squad** · Effort: M (regulatory dependency on PE access)

---

## The Sahm Polish Sprint (batch — not roadmap items)

13 gaps are vs Sahm and almost all are priority 1–2: small UX refinements. **Do not roadmap individually** — bundle into one polish sprint owned by Product Experience Design.

| ID | Feature | Priority | Competitors |
|---|---|---|---|
| SAU-044 | Quick Reorder | 4 | Sahm |
| SAU-051 | Auto-Watchlist on Buy | 2 | Sahm |
| SAU-054 | Standard S&D Layout | 2 | Sahm |
| SAU-097 | Batch Close Positions | 2 | Moomoo |
| XJ-025 | 1-Click Language Switch | 2 | Sahm |
| XJ-027 | Personalized Events Calendar | 2 | Sahm |
| XJ-028 | Tab-Based Navigation | 2 | Sahm |
| XJ-046 | Cashback Prediction Game | 1 | Sahm |

*(Chart touch SAU-050/053 already counted under Charting; ONB-024, RBO-006, SAU-043 counted in their strategic clusters.)*

---

## Appendix — all 36 competitive gaps by squad

### Saudi Market — Saudi Trading Squad (13)

| ID | Feature | Priority | Competitors |
|---|---|---|---|
| SAU-039 | Stock Screener | 10 | Derayah, Investing.com, Moomoo |
| SAU-043 | Money Flow Tracking | 5 | Moomoo, Sahm |
| SAU-044 | Quick Reorder | 4 | Sahm |
| SAU-045 | Major Shareholder | 4 | Derayah, Moomoo |
| SAU-048 | Chart Trading | 4 | TradingView, thinkorswim, NinjaTrader, IBKR |
| SAU-098 | Auto Dividend Reinvest | 3 | Derayah |
| SAU-089 | Visual Asset Allocation | 2 | Moomoo, Investing.com |
| SAU-097 | Batch Close Positions | 2 | Moomoo |
| SAU-054 | Standard S&D Layout | 2 | Sahm |
| SAU-047 | Bracket Order (OCO) | 2 | thinkorswim |
| SAU-051 | Auto-Watchlist on Buy | 2 | Sahm |
| SAU-050 | Chart Touch-and-Hold | 1 | Sahm |
| SAU-053 | Chart Axis to Market Close | 1 | Sahm |

### US Trading — US Trading Squad (6)

| ID | Feature | Priority | Competitors |
|---|---|---|---|
| US-014 | Fractional Shares | 8 | IBKR, Moomoo, Robinhood |
| US-015 | AI-Powered Assistant | 5 | Investing.com, Moomoo |
| US-018 | Whale / Institutional Tracking | 5 | Moomoo, Robinhood |
| US-012 | Stock Screener | 3 | Moomoo, Investing.com |
| US-011 | Level 2 Order Book | 2 | Moomoo, IBKR |
| US-017 | ETF Exposure View | 1 | Moomoo, Investing.com |

### Robo Advisory — Robo Advisory Squad (4)

| ID | Feature | Priority | Competitors |
|---|---|---|---|
| RBO-006 | Try-Before-Invest Simulator | 5 | Derayah Smart, Moomoo, Sahm |
| RBO-005 | Goal-Based Portfolio (Full) | 4 | Derayah Smart, AlJazira Capital |
| RBO-007 | Robo Calculator | 3 | Derayah Smart |
| RBO-008 | Strategy Comparison | 3 | Derayah Smart |

### Platform — Product Experience Design (4)

| ID | Feature | Priority | Competitors |
|---|---|---|---|
| XJ-026 | Free Live Index Prices | 3 | Sahm, Abyan |
| XJ-025 | 1-Click Language Switch | 2 | Sahm |
| XJ-027 | Personalized Events Calendar | 2 | Sahm |
| XJ-028 | Tab-Based Navigation | 2 | Sahm |

### Onboarding — Onboarding Squad (3)

| ID | Feature | Priority | Competitors |
|---|---|---|---|
| ONB-023 | Pre-filled KYC from National ID | 5 | Derayah |
| ONB-024 | Onboarding Checklist / Guide | 5 | Sahm, Derayah Smart |
| ONB-022 | Progress Indicator / Stepper | 4 | Derayah, Derayah Smart |

### Mutual Funds — Mutual Funds Squad (2)

| ID | Feature | Priority | Competitors |
|---|---|---|---|
| MF-012 | Private Funds / PE Access | 5 | AlJazira Capital, Derayah |
| MF-013 | SIP for Mutual Funds | 5 | AlJazira Capital, Derayah Smart |

### Investor Engagement — Investor Engagement Squad (2)

| ID | Feature | Priority | Competitors |
|---|---|---|---|
| XJ-045 | Social Community Feed | 10 | Moomoo |
| XJ-046 | Cashback Prediction Game | 1 | Sahm |

### Cash Management — Cash Management (1)

| ID | Feature | Priority | Competitors |
|---|---|---|---|
| XJ-036 | Apple Pay / Digital Wallet | 5 | Derayah |

### IPOs — IPOs Squad (1)

| ID | Feature | Priority | Competitors |
|---|---|---|---|
| IPO-008 | IPO Popup Banner | 2 | AlJazira Capital |

*Source: Features Map · 2026-08-11 · `features_derived.json` (competitive gaps = status Gap + ≥1 benchmarked competitor).*
