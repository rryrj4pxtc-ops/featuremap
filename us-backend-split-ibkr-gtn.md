# US Trading — IBKR / GTN Backend Split

*US Trading runs on two brokerage backends — **IBKR** (Interactive Brokers) and **GTN** (Global Trading Network). Some features are live on one backend but a gap on the other.*

## Modeling (updated 2026-08-11)
The split is now modeled as **explicit paired feature rows** — `Feature (IBKR)` and `Feature (GTN)` — each with its own status, rather than a `backends` column on a single row. This makes each backend's gap visible in the normal Live/Planned/Gap counts and roadmap.

| Capability | IBKR row | GTN row |
|---|---|---|
| Portfolio P&L View | US-049 — Live | US-110 — Gap |
| Performance Chart | US-053 — Live | US-111 — Gap |
| Analysis Dashboard | US-061 — Live | US-112 — Gap |
| Fractional Shares | US-014 — Live | US-113 — Gap |
| Trailing Order | US-045 — Live | US-114 — Gap |

**Pattern:** every split capability is **Live on IBKR, a gap on GTN** — GTN is the lagging backend for US portfolio/order features.

*The `backends` column + pipeline parsing remain available for any future single-row split, but no feature currently uses it.*

*Source: Ahmed Alghamdi · 2026-08-11 · gap review · Features Map*
