# US Trading — Internal Parity Build List (2026-08-11)

*The 64 US Trading features that exist (or are planned) in the Saudi market but are missing in US. These are **internal parity gaps** — not competitive gaps. Building them brings US Trading to parity with Saudi and is the primary lever on US Trading maturity (~21). Auto-generated from `features_derived.json` by base-name twin matching.*

**Summary:** 27 ready-to-port (Saudi source Live) · 8 Planned · 27 gap-in-both · 2 other.

**Priority order:** Saudi source **Live** first (shipped reference + BRD already exists — fastest to port), then **Planned**, then gap-in-both (needs design in both markets).

| US ID | Feature | Saudi Source | Saudi Status | Reusable BRD |
|---|---|---|---|---|
| | **── Saudi source: Live ──** | | | |
| US-035 | Basket Order | SAU-035 | Live | — |
| US-038 | Order Filter Panel | SAU-036 | Live | — |
| US-039 | Advanced Technical Analysis | SAU-040 | Live | — |
| US-040 | Market-on-Close (MOC) | SAU-007 | Live | ARCD_9245 |
| US-050 | Update Avg Cost Price | SAU-022 | Live | ARCD-2650 |
| US-051 | Portfolio Holdings | SAU-073 | Live | ARCD-2654 |
| US-052 | Official Letter | SAU-074 | Live | — |
| US-053 | Performance Chart | SAU-075 | Live | ARCD-2654 |
| US-059 | Holdings Filter Panel | SAU-094 | Live | — |
| US-060 | Liquidate Holdings | SAU-080 | Live | — |
| US-064 | Sector/Index Filters | SAU-095 | Live | — |
| US-066 | News Screen | SAU-067 | Live | ARCD-24713, ARCD-39221 |
| US-069 | Watchlist | SAU-057 | Live | — |
| US-087 | List of Orders | SAU-120 | Live | — |
| US-088 | Orders Empty State | SAU-037 | Live | — |
| US-089 | Conditional Order Detail | SAU-029 | Live | — |
| US-090 | Transfer Holdings | SAU-078 | Live | — |
| US-091 | Watchlist — Edit / Reorder | SAU-060 | Live | — |
| US-092 | Margin Lending (Murabaha) | SAU-003 | Live | ARCD-1634 |
| US-093 | Auto Margin Approval | SAU-008 | Live | ARCD 1923, ARCD-85843, ARCD-86236 |
| US-094 | Margin Contract Renewal | SAU-009 | Live | ARCD-2367 |
| US-095 | Margin Early Payment | SAU-010 | Live | ARCD-2367 |
| US-096 | Margin Phase 2 (Commodities) | SAU-011 | Live | ARCD-2424 |
| US-098 | Sukuk Trading | SAU-046 | Live | ARCD-72385 |
| US-099 | Place Limit Order | SAU-002 | Live | ARCD-1553, ARCD-87521 |
| US-100 | Basket Order Detail | SAU-030 | Live | — |
| US-101 | Dividends Screen | SAU-068 | Live | — |
| | **── Saudi source: Planned ──** | | | |
| US-041 | Short Selling | SAU-015 | Planned | ARCD-53753 |
| US-042 | Attached Order | SAU-103 | Planned | ARCD-75523 |
| US-047 | Buying Power Swap | SAU-023 | Planned | ARCD-2644 |
| US-054 | Peer Portfolio Comparison | SAU-084 | Planned | ARCD-60816 |
| US-065 | Sector & Exchange Volatility | SAU-025 | Planned | ARCD-58777 |
| US-070 | Watchlist Story | SAU-058 | Planned | — |
| US-072 | StoryTeller | SAU-092 | Planned | — |
| US-102 | Custom Index Against Benchmark | XJ-055 | Planned | ARCD-60887 |
| | **── Saudi source: Gap ──** | | | |
| US-019 | Unusual Activity Alerts | SAU-112 | Gap | — |
| US-021 | Futures Trading | SAU-113 | Gap | — |
| US-024 | Fast Order (No Confirm) | SAU-114 | Gap | — |
| US-025 | Major Shareholder | SAU-045 | Gap | — |
| | **── Saudi source: Gap (unconfirmed) ──** | | | |
| US-036 | Quick Reorder | SAU-044 | Gap (unconfirmed) | — |
| US-037 | Bracket Order (OCO) | SAU-047 | Gap (unconfirmed) | — |
| | **── Saudi source: Gap ──** | | | |
| US-044 | Chain Order | SAU-105 | Gap | — |
| US-045 | Trailing Order | SAU-106 | Gap | ARCD-75523 |
| US-046 | Iceberg Order | SAU-031 | Gap | — |
| US-048 | Instant Settlement | SAU-024 | Gap | ARCD-14352 |
| US-049 | Portfolio P&L View | SAU-020 | Gap | ARCD-2654 |
| US-055 | Portfolio Insights | SAU-085 | Gap | ARCD-60816 |
| US-056 | Portfolio Health Score | SAU-086 | Gap | ARCD 52378 |
| US-057 | Allocation Tracker | SAU-087 | Gap | ARCD-61176 |
| US-061 | Analysis Dashboard | SAU-088 | Gap | — |
| | **── Saudi source: Gap (unconfirmed) ──** | | | |
| US-063 | Visual Asset Allocation | SAU-089 | Gap (unconfirmed) | — |
| US-068 | Money Flow Tracking | SAU-043 | Gap (unconfirmed) | — |
| US-075 | Batch Close Positions | SAU-097 | Gap (unconfirmed) | — |
| US-076 | Auto Dividend Reinvest | SAU-098 | Gap (unconfirmed) | — |
| | **── Saudi source: Gap ──** | | | |
| US-077 | Chart Trading | SAU-048 | Gap | — |
| | **── Saudi source: Gap (unconfirmed) ──** | | | |
| US-078 | Chart Touch-and-Hold | SAU-050 | Gap (unconfirmed) | — |
| US-079 | Chart Axis to Market Close | SAU-053 | Gap (unconfirmed) | — |
| US-080 | Standard S&D Layout | SAU-054 | Gap (unconfirmed) | — |
| US-081 | Auto-Watchlist on Buy | SAU-051 | Gap (unconfirmed) | — |
| | **── Saudi source: Gap ──** | | | |
| US-086 | Minichart Component | SAU-119 | Gap | — |
| US-103 | Stocks Key Facts | XJ-058 | Gap | ARCD-72344 |
| US-104 | Personal Investment Manager | XJ-063 | Gap | ARCD-60444 |
| | **── Saudi source: NO TWIN ──** | | | |
| US-020 | Bonds Trading | — | NO TWIN | — |
| | **── Saudi source: Diff ──** | | | |
| US-097 | Murabaha Margin Lending | SAU-056 | Diff | #25-29 |

*Source: Features Map · 2026-08-11 · US↔Saudi base-name parity match*
