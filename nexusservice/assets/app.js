(function () {
  var doc = document.documentElement;

  // Mobilmeny
  var menuBtn = document.getElementById('menuBtn');
  if (menuBtn) menuBtn.addEventListener('click', function () {
    var hdr = document.querySelector('.header');
    document.getElementById('nav').style.top = hdr.getBoundingClientRect().bottom + 'px';
    var open = doc.classList.toggle('menu-open');
    menuBtn.setAttribute('aria-expanded', open);
    menuBtn.setAttribute('aria-label', open ? 'Stäng meny' : 'Öppna meny');
  });

  // Megameny: klick öppnar, hover öppnar på desktop, Esc och klick utanför stänger
  var mega = document.querySelector('.has-mega');
  if (mega) {
    var trigger = mega.querySelector('button');
    var desktop = window.matchMedia('(min-width: 981px)');
    var timer;
    var set = function (open) {
      mega.classList.toggle('open', open);
      trigger.setAttribute('aria-expanded', open);
    };
    trigger.addEventListener('click', function () { set(!mega.classList.contains('open')); });
    mega.addEventListener('mouseenter', function () { if (desktop.matches) { clearTimeout(timer); set(true); } });
    mega.addEventListener('mouseleave', function () { if (desktop.matches) timer = setTimeout(function () { set(false); }, 180); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') { set(false); doc.classList.remove('menu-open'); } });
    document.addEventListener('click', function (e) { if (desktop.matches && !mega.contains(e.target)) set(false); });
  }

  // Tjänsteindex: förhandsbild följer raden man pekar på
  var preview = document.querySelector('.svc-preview');
  if (preview) {
    var imgs = preview.querySelectorAll('img');
    var cap = preview.querySelector('figcaption');
    var rows = document.querySelectorAll('.svc-row');
    rows.forEach(function (row, i) {
      var show = function () {
        rows.forEach(function (r) { r.classList.remove('is-active'); });
        row.classList.add('is-active');
        imgs.forEach(function (img, j) { img.classList.toggle('is-on', j === i); });
        cap.textContent = row.querySelector('h3').textContent;
      };
      row.addEventListener('mouseenter', show);
      row.addEventListener('focus', show);
    });
  }

  // Innehållsförteckning på tjänstesidan
  var toc = document.querySelectorAll('.toc a');
  if (toc.length && 'IntersectionObserver' in window) {
    var map = {};
    toc.forEach(function (a) { map[a.getAttribute('href').slice(1)] = a; });
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) {
          toc.forEach(function (a) { a.classList.remove('is-active'); });
          var a = map[en.target.id]; if (a) a.classList.add('is-active');
        }
      });
    }, { rootMargin: '-30% 0px -60% 0px' });
    document.querySelectorAll('.svc[id]').forEach(function (s) { io.observe(s); });
  }

  // Diskret inrullning
  var rev = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    var ro = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add('in'); ro.unobserve(en.target); } });
    }, { rootMargin: '0px 0px -8% 0px' });
    rev.forEach(function (el) { ro.observe(el); });
  } else rev.forEach(function (el) { el.classList.add('in'); });

  // Förifyll offertformuläret från länkar som ?kund=brf&tjanst=maleri
  var form = document.getElementById('offertForm');
  if (form) {
    var q = new URLSearchParams(location.search);
    var kund = q.get('kund');
    if (kund) { var r = form.querySelector('input[name="kund"][value="' + kund + '"]'); if (r) r.checked = true; }
    var tj = q.get('tjanst');
    if (tj) { var c = form.querySelector('input[name="tjanst"][value="' + tj + '"]'); if (c) c.checked = true; }

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var status = document.getElementById('formStatus');
      if (!form.checkValidity()) { form.reportValidity(); return; }
      var fd = new FormData(form);
      var labelOf = function (name, val) {
        var el = form.querySelector('input[name="' + name + '"][value="' + val + '"]');
        return el ? el.nextElementSibling.textContent : val;
      };
      var tjanster = fd.getAll('tjanst').map(function (v) { return labelOf('tjanst', v); });
      var lines = [
        'Kundtyp: ' + labelOf('kund', fd.get('kund')),
        'Tjänster: ' + (tjanster.length ? tjanster.join(', ') : 'Ej angivet'),
        '',
        'Namn: ' + fd.get('namn'),
        'Företag/BRF: ' + (fd.get('foretag') || '–'),
        'Telefon: ' + fd.get('telefon'),
        'E-post: ' + fd.get('epost'),
        'Adress/ort: ' + (fd.get('adress') || '–'),
        'Önskad start: ' + (fd.get('start') || '–'),
        '',
        'Beskrivning:',
        fd.get('beskrivning')
      ];
      var subject = 'Offertförfrågan – ' + (tjanster[0] || 'Nexus Service') + ' – ' + fd.get('namn');
      location.href = 'mailto:info@nexusserviceab.se?subject=' + encodeURIComponent(subject) + '&body=' + encodeURIComponent(lines.join('\n'));
      status.textContent = 'Ditt e-postprogram öppnas med förfrågan ifylld. Skicka mejlet så återkommer vi. Fungerar det inte – ring 076-123 45 67.';
    });
  }
})();
