#!/usr/bin/env python3
"""Genererar Nexus Service AB:s webbplats. Ändra text här och kör: python3 build.py"""
from html import escape
from pathlib import Path

ROOT = Path(__file__).parent

PHONE = "076-123 45 67"
PHONE_HREF = "tel:+46761234567"
EMAIL = "info@nexusserviceab.se"
AREA = "Stockholm med omnejd"

ARR = '<svg class="arr" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M4 12h15M13 6l6 6-6 6"/></svg>'
CHEV = '<svg class="chev" viewBox="0 0 10 10" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M1 3l4 4 4-4"/></svg>'
LOGO = '<svg viewBox="0 0 100 100" aria-hidden="true"><path fill="#111416" d="M0 100V0h30l32 46v38L28 36v64z"/><path fill="#E2620B" d="M100 0v100H70L38 54V16l34 48V0z"/></svg>'

GROUPS = {
    "bygg": "Bygg & renovering",
    "fastighet": "Fastighet",
    "ute": "Utemiljö & vinter",
}

# id, grupp, namn, kort text, bild, ingress, brödtext, typiska uppdrag, passar för, avdrag
SERVICES = [
    dict(id="bygg", g="bygg", name="Bygg & reparation", short="Mindre byggjobb, lagningar och åtgärder som inte kan vänta.",
         img="stomme.jpg", alt="Byggarbetare monterar armering på en byggarbetsplats",
         lead="Från en dörr som inte stänger till en vägg som ska flyttas. Vi tar de byggjobb som är för stora att göra själv och för små för en totalentreprenör.",
         body="Vi går igenom vad som behöver göras på plats, säger vad det kostar och när vi kan börja. Arbetet utförs av egna hantverkare och ni har en kontaktperson från start till slut.",
         tasks=["Reparationer efter skador och slitage", "Flytt och byggnation av innerväggar", "Montering av dörrar och fönster", "Ny- och ombyggnad av förråd och skärmtak", "Åtgärder efter besiktning", "Akuta lagningar"],
         fit="Privat · Företag · BRF", avdrag="ROT-avdrag kan gälla för privatpersoner"),
    dict(id="snickeri", g="bygg", name="Snickeri", short="Allt inom snickeri – från mindre reparationer till större projekt.",
         img="hero.jpg", alt="Snickare sågar till en planka med cirkelsåg",
         lead="Snickeri är grunden i det mesta vi gör. Lister, foder, golv, trappor, inbyggnader och platsbyggda lösningar – utfört med rätt material och noggranna detaljer.",
         body="Vi mäter, kapar och monterar på plats. Ska något platsbyggas tar vi fram ett förslag innan arbetet börjar, så att ni vet exakt vad ni får.",
         tasks=["Golvläggning och socklar", "Lister, foder och dörrkarmar", "Platsbyggda förvaringslösningar", "Altaner, trall och staket", "Trappor och räcken", "Köksmontering"],
         fit="Privat · Företag · BRF", avdrag="ROT-avdrag kan gälla för privatpersoner"),
    dict(id="renovering", g="bygg", name="Renovering", short="Kök, badrum och kompletta renoveringar av bostäder och lokaler.",
         img="badrum.jpg", alt="Nyrenoverat badrum med duschvägg och kommod",
         lead="En renovering har många moment och många hantverkare. Vi samordnar dem, så att ni slipper hålla ihop projektet själva.",
         body="Vi tar hand om rivning, bygg, snickeri och måleri i egen regi och planerar ordningen mellan momenten. Ni får en tidplan innan start och vet hela tiden var projektet befinner sig.",
         tasks=["Köksrenovering", "Badrumsrenovering", "Renovering av hela bostäder", "Lokalanpassning för företag", "Ytskiktsrenovering", "Renovering av trapphus och gemensamma ytor"],
         fit="Privat · Företag · BRF", avdrag="ROT-avdrag kan gälla för privatpersoner"),
    dict(id="tak", g="bygg", name="Takarbeten", short="Reparation, underhåll och åtgärder på tak och takavvattning.",
         img="tak.jpg", alt="Hantverkare arbetar uppe på ett villatak",
         lead="Ett tak som läcker förstör mer än sig självt. Vi åtgärdar skador, byter det som är slitet och ser över takavvattningen innan problemet växer.",
         body="Vi börjar med en genomgång av taket och dess anslutningar och föreslår vad som behöver göras nu och vad som kan vänta. Arbetet utförs med säkerhetsutrustning anpassad efter taket.",
         tasks=["Lagning av läckage", "Byte av takpannor och plåtdetaljer", "Rengöring och byte av hängrännor", "Stuprör och takavvattning", "Översyn inför vinter", "Mindre takomläggningar"],
         fit="Privat · Företag · BRF", avdrag="ROT-avdrag kan gälla för privatpersoner"),
    dict(id="rivning", g="bygg", name="Rivning", short="Säker och effektiv rivning av väggar, kök, badrum och andra utrymmen.",
         img="isolering.jpg", alt="Hantverkare arbetar i en öppnad väggkonstruktion med isolering",
         lead="Rivning är första steget i de flesta renoveringar, och det steg som avgör hur resten går. Vi river kontrollerat och skyddar det som ska vara kvar.",
         body="Vi täcker och skyddar golv och angränsande ytor, sorterar rivningsmaterialet och ser till att det transporteras bort. När vi är klara är ytan redo för nästa moment.",
         tasks=["Rivning av kök och badrum", "Rivning av innerväggar", "Rivning av golv och undergolv", "Utrensning av lokaler", "Sortering och bortforsling", "Skydd av kvarvarande ytor"],
         fit="Privat · Företag · BRF", avdrag="ROT-avdrag kan gälla för privatpersoner"),
    dict(id="maleri", g="bygg", name="Måleri", short="Invändigt och utvändigt måleri med fokus på kvalitet och finish.",
         img="mal-roller.jpg", alt="Målarroller med blå färg på en vit vägg",
         lead="Ett bra måleriresultat avgörs av förarbetet. Vi spacklar, slipar och grundar innan vi målar – det syns i finishen och i hur länge den håller.",
         body="Vi målar väggar, tak, snickerier och fasader och väljer färgsystem efter underlaget. Möbler och golv skyddas och vi städar efter oss varje dag.",
         tasks=["Väggar och tak", "Snickerier, dörrar och fönster", "Fasadmålning", "Målning av trapphus", "Tapetsering", "Spackling och förarbete"],
         fit="Privat · Företag · BRF", avdrag="ROT-avdrag kan gälla för privatpersoner"),
    dict(id="fastighetsskotsel", g="fastighet", name="Fastighetsskötsel", short="Löpande skötsel och service av fastigheter, trapphus och gemensamma utrymmen.",
         img="fastighet.jpg", alt="Flerbostadshus med balkonger",
         lead="För fastighetsägare och bostadsrättsföreningar tar vi hand om den löpande skötseln, så att fastigheten fungerar året runt utan att styrelsen behöver jaga hantverkare.",
         body="Vi går igenom fastigheten tillsammans med er och lägger upp en plan för vad som görs, hur ofta och av vem. Det som upptäcks under rondering åtgärdas direkt eller rapporteras med förslag.",
         tasks=["Tillsyn och rondering", "Skötsel av trapphus och entréer", "Gemensamma utrymmen och tvättstugor", "Byte av belysning och förbrukningsmaterial", "Mindre reparationer", "Kontakt med boende vid åtgärder"],
         fit="Fastighetsägare · BRF · Företag", avdrag="Avtal efter fastighetens behov"),
    dict(id="underhall", g="fastighet", name="Invändigt & utvändigt underhåll", short="Planerat underhåll som håller fastigheten i skick och värde.",
         img="mal-fasad.jpg", alt="Målare på stegar målar om en husfasad",
         lead="Planerat underhåll är billigare än akuta åtgärder. Vi utför de punkter som står i er underhållsplan och hjälper till att prioritera när budgeten inte räcker till allt.",
         body="Fasad, fönster, entréer, trapphus, förråd och gårdar. Vi kombinerar bygg, snickeri och måleri i samma uppdrag, så att ett underhållsprojekt inte kräver tre olika leverantörer.",
         tasks=["Fasadrenovering och fasadmålning", "Fönsterrenovering", "Entrépartier och dörrar", "Förråd, soprum och cykelrum", "Åtgärder enligt underhållsplan", "Underhåll av staket och plank"],
         fit="Fastighetsägare · BRF · Företag", avdrag="Fast pris eller löpande räkning"),
    dict(id="utemiljo", g="ute", name="Gräsklippning, häck & trädgård", short="Regelbunden skötsel av gräsmattor, häckar, buskar och planteringar.",
         img="grasmatta.jpg", alt="Nyklippt gräsmatta framför en byggnad",
         lead="En välskött utemiljö är det första man ser. Vi klipper, trimmar och rensar enligt schema under hela säsongen.",
         body="Gräsklippning, häcktrimning och trädgårdsskötsel för villor, företag och bostadsrättsföreningar. Vi håller häckar och buskar friska och i rätt form året runt, och tar hand om plantering, rensning och lövhämtning.",
         tasks=["Regelbunden gräsklippning", "Häcktrimning och beskärning", "Plantering och rensning", "Lövhämtning och höststädning", "Vårstädning av gårdar", "Bortforsling av trädgårdsavfall"],
         fit="Privat · Företag · BRF", avdrag="RUT-avdrag kan gälla för privatpersoner"),
    dict(id="snorojning", g="ute", name="Snöröjning & halkbekämpning", short="Säkra och tillgängliga utemiljöer på vintern.",
         img="sno.jpg", alt="Snötäckt gata med lyktstolpar",
         lead="När snön kommer ska entréer, gångar och parkeringar vara framkomliga – innan de boende och anställda går ut.",
         body="Vi skottar, plogar och sandar enligt överenskomna nivåer och prioriterar entréer och gångstråk. Avtal tecknas inför säsongen så att ni vet att det fungerar när det väl behövs.",
         tasks=["Snöskottning av entréer och gångar", "Plogning av parkeringar och infarter", "Sandning och saltning", "Takskottning och istappar", "Avtal per säsong", "Sandupptagning på våren"],
         fit="Privat · Företag · BRF", avdrag="RUT-avdrag kan gälla för privatpersoner"),
]

PRINCIPLES = [
    ("Kvalitet", "Vi kompromissar aldrig med kvalitet. Rätt material, rätt metod och ett arbete vi kan stå för när ni granskar det."),
    ("Pålitlighet", "Vi håller vad vi lovar – varje gång. Det vi säger i offerten är det vi levererar, i tid och till överenskommet pris."),
    ("Flexibilitet", "Vi anpassar oss efter era behov. Små och stora uppdrag, engångsjobb och löpande avtal."),
    ("Lokalt och engagerat", "Vi bryr oss om våra kunder och vår miljö. Vi finns i Stockholm och tar ansvar för det vi gör här."),
]

PROCESS = [
    ("Kontakt", "Ni beskriver vad som behöver göras – per telefon, mejl eller via offertformuläret."),
    ("Platsbesök", "Vi tittar på uppdraget på plats, ställer rätt frågor och föreslår en lösning."),
    ("Offert", "Ni får en kostnadsfri offert med omfattning, pris och tidplan. Inga dolda tillägg."),
    ("Utförande", "Egna hantverkare utför arbetet. Ni har en kontaktperson genom hela projektet."),
    ("Överlämning", "Vi går igenom resultatet tillsammans med er och städar efter oss innan vi lämnar."),
]

# Årshjul för fastighetsservice. w = vinter, g = utemiljö, f = fastighet
YEAR = [
    ("Jan", [("w", "Snöröjning"), ("w", "Halkbekämpning"), ("f", "Tillsyn")]),
    ("Feb", [("w", "Snöröjning"), ("w", "Takskottning"), ("f", "Tillsyn")]),
    ("Mar", [("w", "Halkbekämpning"), ("f", "Underhållsplan"), ("f", "Tillsyn")]),
    ("Apr", [("g", "Sandupptagning"), ("g", "Vårstädning"), ("f", "Takavvattning")]),
    ("Maj", [("g", "Gräsklippning"), ("g", "Plantering"), ("f", "Fasadöversyn")]),
    ("Jun", [("g", "Gräsklippning"), ("g", "Häcktrimning"), ("f", "Utvändigt måleri")]),
    ("Jul", [("g", "Gräsklippning"), ("f", "Utvändigt måleri"), ("f", "Tillsyn")]),
    ("Aug", [("g", "Gräsklippning"), ("g", "Häcktrimning"), ("f", "Fönster & entréer")]),
    ("Sep", [("g", "Gräsklippning"), ("g", "Beskärning"), ("f", "Trapphus")]),
    ("Okt", [("g", "Lövhämtning"), ("g", "Höststädning"), ("f", "Hängrännor")]),
    ("Nov", [("g", "Lövhämtning"), ("f", "Vinterförberedelse"), ("f", "Invändigt underhåll")]),
    ("Dec", [("w", "Snöröjning"), ("w", "Halkbekämpning"), ("f", "Tillsyn")]),
]

NAV = [("tjanster.html", "Tjänster"), ("fastighet.html", "Fastighetsägare & BRF"), ("om.html", "Om Nexus"), ("kontakt.html", "Kontakt")]


def brand():
    return f'<span class="brand-word"><b>NEXUS</b><small>SERVICE AB</small></span>'


def mega():
    cols = []
    for g, title in GROUPS.items():
        items = "".join(
            f'<li><a href="tjanster.html#{s["id"]}"><b>{escape(s["name"])}</b><span>{escape(s["short"])}</span></a></li>'
            for s in SERVICES if s["g"] == g)
        cols.append(f'<div class="mega-col"><h4>{title}</h4><ul>{items}</ul></div>')
    feature = f'''<a class="mega-feature" href="kontakt.html#offert">
          <img src="img/planering.jpg" alt="" loading="lazy">
          <div><h5>Kostnadsfri offert</h5><p>Beskriv uppdraget så återkommer vi med pris och tidplan.</p><span class="link-arrow">Begär offert {ARR}</span></div>
        </a>'''
    return f'<div class="mega" id="mega"><div class="wrap mega-grid">{"".join(cols)}{feature}</div></div>'


def header(active):
    links = []
    for href, label in NAV:
        cur = ' aria-current="page"' if href == active else ''
        if href == "tjanster.html":
            dc = ' data-current' if active == href else ''
            links.append(f'<div class="has-mega"><button type="button" aria-expanded="false" aria-controls="mega"{dc}>Tjänster {CHEV}</button>{mega()}</div>')
        else:
            links.append(f'<a href="{href}"{cur}>{label}</a>')
    return f'''<a class="skip" href="#main">Hoppa till innehåll</a>
<div class="util">
  <div class="wrap util-inner">
    <nav class="util-seg" aria-label="Kundgrupper">
      <a href="tjanster.html">Privatperson</a>
      <a href="om.html#kunder">Företag</a>
      <a href="fastighet.html">Fastighetsägare &amp; BRF</a>
    </nav>
    <div class="util-meta">
      <span class="util-area">{AREA}</span>
      <a href="{PHONE_HREF}">{PHONE}</a>
      <a href="mailto:{EMAIL}">{EMAIL}</a>
    </div>
  </div>
</div>
<header class="header">
  <div class="wrap header-inner">
    <a class="brand" href="index.html" aria-label="Nexus Service AB – startsida">{LOGO}{brand()}</a>
    <nav class="nav" id="nav" aria-label="Huvudmeny">{"".join(links)}</nav>
    <div class="header-cta">
      <a class="header-phone" href="{PHONE_HREF}">{PHONE}</a>
      <a class="btn btn-orange" href="kontakt.html#offert">Begär offert {ARR}</a>
      <button class="menu-btn" id="menuBtn" type="button" aria-label="Öppna meny" aria-expanded="false" aria-controls="nav"><span></span><span></span><span></span></button>
    </div>
  </div>
</header>'''


def cta_band():
    return f'''<section class="cta-band">
  <div class="wrap cta-inner">
    <h2 class="display">Kontakta oss för en kostnadsfri offert.</h2>
    <div class="cta-side">
      <a class="btn btn-ink" href="kontakt.html#offert">Begär offert {ARR}</a>
      <a class="btn btn-line" href="{PHONE_HREF}">Ring {PHONE} {ARR}</a>
      <p class="cta-note">Vi svarar normalt inom en arbetsdag.</p>
    </div>
  </div>
</section>'''


def footer():
    by = lambda g: "".join(f'<li><a href="tjanster.html#{s["id"]}">{escape(s["name"])}</a></li>' for s in SERVICES if s["g"] == g)
    return f'''<footer class="footer">
  <div class="wrap footer-top">
    <div>
      <a class="brand" href="index.html" aria-label="Nexus Service AB – startsida">{LOGO}{brand()}</a>
      <p class="footer-tag">Bygg, renovering och fastighetsservice för privatpersoner, företag, fastighetsägare och bostadsrättsföreningar i {AREA}.</p>
    </div>
    <div><h4>Bygg &amp; renovering</h4><ul>{by("bygg")}</ul></div>
    <div><h4>Fastighet</h4><ul>{by("fastighet")}<li><a href="fastighet.html">För fastighetsägare &amp; BRF</a></li></ul></div>
    <div><h4>Utemiljö &amp; vinter</h4><ul>{by("ute")}</ul></div>
    <div><h4>Kontakt</h4><ul>
      <li><a href="{PHONE_HREF}">{PHONE}</a></li>
      <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
      <li>{AREA}</li>
      <li><a href="kontakt.html#offert">Begär offert</a></li>
    </ul></div>
  </div>
  <div class="wrap footer-word" aria-hidden="true">NEXUS</div>
  <div class="wrap footer-bottom">
    <span>© 2026 Nexus Service AB</span>
    <span>Vi får det att fungera. Hemma. På jobbet. Överallt.</span>
  </div>
</footer>'''


def page(filename, title, desc, body, active=None):
    html = f'''<!DOCTYPE html>
<html lang="sv">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)}</title>
<meta name="description" content="{escape(desc)}">
<meta property="og:title" content="{escape(title)}">
<meta property="og:description" content="{escape(desc)}">
<meta property="og:image" content="img/hero.jpg">
<meta name="theme-color" content="#111416">
<link rel="icon" href="img/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Schibsted+Grotesk:wght@400;500;600;700;800&display=swap" rel="stylesheet">
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


def page_head(crumb, title, lead, img=None, alt=""):
    image = f'<div class="wrap"><div class="page-head-img"><img src="img/{img}" alt="{escape(alt)}"></div></div>' if img else ''
    return f'''<section class="page-head">
  <div class="wrap page-head-inner">
    <div>
      <nav class="crumbs" aria-label="Brödsmulor"><a href="index.html">Start</a><span>/</span><span>{crumb}</span></nav>
      <h1 class="display">{title}</h1>
    </div>
    <p class="lead">{lead}</p>
  </div>
</section>
{f'<div style="background:linear-gradient(var(--paper) 50%, var(--white) 50%)">{image}</div>' if img else ''}'''


def process_html():
    return "".join(f'<div class="step"><div class="n">{i:02d}</div><h3>{t}</h3><p>{d}</p></div>' for i, (t, d) in enumerate(PROCESS, 1))


def principles_html():
    return "".join(f'<div class="principle"><span class="n">{i:02d}</span><h3>{t}</h3><p>{d}</p></div>' for i, (t, d) in enumerate(PRINCIPLES, 1))


def year_html():
    months = "".join(
        f'<div class="month"><h3>{m}</h3><ul>{"".join(f"<li class={k}>{t}</li>" for k, t in items)}</ul></div>'
        for m, items in YEAR)
    legend = '''<div class="legend">
      <span><i style="background:#5b7c99"></i>Vinter</span>
      <span><i style="background:#5d7f4e"></i>Utemiljö</span>
      <span><i style="background:var(--orange)"></i>Fastighet &amp; underhåll</span>
    </div>'''
    return f'<div class="year" role="list" aria-label="Årshjul för fastighetsservice">{months}</div>{legend}'


# ---------------------------------------------------------------- Startsida
def build_index():
    rows, imgs, n = [], [], 0
    for g, title in GROUPS.items():
        rows.append(f'<div class="svc-group-title">{title}</div>')
        for s in (s for s in SERVICES if s["g"] == g):
            n += 1
            rows.append(f'<a class="svc-row{" is-active" if n == 1 else ""}" href="tjanster.html#{s["id"]}"><span class="n">{n:02d}</span><h3>{escape(s["name"])}</h3>{ARR}<p>{escape(s["short"])}</p></a>')
            imgs.append(f'<img src="img/{s["img"]}" alt=""{" class=is-on" if n == 1 else ""} loading="lazy">')

    body = f'''<section class="hero">
  <div class="hero-media"><img src="img/hero.jpg" alt="Snickare från Nexus Service sågar till virke på en arbetsplats" fetchpriority="high"></div>
  <div class="wrap hero-body">
    <span class="label">Bygg · Renovering · Fastighetsservice</span>
    <h1 class="display">Vi får det att fungera<span>.</span></h1>
    <p class="hero-lead">Hemma. På jobbet. Överallt. Nexus Service tar hand om ditt bygg- och fastighetsprojekt från idé till färdigt resultat – i {AREA}.</p>
    <div class="hero-actions">
      <a class="btn btn-orange" href="kontakt.html#offert">Begär kostnadsfri offert {ARR}</a>
      <a class="btn btn-line on-dark" href="tjanster.html">Se alla tjänster {ARR}</a>
    </div>
  </div>
  <div class="segments">
    <div class="wrap segments-grid">
      <a class="segment" href="tjanster.html"><span class="num">För privatpersoner</span><h2>Hem &amp; villa {ARR}</h2><p>Renovering, snickeri, måleri och trädgård. ROT- och RUT-avdrag där det gäller.</p></a>
      <a class="segment" href="om.html#kunder"><span class="num">För företag</span><h2>Lokaler &amp; verksamheter {ARR}</h2><p>Anpassningar, reparationer och skötsel som inte stör den dagliga driften.</p></a>
      <a class="segment" href="fastighet.html"><span class="num">För fastighetsägare &amp; BRF</span><h2>Fastighetsservice {ARR}</h2><p>Löpande skötsel, underhåll, utemiljö och snöröjning – en kontakt för hela året.</p></a>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="intro reveal">
      <span class="label">Uppdraget</span>
      <p class="statement">Vi hjälper privatpersoner, företag, fastighetsägare och bostadsrättsföreningar med både mindre och större projekt <em>– från löpande underhåll till kompletta renoveringar.</em></p>
    </div>
    <dl class="intro-foot reveal">
      <div><dt>Omfattning</dt><dd>Bygg, renovering, underhåll och fastighetsskötsel i samma bolag.</dd></div>
      <div><dt>Arbetssätt</dt><dd>En kontaktperson, en offert, ett ansvar – från idé till färdigt resultat.</dd></div>
      <div><dt>Område</dt><dd>{AREA}. Hemma, på jobbet och i fastigheten.</dd></div>
    </dl>
  </div>
</section>

<section class="section paper" id="tjanster">
  <div class="wrap">
    <div class="sec-head split">
      <div><span class="label">Tjänster</span><h2 class="h2" style="margin-top:20px">Tio tjänster. En leverantör.</h2></div>
      <p class="lead">Ett projekt kräver ofta flera yrken. Vi har dem under samma tak, så att rivning, bygg, måleri och skötsel hänger ihop.</p>
    </div>
    <div class="svc-index">
      <div class="svc-list">{"".join(rows)}</div>
      <figure class="svc-preview" aria-hidden="true">{"".join(imgs)}<figcaption>{escape(SERVICES[0]["name"])}</figcaption></figure>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="sec-head">
      <span class="label">Affärsområden</span>
      <h2 class="h2">Tre områden som täcker hela fastighetens livscykel.</h2>
    </div>
    <div class="areas">
      <a class="area" href="tjanster.html#renovering">
        <div class="area-img"><img src="img/kok.jpg" alt="Renoverat kök med vita luckor och köksö" loading="lazy"></div>
        <div class="area-body"><span class="tag">01 — Bygg &amp; renovering</span><h3 class="h3">Från en lagning till en totalrenovering.</h3>
          <ul><li>Bygg &amp; reparation <span>ROT</span></li><li>Snickeri <span>ROT</span></li><li>Renovering <span>ROT</span></li><li>Takarbeten, rivning, måleri <span>ROT</span></li></ul></div>
      </a>
      <a class="area" href="fastighet.html">
        <div class="area-img"><img src="img/fastighet2.jpg" alt="Modernt flerbostadshus med balkonger" loading="lazy"></div>
        <div class="area-body"><span class="tag">02 — Fastighet</span><h3 class="h3">Löpande skötsel och planerat underhåll.</h3>
          <ul><li>Fastighetsskötsel <span>Avtal</span></li><li>Trapphus &amp; gemensamma utrymmen <span>Avtal</span></li><li>Invändigt underhåll <span>Projekt</span></li><li>Utvändigt underhåll <span>Projekt</span></li></ul></div>
      </a>
      <a class="area" href="tjanster.html#utemiljo">
        <div class="area-img"><img src="img/tradgard.jpg" alt="Trädgårdsspade och jord vid plantering" loading="lazy"></div>
        <div class="area-body"><span class="tag">03 — Utemiljö &amp; vinter</span><h3 class="h3">Välskötta ytor, sommar som vinter.</h3>
          <ul><li>Gräsklippning <span>RUT</span></li><li>Häcktrimning <span>RUT</span></li><li>Trädgårdsservice <span>RUT</span></li><li>Snöröjning &amp; halkbekämpning <span>RUT</span></li></ul></div>
      </a>
    </div>
  </div>
</section>

<section class="section dark">
  <div class="wrap">
    <div class="sec-head split">
      <div><span class="label on-dark">Så arbetar vi</span><h2 class="h2" style="margin-top:20px">Från idé till färdigt resultat.</h2></div>
      <p class="lead">Samma fem steg oavsett om uppdraget tar en förmiddag eller tre månader.</p>
    </div>
    <div class="process">{process_html()}</div>
  </div>
</section>

<section class="section paper">
  <div class="wrap">
    <div class="sec-head split">
      <div><span class="label">För fastighetsägare &amp; BRF</span><h2 class="h2" style="margin-top:20px">Fastighetens år, planerat.</h2></div>
      <div><p class="lead">Ett exempel på hur ett års fastighetsservice kan se ut. Innehållet anpassas efter er fastighet och ert avtal.</p><a class="link-arrow" href="fastighet.html">Läs om fastighetsservice {ARR}</a></div>
    </div>
    {year_html()}
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="sec-head">
      <span class="label">Det vi står för</span>
      <h2 class="h2">Fyra löften vi mäts mot.</h2>
    </div>
    <div class="principles">{principles_html()}</div>
  </div>
</section>

<section class="region">
  <div class="region-img"><img src="img/stockholm.jpg" alt="Riddarholmen och Stockholms stadssiluett i skymning" loading="lazy"></div>
  <div class="region-body">
    <div>
      <span class="label on-dark">Verksamhetsområde</span>
      <h2 class="h2">{AREA}.</h2>
    </div>
    <div>
      <p>Vi arbetar lokalt. Det betyder korta inställelsetider, hantverkare som känner till stadens fastighetsbestånd och en leverantör som finns kvar när jobbet är klart.</p>
      <a class="btn btn-line on-dark" href="kontakt.html">Kontakta oss {ARR}</a>
    </div>
    <div class="coords"><span>59.3293° N, 18.0686° E</span><span>Stockholm</span></div>
  </div>
</section>

{cta_band()}'''
    page("index.html", "Nexus Service AB – Bygg, renovering och fastighetsservice i Stockholm",
         "Nexus Service utför bygg, reparation, renovering, måleri, takarbeten och fastighetsskötsel för privatpersoner, företag och BRF i Stockholm med omnejd. Kostnadsfri offert.",
         body)


# ---------------------------------------------------------------- Tjänster
def build_services():
    toc, secs = [], []
    for i, s in enumerate(SERVICES, 1):
        toc.append(f'<a href="#{s["id"]}"><span>{i:02d}</span>{escape(s["name"])}</a>')
        tasks = "".join(f"<li>{escape(t)}</li>" for t in s["tasks"])
        secs.append(f'''<article class="svc" id="{s["id"]}">
      <div class="svc-top"><span class="n">{i:02d}</span><span class="group">{GROUPS[s["g"]]}</span></div>
      <h2>{escape(s["name"])}</h2>
      <div class="svc-img"><img src="img/{s["img"]}" alt="{escape(s["alt"])}" loading="lazy"></div>
      <div class="svc-cols">
        <div>
          <p class="lead">{escape(s["lead"])}</p>
          <p class="muted">{escape(s["body"])}</p>
          <h3 class="label" style="margin:28px 0 8px">Typiska uppdrag</h3>
          <ul class="tasks">{tasks}</ul>
        </div>
        <div>
          <dl class="facts">
            <div><dt>Passar för</dt><dd>{s["fit"]}</dd></div>
            <div><dt>Ersättning</dt><dd>{s["avdrag"]}</dd></div>
            <div><dt>Område</dt><dd>{AREA}</dd></div>
            <div><dt>Offert</dt><dd>Kostnadsfri</dd></div>
          </dl>
          <a class="btn btn-ink" style="margin-top:24px;width:100%" href="kontakt.html?tjanst={s["id"]}#offert">Begär offert på {escape(s["name"].lower())} {ARR}</a>
        </div>
      </div>
    </article>''')
    body = page_head("Tjänster", "Tjänster", "Bygg, renovering, underhåll och fastighetsservice. Välj en tjänst – eller kombinera flera i samma uppdrag.") + f'''
<section class="section">
  <div class="wrap svc-layout">
    <nav class="toc" aria-label="Tjänster på sidan"><h4>Alla tjänster</h4>{"".join(toc)}</nav>
    <div>{"".join(secs)}</div>
  </div>
</section>
{cta_band()}'''
    page("tjanster.html", "Tjänster – Nexus Service AB",
         "Bygg och reparation, snickeri, renovering, takarbeten, rivning, måleri, fastighetsskötsel, underhåll, trädgård och snöröjning i Stockholm.",
         body, "tjanster.html")


# ---------------------------------------------------------------- Fastighet & BRF
def build_property():
    body = page_head("Fastighetsägare &amp; BRF", "Fastighets&shy;service för ägare och BRF.",
                     "Löpande skötsel, planerat underhåll, utemiljö och vinter. En leverantör och en kontaktperson för hela fastigheten.",
                     "fastighet2.jpg", "Flerbostadshus med balkonger") + f'''
<section class="section">
  <div class="wrap duo">
    <div>
      <span class="label">Varför en leverantör</span>
      <h2 class="h2" style="margin:20px 0 24px">Färre kontakter. Kortare väg till åtgärd.</h2>
      <p class="lead">När skötsel, reparationer och underhåll ligger hos olika företag blir styrelsen projektledare. Hos oss ligger de i samma avtal.</p>
      <ul class="checklist">
        <li><b>En kontaktperson</b><span>Samma person följer fastigheten och vet vad som gjorts tidigare.</span></li>
        <li><b>Åtgärd direkt</b><span>Det som upptäcks vid rondering och som ryms i avtalet åtgärdas på plats.</span></li>
        <li><b>Hantverkare i samma bolag</b><span>Snickeri, måleri och bygg utan att ta in nya leverantörer.</span></li>
        <li><b>Rapport efter besök</b><span>Ni vet vad som är gjort och vad som behöver planeras.</span></li>
      </ul>
    </div>
    <div class="duo-img"><img src="img/fastighet.jpg" alt="Fasad på flerbostadshus med balkonger" loading="lazy"></div>
  </div>
</section>

<section class="section paper">
  <div class="wrap">
    <div class="sec-head split">
      <div><span class="label">Upplägg</span><h2 class="h2" style="margin-top:20px">Tre sätt att anlita oss.</h2></div>
      <p class="lead">Upplägget anpassas efter fastighetens storlek, skick och er budget. Alla börjar med en kostnadsfri genomgång.</p>
    </div>
    <div class="packages">
      <div class="package"><span class="tag">Löpande</span><h3>Skötselavtal</h3><p>Återkommande tillsyn och skötsel med fast omfattning och fast pris per månad.</p>
        <ul><li>Tillsyn och rondering</li><li>Trapphus och gemensamma utrymmen</li><li>Utemiljö under säsong</li><li>Mindre reparationer</li></ul></div>
      <div class="package"><span class="tag">Säsong</span><h3>Säsongsavtal</h3><p>Utemiljö sommartid och snöröjning vintertid, med beredskap och prioriteringsordning.</p>
        <ul><li>Gräsklippning och häckar</li><li>Lövhämtning och höststädning</li><li>Snöröjning och halkbekämpning</li><li>Vår- och sandupptagning</li></ul></div>
      <div class="package"><span class="tag">Projekt</span><h3>Underhållsprojekt</h3><p>Enskilda åtgärder ur underhållsplanen till fast pris eller på löpande räkning.</p>
        <ul><li>Trapphusrenovering</li><li>Fasad och fönster</li><li>Tak och takavvattning</li><li>Förråd, soprum och entréer</li></ul></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="sec-head split">
      <div><span class="label">Årshjul</span><h2 class="h2" style="margin-top:20px">Så kan ett år se ut.</h2></div>
      <p class="lead">Ett exempel. Vi gör ett eget årshjul för er fastighet tillsammans med styrelsen eller förvaltaren.</p>
    </div>
    {year_html()}
  </div>
</section>

<section class="section dark">
  <div class="wrap duo">
    <div class="duo-img"><img src="img/sno.jpg" alt="Snötäckt gata i Stockholm" loading="lazy"></div>
    <div>
      <span class="label on-dark">Vinter</span>
      <h2 class="h2" style="margin:20px 0 24px">Entréerna klara innan de boende går ut.</h2>
      <p class="lead">Snöröjning och halkbekämpning avtalas inför säsongen med tydliga nivåer, så att ingen behöver undra vem som ansvarar.</p>
      <ul class="checklist">
        <li><b>Prioriterade ytor</b><span>Entréer, gångstråk, trappor och tillgänglighetsanpassade vägar först.</span></li>
        <li><b>Halkbekämpning</b><span>Sandning och saltning efter väderlek.</span></li>
        <li><b>Tak och istappar</b><span>Takskottning och nedtagning av istappar vid behov.</span></li>
      </ul>
    </div>
  </div>
</section>
{cta_band()}'''
    page("fastighet.html", "Fastighetsservice för fastighetsägare och BRF – Nexus Service AB",
         "Fastighetsskötsel, underhåll, utemiljö och snöröjning för bostadsrättsföreningar och fastighetsägare i Stockholm. En leverantör, en kontaktperson.",
         body, "fastighet.html")


# ---------------------------------------------------------------- Om
def build_about():
    body = page_head("Om Nexus", "Vi får det att fungera.",
                     "Nexus Service erbjuder professionella tjänster inom bygg, reparation, renovering och fastighetsskötsel.",
                     "interior.jpg", "Ljust och nyrenoverat vardagsrum med trägolv") + f'''
<section class="section">
  <div class="wrap about-grid">
    <span class="label">Företaget</span>
    <div>
      <p class="statement" style="margin-bottom:48px">Med fokus på kvalitet, noggrannhet och ett professionellt utfört arbete strävar vi efter att alltid hitta rätt lösning för varje kund och projekt.</p>
      <div class="about-text">
        <p>Nexus Service hjälper privatpersoner, företag, fastighetsägare och bostadsrättsföreningar med både mindre och större projekt – från löpande underhåll till kompletta renoveringar.</p>
        <p>Våra tjänster omfattar bland annat bygg- och reparationsarbeten, snickeri, takarbeten, rivning, målning, renovering samt invändigt och utvändigt underhåll av fastigheter.</p>
        <p>Till det kommer utemiljön: gräsklippning, häcktrimning, trädgårdsservice och snöröjning. Det gör att vi kan ta ansvar för en fastighet året runt, inte bara för ett enskilt jobb.</p>
        <p>Vi tar hand om ditt bygg- och fastighetsprojekt från idé till färdigt resultat. Hemma. På jobbet. Överallt.</p>
      </div>
    </div>
  </div>
</section>

<section class="section paper" id="kunder">
  <div class="wrap">
    <div class="sec-head">
      <span class="label">Våra kunder</span>
      <h2 class="h2">Fyra kundgrupper, samma standard.</h2>
    </div>
    <div class="for-whom">
      <div><span class="n">01</span><h3>Privatpersoner</h3><p>Renovering, reparationer, måleri och trädgård i villa, radhus och lägenhet. ROT- och RUT-avdrag där det gäller.</p></div>
      <div><span class="n">02</span><h3>Företag</h3><p>Lokalanpassningar, reparationer och löpande service, planerat så att verksamheten kan fortsätta.</p></div>
      <div><span class="n">03</span><h3>Fastighetsägare</h3><p>Skötsel och underhåll av bostads- och kommersiella fastigheter, med rapportering efter varje insats.</p></div>
      <div><span class="n">04</span><h3>Bostadsrätts&shy;föreningar</h3><p>En leverantör för trapphus, gemensamma utrymmen, utemiljö och vinter – och för underhållsplanens projekt.</p></div>
    </div>
  </div>
</section>

<section class="section dark" id="process">
  <div class="wrap">
    <div class="sec-head split">
      <div><span class="label on-dark">Så arbetar vi</span><h2 class="h2" style="margin-top:20px">Fem steg. Inga överraskningar.</h2></div>
      <p class="lead">Ni vet vad som ska göras, vad det kostar och när det är klart – innan vi börjar.</p>
    </div>
    <div class="process">{process_html()}</div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="sec-head">
      <span class="label">Det vi står för</span>
      <h2 class="h2">Fyra löften vi mäts mot.</h2>
    </div>
    <div class="principles">{principles_html()}</div>
  </div>
</section>
{cta_band()}'''
    page("om.html", "Om Nexus Service AB – Bygg och fastighetsservice i Stockholm",
         "Nexus Service hjälper privatpersoner, företag, fastighetsägare och BRF med bygg, renovering och fastighetsskötsel – från idé till färdigt resultat.",
         body, "om.html")


# ---------------------------------------------------------------- Kontakt
def build_contact():
    checks = "".join(f'<label><input type="checkbox" name="tjanst" value="{s["id"]}"><span>{escape(s["name"])}</span></label>' for s in SERVICES)
    faq = [
        ("Kostar offerten något?", "Nej. Offert och platsbesök är kostnadsfria och utan förpliktelser."),
        ("Kan jag använda ROT- eller RUT-avdrag?", "Som privatperson kan du ofta göra ROT-avdrag på arbetskostnaden för bygg, renovering och måleri, och RUT-avdrag för trädgårdsarbete och snöskottning. Vi går igenom vad som gäller för ditt uppdrag i offerten."),
        ("Vilket område arbetar ni i?", f"Vi arbetar i {AREA}. Hör av dig om du är osäker på om vi täcker din adress."),
        ("Tar ni små jobb?", "Ja. Vi tar både mindre reparationer och större projekt, och engångsjobb lika väl som löpande avtal."),
        ("Hur snabbt kan ni börja?", "Det beror på uppdraget och säsongen. Du får ett startdatum i offerten."),
    ]
    faq_html = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faq)
    body = page_head("Kontakt", "Begär offert.",
                     "Beskriv uppdraget så återkommer vi med en kostnadsfri offert. Du kan också ringa eller mejla direkt.") + f'''
<section class="section" id="offert">
  <div class="wrap contact-grid">
    <div>
      <dl class="contact-card">
        <div><dt>Telefon</dt><dd><a href="{PHONE_HREF}">{PHONE}</a></dd></div>
        <div><dt>E-post</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd></div>
        <div><dt>Webb</dt><dd>www.nexusserviceab.se</dd></div>
        <div><dt>Område</dt><dd>{AREA}</dd></div>
      </dl>
    </div>
    <form class="form" id="offertForm" novalidate>
      <fieldset>
        <legend>1. Jag är</legend>
        <div class="seg-choice">
          <label><input type="radio" name="kund" value="privat" checked><span>Privatperson</span></label>
          <label><input type="radio" name="kund" value="foretag"><span>Företag</span></label>
          <label><input type="radio" name="kund" value="brf"><span>Fastighetsägare / BRF</span></label>
        </div>
      </fieldset>
      <fieldset>
        <legend>2. Det gäller</legend>
        <div class="checks">{checks}</div>
      </fieldset>
      <fieldset>
        <legend>3. Uppgifter</legend>
        <div class="fields">
          <div class="field"><label for="namn">Namn *</label><input id="namn" name="namn" autocomplete="name" required></div>
          <div class="field"><label for="foretag">Företag / BRF</label><input id="foretag" name="foretag" autocomplete="organization"></div>
          <div class="field"><label for="telefon">Telefon *</label><input id="telefon" name="telefon" type="tel" autocomplete="tel" required></div>
          <div class="field"><label for="epost">E-post *</label><input id="epost" name="epost" type="email" autocomplete="email" required></div>
          <div class="field"><label for="adress">Adress eller ort</label><input id="adress" name="adress" autocomplete="street-address"></div>
          <div class="field"><label for="start">Önskad start</label>
            <select id="start" name="start"><option value="">Välj</option><option>Så snart som möjligt</option><option>Inom en månad</option><option>Inom tre månader</option><option>Senare / planeras</option><option>Löpande avtal</option></select></div>
          <div class="field full"><label for="beskrivning">Beskriv uppdraget *</label><textarea id="beskrivning" name="beskrivning" required placeholder="Vad ska göras, ungefärlig storlek, och annat vi bör veta."></textarea></div>
        </div>
      </fieldset>
      <div class="form-foot">
        <p>Förfrågan öppnas i ditt e-postprogram, adresserad till {EMAIL}.</p>
        <button class="btn btn-orange" type="submit">Skicka förfrågan {ARR}</button>
      </div>
      <p class="form-status" id="formStatus" role="status"></p>
    </form>
  </div>
</section>

<section class="section paper">
  <div class="wrap contact-grid">
    <div><span class="label">Vanliga frågor</span><h2 class="h2" style="margin-top:20px">Bra att veta.</h2></div>
    <div class="faq">{faq_html}</div>
  </div>
</section>'''
    page("kontakt.html", "Kontakt och offert – Nexus Service AB",
         "Begär kostnadsfri offert på bygg, renovering eller fastighetsservice i Stockholm. Ring 076-123 45 67 eller mejla info@nexusserviceab.se.",
         body, "kontakt.html")


if __name__ == "__main__":
    build_index()
    build_services()
    build_property()
    build_about()
    build_contact()
    print("Klart: index, tjanster, fastighet, om, kontakt")
