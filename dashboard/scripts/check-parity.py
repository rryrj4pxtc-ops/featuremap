#!/usr/bin/env python3
"""Structural identity certification — Saudi Market vs US Market journey.

Counterparts are keyed by (screen, parent-chain, name) — position-independent, because
us-only rows legitimately shift display_order on one side. Order is checked separately,
on the shared set only.

Run:  scripts/check-parity.sh      (or: python3 scripts/check-parity.py)
Exit: 0 = STRUCTURALLY IDENTICAL, 1 = failures printed.
"""
import json, sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
d = json.loads((BASE / 'data' / 'features_derived.json').read_text())
byid = {f['id']: f for f in d['features']}
# v2.2: the two Market/Orders custodian pairs collapsed onto `backends`, so the (GTN) row
# is archived and the (IBKR) row lost its suffix. Set reduced 4 -> 3.
EXPECTED_US_ONLY = {'Pre/Post Market Trading', 'Fractional Shares', 'Bonds Trading'}

# Rows that exist on one side because the OTHER market's structure forbids them.
# Tadawul has no extended-hours session, so the Saudi Pre/Post twins were deleted in
# v2.3.2 rather than carried as permanent Gaps. Symmetric to Rights Issue / Tradable
# Rights, which are Tadawul mechanics never created on the US side.
EXPECTED_MARKET_STRUCTURE = {'US-188', 'US-189', 'US-191', 'US-192',
                             'US-194', 'US-195', 'US-197', 'US-198'}

# Rows one market carries by PRODUCT DECISION, not market structure. Ahmed ruled
# 2026-08-26 that Government Trades and Insider Trades are needed at US market level
# but not at Saudi market level; both remain shared on the Stock Page.
EXPECTED_PRODUCT_DECISION = {'US-008', 'US-031'}


def par(f):
    for t in (f.get('tags') or []):
        if str(t).startswith('sub-of:'):
            return str(t).split(':', 1)[1].strip()


def chain(f):
    out, c = [], par(f)
    while c and c in byid:
        out.insert(0, byid[c]['name']); c = par(byid[c])
    return tuple(out)


def archived(f):
    return any(str(t).startswith('archived') for t in (f.get('tags') or []))


def klass(f):
    t = ' '.join(str(x) for x in (f.get('tags') or []))
    if 'custodian-branch' in t or 'twin-of' in t: return 'custodian-branch'
    if 'us-only' in t: return 'us-only'
    if 'deliberate-break' in t: return 'deliberate-break'
    if 'market-structure' in t: return 'market-structure'
    if 'us-market-level' in t: return 'product-decision'
    if 'duplicate-of' in t: return 'duplicate'
    return 'UNCLASSIFIED'


AREA = sys.argv[1] if len(sys.argv) > 1 and not sys.argv[1].startswith('-') else 'Market'
M = [f for f in d['features'] if f['journey'] in ('Saudi Market', 'US Trading')
     and f.get('area') == AREA and not archived(f)]
sa = [f for f in M if f['journey'] == 'Saudi Market']
us = [f for f in M if f['journey'] == 'US Trading']
key = lambda f: (f.get('screen'), chain(f), f['name'])
S = {key(f): f for f in sa}
U = {key(f): f for f in us}

only_us = [f for f in us if key(f) not in S]
only_sa = [f for f in sa if key(f) not in U]

# attribute identity on shared nodes
attr = []
for k, s in S.items():
    u = U.get(k)
    if not u: continue
    for name, get in (('parent', lambda f: (chain(f) or (None,))[-1]),
                      ('depth', lambda f: len(chain(f))),
                      ('is_container', lambda f: bool(f.get('is_container'))),
                      ('row_type', lambda f: f.get('row_type'))):
        if get(s) != get(u):
            attr.append((s['name'], name, get(s), get(u)))

# order identity on the shared set only
def seq(rows, shared):
    return [f['name'] for f in sorted([x for x in rows if key(x) in shared],
                                      key=lambda x: (str(x.get('screen')), x.get('display_order') or 0))]
shared = set(S) & set(U)
order_ok = seq(sa, shared) == seq(us, shared)

stat = [(s['name'], s.get('derived_status'), U[k].get('derived_status'))
        for k, s in S.items() if k in U and U[k].get('derived_status') != s.get('derived_status')]
bad = [f for f in only_us + only_sa if klass(f) == 'UNCLASSIFIED']
db = [f for f in only_us + only_sa if klass(f) == 'deliberate-break']
bl_s = [f for f in sa if not f.get('screen')]
bl_u = [f for f in us if not f.get('screen')]
uo = {f['name'] for f in only_us if klass(f) == 'us-only'}
ms = {f['id'] for f in only_us + only_sa if klass(f) == 'market-structure'}
pd_ = {f['id'] for f in only_us + only_sa if klass(f) == 'product-decision'}

print(f"STRUCTURAL IDENTITY CERTIFICATION — Saudi vs US · area={AREA}")
print(f"  rows: Saudi {len(sa)} · US {len(us)} · shared {len(shared)}")
for scr in ('Market Page', 'Stock Page', 'ETF Page', 'Sukuk Page', None):
    s = [f for f in sa if f.get('screen') == scr]; u = [f for f in us if f.get('screen') == scr]
    if s or u:
        print(f"    {str(scr or 'backlog'):14} Saudi {len(s):3} · US {len(u):3}")
print(f"\n  US-only ({len(only_us)}):")
for f in only_us: print(f"    {f['id']:8} {f['name'][:36]:38} [{klass(f)}]")
print(f"  Saudi-only ({len(only_sa)}):" + ("" if only_sa else " none"))
for f in only_sa: print(f"    {f['id']:8} {f['name'][:36]:38} [{klass(f)}]")
print(f"\n  attribute mismatches on shared nodes: {len(attr)}" + ("" if attr else "  (name/parent/depth/is_container/row_type identical)"))
for a in attr: print(f"    {a}")
print(f"  shared-set display order identical: {'YES' if order_ok else 'NO'}")
print(f"  status deltas: {len(stat)}")

gates = [("unclassified differences = 0", not bad, len(bad)),
         ("us-only set == the 4 expected", uo == EXPECTED_US_ONLY, sorted(uo ^ EXPECTED_US_ONLY) or '—'),
         ("deliberate-break class empty", not db, [f['id'] for f in db] or 0),
         ("market-structure == 8 expected", ms == EXPECTED_MARKET_STRUCTURE,
          sorted(ms ^ EXPECTED_MARKET_STRUCTURE) or '—'),
         ("product-decision == 2 expected", pd_ == EXPECTED_PRODUCT_DECISION,
          sorted(pd_ ^ EXPECTED_PRODUCT_DECISION) or '—'),
         ("custodian-branch classified", True, sum(1 for f in only_us + only_sa if klass(f) == 'custodian-branch')),
         ("backlog empty both sides", not bl_s and not bl_u, f"SA {len(bl_s)} US {len(bl_u)}"),
         ("structural attributes identical", not attr, len(attr)),
         ("shared-set order identical", order_ok, 'ok' if order_ok else 'differs')]
print("\n  GATES")
for n, ok, detail in gates:
    print(f"    {n:34} {'PASS' if ok else 'FAIL'}   {detail}")
ok = all(g[1] for g in gates)
print(f"\n  VERDICT: {'STRUCTURALLY IDENTICAL' if ok else 'NOT IDENTICAL'}")
sys.exit(0 if ok else 1)
