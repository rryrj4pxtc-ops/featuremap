/* Trust bar — baseline version · data age · integrity/staleness badge.
 *
 * Renders a fixed strip at the top of every dashboard page so the page can never
 * silently show stale or drifted data.
 *
 *   source_md5   (features_derived.json)  = the workbook that generation READ
 *   master_md5   (status.json)            = the workbook as it is NOW
 *
 * They diverge exactly when someone edited the workbook and did not regenerate —
 * which is the failure that made a week of correct edits look like they had not
 * applied. That case renders amber STALE. status.json integrity:"drift" renders
 * red DRIFT and wins over everything else.
 */
(function () {
  var base = location.pathname.indexOf('/views/') >= 0 ? '..' : '.';

  function rel(iso) {
    if (!iso) return 'unknown';
    var s = (Date.now() - new Date(iso).getTime()) / 1000;
    if (s < 0) s = 0;
    if (s < 90) return 'just now';
    if (s < 5400) return Math.round(s / 60) + ' min ago';
    if (s < 172800) return Math.round(s / 3600) + ' h ago';
    return Math.round(s / 86400) + ' d ago';
  }

  function bar(items, badge) {
    var el = document.createElement('div');
    el.id = 'arc-trustbar';
    el.style.cssText =
      'position:sticky;top:0;z-index:9999;display:flex;gap:18px;align-items:center;' +
      'padding:6px 14px;font:12px/1.4 Arial,"Noto Sans Display",sans-serif;' +
      'background:#000045;color:#A2E3FF;border-bottom:1px solid #221AFB;';
    el.innerHTML = items.map(function (t) { return '<span>' + t + '</span>'; }).join('') +
      '<span style="margin-left:auto;padding:2px 10px;border-radius:10px;font-weight:700;' +
      'color:' + badge.fg + ';background:' + badge.bg + '">' + badge.text + '</span>';
    document.body.insertBefore(el, document.body.firstChild);
  }

  var OK    = { text: 'INTEGRITY OK', bg: '#20C992', fg: '#001018' };
  var STALE = { text: 'STALE — REGENERATE', bg: '#F1B53D', fg: '#001018' };
  var DRIFT = { text: 'DRIFT — DO NOT TRUST', bg: '#D44450', fg: '#FFFFFF' };
  var UNK   = { text: 'STATUS UNKNOWN', bg: '#808080', fg: '#FFFFFF' };

  function get(p) {
    return fetch(base + p + '?v=' + Date.now()).then(function (r) {
      return r.ok ? r.json() : null;
    }).catch(function () { return null; });
  }

  Promise.all([get('/data/features_derived.json'), get('/data/status.json')])
    .then(function (res) {
      var d = res[0], s = res[1];
      var meta = (d && d._meta) || {};
      var items = [
        '<b style="color:#fff">Baseline ' + (meta.baseline_version || '—') + '</b>',
        'Data generated ' + rel(meta.generated_at),
      ];
      var badge = UNK;
      if (s && s.integrity === 'drift') {
        badge = DRIFT;
        items.push('workbook changed outside the guardrail');
      } else if (s && meta.source_md5 && s.master_md5 && meta.source_md5 !== s.master_md5) {
        badge = STALE;
        items.push('workbook edited since this data was generated');
      } else if (s && s.integrity === 'ok') {
        badge = OK;
        items.push('checked ' + rel(s.checked_at));
      }
      bar(items, badge);
    });
})();
