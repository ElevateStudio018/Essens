// Vittoria Städ AB
(function () {
  "use strict";
  // PLATSHÅLLARE: byt till företagets riktiga e-postadress.
  var CONTACT_EMAIL = "info@vittoriastad.se";

  // Herovideo: stå still om besökaren vill ha mindre rörelse
  var heroVideo = document.getElementById("heroVideo");
  if (heroVideo && window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
    heroVideo.removeAttribute("autoplay");
    heroVideo.pause();
  }

  // Header: vit bakgrund vid scroll
  var header = document.getElementById("header");
  function onScroll() { header.classList.toggle("is-scrolled", window.scrollY > 20); }
  onScroll();
  window.addEventListener("scroll", onScroll, { passive: true });

  // Mobilmeny
  var toggle = document.getElementById("navToggle");
  var menu = document.getElementById("mobileMenu");
  function setMenu(open) {
    header.classList.toggle("is-open", open);
    menu.hidden = !open;
    toggle.setAttribute("aria-expanded", String(open));
    toggle.setAttribute("aria-label", open ? "Stäng meny" : "Öppna meny");
  }
  toggle.addEventListener("click", function () { setMenu(menu.hidden); });
  menu.addEventListener("click", function (e) { if (e.target.closest("a")) setMenu(false); });
  document.addEventListener("keydown", function (e) { if (e.key === "Escape") setMenu(false); });
  window.addEventListener("resize", function () { if (window.innerWidth > 860) setMenu(false); });

  // Förval av tjänst i formuläret
  var select = document.getElementById("tjanst");
  document.querySelectorAll("[data-service]").forEach(function (el) {
    el.addEventListener("click", function () { select.value = el.getAttribute("data-service"); });
  });

  // Kontaktformulär – öppnar besökarens e-postprogram med förfrågan ifylld
  var form = document.getElementById("form");
  var msg = document.getElementById("formMsg");
  form.addEventListener("submit", function (e) {
    e.preventDefault();
    var ok = true;
    form.querySelectorAll("[required]").forEach(function (f) {
      var bad = f.type === "checkbox" ? !f.checked : !f.value.trim() || (f.type === "email" && !/^\S+@\S+\.\S+$/.test(f.value));
      (f.type === "checkbox" ? f.parentNode : f).classList.toggle("is-invalid", bad);
      if (bad) ok = false;
    });
    if (!ok) {
      msg.textContent = "Fyll i de obligatoriska fälten (*) och godkänn villkoren.";
      msg.classList.add("is-error");
      return;
    }
    var d = new FormData(form);
    var subject = "Förfrågan: " + d.get("tjanst") + " – " + d.get("namn");
    var body = [
      "Namn: " + d.get("namn"),
      "E-post: " + d.get("epost"),
      "Företag: " + (d.get("foretag") || "-"),
      "Telefon: " + (d.get("telefon") || "-"),
      "Tjänst: " + d.get("tjanst"),
      "",
      d.get("meddelande")
    ].join("\n");
    window.location.href = "mailto:" + CONTACT_EMAIL + "?subject=" + encodeURIComponent(subject) + "&body=" + encodeURIComponent(body);
    msg.classList.remove("is-error");
    msg.textContent = "Tack! Ditt e-postprogram öppnas med förfrågan ifylld – tryck på skicka så återkommer vi inom en arbetsdag.";
  });
  form.addEventListener("input", function (e) {
    var t = e.target;
    (t.type === "checkbox" ? t.parentNode : t).classList.remove("is-invalid");
  });

  var y = document.getElementById("year");
  if (y) y.textContent = new Date().getFullYear();
})();
