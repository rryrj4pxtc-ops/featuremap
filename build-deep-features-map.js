#!/usr/bin/env node
// ════��══════════════════════════════════════════════════════════════════════
//  Features Map — Deep Edition
//  Full-depth Figma extraction: 2.27M nodes, 262K text layers
//  ARC Digital Experience · 2026-04-22
// ══════════════════════��════════════════════════════════════���═══════════════
const PptxGenJS = require("pptxgenjs");
const path = require("path");
const fs = require("fs");

// ── Design tokens ────────────────────────────────────────────────────────
const C = {
  brand: "0029FF", brandSoft: "E8ECFF",
  navy: "0A1F4D", navyDeep: "051233",
  ink: "141421", slate700: "334155", slate600: "475569",
  slate400: "94A3B8", slate200: "CBD5E1", slate100: "F1F4F9",
  line: "E2E8F0", white: "FFFFFF",
  critical: "DC2626", criticalSoft: "FEE2E2",
  opportunity: "D97706", opportunitySoft: "FEF3C7",
  positive: "16A34A", positiveSoft: "DCFCE7",
  insight: "4F46E5", insightSoft: "EEF2FF",
  stable: "0891B2", stableSoft: "CFFAFE",
};
const TONE = {
  critical:    { bg: C.criticalSoft, fg: C.critical },
  opportunity: { bg: C.opportunitySoft, fg: C.opportunity },
  positive:    { bg: C.positiveSoft, fg: C.positive },
  insight:     { bg: C.insightSoft, fg: C.insight },
  stable:      { bg: C.stableSoft, fg: C.stable },
  neutral:     { bg: C.slate100, fg: C.slate600 },
};
const F = { head: "Calibri", body: "Calibri", num: "Calibri" };
const W = 13.333, H = 7.5, M = 0.5;
const TP = 20;
const DATE_LABEL = "2026-04-22";
const softShadow = () => ({ type: "outer", color: "0A1F4D", blur: 12, offset: 2, angle: 90, opacity: 0.08 });

function addHeader(pres, slide, { title, eyebrow, page }) {
  slide.addText("alrajhi", {
    x: M, y: 0.32, w: 0.95, h: 0.28,
    fontFace: F.head, fontSize: 13, bold: true, color: C.brand, align: "left", margin: 0,
  });
  slide.addText("capital", {
    x: M, y: 0.56, w: 0.95, h: 0.22,
    fontFace: F.head, fontSize: 10, color: C.brand, align: "left", margin: 0,
  });
  slide.addShape(pres.shapes.LINE, { x: M + 1.15, y: 0.38, w: 0, h: 0.42, line: { color: C.line, width: 0.75 } });
  if (eyebrow) {
    slide.addText(eyebrow.toUpperCase(), {
      x: M + 1.3, y: 0.30, w: 9, h: 0.22,
      fontFace: F.body, fontSize: 8.5, bold: true, color: C.slate400, charSpacing: 3, margin: 0, align: "left",
    });
  }
  slide.addText(title, {
    x: M + 1.3, y: 0.50, w: 10, h: 0.35,
    fontFace: F.head, fontSize: 15, bold: true, color: C.ink, margin: 0, align: "left",
  });
  if (page) {
    slide.addText([
      { text: String(page).padStart(2, "0"), options: { bold: true, color: C.ink } },
      { text: `  /  ${String(TP).padStart(2, "0")}`, options: { color: C.slate400 } },
    ], { x: W - M - 1.5, y: 0.42, w: 1.5, h: 0.35, fontFace: F.body, fontSize: 10, align: "right", margin: 0 });
  }
  slide.addShape(pres.shapes.LINE, { x: M, y: 0.95, w: W - 2 * M, h: 0, line: { color: C.line, width: 0.75 } });
}

function addFooter(pres, slide, { source, dateLabel }) {
  slide.addShape(pres.shapes.LINE, { x: M, y: 7.15, w: W - 2 * M, h: 0, line: { color: C.line, width: 0.75 } });
  slide.addText(`ARC  ·  DIGITAL EXPERIENCE  ·  ${dateLabel}`, {
    x: M, y: 7.22, w: 6, h: 0.22,
    fontFace: F.body, fontSize: 8, color: C.slate400, charSpacing: 2, margin: 0, align: "left",
  });
  if (source) {
    slide.addText("Source: " + source, {
      x: W - M - 7, y: 7.22, w: 7, h: 0.22,
      fontFace: F.body, fontSize: 8, italic: true, color: C.slate400, margin: 0, align: "right",
    });
  }
}

function addTag(pres, slide, text, { x, y, w = 1.1, tone = "insight" }) {
  const t = TONE[tone] || TONE.neutral;
  slide.addShape(pres.shapes.ROUNDED_RECTANGLE, {
    x, y, w, h: 0.26, fill: { color: t.bg }, line: { width: 0 }, rectRadius: 0.03,
  });
  slide.addText(text, {
    x, y, w, h: 0.26, fontFace: F.body, fontSize: 8, bold: true, color: t.fg,
    charSpacing: 1, align: "center", valign: "middle", margin: 0,
  });
}

function card(pres, slide, { x, y, w, h, fill = C.white }) {
  slide.addShape(pres.shapes.ROUNDED_RECTANGLE, {
    x, y, w, h, fill: { color: fill }, line: { color: C.line, width: 0.5 }, rectRadius: 0.08, shadow: softShadow(),
  });
}

function hBar(pres, slide, { x, y, w, h, pct, color, bgColor = C.slate100 }) {
  slide.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y, w, h, fill: { color: bgColor }, line: { width: 0 }, rectRadius: h / 2 });
  if (pct > 0) {
    slide.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y, w: Math.max(w * pct, h), h, fill: { color }, line: { width: 0 }, rectRadius: h / 2 });
  }
}

// ══════════════════════════════════════════════════════════════════════════
//  DATA — From full-depth extraction
// ══════════════════════════════════════════════════════════════════════════
const MODULES = [
  { name: "OnBoarding KYC", nodes: 295977, pages: 6, screens: 23365, texts: 13530, instances: 17638, modified: "2026-04-21", newPages: ["Fast Onboarding", "First Engagement", "Guest Mode", "Tutorials"] },
  { name: "Home", nodes: 291291, pages: 3, screens: 44604, texts: 38834, instances: 28745, modified: "2026-04-15", newPages: ["Ramadan"] },
  { name: "Tradepad", nodes: 166739, pages: 2, screens: 34823, texts: 32527, instances: 30717, modified: "2026-03-28", newPages: [] },
  { name: "Market", nodes: 406991, pages: 2, screens: 100283, texts: 73645, instances: 62116, modified: "2026-04-21", newPages: [] },
  { name: "Portfolios", nodes: 240353, pages: 5, screens: 44460, texts: 28785, instances: 32124, modified: "2026-04-14", newPages: ["Digital StoryTeller"] },
  { name: "Discover (IPO)", nodes: 427474, pages: 2, screens: 48758, texts: 33706, instances: 30785, modified: "2026-04-20", newPages: ["Discover & Search"] },
  { name: "Profile & Setting", nodes: 230352, pages: 2, screens: 20524, texts: 14758, instances: 18812, modified: "2026-04-15", newPages: [] },
  { name: "Orders", nodes: 210397, pages: 2, screens: 29401, texts: 26253, instances: 25322, modified: "2026-03-26", newPages: [] },
];

const PLATFORM_PARITY = [
  { name: "OnBoarding KYC", mobile: true, web: true, tablet: true },
  { name: "Home", mobile: true, web: true, tablet: true },
  { name: "Tradepad", mobile: true, web: true, tablet: true },
  { name: "Market", mobile: true, web: true, tablet: true },
  { name: "Portfolios", mobile: true, web: true, tablet: true },
  { name: "Discover (IPO)", mobile: true, web: true, tablet: true },
  { name: "Profile & Setting", mobile: true, web: true, tablet: true },
  { name: "Orders", mobile: true, web: true, tablet: true },
];

const SQUADS = [
  { name: "Onboarding", live: 4, planned: 9, figmaOnly: 11, brdOnly: 1, brdFigma: 12, total: 24, gapCount: 3, topGap: "Onboarding checklist", gapScore: null },
  { name: "Saudi Trading", live: 6, planned: 19, figmaOnly: 14, brdOnly: 19, brdFigma: 7, total: 39, gapCount: 11, topGap: "Level 2 Order Book", gapScore: 25 },
  { name: "US Trading", live: 3, planned: 6, figmaOnly: 1, brdOnly: 6, brdFigma: 3, total: 10, gapCount: 15, topGap: "Pre/Post-Market Trading", gapScore: 25 },
  { name: "Portfolio Monitoring", live: 2, planned: 9, figmaOnly: 11, brdOnly: 4, brdFigma: 7, total: 22, gapCount: 4, topGap: "Gain/Loss Tax Report", gapScore: 20 },
  { name: "Wealth Visibility", live: 1, planned: 4, figmaOnly: 0, brdOnly: 4, brdFigma: 1, total: 5, gapCount: 1, topGap: "Apple Pay Funding", gapScore: null },
  { name: "Mutual Funds", live: 1, planned: 9, figmaOnly: 1, brdOnly: 6, brdFigma: 4, total: 11, gapCount: 5, topGap: "Private Funds Access", gapScore: 20 },
  { name: "Robo Advisory", live: 1, planned: 2, figmaOnly: 1, brdOnly: 0, brdFigma: 3, total: 4, gapCount: 4, topGap: "Goal-Based Portfolio", gapScore: 15 },
  { name: "IPOs", live: 2, planned: 4, figmaOnly: 1, brdOnly: 3, brdFigma: 3, total: 7, gapCount: 2, topGap: "US Market IPO", gapScore: null },
  { name: "Corporate Actions", live: 0, planned: 3, figmaOnly: 1, brdOnly: 2, brdFigma: 1, total: 4, gapCount: 1, topGap: "Rights Issue Digital", gapScore: null },
  { name: "Investor Engagement", live: 2, planned: 10, figmaOnly: 4, brdOnly: 11, brdFigma: 1, total: 16, gapCount: 3, topGap: "Social Community Feed", gapScore: 20 },
  { name: "Cross-Journey", live: 2, planned: 12, figmaOnly: 7, brdOnly: 13, brdFigma: 2, total: 22, gapCount: 1, topGap: "Price Alert System", gapScore: 16 },
];

const TOP_GAPS = [
  { rank: 1, name: "Level 2 Market Depth / Order Book", score: 25, squad: "Saudi / US Trading", status: "No Figma, No BRD" },
  { rank: 2, name: "Stock Screener", score: 25, squad: "Saudi / US Trading", status: "FOUND IN FIGMA — Market file" },
  { rank: 3, name: "Pre/Post-Market Trading (US)", score: 25, squad: "US Trading", status: "No Figma, No BRD" },
  { rank: 4, name: "Advanced Technical Analysis Suite", score: 25, squad: "Saudi / US Trading", status: "TradingView integration exists" },
  { rank: 5, name: "Stock Comparison Tool", score: 20, squad: "Saudi / US Trading", status: "No Figma, No BRD" },
  { rank: 6, name: "AI-Powered Assistant / AI Chat", score: 20, squad: "Cross-Journey", status: "No Figma, No BRD" },
  { rank: 7, name: "Paper Trading / Simulated Mode", score: 20, squad: "Cross-Journey", status: "No Figma, No BRD" },
  { rank: 8, name: "Fractional Shares (US)", score: 20, squad: "US Trading", status: "No Figma, No BRD" },
  { rank: 9, name: "Social / Community Feed", score: 20, squad: "Investor Engagement", status: "No Figma, No BRD" },
  { rank: 10, name: "Conditional Orders — Full BRD", score: 20, squad: "Saudi Trading", status: "Figma screens exist (no BRD)" },
  { rank: 11, name: "Personalized Events Calendar", score: 20, squad: "Saudi / US Trading", status: "No Figma, No BRD" },
  { rank: 12, name: "Private Funds / PE Access", score: 20, squad: "Mutual Funds", status: "No Figma, No BRD" },
];

const DISCOVERIES = [
  { feature: "Stock Screener", file: "Market", evidence: "Text label 'Stock Screener' found in Market page", impact: "Gap #2 (score 25/25) may be closing — design has started", tone: "positive" },
  { feature: "UAE Market", file: "Market + Orders", evidence: "Text labels 'UAE Market', 'UAE market' in Market; 'UAE Market Stocks' in Orders", impact: "New 3rd market beyond Saudi and US — not in current features inventory", tone: "opportunity" },
  { feature: "Guest Mode (Web)", file: "OnBoarding KYC", evidence: "Full page with 21 frames + Market Landscape + Benchmark Analysis screens", impact: "Guest Mode designed for Web (not just mobile) — more extensive than BRD scope", tone: "insight" },
  { feature: "Fast Onboarding", file: "OnBoarding KYC", evidence: "New page with 364 sub-frames — streamlined account opening flow", impact: "Simplified KYC variant not in features inventory — could address 87% drop-off", tone: "positive" },
  { feature: "Digital StoryTeller", file: "Portfolios", evidence: "Dedicated page with narrative investment report screens", impact: "Feature #76 (Storyteller) has active Figma work — can be moved to 'Ready to Build'", tone: "positive" },
  { feature: "First Engagement Flow", file: "OnBoarding KYC", evidence: "Dedicated page '1st Login Engagement' with 225+ nodes", impact: "Post-onboarding activation flow — not in current features inventory", tone: "opportunity" },
  { feature: "Ramadan Theme", file: "Home", evidence: "Dedicated 'Ramadan' page in Home file", impact: "Seasonal theming capability — engagement opportunity during Ramadan", tone: "insight" },
  { feature: "Crowd Fund", file: "Multiple", evidence: "Text labels across Home, Market, Orders for Crowd Fund/Crowd Funds", impact: "Crowdfunding product is being designed across multiple modules — more mature than inventory suggests", tone: "opportunity" },
  { feature: "Murabha (Margin) in Discover", file: "Discover (IPO)", evidence: "Text label 'Murabha' in Discover & Search page", impact: "Margin lending discoverable from Discover — cross-module navigation", tone: "insight" },
  { feature: "Power of Attorney (POA)", file: "Discover (IPO)", evidence: "Text labels 'POA', 'Power of Attorney Request' in Discover", impact: "POA flow designed but not in features inventory — needs BRD", tone: "opportunity" },
];

// ══════════════════════════════════════════════════════════════════════════
//  BUILD
// ══════════════════════════════════════════════════════════════════════════
const pres = new PptxGenJS();
pres.defineLayout({ name: "WIDE", width: W, height: H });
pres.layout = "WIDE";

// ── SLIDE 1: COVER ──────────────────────────────────────────────────────
{
  const s = pres.addSlide();
  s.background = { fill: C.navyDeep };
  s.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: 0.06, h: H, fill: { color: C.brand } });

  s.addText("alrajhi capital", {
    x: M + 0.3, y: 0.6, w: 4, h: 0.35,
    fontFace: F.head, fontSize: 14, bold: true, color: C.brand, margin: 0,
  });

  s.addText("ARC Features Map", {
    x: M + 0.3, y: 1.6, w: 10, h: 0.8,
    fontFace: F.head, fontSize: 36, bold: true, color: C.white, margin: 0,
  });
  s.addText("Deep Edition — Full Figma Extraction", {
    x: M + 0.3, y: 2.35, w: 10, h: 0.4,
    fontFace: F.head, fontSize: 18, color: C.brand, margin: 0,
  });
  s.addText("164 features  ·  62 gaps  ·  14 differentiators  ·  2.27M design nodes analyzed", {
    x: M + 0.3, y: 2.85, w: 10, h: 0.35,
    fontFace: F.body, fontSize: 12, color: C.slate400, margin: 0,
  });

  // Key metrics
  const metrics = [
    { num: "2.27M", label: "DESIGN\nNODES" },
    { num: "262K", label: "TEXT\nLAYERS" },
    { num: "246K", label: "COMPONENT\nINSTANCES" },
    { num: "8/8", label: "PLATFORM\n3/3 PARITY" },
    { num: "10", label: "NEW FEATURES\nDISCOVERED" },
  ];
  const mw = 2.1, mx = M + 0.3;
  metrics.forEach((m, i) => {
    const bx = mx + i * (mw + 0.3);
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, {
      x: bx, y: 3.8, w: mw, h: 1.3,
      fill: { color: "0D1B3C" }, line: { color: "1A2D5A", width: 0.5 }, rectRadius: 0.08,
    });
    s.addText(m.num, {
      x: bx, y: 3.9, w: mw, h: 0.6,
      fontFace: F.num, fontSize: 26, bold: true, color: C.brand, align: "center", margin: 0,
    });
    s.addText(m.label, {
      x: bx, y: 4.5, w: mw, h: 0.5,
      fontFace: F.body, fontSize: 8.5, color: C.slate400, align: "center", margin: 0, lineSpacingMultiple: 1.1,
    });
  });

  s.addText("Full-depth extraction from 8 Figma design files  ·  Figma REST API  ·  " + DATE_LABEL, {
    x: M + 0.3, y: 5.6, w: 11, h: 0.25,
    fontFace: F.body, fontSize: 9, italic: true, color: C.slate400, margin: 0,
  });

  s.addText("Digital Experience Department  ·  Al Rajhi Capital", {
    x: M + 0.3, y: 6.5, w: 10, h: 0.25,
    fontFace: F.body, fontSize: 10, color: C.slate200, margin: 0,
  });
}

// ── SLIDE 2: EXTRACTION OVERVIEW ────────────────────────────────────────
{
  const s = pres.addSlide();
  s.background = { fill: C.white };
  addHeader(pres, s, { title: "Deep Extraction Overview — 2.27M Nodes", eyebrow: "FIGMA ANALYSIS", page: 2 });

  // File detail table
  const cols = ["Module", "Nodes", "Pages", "Text Layers", "Instances", "Last Modified"];
  const colW = [2.2, 1.2, 0.7, 1.2, 1.2, 1.5];
  const tX = M, tY = 1.2, rowH = 0.4;

  cols.forEach((c, i) => {
    let cx = tX; for (let j = 0; j < i; j++) cx += colW[j];
    s.addShape(pres.shapes.RECTANGLE, { x: cx, y: tY, w: colW[i], h: rowH, fill: { color: C.navy }, line: { width: 0 } });
    s.addText(c, { x: cx + 0.08, y: tY, w: colW[i] - 0.16, h: rowH, fontFace: F.body, fontSize: 8.5, bold: true, color: C.white, margin: 0, align: i === 0 ? "left" : "center", valign: "middle" });
  });

  const totalNodes = MODULES.reduce((s, m) => s + m.nodes, 0);
  MODULES.forEach((mod, ri) => {
    const ry = tY + rowH + ri * rowH;
    const bg = ri % 2 === 0 ? C.white : C.slate100;
    const vals = [mod.name, mod.nodes.toLocaleString(), mod.pages, mod.texts.toLocaleString(), mod.instances.toLocaleString(), mod.modified];
    vals.forEach((v, ci) => {
      let cx = tX; for (let j = 0; j < ci; j++) cx += colW[j];
      s.addShape(pres.shapes.RECTANGLE, { x: cx, y: ry, w: colW[ci], h: rowH, fill: { color: bg }, line: { color: C.line, width: 0.25 } });
      const fc = ci === 1 ? C.brand : C.ink;
      s.addText(String(v), { x: cx + 0.08, y: ry, w: colW[ci] - 0.16, h: rowH, fontFace: ci === 0 ? F.body : F.num, fontSize: 9, bold: ci <= 1, color: fc, margin: 0, align: ci === 0 ? "left" : "center", valign: "middle" });
    });
  });

  // Right side: node size visualization
  const vizX = 8.5;
  s.addText("Design Complexity", {
    x: vizX, y: 1.2, w: 4, h: 0.3,
    fontFace: F.head, fontSize: 11, bold: true, color: C.ink, margin: 0,
  });
  const maxNodes = 406991;
  MODULES.forEach((mod, i) => {
    const ry = 1.6 + i * 0.48;
    const pct = mod.nodes / maxNodes;
    s.addText(mod.name.split(" ")[0], {
      x: vizX, y: ry, w: 1.2, h: 0.35,
      fontFace: F.body, fontSize: 8, color: C.slate700, margin: 0, align: "right", valign: "middle",
    });
    hBar(pres, s, { x: vizX + 1.3, y: ry + 0.08, w: 3, h: 0.2, pct, color: C.brand });
    s.addText((mod.nodes / 1000).toFixed(0) + "K", {
      x: vizX + 1.3 + 3 * pct + 0.1, y: ry, w: 0.8, h: 0.35,
      fontFace: F.num, fontSize: 8, bold: true, color: C.brand, margin: 0, valign: "middle",
    });
  });

  // Bottom insight
  card(pres, s, { x: M, y: 5.7, w: W - 2 * M, h: 1.1, fill: C.insightSoft });
  addTag(pres, s, "KEY FINDING", { x: M + 0.2, y: 5.8, w: 1.1, tone: "insight" });
  s.addText([
    { text: "Market is the most complex module", options: { bold: true } },
    { text: " (407K nodes, 74K text layers) — followed by Discover (427K nodes). The revamp design effort is heavily concentrated in trading and discovery experiences. ", options: {} },
    { text: "4 new pages discovered", options: { bold: true } },
    { text: " in OnBoarding alone: Fast Onboarding, Guest Mode, Tutorials, and First Engagement — none of which were in the original features inventory.", options: {} },
  ], {
    x: M + 1.5, y: 5.78, w: 10.5, h: 0.95,
    fontFace: F.body, fontSize: 9, color: C.slate700, margin: 0, valign: "middle",
  });

  addFooter(pres, s, { source: "Figma REST API · Full-depth extraction · 8 files · " + DATE_LABEL, dateLabel: DATE_LABEL });
}

// ── SLIDE 3: PLATFORM PARITY MATRIX ─────────────────────────────────────
{
  const s = pres.addSlide();
  s.background = { fill: C.white };
  addHeader(pres, s, { title: "Platform Parity — All 8 Modules at Full Coverage", eyebrow: "PLATFORM ANALYSIS", page: 3 });

  // Big reveal
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, {
    x: M, y: 1.2, w: W - 2*M, h: 1.3,
    fill: { color: C.positiveSoft }, line: { color: C.positive, width: 1 }, rectRadius: 0.1,
  });
  s.addText("8 / 8", {
    x: M + 0.3, y: 1.25, w: 2, h: 1.2,
    fontFace: F.num, fontSize: 48, bold: true, color: C.positive, margin: 0, align: "center", valign: "middle",
  });
  s.addText("All 8 Figma files contain Mobile, Web, and Tablet designs", {
    x: M + 2.5, y: 1.35, w: 8, h: 0.4,
    fontFace: F.head, fontSize: 16, bold: true, color: C.positive, margin: 0,
  });
  s.addText("The unreleased revamp is designed as a fully responsive platform from day one. This is a significant finding — the previous assumption was that tablet coverage was incomplete.", {
    x: M + 2.5, y: 1.8, w: 9, h: 0.5,
    fontFace: F.body, fontSize: 10, color: C.slate700, margin: 0,
  });

  // Parity grid
  const gridY = 2.8;
  const gridH = 0.5;
  const platforms = ["Mobile", "Web", "Tablet"];
  const platformColors = { Mobile: C.brand, Web: C.insight, Tablet: C.stable };
  // Header
  s.addText("Module", {
    x: M, y: gridY, w: 2.5, h: gridH,
    fontFace: F.body, fontSize: 9, bold: true, color: C.white, margin: [0, 8], valign: "middle",
    fill: { color: C.navy },
  });
  platforms.forEach((p, i) => {
    s.addText(p, {
      x: M + 2.5 + i * 1.5, y: gridY, w: 1.5, h: gridH,
      fontFace: F.body, fontSize: 9, bold: true, color: C.white, margin: 0, align: "center", valign: "middle",
      fill: { color: platformColors[p] },
    });
  });
  s.addText("Coverage", {
    x: M + 7, y: gridY, w: 1.2, h: gridH,
    fontFace: F.body, fontSize: 9, bold: true, color: C.white, margin: 0, align: "center", valign: "middle",
    fill: { color: C.navy },
  });

  PLATFORM_PARITY.forEach((pp, i) => {
    const ry = gridY + gridH + i * 0.42;
    const bg = i % 2 === 0 ? C.white : C.slate100;
    s.addShape(pres.shapes.RECTANGLE, { x: M, y: ry, w: 2.5, h: 0.42, fill: { color: bg }, line: { color: C.line, width: 0.25 } });
    s.addText(pp.name, {
      x: M + 0.1, y: ry, w: 2.3, h: 0.42,
      fontFace: F.body, fontSize: 9, bold: true, color: C.ink, margin: 0, valign: "middle",
    });
    [pp.mobile, pp.web, pp.tablet].forEach((has, pi) => {
      const cx = M + 2.5 + pi * 1.5;
      s.addShape(pres.shapes.RECTANGLE, { x: cx, y: ry, w: 1.5, h: 0.42, fill: { color: bg }, line: { color: C.line, width: 0.25 } });
      s.addShape(pres.shapes.ROUNDED_RECTANGLE, {
        x: cx + 0.55, y: ry + 0.08, w: 0.4, h: 0.26,
        fill: { color: has ? C.positive : C.critical }, line: { width: 0 }, rectRadius: 0.04,
      });
      s.addText(has ? "YES" : "NO", {
        x: cx + 0.55, y: ry + 0.08, w: 0.4, h: 0.26,
        fontFace: F.body, fontSize: 7, bold: true, color: C.white, align: "center", valign: "middle", margin: 0,
      });
    });
    s.addShape(pres.shapes.RECTANGLE, { x: M + 7, y: ry, w: 1.2, h: 0.42, fill: { color: C.positiveSoft }, line: { color: C.line, width: 0.25 } });
    s.addText("3/3", {
      x: M + 7, y: ry, w: 1.2, h: 0.42,
      fontFace: F.num, fontSize: 10, bold: true, color: C.positive, align: "center", valign: "middle", margin: 0,
    });
  });

  // Right side: platform design volume
  const rxBase = 9;
  card(pres, s, { x: rxBase, y: 2.8, w: 3.8, h: 3.8 });
  s.addText("Design Volume by Platform", {
    x: rxBase + 0.2, y: 2.9, w: 3.4, h: 0.3,
    fontFace: F.head, fontSize: 10, bold: true, color: C.ink, margin: 0,
  });

  const platVols = [
    { name: "Mobile", count: 334500, pct: 96.6, color: C.brand },
    { name: "Web", count: 5150, pct: 1.5, color: C.insight },
    { name: "Tablet", count: 6568, pct: 1.9, color: C.stable },
  ];
  platVols.forEach((pv, i) => {
    const py = 3.4 + i * 0.9;
    s.addText(pv.name, {
      x: rxBase + 0.3, y: py, w: 1.5, h: 0.25,
      fontFace: F.body, fontSize: 10, bold: true, color: pv.color, margin: 0,
    });
    s.addText(pv.count.toLocaleString() + " frames", {
      x: rxBase + 0.3, y: py + 0.28, w: 2, h: 0.2,
      fontFace: F.num, fontSize: 9, color: C.slate600, margin: 0,
    });
    hBar(pres, s, { x: rxBase + 0.3, y: py + 0.55, w: 3.2, h: 0.16, pct: pv.pct / 100, color: pv.color });
  });

  card(pres, s, { x: M, y: 6.3, w: W - 2*M, h: 0.55, fill: C.insightSoft });
  addTag(pres, s, "INSIGHT", { x: M + 0.2, y: 6.37, w: 0.9, tone: "insight" });
  s.addText("Mobile-first design strategy confirmed: 96.6% of design frames are mobile. Web and Tablet layouts reuse mobile components via responsive adaptation rather than separate designs.", {
    x: M + 1.3, y: 6.33, w: 11, h: 0.48,
    fontFace: F.body, fontSize: 9, color: C.slate700, margin: 0, valign: "middle",
  });

  addFooter(pres, s, { source: "Figma REST API · Full-depth extraction · Platform frame analysis", dateLabel: DATE_LABEL });
}

// ── SLIDE 4: NEW DISCOVERIES ─────���──────────────────────────────────────
{
  const s = pres.addSlide();
  s.background = { fill: C.white };
  addHeader(pres, s, { title: "10 Features Discovered in Deep Extraction", eyebrow: "NEW FINDINGS", page: 4 });

  DISCOVERIES.forEach((d, i) => {
    const col = i % 2;
    const row = Math.floor(i / 2);
    const cx = M + col * 6.3;
    const cy = 1.15 + row * 1.15;
    const cw = 6;
    const ch = 1.05;

    card(pres, s, { x: cx, y: cy, w: cw, h: ch });
    addTag(pres, s, d.file.split(" ")[0].toUpperCase(), { x: cx + 0.12, y: cy + 0.08, w: 1.2, tone: d.tone });
    s.addText(d.feature, {
      x: cx + 1.45, y: cy + 0.05, w: cw - 1.65, h: 0.25,
      fontFace: F.body, fontSize: 10, bold: true, color: C.ink, margin: 0,
    });
    s.addText(d.evidence, {
      x: cx + 0.15, y: cy + 0.35, w: cw - 0.3, h: 0.25,
      fontFace: F.body, fontSize: 8, italic: true, color: C.slate600, margin: 0,
    });
    s.addText(d.impact, {
      x: cx + 0.15, y: cy + 0.62, w: cw - 0.3, h: 0.35,
      fontFace: F.body, fontSize: 8.5, color: C.slate700, margin: 0,
    });
  });

  addFooter(pres, s, { source: "Figma REST API · Full-depth text layer extraction · " + DATE_LABEL, dateLabel: DATE_LABEL });
}

// ── SLIDE 5: GAP STATUS UPDATE ──────────────────────────────────────────
{
  const s = pres.addSlide();
  s.background = { fill: C.white };
  addHeader(pres, s, { title: "Top 12 Gaps — Status After Deep Extraction", eyebrow: "COMPETITIVE INTELLIGENCE", page: 5 });

  const tY = 1.15, rowH = 0.41;
  const gCols = ["#", "Gap Feature", "Score", "Squad", "Figma Status"];
  const gColW = [0.35, 3.2, 0.6, 2, 6.2];

  gCols.forEach((c, i) => {
    let cx = M; for (let j = 0; j < i; j++) cx += gColW[j];
    s.addShape(pres.shapes.RECTANGLE, { x: cx, y: tY, w: gColW[i], h: rowH, fill: { color: C.navy }, line: { width: 0 } });
    s.addText(c, { x: cx + 0.06, y: tY, w: gColW[i] - 0.12, h: rowH, fontFace: F.body, fontSize: 8.5, bold: true, color: C.white, margin: 0, align: i <= 1 ? "left" : (i === 2 ? "center" : "left"), valign: "middle" });
  });

  TOP_GAPS.forEach((g, ri) => {
    const ry = tY + rowH + ri * rowH;
    const isFound = g.status.includes("FOUND");
    const isFigma = g.status.includes("Figma");
    const bg = isFound ? C.positiveSoft : (isFigma ? C.opportunitySoft : (ri % 2 === 0 ? C.white : C.slate100));
    const vals = [g.rank, g.name, g.score, g.squad, g.status];

    vals.forEach((v, ci) => {
      let cx = M; for (let j = 0; j < ci; j++) cx += gColW[j];
      s.addShape(pres.shapes.RECTANGLE, { x: cx, y: ry, w: gColW[ci], h: rowH, fill: { color: bg }, line: { color: C.line, width: 0.25 } });
      let fc = C.ink;
      if (ci === 2) fc = g.score === 25 ? C.critical : C.opportunity;
      if (ci === 4 && isFound) fc = C.positive;
      if (ci === 4 && isFigma && !isFound) fc = C.opportunity;
      if (ci === 4 && !isFigma && !isFound) fc = C.critical;
      s.addText(String(v), { x: cx + 0.06, y: ry, w: gColW[ci] - 0.12, h: rowH, fontFace: ci === 0 || ci === 2 ? F.num : F.body, fontSize: 8.5, bold: ci <= 2 || (ci === 4 && isFound), color: fc, margin: 0, align: ci <= 1 ? "left" : (ci === 2 ? "center" : "left"), valign: "middle" });
    });
  });

  const bY = tY + rowH + TOP_GAPS.length * rowH + 0.2;
  card(pres, s, { x: M, y: bY, w: W - 2*M, h: 0.75, fill: C.positiveSoft });
  addTag(pres, s, "BREAKTHROUGH", { x: M + 0.2, y: bY + 0.08, w: 1.3, tone: "positive" });
  s.addText([
    { text: "Stock Screener (Gap #2, score 25/25) found in Market Figma file", options: { bold: true } },
    { text: " — the design team has already started work on this critical gap. Additionally, Conditional Orders (#10) have Figma screens. 2 of the top 12 gaps show design progress.", options: {} },
  ], {
    x: M + 1.7, y: bY + 0.02, w: 10.5, h: 0.7,
    fontFace: F.body, fontSize: 9, color: C.slate700, margin: 0, valign: "middle",
  });

  addFooter(pres, s, { source: "Competitor Gap Matrix + Figma full-depth text layer scan", dateLabel: DATE_LABEL });
}

// ── SLIDE 6: SQUAD HEATMAP (same as before but updated) ─────────────────
{
  const s = pres.addSlide();
  s.background = { fill: C.white };
  addHeader(pres, s, { title: "Feature Coverage by Squad", eyebrow: "FEATURES MAP", page: 6 });

  const cols = ["Squad", "Total", "Live", "BRD+Figma", "BRD Only", "Figma Only", "Gaps", "Coverage"];
  const colW = [2.2, 0.55, 0.5, 0.85, 0.8, 0.8, 0.55, 6.1];
  const tY = 1.15, rowH = 0.42;

  cols.forEach((c, i) => {
    let cx = M; for (let j = 0; j < i; j++) cx += colW[j];
    s.addShape(pres.shapes.RECTANGLE, { x: cx, y: tY, w: colW[i], h: rowH, fill: { color: C.navy }, line: { width: 0 } });
    s.addText(c, { x: cx + 0.06, y: tY, w: colW[i] - 0.12, h: rowH, fontFace: F.body, fontSize: 8, bold: true, color: C.white, margin: 0, align: i === 0 ? "left" : (i === 7 ? "left" : "center"), valign: "middle" });
  });

  SQUADS.forEach((sq, ri) => {
    const ry = tY + rowH + ri * rowH;
    const bg = ri % 2 === 0 ? C.white : C.slate100;
    const vals = [sq.name, sq.total, sq.live, sq.brdFigma, sq.brdOnly, sq.figmaOnly, sq.gapCount];

    vals.forEach((v, ci) => {
      let cx = M; for (let j = 0; j < ci; j++) cx += colW[j];
      s.addShape(pres.shapes.RECTANGLE, { x: cx, y: ry, w: colW[ci], h: rowH, fill: { color: bg }, line: { color: C.line, width: 0.25 } });
      let fc = C.ink;
      if (ci === 2) fc = C.positive;
      if (ci === 5) fc = C.critical;
      if (ci === 6) fc = C.critical;
      s.addText(String(v), { x: cx + 0.06, y: ry, w: colW[ci] - 0.12, h: rowH, fontFace: ci === 0 ? F.body : F.num, fontSize: ci === 0 ? 9 : 9.5, bold: ci <= 1, color: fc, margin: 0, align: ci === 0 ? "left" : "center", valign: "middle" });
    });

    // Stacked bar in last column
    let cx = M; for (let j = 0; j < 7; j++) cx += colW[j];
    s.addShape(pres.shapes.RECTANGLE, { x: cx, y: ry, w: colW[7], h: rowH, fill: { color: bg }, line: { color: C.line, width: 0.25 } });
    const barX = cx + 0.12, barW = colW[7] - 0.24, barY = ry + 0.11, barH = 0.2;
    const segments = [
      { count: sq.live, color: C.positive },
      { count: Math.max(0, sq.brdFigma - sq.live), color: C.stable },
      { count: sq.brdOnly, color: C.insight },
      { count: sq.figmaOnly, color: C.critical },
    ];
    let offset = 0;
    segments.forEach(seg => {
      if (seg.count > 0) {
        const segW = (seg.count / sq.total) * barW;
        s.addShape(pres.shapes.RECTANGLE, { x: barX + offset, y: barY, w: segW, h: barH, fill: { color: seg.color }, line: { width: 0 } });
        offset += segW;
      }
    });
    if (offset < barW) {
      s.addShape(pres.shapes.RECTANGLE, { x: barX + offset, y: barY, w: barW - offset, h: barH, fill: { color: C.slate200 }, line: { width: 0 } });
    }
  });

  // Legend
  const legY = tY + rowH + SQUADS.length * rowH + 0.2;
  [
    { label: "Live", color: C.positive },
    { label: "BRD + Figma", color: C.stable },
    { label: "BRD Only", color: C.insight },
    { label: "Figma Only", color: C.critical },
  ].forEach((l, i) => {
    const lx = M + i * 2.5;
    s.addShape(pres.shapes.RECTANGLE, { x: lx, y: legY + 0.05, w: 0.18, h: 0.18, fill: { color: l.color }, line: { width: 0 } });
    s.addText(l.label, { x: lx + 0.25, y: legY, w: 1.5, h: 0.28, fontFace: F.body, fontSize: 8.5, color: C.slate700, margin: 0, valign: "middle" });
  });

  addFooter(pres, s, { source: "Features Inventory (164 features) · 100+ BRDs + Figma API + Deep Extraction", dateLabel: DATE_LABEL });
}

// ── SLIDE 7: DIFFERENTIATORS ────────────────────────────────────────────
{
  const s = pres.addSlide();
  s.background = { fill: C.white };
  addHeader(pres, s, { title: "ARC Differentiators — 14 Non-Replicable Advantages", eyebrow: "COMPETITIVE POSITION", page: 7 });

  const diffs = [
    { name: "Murabaha Margin Lending", desc: "Sharia-compliant digital margin — no comparable competitor product" },
    { name: "Purification & Zakat", desc: "Religious compliance calculators not offered by any competitor" },
    { name: "Minor Account + Guardian", desc: "Granular custodian controls unseen in Saudi retail" },
    { name: "Mokafaa + ARG Bundles", desc: "Ecosystem-exclusive loyalty architecture" },
    { name: "Storyteller (Narrative)", desc: "Personalized quarterly investment narrative" },
    { name: "Shariah Multi-List", desc: "General + ARC-specific Shariah lists" },
    { name: "Peer Portfolio Compare", desc: "Anonymized peer P&L benchmarking" },
    { name: "Portfolio Health Score", desc: "Composite quality score not in any benchmark" },
    { name: "SBL Program", desc: "Full SBL with Sharia margin integration" },
    { name: "Gift Campaigns (UCM)", desc: "Date-specific UCM gift campaigns" },
    { name: "Tadawulaty SSO", desc: "Direct Edaa single sign-on" },
    { name: "ZATCA E-Invoices", desc: "Auto e-invoices for wallet + purification" },
  ];

  const cardW = 2.9, cardH = 0.8, gapX = 0.2, gapY = 0.15;
  const cols = 4;
  diffs.forEach((d, i) => {
    const col = i % cols;
    const row = Math.floor(i / cols);
    const cx = M + col * (cardW + gapX);
    const cy = 1.2 + row * (cardH + gapY);

    card(pres, s, { x: cx, y: cy, w: cardW, h: cardH, fill: C.positiveSoft });
    s.addText(`D-${String(i + 1).padStart(2, "0")}  ${d.name}`, {
      x: cx + 0.1, y: cy + 0.08, w: cardW - 0.2, h: 0.28,
      fontFace: F.body, fontSize: 8.5, bold: true, color: C.positive, margin: 0,
    });
    s.addText(d.desc, {
      x: cx + 0.1, y: cy + 0.38, w: cardW - 0.2, h: 0.35,
      fontFace: F.body, fontSize: 7.5, color: C.slate700, margin: 0,
    });
  });

  card(pres, s, { x: M, y: 4.3, w: W - 2*M, h: 0.55, fill: C.positiveSoft });
  addTag(pres, s, "MOAT", { x: M + 0.2, y: 4.37, w: 0.7, tone: "positive" });
  s.addText("ARC's competitive moat is Sharia-first infrastructure + Al Rajhi ecosystem. These 14 differentiators are structurally non-replicable by standalone fintech competitors.", {
    x: M + 1.1, y: 4.33, w: 11, h: 0.48,
    fontFace: F.body, fontSize: 9, color: C.slate700, margin: 0, valign: "middle",
  });

  addFooter(pres, s, { source: "Competitor Gap Matrix · 10+ benchmarks", dateLabel: DATE_LABEL });
}

// ── SLIDE 8: FEATURE READINESS MATRIX ───────────────────────────────────
{
  const s = pres.addSlide();
  s.background = { fill: C.white };
  addHeader(pres, s, { title: "Feature Readiness Matrix", eyebrow: "PLATFORM READINESS", page: 8 });

  const qX = M + 1.5, qY = 1.3, qW = 5, qH = 5;
  const quads = [
    { x: qX, y: qY, label: "BRD ONLY\n(68 features)", count: 68, color: C.insightSoft, txtColor: C.insight, desc: "Need Figma" },
    { x: qX + qW/2, y: qY, label: "READY TO BUILD\n(44 features)", count: 44, color: C.positiveSoft, txtColor: C.positive, desc: "BRD + Figma" },
    { x: qX, y: qY + qH/2, label: "UNDOCUMENTED\n(1 feature)", count: 1, color: C.slate100, txtColor: C.slate600, desc: "Unknown" },
    { x: qX + qW/2, y: qY + qH/2, label: "FIGMA ONLY\n(42 features)", count: 42, color: C.criticalSoft, txtColor: C.critical, desc: "Need BRD" },
  ];

  quads.forEach(q => {
    s.addShape(pres.shapes.RECTANGLE, { x: q.x, y: q.y, w: qW/2, h: qH/2, fill: { color: q.color }, line: { color: C.line, width: 0.5 } });
    s.addText(String(q.count), { x: q.x, y: q.y + 0.3, w: qW/2, h: 0.8, fontFace: F.num, fontSize: 42, bold: true, color: q.txtColor, align: "center", margin: 0, transparency: 20 });
    s.addText(q.label, { x: q.x, y: q.y + qH/4 - 0.3, w: qW/2, h: 0.6, fontFace: F.body, fontSize: 9, color: q.txtColor, align: "center", margin: 0 });
  });

  // Right panel
  const rX = 7.5;
  card(pres, s, { x: rX, y: 1.3, w: 5.3, h: 5.2 });
  s.addText("Action Plan", { x: rX + 0.2, y: 1.4, w: 4, h: 0.3, fontFace: F.head, fontSize: 12, bold: true, color: C.ink, margin: 0 });

  const actions = [
    { num: "44", label: "Ready to Build", desc: "BRD + Figma confirmed. 24 are live, 20 more can enter sprint planning today.", color: C.positive },
    { num: "68", label: "Design Backlog", desc: "BRD approved — design team must create Figma screens. Saudi Trading (19) is the largest backlog.", color: C.insight },
    { num: "42", label: "BRD Backlog", desc: "Designed but no requirements. Squad leads must author BRDs. Portfolio Monitoring (10) is the largest.", color: C.critical },
    { num: "10", label: "Newly Discovered", desc: "Features found in deep extraction not in the original inventory. Must be classified and assigned.", color: C.opportunity },
  ];
  actions.forEach((a, i) => {
    const ay = 1.85 + i * 1.15;
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: rX + 0.3, y: ay, w: 0.65, h: 0.65, fill: { color: a.color }, line: { width: 0 }, rectRadius: 0.06 });
    s.addText(a.num, { x: rX + 0.3, y: ay, w: 0.65, h: 0.65, fontFace: F.num, fontSize: 18, bold: true, color: C.white, align: "center", valign: "middle", margin: 0 });
    s.addText(a.label, { x: rX + 1.1, y: ay + 0.02, w: 3.5, h: 0.22, fontFace: F.body, fontSize: 10, bold: true, color: C.ink, margin: 0 });
    s.addText(a.desc, { x: rX + 1.1, y: ay + 0.28, w: 4, h: 0.5, fontFace: F.body, fontSize: 8.5, color: C.slate700, margin: 0 });
  });

  addFooter(pres, s, { source: "Features Inventory · BRDs + Figma API", dateLabel: DATE_LABEL });
}

// ── SLIDE 9: NEW PAGES DISCOVERED ───────────────────────────────────────
{
  const s = pres.addSlide();
  s.background = { fill: C.white };
  addHeader(pres, s, { title: "New Figma Pages Discovered", eyebrow: "DEEP EXTRACTION", page: 9 });

  const newPages = [
    { module: "OnBoarding KYC", page: "Fast Onboarding", frames: 364, desc: "Streamlined account opening — simplified KYC variant with fewer steps. Could address the 87% onboarding drop-off identified in IA analysis.", impact: "HIGH" },
    { module: "OnBoarding KYC", page: "Guest Mode", frames: 21, desc: "Full Web-based guest experience with Market Landscape and Benchmark Analysis screens. More extensive than the BRD scope (ARCD-75522).", impact: "HIGH" },
    { module: "OnBoarding KYC", page: "First Engagement", frames: 1, desc: "Post-onboarding activation flow (225+ nodes). Designed to engage new users after their first login. Not in features inventory.", impact: "MEDIUM" },
    { module: "OnBoarding KYC", page: "Tutorials", frames: 1, desc: "In-app tutorial screens — onboarding education content. Not in features inventory.", impact: "MEDIUM" },
    { module: "Home", page: "Ramadan", frames: 0, desc: "Seasonal theming page — currently empty but prepared for Ramadan content. Indicates seasonal experience capability.", impact: "LOW" },
    { module: "Portfolios", page: "Digital StoryTeller", frames: 1, desc: "Dedicated page for Feature #76 (Storyteller Quarterly Report). 47 nodes with 26 instances. Design work is more advanced than inventory status suggested.", impact: "HIGH" },
    { module: "Discover (IPO)", page: "Discover & Search", frames: 2, desc: "Expanded discovery experience with Search integration. Contains Murabha, POA, Shariah List, Donation, Smart Investment sub-sections.", impact: "HIGH" },
  ];

  const tY = 1.15, rowH = 0.72;
  ["Module", "New Page", "Description", "Impact"].forEach((c, i) => {
    const cw = [1.8, 1.5, 7.4, 1.6][i];
    let cx = M; for (let j = 0; j < i; j++) cx += [1.8, 1.5, 7.4, 1.6][j];
    s.addShape(pres.shapes.RECTANGLE, { x: cx, y: tY, w: cw, h: 0.35, fill: { color: C.navy }, line: { width: 0 } });
    s.addText(c, { x: cx + 0.06, y: tY, w: cw - 0.12, h: 0.35, fontFace: F.body, fontSize: 8.5, bold: true, color: C.white, margin: 0, align: "left", valign: "middle" });
  });

  newPages.forEach((np, ri) => {
    const ry = tY + 0.35 + ri * rowH;
    const bg = ri % 2 === 0 ? C.white : C.slate100;
    const colWidths = [1.8, 1.5, 7.4, 1.6];
    const vals = [np.module, np.page, np.desc, np.impact];
    vals.forEach((v, ci) => {
      let cx = M; for (let j = 0; j < ci; j++) cx += colWidths[j];
      s.addShape(pres.shapes.RECTANGLE, { x: cx, y: ry, w: colWidths[ci], h: rowH, fill: { color: bg }, line: { color: C.line, width: 0.25 } });
      const fc = ci === 3 ? (v === "HIGH" ? C.critical : (v === "MEDIUM" ? C.opportunity : C.slate600)) : C.ink;
      s.addText(v, { x: cx + 0.06, y: ry, w: colWidths[ci] - 0.12, h: rowH, fontFace: F.body, fontSize: ci === 2 ? 7.5 : 8.5, bold: ci <= 1 || ci === 3, color: fc, margin: 0, align: "left", valign: "middle" });
    });
  });

  addFooter(pres, s, { source: "Figma REST API · Full-depth extraction · Pages not in original figma-screens.md", dateLabel: DATE_LABEL });
}

// ── SLIDE 10: TEXT LAYER TERMINOLOGY MAP ─────────────────────────────────
{
  const s = pres.addSlide();
  s.background = { fill: C.white };
  addHeader(pres, s, { title: "Terminology Map — Key UI Labels Across Modules", eyebrow: "CONTENT ANALYSIS", page: 10 });

  const termGroups = [
    {
      category: "Navigation & Structure",
      terms: ["Home", "Market", "Portfolios", "Orders", "Discover", "Profile", "Tradepad", "Watchlist"],
      note: "Primary nav tabs — consistent across all modules",
    },
    {
      category: "Market Segments",
      terms: ["Saudi Market", "US Market", "UAE Market", "Mutual Fund", "Mashura", "Crowd Fund", "Other Markets"],
      note: "UAE Market and Other Markets are NEW — not in current features inventory",
    },
    {
      category: "Trading Actions",
      terms: ["Buy", "Normal", "Market Price", "Shares", "Amount", "From", "Source", "Max Cash", "Max Margin", "Buying power"],
      note: "Tradepad labels — clear and action-oriented",
    },
    {
      category: "Portfolio Views",
      terms: ["All Saudi Portfolios", "Market Value", "Total Cash", "Unrealized P/L", "Trade", "Transfer", "Apply Finance"],
      note: "'Apply Finance' is the Murabaha CTA — terminology alignment needed",
    },
    {
      category: "Discover Section",
      terms: ["Discover", "Auto Subscription", "Dividend List", "Murabha", "Smart Investment", "Shariah List", "POA", "Donation", "Tadawulaty"],
      note: "POA and Donation are undocumented features discovered in deep extraction",
    },
    {
      category: "Settings & Auth",
      terms: ["Session Time Out", "Activate MPIN", "OTP", "Resend", "Change Password", "Registered Devices"],
      note: "Standard settings — no terminology conflicts detected",
    },
  ];

  let yPos = 1.2;
  termGroups.forEach((tg, gi) => {
    const gh = 0.85;
    const bg = gi % 2 === 0 ? C.white : C.slate100;
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, {
      x: M, y: yPos, w: W - 2*M, h: gh,
      fill: { color: bg }, line: { color: C.line, width: 0.5 }, rectRadius: 0.04,
    });
    s.addText(tg.category, {
      x: M + 0.15, y: yPos + 0.04, w: 2.5, h: 0.22,
      fontFace: F.head, fontSize: 9, bold: true, color: C.navy, margin: 0,
    });

    // Terms as pills
    let termX = M + 0.15;
    tg.terms.forEach(term => {
      const tw = Math.min(term.length * 0.08 + 0.35, 2.5);
      if (termX + tw > W - M - 0.5) { return; }
      s.addShape(pres.shapes.ROUNDED_RECTANGLE, {
        x: termX, y: yPos + 0.3, w: tw, h: 0.22,
        fill: { color: C.brandSoft }, line: { width: 0 }, rectRadius: 0.03,
      });
      s.addText(term, {
        x: termX, y: yPos + 0.3, w: tw, h: 0.22,
        fontFace: F.body, fontSize: 7.5, color: C.navy, align: "center", valign: "middle", margin: 0,
      });
      termX += tw + 0.12;
    });

    s.addText(tg.note, {
      x: M + 0.15, y: yPos + 0.58, w: W - 2*M - 0.3, h: 0.22,
      fontFace: F.body, fontSize: 7.5, italic: true, color: C.slate600, margin: 0,
    });

    yPos += gh + 0.1;
  });

  addFooter(pres, s, { source: "Figma REST API · 262,038 text layers extracted · " + DATE_LABEL, dateLabel: DATE_LABEL });
}

// ── SLIDE 11-13: SQUAD DETAILS (3 slides) ───────────────────────────────
function buildSquadSlide(squads, pageNum, title) {
  const s = pres.addSlide();
  s.background = { fill: C.white };
  addHeader(pres, s, { title, eyebrow: "SQUAD DETAIL", page: pageNum });

  const cw = (W - 2*M - 0.3) / 2;
  const ch = 2.5;

  squads.forEach((sq, i) => {
    const col = i % 2, row = Math.floor(i / 2);
    const cx = M + col * (cw + 0.3), cy = 1.2 + row * (ch + 0.2);

    card(pres, s, { x: cx, y: cy, w: cw, h: ch });
    s.addText(sq.name, { x: cx + 0.2, y: cy + 0.1, w: cw - 1.5, h: 0.3, fontFace: F.head, fontSize: 12, bold: true, color: C.ink, margin: 0 });
    s.addText(String(sq.total), { x: cx + cw - 1.3, y: cy + 0.08, w: 0.6, h: 0.35, fontFace: F.num, fontSize: 20, bold: true, color: C.brand, margin: 0, align: "center" });
    s.addText("features", { x: cx + cw - 0.75, y: cy + 0.15, w: 0.6, h: 0.25, fontFace: F.body, fontSize: 8, color: C.slate600, margin: 0 });

    const miniY = cy + 0.5;
    [
      { label: "Live", val: sq.live, color: C.positive },
      { label: "BRD+Figma", val: sq.brdFigma, color: C.stable },
      { label: "Figma Only", val: sq.figmaOnly, color: C.critical },
      { label: "Gaps", val: sq.gapCount, color: C.critical },
    ].forEach((mi, j) => {
      const mx = cx + 0.2 + j * 1.45;
      s.addText(String(mi.val), { x: mx, y: miniY, w: 0.4, h: 0.22, fontFace: F.num, fontSize: 12, bold: true, color: mi.color, margin: 0 });
      s.addText(mi.label, { x: mx + 0.42, y: miniY, w: 0.9, h: 0.22, fontFace: F.body, fontSize: 7.5, color: C.slate600, margin: 0, valign: "middle" });
    });

    // Coverage bar
    const barY = miniY + 0.35, barW = cw - 0.4;
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: cx + 0.2, y: barY, w: barW, h: 0.18, fill: { color: C.slate200 }, line: { width: 0 }, rectRadius: 0.09 });
    let off = 0;
    [
      { count: sq.live, color: C.positive },
      { count: Math.max(0, sq.brdFigma - sq.live), color: C.stable },
      { count: sq.brdOnly, color: C.insight },
      { count: sq.figmaOnly, color: C.critical },
    ].forEach(seg => {
      if (seg.count > 0) {
        const sw = (seg.count / sq.total) * barW;
        s.addShape(pres.shapes.RECTANGLE, { x: cx + 0.2 + off, y: barY, w: sw, h: 0.18, fill: { color: seg.color }, line: { width: 0 } });
        off += sw;
      }
    });

    s.addShape(pres.shapes.LINE, { x: cx + 0.2, y: barY + 0.32, w: cw - 0.4, h: 0, line: { color: C.line, width: 0.5 } });
    if (sq.topGap) {
      s.addText(`Top gap: ${sq.topGap}${sq.gapScore ? ` (${sq.gapScore}/25)` : ""}`, {
        x: cx + 0.2, y: barY + 0.4, w: cw - 0.4, h: 0.2,
        fontFace: F.body, fontSize: 8, color: C.critical, margin: 0,
      });
    }

    const livePct = Math.round((sq.live / sq.total) * 100);
    s.addText(`${livePct}% live`, {
      x: cx + 0.2, y: cy + ch - 0.4, w: 1.5, h: 0.22,
      fontFace: F.body, fontSize: 9, bold: true,
      color: livePct >= 30 ? C.positive : (livePct >= 15 ? C.opportunity : C.critical), margin: 0,
    });
  });
  addFooter(pres, s, { source: "Features Inventory · BRDs + Figma API", dateLabel: DATE_LABEL });
}

buildSquadSlide(SQUADS.slice(0, 4), 11, "Trading & Portfolio Squads");
buildSquadSlide(SQUADS.slice(4, 8), 12, "Wealth, Funds, IPOs & Corporate Actions");
buildSquadSlide(SQUADS.slice(8, 11), 13, "Engagement & Cross-Journey");

// ── SLIDE 14: DESIGN ACTIVITY TIMELINE ──────────────────────────────────
{
  const s = pres.addSlide();
  s.background = { fill: C.white };
  addHeader(pres, s, { title: "Design Activity — Last Modified Dates", eyebrow: "DESIGN VELOCITY", page: 14 });

  const timeline = [
    { date: "2026-04-21", files: ["OnBoarding KYC", "Market"], status: "Active today" },
    { date: "2026-04-20", files: ["Discover (IPO)"], status: "Active yesterday" },
    { date: "2026-04-15", files: ["Home", "Profile & Setting"], status: "Active this week" },
    { date: "2026-04-14", files: ["Portfolios"], status: "Active this week" },
    { date: "2026-03-28", files: ["Tradepad"], status: "3+ weeks ago" },
    { date: "2026-03-26", files: ["Orders"], status: "3+ weeks ago" },
  ];

  timeline.forEach((tl, i) => {
    const ty = 1.3 + i * 0.85;
    const isActive = tl.date >= "2026-04-14";

    // Date badge
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, {
      x: M, y: ty, w: 1.6, h: 0.55,
      fill: { color: isActive ? C.positiveSoft : C.opportunitySoft },
      line: { width: 0 }, rectRadius: 0.06,
    });
    s.addText(tl.date, {
      x: M, y: ty + 0.02, w: 1.6, h: 0.3,
      fontFace: F.num, fontSize: 11, bold: true, color: isActive ? C.positive : C.opportunity, align: "center", margin: 0,
    });
    s.addText(tl.status, {
      x: M, y: ty + 0.3, w: 1.6, h: 0.22,
      fontFace: F.body, fontSize: 7.5, color: isActive ? C.positive : C.opportunity, align: "center", margin: 0,
    });

    // Connector line
    if (i < timeline.length - 1) {
      s.addShape(pres.shapes.LINE, { x: M + 0.8, y: ty + 0.55, w: 0, h: 0.3, line: { color: C.line, width: 1 } });
    }

    // File cards
    tl.files.forEach((f, fi) => {
      const fx = M + 2 + fi * 3.5;
      card(pres, s, { x: fx, y: ty, w: 3.2, h: 0.55 });
      s.addText(f, { x: fx + 0.15, y: ty + 0.05, w: 2.9, h: 0.25, fontFace: F.body, fontSize: 10, bold: true, color: C.ink, margin: 0 });
      const mod = MODULES.find(m => m.name === f);
      if (mod) {
        s.addText(`${(mod.nodes/1000).toFixed(0)}K nodes · ${mod.pages} pages`, {
          x: fx + 0.15, y: ty + 0.3, w: 2.9, h: 0.2,
          fontFace: F.body, fontSize: 8, color: C.slate600, margin: 0,
        });
      }
    });
  });

  card(pres, s, { x: M, y: 6.3, w: W - 2*M, h: 0.55, fill: C.opportunitySoft });
  addTag(pres, s, "WATCH", { x: M + 0.2, y: 6.37, w: 0.8, tone: "opportunity" });
  s.addText("Tradepad and Orders haven't been modified in 3+ weeks. OnBoarding and Market are actively being worked on today. Design resources appear concentrated on onboarding and market experience.", {
    x: M + 1.2, y: 6.33, w: 11, h: 0.48,
    fontFace: F.body, fontSize: 9, color: C.slate700, margin: 0, valign: "middle",
  });

  addFooter(pres, s, { source: "Figma REST API · lastModified metadata �� " + DATE_LABEL, dateLabel: DATE_LABEL });
}

// ── SLIDE 15: RECOMMENDATIONS ───���───────────────────────────────────────
{
  const s = pres.addSlide();
  s.background = { fill: C.white };
  addHeader(pres, s, { title: "Strategic Recommendations — Deep Edition", eyebrow: "FEATURES MAP", page: 15 });

  const recs = [
    { num: "01", title: "Add 10 Discovered Features to Inventory", desc: "Stock Screener, UAE Market, Fast Onboarding, Guest Mode (Web), First Engagement, Tutorials, Digital StoryTeller, Ramadan Theme, POA, Crowd Fund — all found in Figma but missing from the 154-feature inventory. Classify, assign to squads, and write BRDs.", priority: "URGENT", tone: "critical" },
    { num: "02", title: "Reclassify Stock Screener Gap", desc: "Gap #2 (score 25/25) has active Figma design in Market file. Update gap matrix status from 'No Figma' to 'In Design'. Write BRD if one doesn't exist. This is the highest-impact gap already being addressed.", priority: "HIGH", tone: "positive" },
    { num: "03", title: "Complete Squad Validation (14 Days Overdue)", desc: "April 7 deadline passed. Deep extraction reveals the inventory is incomplete (10 new features found). Validation must include these new discoveries. Set new deadline: May 1.", priority: "URGENT", tone: "critical" },
    { num: "04", title: "Investigate UAE Market Scope", desc: "UAE Market labels found across Market and Orders files. This is a 3rd market beyond Saudi and US — not in any BRD. Confirm if this is intentional scope or placeholder design. If real, it's a major product expansion.", priority: "HIGH", tone: "opportunity" },
    { num: "05", title: "Prioritize Fast Onboarding Design", desc: "364 sub-frames in the Fast Onboarding page suggest significant design investment. With 87% onboarding drop-off (from IA analysis), this streamlined flow could be the highest-ROI feature to build next.", priority: "HIGH", tone: "opportunity" },
    { num: "06", title: "Refresh Figma Token Monthly", desc: "Token expired between sessions. Set a calendar reminder to regenerate the personal access token on the 1st of each month. Store in .zshrc for automated scripts.", priority: "LOW", tone: "neutral" },
  ];

  recs.forEach((r, i) => {
    const ry = 1.15 + i * 0.95;
    card(pres, s, { x: M, y: ry, w: W - 2*M, h: 0.85 });
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: M + 0.15, y: ry + 0.15, w: 0.5, h: 0.5, fill: { color: C.navy }, line: { width: 0 }, rectRadius: 0.06 });
    s.addText(r.num, { x: M + 0.15, y: ry + 0.15, w: 0.5, h: 0.5, fontFace: F.num, fontSize: 16, bold: true, color: C.white, align: "center", valign: "middle", margin: 0 });
    s.addText(r.title, { x: M + 0.8, y: ry + 0.08, w: 8.5, h: 0.25, fontFace: F.body, fontSize: 10, bold: true, color: C.ink, margin: 0 });
    addTag(pres, s, r.priority, { x: M + 9.5, y: ry + 0.1, w: 0.9, tone: r.tone });
    s.addText(r.desc, { x: M + 0.8, y: ry + 0.38, w: 11.3, h: 0.4, fontFace: F.body, fontSize: 8, color: C.slate700, margin: 0 });
  });

  addFooter(pres, s, { source: "Deep Figma extraction synthesis + Features Map + IA analysis", dateLabel: DATE_LABEL });
}

// ── SLIDE 16-18: COMPETITIVE LANDSCAPE ──────────────────────────────────
{
  const s = pres.addSlide();
  s.background = { fill: C.white };
  addHeader(pres, s, { title: "Competitive Landscape — Who Leads Where", eyebrow: "COMPETITIVE INTELLIGENCE", page: 16 });

  const competitors = [
    { name: "Moomoo", gaps: 12, strengths: "L2 depth, AI assistant, stock comparison, community feed, paper trading, fractional shares, money flow", color: C.critical },
    { name: "Derayah / Smart", gaps: 9, strengths: "Conditional orders, Apple Pay, SIP, goal-based investing, pre-filled KYC, dividend reinvestment", color: C.critical },
    { name: "Sahm Capital", gaps: 11, strengths: "Tab navigation, free live prices, personalized calendar, social proof nudges, always-on price view", color: C.critical },
    { name: "AlJazira Capital", gaps: 4, strengths: "Private funds (10+), SIP, Nomu institutional IPO, IPO popup banners", color: C.opportunity },
    { name: "Investing.com", gaps: 5, strengths: "Stock screener, multi-type alerts, fundamental data, ETF exposure", color: C.opportunity },
    { name: "IBKR / Global", gaps: 7, strengths: "Pre/post market, fractional shares, L2 depth, bonds, futures, advanced orders", color: C.opportunity },
  ];

  const cw = (W - 2*M - 0.4) / 2;
  competitors.forEach((comp, i) => {
    const col = i % 2, row = Math.floor(i / 2);
    const cx = M + col * (cw + 0.4), cy = 1.2 + row * 1.75;

    card(pres, s, { x: cx, y: cy, w: cw, h: 1.55 });
    s.addText(comp.name, { x: cx + 0.2, y: cy + 0.1, w: cw - 1.4, h: 0.28, fontFace: F.head, fontSize: 12, bold: true, color: C.ink, margin: 0 });
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: cx + cw - 1.1, y: cy + 0.12, w: 0.9, h: 0.26, fill: { color: comp.color }, line: { width: 0 }, rectRadius: 0.04 });
    s.addText(`${comp.gaps} gaps`, { x: cx + cw - 1.1, y: cy + 0.12, w: 0.9, h: 0.26, fontFace: F.num, fontSize: 9, bold: true, color: C.white, align: "center", valign: "middle", margin: 0 });
    s.addText("Key advantages over ARC:", { x: cx + 0.2, y: cy + 0.48, w: cw - 0.4, h: 0.18, fontFace: F.body, fontSize: 8, bold: true, color: C.slate600, margin: 0 });
    s.addText(comp.strengths, { x: cx + 0.2, y: cy + 0.7, w: cw - 0.4, h: 0.75, fontFace: F.body, fontSize: 8.5, color: C.slate700, margin: 0 });
  });

  addFooter(pres, s, { source: "Benchmark reports: Moomoo, Derayah, AlJazira, Sahm, Investing.com, IBKR", dateLabel: DATE_LABEL });
}

// ── SLIDE 19: DOCUMENTATION DEBT ────────────────────────────────────────
{
  const s = pres.addSlide();
  s.background = { fill: C.white };
  addHeader(pres, s, { title: "Documentation Debt — Close the Gap", eyebrow: "GOVERNANCE", page: 17 });

  // Two columns
  const figmaOnlySquads = SQUADS.filter(sq => sq.figmaOnly > 0);
  card(pres, s, { x: M, y: 1.2, w: 5.8, h: 3.5 });
  s.addText("42 Features Need BRDs", { x: M + 0.2, y: 1.3, w: 5, h: 0.3, fontFace: F.head, fontSize: 12, bold: true, color: C.critical, margin: 0 });
  figmaOnlySquads.forEach((sq, i) => {
    const ry = 1.75 + i * 0.38;
    s.addText(sq.name, { x: M + 0.3, y: ry, w: 2, h: 0.28, fontFace: F.body, fontSize: 9, color: C.ink, margin: 0, align: "right", valign: "middle" });
    hBar(pres, s, { x: M + 2.5, y: ry + 0.04, w: 2, h: 0.18, pct: sq.figmaOnly / 12, color: C.critical });
    s.addText(String(sq.figmaOnly), { x: M + 4.7, y: ry, w: 0.5, h: 0.28, fontFace: F.num, fontSize: 10, bold: true, color: C.critical, margin: 0, valign: "middle" });
  });

  card(pres, s, { x: 6.8, y: 1.2, w: 6, h: 3.5 });
  s.addText("68 Features Need Figma", { x: 7, y: 1.3, w: 5, h: 0.3, fontFace: F.head, fontSize: 12, bold: true, color: C.insight, margin: 0 });
  const brdOnlySquads = SQUADS.filter(sq => sq.brdOnly > 0);
  brdOnlySquads.forEach((sq, i) => {
    const ry = 1.75 + i * 0.38;
    s.addText(sq.name, { x: 7.1, y: ry, w: 2, h: 0.28, fontFace: F.body, fontSize: 9, color: C.ink, margin: 0, align: "right", valign: "middle" });
    hBar(pres, s, { x: 9.3, y: ry + 0.04, w: 2.2, h: 0.18, pct: sq.brdOnly / 19, color: C.insight });
    s.addText(String(sq.brdOnly), { x: 11.7, y: ry, w: 0.5, h: 0.28, fontFace: F.num, fontSize: 10, bold: true, color: C.insight, margin: 0, valign: "middle" });
  });

  // Bottom: updated inventory count
  card(pres, s, { x: M, y: 5.0, w: W - 2*M, h: 1.8, fill: C.opportunitySoft });
  s.addText("Updated Inventory: 154 → 164 features", {
    x: M + 0.3, y: 5.1, w: 8, h: 0.3,
    fontFace: F.head, fontSize: 14, bold: true, color: C.opportunity, margin: 0,
  });
  s.addText("Deep extraction revealed 10 features not in the original inventory. After adding these, the total rises from 154 to approximately 164 features. The documentation debt increases accordingly:\n\n" +
    "• 42 → 52 features with Figma but no BRD (10 new discoveries need BRDs)\n" +
    "• 68 features with BRD but no Figma (unchanged)\n" +
    "• Squad validation must now cover 164 features instead of 154", {
    x: M + 0.3, y: 5.45, w: 11.5, h: 1.2,
    fontFace: F.body, fontSize: 9, color: C.slate700, margin: 0,
  });

  addFooter(pres, s, { source: "Features Inventory + Deep Figma extraction · " + DATE_LABEL, dateLabel: DATE_LABEL });
}

// ── SLIDE 20: CLOSING ───────────────────────────────────────────────────
{
  const s = pres.addSlide();
  s.background = { fill: C.navyDeep };
  s.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: 0.06, h: H, fill: { color: C.brand } });

  s.addText("Features Map — Deep Edition", {
    x: M + 0.3, y: 1.2, w: 10, h: 0.6,
    fontFace: F.head, fontSize: 28, bold: true, color: C.white, margin: 0,
  });
  s.addText("Key Takeaways", {
    x: M + 0.3, y: 1.85, w: 10, h: 0.35,
    fontFace: F.head, fontSize: 14, color: C.brand, margin: 0,
  });

  const takeaways = [
    "2.27M design nodes analyzed across 8 Figma files — the most comprehensive ARC design audit to date",
    "All 8 modules have Mobile + Web + Tablet designs — full platform parity confirmed",
    "10 new features discovered: Stock Screener in design, UAE Market, Fast Onboarding, Guest Mode (Web), and more",
    "Stock Screener (Gap #2, score 25/25) is actively being designed — highest-impact gap is closing",
    "164 features total (up from 154) — documentation debt now larger than previously estimated",
    "Fast Onboarding could address 87% drop-off — most promising new discovery for immediate ROI",
    "Design activity concentrated on OnBoarding and Market (modified today) — Tradepad and Orders stale 3+ weeks",
  ];

  takeaways.forEach((t, i) => {
    s.addText(t, {
      x: M + 0.6, y: 2.5 + i * 0.5, w: 11, h: 0.4,
      fontFace: F.body, fontSize: 11, color: C.slate200, margin: 0,
      bullet: { type: "number", style: "arabicPeriod", color: C.brand },
    });
  });

  s.addText("Digital Experience Department  ·  Al Rajhi Capital  ·  " + DATE_LABEL, {
    x: M + 0.3, y: 6.5, w: 10, h: 0.25,
    fontFace: F.body, fontSize: 10, color: C.slate200, margin: 0,
  });
}

// ── SAVE ─────────────────────────────────────────────────────────────────
const outDir = path.join(__dirname, "reports");
if (!fs.existsSync(outDir)) fs.mkdirSync(outDir, { recursive: true });
const outFile = path.join(outDir, `features-map-deep-${DATE_LABEL}.pptx`);

pres.writeFile({ fileName: outFile }).then(() => {
  console.log(`\n  Done → ${outFile}\n`);
}).catch(err => {
  console.error("Error:", err);
  process.exit(1);
});
