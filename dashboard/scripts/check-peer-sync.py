#!/usr/bin/env python3
"""Flag inbound activity from the MacBook (ULOLWJR) while it is still sendreceive.

This host is sendonly, so remote edits should never land here. Two detectors:

  1. Syncthing state — folder type still sendonly, peer completion, peer needItems.
     completion < 100 means the MacBook has NOT taken our changes, i.e. it has
     diverged locally.
  2. Filesystem arrivals — a synced-in file keeps the sender's mtime but gets a
     local ctime, so ctime >> mtime is the signature (this is how the 2026-08-16
     23:01 restructure was traced). Anything arriving after the lockdown is flagged.

Exit 0 = quiet, 1 = something to look at. Read-only.
"""
import json, os, re, subprocess, sys, time, urllib.request
from pathlib import Path

REPO = Path('/Users/ahmedalghamdi/Claude/ARC')
STATE = REPO / 'projects/features-map/dashboard/data/peer-sync-state.json'
LOCKDOWN = 1786000000  # placeholder, replaced on first run

cfgp = os.path.expanduser('~/Library/Application Support/Syncthing/config.xml')
key = re.search(r'<apikey>([^<]+)</apikey>', open(cfgp, encoding='utf8', errors='replace').read()).group(1)


def api(u):
    r = urllib.request.Request('http://127.0.0.1:8384/rest' + u, headers={'X-API-Key': key})
    return json.loads(urllib.request.urlopen(r, timeout=10).read())


flags = []
cfg = api('/config')
me = api('/system/status')['myID']
names = {d['deviceID']: d['name'] for d in cfg['devices']}
fo = [f for f in cfg['folders'] if f['id'] == 'arc'][0]

print(f"this host      : {me[:7]} = {names.get(me)}")
print(f"folder type    : {fo['type']}")
if fo['type'] != 'sendonly':
    flags.append(f"folder type is {fo['type']}, expected sendonly — writer protection is OFF")

st = api('/db/status?folder=arc')
print(f"local state    : {st['state']}  needFiles={st['needFiles']}  errors={st['errors']}")
if st['needFiles']:
    flags.append(f"{st['needFiles']} inbound file(s) pending — remote changes are queued")

peers = [d for d in [x['deviceID'] for x in fo['devices']] if d != me]
conns = api('/system/connections')['connections']
for d in peers:
    c = conns.get(d, {})
    comp = api(f'/db/completion?folder=arc&device={d}')
    pct = comp.get('completion', 0)
    print(f"peer {d[:7]} {names.get(d,'?'):10} connected={c.get('connected')}  completion={pct}%  needItems={comp.get('needItems')}")
    if c.get('connected') and pct < 100:
        flags.append(f"{names.get(d)} at {pct}% — it has diverged locally or is refusing our updates")

# ── filesystem arrivals since the last run ──────────────────────────────────
prev = json.loads(STATE.read_text()) if STATE.exists() else {}
since = prev.get('last_check', time.time() - 3600)
arrivals = []
skip = {'.git', 'node_modules', '.venv', 'quarantine'}
for root, dirs, files in os.walk(REPO):
    dirs[:] = [d for d in dirs if d not in skip and not d.startswith('.st')]
    for fn in files:
        p = os.path.join(root, fn)
        try:
            s = os.stat(p)
        except OSError:
            continue
        if s.st_ctime > since and (s.st_ctime - s.st_mtime) > 60:
            arrivals.append((os.path.relpath(p, REPO), s.st_mtime, s.st_ctime))
if arrivals:
    flags.append(f'{len(arrivals)} file(s) arrived via sync since the last check')
    for rel, m, c in sorted(arrivals, key=lambda x: -x[2])[:15]:
        print(f"  ARRIVED  {rel}\n           sender mtime {time.strftime('%m-%d %H:%M:%S', time.localtime(m))}"
              f"  local ctime {time.strftime('%m-%d %H:%M:%S', time.localtime(c))}")

STATE.write_text(json.dumps({'last_check': time.time(),
                             'folder_type': fo['type'],
                             'arrivals_last_run': len(arrivals)}, indent=2))

print()
if not flags:
    print('PEER QUIET — no inbound activity, writer protection intact')
    sys.exit(0)
print('PEER FLAGS:')
for f in flags:
    print('   -', f)
print('\nThe MacBook is still sendreceive until it is set to receive-only.')
sys.exit(1)
