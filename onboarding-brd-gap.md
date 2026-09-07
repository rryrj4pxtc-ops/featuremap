# Onboarding — BRD Gap Analysis
**Onboarding features with no BRD:** 64  |  **Generated:** 2026-08-10

> The onboarding 'gap' is inflated by **account-type duplication** — the same screen is entered once per account type (ARB / Local / Global / Corporate / Minor). 19 documented variants were just linked (Corporate sub-screens, Login, Guest Mode). The remaining features cluster into **12 screen-families** (each needs ONE BRD covering all account-type variants) plus 4 singletons.

---

## Screen-families — 12 BRDs cover 60 features
> Write one BRD per row; it covers all listed account-type variants.

| Screen (one BRD each) | Variants | Feature IDs |
|---|---|---|
| Splash Screen & App Launch | 5 | ONB-014, ONB-048, ONB-066, ONB-084, ONB-102 |
| Add/Create Password | 5 | ONB-016, ONB-050, ONB-068, ONB-086, ONB-104 |
| Face ID / Biometric Setup | 5 | ONB-017, ONB-051, ONB-069, ONB-087, ONB-105 |
| Change Password | 5 | ONB-018, ONB-052, ONB-070, ONB-088, ONB-106 |
| KYC Confirmation Screens | 5 | ONB-020, ONB-053, ONB-071, ONB-089, ONB-107 |
| Progress Indicator / Stepper | 5 | ONB-022, ONB-054, ONB-072, ONB-090, ONB-108 |
| Onboarding Checklist / Guide | 5 | ONB-024, ONB-055, ONB-073, ONB-091, ONB-109 |
| First Engagement | 5 | ONB-025, ONB-056, ONB-074, ONB-092, ONB-110 |
| Tutorials / How-To Guides | 5 | ONB-040, ONB-058, ONB-076, ONB-094, ONB-112 |
| How to Deposit Guide | 5 | ONB-041, ONB-059, ONB-077, ONB-095, ONB-113 |
| How to Trade Guide | 5 | ONB-042, ONB-060, ONB-078, ONB-096, ONB-114 |
| Data Consent Management | 5 | ONB-043, ONB-061, ONB-079, ONB-097, ONB-115 |

## Singletons (4)
| Feature | Definition |
|---|---|
| ONB-012 Guardian Trading for Minor | Execute trades on behalf of minor |
| ONB-021 Family Members Overview | Home screen showing linked family accounts |
| ONB-023 Pre-filled KYC from National I | Pre-fill fields from ID data — faster regist |
| ONB-026 Fast Onboarding | Streamlined reduced-step KYC (364 screens) |

---

## Recommendation
- The 64 gaps collapse to **~16 BRDs** (not 64) once account-type duplication is accounted for.
- **Consider consolidating** the 5×-duplicated screen rows in the features map itself — one feature with an 'account types' attribute would be cleaner than 5 near-identical rows and would shrink the apparent gap.
- Priority families: authentication (Add/Create Password, Face ID, Change Password) and KYC Confirmation — core to every onboarding flow.

*Source: Features Map · 2026-08-10 · features_derived.json*
