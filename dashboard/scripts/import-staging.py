#!/usr/bin/env python3
"""IMPORT — validate and diff staging/features-edit.xlsx against the master.

Default run is READ-ONLY: it validates, prints a cell-level diff, and stops.
Nothing is written until Ahmed confirms and the run is repeated with --apply,
which routes the changes through the guardrail (backup → apply → save → re-open
→ verify → diff → change note → regenerate → verify JSON counts).

The staging file NEVER replaces features-master.xlsx. Only the differing cells in
name, status and Level1–Level7 are copied across.
"""
import hashlib, json, shutil, sys
from datetime import date
from pathlib import Path
import openpyxl

D = Path(__file__).resolve().parents[1]
MASTER = D / 'features-master.xlsx'
STAGE = D / 'staging' / 'features-edit.xlsx'
APPLY = '--apply' in sys.argv

COLS = {'name': 2, 'status': 4,
        'Level1': 21, 'Level2': 22, 'Level3': 23, 'Level4': 24,
        'Level5': 25, 'Level6': 26, 'Level7': 27}
VALID_STATUS = {'Live', 'Planned', 'Gap'}


def read(path):
    wb = openpyxl.load_workbook(path)
    if 'Features' not in wb.sheetnames:
        return None, wb, f"sheet 'Features' not found (sheets: {wb.sheetnames})"
    ws = wb['Features']
    rows = {}
    for r in range(4, ws.max_row + 1):
        i = ws.cell(r, 1).value
        if i: rows[str(i).strip()] = r
    return ws, wb, rows


# ── (a) VALIDATE ────────────────────────────────────────────────────────────
if not STAGE.exists():
    print(f'no staging file at {STAGE} — nothing to import'); sys.exit(0)

mws, mwb, mrows = read(MASTER)
sws, swb, srows = read(STAGE)
problems = []
if isinstance(srows, str):
    print('VALIDATION FAILED:'); print('   ', srows); sys.exit(1)

mh = [mws.cell(2, c).value for c in range(1, 28)]
sh = [sws.cell(2, c).value for c in range(1, 28)]
if mh != sh:
    for c, (a, b) in enumerate(zip(mh, sh), 1):
        if a != b: problems.append(f'header col {c}: master {a!r} vs staging {b!r}')

blank = [r for r in range(4, sws.max_row + 1)
         if any(sws.cell(r, c).value not in (None, '') for c in range(2, 12))
         and not sws.cell(r, 1).value]
for r in blank: problems.append(f'row {r}: data present but id is empty')

for fid, r in srows.items():
    st = sws.cell(r, COLS['status']).value
    if st not in VALID_STATUS:
        problems.append(f'{fid}: status {st!r} not in Live/Planned/Gap')
    lv = [sws.cell(r, COLS[f'Level{i}']).value for i in range(1, 8)]
    # Level5 is group-only, so a direct feature legitimately has Level5 empty and
    # Level6 filled. The rules are: Level6 needs Level4; Level7 needs Level5 AND
    # Level6; Levels 1-4 must not skip.
    if lv[5] and not lv[3]: problems.append(f'{fid}: Level6 filled but Level4 empty')
    if lv[6] and not (lv[4] and lv[5]): problems.append(f'{fid}: Level7 filled without Level5+Level6')
    if lv[4] and not lv[3]: problems.append(f'{fid}: Level5 filled but Level4 empty')
    for i in range(1, 4):
        if lv[i] and not lv[i - 1]: problems.append(f'{fid}: Level{i+1} filled but Level{i} empty')

if problems:
    print(f'VALIDATION FAILED — {len(problems)} problem(s):')
    for p in problems: print('   ', p)
    print('\nSTOPPED. Fix the staging file and re-run.')
    sys.exit(1)
print(f'VALIDATION OK — sheet, headers, ids, statuses and Level paths all clean '
      f'({len(srows)} rows in staging, {len(mrows)} in master)')

# ── (b) DIFF ────────────────────────────────────────────────────────────────
changes, unknown = [], []
for fid, sr in srows.items():
    mr = mrows.get(fid)
    if mr is None:
        unknown.append(fid); continue
    for label, col in COLS.items():
        a, b = mws.cell(mr, col).value, sws.cell(sr, col).value
        if (a or None) != (b or None):
            changes.append((fid, label, a, b, mr, col))

print(f'\nDIFF — {len(changes)} cell change(s) across {len({c[0] for c in changes})} row(s)')
for fid, label, a, b, _, _ in changes:
    print(f'   {fid:9} {label:7} {a!r} -> {b!r}')
if unknown:
    print(f'\n   {len(unknown)} staging id(s) not in master (would be new rows — not auto-created): {unknown}')
missing = [f for f in mrows if f not in srows]
if missing:
    print(f'   {len(missing)} master id(s) absent from staging — ignored, never deleted')

if not changes:
    print('\nNothing to apply. Staging file left in place.'); sys.exit(0)

# ── (c) APPLY — only with explicit confirmation ─────────────────────────────
if not APPLY:
    print('\nREAD-ONLY RUN. Nothing written.')
    print('Confirm the diff above, then re-run:  python3 import-staging.py --apply')
    sys.exit(0)

bak = MASTER.with_name(MASTER.name + f'.bak-{date.today().isoformat()}-import-staging')
shutil.copyfile(MASTER, bak)
print(f'\nbackup -> {bak.name}')
for fid, label, a, b, mr, col in changes:
    mws.cell(mr, col).value = b
total = sum(1 for r in range(4, mws.max_row + 1) if mws.cell(r, 1).value)
mws.cell(3, 1).value = (f"Last updated: {date.today().strftime('%d %b %Y')}  |  Schema v1.6  "
                        f"|  {total} features  |  Level1-7 hierarchy (Saudi Portfolio)")
mwb.save(MASTER)

# re-open fresh and confirm every change landed
rws, _, rrows = read(MASTER)
bad = [f'{fid} {label}: expected {b!r}, found {rws.cell(rrows[fid], col).value!r}'
       for fid, label, a, b, mr, col in changes
       if (rws.cell(rrows[fid], col).value or None) != (b or None)]
if bad:
    print('APPLY FAILED — these cells did not land:')
    for x in bad: print('   ', x)
    print(f'Restore with: cp {bak.name} features-master.xlsx')
    sys.exit(1)
print(f'APPLIED and re-read clean — {len(changes)} cell(s) written')
print('\nNext (mandatory): xlsx-to-features-json.py, derive_status.py, verify JSON counts,')
print('re-record data/master-integrity.json, then delete the staging file.')
