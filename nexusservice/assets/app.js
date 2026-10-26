(function () {
  var doc = document.documentElement;

  var menuBtn = document.getElementById('menuBtn');
  if (menuBtn) menuBtn.addEventListener('click', function () {
    var open = doc.classList.toggle('menu-open');
    menuBtn.setAttribute('aria-expanded', open);
    menuBtn.textContent = open ? 'Stäng' : 'Meny';
  });

  // Rullgardinsmeny för tjänster
  var dd = document.querySelector('.dd');
  if (dd) {
    var btn = dd.querySelector('button');
    var set = function (open) { dd.classList.toggle('open', open); btn.setAttribute('aria-expanded', open); };
    btn.addEventListener('click', function (e) { e.stopPropagation(); set(!dd.classList.contains('open')); });
    document.addEventListener('click', function (e) { if (!dd.contains(e.target)) set(false); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') set(false); });
  }

  // Offertformuläret: förifyll från länkar som kontakt.html?tjanst=maleri&kund=brf
  var form = document.getElementById('offertForm');
  if (!form) return;
  var q = new URLSearchParams(location.search);
  ['kund', 'tjanst'].forEach(function (name) {
    var v = q.get(name);
    var el = v && form.querySelector('input[name="' + name + '"][value="' + v + '"]');
    if (el) el.checked = true;
  });

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    if (!form.checkValidity()) { form.reportValidity(); return; }
    var fd = new FormData(form);
    var text = function (name, val) {
      var el = form.querySelector('input[name="' + name + '"][value="' + val + '"]');
      return el ? el.parentNode.textContent.trim() : val;
    };
    var tjanster = fd.getAll('tjanst').map(function (v) { return text('tjanst', v); });
    var body = [
      'Kund: ' + text('kund', fd.get('kund')),
      'Gäller: ' + (tjanster.join(', ') || 'Ej angivet'),
      '',
      'Namn: ' + fd.get('namn'),
      'Företag/förening: ' + (fd.get('foretag') || '-'),
      'Telefon: ' + fd.get('telefon'),
      'E-post: ' + fd.get('epost'),
      'Adress: ' + (fd.get('adress') || '-'),
      'När: ' + (fd.get('start') || '-'),
      '',
      fd.get('beskrivning')
    ].join('\n');
    var subject = 'Offertförfrågan: ' + (tjanster[0] || 'Nexus Service') + ', ' + fd.get('namn');
    location.href = 'mailto:info@nexusserviceab.se?subject=' + encodeURIComponent(subject) + '&body=' + encodeURIComponent(body);
    document.getElementById('formStatus').textContent = 'Ditt e-postprogram öppnas med förfrågan ifylld. Skicka mejlet så hör vi av oss. Om inget händer kan du ringa 076-123 45 67.';
  });
})();
