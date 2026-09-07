# ARC Live App Bugs — International Brokerage
*Source: 20260325 - International brokerage app gap analysis vShared.pdf*
*Identified: 2026-03-25*
*Scope: International Brokerage (US Trading) experience*

| # | Bug | Category | Severity | Description |
|---|---|---|---|---|
| B-01 | SMS notifications for deposits/transfers | Notifications | Medium | SMS messages sent for deposits and transfers lack clarity and structure — recipients cannot easily parse the transaction details from the message format. |
| B-02 | Bid & Ask layout inconsistency | Data Display | High | Arabic interface shows Bid and Ask on opposite sides in the header vs. the price table, creating a directional mismatch. English interface also shows labels on the wrong sides. Affects order decision-making. |
| B-03 | Insufficient funds redirect shows wrong currency | Order Flow | High | When a USD order is rejected for insufficient funds, the app redirects the user to fund their SAR wallet instead of their USD account — wrong currency shown to user, causing confusion. |
| B-04 | Order status mismatch between SMS and app | Order Tracking | High | After a trade executes, the confirmation SMS says "completed" but the app shows the order as "active" in Today's Orders and only "completed" under Last Month's Transactions — inconsistent state across surfaces. |
| B-05 | US portfolio size shown incorrectly on home screen | Portfolio Display | Critical | Home page portfolio breakdown displays a wrong value for US market holdings (e.g., $2 displayed instead of the actual $48,000) — a major data accuracy issue affecting client trust. |
| B-06 | Portfolio performance discrepancy | Portfolio Display | Critical | Total portfolio performance shown on the home screen does not match the sum of individual market performance figures — numbers are inconsistent across home and portfolio views. |
| B-07 | Earnings announcements shown during trading hours | Market Data | Medium | Earnings announcements appear in-app at 11 AM while the market is open. These should be shown before market open or after market close to avoid misleading trading signals during live sessions. |
| B-08 | Swipe-to-cancel available on executed orders | Order Management | High | The swipe-to-cancel gesture is active on already-executed orders. When triggered, the app attempts to cancel an order that is already filled and returns a "rejected" status — confusing and potentially alarming for users. |
| B-09 | Rejected order blocks cash + SMS confirms non-existent order | Order Flow | Critical | A rejected order incorrectly blocks the user's cash balance, preventing new orders from being placed. Simultaneously, the SMS system sends an execution confirmation for a new order that never appears in the app — two compounding failures in one flow. |
| B-10 | Visual price indicator misalignment on range scale | Data Display | Low | The price indicator marker on the stock's price range scale does not visually align with the actual current price — a display rendering issue that reduces data readability. |

---

> **Note:** These are bugs in the CURRENT LIVE APP — not the Figma revamp. Must be logged with squad leads and resolved before or alongside the revamp launch.
