#!/usr/bin/env python3
"""Export all 164 features to Excel for squad validation."""
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from datetime import date

wb = openpyxl.Workbook()

# ── Styles ────────────────────────────────────────────────────────────────
navy = "0A1F4D"
brand = "0029FF"
green_fill = PatternFill(start_color="DCFCE7", end_color="DCFCE7", fill_type="solid")
blue_fill = PatternFill(start_color="EEF2FF", end_color="EEF2FF", fill_type="solid")
red_fill = PatternFill(start_color="FEE2E2", end_color="FEE2E2", fill_type="solid")
yellow_fill = PatternFill(start_color="FEF3C7", end_color="FEF3C7", fill_type="solid")
header_fill = PatternFill(start_color=navy, end_color=navy, fill_type="solid")
header_font = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
body_font = Font(name="Calibri", size=10)
bold_font = Font(name="Calibri", size=10, bold=True)
wrap = Alignment(wrap_text=True, vertical="top")
center = Alignment(horizontal="center", vertical="center", wrap_text=True)
thin_border = Border(
    left=Side(style="thin", color="D1D5DB"),
    right=Side(style="thin", color="D1D5DB"),
    top=Side(style="thin", color="D1D5DB"),
    bottom=Side(style="thin", color="D1D5DB"),
)

STATUS_FILL = {
    "Live": green_fill,
    "Planned": blue_fill,
    "Planned (Figma-only)": red_fill,
    "Unknown": yellow_fill,
    "NEW — Deep Extraction": yellow_fill,
}

# ── Feature Data ──────────────────────────────────────────────────────────
# (id, feature, description, status, source, brd_ref, squad)
FEATURES = [
    # Onboarding
    (1, "Digital Account Opening (Saudi Nationals)", "Standard onboarding journey for Saudi nationals to create an ARC investment account via SuperApp or SuperWeb.", "Live", "BRD + Figma", "ARCD-47480", "Onboarding"),
    (2, "GCC Customer Onboarding", "Onboarding flow for GCC clients with real-time identity document verification and face verification.", "Planned", "BRD + Figma", "ARCD-47480", "Onboarding"),
    (3, "Family Onboarding (Non-Saudi / Non-ARB)", "Enables ARC customers to digitally onboard non-Saudi and non-ARB family members.", "Planned", "BRD + Figma", "ARCD-26191", "Onboarding"),
    (4, "Expired ID Handling During Onboarding", "Automated workflow that detects expired national IDs at onboarding initiation.", "Planned", "BRD + Figma", "ARCD-73474", "Onboarding"),
    (5, "GCC Customer ID Update (Existing Clients)", "Dedicated workflow for existing GCC clients to update expired identification documents.", "Planned", "BRD + Figma", "ARCD-47480", "Onboarding"),
    (6, "Foreign Customer Identity Verification", "Real-time identity document verification and face scan for non-Saudi, non-GCC customers.", "Planned", "BRD + Figma", "ARCD-79680", "Onboarding"),
    (7, "FATCA / CRS KYC Indicia Update", "Allows existing clients to update their FATCA and CRS tax indicia.", "Planned", "BRD + Figma", "ARCD-58762", "Onboarding"),
    (8, "Minor Account Onboarding", "Guardian-initiated onboarding flow to create investment accounts for minor children.", "Live", "BRD + Figma", "ARCD 45978", "Onboarding"),
    (9, "Minor Trading Restrictions (Custodian Controls)", "Empowers guardians to configure trade amount limits, withdrawal limits, product access on minor accounts.", "Planned", "BRD", "ARCD 45978", "Onboarding"),
    (10, "Guardian Trading on Behalf of Minor", "Enables a guardian to execute trades on behalf of their linked minor's portfolio.", "Planned", "BRD + Figma", "Guardian Trade BRD", "Onboarding"),
    (11, "IBKR International Brokerage Onboarding", "Onboarding flow to create and activate an International Brokerage account backed by IBKR.", "Planned", "BRD + Figma", "ARCD-70106", "Onboarding"),
    (12, "Update National Address", "Self-service flow for clients to update their registered national address.", "Live", "BRD + Figma", "ARCD-14242", "Onboarding"),
    (13, "Session Upgrade & OTP Flow Enhancement", "One-time session upgrade for multiple high-value actions without repeated verification.", "Live", "BRD + Figma", "ARCD-84906", "Onboarding"),
    (14, "Splash Screen & App Launch", "Initial app splash screen shown on launch before authentication.", "Planned (Figma-only)", "Figma", "—", "Onboarding"),
    (15, "Login Screen", "Username/password login entry screen for existing clients.", "Planned (Figma-only)", "Figma", "—", "Onboarding"),
    (16, "Add / Create Password", "Screen for new clients to set up their account password during onboarding.", "Planned (Figma-only)", "Figma", "—", "Onboarding"),
    (17, "Face ID / Biometric Setup", "Setup screens for Face ID authentication (3-step flow).", "Planned (Figma-only)", "Figma", "—", "Onboarding"),
    (18, "Change Password", "Self-service flow for clients to update their account password.", "Planned (Figma-only)", "Figma", "—", "Onboarding"),
    (19, "Non-ARB Bank Account Info Entry", "Screen to capture external bank account details for clients without an ARB account.", "Planned (Figma-only)", "Figma", "—", "Onboarding"),
    (20, "KYC Confirmation / Message Screens", "Success, error, and informational modal screens across the KYC flow.", "Planned (Figma-only)", "Figma", "—", "Onboarding"),
    (21, "Home — Family Members Overview", "Screen showing all linked family member accounts accessible from the home screen.", "Planned (Figma-only)", "Figma", "—", "Onboarding"),
    # Saudi Trading
    (22, "Place Market Order (Saudi Market)", "Enables clients to place a buy or sell market order for Saudi Exchange stocks.", "Live", "BRD + Figma", "ARCD-14312", "Saudi Trading"),
    (23, "Place Limit Order (Saudi Market)", "Enables clients to place a limit buy or sell order at a specified price.", "Live", "BRD + Figma", "ARCD-1553", "Saudi Trading"),
    (24, "Market-on-Close (MOC) Order", "Conditional order type that executes at the Saudi market's official closing price.", "Planned", "BRD", "ARCD_9245", "Saudi Trading"),
    (25, "Apply for Margin Lending (Murabaha) via SuperApp", "Digital application flow for Murabaha margin lending through the SuperApp.", "Live", "BRD", "ARCD-1634", "Saudi Trading"),
    (26, "Automated Margin Lending Approval", "Automates Compliance and Risk approvals for margin lending applications.", "Planned", "BRD", "ARCD 1923", "Saudi Trading"),
    (27, "Margin Lending Contract Renewal", "Digital flow for renewing an existing Murabaha margin lending contract.", "Planned", "BRD", "ARCD-2367", "Saudi Trading"),
    (28, "Margin Lending Early Payment", "Allows clients to make early partial or full repayment on a Murabaha contract.", "Planned", "BRD", "ARCD-2367", "Saudi Trading"),
    (29, "Margin Lending Full Integration Phase 2 (Commodities)", "Integrates commodity contractor buy/sell execution and digital promissory notes.", "Planned", "BRD", "ARCD-2424", "Saudi Trading"),
    (30, "Derivatives (Options) Trading", "Full options trading capability on Saudi Exchange (DOTS system).", "Planned", "BRD + Figma", "ARCD-1983", "Saudi Trading"),
    (31, "Securities Borrowing & Lending (SBL) Program", "Enables eligible clients to lend shares to earn yield or borrow shares to short sell.", "Planned", "BRD", "ARCD-53753", "Saudi Trading"),
    (32, "SBL Agreement & Suitability Digital Acceptance", "Digital enrollment flow for whitelisted clients to accept SBL agreement.", "Planned", "BRD", "ARCD-86486", "Saudi Trading"),
    (33, "Short Selling", "Allows eligible clients to sell borrowed securities short in the Saudi market.", "Planned", "BRD", "ARCD-53753", "Saudi Trading"),
    (34, "Tadawulaty Platform Access (Single Sign-On)", "Enables clients to access Edaa's Tadawulaty platform directly from the SuperApp.", "Planned", "BRD", "ARCD-22970", "Saudi Trading"),
    (35, "Tadawul News Push Notifications", "Sends real-time Tadawul market news as push notifications.", "Planned", "BRD", "ARCD-39221", "Saudi Trading"),
    (36, "Top Trending (Heated) Stocks List", "Displays a dynamic, hourly-updated list of the top 20-30 most-searched stocks.", "Planned", "BRD", "ARCD-41012", "Saudi Trading"),
    (37, "Nomu (Parallel Market) Subscription", "Enables eligible clients to apply for Nomu subscriptions through the SuperApp.", "Live", "BRD + Figma", "ARCD-1922", "Saudi Trading"),
    (38, "Nomu IPO Subscription for Institutional Clients", "Allows institutional ARC customers to subscribe to Nomu market IPOs.", "Planned", "BRD + Figma", "ARCD-47866", "Saudi Trading"),
    (39, "View Saudi Market Portfolio Performance (P&L)", "Shows clients a historical P&L performance chart for Saudi market portfolio.", "Planned", "BRD + Figma", "ARCD-2654", "Saudi Trading"),
    (40, "View Overall P&L History for Local Stocks (Sold)", "Comprehensive historical profit and loss report for all sold Saudi stocks.", "Planned", "BRD", "ARCD 60444", "Saudi Trading"),
    (41, "Update Average Cost Price", "Allows clients to manually update the average cost price of a holding.", "Planned", "BRD", "ARCD-2650", "Saudi Trading"),
    (42, "Block Codes Management (AML)", "Back-office tool to create, assign, update, and remove AML-related block codes.", "Live", "BRD", "ARCD-2792", "Saudi Trading"),
    (43, "Buying Power Swap (Local to International)", "Allows clients to use Saudi market buying power to fund international orders.", "Planned", "BRD", "ARCD-2644", "Saudi Trading"),
    (44, "Instant Settlement (T+0 / T+1)", "Option to receive sale proceeds instantly rather than waiting for T+2.", "Planned", "BRD + Figma", "ARCD-14352", "Saudi Trading"),
    (45, "TILA Subscription & Price Display", "Manages the Tadawul Information License Agreement subscription.", "Live", "BRD", "ARCD-2933", "Saudi Trading"),
    (46, "View Stock Sector & Exchange Volatility", "Displays historical volatility indicators for stocks, sectors, and the exchange.", "Planned", "BRD", "ARCD-58777", "Saudi Trading"),
    (47, "Saudi Portfolio — Tradable Rights Screen", "Screen displaying tradable rights (huqooq) available for the client's portfolio.", "Planned (Figma-only)", "Figma", "—", "Saudi Trading"),
    (48, "Market Home — Tablet Layout", "Tablet-optimised market overview layout.", "Planned (Figma-only)", "Figma", "—", "Saudi Trading"),
    (49, "Orders — UAE Market Stocks List", "Order history and active orders for UAE market stock orders.", "Planned (Figma-only)", "Figma", "—", "Saudi Trading"),
    (50, "Order Detail — Conditional Order", "Full detail view of an active or executed conditional (stop/trigger) order.", "Planned (Figma-only)", "Figma", "—", "Saudi Trading"),
    (51, "Order Detail — Basket Order", "Full detail and management screen for basket orders (group of stocks).", "Planned (Figma-only)", "Figma", "—", "Saudi Trading"),
    (52, "Order Detail — Slicing / Iceberg Order", "Full detail view for iceberg/slicing order type.", "Planned (Figma-only)", "Figma", "—", "Saudi Trading"),
    (53, "Order Detail — Interval Order", "Full detail view for interval (scheduled) order type.", "Planned (Figma-only)", "Figma", "—", "Saudi Trading"),
    (54, "Order Detail — Stop Loss Order", "Full detail view of an active stop loss order.", "Planned (Figma-only)", "Figma", "—", "Saudi Trading"),
    (55, "Order Detail — Take Profit Order", "Full detail view of an active take profit order.", "Planned (Figma-only)", "Figma", "—", "Saudi Trading"),
    (56, "Basket Order — Create / Set Condition Screen", "Screen for creating a new basket order and defining execution conditions.", "Planned (Figma-only)", "Figma", "—", "Saudi Trading"),
    (57, "Order Filter Panel", "Filter and sort panel for the orders list.", "Planned (Figma-only)", "Figma", "—", "Saudi Trading"),
    (58, "Orders Empty State Screen", "Empty state screen shown when no orders exist.", "Planned (Figma-only)", "Figma", "—", "Saudi Trading"),
    # US Trading
    (59, "Place US Market Order", "Enables clients to place buy or sell orders for US-listed stocks.", "Live", "BRD + Figma", "ARCD-70106", "US Trading"),
    (60, "US Market Stock Search & Listing (Enhanced)", "Improved search experience for US stocks across all indices.", "Planned", "BRD", "ARCD-50707", "US Trading"),
    (61, "US Market Stock Profile Page", "Detailed stock information page for US-listed stocks.", "Live", "BRD + Figma", "ARCD-14312", "US Trading"),
    (62, "International Options Page (US Stocks)", "Consolidated options chain view for US market stocks.", "Planned", "BRD + Figma", "ARCD-72350", "US Trading"),
    (63, "Bulls vs. Bears Case Summary (US Stocks)", "Displays concise bullish and bearish case summaries for each US stock.", "Planned", "BRD", "ARCD-61067", "US Trading"),
    (64, "Why Is It Moving — Stock Insights", "Provides real-time AI-driven explanations of why a US stock price is moving.", "Planned", "BRD", "ARCD-60875", "US Trading"),
    (65, "Government Trading Data (US Congress Disclosures)", "Shows real-time US congressional stock trading disclosures.", "Planned", "BRD", "ARCD-72957", "US Trading"),
    (66, "Trending Tickers (US Market)", "Displays a list of US stocks gaining retail investor attention.", "Planned", "BRD", "ARCD-72979", "US Trading"),
    (67, "Shariah Compliance Lists (Multi-Listing)", "Allows clients to select and apply either General or ARC-specific Shariah list.", "Live", "BRD", "ARCD-2067", "US Trading"),
    (68, "US Market Settings", "Configuration screen for US market-specific settings.", "Planned (Figma-only)", "Figma", "—", "US Trading"),
    # Portfolio Monitoring
    (69, "View Saudi Market Portfolio Holdings", "Displays current Saudi market portfolio holdings, quantities, average cost, current value.", "Live", "BRD + Figma", "ARCD-2654", "Portfolio Monitoring"),
    (70, "View Saudi Market Portfolio Performance Chart", "Shows a graphical performance chart over selectable time periods.", "Planned", "BRD + Figma", "ARCD-2654", "Portfolio Monitoring"),
    (71, "Peer Portfolio Comparison", "Benchmarks client's P&L percentage against anonymized peers.", "Planned", "BRD + Figma", "ARCD-60816", "Portfolio Monitoring"),
    (72, "Portfolio Insights", "Provides diversification analysis, concentration alerts, sector breakdown.", "Planned", "BRD + Figma", "ARCD-60816", "Portfolio Monitoring"),
    (73, "Portfolio Health Score", "Calculates and displays an overall health score for the client's portfolio.", "Planned", "BRD + Figma", "ARCD 52378", "Portfolio Monitoring"),
    (74, "Investment Allocation Tracker", "Enables clients to define and monitor target allocation percentages.", "Planned", "BRD", "ARCD-61176", "Portfolio Monitoring"),
    (75, "Goal Tracker", "Allows clients to define financial investment goals and monitor progress.", "Planned", "BRD", "ARCD 55733", "Portfolio Monitoring"),
    (76, "Storyteller (Quarterly Performance Report)", "Generates a personalized narrative-driven quarterly investment overview.", "Planned", "BRD + Figma", "ARCD 19542", "Portfolio Monitoring"),
    (77, "Analyst Ratings on Stocks", "Shows real-time stock ratings from verified analyst firms.", "Planned", "BRD", "ARCD-60979", "Portfolio Monitoring"),
    (78, "Earnings Calendar (International)", "Centralized view of upcoming and past company earnings announcements.", "Planned", "BRD", "ARCD - Earnings Calendar", "Portfolio Monitoring"),
    (79, "Customer Investment Holdings Letter (Authenticated PDF)", "Enables clients to generate an authenticated PDF report of all holdings.", "Live", "BRD + Figma", "Holdings Letter BRD", "Portfolio Monitoring"),
    (80, "Stock Holdings Filter Panel", "Filter panel for sorting and filtering stock holdings.", "Planned (Figma-only)", "Figma", "—", "Portfolio Monitoring"),
    (81, "Saudi Portfolio — Choose Portfolio Selector", "Portfolio selector screen when client has multiple Saudi portfolios.", "Planned (Figma-only)", "Figma", "—", "Portfolio Monitoring"),
    (82, "Saudi Portfolio — Sectors / Index / Shariah Filter Panels", "Filter panels for sorting holdings by sector, index, or Shariah compliance.", "Planned (Figma-only)", "Figma", "—", "Portfolio Monitoring"),
    (83, "Saudi Portfolio — Transfer Holdings", "Screen to initiate an in-specie transfer of holdings between portfolios.", "Planned (Figma-only)", "Figma", "—", "Portfolio Monitoring"),
    (84, "Saudi Portfolio — Add Holdings to Watchlist", "Quick-add flow to add a held stock to the watchlist from portfolio.", "Planned (Figma-only)", "Figma", "—", "Portfolio Monitoring"),
    (85, "Saudi Portfolio — Liquidate Holdings Flow", "Bulk liquidation flow for closing out positions.", "Planned (Figma-only)", "Figma", "—", "Portfolio Monitoring"),
    (86, "US Portfolio — Choose Portfolio Selector", "Portfolio selector when client has multiple US market portfolios.", "Planned (Figma-only)", "Figma", "—", "Portfolio Monitoring"),
    (87, "Portfolio Analysis Dashboard", "Analytics hub showing top stocks, gains/losses, allocation, trading activity.", "Planned (Figma-only)", "Figma", "—", "Portfolio Monitoring"),
    (88, "Portfolio Reports (Downloadable)", "Downloadable portfolio performance reports with filter controls.", "Planned (Figma-only)", "Figma", "—", "Portfolio Monitoring"),
    (89, "Portfolio Preference Settings", "Display preference settings for portfolio view.", "Planned (Figma-only)", "Figma", "—", "Portfolio Monitoring"),
    # Wealth Visibility
    (90, "View Total Cash & Buying Power (Aggregated)", "Consolidated view of total available cash and buying power.", "Planned", "BRD", "ARCD-72218", "Wealth Visibility"),
    (91, "Cash-In from ARB Account to Portfolio", "Allows clients to transfer funds from linked Al Rajhi Bank account.", "Live", "BRD + Figma", "ARCD-2651", "Wealth Visibility"),
    (92, "Multi-Currency Wallet (UCM) Enhancements", "Enhances the UCM wallet to support additional currencies.", "Planned", "BRD", "ARCD-72195", "Wealth Visibility"),
    (93, "Multi Virtual IBANs", "Assigns unique Virtual IBANs to each client portfolio and UCM wallet.", "Planned", "BRD", "ARCD-72196", "Wealth Visibility"),
    (94, "Wallet Transaction Invoices (ZATCA-Compliant)", "Automatically generates ZATCA-compliant electronic invoices.", "Planned", "BRD", "ARCD - UCM Wallet Invoices", "Wealth Visibility"),
    # Mutual Funds
    (95, "Subscribe to Mutual Fund (SAR Portfolio)", "Allows clients to subscribe to ARC's SAR-denominated mutual funds.", "Live", "BRD + Figma", "ARCD-47782", "Mutual Funds"),
    (96, "Subscribe to USD Mutual Fund Using SAR Account", "Enables clients to subscribe to USD funds using SAR accounts with auto FX.", "Planned", "BRD + Figma", "ARCD-32980", "Mutual Funds"),
    (97, "Redeem / Cancel Mutual Fund Subscription Order", "Allows clients to cancel a pending subscription or redemption order.", "Planned", "BRD + Figma", "Cancel Sub/Red BRD", "Mutual Funds"),
    (98, "Cancel Mutual Fund Portfolio (SAR/USD)", "Enables clients to fully cancel and close an active mutual fund portfolio.", "Planned", "BRD", "Cancel Portfolio BRD", "Mutual Funds"),
    (99, "Mutual Fund Portfolio Performance Chart", "Displays investment performance chart over selectable time periods.", "Planned", "BRD + Figma", "ARCD-47782", "Mutual Funds"),
    (100, "Mutual Fund Dividend History & Total Dividends", "Shows complete dividend history and cumulative totals.", "Planned", "BRD", "ARCD-47782", "Mutual Funds"),
    (101, "Mutual Funds Segregated by Asset Class", "Organizes the fund catalog by asset class to improve discovery.", "Planned", "BRD", "ARCD-47782", "Mutual Funds"),
    (102, "Fund Historical Performance View", "Displays historical performance chart of a fund available for subscription.", "Planned", "BRD", "ARCD-47782", "Mutual Funds"),
    (103, "Show Mutual Fund Buy Orders as Blocked Amounts", "Displays pending fund buy orders as blocked amounts in portfolio.", "Planned", "BRD", "ARCD-48329", "Mutual Funds"),
    (104, "Margin Lending on Mutual Funds (Collateral)", "Allows clients to include fund units as eligible collateral.", "Planned", "BRD", "ARCD-8609", "Mutual Funds"),
    (105, "Mutual Fund Portfolio — Switch Funds Flow", "Multi-step flow for switching between mutual fund products.", "Planned (Figma-only)", "Figma", "—", "Mutual Funds"),
    # Robo Advisory
    (106, "Robo Advisory Onboarding", "New-client onboarding flow including suitability questions and risk profile.", "Live", "BRD + Figma", "ARCD-74031", "Robo Advisory"),
    (107, "Create Robo Portfolio & Investment Risk Profile", "Allows clients to create a Robo portfolio and assign risk profile.", "Planned", "BRD + Figma", "ARCD-74031", "Robo Advisory"),
    (108, "Robo Portfolio Cash Withdrawal", "Enables Robo clients to withdraw cash from their Robo portfolio.", "Planned", "BRD + Figma", "ARCD-74031", "Robo Advisory"),
    (109, "Mashura (Robo Advisory) Reports", "Reporting screens specific to the Robo Advisory product.", "Planned (Figma-only)", "Figma", "—", "Robo Advisory"),
    # IPOs
    (110, "Subscribe to Main Market IPO", "Allows clients to apply for an IPO subscription on the Saudi main market.", "Live", "BRD + Figma", "ARCD-1594", "IPOs"),
    (111, "View IPO Details & Subscription Status", "Displays upcoming and active IPO listings with subscription status.", "Live", "BRD + Figma", "ARCD-1594", "IPOs"),
    (112, "Subscribe to Nomu (Parallel Market) IPO", "Enables eligible clients to subscribe to Nomu IPOs.", "Planned", "BRD", "ARCD-1922", "IPOs"),
    (113, "Nomu IPO Subscription for Institutional Clients", "Allows institutional customers to submit Nomu IPO requests.", "Planned", "BRD", "ARCD-47866", "IPOs"),
    (114, "Auto-Subscribe Plan (Subscription Engine)", "Enables recurring automated subscription plans.", "Planned", "BRD + Figma", "ARCD-2632", "IPOs"),
    (115, "Qualified Client Verification for Private Fund IPOs", "Enforces CMA-mandated eligibility checks for restricted funds.", "Planned", "BRD", "ARCD-22937", "IPOs"),
    (116, "Discover Home", "Main Discover section landing page.", "Planned (Figma-only)", "Figma", "—", "IPOs"),
    # Corporate Actions
    (117, "Dividends Calendar (International)", "Financial calendar view of upcoming dividend announcements.", "Planned", "BRD + Figma", "ARCD-72987", "Corporate Actions"),
    (118, "Insider Trades Feed (International)", "Displays executive-level insider trading disclosures.", "Planned", "BRD", "ARCD-68490", "Corporate Actions"),
    (119, "Purification Calculator", "Allows clients to calculate their Sharia-required purification amount.", "Planned", "BRD", "ARCD-1096", "Corporate Actions"),
    (120, "Stocks Dividend Calculator", "Interactive calculator for estimating dividend income.", "Planned (Figma-only)", "Figma", "—", "Corporate Actions"),
    # Investor Engagement
    (121, "Spin the Wheel for Discounts", "Gamified reward feature for commission discounts after trading milestones.", "Planned", "BRD", "ARCD-16056", "Investor Engagement"),
    (122, "Prepaid Commission Bundle (Commission-Free Trading)", "Allows clients to subscribe to a prepaid commission-free bundle.", "Planned", "BRD", "ARCD-17031", "Investor Engagement"),
    (123, "Bundle Benefits (ARG Group Bundle Engine)", "Displays and activates Al Rajhi Group bundle benefits.", "Live", "BRD", "ARCD 18697", "Investor Engagement"),
    (124, "Mokafaa Loyalty Points Redemption", "Allows clients to redeem Mokafaa loyalty points as cash for investing.", "Planned", "BRD", "ARCD 67739", "Investor Engagement"),
    (125, "ARC Debit Card", "ARC-branded debit card linked to UCM wallet.", "Planned", "BRD", "ARCD 72647", "Investor Engagement"),
    (126, "Buy Transaction Round-Up", "Rounds up each buy transaction and invests the spare change.", "Planned", "BRD", "ARCD 73671", "Investor Engagement"),
    (127, "Social Trading (Follow & Copy Traders)", "Enables clients to discover, follow, and replicate trading strategies.", "Planned", "BRD", "ARCD-72352", "Investor Engagement"),
    (128, "Smart Saving Plan (Bulk Orders via ARB)", "Processes bulk deposit and subscription orders from ARB.", "Live", "BRD", "Smart Saving Plan BRD", "Investor Engagement"),
    (129, "Gifting List with Date Selection", "Back-office tool for generating a gifting list with date range.", "Planned", "BRD", "ARCD-42865", "Investor Engagement"),
    (130, "Investment Referral / Date-Based Gift Campaigns", "Configures and delivers date-specific gift campaigns.", "Planned", "BRD", "ARCD-42865", "Investor Engagement"),
    (131, "Preferred Language for Notifications", "Allows clients to select preferred language for all notifications.", "Planned", "BRD + Figma", "ARCD-37611", "Investor Engagement"),
    (132, "Email Notification Templates Revamp", "Redesigned email notification templates for all events.", "Planned", "BRD", "ARCD 20124", "Investor Engagement"),
    (133, "Charity Investment / Donation Screen", "Screen for charity donation or investment product offerings.", "Planned (Figma-only)", "Figma", "—", "Investor Engagement"),
    (134, "Crowdfund Portfolios Home", "Portfolio view for crowd investment products.", "Planned (Figma-only)", "Figma", "—", "Investor Engagement"),
    (135, "Orders — Crowd Funds List", "Order history for crowd investment fund orders.", "Planned (Figma-only)", "Figma", "—", "Investor Engagement"),
    # Cross-Journey
    (136, "Guest Mode (Discovery Mode)", "Allows non-registered users to explore the SuperApp without KYC.", "Planned", "BRD + Figma", "ARCD-75522", "Cross-Journey"),
    (137, "Zakat Calculator", "Enables clients to calculate Zakat due on their investment holdings.", "Live", "BRD", "ARCD-1283", "Cross-Journey"),
    (138, "Purification ZATCA-Compliant Invoice", "Generates ZATCA-compliant electronic invoices for purification.", "Planned", "BRD", "ARCD-14553", "Cross-Journey"),
    (139, "Economic Calendar (International)", "Real-time global economic calendar showing key indicators.", "Planned", "BRD", "ARCD 61046", "Cross-Journey"),
    (140, "ARC News Screener (Personalized News Dashboard)", "Configurable personalized news dashboard with custom widgets.", "Planned", "BRD", "ARCD-82616", "Cross-Journey"),
    (141, "Ticker Chart Integration (TradingView)", "Integrates advanced interactive price charts into stock pages.", "Live", "BRD + Figma", "ARCD-1553", "Cross-Journey"),
    (142, "Ticker Chart — ARC Package Subscriptions", "Allows clients to access premium TradingView features via ARC.", "Planned", "BRD", "ARCD-2627", "Cross-Journey"),
    (143, "CRM Case Management (End-to-End Digital)", "Digital CRM system for clients to raise, track, and resolve cases.", "Planned", "BRD", "ARCD-85537", "Cross-Journey"),
    (144, "Mada / Credit Card 3D Secure Authentication", "Adds 3D Secure verification when linking a new card.", "Planned", "BRD", "ARCD-68518", "Cross-Journey"),
    (145, "Mada / Credit Card Transaction Limits", "Enables daily transaction limit controls per client for linked cards.", "Planned", "BRD", "ARCD-68518", "Cross-Journey"),
    (146, "Cash-Out Enhancements (GCC to External Bank)", "Allows GCC clients to withdraw cash to linked bank accounts.", "Planned", "BRD", "ARCD-34470", "Cross-Journey"),
    (147, "International Indices Historical Data (ODS)", "Provides accurate historical data for major international indices.", "Planned", "BRD", "ARCD-68581", "Cross-Journey"),
    (148, "View Commission Discount on Saudi Market Trades", "Displays the applicable commission discount rate on trade screens.", "Planned", "BRD", "ARCD-60436", "Cross-Journey"),
    (149, "Saudi Market Stock Profile Information (Enhanced)", "Enhances stock info page with additional data fields.", "Planned", "BRD", "ARCD-14312", "Cross-Journey"),
    (150, "Stock Sector & Exchange Liquidity Indicators", "Displays liquidity indicators for stocks, sectors, and the exchange.", "Unknown", "BRD", "ARCD-41013", "Cross-Journey"),
    (151, "Session Timeout Settings", "Settings screen to configure automatic session timeout duration.", "Planned (Figma-only)", "Figma", "—", "Cross-Journey"),
    (152, "Always On Display Setting", "Toggle to keep the device screen on while using the app.", "Planned (Figma-only)", "Figma", "—", "Cross-Journey"),
    (153, "Index Feed Bar Settings", "Setting to show/hide or configure the live market index ticker bar.", "Planned (Figma-only)", "Figma", "—", "Cross-Journey"),
    (154, "Registered Devices Management", "List of devices registered for this account with option to revoke.", "Planned (Figma-only)", "Figma", "—", "Cross-Journey"),
    # ── NEW: Deep Extraction Discoveries ──────────────────────────────────
    (155, "Stock Screener", "Filter stocks by fundamentals, technicals, sector. Found as text label in Market Figma file.", "NEW — Deep Extraction", "Figma (text label)", "—", "Saudi Trading / US Trading"),
    (156, "UAE Market", "Third market beyond Saudi and US. Labels found across Market and Orders files.", "NEW — Deep Extraction", "Figma (text labels)", "—", "Saudi Trading"),
    (157, "Fast Onboarding", "Streamlined account opening — simplified KYC variant. 364 sub-frames in dedicated Figma page.", "NEW — Deep Extraction", "Figma (full page)", "—", "Onboarding"),
    (158, "Guest Mode — Web Experience", "Full web-based guest experience with Market Landscape and Benchmark Analysis screens.", "NEW — Deep Extraction", "Figma (21 frames)", "—", "Cross-Journey"),
    (159, "First Engagement Flow", "Post-first-login activation flow. 225+ nodes in dedicated Figma page.", "NEW — Deep Extraction", "Figma (full page)", "—", "Onboarding"),
    (160, "In-App Tutorials", "In-app tutorial screens — onboarding education content.", "NEW — Deep Extraction", "Figma (full page)", "—", "Onboarding"),
    (161, "Digital StoryTeller (Enhanced)", "Dedicated Figma page for narrative quarterly report — design more advanced than inventory showed.", "NEW — Deep Extraction", "Figma (full page)", "—", "Portfolio Monitoring"),
    (162, "Ramadan Theme", "Seasonal theming page — prepared for Ramadan content.", "NEW — Deep Extraction", "Figma (empty page)", "—", "Cross-Journey"),
    (163, "Power of Attorney (POA) Request", "POA flow designed in Discover section. Text labels found in deep extraction.", "NEW — Deep Extraction", "Figma (text labels)", "—", "Cross-Journey"),
    (164, "Crowd Fund (Cross-Module)", "Crowdfunding product designed across Home, Market, Orders — more mature than inventory suggested.", "NEW — Deep Extraction", "Figma (text labels)", "—", "Investor Engagement"),
]

# ── Sheet 1: All Features ─────────────────────────────────────────────────
ws = wb.active
ws.title = "All Features"

headers = ["#", "Feature Name", "Description", "Squad", "Current Status\n(from BRD)", "Source", "BRD Reference",
           "VERIFIED\nLive?", "VERIFIED\nStatus", "Squad Lead\nConfirmed?", "Notes / Comments"]
col_widths = [5, 35, 55, 18, 16, 14, 16, 10, 14, 12, 30]

for ci, h in enumerate(headers, 1):
    cell = ws.cell(row=1, column=ci, value=h)
    cell.font = header_font
    cell.fill = header_fill
    cell.alignment = center
    cell.border = thin_border
    ws.column_dimensions[get_column_letter(ci)].width = col_widths[ci - 1]

for ri, feat in enumerate(FEATURES, 2):
    fid, fname, fdesc, fstatus, fsource, fbrd, fsquad = feat
    vals = [fid, fname, fdesc, fsquad, fstatus, fsource, fbrd, "", "", "", ""]
    for ci, v in enumerate(vals, 1):
        cell = ws.cell(row=ri, column=ci, value=v)
        cell.font = body_font
        cell.alignment = wrap
        cell.border = thin_border

        # Color-code status column
        if ci == 5:
            cell.font = bold_font
            fill = STATUS_FILL.get(fstatus)
            if fill:
                cell.fill = fill

        # Color-code verification columns
        if ci in (8, 9, 10):
            cell.fill = PatternFill(start_color="FFFBEB", end_color="FFFBEB", fill_type="solid")

ws.auto_filter.ref = f"A1:K{len(FEATURES) + 1}"
ws.freeze_panes = "A2"

# ── Sheet 2: Summary by Squad ─────────────────────────────────────────────
ws2 = wb.create_sheet("Summary by Squad")
squad_stats = {}
for feat in FEATURES:
    sq = feat[6]
    if sq not in squad_stats:
        squad_stats[sq] = {"total": 0, "live": 0, "planned": 0, "figma_only": 0, "new": 0, "unknown": 0}
    squad_stats[sq]["total"] += 1
    st = feat[3]
    if st == "Live":
        squad_stats[sq]["live"] += 1
    elif st.startswith("Planned (Figma"):
        squad_stats[sq]["figma_only"] += 1
    elif st.startswith("NEW"):
        squad_stats[sq]["new"] += 1
    elif st == "Unknown":
        squad_stats[sq]["unknown"] += 1
    else:
        squad_stats[sq]["planned"] += 1

s2_headers = ["Squad", "Total", "Live", "Planned", "Figma-Only", "New (Deep)", "Unknown", "% Live"]
s2_widths = [25, 8, 8, 10, 12, 12, 10, 10]
for ci, h in enumerate(s2_headers, 1):
    cell = ws2.cell(row=1, column=ci, value=h)
    cell.font = header_font
    cell.fill = header_fill
    cell.alignment = center
    cell.border = thin_border
    ws2.column_dimensions[get_column_letter(ci)].width = s2_widths[ci - 1]

for ri, (sq, st) in enumerate(sorted(squad_stats.items()), 2):
    pct = f"{round(st['live'] / st['total'] * 100)}%" if st['total'] else "0%"
    vals = [sq, st["total"], st["live"], st["planned"], st["figma_only"], st["new"], st["unknown"], pct]
    for ci, v in enumerate(vals, 1):
        cell = ws2.cell(row=ri, column=ci, value=v)
        cell.font = bold_font if ci <= 1 else body_font
        cell.alignment = center if ci > 1 else Alignment(vertical="center")
        cell.border = thin_border

# Totals row
tr = len(squad_stats) + 2
totals = ["TOTAL", sum(s["total"] for s in squad_stats.values()),
          sum(s["live"] for s in squad_stats.values()),
          sum(s["planned"] for s in squad_stats.values()),
          sum(s["figma_only"] for s in squad_stats.values()),
          sum(s["new"] for s in squad_stats.values()),
          sum(s["unknown"] for s in squad_stats.values()),
          f"{round(sum(s['live'] for s in squad_stats.values()) / sum(s['total'] for s in squad_stats.values()) * 100)}%"]
for ci, v in enumerate(totals, 1):
    cell = ws2.cell(row=tr, column=ci, value=v)
    cell.font = Font(name="Calibri", size=11, bold=True, color=navy)
    cell.fill = PatternFill(start_color="E8ECFF", end_color="E8ECFF", fill_type="solid")
    cell.alignment = center if ci > 1 else Alignment(vertical="center")
    cell.border = thin_border

# ── Sheet 3: Instructions ─────────────────────────────────────────────────
ws3 = wb.create_sheet("Instructions")
ws3.column_dimensions["A"].width = 80
instructions = [
    "ARC FEATURES MAP — SQUAD VALIDATION SHEET",
    "",
    f"Generated: {date.today().isoformat()}",
    "Owner: Ahmed Alghamdi — Head of Digital Experience",
    "",
    "HOW TO USE THIS SHEET:",
    "",
    '1. Go to the "All Features" tab',
    "2. Filter by your squad name (Column D)",
    "3. For each feature in your squad:",
    '   - Column H (VERIFIED Live?): Enter YES or NO',
    '   - Column I (VERIFIED Status): Enter one of: Live / Planned / Not Planned / Deprecated / In Development',
    '   - Column J (Squad Lead Confirmed?): Enter your name',
    '   - Column K (Notes): Add any comments — missing features, wrong ownership, etc.',
    "",
    "STATUS DEFINITIONS:",
    '   Live = Feature is active in the current production app',
    '   Planned = BRD approved, not yet in production',
    '   Planned (Figma-only) = Designed in Figma but no BRD written',
    '   NEW — Deep Extraction = Found in Figma during deep extraction, not in original inventory',
    '   Unknown = Status could not be determined from BRD',
    "",
    "IMPORTANT:",
    "   - The 'Current Status' column is based on BRD documents ONLY — it has NOT been verified",
    "   - 10 new features were discovered in deep Figma extraction and need classification",
    "   - If a feature is missing from this list, add it at the bottom of the All Features tab",
    "",
    "DEADLINE: May 1, 2026",
    "Return to: Ahmed Alghamdi — Head of Digital Experience",
]
for ri, line in enumerate(instructions, 1):
    cell = ws3.cell(row=ri, column=1, value=line)
    if ri == 1:
        cell.font = Font(name="Calibri", size=14, bold=True, color=navy)
    elif line.startswith("HOW TO USE") or line.startswith("STATUS DEF") or line.startswith("IMPORTANT") or line.startswith("DEADLINE"):
        cell.font = Font(name="Calibri", size=11, bold=True, color="DC2626")
    else:
        cell.font = Font(name="Calibri", size=11)

# ── Save ──────────────────────────────────────────────────────────────────
out_path = "/Users/ahmedalghamdi/Claude/ARC/projects/features-map/reports/features-map-validation-2026-04-22.xlsx"
wb.save(out_path)
print(f"\nDone → {out_path}")
print(f"  {len(FEATURES)} features across {len(squad_stats)} squads")
