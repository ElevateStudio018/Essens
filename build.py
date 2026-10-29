"""Generates the static site. Run: python3 build.py"""
import html
from pathlib import Path

# Elevate Studio's credit under every footer: the mark and the name, the whole of it one link to elevatestudio.nu.
ELEVATE_CREDIT = '''<!-- elevate-credit -->
<style>.elevate-credit{max-width:1240px;margin:24px auto 0;padding:20px 16px 0;border-top:1px solid rgba(128,128,128,.25);display:flex;justify-content:center;box-sizing:border-box}.elevate-credit a{display:inline-flex;align-items:center;gap:10px;padding:8px 0;font:inherit;font-size:15px;line-height:1;color:inherit;opacity:.55;text-decoration:none;transition:opacity .2s}.elevate-credit a:hover,.elevate-credit a:focus-visible{opacity:1}.elevate-credit svg{width:20px;height:20px;flex:none;display:block}@media(min-width:1024px){.elevate-credit a{font-size:16px}}</style>
<div class="elevate-credit"><a href="https://elevatestudio.nu" target="_blank" rel="noopener"><svg viewBox="0 0 1884.3 1353.9" aria-hidden="true"><path d="M0.0 1353.9 L1218.7 0.0 L1218.7 329.1 L479.7 1136.4 L786.7 1132.4 L1215.5 687.4 L1884.3 1349.9 L1590.1 1349.9 L1218.6 994.7 L865.4 1349.9Z" fill="currentColor"/></svg>Byggd av Elevate Studio</a></div>
'''


ROOT = Path(__file__).parent
ARROW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
ARROW_UR = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
IMG = "assets/img/"

# ---------------------------------------------------------------- projects
# cat: villor | flerbostadshus | kontor | ovrigt
PROJECTS = [
    dict(slug="savelangen", title="Villa Sävelången", sub="Nyproduktion av villa", short="Nyproduktion, Ingared", cat="villor",
         cover="Villa-Savelangen-bild-2-4_3.webp", hero="Villa-Savelangen-bild-2-4_3.webp",
         spec=[("Status", "Färdigställd (2026)"), ("Omfattning", "Skissarbete, bygglov, bygghandlingar"),
               ("Beställare", '<a href="https://ahlnings.se/" target="_blank" rel="noopener">Ahlnings Bygg</a>'), ("Visualiseringar", "PI Visual")],
         text=["Insmugen på en lummig villagata i Ingared har vi ritat ett tillskott på två villor.",
               "Villa Sävelången är en modern enplansvilla på 148 kvm. Byggnadens utformning ger en fin uppdelning mellan olika funktioner, samtidigt som helheten knyts ihop med en rik variation på såväl utvändiga som invändiga rum.",
               "Den strama, relativt tillslutna entrégården skapar en förväntan när man anländer till platsen. Väl inne möts man av de välplanerade sociala ytorna med flera kopplingar ut i trädgården och utsikt mot badplats och sjön Sävelången.",
               "Uppdelningen, och kopplingarna, mellan sociala och mer privata delar av bostaden skapar en dynamik samtidigt som det även rent praktiskt underlättar för familjelivets skiftande behov av gemenskap och avskildhet.",
               'Se även intilliggande <a class="link" href="ingared.html">Villa Ingared</a>.'],
         gallery=[("Villa-Savelangen-bild-1-4_3.webp", "full"), ("Plan-Savelangen.webp", "full plan"),
                  ("Villa-Savelangen-bild-3-1_1.webp", ""), ("draft-interior.webp", "")]),
    dict(slug="hantverksgatan", title="Hantverksgatan 18", sub="Nybyggnad av flerbostadshus", short="Hyreshus, Alingsås", cat="flerbostadshus",
         cover="240417-Hantverksg-fotomontage-storre.webp", hero="240417-Hantverksg-utzoomad-16_9.webp",
         spec=[("Typ", "Nyproduktion hyresrätter"), ("Plats", "Alingsås"), ("Omfattning", "Skissarbete, bygglov, bygghandlingar"),
               ("Beställare", '<a href="https://www.arkbladfastigheter.se/" target="_blank" rel="noopener">Arkblad Fastigheter</a>'), ("Status", "Färdigställt 2025")],
         text=["På Hantverksgatan, precis vid infarten till Alingsås, har Essens Arkitektur ritat ett nytt flerbostadshus. Huset består av 15 hyreslägenheter, från ettor på 32 m² till yteffektiva treor på 69 m².",
               "Projektet tillför modern arkitektur med hänsyn till den omgivande småstadsmiljön. Byggnaden är utformad för att harmonisera med gatans befintliga karaktär. Utformning och byggnadshöjd följer områdets rytm, vilket gör att huset smälter naturligt in i gatubilden.",
               "Hyresvärden, som också bygger huset, har lagt stor vikt vid rationell konstruktion och hållbar planering. Resultatet är högkvalitativa och samtidigt yteffektiva bostäder, vilket bidrar till rimliga hyresnivåer för framtida hyresgäster.",
               "Lägenheterna är ljusa och genomtänkta, där tvåor och treor har fönster i flera väderstreck. Alla lägenheter har sovrum mot lugn sida och tillgång till generösa balkonger eller uteplatser.",
               "Utöver den genomtänkta förvaringen i lägenheterna får alla även generösa förråd i antingen källare eller på vinden samt cykelrum med direkt utgång, vilket underlättar både för cyklister och barnfamiljer."],
         gallery=[("Normalplan-forstorad.webp", "full plan"), ("240417-Fasad-pres-5_4.webp", ""), ("240417-Hantverksg-fotomontage-storre.webp", "")]),
    dict(slug="ingared", title="Villa Ingared", sub="Nyproduktion av villa", short="Nyproduktion, Ingared", cat="villor",
         cover="Villa-Ingared-bild-2red-1_1.webp", hero="Villa-Ingared-Gata.webp",
         spec=[("Status", "Pågående, 2024–"), ("Omfattning", "Skissarbete, bygglov, bygghandlingar"),
               ("Beställare", '<a href="https://ahlnings.se/" target="_blank" rel="noopener">Ahlnings Bygg</a>'), ("Visualiseringar", "PI Visual")],
         text=["På Sandviksvägen i Ingared har vi utformat två unika villor till försäljning.",
               "En av dessa villor är Villa Ingared, en modern familjevilla på 153 kvm med både badplats, förskola och skola inom 150 m radie!",
               "Ambitionen med utformningen var att tilltala barnfamiljer som i vanliga fall hade tittat i huskataloger efter sitt drömhus. Vi vill visa att ett platsspecifikt, arkitektritat hus inte behöver kosta mer utan snarare att man får mer för pengarna. Både utifrån en genomritad planlösning med fina detaljer och hur husets placering får ut maximalt av tomten!",
               'Se även den intilliggande enplansvillan <a class="link" href="savelangen.html">Villa Sävelången</a>.',
               "Huset är sålt och under uppförande, beräknad inflytt sommaren 2026."],
         gallery=[("Villa-Ingared-Tradgard.webp", "full"), ("Villa-Ingared-Plan-1.webp", "plan"), ("Villa-Ingared-Plan-2.webp", "plan"),
                  ("Villa-Ingared-Interior.webp", ""), ("Villa-Ingared-Interior-2.webp", "")]),
    dict(slug="bankahall", title="Villa Bankahall", sub="Om- & tillbyggnad av villa", short="Ombyggnad, Varberg", cat="villor",
         cover="MG_7418-1-beskuren.webp", hero="MG_7418-1-beskuren.webp",
         spec=[("Plats", "Träslövsläge, Varberg"), ("Typ", "Om- & tillbyggnad villa"), ("Beställare", "Privat"), ("År", "2021")],
         text=["I Träslövsläge, söder om Varberg, ligger villa Bankahall. Villan byggdes 1959, läget var ypperligt för fiskarfamiljen med närheten till fiskehamnen. Köket placerades ut mot gatan där man enkelt kunde vinka till grannarna när man var i land, att baksidan hade en fantastisk havsutsikt brydde man sig inte lika mycket om. Huset stack ut på gatan med sin moderna eternitfasad och asymmetriska takform.",
               "Huset stannade i familjen till 2020. De nya ägarna föll också för läget, men denna gång var det baksidans havsutsikt som var det primära.",
               "Joakim kopplades in i ett tidigt skede för att skissa på en om- och tillbyggnad och fanns sedan med genom hela processen, från skiss och bygglovshandlingar till kontakt med byggare under byggnation.",
               "Visionen med ombyggnaden var att skapa en rumsupplevelse i sekvenser, från den ombonade, tillbyggda entréverandan, via den luftiga trapphallen för att sedan mötas av utsikten i samvarodelen.",
               "En våning upp tillskapades en tillbyggnad med slutdestinationen i biblioteket, ett rofyllt rum med utsikt först över viken som gett huset dess namn och vidare ut över Kattegatt."],
         gallery=[("MG_7425-1-beskuren.webp", ""), ("MG_7442_red.webp", ""), ("Planlosning-Bankahall.webp", "full plan"),
                  ("Bankahall-sektion.webp", "full plan"), ("MG_7444-1-beskuren.webp", ""), ("MG_7432-1.webp", "")]),
    dict(slug="rum-under-himlen", title="Rum under himlen", sub="Ombyggnad kyrkobyggnad", short="Ombyggnad Pingst, Katrineholm", cat="ovrigt",
         cover="Ombyggnad-kyrka.webp", hero="3D-kyrksal.webp",
         spec=[("Status", "Pågående, 2023–"), ("Omfattning", "Skissfas, vision, kalkylunderlag"), ("Plats", "Katrineholm")],
         text=["Pingstkyrkan i Katrineholm bildades 1916. Kyrkobyggnaden uppfördes 1933 och fick en större om- och tillbyggnad på 70-talet.",
               "Församlingen har nu under en längre tid sett behov av att uppdatera sina lokaler för dagens, och framtidens behov.",
               "Essens Arkitektur blev anlitade för att hjälpa församlingen i ombyggnadsprocessen, att se potentialen i det befintliga och utreda möjliga vägar framåt. Arbetet omfattade entrévåningen, med tyngdpunkt på kyrksalen.",
               "I kyrksalen ändras dagens svåranvända estrad i många etage till en lägre i ett plan. Detta ger ett tydligare fokus och ökad närhet i gudstjänstrummet. Rent praktiskt förbättras lokalerna i sin helhet genom förbättrad tillgänglighet, bättre flöden, mer samlade förrådsytor, nytt mötesrum, uppdaterad sidosal etc.",
               "Projektet är pågående, för tillfället i en vilande/processande fas."],
         extra='''<p class="eyebrow" style="margin-top:2.5rem">Tidig skiss och visionstext</p>
<p class="poem">Allt har sin plats, det finns rum för<br>allt som sker under himlen<br>Ett rum för födelse, ett rum för död<br>Ett rum för skratt, ett rum för gråt<br>Ett rum för sorg, ett rum för att dansa<br>Ett rum för tystnad, ett rum för jubel<br>I rummet skapas en mötesplats där vi får komma med hela oss<br>En plats där mötet med den Levande kan förvandla oss, hela oss<br>I rummet blir våra olikheter till ett ackord<br>Hjärtats ton blir del i symfonin som sträcker sig högre, längre, djupare<br>Allt får sin plats, i Rum under Himlen</p>
<h3 style="margin-top:2.5rem;margin-bottom:1rem">Kyrkoarkitektur – en specialkompetens</h3>
<p>Genom åren har vi varit delaktiga i såväl nybyggnads- som ombyggnadsprojekt för kyrkor inom Pingst, Equmenia samt Syrisk-ortodoxa kyrkan (inkluderat projekt utförda innan uppstart av Essens Arkitektur).</p>
<p>Behöver ni hjälp inom detta område, <a class="link" href="../kontakt.html">tveka inte att höra av er</a>.</p>''',
         gallery=[("Plan-Katrineholm-pingst.webp", "full plan"), ("Katrineholm-Pingst-skiss.webp", "full"),
                  ("Frihamnskyrkan.webp", "", "Frihamnskyrkan, Göteborg – lokal- och funktionsarbete samt arkitektjury (vinnande bidrag ritat av Elding Oscarson)."),
                  ("Syrisk-Ortodoxa-kyrkan-1.webp", "", "Syrisk-ortodoxa kyrkan i Tynnered – handläggande arkitekt under nybyggnationen.")]),
    dict(slug="ferrum", title="Brf Ferrum", sub="Nybyggnad av flerbostadshus", short="Flerbostadshus, Borås", cat="flerbostadshus",
         cover="Exterior_Filter.webp", hero="Jarnhattan_fasad1.webp",
         spec=[("Plats", "Borås"), ("Typ", "Nybyggnad av flerbostadshus"), ("Beställare", "RO Gruppen/Stadsporten"), ("År", "Färdigställt 2023")],
         text=["Brf Ferrum består av 66 lägenheter med en spridning från ettor på 35 kvm till vindsvåningar på ca 100 kvm.",
               "Utformningen är anpassad efter den sluttande tomten. Materialval och gestaltning förstärker en stadsmässig känsla samtidigt som projektet knyter an till platsens småskalighet genom att dela upp byggnaden i flera olika delar.",
               "För de boende blir uppdelningen av huset en fin kvalitet där de tre trapphusen får olika utseende och karaktär. I utformningen av lägenheterna har yteffektiva planlösningar kombinerats med en ljus och rymlig känsla. Det har åstadkommits genom att göra lägenheterna grunda med långsidan vänd mot fasaden.",
               '<span class="muted">Projektet utfört under tidigare anställning på Forum Arkitekter. Visualisering av Anton Edberg, Forum Arkitekter.</span>'],
         gallery=[("Exterior_Filter.webp", "full"), ("ex-lgh.webp", "full plan"), ("Foto-Ferrum-kopiera_mindre.webp", "full")]),
    dict(slug="kusken", title="Kv Kusken", sub="Nybyggnad kontor", short="Kontorsbyggnad, Mölndal", cat="kontor",
         cover="Kusken-3x4-8.webp", hero="Kusken-1-red.webp",
         spec=[("Plats", "Åby, Mölndal"), ("Typ", "Nybyggnad kontor"), ("Beställare", "Plusfastigheter/Byggfokus"), ("År", "2020"),
               ("Foto", '<a href="https://almerangfotografi.se/" target="_blank" rel="noopener">Hannes Almeräng</a>')],
         text=["I Mölndal, strax intill Åby travbana, ligger kvarteret Kusken.",
               "Husvolymen är uppdelad i sektioner som trappar sig följsamt efter gatans lutning. Byggnaden får en stark karaktär genom utformningen där en sockelvåning i tegel kombineras med svart korrugerad plåt som sömlöst fortsätter från övervåningen upp över det branta taket.",
               "På insidan möter man ljusa och flexibla kontorsytor. Kontoret mot södergaveln får en vindsvåning med mötesrum och takterrass med utsikt över Mölndal och Sisjön.",
               '<span class="muted">Projektet utfört under tidigare anställning på Forum Arkitekter.</span>'],
         gallery=[("Kusken-3x4-8.webp", "full"), ("Kusken-3x4-5.webp", ""), ("Kusken-3x4-6.webp", ""),
                  ("Fasadvy-pp33db1cj5y240fgj1bz05znr9tzozrvgr1y69fesg.webp", "full plan"),
                  ("Kusken-3x4-2.webp", ""), ("Kusken-1x1-2.webp", ""), ("Kusken-3x4-10.webp", ""), ("Kusken-3x4-12.webp", "")]),
    dict(slug="hemsjo", title="Villa Hemsjö", sub="Nyproduktion av villa", short="Nyproduktion, Hemsjö", cat="villor",
         cover="Villa-Hemsjo-4_3.webp", hero="Villa-Hemsjo-16_9.webp",
         spec=[("Status", "Under byggnation (beräknat färdigt 2026)"), ("Omfattning", "Skissarbete, bygglov, bygghandlingar"),
               ("Beställare", '<a href="https://www.ekabbygg.se/" target="_blank" rel="noopener">EKAB Bygg</a>')],
         text=["Villa Hemsjö är en nyproducerad villa i Hemsjö utanför Alingsås. Platsen erbjuder en lugn, lantlig idyll med milsvid utsikt i riktning mot Mjörn och Alingsås.",
               "Utformningen är skräddarsydd för att passa in på platsen och ta vara på de specifika förutsättningarna och utmaningarna. Husets form följer den sluttande tomtens naturliga höjdkurvor.",
               "Planlösningen har en tydlig uppdelning mellan en social del med samvaro och kök och en mer privat del med sovrum och separat allrum.",
               "Genom placeringen av de sociala delarna bildas en ’länk’ med uteplatser på båda sidorna: både mot den skyddade gårdssidan i söder och mot utsikten och solnedgången över Mjörn.",
               "Projektet är ett samarbete med EKAB Bygg, huset är under byggnation och kommer ut på marknaden vid färdigställandet 2026."],
         gallery=[("Villa-Hemsjo-plan.webp", "full plan"), ("Villa-Hemsjo-Interior.webp", ""), ("Hemsjo-Vy-Web.webp", "")]),
    dict(slug="hjortas", title="Hjortås Retreat", sub="Konvertering av lada", short="Om- & tillbyggnad, Sollebrunn", cat="villor ovrigt",
         cover="Hjortas-sidan-web.webp", hero="Hjortas-panorama-web.webp",
         spec=[("Typ", "Ombyggnad, tillbyggnad"), ("Omfattning", "Skissarbete, bygglov, bygghandlingar"), ("Plats", "Sollebrunn, Alingsås"),
               ("Beställare", "Privat"), ("Status", "Slutbesked 2024")],
         text=["I skogarna utanför Sollebrunn har Essens Arkitektur förvandlat en gammal lada till ett modernt fritidsboende med fokus på jakt och friluftsliv.",
               "Projektet omfattar både en ombyggnad och tillbyggnad, där den ursprungliga byggnaden har fått nytt liv som ett funktionellt och unikt fritidshus.",
               "Materialval och utformning är inspirerade av den befintliga ladan. Ambitionen och önskemålet var att skapa ett ombonat och rustikt, men samtidigt luftigt och modernt, fritidsboende. Resultatet är en modern skogsretreat, där man kan dra sig tillbaka efter en dag ute i naturen.",
               "Utformningen av de sociala ytorna skapar en tydlig kontrast mellan olika rumsligheter. Kök och matplats präglas av rymd och höjd medan de lägre, mer ombonade delarna inbjuder till att slå sig ner och njuta av både utsikten och värmen från brasan.",
               "Med genomtänkt fönstersättning, och noggrant utvalda utblickar i olika väderstreck, skapas kopplingar till den omgivande naturen och fint varierande ljusinsläpp över hela dygnet."],
         gallery=[("Hjortas-sidan-web.webp", "full"), ("Hjortas-Plan-1.webp", "plan"), ("Hjortas-Plan-2.webp", "plan"),
                  ("Hjortas-interior-web.webp", "full"),
                  ("Hjortas-front-sq-Before-web.webp", "", "Före"), ("Hjortas-front-square-web.webp", "", "Efter")]),
    dict(slug="lakaren", title="Kv Läkaren", sub="Detaljplanearbete", short="Detaljplan, Trollhättan", cat="flerbostadshus",
         cover="Kv-Lakaren-Gron-illustrationsplan.webp", hero="Lakaren-situationsplan-3D-View-3D-View-1_FotoSketcher.webp",
         spec=[("Plats", "Trollhättan"), ("Typ", "Detaljplanearbete"), ("Beställare", "Willhem & Kungsleden"), ("Status", "Under granskning")],
         text=["I anslutning till det gamla lasarettsområdet i Trollhättan pågår ett detaljplanearbete som bl.a. omfattar tillskott av ny bostadsbyggnation.",
               "Nya punkthus tillskapas i randen till ett skogsparti. Utformningen är gjord med avsikt att bevara befintlig grönska och snarare tillgängliggöra området och höja dess status som rekreationsområde.",
               "Lägenhetsfördelningen skapar en variation av boende. Samtliga lägenheter får goda kvaliteter som generösa balkonger och fönster i flera riktningar.",
               '<span class="muted">Projektet utfört under tidigare anställning på Forum Arkitekter.</span>'],
         gallery=[("Kv-Lakaren-Gron-illustrationsplan.webp", "full plan"), ("Lakaren-Punkthus-typplan.webp", "plan"), ("Lakaren-Punkthus.webp", "")]),
    dict(slug="glc", title="GLC Gårdsten", sub="Nybyggnad av logistikanläggning samt kontor", short="Logistikanläggning, Göteborg", cat="kontor",
         cover="Glc-web-1.webp", hero="Glc-web-1.webp",
         spec=[("Plats", "Gårdsten, Göteborg"), ("Typ", "Nybyggnad kontor/logistik"), ("Beställare", "Serneke"), ("År", "2016"),
               ("Foto", '<a href="https://www.almerangfotografi.se/" target="_blank" rel="noopener">Hannes Almeräng</a>')],
         text=["Nybyggnad av logistikanläggning samt kontor i Gårdsten, Göteborg.",
               '<span class="muted">Projektet utfört under tidigare anställning på Forum Arkitekter.</span>'],
         gallery=[("Glc-web-10.webp", "full")]),
    dict(slug="alsike", title="Alsike Klosterby", sub="Idéskiss – retreatstugor", short="Retreatstugor, Uppland", cat="ovrigt",
         cover="Eremitage-2_1-red.webp", hero="Eremitage-2_1-red.webp",
         spec=[("Plats", "Alsike, Uppland"), ("Typ", "Idéskiss"), ("Beställare", "Alsike Kloster (pro bono)"), ("År", "2016")],
         text=["I Alsike, mellan Stockholm och Uppsala, ligger sedan 1964 Alsike Kloster. Klostret har sedan lång tid fungerat som en fristad för människor på flykt.",
               "Sedan 2009 finns visioner för en expansion av verksamheten, att utveckla klostret till en klosterby där en blandning av verksamheter skapar möten för integration, ekologiskt boende, rekreation etc.",
               "Som ett bidrag till visionen jobbade Joakim under våren 2016 med att visualisera hur visionen skulle kunna byggas. Uppdraget skedde pro bono och i form av examensarbete i Arkitektur på Chalmers.",
               "En del av examensarbetet omfattade ett förslag på nybyggnad av eremitstugor för kortare enskilda retreater, med fokus på meditativ vandring inåt och uppåt."],
         gallery=[("Eremitage-kvadrat.webp", "full"), ("Planer-o-sektion-Eremitage.webp", "full plan"), ("Fasad-VertiEremit-2.webp", "full plan")]),
]
BY = {p["slug"]: p for p in PROJECTS}
CATS = [("alla", "Alla"), ("flerbostadshus", "Flerbostadshus"), ("villor", "Villor"), ("kontor", "Kontor/Industri"), ("ovrigt", "Övrigt")]

# ---------------------------------------------------------------- layout
NAV = [("index.html", "Hem"), ("projekt.html", "Projekt"), ("tjanster.html", "Tjänster"), ("info.html", "Om oss"), ("kontakt.html", "Kontakt")]


def page(path, title, desc, body, active="", og_img="Villa-Savelangen-bild-1-1_1.webp"):
    depth = path.count("/")
    r = "../" * depth
    links = "".join(f'<li><a href="{r}{h}"{" aria-current=page" if h == active else ""}>{t}</a></li>' for h, t in NAV)
    body = body.replace("{R}", r)
    out = f"""<!doctype html>
<html lang="sv">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{html.escape(desc)}">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:image" content="{r}{IMG}{og_img}">
<meta property="og:locale" content="sv_SE">
<link rel="icon" href="{r}{IMG}favicon.webp">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,300;0,400;0,500;1,300&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{r}assets/css/style.css">
</head>
<body>
<header class="site-header">
  <nav class="nav" aria-label="Huvudmeny">
    <a class="logo" href="{r}index.html" aria-label="Essens Arkitektur – startsida"><img src="{r}{IMG}logo.png" alt="Essens Arkitektur" width="190" height="60"></a>
    <ul>{links}</ul>
    <a class="btn btn-primary" href="{r}kontakt.html">Boka första möte {ARROW}</a>
    <button class="burger" aria-label="Meny" aria-expanded="false"><span></span><span></span></button>
  </nav>
</header>
<main>
{body}
</main>
<footer class="footer">
  <div class="wrap">
    <div class="footer-top">
      <div>
        <a class="logo" href="{r}index.html"><img src="{r}{IMG}logo.png" alt="Essens Arkitektur" width="190" height="60"></a>
        <p class="muted" style="max-width:34ch">Arkitektur som förenklar, förskönar och förvaltar. Arkitektkontor i Alingsås – verksamma i hela Västsverige.</p>
      </div>
      <div><h4>Sidor</h4><ul>{"".join(f'<li><a href="{r}{h}">{t}</a></li>' for h, t in NAV[1:])}</ul></div>
      <div><h4>Kontakt</h4><ul><li><a href="mailto:kontakt@essensarkitektur.se">kontakt@essensarkitektur.se</a></li><li><a href="tel:+46733998880">0733-99 88 80</a></li><li><a href="https://www.instagram.com/essensarkitektur/" target="_blank" rel="noopener">Instagram</a></li></ul></div>
      <div><h4>Adress</h4><p>Brasegatan 23<br>441 65 Alingsås</p></div>
    </div>
    <div class="footer-bottom"><span>© Sätterman Essens Arkitektur AB · Org.nr 559379-2764</span><span>Arkitekt SAR/MSA</span></div>
  </div>
{ELEVATE_CREDIT}</footer>
<script src="{r}assets/js/main.js" defer></script>
</body>
</html>
"""
    dest = ROOT / path
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(out, encoding="utf-8")


def card(p, cls="", r="{R}"):
    return f'''<a class="card reveal {cls}" href="{r}projekt/{p["slug"]}.html" data-cat="{p["cat"]}">
  <div class="img"><img src="{r}{IMG}{p["cover"]}" alt="{p["title"]}" loading="lazy"></div>
  <div class="meta"><div><h3>{p["title"]}</h3><small>{p["short"]}</small></div><span class="arrow">{ARROW_UR}</span></div>
</a>'''


CTA = f'''<section class="cta reveal">
  <img src="{{R}}{IMG}Hjortas-panorama-web.webp" alt="" loading="lazy">
  <div class="wrap">
    <span class="eyebrow" style="color:#e6d3bf">Går ni i byggtankar?</span>
    <h2>Låt oss ta det första steget tillsammans.</h2>
    <p>Ett första möte är alltid förutsättningslöst. Vi träffas gärna på platsen och går igenom era förutsättningar och önskemål.</p>
    <div class="btns"><a class="btn btn-light" href="{{R}}kontakt.html">Skicka projektförfrågan {ARROW}</a><a class="btn btn-ghost" href="tel:+46733998880">Ring 0733-99 88 80</a></div>
  </div>
</section>'''

# ---------------------------------------------------------------- home
home = f'''
<section class="hero">
  <div class="hero-inner">
    <img src="{{R}}{IMG}Villa-Savelangen-bild-2-4_3.webp" alt="Villa Sävelången, Ingared" fetchpriority="high">
    <a class="hero-tag" href="{{R}}projekt/savelangen.html">Aktuellt: Villa Sävelången →</a>
    <div class="hero-content">
      <div>
        <span class="eyebrow" style="color:#e6d3bf">Arkitektkontor i Alingsås</span>
        <h1>Arkitektur där vardagen får rum</h1>
      </div>
      <div>
        <p>Vi utformar byggnader med omsorg och generositet – platser som skapar förutsättningar för liv. För privatpersoner, företag och fastighetsutvecklare.</p>
        <div class="btns"><a class="btn btn-light" href="{{R}}kontakt.html">Boka ett första möte {ARROW}</a><a class="btn btn-ghost" href="{{R}}projekt.html">Se projekt</a></div>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="split top">
      <div class="reveal">
        <span class="eyebrow">Filosofi</span>
        <h2>Förenkla. Försköna. Förvalta.</h2>
      </div>
      <div class="reveal">
        <p class="lead">Hemmet, jobbet, fritiden – stora delar av livet utspelar sig i, eller kring, olika byggnader. Hur vi formar våra livsmiljöer påverkar hur vi lever våra liv.</p>
      </div>
    </div>
    <div class="values">
      <div class="value reveal"><span class="num">01</span><h3>Förenkla</h3><p>God arkitektur förenklar och skapar förutsättningar för liv – rum för möten, kreativitet och rekreation. Ofta är den mest rationella lösningen också den enklaste.</p></div>
      <div class="value reveal"><span class="num">02</span><h3>Försköna</h3><p>Väl utformade miljöer påverkar hur vi mår. Vi förskönar och förbättrar platsen där huset står, med omsorg om både helhet och detaljer.</p></div>
      <div class="value reveal"><span class="num">03</span><h3>Förvalta</h3><p>Varje hus vi ritar ska på bästa sätt förvalta de ekonomiska, sociala och ekologiska resurser som projektet tar i anspråk.</p></div>
    </div>
  </div>
</section>

<section style="padding-top:0">
  <div class="wrap">
    <div class="section-head">
      <div class="reveal"><span class="eyebrow">Utvalda projekt</span><h2>Från första skiss<br>till färdigt hus</h2></div>
      <a class="btn btn-ghost reveal" href="{{R}}projekt.html">Alla projekt {ARROW}</a>
    </div>
    <div class="grid">
      {card(BY["hjortas"], "wide")}
      {card(BY["ingared"])}
      {card(BY["kusken"])}
      {card(BY["hantverksgatan"], "wide")}
    </div>
  </div>
</section>

<section class="dark">
  <div class="wrap">
    <div class="split">
      <div class="rounded portrait reveal"><img src="{{R}}{IMG}Joakim-Essens.webp" alt="Joakim Sätterman, arkitekt SAR/MSA" loading="lazy"></div>
      <div class="reveal">
        <span class="eyebrow">Om Essens</span>
        <h2>En arkitekt med er hela vägen</h2>
        <p class="lead" style="margin-top:1.4rem">Essens Arkitektur drivs av Joakim Sätterman, arkitekt SAR/MSA. Vi ritar hus och utvecklar fastigheter åt både företag och privatpersoner – varje projekt utformas med lyhördhet och inlevelseförmåga.</p>
        <p class="muted" style="margin-top:1rem">Kompetens och engagemang gör oss till en samarbetspartner genom hela processen, från de första tankarna till färdigbyggt resultat.</p>
        <div class="facts">
          <div><b>10+</b><span>års erfarenhet</span></div>
          <div><b>2022</b><span>grundat i Alingsås</span></div>
          <div><b>SAR/MSA</b><span>Chalmers-utbildad</span></div>
        </div>
        <a class="btn btn-light" style="margin-top:36px" href="{{R}}info.html">Läs mer om oss {ARROW}</a>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="split top">
      <div class="reveal">
        <span class="eyebrow">Tjänster</span>
        <h2>Anlita arkitekt?</h2>
        <p class="lead" style="margin-top:1.4rem">Oavsett om det gäller ett attefallshus, en villa eller ett flerbostadshus hjälper vi er genom processen.</p>
        <a class="btn btn-primary" style="margin-top:2rem" href="{{R}}tjanster.html">Så går det till {ARROW}</a>
      </div>
      <ul class="service-list reveal">
        <li>Nybyggnad <span>Villa · Flerbostadshus · Kontor</span></li>
        <li>Ombyggnad &amp; tillbyggnad <span>Befintliga byggnader</span></li>
        <li>Bygglov &amp; bygganmälan <span>Ritningar &amp; ombud</span></li>
        <li>Förhandsbesked &amp; avstyckning <span>Obebyggda tomter</span></li>
        <li>Markanvisning, planbesked &amp; detaljplan <span>Fastighetsutveckling</span></li>
      </ul>
    </div>
  </div>
</section>

<section style="padding-top:0">
  <div class="wrap">
    <div class="price reveal">
      <div class="big">1–3<small>%</small></div>
      <div>
        <span class="eyebrow">Vad kostar det?</span>
        <h3 style="font-size:clamp(1.4rem,2.4vw,1.9rem);margin-bottom:.8rem">”Som några kvadratmeter”, brukar vi svara.</h3>
        <p class="muted">I många fall utgör vårt arvode 1–3 % av den totala byggkostnaden. Lyckas vi spara in några kvadratmeter, eller ger er mer kvalitet per kvadratmeter, tjänar ni snabbt in kostnaden.</p>
      </div>
    </div>
  </div>
</section>

{CTA}
'''
page("index.html", "Arkitekt Alingsås | Essens Arkitektur",
     "Essens Arkitektur i Alingsås ritar villor, flerbostadshus och kontor med omsorg. Arkitektur som förenklar, förskönar och förvaltar. Boka ett första möte.",
     home, "index.html")

# ---------------------------------------------------------------- projects list
filters = "".join(f'<button data-filter="{k}"{" class=active" if k == "alla" else ""}>{v}</button>' for k, v in CATS)
plist = f'''
<section class="page-hero">
  <div class="wrap">
    <span class="eyebrow">Projekt</span>
    <h1>Ett urval av våra projekt</h1>
    <p class="lead">Bostäder, kontor och industri, men även stadsbyggnad, fastighetsutveckling och kyrkor – från idéskiss till färdigställt hus.</p>
  </div>
</section>
<section style="padding-top:0">
  <div class="wrap">
    <div class="filters" role="group" aria-label="Filtrera projekt">{filters}</div>
    <div class="grid">{"".join(card(p, "half" if i < 2 else "") for i, p in enumerate(PROJECTS))}</div>
  </div>
</section>
{CTA}
'''
page("projekt.html", "Projekt | Essens Arkitektur",
     "Se ett urval av Essens Arkitekturs projekt: villor, flerbostadshus, kontor, kyrkor och detaljplaner i Västsverige.", plist, "projekt.html")

# ---------------------------------------------------------------- project pages
for i, p in enumerate(PROJECTS):
    prev, nxt = PROJECTS[i - 1], PROJECTS[(i + 1) % len(PROJECTS)]
    spec = "".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in p["spec"])
    figs = []
    for g in p["gallery"]:
        src, cls = g[0], g[1]
        cap = f"<figcaption>{g[2]}</figcaption>" if len(g) > 2 else ""
        figs.append(f'<figure class="reveal {cls}"><img src="{{R}}{IMG}{src}" alt="{p["title"]}" loading="lazy">{cap}</figure>')
    body = f'''
<section class="p-hero" style="padding-bottom:0">
  <div class="rounded"><img src="{{R}}{IMG}{p["hero"]}" alt="{p["title"]}" fetchpriority="high"></div>
</section>
<section style="padding-top:0">
  <div class="wrap">
    <div class="p-intro">
      <div class="p-text">
        <a class="link muted" href="{{R}}projekt.html" style="border:0;margin-bottom:1.6rem;font-weight:400">← Alla projekt</a>
        <h1>{p["title"]}</h1>
        <p class="sub">{p["sub"]}</p>
        {"".join(f"<p>{t}</p>" for t in p["text"])}
        {p.get("extra", "")}
      </div>
      <aside class="spec">
        <dl>{spec}</dl>
        <a class="btn btn-primary" href="{{R}}kontakt.html">Liknande projekt? Hör av er {ARROW}</a>
      </aside>
    </div>
    <div class="gallery">{"".join(figs)}</div>
    <nav class="pager" aria-label="Fler projekt">
      <a href="{prev["slug"]}.html"><small>Föregående</small><b>{prev["title"]}</b></a>
      <a href="{nxt["slug"]}.html"><small>Nästa</small><b>{nxt["title"]}</b></a>
    </nav>
  </div>
</section>
{CTA}
<div class="lb" role="dialog" aria-label="Bildvisning"><button aria-label="Stäng">×</button><img src="" alt=""></div>
'''
    desc = (p["text"][0][:150]).replace('"', "")
    page(f"projekt/{p['slug']}.html", f"{p['title']} | Essens Arkitektur", desc, body, "projekt.html", og_img=p["cover"])

# ---------------------------------------------------------------- services
services = [
    ("Nybyggnad", "Att bygga nytt kan omfatta allt från ett attefallshus eller en villa till större kommersiella projekt, som flerbostadshus, grupphusområden, kontor, industri etc. Vi utgår ifrån era unika behov och önskemål för att tillsammans förverkliga visionen."),
    ("Ombyggnad & tillbyggnad", "Ibland finns lösningen närmare till hands än en nybyggnad. Med utgångspunkt i det befintliga ser vi till att ta fram dess inneboende potential. Med precision adderar vi, eller tar bort, det som behövs för att byggnaden bättre ska möta dagens och framtidens behov. För företag hjälper vi till exempel till med kontors- och lokalanpassning och konverteringar, där t.ex. outnyttjade lokaler eller biytor kan få nytt liv som lägenheter."),
    ("Bygglov & bygganmälan", "Många projekt kräver ett bygglov, eller en bygganmälan. Vi hjälper till med tolkning av detaljplan, avstämningar med kommunen samt att ta fram de bygglovsritningar som behövs. I den mån ni önskar kan vi sedan vara ert ombud under bygglovsprocessen."),
    ("Förhandsbesked & avstyckningar", "Vill ni bebygga en obebyggd tomt utanför detaljplanerat område, eller stycka av en tomt, rekommenderas en ansökan om förhandsbesked. Även om detaljeringen ofta kan vara lägre än vid en bygglovsansökan bestäms mycket av potentialen i förhandsbeskedet. Vi hjälper till att skissa upp förutsättningarna, producerar de ritningar som behövs och finns med i kontakten med kommunen och övriga myndigheter."),
    ("Markanvisning, planbesked & detaljplaner", "Vi har stor erfarenhet av att hjälpa fastighetsutvecklare i tidiga skeden. Genom att vara lyhörda för er affärsmodell och era målsättningar kan vårt deltagande skapa stora värden. Vi har ofta god förförståelse för kommunens krav och ambitioner och i dialog kan vi utforma ett förslag som alla vinner på."),
]
svc = "".join(f'<div class="service reveal{" span" if i == 4 else ""}"><h3><span>0{i+1}</span>{html.escape(t)}</h3><p>{d}</p></div>' for i, (t, d) in enumerate(services))
tj = f'''
<section class="page-hero">
  <div class="wrap">
    <div class="split">
      <div>
        <span class="eyebrow">Tjänster</span>
        <h1>Vi ritar hus åt företag och privatpersoner</h1>
        <p class="lead">Här beskriver vi hur vi arbetar för att förverkliga våra kunders byggprojekt. Är ni ett företag – hör av er så berättar vi mer om hur vi kan hjälpa er.</p>
        <a class="btn btn-primary" style="margin-top:2rem" href="{{R}}kontakt.html">Kontakta oss {ARROW}</a>
      </div>
      <a class="rounded portrait reveal" href="{{R}}projekt/hemsjo.html"><img src="{{R}}{IMG}Hemsjo-Vy-Web.webp" alt="Villa Hemsjö"></a>
    </div>
  </div>
</section>
<section style="padding-top:0"><div class="wrap"><div class="services">{svc}</div></div></section>

<section style="padding-top:0">
  <div class="wrap">
    <div class="split">
      <div class="reveal">
        <span class="eyebrow">Anlita arkitekt – en nybörjarguide</span>
        <h2>Arkitektritat är en prisvärd investering</h2>
        <p class="lead" style="margin-top:1.4rem">Att stå inför ett husbygge är en ovan situation för många. Valet av arkitekt görs tidigt och har en avgörande påverkan på slutresultatet.</p>
        <p class="muted" style="margin-top:1rem">Att välja rätt är inte enbart att ta in offerter och välja den billigaste. För att möta era förväntningar krävs det att vi är lyhörda och tar tid att förstå era behov och prioriteringar. När förutsättningarna blir tydligare blir också resultatet effektivare – mer konkret: ett bättre, effektivare och mer prisvärt hus.</p>
        <p class="muted">Ett bra arkitektritat hus är inte en lyxvara för några få, utan en livskvalitet som ska vara tillgänglig oavsett om man bor i en hyreslägenhet, BRF eller villa.</p>
      </div>
      <div class="grid reveal" style="grid-template-columns:1fr 1fr">
        <a class="rounded" href="{{R}}projekt/hantverksgatan.html" style="grid-column:1/-1;aspect-ratio:5/4"><img src="{{R}}{IMG}240417-Fasad-pres-5_4.webp" alt="Hantverksgatan 18, Alingsås" loading="lazy"></a>
      </div>
    </div>
  </div>
</section>

<section style="padding-top:0">
  <div class="wrap">
    <div class="price reveal">
      <div class="big">1–3<small>%</small></div>
      <div>
        <span class="eyebrow">Vad kostar det att anlita en arkitekt?</span>
        <h3 style="font-size:clamp(1.4rem,2.4vw,1.9rem);margin-bottom:.8rem">Så då rakt på sak: som några kvadratmeter.</h3>
        <p class="muted">Ser man till vad det normalt kostar att bygga nytt motsvarar vårt arvode inte många kvadratmeter. Därför är skissprocessen och förarbetet något som konkret lönar sig i längden: lyckas vi spara in några kvadratmeter, eller ger er mer kvalitet per kvadratmeter, tjänar ni snabbt in på att anlita oss. Alla projekt är olika, men i många fall utgör vårt arvode 1–3 % av den totala byggkostnaden.</p>
      </div>
    </div>
  </div>
</section>

<section class="dark">
  <div class="wrap">
    <div class="section-head">
      <div><span class="eyebrow">Vad är första steget?</span><h2>Tre steg till start</h2></div>
      <a class="btn btn-light" href="{{R}}kontakt.html">Boka första mötet {ARROW}</a>
    </div>
    <div class="steps">
      <div class="step reveal"><h3>Ett första möte</h3><p>Vi träffas, förslagsvis på platsen, och går igenom förutsättningar och önskemål.</p></div>
      <div class="step reveal"><h3>Projektförslag &amp; budget</h3><p>När vi förstått era önskemål tar vi fram ett förslag på arbetsupplägg samt tids- och kostnadsuppskattning.</p></div>
      <div class="step reveal"><h3>Arbetet kan börja</h3><p>Efter ert godkännande kan samarbetet påbörjas!</p></div>
    </div>
  </div>
</section>
<section style="padding-bottom:0"></section>
{CTA}
'''
page("tjanster.html", "Tjänster – anlita arkitekt | Essens Arkitektur",
     "Nybyggnad, ombyggnad, bygglov, förhandsbesked och detaljplaner. Så går det till att anlita Essens Arkitektur – och vad det kostar.", tj, "tjanster.html")

# ---------------------------------------------------------------- info
info = f'''
<section class="page-hero">
  <div class="wrap">
    <div class="split">
      <div>
        <span class="eyebrow">Om oss</span>
        <h1>Lokal förankring, bred erfarenhet</h1>
        <p class="lead">Essens Arkitektur har sin bas i Alingsås. Arbetsområdet omfattar större delen av Västsverige – inom våra specialområden även längre än så.</p>
      </div>
      <div class="rounded portrait reveal"><img src="{{R}}{IMG}Joakim-Essens-Front.webp" alt="Joakim Sätterman, arkitekt SAR/MSA"></div>
    </div>
  </div>
</section>
<section style="padding-top:0">
  <div class="wrap">
    <div class="split top">
      <div class="reveal"><span class="eyebrow">Joakim Sätterman</span><h2>Arkitekt SAR/MSA</h2></div>
      <div class="reveal">
        <p>Företaget drivs av Joakim Sätterman, arkitekt SAR/MSA. Innan han grundade företaget 2022 arbetade han i åtta år på ett större arkitektkontor, med ansvar för projekt samt ledningsuppgifter.</p>
        <p>Vi har en bred <a class="link" href="{{R}}projekt.html">projekterfarenhet</a>, främst bostäder och kontor/industri men även stadsbyggnad/fastighetsutveckling, förskolor, <a class="link" href="{{R}}projekt/rum-under-himlen.html">kyrkor</a> etc.</p>
        <p>Joakim har en utbildning i Arkitektur &amp; Teknik från Chalmers Tekniska Högskola, vilket utöver en masterexamen i Arkitektur &amp; Stadsbyggnad även innefattar ingenjörsutbildning inom konstruktion, byggnadsfysik, akustik etc.</p>
      </div>
    </div>
  </div>
</section>
<section class="dark">
  <div class="wrap">
    <div class="split top">
      <div class="reveal"><span class="eyebrow">Filosofi</span><h2>Att fånga arkitekturens essens</h2></div>
      <p class="lead reveal">Arkitektur har kraften att möta människans grundläggande behov genom väl genomtänkta byggnader och miljöer. För att uppnå detta arbetar vi utifrån tre ledord: Förenkla, Försköna &amp; Förvalta.</p>
    </div>
    <div class="steps" style="margin-top:56px;counter-reset:s">
      <div class="step reveal"><h3>Förenkla</h3><p>God arkitektur kan förenkla människors vardag, skapa förutsättningar för möten och trivsel, rum för både kreativitet och rekreation.</p><p style="margin-top:1em">Förenkla kan också gälla själva utformningen, där den mest rationella lösningen ofta är den enklaste – ur ekonomiska, funktionella, tekniska och estetiska perspektiv.</p></div>
      <div class="step reveal"><h3>Försköna</h3><p>Studier visar att väl utformade miljöer påverkar hur vi mår! Vi strävar därför efter att våra projekt ska försköna och förbättra.</p><p style="margin-top:1em">Detta innefattar omsorg om både helhet och detaljer, en inlevelse i hur människor använder byggnaderna och hur platsens potential kan lyftas fram och utvecklas.</p></div>
      <div class="step reveal"><h3>Förvalta</h3><p>Varje projekt börjar med ett förtroende från våra kunder, vilket vi förvaltar genom att lyhört anpassa oss till projektets ekonomiska, tekniska och funktionella förutsättningar.</p><p style="margin-top:1em">Vårt ansvar går dock längre än den direkta beställaren. Vi värnar om projektets hållbarhet och ser till ekologiska, sociala och ekonomiska aspekter för att skapa en hållbar helhet.</p></div>
    </div>
  </div>
</section>
<section style="padding-bottom:0"></section>
{CTA}
'''
page("info.html", "Om oss | Essens Arkitektur", "Essens Arkitektur drivs av Joakim Sätterman, arkitekt SAR/MSA, med bas i Alingsås. Läs om vår filosofi: förenkla, försköna, förvalta.", info, "info.html")

# ---------------------------------------------------------------- contact
types = ["Nybyggnad", "Om-/tillbyggnad", "Bygglov", "Förhandsbesked", "Fastighetsutveckling", "Annat"]
chips = "".join(f'<input type="checkbox" id="t{i}" name="typ" value="{t}"><label for="t{i}">{t}</label>' for i, t in enumerate(types))
kontakt = f'''
<section class="page-hero" style="padding-bottom:40px">
  <div class="wrap">
    <span class="eyebrow">Kontakt</span>
    <h1>Går ni i byggtankar?</h1>
    <p class="lead">Hör gärna av er så diskuterar vi hur vi kan hjälpa er vidare. Det första mötet är alltid förutsättningslöst.</p>
  </div>
</section>
<section style="padding-top:0">
  <div class="wrap">
    <div class="contact-grid">
      <div class="contact-info reveal">
        <div class="rounded" style="aspect-ratio:4/3"><img src="{{R}}{IMG}A9A0255-55.webp" alt="Essens Arkitektur" style="object-position:center 30%"></div>
        <dl>
          <div><dt>E-post</dt><dd><a href="mailto:kontakt@essensarkitektur.se">kontakt@essensarkitektur.se</a></dd></div>
          <div><dt>Telefon</dt><dd><a href="tel:+46733998880">0733-99 88 80</a></dd></div>
          <div><dt>Instagram</dt><dd><a href="https://www.instagram.com/essensarkitektur/" target="_blank" rel="noopener">@essensarkitektur</a></dd></div>
          <div><dt>Adress</dt><dd>Sätterman Essens Arkitektur AB<br>Brasegatan 23, 441 65 Alingsås</dd></div>
          <div><dt>Org.nr</dt><dd>559379-2764</dd></div>
        </dl>
      </div>
      <form class="form reveal" id="forfragan">
        <h2>Projektförfrågan</h2>
        <p class="muted">Berätta kort om ert projekt – vi återkommer inom kort.</p>
        <label>Vad gäller det?</label>
        <div class="chips">{chips}</div>
        <div class="row">
          <div><label for="namn">Namn *</label><input id="namn" name="namn" required autocomplete="name"></div>
          <div><label for="epost">E-post *</label><input id="epost" name="epost" type="email" required autocomplete="email"></div>
        </div>
        <div class="row">
          <div><label for="telefon">Telefonnummer</label><input id="telefon" name="telefon" type="tel" autocomplete="tel"></div>
          <div><label for="adress">Adress / plats för projektet</label><input id="adress" name="adress"></div>
        </div>
        <label for="beskrivning">Projektbeskrivning *</label>
        <textarea id="beskrivning" name="beskrivning" required placeholder="T.ex. typ av byggnad, ungefärlig storlek, tidplan och vad ni behöver hjälp med."></textarea>
        <button class="btn btn-primary" type="submit">Skicka förfrågan {ARROW}</button>
        <p class="note">Vi svarar normalt inom ett par arbetsdagar.</p>
      </form>
    </div>
  </div>
</section>
'''
page("kontakt.html", "Kontakt | Essens Arkitektur", "Kontakta Essens Arkitektur i Alingsås. Skicka en projektförfrågan eller ring 0733-99 88 80.", kontakt, "kontakt.html")
print("built", 5 + len(PROJECTS), "pages")
