#!/usr/bin/env node
// ═══════════════════════════════════════════════════════════════════════════
//  Features Map — Visual Deck Builder
//  ARC Digital Experience · 164 features, 62 gaps, 14 differentiators
// ═══════════════════════════════════════════════════════════════════════════
const PptxGenJS = require("pptxgenjs");
const path = require("path");

// ── Design tokens (matching investor-behavior template) ──────────────────
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
const TOTAL_PAGES = 16;
const softShadow = () => ({ type: "outer", color: "0A1F4D", blur: 12, offset: 2, angle: 90, opacity: 0.08 });
const liftShadow = () => ({ type: "outer", color: "0A1F4D", blur: 18, offset: 3, angle: 90, opacity: 0.12 });

const DATE_LABEL = "2026-04-22";

// ── Helpers ──────────────────────────────────────────────────────────────
function addHeader(pres, slide, { title, eyebrow, page }) {
  slide.addText("alrajhi", {
    x: M, y: 0.32, w: 0.95, h: 0.28,
    fontFace: F.head, fontSize: 13, bold: true, color: C.brand, align: "left", margin: 0,
  });
  slide.addText("capital", {
    x: M, y: 0.56, w: 0.95, h: 0.22,
    fontFace: F.head, fontSize: 10, color: C.brand, align: "left", margin: 0,
  });
  slide.addShape(pres.shapes.LINE, {
    x: M + 1.15, y: 0.38, w: 0, h: 0.42,
    line: { color: C.line, width: 0.75 },
  });
  if (eyebrow) {
    slide.addText(eyebrow.toUpperCase(), {
      x: M + 1.3, y: 0.30, w: 9, h: 0.22,
      fontFace: F.body, fontSize: 8.5, bold: true, color: C.slate400,
      charSpacing: 3, margin: 0, align: "left",
    });
  }
  slide.addText(title, {
    x: M + 1.3, y: 0.50, w: 10, h: 0.35,
    fontFace: F.head, fontSize: 15, bold: true, color: C.ink, margin: 0, align: "left",
  });
  if (page) {
    slide.addText([
      { text: String(page).padStart(2, "0"), options: { bold: true, color: C.ink } },
      { text: `  /  ${String(TOTAL_PAGES).padStart(2, "0")}`, options: { color: C.slate400 } },
    ], {
      x: W - M - 1.5, y: 0.42, w: 1.5, h: 0.35,
      fontFace: F.body, fontSize: 10, align: "right", margin: 0,
    });
  }
  slide.addShape(pres.shapes.LINE, {
    x: M, y: 0.95, w: W - 2 * M, h: 0,
    line: { color: C.line, width: 0.75 },
  });
}

function addFooter(pres, slide, { source, dateLabel }) {
  slide.addShape(pres.shapes.LINE, {
    x: M, y: 7.15, w: W - 2 * M, h: 0,
    line: { color: C.line, width: 0.75 },
  });
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
    x, y, w, h: 0.26,
    fill: { color: t.bg }, line: { color: t.bg, width: 0 },
    rectRadius: 0.03,
  });
  slide.addText(text, {
    x, y, w, h: 0.26,
    fontFace: F.body, fontSize: 8, bold: true, color: t.fg,
    charSpacing: 1, align: "center", valign: "middle", margin: 0,
  });
}

function card(pres, slide, { x, y, w, h, fill = C.white }) {
  slide.addShape(pres.shapes.ROUNDED_RECTANGLE, {
    x, y, w, h,
    fill: { color: fill },
    line: { color: C.line, width: 0.5 },
    rectRadius: 0.08,
    shadow: softShadow(),
  });
}

function bigNum(slide, { x, y, num, label, color = C.ink }) {
  slide.addText(String(num), {
    x, y, w: 1.8, h: 0.55,
    fontFace: F.num, fontSize: 32, bold: true, color, margin: 0, align: "center",
  });
  slide.addText(label, {
    x, y: y + 0.5, w: 1.8, h: 0.25,
    fontFace: F.body, fontSize: 9, color: C.slate600, margin: 0, align: "center",
  });
}

function hBar(pres, slide, { x, y, w, h, pct, color, bgColor = C.slate100 }) {
  slide.addShape(pres.shapes.ROUNDED_RECTANGLE, {
    x, y, w, h, fill: { color: bgColor }, line: { width: 0 }, rectRadius: h / 2,
  });
  if (pct > 0) {
    slide.addShape(pres.shapes.ROUNDED_RECTANGLE, {
      x, y, w: Math.max(w * pct, h), h, fill: { color }, line: { width: 0 }, rectRadius: h / 2,
    });
  }
}

// ══════════════════════════════════════════════════════════════════════════
//  DATA
// ══════════════════════════════════════════════════════════════════════════
const SQUADS = [
  { name: "Onboarding",          live: 4,  planned: 9,  figmaOnly: 11, brdOnly: 1,  brdFigma: 12, total: 24, topGap: "Onboarding checklist", gapScore: null, gapCount: 3 },
  { name: "Saudi Trading",       live: 6,  planned: 19, figmaOnly: 14, brdOnly: 19, brdFigma: 7,  total: 39, topGap: "Level 2 Order Book", gapScore: 25, gapCount: 11 },
  { name: "US Trading",          live: 3,  planned: 6,  figmaOnly: 1,  brdOnly: 6,  brdFigma: 3,  total: 10, topGap: "Pre/Post-Market Trading", gapScore: 25, gapCount: 15 },
  { name: "Portfolio Monitoring", live: 2,  planned: 9,  figmaOnly: 11, brdOnly: 4,  brdFigma: 7,  total: 22, topGap: "Gain/Loss Tax Report", gapScore: 20, gapCount: 4 },
  { name: "Wealth Visibility",   live: 1,  planned: 4,  figmaOnly: 0,  brdOnly: 4,  brdFigma: 1,  total: 5,  topGap: "Apple Pay Funding", gapScore: null, gapCount: 1 },
  { name: "Mutual Funds",        live: 1,  planned: 9,  figmaOnly: 1,  brdOnly: 6,  brdFigma: 4,  total: 11, topGap: "Private Funds Access", gapScore: 20, gapCount: 5 },
  { name: "Robo Advisory",       live: 1,  planned: 2,  figmaOnly: 1,  brdOnly: 0,  brdFigma: 3,  total: 4,  topGap: "Goal-Based Portfolio", gapScore: 15, gapCount: 4 },
  { name: "IPOs",                live: 2,  planned: 4,  figmaOnly: 1,  brdOnly: 3,  brdFigma: 3,  total: 7,  topGap: "US Market IPO", gapScore: null, gapCount: 2 },
  { name: "Corporate Actions",   live: 0,  planned: 3,  figmaOnly: 1,  brdOnly: 2,  brdFigma: 1,  total: 4,  topGap: "Rights Issue Digital", gapScore: null, gapCount: 1 },
  { name: "Investor Engagement", live: 2,  planned: 10, figmaOnly: 4,  brdOnly: 11, brdFigma: 1,  total: 16, topGap: "Social Community Feed", gapScore: 20, gapCount: 3 },
  { name: "Cross-Journey",       live: 2,  planned: 12, figmaOnly: 7,  brdOnly: 13, brdFigma: 2,  total: 22, topGap: "Price Alert System", gapScore: 16, gapCount: 1 },
];

const TOP_GAPS = [
  { rank: 1,  name: "Level 2 Market Depth / Order Book", score: 25, squad: "Saudi / US Trading", competitors: "Moomoo, Derayah, Alinma, IBKR" },
  { rank: 2,  name: "Stock Screener", score: 25, squad: "Saudi / US Trading", competitors: "Moomoo, Investing.com, Derayah" },
  { rank: 3,  name: "Pre/Post-Market Trading (US)", score: 25, squad: "US Trading", competitors: "Moomoo, Robinhood, IBKR" },
  { rank: 4,  name: "Advanced Technical Analysis Suite", score: 25, squad: "Saudi / US Trading", competitors: "Moomoo, TradingView, thinkorswim" },
  { rank: 5,  name: "Stock Comparison Tool (Multi-Stock)", score: 20, squad: "Saudi / US Trading", competitors: "Moomoo (6), Derayah (2)" },
  { rank: 6,  name: "AI-Powered Assistant / AI Chat", score: 20, squad: "US Trading / Cross", competitors: "Moomoo AI, US competitors" },
  { rank: 7,  name: "Paper Trading / Simulated Mode", score: 20, squad: "Cross-Journey", competitors: "Moomoo, Derayah Smart, Sahm" },
  { rank: 8,  name: "Fractional Shares (US)", score: 20, squad: "US Trading", competitors: "Moomoo, Robinhood, IBKR" },
  { rank: 9,  name: "Social / Community Feed", score: 20, squad: "Investor Engagement", competitors: "Moomoo, Sahm" },
  { rank: 10, name: "Conditional Orders — Full BRD (Saudi)", score: 20, squad: "Saudi Trading", competitors: "Derayah, AlJazira, Sahm" },
  { rank: 11, name: "Personalized Events Calendar", score: 20, squad: "Saudi / US Trading", competitors: "Sahm" },
  { rank: 12, name: "Private Funds / PE Access", score: 20, squad: "Mutual Funds", competitors: "AlJazira, Derayah" },
  { rank: 13, name: "Liquidity / Money Flow Tracking", score: 20, squad: "Saudi / US Trading", competitors: "Moomoo, Sahm" },
  { rank: 14, name: "SIP for Mutual Funds", score: 20, squad: "Mutual Funds / Robo", competitors: "AlJazira, Derayah Smart" },
  { rank: 15, name: "Gain / Loss Tax Report", score: 20, squad: "Portfolio Monitoring", competitors: "Derayah, Saudi competitors" },
];

const DIFFERENTIATORS = [
  { name: "Murabaha Margin Lending (Sharia)", why: "Full Sharia-compliant digital margin — no comparable competitor" },
  { name: "Purification & Zakat Calculators", why: "Unique religious compliance tools — no competitor offers natively" },
  { name: "Minor Account + Guardian Controls", why: "Granular custodian controls unseen in Saudi retail competitors" },
  { name: "Mokafaa + ARG Group Bundle", why: "Ecosystem-exclusive loyalty architecture — non-replicable by competitors" },
  { name: "Storyteller (Narrative Report)", why: "Personalized quarterly narrative — no competitor produces this" },
  { name: "Shariah Multi-List Selection", why: "General + ARC-specific Shariah lists — more sophisticated than single filter" },
  { name: "Peer Portfolio Comparison", why: "Anonymized peer benchmarking — Moomoo has community, not peer P&L" },
  { name: "Portfolio Health Score", why: "Composite portfolio quality score — not observed in any benchmark" },
  { name: "SBL Program (Lending + Short Selling)", why: "Full SBL with Sharia margin integration — not offered by Saudi retail" },
  { name: "Investment Referral / Gift Campaigns", why: "Date-specific UCM gift campaigns + Mokafaa — unique rewards stack" },
  { name: "Tadawulaty Platform SSO", why: "Direct Edaa SSO — regulatory infrastructure advantage" },
  { name: "ZATCA-Compliant E-Invoices", why: "Auto e-invoices for wallet + purification — regulatory compliance leader" },
];

const NEW_GAPS_SAHM = [
  { id: "G-52", name: "Hover for Intra-Day Prices", score: 16 },
  { id: "G-54", name: "Expanded US Stock Inventory", score: 16 },
  { id: "G-56", name: "Always-On Live Price View", score: 16 },
  { id: "G-57", name: "Free Live Index Prices", score: 16 },
  { id: "G-59", name: "Personalized Events Calendar", score: 20 },
  { id: "G-61", name: "Advanced Trade Button", score: 16 },
  { id: "G-62", name: "Tab-Based Navigation", score: 16 },
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

  // Accent line
  s.addShape(pres.shapes.RECTANGLE, {
    x: 0, y: 0, w: 0.06, h: H, fill: { color: C.brand },
  });

  s.addText("alrajhi capital", {
    x: M + 0.3, y: 0.6, w: 4, h: 0.35,
    fontFace: F.head, fontSize: 14, bold: true, color: C.brand, margin: 0,
  });

  s.addText("ARC Features Map", {
    x: M + 0.3, y: 1.8, w: 10, h: 0.8,
    fontFace: F.head, fontSize: 36, bold: true, color: C.white, margin: 0,
  });
  s.addText("Complete Platform Feature Inventory, Competitive Gaps & Differentiators", {
    x: M + 0.3, y: 2.6, w: 10, h: 0.4,
    fontFace: F.body, fontSize: 14, color: C.slate400, margin: 0,
  });

  // Key numbers row
  const metrics = [
    { num: "164", label: "FEATURES\nMAPPED" },
    { num: "62", label: "COMPETITOR\nGAPS" },
    { num: "14", label: "ARC\nDIFFERENTIATORS" },
    { num: "11", label: "SQUADS\nCOVERED" },
    { num: "8", label: "FIGMA FILES\nEXTRACTED" },
  ];
  const mw = 2.1, mx = M + 0.3;
  metrics.forEach((m, i) => {
    const bx = mx + i * (mw + 0.3);
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, {
      x: bx, y: 3.6, w: mw, h: 1.3,
      fill: { color: "0D1B3C" }, line: { color: "1A2D5A", width: 0.5 },
      rectRadius: 0.08,
    });
    s.addText(m.num, {
      x: bx, y: 3.7, w: mw, h: 0.6,
      fontFace: F.num, fontSize: 28, bold: true, color: C.brand, align: "center", margin: 0,
    });
    s.addText(m.label, {
      x: bx, y: 4.3, w: mw, h: 0.5,
      fontFace: F.body, fontSize: 8.5, color: C.slate400, align: "center", margin: 0, lineSpacingMultiple: 1.1,
    });
  });

  // Sources
  s.addText("Sources: 100+ BRDs  ·  8 Figma files (unreleased revamp)  ·  10+ competitor benchmarks  ·  App Store data", {
    x: M + 0.3, y: 5.3, w: 11, h: 0.25,
    fontFace: F.body, fontSize: 9, italic: true, color: C.slate400, margin: 0,
  });

  s.addText("Digital Experience Department  ·  Al Rajhi Capital  ·  " + DATE_LABEL, {
    x: M + 0.3, y: 6.5, w: 10, h: 0.25,
    fontFace: F.body, fontSize: 10, color: C.slate200, margin: 0,
  });
}

// ── SLIDE 2: PLATFORM SNAPSHOT ──────────────────────────────────────────
{
  const s = pres.addSlide();
  s.background = { fill: C.white };
  addHeader(pres, s, { title: "Platform Snapshot", eyebrow: "FEATURES MAP", page: 2 });

  // Top stat cards
  const stats = [
    { num: "164", label: "Total Features", color: C.brand },
    { num: "24", label: "Live in Production", color: C.positive },
    { num: "129", label: "Planned", color: C.opportunity },
    { num: "42", label: "Figma-Only (No BRD)", color: C.critical },
    { num: "68", label: "BRD-Only (No Figma)", color: C.insight },
    { num: "44", label: "BRD + Figma Confirmed", color: C.stable },
  ];
  stats.forEach((st, i) => {
    const bx = M + i * 2.05;
    card(pres, s, { x: bx, y: 1.2, w: 1.9, h: 1.15 });
    s.addText(st.num, {
      x: bx, y: 1.3, w: 1.9, h: 0.5,
      fontFace: F.num, fontSize: 26, bold: true, color: st.color, align: "center", margin: 0,
    });
    s.addText(st.label, {
      x: bx + 0.1, y: 1.85, w: 1.7, h: 0.4,
      fontFace: F.body, fontSize: 8.5, color: C.slate600, align: "center", margin: 0,
    });
  });

  // Documentation health bar chart
  const docY = 2.7;
  s.addText("Documentation Health", {
    x: M, y: docY, w: 5, h: 0.3,
    fontFace: F.head, fontSize: 12, bold: true, color: C.ink, margin: 0,
  });

  const docBars = [
    { label: "BRD + Figma", count: 44, pct: 44/164, color: C.positive },
    { label: "BRD Only", count: 68, pct: 68/164, color: C.insight },
    { label: "Figma Only", count: 42, pct: 42/164, color: C.critical },
    { label: "Deep Extraction", count: 10, pct: 10/164, color: C.opportunity },
  ];
  docBars.forEach((b, i) => {
    const by = docY + 0.45 + i * 0.5;
    s.addText(b.label, {
      x: M, y: by, w: 1.6, h: 0.3,
      fontFace: F.body, fontSize: 9, color: C.slate700, margin: 0, align: "right",
    });
    hBar(pres, s, { x: M + 1.75, y: by + 0.05, w: 4, h: 0.22, pct: b.pct, color: b.color });
    s.addText(`${b.count}  (${Math.round(b.pct * 100)}%)`, {
      x: M + 5.9, y: by, w: 1.2, h: 0.3,
      fontFace: F.num, fontSize: 9, bold: true, color: b.color, margin: 0,
    });
  });

  // Right side: competitive position
  const cpX = 7.8;
  s.addText("Competitive Position", {
    x: cpX, y: docY, w: 5, h: 0.3,
    fontFace: F.head, fontSize: 12, bold: true, color: C.ink, margin: 0,
  });

  const cpStats = [
    { label: "Competitor Gaps", count: 62, color: C.critical, desc: "Features competitors have that ARC lacks" },
    { label: "ARC Differentiators", count: 14, color: C.positive, desc: "Features unique to ARC or notably stronger" },
    { label: "Parity Features", count: 33, color: C.stable, desc: "Features at comparable level" },
  ];
  cpStats.forEach((cp, i) => {
    const cy = docY + 0.45 + i * 0.65;
    card(pres, s, { x: cpX, y: cy, w: 4.8, h: 0.55 });
    s.addText(String(cp.count), {
      x: cpX + 0.15, y: cy + 0.05, w: 0.7, h: 0.45,
      fontFace: F.num, fontSize: 20, bold: true, color: cp.color, margin: 0, align: "center",
    });
    s.addText(cp.label, {
      x: cpX + 0.9, y: cy + 0.05, w: 2.5, h: 0.22,
      fontFace: F.body, fontSize: 10, bold: true, color: C.ink, margin: 0,
    });
    s.addText(cp.desc, {
      x: cpX + 0.9, y: cy + 0.28, w: 3.7, h: 0.22,
      fontFace: F.body, fontSize: 8, color: C.slate600, margin: 0,
    });
  });

  // Bottom: Live percentage
  const liveY = 4.9;
  s.addText("Production Readiness", {
    x: M, y: liveY, w: 5, h: 0.3,
    fontFace: F.head, fontSize: 12, bold: true, color: C.ink, margin: 0,
  });
  s.addText("Only 16% of mapped features are live. 84% remain in planning or design.", {
    x: M, y: liveY + 0.32, w: 7, h: 0.25,
    fontFace: F.body, fontSize: 9, color: C.slate600, margin: 0,
  });
  hBar(pres, s, { x: M, y: liveY + 0.7, w: W - 2 * M, h: 0.35, pct: 24/164, color: C.positive });
  s.addText("24 Live", {
    x: M + 0.15, y: liveY + 0.7, w: 1.5, h: 0.35,
    fontFace: F.body, fontSize: 9, bold: true, color: C.white, margin: 0, valign: "middle",
  });
  s.addText("130 Planned / Designed / Unknown", {
    x: M + (W - 2*M) * (24/164) + 0.3, y: liveY + 0.7, w: 4, h: 0.35,
    fontFace: F.body, fontSize: 9, color: C.slate600, margin: 0, valign: "middle",
  });

  // Insight callout
  card(pres, s, { x: M, y: 5.9, w: W - 2*M, h: 0.9, fill: C.insightSoft });
  addTag(pres, s, "KEY INSIGHT", { x: M + 0.2, y: 6.0, w: 1.1, tone: "insight" });
  s.addText("42 features exist in Figma with no BRD — these represent design intent without product commitment. 68 features have BRDs but no Figma screens yet. Closing this documentation gap is the #1 prerequisite for accurate roadmap planning.", {
    x: M + 1.5, y: 5.98, w: 10.5, h: 0.75,
    fontFace: F.body, fontSize: 9, color: C.slate700, margin: 0, valign: "middle",
  });

  addFooter(pres, s, { source: "Features Inventory (164 features) · BRDs + Figma API + Deep Extraction · 2026-04-22", dateLabel: DATE_LABEL });
}

// ── SLIDE 3: SQUAD HEATMAP ──────────────────────────────────────────────
{
  const s = pres.addSlide();
  s.background = { fill: C.white };
  addHeader(pres, s, { title: "Feature Coverage by Squad", eyebrow: "FEATURES MAP", page: 3 });

  // Table header
  const cols = ["Squad", "Total", "Live", "Planned", "Figma-Only", "BRD-Only", "Coverage"];
  const colW = [2.4, 0.7, 0.7, 0.9, 1.0, 1.0, 5.6];
  const tX = M;
  const tY = 1.2;
  const rowH = 0.42;

  // Header row
  cols.forEach((c, i) => {
    let cx = tX;
    for (let j = 0; j < i; j++) cx += colW[j];
    s.addShape(pres.shapes.RECTANGLE, {
      x: cx, y: tY, w: colW[i], h: rowH,
      fill: { color: C.navy }, line: { width: 0 },
    });
    s.addText(c, {
      x: cx + 0.08, y: tY, w: colW[i] - 0.16, h: rowH,
      fontFace: F.body, fontSize: 8.5, bold: true, color: C.white, margin: 0,
      align: i === 0 ? "left" : (i === 6 ? "left" : "center"), valign: "middle",
    });
  });

  // Data rows
  SQUADS.forEach((sq, ri) => {
    const ry = tY + rowH + ri * rowH;
    const bg = ri % 2 === 0 ? C.white : C.slate100;
    const vals = [sq.name, sq.total, sq.live, sq.planned, sq.figmaOnly, sq.brdOnly];

    vals.forEach((v, ci) => {
      let cx = tX;
      for (let j = 0; j < ci; j++) cx += colW[j];
      s.addShape(pres.shapes.RECTANGLE, {
        x: cx, y: ry, w: colW[ci], h: rowH,
        fill: { color: bg }, line: { color: C.line, width: 0.25 },
      });
      let fc = C.ink;
      if (ci === 2) fc = C.positive;
      if (ci === 4) fc = C.critical;
      if (ci === 5) fc = C.insight;
      s.addText(String(v), {
        x: cx + 0.08, y: ry, w: colW[ci] - 0.16, h: rowH,
        fontFace: ci === 0 ? F.body : F.num, fontSize: ci === 0 ? 9 : 10,
        bold: ci === 0 || ci === 1, color: fc, margin: 0,
        align: ci === 0 ? "left" : "center", valign: "middle",
      });
    });

    // Coverage bar in last column
    let cx = tX;
    for (let j = 0; j < 6; j++) cx += colW[j];
    s.addShape(pres.shapes.RECTANGLE, {
      x: cx, y: ry, w: colW[6], h: rowH,
      fill: { color: bg }, line: { color: C.line, width: 0.25 },
    });

    const barX = cx + 0.15;
    const barW = colW[6] - 0.3;
    const barY = ry + 0.11;
    const barH = 0.2;

    // Stacked bar: live (green) + brdFigma (teal) + brdOnly (blue) + figmaOnly (red)
    const segments = [
      { count: sq.live, color: C.positive },
      { count: sq.brdFigma - sq.live, color: C.stable },
      { count: sq.brdOnly, color: C.insight },
      { count: sq.figmaOnly, color: C.critical },
    ];
    let offset = 0;
    segments.forEach(seg => {
      if (seg.count > 0) {
        const segW = (seg.count / sq.total) * barW;
        s.addShape(pres.shapes.RECTANGLE, {
          x: barX + offset, y: barY, w: segW, h: barH,
          fill: { color: seg.color }, line: { width: 0 },
        });
        offset += segW;
      }
    });
    // Background for remainder
    if (offset < barW) {
      s.addShape(pres.shapes.RECTANGLE, {
        x: barX + offset, y: barY, w: barW - offset, h: barH,
        fill: { color: C.slate200 }, line: { width: 0 },
      });
    }
  });

  // Legend
  const legY = tY + rowH + SQUADS.length * rowH + 0.3;
  const legItems = [
    { label: "Live", color: C.positive },
    { label: "BRD + Figma", color: C.stable },
    { label: "BRD Only", color: C.insight },
    { label: "Figma Only", color: C.critical },
  ];
  legItems.forEach((l, i) => {
    const lx = M + i * 2.5;
    s.addShape(pres.shapes.RECTANGLE, {
      x: lx, y: legY + 0.05, w: 0.2, h: 0.2,
      fill: { color: l.color }, line: { width: 0 },
    });
    s.addText(l.label, {
      x: lx + 0.28, y: legY, w: 1.5, h: 0.3,
      fontFace: F.body, fontSize: 8.5, color: C.slate700, margin: 0, valign: "middle",
    });
  });

  // Insight
  card(pres, s, { x: M, y: legY + 0.55, w: W - 2*M, h: 0.7, fill: C.opportunitySoft });
  addTag(pres, s, "OBSERVATION", { x: M + 0.2, y: legY + 0.62, w: 1.2, tone: "opportunity" });
  s.addText("Saudi Trading (37) and Portfolio Monitoring (21) are the largest modules. Corporate Actions (4) and Robo Advisory (4) are the leanest — high expansion potential. 0 features live in Corporate Actions.", {
    x: M + 1.6, y: legY + 0.6, w: 10.5, h: 0.6,
    fontFace: F.body, fontSize: 9, color: C.slate700, margin: 0, valign: "middle",
  });

  addFooter(pres, s, { source: "Features Inventory · 164 features across 12 squads", dateLabel: DATE_LABEL });
}

// ── SLIDE 4: TOP 15 PRIORITY GAPS ───────────────────────────────────────
{
  const s = pres.addSlide();
  s.background = { fill: C.white };
  addHeader(pres, s, { title: "Top 15 Priority Gaps — Ranked by Impact", eyebrow: "COMPETITIVE INTELLIGENCE", page: 4 });

  const tY = 1.15;
  const rowH = 0.36;
  const gapCols = ["#", "Gap Feature", "Score", "Squad", "Competitors With It"];
  const gapColW = [0.35, 3.5, 0.65, 2.2, 5.6];

  // Header
  gapCols.forEach((c, i) => {
    let cx = M;
    for (let j = 0; j < i; j++) cx += gapColW[j];
    s.addShape(pres.shapes.RECTANGLE, {
      x: cx, y: tY, w: gapColW[i], h: rowH,
      fill: { color: C.critical }, line: { width: 0 },
    });
    s.addText(c, {
      x: cx + 0.06, y: tY, w: gapColW[i] - 0.12, h: rowH,
      fontFace: F.body, fontSize: 8, bold: true, color: C.white, margin: 0,
      align: i <= 1 ? "left" : (i === 2 ? "center" : "left"), valign: "middle",
    });
  });

  // Rows
  TOP_GAPS.forEach((g, ri) => {
    const ry = tY + rowH + ri * rowH;
    const bg = ri % 2 === 0 ? C.white : C.criticalSoft;
    const vals = [g.rank, g.name, g.score + "/25", g.squad, g.competitors];

    vals.forEach((v, ci) => {
      let cx = M;
      for (let j = 0; j < ci; j++) cx += gapColW[j];
      s.addShape(pres.shapes.RECTANGLE, {
        x: cx, y: ry, w: gapColW[ci], h: rowH,
        fill: { color: bg }, line: { color: C.line, width: 0.25 },
      });
      let fc = C.ink;
      if (ci === 2) fc = g.score === 25 ? C.critical : C.opportunity;
      s.addText(String(v), {
        x: cx + 0.06, y: ry, w: gapColW[ci] - 0.12, h: rowH,
        fontFace: ci === 0 || ci === 2 ? F.num : F.body,
        fontSize: ci === 2 ? 9 : 8.5,
        bold: ci <= 2, color: fc, margin: 0,
        align: ci <= 1 ? "left" : (ci === 2 ? "center" : "left"), valign: "middle",
      });
    });
  });

  // Score formula
  const fY = tY + rowH + TOP_GAPS.length * rowH + 0.15;
  s.addText("Priority Score = Competitive Pressure (1-5)  ×  Investor Demand (1-5)  ·  Max: 25", {
    x: M, y: fY, w: 8, h: 0.25,
    fontFace: F.body, fontSize: 8.5, italic: true, color: C.slate600, margin: 0,
  });

  addFooter(pres, s, { source: "Competitor Gap Matrix · 10+ benchmarks · Moomoo, Derayah, AlJazira, Sahm, Investing.com, IBKR", dateLabel: DATE_LABEL });
}

// ── SLIDE 5: GAP DISTRIBUTION VISUAL ────────────────────────────────────
{
  const s = pres.addSlide();
  s.background = { fill: C.white };
  addHeader(pres, s, { title: "Gap Distribution by Squad", eyebrow: "COMPETITIVE INTELLIGENCE", page: 5 });

  const gapSquads = [
    { name: "US Trading", gaps: 15, topScore: 25 },
    { name: "Saudi Trading", gaps: 11, topScore: 25 },
    { name: "Mutual Funds", gaps: 5, topScore: 20 },
    { name: "Portfolio Monitoring", gaps: 4, topScore: 20 },
    { name: "Robo Advisory", gaps: 4, topScore: 15 },
    { name: "Onboarding", gaps: 3, topScore: null },
    { name: "Investor Engagement", gaps: 3, topScore: 20 },
    { name: "IPOs", gaps: 2, topScore: null },
    { name: "Cross-Journey", gaps: 1, topScore: 16 },
    { name: "Wealth Visibility", gaps: 1, topScore: null },
    { name: "Corporate Actions", gaps: 1, topScore: null },
  ];

  const maxGaps = 15;
  const barStartX = M + 2.4;
  const barMaxW = 5.5;
  const bY = 1.3;

  gapSquads.forEach((gs, i) => {
    const ry = bY + i * 0.48;
    s.addText(gs.name, {
      x: M, y: ry, w: 2.3, h: 0.35,
      fontFace: F.body, fontSize: 9, color: C.ink, margin: 0, align: "right", valign: "middle",
    });

    const pct = gs.gaps / maxGaps;
    const barColor = gs.gaps >= 10 ? C.critical : (gs.gaps >= 4 ? C.opportunity : C.slate400);
    hBar(pres, s, { x: barStartX, y: ry + 0.06, w: barMaxW, h: 0.24, pct, color: barColor });

    s.addText(String(gs.gaps), {
      x: barStartX + barMaxW * pct + 0.15, y: ry, w: 0.5, h: 0.35,
      fontFace: F.num, fontSize: 10, bold: true, color: barColor, margin: 0, valign: "middle",
    });

    if (gs.topScore) {
      s.addText(`Top: ${gs.topScore}/25`, {
        x: barStartX + barMaxW * pct + 0.65, y: ry, w: 1.2, h: 0.35,
        fontFace: F.body, fontSize: 8, color: C.slate600, margin: 0, valign: "middle",
      });
    }
  });

  // Right panel: new gaps from Sahm analysis
  const rX = 9;
  card(pres, s, { x: rX, y: 1.3, w: 3.8, h: 4.5 });
  s.addText("New Gaps (Sahm Analysis)", {
    x: rX + 0.2, y: 1.4, w: 3.4, h: 0.3,
    fontFace: F.head, fontSize: 10, bold: true, color: C.ink, margin: 0,
  });
  s.addText("15 additional gaps identified from International Brokerage gap analysis (March 2026)", {
    x: rX + 0.2, y: 1.72, w: 3.4, h: 0.4,
    fontFace: F.body, fontSize: 8, color: C.slate600, margin: 0,
  });

  NEW_GAPS_SAHM.forEach((ng, i) => {
    const ny = 2.25 + i * 0.38;
    s.addText(ng.id, {
      x: rX + 0.2, y: ny, w: 0.55, h: 0.28,
      fontFace: F.num, fontSize: 8, bold: true, color: C.critical, margin: 0,
    });
    s.addText(ng.name, {
      x: rX + 0.75, y: ny, w: 2.2, h: 0.28,
      fontFace: F.body, fontSize: 8.5, color: C.ink, margin: 0,
    });
    s.addText(String(ng.score), {
      x: rX + 3.0, y: ny, w: 0.6, h: 0.28,
      fontFace: F.num, fontSize: 9, bold: true, color: ng.score >= 20 ? C.critical : C.opportunity, margin: 0, align: "center",
    });
  });

  // Bottom insight
  const insY = 6.1;
  card(pres, s, { x: M, y: insY, w: W - 2*M, h: 0.7, fill: C.criticalSoft });
  addTag(pres, s, "CRITICAL", { x: M + 0.2, y: insY + 0.08, w: 1.0, tone: "critical" });
  s.addText("US Trading and Saudi Trading account for 54% of all gaps (26 of 48 original + 14 of 15 Sahm gaps). These two squads face the highest competitive pressure and need the most feature investment.", {
    x: M + 1.4, y: insY + 0.02, w: 10.7, h: 0.65,
    fontFace: F.body, fontSize: 9, color: C.slate700, margin: 0, valign: "middle",
  });

  addFooter(pres, s, { source: "Competitor Gap Matrix + Sahm Int'l Brokerage Analysis · 2026-03-26", dateLabel: DATE_LABEL });
}

// ── SLIDE 6: ARC DIFFERENTIATORS ────────────────────────────────────────
{
  const s = pres.addSlide();
  s.background = { fill: C.white };
  addHeader(pres, s, { title: "ARC Differentiators — 14 Unique Advantages", eyebrow: "COMPETITIVE POSITION", page: 6 });

  const cardW = 3.85;
  const cardH = 1.2;
  const gapX = 0.3;
  const gapY = 0.25;
  const startX = M;
  const startY = 1.2;
  const cols = 3;

  DIFFERENTIATORS.forEach((d, i) => {
    const col = i % cols;
    const row = Math.floor(i / cols);
    const cx = startX + col * (cardW + gapX);
    const cy = startY + row * (cardH + gapY);

    card(pres, s, { x: cx, y: cy, w: cardW, h: cardH, fill: C.positiveSoft });
    s.addText(`D-${String(i + 1).padStart(2, "0")}`, {
      x: cx + 0.12, y: cy + 0.1, w: 0.5, h: 0.2,
      fontFace: F.num, fontSize: 8, bold: true, color: C.positive, margin: 0,
    });
    s.addText(d.name, {
      x: cx + 0.12, y: cy + 0.3, w: cardW - 0.24, h: 0.35,
      fontFace: F.body, fontSize: 9.5, bold: true, color: C.ink, margin: 0,
    });
    s.addText(d.why, {
      x: cx + 0.12, y: cy + 0.65, w: cardW - 0.24, h: 0.48,
      fontFace: F.body, fontSize: 7.5, color: C.slate700, margin: 0,
    });
  });

  // Bottom insight
  card(pres, s, { x: M, y: 6.2, w: W - 2*M, h: 0.65, fill: C.positiveSoft });
  addTag(pres, s, "STRENGTH", { x: M + 0.2, y: 6.28, w: 1.0, tone: "positive" });
  s.addText("ARC's moat is Sharia-first financial infrastructure (Murabaha, Purification, Zakat) + Al Rajhi ecosystem integration (Mokafaa, ARG bundles). These are non-replicable by standalone fintech competitors.", {
    x: M + 1.4, y: 6.24, w: 10.7, h: 0.55,
    fontFace: F.body, fontSize: 9, color: C.slate700, margin: 0, valign: "middle",
  });

  addFooter(pres, s, { source: "Competitor Gap Matrix · 10+ competitor benchmarks · 2026-03-26", dateLabel: DATE_LABEL });
}

// ── SLIDES 7-9: SQUAD DETAILS (3 slides, ~4 squads each) ───────────────
function buildSquadDetailSlide(pres, squadsSlice, pageNum, subtitle) {
  const s = pres.addSlide();
  s.background = { fill: C.white };
  addHeader(pres, s, { title: subtitle, eyebrow: "SQUAD DETAIL", page: pageNum });

  const cardW = (W - 2 * M - 0.3) / 2;
  const cardH = 2.6;

  squadsSlice.forEach((sq, i) => {
    const col = i % 2;
    const row = Math.floor(i / 2);
    const cx = M + col * (cardW + 0.3);
    const cy = 1.2 + row * (cardH + 0.25);

    card(pres, s, { x: cx, y: cy, w: cardW, h: cardH });

    // Squad name
    s.addText(sq.name, {
      x: cx + 0.2, y: cy + 0.12, w: cardW - 1.8, h: 0.3,
      fontFace: F.head, fontSize: 12, bold: true, color: C.ink, margin: 0,
    });
    // Total
    s.addText(String(sq.total), {
      x: cx + cardW - 1.5, y: cy + 0.08, w: 0.6, h: 0.35,
      fontFace: F.num, fontSize: 20, bold: true, color: C.brand, margin: 0, align: "center",
    });
    s.addText("features", {
      x: cx + cardW - 0.95, y: cy + 0.15, w: 0.8, h: 0.25,
      fontFace: F.body, fontSize: 8, color: C.slate600, margin: 0,
    });

    // Mini stats
    const miniY = cy + 0.55;
    const miniItems = [
      { label: "Live", val: sq.live, color: C.positive },
      { label: "Planned", val: sq.planned, color: C.opportunity },
      { label: "Figma-Only", val: sq.figmaOnly, color: C.critical },
      { label: "BRD-Only", val: sq.brdOnly, color: C.insight },
    ];
    miniItems.forEach((mi, j) => {
      const mx = cx + 0.2 + j * 1.45;
      s.addText(String(mi.val), {
        x: mx, y: miniY, w: 0.5, h: 0.25,
        fontFace: F.num, fontSize: 12, bold: true, color: mi.color, margin: 0,
      });
      s.addText(mi.label, {
        x: mx + 0.5, y: miniY, w: 0.9, h: 0.25,
        fontFace: F.body, fontSize: 8, color: C.slate600, margin: 0, valign: "middle",
      });
    });

    // Stacked bar
    const barY = miniY + 0.38;
    const barW = cardW - 0.4;
    const segments = [
      { count: sq.live, color: C.positive },
      { count: sq.brdFigma - sq.live, color: C.stable },
      { count: sq.brdOnly, color: C.insight },
      { count: sq.figmaOnly, color: C.critical },
    ];
    let offset = 0;
    // Background bar
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, {
      x: cx + 0.2, y: barY, w: barW, h: 0.18,
      fill: { color: C.slate200 }, line: { width: 0 }, rectRadius: 0.09,
    });
    segments.forEach(seg => {
      if (seg.count > 0) {
        const segW = (seg.count / sq.total) * barW;
        s.addShape(pres.shapes.RECTANGLE, {
          x: cx + 0.2 + offset, y: barY, w: segW, h: 0.18,
          fill: { color: seg.color }, line: { width: 0 },
        });
        offset += segW;
      }
    });

    // Gaps section
    const gapY = barY + 0.35;
    s.addShape(pres.shapes.LINE, {
      x: cx + 0.2, y: gapY, w: cardW - 0.4, h: 0,
      line: { color: C.line, width: 0.5 },
    });
    s.addText(`${sq.gapCount} Competitive Gap${sq.gapCount !== 1 ? "s" : ""}`, {
      x: cx + 0.2, y: gapY + 0.08, w: 2.5, h: 0.22,
      fontFace: F.body, fontSize: 9, bold: true, color: C.critical, margin: 0,
    });
    if (sq.topGap) {
      s.addText(`Top: ${sq.topGap}${sq.gapScore ? " (" + sq.gapScore + "/25)" : ""}`, {
        x: cx + 0.2, y: gapY + 0.32, w: cardW - 0.4, h: 0.2,
        fontFace: F.body, fontSize: 8.5, color: C.slate700, margin: 0,
      });
    }

    // Live percentage
    const livePct = Math.round((sq.live / sq.total) * 100);
    s.addText(`${livePct}% live`, {
      x: cx + 0.2, y: cy + cardH - 0.45, w: 2, h: 0.25,
      fontFace: F.body, fontSize: 9, bold: true,
      color: livePct >= 30 ? C.positive : (livePct >= 15 ? C.opportunity : C.critical),
      margin: 0,
    });
  });

  addFooter(pres, s, { source: "Features Inventory · BRDs + Figma API", dateLabel: DATE_LABEL });
}

buildSquadDetailSlide(pres, SQUADS.slice(0, 4), 7, "Squad Detail — Trading & Portfolio");
buildSquadDetailSlide(pres, SQUADS.slice(4, 8), 8, "Squad Detail — Wealth, Funds & IPOs");
buildSquadDetailSlide(pres, SQUADS.slice(8, 11), 9, "Squad Detail — Engagement & Cross-Journey");

// ── SLIDE 10: FEATURE STATUS MATRIX (BUBBLE MAP) ───────────────────────
{
  const s = pres.addSlide();
  s.background = { fill: C.white };
  addHeader(pres, s, { title: "Feature Readiness Matrix", eyebrow: "PLATFORM READINESS", page: 10 });

  // X axis: Documentation (BRD status) / Y axis: Design (Figma status)
  // Quadrants
  const qX = M + 1.5, qY = 1.3, qW = 5, qH = 5;

  // Quadrant backgrounds
  const quads = [
    { x: qX, y: qY, label: "PLANNED ONLY\n(BRD, no design)", count: 68, color: C.insightSoft, txtColor: C.insight },
    { x: qX + qW/2, y: qY, label: "READY TO BUILD\n(BRD + Figma)", count: 44, color: C.positiveSoft, txtColor: C.positive },
    { x: qX, y: qY + qH/2, label: "NO DOCUMENTATION\n(Unknown/Gap)", count: 1, color: C.slate100, txtColor: C.slate600 },
    { x: qX + qW/2, y: qY + qH/2, label: "DESIGN ONLY\n(Figma, no BRD)", count: 42, color: C.criticalSoft, txtColor: C.critical },
  ];

  quads.forEach(q => {
    s.addShape(pres.shapes.RECTANGLE, {
      x: q.x, y: q.y, w: qW/2, h: qH/2,
      fill: { color: q.color }, line: { color: C.line, width: 0.5 },
    });
    s.addText(String(q.count), {
      x: q.x, y: q.y + 0.3, w: qW/2, h: 0.8,
      fontFace: F.num, fontSize: 42, bold: true, color: q.txtColor, align: "center", margin: 0, transparency: 20,
    });
    s.addText(q.label, {
      x: q.x, y: q.y + qH/4 - 0.3, w: qW/2, h: 0.6,
      fontFace: F.body, fontSize: 9, color: q.txtColor, align: "center", margin: 0,
    });
  });

  // Axis labels
  s.addText("BRD EXISTS", {
    x: qX, y: qY - 0.3, w: qW/2, h: 0.25,
    fontFace: F.body, fontSize: 8, bold: true, color: C.ink, align: "center", margin: 0,
  });
  s.addText("BRD + FIGMA", {
    x: qX + qW/2, y: qY - 0.3, w: qW/2, h: 0.25,
    fontFace: F.body, fontSize: 8, bold: true, color: C.ink, align: "center", margin: 0,
  });

  s.addText("FIGMA\nEXISTS", {
    x: qX - 1.2, y: qY + qH/2, w: 1, h: qH/2,
    fontFace: F.body, fontSize: 8, bold: true, color: C.ink, align: "center", valign: "middle", margin: 0,
  });
  s.addText("NO\nFIGMA", {
    x: qX - 1.2, y: qY, w: 1, h: qH/2,
    fontFace: F.body, fontSize: 8, bold: true, color: C.ink, align: "center", valign: "middle", margin: 0,
  });

  // Right panel: What it means
  const rX = 7.5;
  card(pres, s, { x: rX, y: 1.3, w: 5.3, h: 5.2 });
  s.addText("What This Means", {
    x: rX + 0.2, y: 1.4, w: 4, h: 0.3,
    fontFace: F.head, fontSize: 12, bold: true, color: C.ink, margin: 0,
  });

  const insights = [
    { icon: "44", label: "Ready to Build", desc: "Both BRD and Figma exist. These features can enter development sprint planning immediately. Only 24 of these are actually live.", color: C.positive },
    { icon: "68", label: "Need Design", desc: "BRD approved but no Figma screens in the revamp. Design team must prioritize these to unblock development.", color: C.insight },
    { icon: "42", label: "Need BRD", desc: "Designed in Figma but no formal product requirements. Squad leads must write BRDs to formalize scope and acceptance criteria.", color: C.critical },
    { icon: "24", label: "Live Today", desc: "Actually in production. This is only 16% of total inventory — the platform has massive unrealized potential.", color: C.positive },
  ];
  insights.forEach((ins, i) => {
    const iy = 1.85 + i * 1.1;
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, {
      x: rX + 0.3, y: iy, w: 0.65, h: 0.65,
      fill: { color: ins.color }, line: { width: 0 }, rectRadius: 0.06,
    });
    s.addText(ins.icon, {
      x: rX + 0.3, y: iy, w: 0.65, h: 0.65,
      fontFace: F.num, fontSize: 18, bold: true, color: C.white, align: "center", valign: "middle", margin: 0,
    });
    s.addText(ins.label, {
      x: rX + 1.1, y: iy + 0.02, w: 3.5, h: 0.22,
      fontFace: F.body, fontSize: 10, bold: true, color: C.ink, margin: 0,
    });
    s.addText(ins.desc, {
      x: rX + 1.1, y: iy + 0.28, w: 4, h: 0.5,
      fontFace: F.body, fontSize: 8.5, color: C.slate700, margin: 0,
    });
  });

  addFooter(pres, s, { source: "Features Inventory cross-reference · BRDs + Figma API", dateLabel: DATE_LABEL });
}

// ── SLIDE 11: PARITY FEATURES ───────────────────────────────────────────
{
  const s = pres.addSlide();
  s.background = { fill: C.white };
  addHeader(pres, s, { title: "Parity Features — ARC Matches Market (33)", eyebrow: "COMPETITIVE POSITION", page: 11 });

  const parityGroups = [
    { category: "Trading", features: ["Market/Limit Orders (Saudi)", "US Market Orders", "Options Trading (Saudi + US)", "TradingView Charts", "Trending/Top Movers", "Commission-Free Bundles"] },
    { category: "Portfolio & Wealth", features: ["P&L Performance Chart", "Portfolio Insights", "Goal Tracker (Basic)", "Multi-Currency Wallet", "Asset Allocation"] },
    { category: "Funds & IPO", features: ["Mutual Fund Subscribe/Redeem", "Robo Advisory (Basic)", "IPO Subscription (Main + Nomu)", "Auto-Subscribe Engine"] },
    { category: "Market Intelligence", features: ["Economic Calendar", "Earnings Calendar", "Dividends Calendar", "Analyst Ratings", "Insider/Gov't Trades", "News Feed", "Bulls vs Bears", "Why Is It Moving"] },
    { category: "Platform", features: ["Face ID / Biometric Login", "Digital KYC", "Guest / Discovery Mode", "Shariah Filter", "Social/Copy Trading", "CRM Case Management", "Buy Round-Up"] },
  ];

  let pyBase = 1.2;
  parityGroups.forEach((pg, gi) => {
    const gY = pyBase + gi * 1.1;
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, {
      x: M, y: gY, w: W - 2*M, h: 0.9,
      fill: { color: gi % 2 === 0 ? C.stableSoft : C.white },
      line: { color: C.line, width: 0.5 }, rectRadius: 0.06,
    });
    s.addText(pg.category, {
      x: M + 0.15, y: gY + 0.05, w: 2, h: 0.25,
      fontFace: F.head, fontSize: 10, bold: true, color: C.stable, margin: 0,
    });

    pg.features.forEach((feat, fi) => {
      const col = fi % 4;
      const row = Math.floor(fi / 4);
      const fx = M + 0.15 + col * 3.05;
      const fy = gY + 0.35 + row * 0.28;
      s.addText("  " + feat, {
        x: fx, y: fy, w: 3, h: 0.25,
        fontFace: F.body, fontSize: 8, color: C.ink, margin: 0, bullet: { type: "number", style: "checkMark", color: C.stable },
      });
    });
  });

  addFooter(pres, s, { source: "Competitor Gap Matrix · Parity analysis across 10+ benchmarks", dateLabel: DATE_LABEL });
}

// ── SLIDE 12: FIGMA SCREEN INVENTORY ────────────────────────────────────
{
  const s = pres.addSlide();
  s.background = { fill: C.white };
  addHeader(pres, s, { title: "Figma Screen Inventory — 157 Screens Across 8 Files", eyebrow: "DESIGN COVERAGE", page: 12 });

  const figmaFiles = [
    { name: "OnBoarding KYC", screens: 23, pages: 1, key: "PgN7nzg8C…" },
    { name: "Home", screens: 3, pages: 1, key: "KbRt2Jimf…" },
    { name: "Tradepad", screens: 4, pages: 1, key: "PXgN11AxL…" },
    { name: "Market", screens: 4, pages: 1, key: "p7TSYYTNe…" },
    { name: "Portfolios", screens: 53, pages: 3, key: "4ybkyLURb…" },
    { name: "Discover (IPO)", screens: 12, pages: 1, key: "PEMRwaRLp…" },
    { name: "Profile & Setting", screens: 10, pages: 1, key: "cMRqMd2ow…" },
    { name: "Orders", screens: 48, pages: 1, key: "BhwWZvTq5…" },
  ];

  const totalScreens = figmaFiles.reduce((s, f) => s + f.screens, 0);
  const maxScreens = 53; // Portfolios

  const bStartX = M + 2.8;
  const bMaxW = 6;
  const startY = 1.3;

  figmaFiles.forEach((ff, i) => {
    const ry = startY + i * 0.62;
    // File name
    s.addText(ff.name, {
      x: M, y: ry, w: 2.5, h: 0.4,
      fontFace: F.body, fontSize: 10, bold: true, color: C.ink, margin: 0, align: "right", valign: "middle",
    });

    // Bar
    const pct = ff.screens / maxScreens;
    const barColor = ff.screens >= 40 ? C.brand : (ff.screens >= 10 ? C.insight : C.slate400);
    hBar(pres, s, { x: bStartX, y: ry + 0.08, w: bMaxW, h: 0.28, pct, color: barColor });

    s.addText(String(ff.screens), {
      x: bStartX + bMaxW * pct + 0.15, y: ry, w: 0.6, h: 0.4,
      fontFace: F.num, fontSize: 12, bold: true, color: barColor, margin: 0, valign: "middle",
    });

    s.addText(`${ff.pages} page${ff.pages > 1 ? "s" : ""}`, {
      x: bStartX + bMaxW * pct + 0.75, y: ry, w: 1, h: 0.4,
      fontFace: F.body, fontSize: 8, color: C.slate600, margin: 0, valign: "middle",
    });
  });

  // Summary stats on right
  const rsX = 10;
  card(pres, s, { x: rsX, y: 1.3, w: 2.8, h: 2.5 });
  bigNum(s, { x: rsX + 0.5, y: 1.5, num: totalScreens, label: "Total Screens", color: C.brand });
  s.addShape(pres.shapes.LINE, {
    x: rsX + 0.4, y: 2.55, w: 2, h: 0,
    line: { color: C.line, width: 0.5 },
  });
  bigNum(s, { x: rsX + 0.5, y: 2.7, num: 8, label: "Figma Files", color: C.insight });

  // Observations
  const obsY = 6.0;
  card(pres, s, { x: M, y: obsY, w: W - 2*M, h: 0.85, fill: C.insightSoft });
  addTag(pres, s, "DESIGN DENSITY", { x: M + 0.2, y: obsY + 0.08, w: 1.3, tone: "insight" });
  s.addText("Portfolios (53 screens) and Orders (48 screens) dominate design effort — together they hold 64% of all screens. Home has only 3 screens, suggesting the revamp home is minimalist or work-in-progress. Watchlist file is empty.", {
    x: M + 1.7, y: obsY + 0.02, w: 10.5, h: 0.78,
    fontFace: F.body, fontSize: 9, color: C.slate700, margin: 0, valign: "middle",
  });

  addFooter(pres, s, { source: "Figma REST API · depth-3 extraction · 8 design files · 2026-03-26", dateLabel: DATE_LABEL });
}

// ── SLIDE 13: COMPETITIVE LANDSCAPE OVERVIEW ────────────────────────────
{
  const s = pres.addSlide();
  s.background = { fill: C.white };
  addHeader(pres, s, { title: "Competitive Landscape — Who Leads Where", eyebrow: "COMPETITIVE INTELLIGENCE", page: 13 });

  const competitors = [
    { name: "Moomoo", strengths: "Level 2 depth, AI assistant, stock comparison, community feed, money flow, paper trading, fractional shares", gapsVsArc: 12, color: C.critical },
    { name: "Derayah / Smart", strengths: "Conditional orders, Apple Pay, SIP, goal-based investing, pre-filled KYC, dividend reinvestment, progress indicator", gapsVsArc: 9, color: C.critical },
    { name: "AlJazira Capital", strengths: "Private funds (10+), SIP, Nomu institutional IPO, IPO popup banners", gapsVsArc: 4, color: C.opportunity },
    { name: "Sahm", strengths: "Tab navigation, live prices free, personalized calendar, social proof nudges, always-on price view, demo mode", gapsVsArc: 11, color: C.critical },
    { name: "Investing.com", strengths: "Stock screener, multi-type alerts, fundamental data, ETF exposure, economic/earnings calendars", gapsVsArc: 5, color: C.opportunity },
    { name: "IBKR / Global", strengths: "Pre/post market, fractional shares, L2 depth, bonds, futures, advanced order types", gapsVsArc: 7, color: C.opportunity },
  ];

  const cardW = (W - 2*M - 0.5) / 2;

  competitors.forEach((comp, i) => {
    const col = i % 2;
    const row = Math.floor(i / 2);
    const cx = M + col * (cardW + 0.5);
    const cy = 1.2 + row * 1.85;

    card(pres, s, { x: cx, y: cy, w: cardW, h: 1.65 });

    // Name + gap count
    s.addText(comp.name, {
      x: cx + 0.2, y: cy + 0.1, w: cardW - 1.5, h: 0.3,
      fontFace: F.head, fontSize: 12, bold: true, color: C.ink, margin: 0,
    });
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, {
      x: cx + cardW - 1.2, y: cy + 0.12, w: 1, h: 0.28,
      fill: { color: comp.color }, line: { width: 0 }, rectRadius: 0.04,
    });
    s.addText(`${comp.gapsVsArc} gaps`, {
      x: cx + cardW - 1.2, y: cy + 0.12, w: 1, h: 0.28,
      fontFace: F.num, fontSize: 9, bold: true, color: C.white, align: "center", valign: "middle", margin: 0,
    });

    // Strengths
    s.addText("Key advantages over ARC:", {
      x: cx + 0.2, y: cy + 0.48, w: cardW - 0.4, h: 0.2,
      fontFace: F.body, fontSize: 8, bold: true, color: C.slate600, margin: 0,
    });
    s.addText(comp.strengths, {
      x: cx + 0.2, y: cy + 0.7, w: cardW - 0.4, h: 0.85,
      fontFace: F.body, fontSize: 8.5, color: C.slate700, margin: 0,
    });
  });

  addFooter(pres, s, { source: "Benchmark reports: Moomoo, Derayah, AlJazira, Sahm, Investing.com, IBKR · 2024-2025", dateLabel: DATE_LABEL });
}

// ── SLIDE 14: DOCUMENTATION DEBT ────────────────────────────────────────
{
  const s = pres.addSlide();
  s.background = { fill: C.white };
  addHeader(pres, s, { title: "Documentation Debt — Action Required", eyebrow: "GOVERNANCE", page: 14 });

  // Left: Figma-only features needing BRDs
  const figmaOnlySquads = SQUADS.filter(sq => sq.figmaOnly > 0);
  card(pres, s, { x: M, y: 1.2, w: 5.8, h: 5.5 });
  s.addText("42 Features Need BRDs", {
    x: M + 0.2, y: 1.3, w: 5, h: 0.3,
    fontFace: F.head, fontSize: 12, bold: true, color: C.critical, margin: 0,
  });
  s.addText("Designed in Figma but no formal requirements written. Squad leads must author BRDs.", {
    x: M + 0.2, y: 1.62, w: 5.2, h: 0.35,
    fontFace: F.body, fontSize: 8.5, color: C.slate600, margin: 0,
  });

  figmaOnlySquads.forEach((sq, i) => {
    const ry = 2.15 + i * 0.45;
    s.addText(sq.name, {
      x: M + 0.3, y: ry, w: 2.3, h: 0.32,
      fontFace: F.body, fontSize: 9, color: C.ink, margin: 0, align: "right", valign: "middle",
    });
    hBar(pres, s, { x: M + 2.8, y: ry + 0.06, w: 2, h: 0.2, pct: sq.figmaOnly / 12, color: C.critical });
    s.addText(String(sq.figmaOnly), {
      x: M + 5, y: ry, w: 0.5, h: 0.32,
      fontFace: F.num, fontSize: 10, bold: true, color: C.critical, margin: 0, valign: "middle",
    });
  });

  // Right: BRD-only features needing Figma
  card(pres, s, { x: 6.8, y: 1.2, w: 6, h: 5.5 });
  s.addText("68 Features Need Figma Screens", {
    x: 7, y: 1.3, w: 5, h: 0.3,
    fontFace: F.head, fontSize: 12, bold: true, color: C.insight, margin: 0,
  });
  s.addText("BRD approved but not yet incorporated into the Figma revamp. Design team to prioritize.", {
    x: 7, y: 1.62, w: 5.5, h: 0.35,
    fontFace: F.body, fontSize: 8.5, color: C.slate600, margin: 0,
  });

  const brdOnlySquads = SQUADS.filter(sq => sq.brdOnly > 0);
  brdOnlySquads.forEach((sq, i) => {
    const ry = 2.15 + i * 0.45;
    s.addText(sq.name, {
      x: 7.1, y: ry, w: 2.3, h: 0.32,
      fontFace: F.body, fontSize: 9, color: C.ink, margin: 0, align: "right", valign: "middle",
    });
    hBar(pres, s, { x: 9.6, y: ry + 0.06, w: 2.2, h: 0.2, pct: sq.brdOnly / 19, color: C.insight });
    s.addText(String(sq.brdOnly), {
      x: 12, y: ry, w: 0.5, h: 0.32,
      fontFace: F.num, fontSize: 10, bold: true, color: C.insight, margin: 0, valign: "middle",
    });
  });

  // Bottom action card
  card(pres, s, { x: M, y: 6.0, w: W - 2*M, h: 0.85, fill: C.opportunitySoft });
  addTag(pres, s, "ACTION REQUIRED", { x: M + 0.2, y: 6.08, w: 1.4, tone: "opportunity" });
  s.addText("Squad validation deadline was April 7, 2026 — now 14 days overdue. Ahmed must follow up with squad leads to confirm live status and ownership. Until validated, the features map cannot be used as roadmap input with confidence.", {
    x: M + 1.8, y: 6.02, w: 10.4, h: 0.78,
    fontFace: F.body, fontSize: 9, color: C.slate700, margin: 0, valign: "middle",
  });

  addFooter(pres, s, { source: "Features Inventory · Squad Validation Checklist (deadline: 2026-04-07)", dateLabel: DATE_LABEL });
}

// ── SLIDE 15: STRATEGIC RECOMMENDATIONS ─────────────────────────────────
{
  const s = pres.addSlide();
  s.background = { fill: C.white };
  addHeader(pres, s, { title: "Strategic Recommendations", eyebrow: "FEATURES MAP", page: 15 });

  const recs = [
    {
      num: "01", title: "Close Documentation Gap — 42 BRDs + 68 Figma Screens",
      desc: "42 features have Figma designs without BRDs (no requirements). 68 have BRDs without Figma screens (no design). Cross-reference and close both sides. Without this, roadmap accuracy is guesswork.",
      owner: "Squad Leads + Design Team", priority: "URGENT", tone: "critical",
    },
    {
      num: "02", title: "Address Top 4 Score-25 Gaps Immediately",
      desc: "Level 2 Order Book, Stock Screener, Pre/Post-Market Trading, and Advanced TA Suite all scored maximum 25/25. These are the features active traders expect — losing users to Moomoo and Derayah is a real risk.",
      owner: "Saudi Trading + US Trading Squads", priority: "CRITICAL", tone: "critical",
    },
    {
      num: "03", title: "Complete Squad Validation (14 Days Overdue)",
      desc: "The April 7 deadline for squad leads to confirm feature live status has passed. Without validation, the 'Live' count of 24 is unverified and may be inaccurate. Send reminder and set new deadline.",
      owner: "Ahmed Alghamdi", priority: "HIGH", tone: "opportunity",
    },
    {
      num: "04", title: "Invest in Trading Experience Competitiveness",
      desc: "US Trading (15 gaps) and Saudi Trading (11 gaps) carry 54% of all competitive gaps. Allocate design and development resources proportionally. Trading is the core revenue driver.",
      owner: "Strategy & Intelligence", priority: "HIGH", tone: "opportunity",
    },
    {
      num: "05", title: "Leverage Sharia-First Differentiators in Marketing",
      desc: "ARC's 14 differentiators cluster around Sharia compliance (Murabaha, Purification, Zakat) and Al Rajhi ecosystem integration (Mokafaa, ARG bundles). These are non-replicable moats that should be front-and-center in positioning.",
      owner: "Head of Digital Experience", priority: "MEDIUM", tone: "positive",
    },
    {
      num: "06", title: "Expand Underdeveloped Modules",
      desc: "Corporate Actions (0 live, 4 total), Robo Advisory (1 live, 4 total), and Wealth Visibility (1 live, 5 total) are significantly underbuilt. Prioritize based on investor segment demand data.",
      owner: "Product Experience Design", priority: "MEDIUM", tone: "insight",
    },
  ];

  recs.forEach((r, i) => {
    const ry = 1.2 + i * 0.95;
    card(pres, s, { x: M, y: ry, w: W - 2*M, h: 0.85 });

    // Number badge
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, {
      x: M + 0.15, y: ry + 0.15, w: 0.5, h: 0.5,
      fill: { color: C.navy }, line: { width: 0 }, rectRadius: 0.06,
    });
    s.addText(r.num, {
      x: M + 0.15, y: ry + 0.15, w: 0.5, h: 0.5,
      fontFace: F.num, fontSize: 16, bold: true, color: C.white, align: "center", valign: "middle", margin: 0,
    });

    // Title + Priority tag
    s.addText(r.title, {
      x: M + 0.8, y: ry + 0.08, w: 8, h: 0.28,
      fontFace: F.body, fontSize: 10, bold: true, color: C.ink, margin: 0,
    });
    addTag(pres, s, r.priority, { x: M + 9, y: ry + 0.1, w: 0.9, tone: r.tone });

    // Description
    s.addText(r.desc, {
      x: M + 0.8, y: ry + 0.38, w: 9.5, h: 0.4,
      fontFace: F.body, fontSize: 8, color: C.slate700, margin: 0,
    });

    // Owner
    s.addText("Owner: " + r.owner, {
      x: M + 10.5, y: ry + 0.38, w: 2, h: 0.4,
      fontFace: F.body, fontSize: 7.5, italic: true, color: C.slate600, margin: 0, align: "right",
    });
  });

  addFooter(pres, s, { source: "Features Map synthesis · Competitor Gap Matrix · Squad Validation", dateLabel: DATE_LABEL });
}

// ── SLIDE 16: CLOSING ───────────────────────────────────────────────────
{
  const s = pres.addSlide();
  s.background = { fill: C.navyDeep };
  s.addShape(pres.shapes.RECTANGLE, {
    x: 0, y: 0, w: 0.06, h: H, fill: { color: C.brand },
  });

  s.addText("Features Map Summary", {
    x: M + 0.3, y: 1.5, w: 10, h: 0.6,
    fontFace: F.head, fontSize: 28, bold: true, color: C.white, margin: 0,
  });

  const summary = [
    "164 features mapped across 12 squads — 24 live (15%), 140 in pipeline",
    "62 competitive gaps identified — 4 at maximum severity (25/25)",
    "14 ARC differentiators — Sharia-first financial infrastructure + Al Rajhi ecosystem",
    "42 Figma designs with no BRD — design intent without product commitment",
    "68 BRDs with no Figma screens — requirements without design execution",
    "Squad validation 14 days overdue — follow up required immediately",
  ];

  summary.forEach((line, i) => {
    s.addText(line, {
      x: M + 0.6, y: 2.5 + i * 0.45, w: 10, h: 0.35,
      fontFace: F.body, fontSize: 12, color: C.slate200, margin: 0,
      bullet: { type: "number", style: "arabicPeriod", color: C.brand },
    });
  });

  s.addText("Next: Refresh Figma token → Deep component extraction → Platform parity matrix → Depth analysis", {
    x: M + 0.3, y: 5.5, w: 10, h: 0.3,
    fontFace: F.body, fontSize: 10, italic: true, color: C.slate400, margin: 0,
  });

  s.addText("Digital Experience Department  ·  Al Rajhi Capital  ·  " + DATE_LABEL, {
    x: M + 0.3, y: 6.5, w: 10, h: 0.25,
    fontFace: F.body, fontSize: 10, color: C.slate200, margin: 0,
  });
}

// ── SAVE ─────────────────────────────────────────────────────────────────
const outDir = path.join(__dirname, "reports");
const outFile = path.join(outDir, `features-map-${DATE_LABEL}.pptx`);

const fs = require("fs");
if (!fs.existsSync(outDir)) fs.mkdirSync(outDir, { recursive: true });

pres.writeFile({ fileName: outFile }).then(() => {
  console.log(`\n  Done → ${outFile}\n`);
}).catch(err => {
  console.error("Error:", err);
  process.exit(1);
});
