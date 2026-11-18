// Menü auf dem Handy auf- und zuklappen
(function () {
  var btn = document.querySelector('.menu-toggle');
  var menu = document.getElementById('menu');
  if (btn && menu) {
    btn.addEventListener('click', function () {
      var open = menu.classList.toggle('open');
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    menu.addEventListener('click', function (e) {
      if (e.target.tagName === 'A') { menu.classList.remove('open'); btn.setAttribute('aria-expanded', 'false'); }
    });
  }

  // Anfrageformular: öffnet das E-Mail-Programm mit vorausgefüllter Nachricht.
  // Es werden keine Daten an fremde Server übertragen.
  var form = document.getElementById('anfrage');
  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var f = form.elements;
      var subject = 'Anfrage über die Website – ' + f.leistung.value;
      var lines = [
        'Guten Tag Herr Aldermann,',
        '',
        'ich interessiere mich für: ' + f.leistung.value,
        '',
        'Objekt / Ort: ' + f.ort.value,
        '',
        f.nachricht.value,
        '',
        'Name: ' + f.name.value,
        'Telefon: ' + (f.telefon.value || '–'),
        '',
        'Viele Grüße'
      ];
      window.location.href = 'mailto:objektservicealdermann@gmail.com'
        + '?subject=' + encodeURIComponent(subject)
        + '&body=' + encodeURIComponent(lines.join('\n'));
    });
  }

  var y = document.getElementById('jahr');
  if (y) y.textContent = new Date().getFullYear();
})();
