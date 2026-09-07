#!/usr/bin/env python3
"""
extract_screens_batch1.py
Batch 1: Extract screens from OnBoarding (KYC), Portfolios, Watchlist.
Produces dashboard/data/screens.json with all elements linked to features and BRDs.
Migrates existing Holdings prototype nodes.
"""
import json, os, sys, time
from datetime import date
from urllib.request import Request, urlopen
from urllib.error import HTTPError

FIGMA_TOKEN = os.environ.get("FIGMA_TOKEN")
if not FIGMA_TOKEN:
    print("ERROR: FIGMA_TOKEN not set")
    sys.exit(1)

HERE = os.path.dirname(os.path.abspath(__file__))
DASH = os.path.join(HERE, "..")
DATA = os.path.join(DASH, "data")

# ── File keys ──
FILES = {
    "OnBoarding (KYC)": "PgN7nzg8CcueY12mu6TIVe",
    "Portfolios": "4ybkyLURbOhzauw8ugkHGp",
    "Watchlist": "muzIamMJ7ycvstbVnWbXvi",
}

# ── Load features and BRDs ──
features = json.load(open(os.path.join(DATA, "features.json")))["features"]
brds_data = json.load(open(os.path.join(DATA, "brds.json")))["brds"]
feat_by_id = {f["id"]: f for f in features}
feat_by_file = {}
feat_by_journey = {}
for f in features:
    ff = f.get("figma_file")
    if ff:
        feat_by_file.setdefault(ff, []).append(f)
    j = f.get("journey")
    if j:
        feat_by_journey.setdefault(j, []).append(f)

# ── Figma API helper ──
def figma_get(url):
    req = Request(url, headers={"X-Figma-Token": FIGMA_TOKEN})
    try:
        resp = urlopen(req, timeout=30)
        return json.loads(resp.read())
    except HTTPError as e:
        print(f"  API error {e.code}: {url}")
        return None

def get_node(file_key, node_id, depth=10):
    url = f"https://api.figma.com/v1/files/{file_key}/nodes?ids={node_id}&depth={depth}"
    data = figma_get(url)
    if not data or "nodes" not in data:
        return None
    return list(data["nodes"].values())[0].get("document")

def figma_url(file_key, node_id):
    return f"https://www.figma.com/design/{file_key}?node-id={node_id.replace(':','-')}"

# ── Element extraction ──
SKIP_TYPES = {"VECTOR", "BOOLEAN_OPERATION", "RECTANGLE", "ELLIPSE", "LINE", "STAR", "REGULAR_POLYGON", "SLICE"}
SKIP_NAMES = {"Rectangle", "Vector", "Ellipse", "Line", "Union", "Border", "Cap", "Capacity", "Shade", "Stroke"}
FLOW_NAMES = {"Flow Section", "Flow Info", "Annotation", "popUpBar", "Home Indicator"}
CHROME_NAMES = {"StatusBar", "Time", "Levels", "Battery", "Wifi", "Cellular Connection", "Rectangle 2"}

def extract_elements(node, file_key, parent_id, figma_file, depth=0, max_depth=6):
    """Recursively extract meaningful elements from a Figma node."""
    elements = []
    if depth > max_depth:
        return elements

    for child in node.get("children", []):
        if child.get("visible") == False:
            continue

        name = (child.get("name") or "").strip()
        ntype = child.get("type", "")
        nid = child.get("id", "")
        chars = child.get("characters", "")
        children = child.get("children", [])

        # Skip vectors, shapes, unnamed
        if ntype in SKIP_TYPES and not name:
            continue
        if name in SKIP_NAMES or not name:
            continue
        # Skip flow labels and annotations
        if name in FLOW_NAMES:
            continue

        # Determine element type
        etype = classify_element(name, ntype, chars, children)

        if etype == "skip":
            continue

        sample = chars if chars else None

        elem = {
            "name": name,
            "type": etype,
            "parent_id": parent_id,
            "figma_file": figma_file,
            "figma_node_id": nid,
            "figma_url": figma_url(file_key, nid),
            "sample_value": sample,
        }
        elements.append(elem)

        # If it's a group, recurse into children
        if etype == "group" and children:
            sub_elements = extract_elements(child, file_key, None, figma_file, depth + 1, max_depth)
            elements.extend(sub_elements)

    return elements

def classify_element(name, ntype, chars, children):
    nl = name.lower()

    # Skip decorative/structural
    if nl.startswith("rectangle") or nl.startswith("vector") or nl.startswith("frame 214"):
        return "skip"
    if ntype in SKIP_TYPES:
        return "skip"

    # Chrome
    if name in CHROME_NAMES or nl in ("statusbar", "time", "levels", "battery", "home indicator"):
        return "chrome"

    # Actions
    action_keywords = ["button", "btn", "cta", "submit", "confirm", "cancel", "close", "save",
                       "buy", "sell", "add", "remove", "delete", "create", "continue", "next",
                       "back", "proceed", "sign", "login", "register", "apply", "subscribe",
                       "transfer", "withdraw", "deposit", "liquidate", "switch", "redeem"]
    if any(kw in nl for kw in action_keywords):
        if ntype in ("INSTANCE", "FRAME") or (ntype == "TEXT" and chars):
            return "action"

    # Navigation
    nav_keywords = ["tab", "nav", "menu", "breadcrumb", "link", "bottom bar", "bottombar", "header"]
    if any(kw in nl for kw in nav_keywords):
        return "navigation"

    # Groups
    if ntype == "SECTION" or (ntype == "FRAME" and len(children) > 2 and not chars):
        return "group"
    if ntype == "INSTANCE" and len(children) > 2 and not chars:
        return "group"

    # Fields (text elements, data displays)
    if ntype == "TEXT" or chars:
        return "field"
    if ntype == "INSTANCE" and len(children) <= 2:
        return "field"
    if ntype == "FRAME" and len(children) <= 2:
        return "field"

    return "field"

# ── Feature matching ──
def match_feature(element_name, figma_file, journey_fallback=None):
    """Match an element to a feature. Returns (feature_id, brd_list, reason)."""
    ename = element_name.lower()

    # First: try features with matching figma_file
    file_features = feat_by_file.get(figma_file, [])
    best, score, reason = _best_match(ename, file_features)
    if best and score >= 6:
        brds = best.get("brd", [])
        if not brds:
            brds = ["REVIEW"]
            reason += " | Feature has no BRD yet"
        return best["id"], brds, reason

    # Fallback: try journey match
    if journey_fallback:
        j_features = feat_by_journey.get(journey_fallback, [])
        best2, score2, reason2 = _best_match(ename, j_features)
        if best2 and score2 >= 6:
            brds = best2.get("brd", [])
            if not brds:
                brds = ["REVIEW"]
                reason2 += " | Feature has no BRD yet"
            return best2["id"], brds, f"Journey-fallback: {reason2}"

    return None, ["REVIEW"], f"No feature match for '{element_name}'"

def _best_match(ename, feature_list):
    best = None
    best_score = 0
    best_reason = ""

    for f in feature_list:
        fname = f.get("name", "").lower()
        fdef = (f.get("definition") or "").lower()
        score = 0

        # Word overlap
        ewords = set(w for w in ename.replace("-", " ").replace("_", " ").split() if len(w) > 2)
        fwords = set(w for w in fname.replace("-", " ").replace("_", " ").split() if len(w) > 2)

        overlap = ewords & fwords
        score += len(overlap) * 8

        # Substring matching
        for ew in ewords:
            if ew in fdef:
                score += 3

        # Exact name containment
        if ename in fname or fname in ename:
            score += 15

        # Key term boosts
        BOOSTS = {
            "otp": ["otp", "verification"],
            "login": ["login", "authentication", "sign in"],
            "password": ["password", "pin", "passcode"],
            "face id": ["biometric", "face id", "facial"],
            "nafath": ["nafath", "national single sign"],
            "kyc": ["kyc", "know your customer", "verification"],
            "portfolio": ["portfolio", "holdings"],
            "watchlist": ["watchlist", "watch list"],
            "holding": ["holding", "portfolio"],
            "chart": ["chart", "performance", "graph"],
            "filter": ["filter", "sort", "sector"],
            "transfer": ["transfer"],
            "liquidate": ["liquidate", "close position"],
            "health score": ["health score"],
            "insights": ["insight", "analysis"],
            "peer": ["peer", "comparison", "benchmark"],
            "report": ["report", "download"],
            "storyteller": ["storyteller", "narrative"],
            "allocation": ["allocation", "diversif"],
            "mutual fund": ["mutual fund", "fund"],
            "robo": ["robo", "mashura"],
            "crowdfund": ["crowdfund"],
            "dividend": ["dividend"],
            "earnings": ["earnings"],
            "analyst": ["analyst", "rating"],
            "news": ["news"],
            "minichart": ["chart", "mini"],
            "account": ["account", "onboarding"],
            "guest": ["guest mode"],
            "tutorial": ["tutorial", "onboarding"],
            "notification": ["notification", "message"],
            "splash": ["splash", "welcome"],
        }
        for key, boost_terms in BOOSTS.items():
            if key in ename:
                for bt in boost_terms:
                    if bt in fname or bt in fdef:
                        score += 10

        if score > best_score:
            best = f
            best_score = score
            best_reason = f"'{ename}' matched '{f['name']}' (score={score})"

    return best, best_score, best_reason

# ── Screen definitions per file ──
# Each entry: (node_id, screen_name, section_name, journey_fallback)

ONBOARDING_SCREENS = [
    # Login section
    ("4012:25058", "Login", "Login", "Onboarding"),
    ("4012:27618", "Add Password", "Login", "Onboarding"),
    ("4012:30175", "Login — PIN Entry", "Login", "Onboarding"),
    ("4012:32732", "Splash Screen", "Login", "Onboarding"),
    ("4012:35284", "Face ID Setup 1", "Login", "Onboarding"),
    ("4012:35292", "Face ID Setup 2", "Login", "Onboarding"),
    # Summary KYC section — representative screens
    ("4012:5158", "Open Account — Summary", "Summary KYC", "Onboarding"),
    ("4012:5190", "KYC Option 1", "Summary KYC", "Onboarding"),
    # ARB Account section
    ("4012:6778", "Open Account — ARB", "ARB Account", "Onboarding"),
    ("4012:6812", "Open Account — ARB Step 2", "ARB Account", "Onboarding"),
    ("4012:6863", "Message — ARB Account", "ARB Account", "Onboarding"),
    # Non-ARB Account
    ("4012:6898", "Open Account — Non-ARB", "Non-ARB Account", "Onboarding"),
    ("4012:7055", "OTP Verification", "Non-ARB Account", "Onboarding"),
    # Edit KYC
    ("4012:6227", "Edit KYC — Personal Info", "Edit KYC", "Onboarding"),
    ("4012:6268", "Edit KYC — Address", "Edit KYC", "Onboarding"),
    ("4012:6314", "Edit KYC — Investment Profile", "Edit KYC", "Onboarding"),
    # Notifications & Messages
    ("4012:7219", "Message Screen 1", "Notifications & Messages", "Onboarding"),
    ("4012:7223", "Message Screen 2", "Notifications & Messages", "Onboarding"),
    # KYC main section — key screens
    ("4012:38168", "KYC — Open Account Step 1", "KYC", "Onboarding"),
    ("4012:38206", "KYC — Open Account Step 2", "KYC", "Onboarding"),
    ("4012:38244", "KYC — Open Account Step 3", "KYC", "Onboarding"),
    ("4012:38325", "KYC — Personal Details", "KYC", "Onboarding"),
    # Global Onboarding
    ("4012:42547", "Global Onboarding — Step 1", "Global Onboarding", "Onboarding"),
    ("4012:42581", "Global Onboarding — Step 2", "Global Onboarding", "Onboarding"),
    ("4012:42634", "Global Onboarding — OTP", "Global Onboarding", "Onboarding"),
    ("4012:42657", "Global Onboarding — Login", "Global Onboarding", "Onboarding"),
    # Corporate Onboarding
    ("4012:45232", "Corporate — OTP", "Corporate Onboarding", "Onboarding"),
    ("4012:45256", "Corporate — Open Account", "Corporate Onboarding", "Onboarding"),
    # Corporate KYC
    ("4012:50407", "Corporate KYC — Option 2", "Corporate KYC", "Onboarding"),
    ("4012:50436", "Corporate KYC — Address", "Corporate KYC", "Onboarding"),
    ("4012:50632", "Corporate KYC — Step 1", "Corporate KYC", "Onboarding"),
    # Fast Onboarding
    ("4314:21965", "Fast Onboarding", "Fast Onboarding", "Onboarding"),
    # Guest Mode
    ("4384:15739", "Guest Mode", "Guest Mode", "Onboarding"),
    # Tutorials
    ("4316:985", "Tutorials", "Tutorials", "Onboarding"),
    # First Engagement
    ("4388:38972", "First Login Engagement", "First Engagement", "Onboarding"),
    # Modal Screens
    ("4029:58160", "Modal — Verification", "Modals", "Onboarding"),
    ("4029:58256", "Modal — Confirmation", "Modals", "Onboarding"),
]

PORTFOLIOS_SCREENS = [
    # Saudi Portfolios (skip Holding Overview 2007:27437 — already extracted)
    ("2007:25488", "Saudi Portfolio Home", "Saudi Portfolios", "Portfolio Monitoring"),
    ("2007:25636", "Saudi Portfolio Home — Alt", "Saudi Portfolios", "Portfolio Monitoring"),
    ("2007:25898", "Index Filter", "Saudi Portfolios", "Portfolio Monitoring"),
    ("2007:27523", "Holding Overview — Alt State 1", "Saudi Portfolios", "Portfolio Monitoring"),
    ("2007:27595", "Holding Overview — Alt State 2", "Saudi Portfolios", "Portfolio Monitoring"),
    ("2007:28669", "Sectors Filter", "Saudi Portfolios", "Portfolio Monitoring"),
    ("2007:28734", "More Options Menu", "Saudi Portfolios", "Portfolio Monitoring"),
    ("2007:29544", "Choose Portfolio", "Saudi Portfolios", "Portfolio Monitoring"),
    ("2007:29592", "Shariah Filter", "Saudi Portfolios", "Portfolio Monitoring"),
    ("2007:29626", "Sectors Filter — Alt", "Saudi Portfolios", "Portfolio Monitoring"),
    ("2007:29662", "Research Filter", "Saudi Portfolios", "Portfolio Monitoring"),
    ("2007:29689", "Transfer Holdings — Step 1", "Saudi Portfolios", "Portfolio Monitoring"),
    ("2007:29726", "Transfer Holdings — Step 2", "Saudi Portfolios", "Portfolio Monitoring"),
    ("2007:29897", "Transfer — Success Message", "Saudi Portfolios", "Portfolio Monitoring"),
    ("2007:35066", "Add Holdings to Watchlist", "Saudi Portfolios", "Portfolio Monitoring"),
    ("2007:35148", "Tradable Rights Filter", "Saudi Portfolios", "Portfolio Monitoring"),
    ("2007:38461", "Asset Selection", "Saudi Portfolios", "Portfolio Monitoring"),
    ("2007:38601", "Liquidate Holdings — Step 1", "Saudi Portfolios", "Portfolio Monitoring"),
    ("2007:38664", "Liquidate Holdings — Step 2", "Saudi Portfolios", "Portfolio Monitoring"),
    ("2007:38746", "Liquidate Holdings — Confirm", "Saudi Portfolios", "Portfolio Monitoring"),
    # US Portfolios
    ("2007:39102", "US Portfolios Section", "US Portfolios", "Portfolio Monitoring"),
    # Mutual Fund Portfolios
    ("2007:42170", "Mutual Fund Portfolios Section", "Mutual Fund Portfolios", "Portfolio Monitoring"),
    # Crowdfund Portfolios
    ("2007:50525", "Crowdfund Portfolios Section", "Crowdfund Portfolios", "Portfolio Monitoring"),
    # LMS (Margin)
    ("2007:52965", "LMS Portfolios Section", "LMS Portfolios", "Portfolio Monitoring"),
    # Mashura (Robo)
    ("2007:55610", "Mashura Portfolios Section", "Mashura Portfolios", "Portfolio Monitoring"),
    # Performance Analysis
    ("2106:58072", "Top Stocks Analysis", "Portfolio Analysis", "Portfolio Monitoring"),
    ("2106:58349", "Gains & Losses Analysis", "Portfolio Analysis", "Portfolio Monitoring"),
    ("2106:58522", "Allocation Analysis", "Portfolio Analysis", "Portfolio Monitoring"),
    ("2106:58654", "Cash Allocation", "Portfolio Analysis", "Portfolio Monitoring"),
    ("2106:58790", "Trading Activity", "Portfolio Analysis", "Portfolio Monitoring"),
    ("2106:59106", "Peers Compare Landing", "Portfolio Analysis", "Portfolio Monitoring"),
    ("2050:14786", "Health Score", "Portfolio Analysis", "Portfolio Monitoring"),
    ("2050:15143", "Health Score — Detail", "Portfolio Analysis", "Portfolio Monitoring"),
    ("2050:15509", "Factor Breakdown", "Portfolio Analysis", "Portfolio Monitoring"),
    # Reports
    ("2108:84715", "Saudi Reports Section", "Reports", "Portfolio Monitoring"),
    ("2108:89590", "Mashura Reports Section", "Reports", "Portfolio Monitoring"),
    # Digital StoryTeller
    ("2123:68770", "Digital StoryTeller Section", "Digital StoryTeller", "Portfolio Monitoring"),
    # Switch Funds
    ("2007:35624", "Switch Funds — Step 1", "Saudi Portfolios", "Portfolio Monitoring"),
    ("2007:35698", "Switch Funds — Step 2", "Saudi Portfolios", "Portfolio Monitoring"),
]

WATCHLIST_SCREENS = [
    # Main watchlist screens
    ("2012:14669", "Story Wishlist", "Watchlist", "Saudi Market"),
    ("2012:31313", "Watchlist From View 1", "Watchlist", "Saudi Market"),
    ("2012:31364", "Watchlist From View 2", "Watchlist", "Saudi Market"),
    ("2012:35864", "Watchlist Empty", "Watchlist", "Saudi Market"),
    ("2012:35887", "Watchlist Main View", "Watchlist", "Saudi Market"),
    ("2012:39946", "Menu Item", "Watchlist", "Saudi Market"),
    ("2015:17180", "Watchlist Home", "Watchlist", "Saudi Market"),
    # Standalone screens in watchlist page
    ("2018:50473", "Moving Up Screen", "Watchlist Screens", "Saudi Market"),
    ("2018:53055", "Moving Down Screen", "Watchlist Screens", "Saudi Market"),
    ("2018:55635", "Bulls vs Bears Screen", "Watchlist Screens", "Saudi Market"),
    ("2018:58217", "Analyst Ratings Screen", "Watchlist Screens", "Saudi Market"),
    ("2018:60820", "News Screen", "Watchlist Screens", "Saudi Market"),
    ("2018:63412", "Dividends Screen", "Watchlist Screens", "Saudi Market"),
    ("2018:66195", "Earnings Screen", "Watchlist Screens", "Saudi Market"),
    ("2018:68787", "Insider Trades Screen", "Watchlist Screens", "Saudi Market"),
    ("2018:71425", "Government Trades Screen", "Watchlist Screens", "Saudi Market"),
    ("2018:76715", "Story Wishlist Detail", "Watchlist Screens", "Saudi Market"),
    # Minichart variants (second section)
    ("2012:72580", "Minichart View 1", "Watchlist Charts", "Saudi Market"),
    ("2012:72588", "Minichart View 2", "Watchlist Charts", "Saudi Market"),
]


# ── Main extraction ──
all_nodes = []
counter = [0]
HOLDINGS_FRAME_ID = "2007:27437"  # Skip this — already extracted

def next_id():
    counter[0] += 1
    return f"scr-{counter[0]:04d}"

def process_file(file_name, file_key, screen_defs):
    """Process one Figma file: fetch screens, extract elements, link features."""
    print(f"\n{'='*60}")
    print(f"  Starting: {file_name}")
    print(f"{'='*60}")

    file_root_id = next_id()
    all_nodes.append({
        "id": file_root_id,
        "name": file_name,
        "type": "group",
        "parent_id": None,
        "figma_file": file_name,
        "figma_url": f"https://www.figma.com/design/{file_key}",
        "linked_feature_id": None,
        "linked_brd": [],
        "match_reason": f"File root: {file_name}",
    })

    # Group screens by section
    sections = {}
    for (nid, sname, sec_name, journey) in screen_defs:
        sections.setdefault(sec_name, []).append((nid, sname, journey))

    for sec_name, screens in sections.items():
        sec_id = next_id()
        all_nodes.append({
            "id": sec_id,
            "name": sec_name,
            "type": "group",
            "parent_id": file_root_id,
            "figma_file": file_name,
            "figma_url": f"https://www.figma.com/design/{file_key}",
            "linked_feature_id": None,
            "linked_brd": [],
            "match_reason": f"Section: {sec_name}",
        })

        for (node_id, screen_name, journey) in screens:
            # Skip Holdings frame (already migrated)
            if node_id == HOLDINGS_FRAME_ID:
                print(f"  Skipping {screen_name} (already in Holdings prototype)")
                continue

            print(f"  Fetching: {screen_name} ({node_id})...")

            # Check if this is a section-level node (contains sub-sections)
            is_section = node_id in ("2007:39102", "2007:42170", "2007:50525", "2007:52965",
                                     "2007:55610", "2108:84715", "2108:89590", "2123:68770",
                                     "4314:21965", "4384:15739", "4316:985", "4388:38972",
                                     "4029:58160", "4029:58256")

            depth = 4 if is_section else 8
            doc = get_node(file_key, node_id, depth=depth)
            if not doc:
                print(f"    WARN: Could not fetch node {node_id}")
                continue

            time.sleep(0.3)  # Rate limiting

            screen_id = next_id()

            # Try to match the screen itself to a feature
            feat_id, brd_list, reason = match_feature(screen_name, file_name, journey)

            all_nodes.append({
                "id": screen_id,
                "name": screen_name,
                "type": "screen",
                "parent_id": sec_id,
                "figma_file": file_name,
                "figma_url": figma_url(file_key, node_id),
                "linked_feature_id": feat_id,
                "linked_brd": brd_list,
                "match_reason": reason,
            })

            # Extract child elements
            elements = extract_elements(doc, file_key, screen_id, file_name, depth=0, max_depth=5)

            for elem in elements:
                eid = next_id()
                elem["id"] = eid
                if elem["parent_id"] is None:
                    elem["parent_id"] = screen_id

                if elem["type"] == "chrome":
                    elem["linked_feature_id"] = None
                    elem["linked_brd"] = []
                    elem["match_reason"] = "Chrome / decorative"
                else:
                    fid, brds, reason = match_feature(elem["name"], file_name, journey)
                    elem["linked_feature_id"] = fid
                    elem["linked_brd"] = brds
                    elem["match_reason"] = reason

                # Clean up internal field
                if "figma_node_id" in elem:
                    del elem["figma_node_id"]

                all_nodes.append(elem)

            print(f"    -> {len(elements)} elements extracted")

    print(f"  File total: {sum(1 for n in all_nodes if n['figma_file']==file_name)} nodes")

# ── Migrate existing Holdings nodes ──
print("Migrating existing Holdings prototype nodes...")
holdings_path = os.path.join(DATA, "screens-holdings-prototype.json")
holdings_migrated = 0
if os.path.exists(holdings_path):
    hdata = json.load(open(holdings_path))
    for node in hdata.get("nodes", []):
        all_nodes.append(node)
        holdings_migrated += 1
    print(f"  Migrated {holdings_migrated} Holdings nodes")
else:
    print("  WARN: screens-holdings-prototype.json not found")

# ── Process files ──
process_file("OnBoarding (KYC)", FILES["OnBoarding (KYC)"], ONBOARDING_SCREENS)
process_file("Portfolios", FILES["Portfolios"], PORTFOLIOS_SCREENS)
process_file("Watchlist", FILES["Watchlist"], WATCHLIST_SCREENS)

# ── Post-process: propagate screen-level links to unlinked children ──
print("\nPost-processing: propagating screen links to unlinked children...")
node_by_id = {n["id"]: n for n in all_nodes}
propagated = 0
for n in all_nodes:
    if n["type"] in ("group", "screen"):
        continue
    if n.get("linked_feature_id"):
        continue
    if "REVIEW" not in n.get("linked_brd", []):
        continue
    # Find parent screen
    pid = n.get("parent_id")
    parent = node_by_id.get(pid)
    # Walk up to find a screen parent
    visited = set()
    while parent and parent["type"] not in ("screen",) and parent.get("parent_id") and parent["id"] not in visited:
        visited.add(parent["id"])
        parent = node_by_id.get(parent.get("parent_id"))
    if parent and parent.get("linked_feature_id") and parent.get("linked_brd") and "REVIEW" not in parent.get("linked_brd", []):
        n["linked_feature_id"] = parent["linked_feature_id"]
        n["linked_brd"] = parent["linked_brd"]
        n["match_reason"] = f"Inherited from parent screen '{parent['name']}' -> {parent['linked_feature_id']}"
        propagated += 1
print(f"  Propagated {propagated} links from parent screens")

# ── Write consolidated JSON ──
output = {
    "_meta": {
        "schema_version": "1.0",
        "last_updated": date.today().strftime("%Y-%m-%d"),
        "files_processed": ["OnBoarding (KYC)", "Portfolios", "Watchlist"],
        "generated_by": "extract_screens_batch1.py",
    },
    "screens": all_nodes,
}

out_path = os.path.join(DATA, "screens.json")
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(output, f, indent=2, ensure_ascii=False)

# ── Stats ──
print(f"\n{'='*60}")
print(f"  EXTRACTION SUMMARY")
print(f"{'='*60}")

total = len(all_nodes)
by_file = {}
by_type = {}
linked_count = 0
review_count = 0
chrome_count = 0
unlinked_count = 0

for n in all_nodes:
    ff = n.get("figma_file", "?")
    by_file[ff] = by_file.get(ff, 0) + 1
    nt = n.get("type", "?")
    by_type[nt] = by_type.get(nt, 0) + 1

    brds = n.get("linked_brd", [])
    fid = n.get("linked_feature_id")

    if nt == "chrome":
        chrome_count += 1
    elif fid and brds and "REVIEW" not in brds:
        linked_count += 1
    elif "REVIEW" in brds:
        review_count += 1
    else:
        unlinked_count += 1

# Leaf nodes only for percentages
leaf_nodes = [n for n in all_nodes if n["type"] not in ("group",)]
leaf_total = len(leaf_nodes)
leaf_linked = sum(1 for n in leaf_nodes if n.get("linked_feature_id") and n.get("linked_brd") and "REVIEW" not in n.get("linked_brd", []) and n["type"] != "chrome")
leaf_review = sum(1 for n in leaf_nodes if "REVIEW" in n.get("linked_brd", []) and n["type"] != "chrome")
leaf_chrome = sum(1 for n in leaf_nodes if n["type"] == "chrome")
leaf_unlinked = leaf_total - leaf_linked - leaf_review - leaf_chrome

print(f"Total nodes:         {total}")
print(f"  Holdings migrated: {holdings_migrated}")
print(f"  New nodes:         {total - holdings_migrated}")
print(f"\nBy file:")
for ff, cnt in sorted(by_file.items()):
    print(f"  {ff:25s}  {cnt}")
print(f"\nBy type:")
for nt, cnt in sorted(by_type.items()):
    print(f"  {nt:15s}  {cnt}")

print(f"\nLinking (leaf nodes): {leaf_total}")
if leaf_total > 0:
    print(f"  Confident:   {leaf_linked:4d}  ({100*leaf_linked/leaf_total:.0f}%)")
    print(f"  REVIEW:      {leaf_review:4d}  ({100*leaf_review/leaf_total:.0f}%)")
    print(f"  Unlinked:    {leaf_unlinked:4d}  ({100*leaf_unlinked/leaf_total:.0f}%)")
    print(f"  Chrome:      {leaf_chrome:4d}  ({100*leaf_chrome/leaf_total:.0f}%)")

# Top 10 features by link count
feat_counts = {}
for n in all_nodes:
    fid = n.get("linked_feature_id")
    if fid:
        feat_counts[fid] = feat_counts.get(fid, 0) + 1

print(f"\nTop 10 most-linked features:")
for fid, cnt in sorted(feat_counts.items(), key=lambda x: -x[1])[:10]:
    fname = feat_by_id.get(fid, {}).get("name", "?")
    print(f"  {fid:10s}  {cnt:3d}  {fname}")

# Features with figma_file set but never matched
matched_feats = set(feat_counts.keys())
for ff in FILES:
    file_feats = [f for f in features if f.get("figma_file") == ff]
    unmatched = [f for f in file_feats if f["id"] not in matched_feats]
    if unmatched:
        print(f"\nFeatures with figma_file='{ff}' but never matched:")
        for f in unmatched:
            print(f"  {f['id']:10s}  {f['name']}")

print(f"\nSaved: {out_path}")
print(f"{'='*60}")
