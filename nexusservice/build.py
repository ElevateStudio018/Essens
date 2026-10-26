#!/usr/bin/env python3
"""Genererar Nexus Service AB:s webbplats. Ändra text här och kör: python3 build.py"""
from html import escape
from pathlib import Path

ROOT = Path(__file__).parent

PHONE = "076-123 45 67"
PHONE_HREF = "tel:+46761234567"
EMAIL = "info@nexusserviceab.se"
AREA = "Stockholm med omnejd"
SLOGAN = "Vi får det att fungera. Hemma. På jobbet. Överallt."

LOGO = '<svg viewBox="0 0 100 100" aria-hidden="true"><path fill="#22272b" d="M0 100V0h30l32 46v38L28 36v64z"/><path fill="#d9600d" d="M100 0v100H70L38 54V16l34 48V0z"/></svg>'

# img = None betyder att tjänsten visas utan bild tills det finns ett eget foto
SERVICES = [
    dict(id="bygg", name="Bygg och reparation", img="bygg.jpg", alt="Byggarbetare på en byggarbetsplats",
         text=["Vi utför byggarbeten och reparationer i bostäder, lokaler och fastigheter. Det kan gälla allt från att laga en skada eller byta en dörr till att flytta en vägg eller bygga ett förråd.",
               "Vi kommer ut och tittar på vad som behöver göras innan vi lämnar en offert. Arbetet görs av våra egna hantverkare."],
         tasks=["Reparationer efter skador och slitage", "Nya eller flyttade innerväggar", "Byte av dörrar och fönster", "Förråd och skärmtak", "Åtgärder efter besiktning"],
         fit="Privatpersoner, företag och föreningar", avdrag="ROT-avdrag kan gälla för privatpersoner."),
    dict(id="snickeri", name="Snickeri", img="hero.jpg", alt="Snickare sågar till virke",
         text=["Vi gör allt inom snickeri, från mindre reparationer till större projekt. Golv, lister, foder, trappor, altaner och platsbyggd förvaring är vanliga uppdrag.",
               "Ska något byggas på plats får du ett förslag och ett pris innan vi börjar."],
         tasks=["Golvläggning och socklar", "Lister, foder och karmar", "Platsbyggd förvaring", "Altaner, trall och staket", "Trappor och räcken", "Köksmontering"],
         fit="Privatpersoner, företag och föreningar", avdrag="ROT-avdrag kan gälla för privatpersoner."),
    dict(id="renovering", name="Renovering", img="badrum.jpg", alt="Nyrenoverat badrum med duschvägg",
         text=["Vi renoverar kök, badrum, hela bostäder och lokaler. Eftersom vi har rivning, bygg, snickeri och måleri i samma företag behöver du inte samordna flera olika hantverkare.",
               "Innan vi börjar får du en tidplan, och under arbetet har du en kontaktperson hos oss."],
         tasks=["Köksrenovering", "Badrumsrenovering", "Renovering av hela bostäder", "Anpassning av lokaler", "Nya ytskikt"],
         fit="Privatpersoner, företag och föreningar", avdrag="ROT-avdrag kan gälla för privatpersoner."),
    dict(id="tak", name="Takarbeten", img=None,
         text=["Vi lagar läckage, byter skadade takpannor och plåtdetaljer och ser över hängrännor och stuprör. Vi börjar med att gå igenom taket och berättar vad som behöver göras nu och vad som kan vänta."],
         tasks=["Lagning av läckage", "Byte av takpannor och plåt", "Hängrännor och stuprör", "Översyn inför vintern"],
         fit="Privatpersoner, företag och föreningar", avdrag="ROT-avdrag kan gälla för privatpersoner."),
    dict(id="rivning", name="Rivning", img="isolering.jpg", alt="Öppnad vägg under renovering",
         text=["Vi river väggar, kök, badrum och andra utrymmen på ett säkert och effektivt sätt. Golv och ytor som ska vara kvar skyddas, och vi sorterar och kör bort rivningsmaterialet."],
         tasks=["Rivning av kök och badrum", "Rivning av innerväggar", "Golv och undergolv", "Utrensning av lokaler", "Bortforsling"],
         fit="Privatpersoner, företag och föreningar", avdrag="ROT-avdrag kan gälla för privatpersoner."),
    dict(id="maleri", name="Måleri", img="mal-roller.jpg", alt="Målarroller mot en vägg",
         text=["Vi målar invändigt och utvändigt med fokus på kvalitet och finish. Det mesta av resultatet avgörs av förarbetet, så vi spacklar, slipar och grundar ordentligt innan vi målar.",
               "Vi täcker möbler och golv och städar efter oss varje dag."],
         tasks=["Väggar och tak", "Dörrar, fönster och snickerier", "Fasader", "Trapphus", "Tapetsering"],
         fit="Privatpersoner, företag och föreningar", avdrag="ROT-avdrag kan gälla för privatpersoner."),
    dict(id="fastighetsskotsel", name="Fastighetsskötsel", img="fastighet.jpg", alt="Flerbostadshus med balkonger",
         text=["Vi sköter fastigheter, trapphus och gemensamma utrymmen löpande. Vid varje besök går vi igenom fastigheten, åtgärdar det som ingår i avtalet och meddelar er om sådant som behöver planeras."],
         tasks=["Tillsyn och rondering", "Trapphus och entréer", "Tvättstugor och gemensamma utrymmen", "Byte av belysning", "Mindre reparationer"],
         fit="Bostadsrättsföreningar, fastighetsägare och företag", avdrag="Löpande avtal eller enstaka uppdrag."),
    dict(id="underhall", name="Underhåll av fastigheter", img=None,
         text=["Vi utför invändigt och utvändigt underhåll, till exempel punkter i föreningens underhållsplan. Fasader, fönster, entréer, förråd och soprum är vanliga uppdrag. Vi kan också hjälpa till att prioritera när allt inte ryms i årets budget."],
         tasks=["Fasader och fönster", "Entréer och dörrar", "Förråd, soprum och cykelrum", "Staket och plank", "Åtgärder enligt underhållsplan"],
         fit="Bostadsrättsföreningar, fastighetsägare och företag", avdrag="Fast pris eller löpande räkning."),
    dict(id="utemiljo", name="Gräsklippning, häckar och trädgård", img="tradgard.jpg", alt="Trädgårdsspade i planteringsjord",
         text=["Vi klipper gräs regelbundet under säsongen, trimmar häckar och buskar och tar hand om planteringar. På hösten hämtar vi löv och städar inför vintern."],
         tasks=["Gräsklippning", "Häcktrimning och beskärning", "Plantering och rensning", "Lövhämtning", "Vårstädning"],
         fit="Privatpersoner, företag och föreningar", avdrag="RUT-avdrag kan gälla för privatpersoner."),
    dict(id="snorojning", name="Snöröjning och halkbekämpning", img="sno.jpg", alt="Snötäckt gata med lyktstolpar",
         text=["Vi skottar och sandar entréer, gångar och parkeringar så att de går att använda även när det har snöat. Avtal tecknas inför säsongen, så att det är klart vem som ansvarar när snön kommer."],
         tasks=["Snöskottning av entréer och gångar", "Plogning", "Sandning och saltning", "Takskottning"],
         fit="Privatpersoner, företag och föreningar", avdrag="RUT-avdrag kan gälla för privatpersoner."),
]

VALUES = [
    ("Kvalitet", "Vi kompromissar aldrig med kvalitet."),
    ("Pålitlighet", "Vi håller vad vi lovar, varje gång."),
    ("Flexibilitet", "Vi anpassar oss efter dina behov."),
    ("Lokalt och engagerat", "Vi bryr oss om våra kunder och vår miljö."),
]



def header(active):
    menu = "".join(f'<a href="tjanster.html#{s["id"]}">{s["name"]}</a>' for s in SERVICES)
    cur = lambda k: ' aria-current="page"' if k == active else ''
    return f'''<a class="skip" href="#main">Till innehållet</a>
<div class="topbar"><div class="wrap">
  <span class="hide-s muted">{AREA}</span>
  <a href="{PHONE_HREF}">{PHONE}</a>
  <a href="mailto:{EMAIL}">{EMAIL}</a>
  <a href="kontakt.html">Kontakt</a>
</div></div>
<header class="header"><div class="wrap">
  <a class="logo" href="index.html" aria-label="Nexus Service AB, till startsidan">{LOGO}<span><b>NEXUS</b><small>SERVICE AB</small></span></a>
  <button class="menu-btn" id="menuBtn" type="button" aria-expanded="false" aria-controls="nav">Meny</button>
  <nav class="nav" id="nav" aria-label="Huvudmeny">
    <div class="dd"><button type="button" aria-expanded="false"{' class="current"' if active == "tjanster" else ''}>Tjänster</button>
      <div class="dd-menu">{menu}<a class="all" href="tjanster.html">Alla tjänster</a></div></div>
    <a href="tjanster.html"{cur("privat")}>Privatperson</a>
    <a href="om.html#foretag"{cur("foretag")}>Företag</a>
    <a href="fastighet.html"{cur("brf")}>BRF och fastighetsägare</a>
    <a href="om.html"{cur("om")}>Om oss</a>
    <a class="btn nav-cta" href="kontakt.html">Begär offert</a>
  </nav>
  <a class="btn cta" href="kontakt.html">Begär offert</a>
</div></header>'''


def contact_box():
    return f'''<section class="section"><div class="wrap">
  <div class="contact-box">
    <div>
      <h2>Kontakta oss för en kostnadsfri offert</h2>
      <p>Berätta vad du behöver hjälp med, så återkommer vi med ett pris och ett förslag på när vi kan börja.</p>
    </div>
    <div class="lines">
      <a href="{PHONE_HREF}">{PHONE}</a><br>
      <a href="mailto:{EMAIL}">{EMAIL}</a><br>
      <a class="btn" href="kontakt.html">Skicka en förfrågan</a>
    </div>
  </div>
</div></section>'''


def footer():
    half = len(SERVICES) // 2
    col = lambda items: "".join(f'<li><a href="tjanster.html#{s["id"]}">{s["name"]}</a></li>' for s in items)
    return f'''<footer class="footer">
  <div class="wrap cols">
    <div>
      <a class="logo" href="index.html" aria-label="Nexus Service AB">{LOGO}<span><b>NEXUS</b><small>SERVICE AB</small></span></a>
      <p>Bygg, renovering och fastighetsservice i {AREA}.</p>
      <ul><li><a href="{PHONE_HREF}">{PHONE}</a></li><li><a href="mailto:{EMAIL}">{EMAIL}</a></li></ul>
    </div>
    <div><h2>Tjänster</h2><ul>{col(SERVICES[:half])}</ul></div>
    <div><h2>&nbsp;</h2><ul>{col(SERVICES[half:])}</ul></div>
    <div><h2>Nexus Service</h2><ul>
      <li><a href="om.html">Om oss</a></li>
      <li><a href="fastighet.html">För bostadsrättsföreningar</a></li>
      <li><a href="om.html#foretag">För företag</a></li>
      <li><a href="kontakt.html">Kontakt och offert</a></li>
    </ul></div>
  </div>
  <div class="wrap bottom"><span>© 2026 Nexus Service AB</span><span>{SLOGAN}</span></div>
</footer>'''


def page(filename, title, desc, body, active=None):
    html = f'''<!DOCTYPE html>
<html lang="sv">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)}</title>
<meta name="description" content="{escape(desc)}">
<link rel="icon" href="img/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Source+Sans+3:wght@400;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
{header(active)}
<main id="main">
{body}
</main>
{footer()}
<script src="assets/app.js"></script>
</body>
</html>
'''
    (ROOT / filename).write_text(html, encoding="utf-8")


def page_top(crumb, h1, text):
    return f'''<div class="page-top"><div class="wrap">
  <div class="crumbs"><a href="index.html">Start</a> / {crumb}</div>
  <h1>{h1}</h1>
  <p>{text}</p>
</div></div>'''


def build_index():
    acc = "".join(
        f'<details><summary>{s["name"]}</summary><div class="acc-body"><p>{s["text"][0]}</p>'
        f'<a class="more" href="tjanster.html#{s["id"]}">Läs mer om {s["name"].lower()}</a></div></details>'
        for s in SERVICES)
    body = f'''<section class="intro"><div class="wrap">
  <div>
    <p class="slogan">{SLOGAN}</p>
    <h1>Bygg, renovering och fastighetsservice i Stockholm</h1>
    <p>Nexus Service hjälper privatpersoner, företag, fastighetsägare och bostadsrättsföreningar med både mindre och större projekt, från löpande underhåll till kompletta renoveringar.</p>
    <div class="btns">
      <a class="btn" href="kontakt.html">Begär kostnadsfri offert</a>
      <a class="btn btn-outline" href="{PHONE_HREF}">Ring {PHONE}</a>
    </div>
  </div>
  <img src="img/hero.jpg" alt="Snickare sågar till virke" width="2000" height="1333" fetchpriority="high">
</div></section>

<section class="section"><div class="wrap">
  <div class="section-title"><h2>Vad kan vi hjälpa dig med?</h2></div>
  <div class="entries">
    <a class="entry" href="tjanster.html#renovering"><img src="img/kok.jpg" alt="Renoverat kök" loading="lazy">
      <div><h3>Ska du renovera?</h3><p>Kök, badrum eller hela bostaden. Vi river, bygger, snickrar och målar.</p></div></a>
    <a class="entry" href="tjanster.html#maleri"><img src="img/mal-roller.jpg" alt="Målarroller mot en vägg" loading="lazy">
      <div><h3>Behöver något målas?</h3><p>Väggar, tak, snickerier och fasader, invändigt och utvändigt.</p></div></a>
    <a class="entry" href="fastighet.html"><img src="img/fastighet2.jpg" alt="Flerbostadshus" loading="lazy">
      <div><h3>Sitter du i en styrelse?</h3><p>Skötsel, underhåll, utemiljö och snöröjning för föreningar och fastighetsägare.</p></div></a>
    <a class="entry" href="tjanster.html#utemiljo"><img src="img/grasmatta.jpg" alt="Nyklippt gräsmatta" loading="lazy">
      <div><h3>Ska gården skötas?</h3><p>Gräsklippning och häckar på sommaren, snöröjning på vintern.</p></div></a>
  </div>
</div></section>

<section class="section alt"><div class="wrap split">
  <div>
    <h2>Våra tjänster</h2>
    <p>Vi har flera yrken i samma företag. Därför kan vi ta både små jobb och projekt där flera moment hänger ihop, till exempel när ett badrum ska rivas, byggas om och målas.</p>
    <p><a class="more" href="tjanster.html">Se alla tjänster</a></p>
    <img src="img/verktyg.jpg" alt="Verktyg i en verktygsvägg" loading="lazy">
  </div>
  <div class="acc">{acc}</div>
</div></section>

<section class="section"><div class="wrap media">
  <img src="img/fastighet.jpg" alt="Flerbostadshus med balkonger" loading="lazy">
  <div>
    <h2>För bostadsrättsföreningar och fastighetsägare</h2>
    <p>Många föreningar har en leverantör för trapphusen, en för trädgården, en för snön och flera till för reparationer. Vi kan ta hand om det mesta i ett och samma avtal, med en kontaktperson som känner fastigheten.</p>
    <ul>
      <li>Löpande skötsel av trapphus och gemensamma utrymmen</li>
      <li>Gräsklippning, häckar och lövhämtning</li>
      <li>Snöröjning och halkbekämpning</li>
      <li>Reparationer och planerat underhåll</li>
    </ul>
    <a class="more" href="fastighet.html">Läs mer om fastighetsservice</a>
  </div>
</div></section>

<section class="section alt"><div class="wrap media flip">
  <img src="img/planering.jpg" alt="Ritningar på ett bord" loading="lazy">
  <div>
    <h2>Om Nexus Service</h2>
    <p>Vi erbjuder tjänster inom bygg, reparation, renovering och fastighetsskötsel. Med fokus på kvalitet, noggrannhet och ett professionellt utfört arbete försöker vi alltid hitta rätt lösning för varje kund och projekt.</p>
    <p>Vi tar hand om ditt bygg- och fastighetsprojekt från idé till färdigt resultat.</p>
    <a class="more" href="om.html">Mer om oss</a>
  </div>
</div></section>

{contact_box()}'''
    page("index.html", "Nexus Service AB | Bygg, renovering och fastighetsservice i Stockholm",
         "Nexus Service utför bygg, reparation, renovering, måleri, takarbeten och fastighetsskötsel för privatpersoner, företag och bostadsrättsföreningar i Stockholm. Kostnadsfri offert.",
         body)


def build_services():
    side = "".join(f'<li><a href="#{s["id"]}">{s["name"]}</a></li>' for s in SERVICES)
    secs = []
    for s in SERVICES:
        img = f'<img src="img/{s["img"]}" alt="{escape(s["alt"])}" loading="lazy">' if s["img"] else ""
        text = "".join(f"<p>{t}</p>" for t in s["text"])
        tasks = "".join(f"<li>{t}</li>" for t in s["tasks"])
        secs.append(f'''<section class="service" id="{s["id"]}">
    <h2>{s["name"]}</h2>
    {img}
    <div class="cols">
      <div>{text}<h3>Exempel på uppdrag</h3><ul>{tasks}</ul></div>
      <div class="box">
        <h3>Passar för</h3><p>{s["fit"]}</p>
        <h3>Avdrag och avtal</h3><p>{s["avdrag"]}</p>
        <h3>Offert</h3><p>Kostnadsfri. Vi tittar gärna på plats först.</p>
        <a class="btn" href="kontakt.html?tjanst={s["id"]}">Begär offert</a>
      </div>
    </div>
  </section>''')
    body = page_top("Tjänster", "Tjänster",
                    "Bygg, renovering, underhåll och fastighetsservice. Du kan anlita oss för en enskild tjänst eller kombinera flera i samma uppdrag.") + f'''
<div class="section"><div class="wrap layout">
  <nav class="side" aria-label="Tjänster"><h2>På den här sidan</h2><ul>{side}</ul></nav>
  <div>{"".join(secs)}</div>
</div></div>
{contact_box()}'''
    page("tjanster.html", "Tjänster | Nexus Service AB",
         "Bygg och reparation, snickeri, renovering, takarbeten, rivning, måleri, fastighetsskötsel, underhåll, trädgård och snöröjning i Stockholm.",
         body, "tjanster")


def build_property():
    body = page_top("Bostadsrättsföreningar och fastighetsägare", "Fastighetsservice för föreningar och fastighetsägare",
                    "Löpande skötsel, underhåll, utemiljö och snöröjning med en kontaktperson för hela fastigheten.") + f'''
<section class="section"><div class="wrap media">
  <div>
    <h2>Det här kan vi ta hand om</h2>
    <p>Vi går igenom fastigheten tillsammans med styrelsen eller förvaltaren och kommer överens om vad som ska göras, hur ofta och till vilket pris. Det som upptäcks vid våra besök och som ingår i avtalet åtgärdar vi direkt. Annat rapporterar vi till er med ett förslag.</p>
    <ul>
      <li>Tillsyn och rondering</li>
      <li>Skötsel av trapphus, entréer, tvättstugor och andra gemensamma utrymmen</li>
      <li>Gräsklippning, häckar, planteringar och lövhämtning</li>
      <li>Snöröjning, halkbekämpning och takskottning</li>
      <li>Reparationer, måleri och snickeri</li>
      <li>Planerat underhåll av fasader, fönster, tak och förråd</li>
    </ul>
  </div>
  <img src="img/fastighet2.jpg" alt="Flerbostadshus med balkonger" loading="lazy">
</div></section>

<section class="section alt"><div class="wrap">
  <div class="section-title">
    <h2>Exempel på ett år</h2>
    <p>Så här kan arbetet fördelas över året. Innehållet bestäms utifrån er fastighet och ert avtal.</p>
  </div>
  <div class="table-wrap"><table class="plan">
    <thead><tr><th>Period</th><th>Utemiljö</th><th>Fastighet</th><th>Vinter</th></tr></thead>
    <tbody>
      <tr><th>Januari–mars</th><td>–</td><td>Tillsyn, genomgång av underhållsplanen</td><td>Snöröjning, halkbekämpning, takskottning</td></tr>
      <tr><th>April–maj</th><td>Sandupptagning, vårstädning, plantering, första gräsklippningen</td><td>Översyn av tak, hängrännor och fasad</td><td>–</td></tr>
      <tr><th>Juni–augusti</th><td>Gräsklippning, häcktrimning</td><td>Utvändigt måleri och underhåll</td><td>–</td></tr>
      <tr><th>September–november</th><td>Beskärning, lövhämtning, höststädning</td><td>Rensning av hängrännor, invändigt underhåll</td><td>Förberedelser inför vintern</td></tr>
      <tr><th>December</th><td>–</td><td>Tillsyn</td><td>Snöröjning, halkbekämpning</td></tr>
    </tbody>
  </table></div>
</div></section>

<section class="section"><div class="wrap split">
  <div>
    <h2>Olika sätt att anlita oss</h2>
    <h3>Löpande avtal</h3>
    <p>Återkommande skötsel och tillsyn med en bestämd omfattning och ett fast pris per månad.</p>
    <h3>Säsongsavtal</h3>
    <p>Utemiljön på sommaren och snöröjningen på vintern, med överenskommen prioritering av ytor.</p>
    <h3>Enskilda uppdrag</h3>
    <p>Reparationer och projekt ur underhållsplanen, till fast pris eller på löpande räkning.</p>
  </div>
  <img src="img/sno.jpg" alt="Snötäckt gata" loading="lazy">
</div></section>

{contact_box()}'''
    page("fastighet.html", "Fastighetsservice för BRF och fastighetsägare | Nexus Service AB",
         "Fastighetsskötsel, underhåll, utemiljö och snöröjning för bostadsrättsföreningar och fastighetsägare i Stockholm.",
         body, "brf")


def build_about():
    values = "".join(f"<div><dt>{t}</dt><dd>{d}</dd></div>" for t, d in VALUES)
    body = page_top("Om oss", "Om Nexus Service",
                    "Vi tar hand om ditt bygg- och fastighetsprojekt från idé till färdigt resultat.") + f'''
<section class="section"><div class="wrap media">
  <div>
    <h2>Det här gör vi</h2>
    <p>Nexus Service erbjuder professionella tjänster inom bygg, reparation, renovering och fastighetsskötsel. Vi hjälper privatpersoner, företag, fastighetsägare och bostadsrättsföreningar med både mindre och större projekt, från löpande underhåll till kompletta renoveringar.</p>
    <p>Våra tjänster omfattar bland annat bygg- och reparationsarbeten, snickeri, takarbeten, rivning, målning, renovering samt invändigt och utvändigt underhåll av fastigheter. Vi sköter också gräsmattor, häckar och trädgårdar och röjer snö på vintern.</p>
    <p>Med fokus på kvalitet, noggrannhet och ett professionellt utfört arbete försöker vi alltid hitta rätt lösning för varje kund och projekt.</p>
  </div>
  <img src="img/stockholm.jpg" alt="Riddarholmen i Stockholm" loading="lazy">
</div></section>

<section class="section alt" id="foretag"><div class="wrap split">
  <div>
    <h2>Vem vi arbetar för</h2>
    <h3>Privatpersoner</h3>
    <p>Renovering, reparationer, måleri och trädgård i villa, radhus och lägenhet.</p>
    <h3>Företag</h3>
    <p>Anpassning och reparation av lokaler och löpande service, planerat så att verksamheten kan fortsätta som vanligt.</p>
    <h3>Fastighetsägare och bostadsrättsföreningar</h3>
    <p>Skötsel och underhåll av fastigheter, gemensamma utrymmen och utemiljöer. <a href="fastighet.html">Läs mer</a></p>
  </div>
  <div>
    <h2>Så går det till</h2>
    <ol class="steps">
      <li>Du kontaktar oss per telefon, mejl eller via formuläret och berättar vad som behöver göras.</li>
      <li>Vi kommer ut och tittar på plats om det behövs.</li>
      <li>Du får en kostnadsfri offert med pris och tidplan.</li>
      <li>Vi utför arbetet. Du har en kontaktperson hos oss hela vägen.</li>
      <li>Vi går igenom resultatet tillsammans och städar efter oss.</li>
    </ol>
  </div>
</div></section>

<section class="section"><div class="wrap">
  <div class="section-title"><h2>Det här står vi för</h2></div>
  <dl class="values">{values}</dl>
</div></section>

{contact_box()}'''
    page("om.html", "Om oss | Nexus Service AB",
         "Nexus Service hjälper privatpersoner, företag, fastighetsägare och bostadsrättsföreningar i Stockholm med bygg, renovering och fastighetsskötsel.",
         body, "om")


def build_contact():
    checks = "".join(f'<label><input type="checkbox" name="tjanst" value="{s["id"]}"> {s["name"]}</label>' for s in SERVICES)
    faq = [
        ("Kostar offerten något?", "Nej, offerten är kostnadsfri."),
        ("Kan jag göra ROT- eller RUT-avdrag?", "Som privatperson kan du ofta göra ROT-avdrag på arbetskostnaden för bygg, renovering och måleri, och RUT-avdrag för trädgårdsarbete och snöskottning. I offerten står det vad som gäller för ditt uppdrag."),
        ("Var arbetar ni?", f"I {AREA}. Hör av dig om du är osäker på om vi kommer till din adress."),
        ("Tar ni små jobb också?", "Ja. Vi tar både mindre reparationer och större projekt."),
    ]
    faq_html = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faq)
    body = page_top("Kontakt", "Kontakt och offert",
                    "Ring, mejla eller fyll i formuläret så återkommer vi med en kostnadsfri offert.") + f'''
<section class="section"><div class="wrap contact-grid">
  <div>
    <ul class="contact-list">
      <li><span>Telefon</span><a href="{PHONE_HREF}">{PHONE}</a></li>
      <li><span>E-post</span><a href="mailto:{EMAIL}">{EMAIL}</a></li>
      <li><span>Webb</span>www.nexusserviceab.se</li>
      <li><span>Område</span>{AREA}</li>
    </ul>
    <h2>Vanliga frågor</h2>
    <div class="faq">{faq_html}</div>
  </div>
  <form class="form" id="offertForm" novalidate>
    <h2>Begär offert</h2>
    <fieldset><legend>Jag är</legend><div class="opts">
      <label><input type="radio" name="kund" value="privat" checked> Privatperson</label>
      <label><input type="radio" name="kund" value="foretag"> Företag</label>
      <label><input type="radio" name="kund" value="brf"> Bostadsrättsförening eller fastighetsägare</label>
    </div></fieldset>
    <fieldset><legend>Det gäller</legend><div class="opts">{checks}</div></fieldset>
    <div class="fields">
      <div class="field"><label for="namn">Namn</label><input id="namn" name="namn" autocomplete="name" required></div>
      <div class="field"><label for="foretag">Företag eller förening (valfritt)</label><input id="foretag" name="foretag" autocomplete="organization"></div>
      <div class="field"><label for="telefon">Telefon</label><input id="telefon" name="telefon" type="tel" autocomplete="tel" required></div>
      <div class="field"><label for="epost">E-post</label><input id="epost" name="epost" type="email" autocomplete="email" required></div>
      <div class="field"><label for="adress">Adress (valfritt)</label><input id="adress" name="adress" autocomplete="street-address"></div>
      <div class="field"><label for="start">När vill du att vi börjar?</label>
        <select id="start" name="start"><option value="">Välj</option><option>Så snart som möjligt</option><option>Inom en månad</option><option>Inom tre månader</option><option>Längre fram</option><option>Löpande avtal</option></select></div>
      <div class="field full"><label for="beskrivning">Beskriv vad som ska göras</label><textarea id="beskrivning" name="beskrivning" required></textarea></div>
    </div>
    <div class="form-actions"><button class="btn" type="submit">Skicka förfrågan</button></div>
    <p class="form-note">När du skickar öppnas ditt e-postprogram med förfrågan ifylld till {EMAIL}.</p>
    <p class="form-status" id="formStatus" role="status"></p>
  </form>
</div></section>'''
    page("kontakt.html", "Kontakt och offert | Nexus Service AB",
         "Begär en kostnadsfri offert på bygg, renovering eller fastighetsservice i Stockholm. Ring 076-123 45 67 eller mejla info@nexusserviceab.se.",
         body, "kontakt")


if __name__ == "__main__":
    build_index()
    build_services()
    build_property()
    build_about()
    build_contact()
    print("Klart")
