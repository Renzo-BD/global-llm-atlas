(() => {
  const statusLabel = (meta) => {
    if (!meta) return '<span class="cap unknown" title="Android availability not independently verified">?</span>';
    if (meta.status === 'native') return '<span class="cap yes" title="Official Android app verified">✓</span>';
    if (meta.status === 'regional') return '<span class="cap" title="Official regional Android distribution">R</span>';
    if (meta.status === 'pwa') return '<span class="cap" title="Installable web app / PWA">PWA</span>';
    return '<span class="cap unknown">?</span>';
  };

  const addHeaders = () => {
    const row = document.querySelector('table thead tr');
    if (!row || row.querySelector('[data-android-col]')) return;
    const headers = [...row.children];
    const webIndex = headers.findIndex((th) => th.textContent.trim().toLowerCase() === 'web');
    if (webIndex < 0) return;
    const android = document.createElement('th');
    android.dataset.androidCol = '1';
    android.textContent = 'Android';
    const play = document.createElement('th');
    play.dataset.androidCol = '1';
    play.textContent = 'Google Play';
    row.insertBefore(play, row.children[webIndex + 1] || null);
    row.insertBefore(android, play);
  };

  const enrichRows = (androidById) => {
    const body = document.getElementById('rows');
    if (!body) return;
    [...body.querySelectorAll('tr')].forEach((tr) => {
      if (tr.querySelector('[data-android-cell]')) return;
      const id = tr.querySelector('.sub')?.textContent?.split('·')[0]?.trim();
      if (!id) return;
      const meta = androidById.get(id);
      const cells = [...tr.children];
      const webCell = cells[7];
      if (!webCell) return;

      const androidTd = document.createElement('td');
      androidTd.dataset.androidCell = '1';
      androidTd.innerHTML = statusLabel(meta);

      const playTd = document.createElement('td');
      playTd.dataset.androidCell = '1';
      if (meta?.distribution === 'google-play' && meta.url) {
        const a = document.createElement('a');
        a.className = 'open';
        a.href = meta.url;
        a.target = '_blank';
        a.rel = 'noopener noreferrer';
        a.textContent = 'Play ↗';
        playTd.appendChild(a);
      } else {
        playTd.innerHTML = '<span class="sub">—</span>';
      }

      tr.insertBefore(playTd, webCell.nextSibling);
      tr.insertBefore(androidTd, playTd);
    });
  };

  const start = async () => {
    try {
      addHeaders();
      const response = await fetch('./data/android.json', { cache: 'no-store' });
      if (!response.ok) throw new Error(`HTTP ${response.status}`);
      const data = await response.json();
      const androidById = new Map((data.entries || []).map((x) => [x.id, x]));
      const body = document.getElementById('rows');
      if (!body) return;
      const refresh = () => enrichRows(androidById);
      refresh();
      new MutationObserver(refresh).observe(body, { childList: true, subtree: false });
    } catch (err) {
      console.error('Android column enrichment failed:', err);
    }
  };

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', start, { once: true });
  } else {
    start();
  }
})();
