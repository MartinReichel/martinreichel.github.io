/* ============================================================
   Martin Reichel – osobní web  |  main.js
   ============================================================ */
(function () {
    'use strict';

    /* Mobilní navigace */
    var toggle   = document.getElementById('nav-toggle');
    var navLinks = document.getElementById('nav-links');

    toggle.addEventListener('click', function () {
        navLinks.classList.toggle('open');
    });
    navLinks.querySelectorAll('a').forEach(function (a) {
        a.addEventListener('click', function () { navLinks.classList.remove('open'); });
    });

    /* Scroll reveal */
    var revealEls = document.querySelectorAll('.reveal');

    function checkReveal() {
        var wh = window.innerHeight;
        revealEls.forEach(function (el) {
            if (el.getBoundingClientRect().top < wh - 40) {
                el.classList.add('visible');
            }
        });
    }

    window.addEventListener('scroll', checkReveal, { passive: true });
    window.addEventListener('resize', checkReveal, { passive: true });
    window.addEventListener('load',   checkReveal);
    setTimeout(checkReveal, 50);

    /* Aktivní odkaz v navigaci */
    var sections = document.querySelectorAll('section[id]');
    var navItems = document.querySelectorAll('.nav__links a');

    window.addEventListener('scroll', function () {
        var current = '';
        sections.forEach(function (s) {
            if (window.scrollY >= s.offsetTop - 90) current = s.id;
        });
        navItems.forEach(function (a) {
            a.classList.toggle('active', a.getAttribute('href') === '#' + current);
        });
    }, { passive: true });

})();
