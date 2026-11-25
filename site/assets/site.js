/* Enterprise Foundation Solutions — site script */
(function () {
  // ---- Settings the owner/developer can change ---------------------------
  var BUSINESS_EMAIL = 'Kofiyeboah05@yahoo.com';
  var WHATSAPP_NUMBER = '233244802816'; // 0244 802 816 in international format
  // Paste a form-service endpoint here (e.g. Formspree, Basin, Web3Forms) so
  // enquiries are saved and emailed. Left empty, the form opens a pre-filled
  // email in the visitor's mail app instead.
  var FORM_ENDPOINT = '';
  // -------------------------------------------------------------------------

  // Installable app: offline support (needs https or localhost)
  if ('serviceWorker' in navigator) {
    window.addEventListener('load', function () {
      navigator.serviceWorker.register('sw.js').catch(function () {});
    });
  }

  // "Install the app" card. Sits above the bottom action bar so nothing covers it.
  // Android/desktop Chrome: uses the browser's install prompt.
  // iPhone/iPad Safari: no prompt exists, so it shows the Add to Home Screen steps.
  (function () {
    var standalone = window.matchMedia('(display-mode: standalone)').matches || navigator.standalone;
    var KEY = 'efs-install-dismissed';
    var dismissed = +localStorage.getItem(KEY) || 0;
    if (standalone || Date.now() - dismissed < 14 * 864e5) return;
    var ua = navigator.userAgent;
    var ios = /iPhone|iPad|iPod/.test(ua) || (navigator.platform === 'MacIntel' && navigator.maxTouchPoints > 1);
    var iosSafari = ios && !/CriOS|FxiOS|EdgiOS|GSA\//.test(ua);
    var deferred = null;

    function show() {
      if (document.querySelector('.install-card')) return;
      var card = document.createElement('div');
      card.className = 'install-card';
      card.setAttribute('role', 'dialog');
      card.setAttribute('aria-label', 'Install the app');
      card.innerHTML =
        '<img src="assets/icon-192.png" alt="" width="44" height="44">' +
        '<div class="install-text"><strong>Get the EFS app</strong><span>' +
        (deferred ? 'Quick access from your home screen, even offline.'
          : 'Tap <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-label="Share"><path d="M12 3v12M7 8l5-5 5 5M5 13v6a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2v-6"/></svg> Share, then <b>Add to Home Screen</b>.') +
        '</span></div>' +
        (deferred ? '<button class="btn btn-primary install-go" type="button">Install</button>' : '') +
        '<button class="install-x" type="button" aria-label="Not now">&times;</button>';
      document.body.appendChild(card);
      document.body.classList.add('has-install');
      requestAnimationFrame(function () { card.classList.add('in'); });
      function close() {
        localStorage.setItem(KEY, Date.now());
        card.remove(); document.body.classList.remove('has-install');
      }
      card.querySelector('.install-x').addEventListener('click', close);
      var go = card.querySelector('.install-go');
      if (go) go.addEventListener('click', function () {
        deferred.prompt();
        deferred.userChoice.then(function () { deferred = null; close(); });
      });
    }

    window.addEventListener('beforeinstallprompt', function (e) {
      e.preventDefault(); deferred = e; setTimeout(show, 1500);
    });
    window.addEventListener('appinstalled', function () {
      var c = document.querySelector('.install-card'); if (c) c.remove();
      document.body.classList.remove('has-install');
    });
    if (iosSafari) setTimeout(show, 2500);
  })();

  // Scroll-in motion: cards and headings ease up as they come into view.
  // Skipped when the visitor has asked for reduced motion.
  if ('IntersectionObserver' in window && !window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    var items = document.querySelectorAll(
      'main h2, .card, .problem, .tile, .proof-grid, .founder-visual, .svc-tabs, .do-list li, .next-panel, .dark .wrap, .scene, .svc-photo');
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add('shown'); io.unobserve(en.target); }
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
    items.forEach(function (el) {
      // anything already on screen at load shows at once; siblings stagger
      var r = el.getBoundingClientRect();
      if (r.top < innerHeight && r.bottom > 0) return;
      var sibs = el.parentNode ? Array.prototype.indexOf.call(el.parentNode.children, el) : 0;
      el.style.setProperty('--d', Math.min(sibs, 4) * 0.07 + 's');
      el.classList.add('reveal');
      io.observe(el);
    });
    document.documentElement.classList.add('js-reveal');
  }

  // Mobile menu
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.getElementById('site-nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
      toggle.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
      document.body.classList.toggle('menu-open', open);
    });
  }

  // WhatsApp links carry a draft message; the visitor chooses to send it.
  document.querySelectorAll('[data-wa]').forEach(function (a) {
    var topic = a.getAttribute('data-wa');
    var text = 'Hello Enterprise Foundation Solutions, I would like to discuss ' +
      (topic ? 'your ' + topic + ' service.' : 'how you can help my business.');
    a.href = 'https://wa.me/' + WHATSAPP_NUMBER + '?text=' + encodeURIComponent(text);
    a.target = '_blank';
    a.rel = 'noopener';
  });

  // Contact-link click counts (no personal data). Hook into analytics later.
  document.addEventListener('click', function (e) {
    var a = e.target.closest('a');
    if (!a) return;
    var kind = a.href.indexOf('wa.me') > -1 ? 'whatsapp_click'
      : a.href.indexOf('tel:') === 0 ? 'call_click'
      : a.href.indexOf('mailto:') === 0 ? 'email_click'
      : a.classList.contains('cta-consult') ? 'consultation_click' : null;
    if (kind && window.gtag) window.gtag('event', kind, { page: location.pathname });
  });

  // ---- Service tabs (homepage) ----------------------------------------
  document.querySelectorAll('[data-tabs]').forEach(function (root) {
    var tabs = Array.prototype.slice.call(root.querySelectorAll('[role=tab]'));
    var panels = tabs.map(function (t) { return document.getElementById(t.getAttribute('aria-controls')); });
    root.classList.add('js');
    function select(i, focus) {
      tabs.forEach(function (t, j) {
        var on = j === i;
        t.setAttribute('aria-selected', on ? 'true' : 'false');
        t.tabIndex = on ? 0 : -1;
        panels[j].hidden = !on;
        panels[j].classList.toggle('enter', on);
      });
      if (focus) tabs[i].focus();
      // keep the active tab visible in the scrolling row on phones
      var list = tabs[i].parentNode;
      list.scrollTo({ left: tabs[i].offsetLeft - (list.clientWidth - tabs[i].offsetWidth) / 2, behavior: 'smooth' });
    }
    tabs.forEach(function (t, i) {
      t.addEventListener('click', function () { select(i, false); });
      t.addEventListener('keydown', function (e) {
        var k = e.key, n = tabs.length, to = null;
        if (k === 'ArrowRight') to = (i + 1) % n;
        else if (k === 'ArrowLeft') to = (i - 1 + n) % n;
        else if (k === 'Home') to = 0;
        else if (k === 'End') to = n - 1;
        if (to !== null) { e.preventDefault(); select(to, true); }
      });
    });
    select(0, false);
  });

  // ---- Enquiry form ------------------------------------------------------
  var form = document.getElementById('enquiry');
  if (!form) return;

  var params = new URLSearchParams(location.search);
  var svc = params.get('service');
  var select = form.querySelector('#service');
  if (svc && select) {
    for (var i = 0; i < select.options.length; i++) {
      if (select.options[i].value === svc) select.value = svc;
    }
  }
  var src = form.querySelector('#source');
  if (src) src.value = params.get('from') || document.referrer || '';

  function field(id) { return form.querySelector('#' + id); }
  function setInvalid(id, bad) {
    var el = field(id); if (!el) return;
    el.closest('.field').classList.toggle('invalid', bad);
    el.setAttribute('aria-invalid', bad ? 'true' : 'false');
  }
  function validate() {
    var ok = true;
    ['name', 'business', 'service', 'challenge'].forEach(function (id) {
      var bad = !field(id).value.trim(); setInvalid(id, bad); if (bad) ok = false;
    });
    var email = field('email').value.trim();
    var phone = field('phone').value.trim();
    var emailBad = email && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
    var phoneBad = phone && phone.replace(/[^\d]/g, '').length < 9;
    var none = !email && !phone;
    setInvalid('email', none || emailBad);
    setInvalid('phone', none || phoneBad);
    var contactErr = document.getElementById('contact-err');
    contactErr.style.display = none ? 'block' : 'none';
    if (none || emailBad || phoneBad) ok = false;
    return ok;
  }

  var status = document.getElementById('form-status');
  var btn = form.querySelector('button[type=submit]');
  var sending = false;

  function show(html, cls) {
    status.className = 'alert ' + cls;
    status.innerHTML = html;
    status.hidden = false;
    status.focus();
  }
  function ref() {
    var d = new Date();
    return 'EFS-' + d.getFullYear().toString().slice(2) +
      ('0' + (d.getMonth() + 1)).slice(-2) + ('0' + d.getDate()).slice(-2) + '-' +
      Math.random().toString(36).slice(2, 6).toUpperCase();
  }
  function summary(data, reference) {
    return [
      'Reference: ' + reference,
      'Name: ' + data.name,
      'Business: ' + data.business,
      'Email: ' + (data.email || '-'),
      'Phone: ' + (data.phone || '-'),
      'Service needed: ' + data.service,
      'Location: ' + (data.location || '-'),
      'Preferred contact: ' + (data.contact_method || '-'),
      'Timing: ' + (data.timing || '-'),
      '',
      'Main challenge:',
      data.challenge
    ].join('\n');
  }

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    if (sending) return;
    if (form.querySelector('.hp input').value) return; // spam trap
    if (!validate()) {
      show('Please check the highlighted fields.', 'alert-bad');
      var first = form.querySelector('.invalid input, .invalid select, .invalid textarea');
      if (first) first.focus();
      return;
    }
    var data = {};
    new FormData(form).forEach(function (v, k) { data[k] = String(v).trim(); });
    var reference = ref();
    data.reference = reference;

    if (!FORM_ENDPOINT) {
      var subject = 'Consultation request: ' + data.service + ' (' + data.business + ')';
      location.href = 'mailto:' + BUSINESS_EMAIL + '?subject=' + encodeURIComponent(subject) +
        '&body=' + encodeURIComponent(summary(data, reference));
      show('<strong>Your email app should now open with your request filled in.</strong> ' +
        'Please press <em>Send</em> there to complete it. Reference: <strong>' + reference + '</strong>.<br>' +
        'If nothing opened, email <a href="mailto:' + BUSINESS_EMAIL + '">' + BUSINESS_EMAIL + '</a>, ' +
        'call <a href="tel:+233244802816">0244 802 816</a> or ' +
        '<a href="https://wa.me/' + WHATSAPP_NUMBER + '" target="_blank" rel="noopener">chat on WhatsApp</a>.',
        'alert-ok');
      return;
    }

    sending = true; btn.disabled = true; btn.textContent = 'Sending…';
    fetch(FORM_ENDPOINT, {
      method: 'POST',
      headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' },
      body: JSON.stringify(data)
    }).then(function (r) {
      if (!r.ok) throw new Error('bad status');
      form.reset();
      form.hidden = true;
      show('<strong>Thank you. Your request has been received.</strong> Our team will contact you to discuss the next step.' +
        '<br>Your reference number is <strong>' + reference + '</strong>.', 'alert-ok');
      if (window.gtag) window.gtag('event', 'enquiry_submitted', { service: data.service });
    }).catch(function () {
      show('<strong>Sorry, your request could not be sent.</strong> Your details are still in the form, so you can try again. ' +
        'Or call <a href="tel:+233244802816">0244 802 816</a>, ' +
        '<a href="https://wa.me/' + WHATSAPP_NUMBER + '" target="_blank" rel="noopener">chat on WhatsApp</a> or email ' +
        '<a href="mailto:' + BUSINESS_EMAIL + '">' + BUSINESS_EMAIL + '</a>.', 'alert-bad');
    }).then(function () {
      sending = false; btn.disabled = false; btn.textContent = 'Send my request';
    });
  });
})();
