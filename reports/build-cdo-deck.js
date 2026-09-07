#!/usr/bin/env node
/**
 * build-cdo-deck.js
 * Builds the CDO evidence-based feature matrix deck using arc-deck-template.
 *
 * Reads:
 *   data/features_derived.json
 *   data/coverage.json
 *   data/verified_live.json
 *
 * Usage:  node projects/features-map/reports/build-cdo-deck.js
 * Output: projects/features-map/reports/cdo-feature-matrix-YYYY-MM-DD.pptx
 */

const fs = require("fs");
const path = require("path");
const { Deck, THEME } = require(
  path.join(__dirname, "..", "..", "..", "assets", "templates", "arc-deck-template", "arc-template")
);

const ARC = path.join(__dirname, "..", "..", "..");
const load = (rel) => JSON.parse(fs.readFileSync(path.join(ARC, rel), "utf-8"));

// ── Load data ──────────────────────────────────────────────────────────────────
const derived   = load("data/features_derived.json");
const coverage  = load("data/coverage.json");
const verified  = load("data/verified_live.json");
const features  = derived.features || [];
const covCells  = Object.values(coverage);

// ── Compute stats (never hardcode) ─────────────────────────────────────────────
const total = features.length;
const byStatus = {};
for (const f of features) {
  const s = f.derived_status || "Unknown";
  byStatus[s] = (byStatus[s] || 0) + 1;
}
const conflictCount = features.filter((f) => f.status_conflict).length;

// Verified conflicts: features where verified_live flipped the hand-typed status
const verifiedConflicts = features.filter(
  (f) => f.status_conflict && verified[f.id] && verified[f.id].confidence === "high"
);
const xj020 = verifiedConflicts.find((f) => f.id === "XJ-020") || {};
const mf005 = verifiedConflicts.find((f) => f.id === "MF-005") || {};
const xj020ev = verified["XJ-020"] || {};
const mf005ev = verified["MF-005"] || {};

// Coverage stats
const covTotal = covCells.length;
const covHigh  = covCells.filter((c) => c.confidence === "high").length;
const covLow   = covCells.filter((c) => c.confidence === "low").length;

// Top gaps by priority
const gaps = features
  .filter((f) => (f.derived_status || "").startsWith("Gap"))
  .filter((f) => f.priority != null && f.priority > 0)
  .sort((a, b) => b.priority - a.priority)
  .slice(0, 8);

// Status distribution for chart
const STATUS_ORDER  = ["Live", "Gap (unconfirmed)", "Planned", "Diff", "Unverified"];
const STATUS_COLORS = {
  Live:               "20C992",
  "Gap (unconfirmed)":"F43653",
  Planned:            "00B2FF",
  Diff:               "F1B53D",
  Unverified:         "94A3B8",
};

const today = new Date().toISOString().slice(0, 10);

// ── Build deck ─────────────────────────────────────────────────────────────────
const deck = new Deck({
  deckName: "ARC Feature Matrix",
  date: today,
  author: "ARC Digital Experience",
});

// ── Slide 1: Cover ─────────────────────────────────────────────────────────────
deck.addCover({
  eyebrow: "AL RAJHI CAPITAL  ·  DIGITAL EXPERIENCE",
  title: "The ARC Feature Matrix",
  titleAccent: "From Assertion to Evidence.",
  subtitle: `${total} features. Every status earned from App Store data, competitor intel, and Figma — never typed by hand.`,
});

// ── Slide 2: The Problem ───────────────────────────────────────────────────────
deck.addContent({
  eyebrow: "THE PROBLEM",
  title: "The matrix was self-reported.",
  subtitle: "Status was typed by hand with no link to what ARC actually ships.",
  draw(slide, { THEME: T }) {
    // Big stat
    slide.addText(String(conflictCount), {
      x: T.M, y: 3.0, w: 3.5, h: 1.2,
      fontFace: T.font.serif, fontSize: 72, bold: true,
      color: T.color.purple, margin: 0,
    });
    slide.addText(
      `of ${total} rows where the hand-typed status\ndiverged from the evidence.`,
      {
        x: T.M, y: 4.2, w: 6.0, h: 0.7,
        fontFace: T.font.sans, fontSize: 14,
        color: T.color.navy, margin: 0,
      }
    );

    // Explanation bullets
    const bullets = [
      "Status was typed by hand in the xlsx — Live, Planned, Gap, Diff.",
      "No automated check against App Store releases or competitor data.",
      "Features marked Live had no evidence they actually shipped.",
    ];
    bullets.forEach((t, i) => {
      slide.addText(t, {
        x: T.M, y: 5.2 + i * 0.45, w: 11.0, h: 0.4,
        fontFace: T.font.sans, fontSize: 12, color: T.color.body, margin: 6,
        fill: { color: i % 2 === 0 ? T.color.tintPurple : T.color.white },
      });
    });
  },
});

// ── Slide 3: Proof It Was Wrong ────────────────────────────────────────────────
deck.addCards({
  eyebrow: "PROOF IT WAS WRONG",
  title: "Two features the system caught.",
  subtitle: "Both were detected automatically from ARC App Store v8.0.11 release notes.",
  cards: [
    {
      num: "01",
      title: `${xj020.name || "Configurable Price Alerts"} — typed GAP, shipped`,
      body: xj020ev.evidence || "(no evidence loaded)",
    },
    {
      num: "02",
      title: `${mf005.name || "Fund Performance Chart"} — typed PLANNED, shipped`,
      body: mf005ev.evidence || "(no evidence loaded)",
    },
  ],
});

// ── Slide 4: The Pipeline ──────────────────────────────────────────────────────
deck.addContent({
  eyebrow: "THE PIPELINE",
  title: "Evidence in, status out.",
  subtitle: "Runs unattended every Thursday. No human edits status.",
  draw(slide, { THEME: T }) {
    // Layout: 5 columns across 12.03" usable width (0.65 margin each side)
    // [Sources] → [derive_status.py] → [Derived Status] → [Outputs]
    // Columns: box  arrow  box  arrow  box  arrow  box  arrow  box
    const contentW = 13.333 - 2 * T.M;  // 12.03"
    const boxW = 2.2;
    const arrowW = 0.65;
    // 4 boxes + 3 arrows = 4*2.2 + 3*0.65 = 10.75 → center in 12.03
    const totalW = 4 * boxW + 3 * arrowW;
    const x0 = T.M + (contentW - totalW) / 2;

    const boxH = 0.65, boxR = 0.04;
    const centerY = 4.35;  // vertical center of content area

    // Positions of the 4 column centers
    const colX = [
      x0,
      x0 + boxW + arrowW,
      x0 + 2 * (boxW + arrowW),
      x0 + 3 * (boxW + arrowW),
    ];

    // Column 1: three stacked source boxes
    const sources = ["ARC App Store", "Competitor Intel", "Figma Designs"];
    const stackGap = 0.15;
    const stackH = 3 * boxH + 2 * stackGap;
    const stackY0 = centerY - stackH / 2;
    sources.forEach((label, i) => {
      const y = stackY0 + i * (boxH + stackGap);
      slide.addShape("roundRect", {
        x: colX[0], y, w: boxW, h: boxH, rectRadius: boxR,
        fill: { color: T.color.white },
        line: { color: T.color.hairline, width: 0.75 },
      });
      slide.addText(label, {
        x: colX[0], y, w: boxW, h: boxH, align: "center", valign: "middle",
        fontFace: T.font.sans, fontSize: 11, bold: true,
        color: T.color.navy, margin: 0,
      });
    });

    // Arrow 1
    slide.addShape("line", {
      x: colX[0] + boxW + 0.05, y: centerY, w: arrowW - 0.1, h: 0,
      line: { color: T.color.purple, width: 2, endArrowType: "triangle" },
    });

    // Column 2: derive_status.py (accent box)
    slide.addShape("roundRect", {
      x: colX[1], y: centerY - boxH / 2, w: boxW, h: boxH, rectRadius: boxR,
      fill: { color: T.color.tintPurple },
      line: { color: T.color.purple, width: 1 },
    });
    slide.addText("derive_status.py", {
      x: colX[1], y: centerY - boxH / 2, w: boxW, h: boxH,
      align: "center", valign: "middle",
      fontFace: T.font.sans, fontSize: 11, bold: true,
      color: T.color.purple, margin: 0,
    });

    // Arrow 2
    slide.addShape("line", {
      x: colX[1] + boxW + 0.05, y: centerY, w: arrowW - 0.1, h: 0,
      line: { color: T.color.purple, width: 2, endArrowType: "triangle" },
    });

    // Column 3: Derived Status
    slide.addShape("roundRect", {
      x: colX[2], y: centerY - boxH / 2, w: boxW, h: boxH, rectRadius: boxR,
      fill: { color: T.color.white },
      line: { color: T.color.hairline, width: 0.75 },
    });
    slide.addText("Derived Status", {
      x: colX[2], y: centerY - boxH / 2, w: boxW, h: boxH,
      align: "center", valign: "middle",
      fontFace: T.font.sans, fontSize: 11, bold: true,
      color: T.color.navy, margin: 0,
    });

    // Arrow 3
    slide.addShape("line", {
      x: colX[2] + boxW + 0.05, y: centerY, w: arrowW - 0.1, h: 0,
      line: { color: T.color.purple, width: 2, endArrowType: "triangle" },
    });

    // Column 4: two stacked output boxes
    const outputs = ["Dashboard", "Thursday Report"];
    const outStackH = 2 * boxH + stackGap;
    const outY0 = centerY - outStackH / 2;
    outputs.forEach((label, i) => {
      const y = outY0 + i * (boxH + stackGap);
      slide.addShape("roundRect", {
        x: colX[3], y, w: boxW, h: boxH, rectRadius: boxR,
        fill: { color: T.color.white },
        line: { color: T.color.hairline, width: 0.75 },
      });
      slide.addText(label, {
        x: colX[3], y, w: boxW, h: boxH, align: "center", valign: "middle",
        fontFace: T.font.sans, fontSize: 11, bold: true,
        color: T.color.navy, margin: 0,
      });
    });
  },
});

// ── Slide 5: What Honesty Costs ────────────────────────────────────────────────
deck.addContent({
  eyebrow: "WHAT HONESTY COSTS",
  title: "The real status distribution.",
  subtitle: "The system refuses to claim what it cannot prove.",
  draw(slide, { pptx, THEME: T }) {
    const labels = STATUS_ORDER.filter((s) => (byStatus[s] || 0) > 0);
    const values = labels.map((s) => byStatus[s] || 0);
    const colors = labels.map((s) => STATUS_COLORS[s] || T.color.label);

    // Horizontal bar chart via addChart
    slide.addChart(pptx.charts.BAR, [
      {
        name: "Features",
        labels,
        values,
      },
    ], {
      x: 1.5, y: 2.9, w: 10.5, h: 3.5,
      barDir: "bar",
      barGrouping: "clustered",
      showValue: true,
      valueBarColors: true,
      chartColors: colors,
      catAxisOrientation: "maxMin",      // top-to-bottom category order
      valAxisHidden: true,
      catAxisLabelFontSize: 11,
      catAxisLabelFontBold: true,
      catAxisLabelColor: T.color.navy,
      catAxisLabelFontFace: T.font.sans,
      catAxisLineShow: false,
      valAxisLineShow: false,
      valAxisMajorGridShow: false,
      dataLabelFontSize: 11,
      dataLabelFontBold: true,
      dataLabelFontFace: T.font.sans,
      dataLabelColor: T.color.navy,
      dataLabelPosition: "outEnd",
      showLegend: false,
      plotArea: { fill: { color: T.color.cream } },
    });

    // Caption
    const unverifiedCount = (byStatus["Unverified"] || 0) + (byStatus["Gap (unconfirmed)"] || 0);
    slide.addText(
      `${unverifiedCount} of ${total} features read Unverified or Gap (unconfirmed) — the system won't claim what it can't prove.`,
      {
        x: T.M, y: 6.6, w: 11.0, h: 0.35,
        fontFace: T.font.sans, fontSize: 10, italic: true,
        color: T.color.label, margin: 0,
      }
    );
  },
});

// ── Slide 6: Gaps That Survive Scrutiny ────────────────────────────────────────
deck.addContent({
  eyebrow: "EVIDENCED GAPS",
  title: "The gaps that survive scrutiny.",
  subtitle: `Top ${gaps.length} gaps ranked by impact × competitor pressure.`,
  draw(slide, { THEME: T }) {
    // Full-width table: 12" across the content area
    const tableW = 12.03;
    const tableX = T.M;
    const tableY = 3.0;
    // Available height: from 3.0 to ~6.5 = 3.5" for header + 8 rows + caption
    const headerH = 0.38;
    const rowCount = gaps.length || 1;
    const rowH = Math.min(0.38, (3.2 - headerH) / rowCount);  // fill vertical space
    const colW = [1.3, 6.53, 1.3, 1.4, 1.5];  // sum = 12.03

    const cellBorder = [
      { type: "solid", pt: 0.5, color: T.color.hairline },
      { type: "solid", pt: 0.5, color: T.color.hairline },
      { type: "solid", pt: 0.5, color: T.color.hairline },
      { type: "solid", pt: 0.5, color: T.color.hairline },
    ];
    const hdrStyle = {
      bold: true, fontSize: 13, fontFace: T.font.sans,
      color: "FFFFFF", fill: "5A48E8",
      valign: "middle", border: cellBorder, margin: [4, 8, 4, 8],
    };

    const headerRow = [
      { text: "ID",       options: { ...hdrStyle, align: "center" } },
      { text: "Feature",  options: { ...hdrStyle, align: "left" } },
      { text: "Impact",   options: { ...hdrStyle, align: "center" } },
      { text: "Pressure", options: { ...hdrStyle, align: "center" } },
      { text: "Priority", options: { ...hdrStyle, align: "center" } },
    ];

    const dataRows = gaps.map((g, i) => {
      const rowFill = i % 2 === 0 ? T.color.white : T.color.tintPurple;
      const base = { fontSize: 13, fontFace: T.font.sans, valign: "middle", fill: rowFill, border: cellBorder, margin: [4, 8, 4, 8] };
      return [
        { text: g.id,                      options: { ...base, color: T.color.purple, bold: true, align: "center" } },
        { text: g.name,                    options: { ...base, color: T.color.navy, align: "left" } },
        { text: String(g.impact || "—"),   options: { ...base, color: T.color.body, align: "center" } },
        { text: String(g.pressure || "—"), options: { ...base, color: T.color.body, align: "center" } },
        { text: String(g.priority || "—"), options: { ...base, color: T.color.navy, bold: true, align: "center" } },
      ];
    });

    slide.addTable([headerRow, ...dataRows], {
      x: tableX, y: tableY, w: tableW,
      colW,
      rowH: [headerH, ...Array(rowCount).fill(rowH)],
    });

    slide.addText(
      "Pressure verification in progress — ranking sharpens as evidence accumulates.",
      {
        x: T.M, y: 6.6, w: 11.0, h: 0.3,
        fontFace: T.font.sans, fontSize: 10, italic: true,
        color: T.color.label, margin: 0,
      }
    );
  },
});

// ── Slide 7: Closing ───────────────────────────────────────────────────────────
deck.addClosing({
  eyebrow: "THE ASK",
  title: "Stop asserting.",
  titleAccent: "Approve the method.",
  subtitle: "Two decisions for the CDO.",
  note:
    "1. Adopt the derived matrix as the source of truth — retire hand-typed status.\n" +
    "2. Approve the top evidenced gaps as roadmap candidates.",
});

// ── Write ──────────────────────────────────────────────────────────────────────
const outPath = path.join(__dirname, `cdo-feature-matrix-${today}.pptx`);
deck.write(outPath).then(() => {
  console.log(`Wrote ${outPath}`);
  console.log(`  ${total} features, ${conflictCount} conflicts, ${gaps.length} top gaps`);
  console.log(`  Coverage: ${covTotal} cells (${covHigh} high, ${covLow} low)`);
  console.log(`  Verified: ${Object.keys(verified).length} features`);
});
