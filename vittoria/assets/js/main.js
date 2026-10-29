// Vittoria Städ AB
(function () {
  "use strict";
  // PLATSHÅLLARE: byt till företagets riktiga e-postadress.
  var CONTACT_EMAIL = "info@vittoriastad.se";

  var doc = document.documentElement;
  doc.classList.add("js");

  // Hero-variant (förhandsgranskning): ?hero=1–5
  var hero = document.getElementById("hero");
  var heroParam = new URLSearchParams(window.location.search).get("hero");
  if (hero && /^[1-5]$/.test(heroParam || "")) hero.className = "hero hero--v" + heroParam;

  // Herovideo: stå still om besökaren vill ha mindre rörelse
  var heroVideo = document.getElementById("heroVideo");
  if (heroVideo && window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
    heroVideo.removeAttribute("autoplay");
    heroVideo.pause();
  }

  // Header bakgrund vid scroll
  var header = document.querySelector(".header");
  function onScroll() { header.classList.toggle("is-scrolled", window.scrollY > 30); }
  onScroll();
  window.addEventListener("scroll", onScroll, { passive: true });

  // Mobilmeny
  var burger = document.getElementById("burger");
  var nav = document.getElementById("nav");
  function setNav(open) {
    document.body.classList.toggle("nav-open", open);
    header.classList.toggle("nav-shown", open);
    burger.setAttribute("aria-expanded", String(open));
    burger.setAttribute("aria-label", open ? "Stäng meny" : "Öppna meny");
  }
  burger.addEventListener("click", function () { setNav(!document.body.classList.contains("nav-open")); });
  nav.addEventListener("click", function (e) { if (e.target.closest("a")) setNav(false); });
  document.addEventListener("keydown", function (e) { if (e.key === "Escape") setNav(false); });
  window.addEventListener("resize", function () { if (window.innerWidth > 960) setNav(false); });

  // Aktiv menylänk
  var links = Array.prototype.slice.call(nav.querySelectorAll('a[href^="#"]'));
  var sections = links.map(function (a) { return document.querySelector(a.getAttribute("href")); });
  if ("IntersectionObserver" in window) {
    var spy = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        links.forEach(function (a, i) { a.classList.toggle("is-active", sections[i] === en.target); });
      });
    }, { rootMargin: "-45% 0px -50% 0px" });
    sections.forEach(function (s) { if (s) spy.observe(s); });
  }

  // Animationer vid scroll
  var reveals = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add("is-in"); io.unobserve(en.target); }
      });
    }, { threshold: 0.12, rootMargin: "0px 0px -40px 0px" });
    reveals.forEach(function (el, i) {
      el.style.transitionDelay = (i % 4) * 70 + "ms";
      io.observe(el);
    });
  } else {
    reveals.forEach(function (el) { el.classList.add("is-in"); });
  }

  // Förval av tjänst i formuläret
  var select = document.getElementById("tjanst");
  document.querySelectorAll("[data-service]").forEach(function (el) {
    el.addEventListener("click", function () { select.value = el.getAttribute("data-service"); });
  });

  // Offertkortet i hero skickar vidare till kontaktformuläret
  var heroQuote = document.getElementById("heroQuote");
  if (heroQuote) heroQuote.addEventListener("submit", function (e) {
    e.preventDefault();
    var d = new FormData(heroQuote);
    ["namn", "epost", "tjanst"].forEach(function (k) {
      var f = form.querySelector('[name="' + k + '"]');
      if (f && d.get(k)) f.value = d.get(k);
    });
    document.getElementById("kontakt").scrollIntoView({ behavior: "smooth" });
    setTimeout(function () { form.querySelector('[name="meddelande"]').focus({ preventScroll: true }); }, 700);
  });

  // Omdömen
  var slider = document.getElementById("slider");
  if (slider) {
    var slides = slider.querySelectorAll(".slide");
    var dots = slider.querySelector(".dots");
    var current = 0, timer;
    slides.forEach(function (_, i) {
      var b = document.createElement("button");
      b.setAttribute("role", "tab");
      b.setAttribute("aria-label", "Omdöme " + (i + 1));
      b.addEventListener("click", function () { go(i); restart(); });
      dots.appendChild(b);
    });
    function go(i) {
      current = (i + slides.length) % slides.length;
      slides.forEach(function (s, j) { s.classList.toggle("is-active", j === current); });
      dots.querySelectorAll("button").forEach(function (b, j) { b.setAttribute("aria-selected", String(j === current)); });
    }
    function restart() { clearInterval(timer); timer = setInterval(function () { go(current + 1); }, 7000); }
    slider.querySelectorAll(".round").forEach(function (b) {
      b.addEventListener("click", function () { go(current + Number(b.getAttribute("data-dir"))); restart(); });
    });
    go(0); restart();
  }

  // Kontaktformulär – öppnar besökarens e-postprogram med förfrågan ifylld
  var form = document.getElementById("form");
  var msg = document.getElementById("formMsg");
  form.addEventListener("submit", function (e) {
    e.preventDefault();
    var ok = true;
    form.querySelectorAll("[required]").forEach(function (f) {
      var bad = f.type === "checkbox" ? !f.checked : !f.value.trim() || (f.type === "email" && !/^\S+@\S+\.\S+$/.test(f.value));
      f.classList.toggle("is-invalid", bad);
      if (bad) ok = false;
    });
    if (!ok) {
      msg.textContent = "Fyll i de obligatoriska fälten (*) och godkänn villkoren.";
      msg.classList.add("is-error");
      return;
    }
    var d = new FormData(form);
    var subject = "Förfrågan" + (d.get("tjanst") ? ": " + d.get("tjanst") : "") + " – " + d.get("namn");
    var body = [
      "Namn: " + d.get("namn"),
      "E-post: " + d.get("epost"),
      "Företag: " + (d.get("foretag") || "-"),
      "Telefon: " + (d.get("telefon") || "-"),
      "Tjänst: " + (d.get("tjanst") || "-"),
      "",
      d.get("meddelande")
    ].join("\n");
    window.location.href = "mailto:" + CONTACT_EMAIL + "?subject=" + encodeURIComponent(subject) + "&body=" + encodeURIComponent(body);
    msg.classList.remove("is-error");
    msg.textContent = "Tack! Ditt e-postprogram öppnas med förfrågan ifylld – tryck på skicka så återkommer vi inom en arbetsdag.";
  });
  form.addEventListener("input", function (e) { e.target.classList.remove("is-invalid"); });

  var y = document.getElementById("year");
  if (y) y.textContent = new Date().getFullYear();
})();
