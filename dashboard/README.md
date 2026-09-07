# Features Map Dashboard

Self-contained dashboard for the ARC Digital Experience feature inventory.

---

## Architecture

```
features-master.xlsx          ← Single source of truth (edit here)
        │
        ▼
scripts/xlsx-to-features-json.py   ← Export script (Python 3 + openpyxl)
        │
        ├── data/features.json
        ├── data/brds.json
        └── data/benchmarks.json
              │
              ▼
      index.html → views/cockpit.html   (KPI dashboard)
                 → views/heatmap.html   (competitor parity matrix)
                 → views/atlas.html     (D3 mind map — static copy)
```

No build step. No bundler. Open `index.html` in any browser.

---

## Quick Start

### 1. Create the blank Excel template (one-time)

```bash
python3 scripts/build_template.py
```

Produces `features-master.xlsx` with validated dropdowns, conditional formatting, and pre-populated Benchmarks.

### 2. Populate the Excel

Open `features-master.xlsx` and fill in the **Features**, **BRDs**, and **Benchmarks** sheets. See `SCHEMA.md` for field definitions and allowed values.

### 3. Export to JSON

```bash
python3 scripts/xlsx-to-features-json.py
```

Reads the Excel, validates every row, and writes three JSON files into `data/`. Exits non-zero if there are hard errors (missing required fields, invalid enums, duplicate IDs).

### 4. View the dashboard

Open `index.html` in a browser. The three views load JSON via `fetch()` — no server needed if opened via `file://` in most browsers (or use `python3 -m http.server 8000`).

---

## Files

| File | Purpose |
|------|---------|
| `features-master.xlsx` | Single source of truth for all feature data |
| `scripts/build_template.py` | Creates the blank xlsx template with validation rules |
| `scripts/xlsx-to-features-json.py` | Exports xlsx to JSON with validation |
| `data/features.json` | Feature records consumed by cockpit and heatmap |
| `data/brds.json` | BRD registry |
| `data/benchmarks.json` | Canonical competitor list |
| `SCHEMA.md` | Full field-level documentation for all three schemas |
| `index.html` | Landing page with links to three views |
| `views/cockpit.html` | KPI summary, journey health, gaps, differentiators, attention queue |
| `views/heatmap.html` | Journey x competitor parity heatmap with drill-down panel |
| `views/atlas.html` | D3 mind map (verbatim copy of the original mind map) |

---

## Operating Model

1. **Edit** `features-master.xlsx` — this is the only file you ever edit for data changes.
2. **Run** `python3 scripts/xlsx-to-features-json.py` — validates and exports.
3. **Open** `index.html` — views read from `data/*.json` at load time.

Never edit the JSON files directly. Never modify `atlas.html` for data changes — that view uses its own embedded dataset from the original mind map.

---

## Dependencies

- **Python 3.8+** with `openpyxl` (`pip install openpyxl`)
- A modern browser (Chrome, Safari, Firefox, Edge)
- No other dependencies. No Node.js. No build tools.

---

## Color Palette

| Token | Hex | Usage |
|-------|-----|-------|
| Background | `#000045` | Page background |
| Surface | `#09009E` | Cards, panels |
| Accent | `#221AFB` | Borders, highlights |
| Text | `#FFFFFF` | Primary text |
| Muted | `#A2E3FF` | Secondary text, labels |
| Live / Success | `#20C992` | Live status |
| Planned / Info | `#00B2FF` | Planned status |
| Gap / Danger | `#F43653` | Gap status, alerts |
| Diff / Warning | `#F1B53D` | Differentiator status |
