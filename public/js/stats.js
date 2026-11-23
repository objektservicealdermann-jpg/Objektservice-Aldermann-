/* Besucherstatistik ohne Cookies (PostHog, EU-Server).
   Gespeichert wird nichts im Browser; IP-Adressen werden von PostHog verworfen.
   Gezählt werden nur Seitenaufrufe und Klicks auf Anrufen / WhatsApp / E-Mail. */
(function () {
  if (navigator.doNotTrack === '1' || window.doNotTrack === '1') return;
  if (!/objektservicealdermann\.com$/.test(location.hostname)) return;

  function start() {
    var s = document.createElement('script');
    s.src = '/js/vendor/posthog.js?v=1.454.0';
    s.async = true;
    s.onload = function () {
      if (!window.posthog || !window.posthog.init) return;
      window.posthog.init('phc_o9fefbSKWAAAsRfRLAFjEd9oJJRNfh744s6n5d8aPZZx', {
        api_host: 'https://eu.i.posthog.com',
        cookieless_mode: 'always',
        persistence: 'memory',
        autocapture: false,
        capture_pageview: true,
        capture_pageleave: false,
        disable_session_recording: true,
        disable_surveys: true,
        disable_external_dependency_loading: true,
        advanced_disable_flags: true,
        person_profiles: 'never',
        ip: false
      });
    };
    document.head.appendChild(s);
  }

  document.addEventListener('click', function (e) {
    var a = e.target.closest && e.target.closest('a[href]');
    if (!a || !window.posthog || !window.posthog.capture) return;
    var h = a.getAttribute('href') || '';
    var name = /^tel:/.test(h) ? 'Klick Anrufen' : /wa\.me|whatsapp/.test(h) ? 'Klick WhatsApp' : /^mailto:/.test(h) ? 'Klick E-Mail' : null;
    if (name) window.posthog.capture(name, { seite: location.pathname });
  }, true);

  if (document.readyState === 'complete') setTimeout(start, 1500);
  else window.addEventListener('load', function () { setTimeout(start, 1500); });
})();
