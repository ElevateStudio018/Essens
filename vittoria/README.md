# Vittoria Städ AB – webbplats

Statisk, responsiv one-page-sajt för ett städföretag. Typsnitt: Jost (rubriker och knappar), Fraunces (logotypen) och Source Sans 3 (brödtext). Färger: vit bakgrund, marinblå varumärkesfärg och mörk navy-sektion.

- `index.html` – sektioner: hero med video, om oss, därför Vittoria, tjänster, vanliga frågor, kontakt och sidfot
- `assets/css/style.css` – stil och brytpunkter (1080 / 860 / 560 px)
- `assets/js/main.js` – header vid scroll, mobilmeny och kontaktformulär
- `assets/video/` – herovideo (1080p för dator, 720p för mobil) ihopklippt av sju klipp från Pexels (fri licens, fotograf Tima Miroshnichenko): 6195141, 6195524, 6196266, 6196269, 6195523, 6196262, 6197062
- `assets/img/` – bilder från Unsplash (fri licens) och en stillbild ur videon som visas medan den laddar.

## Byt ut innan publicering (platshållare)

Det gick inte att hitta någon befintlig sajt för Vittoria Städ AB, så följande är platshållare:

- Telefon `070-000 00 00`, e-post `info@vittoriastad.se`, ort och öppettider (i `index.html` kontaktsektionen och sidfoten)
- `CONTACT_EMAIL` i `assets/js/main.js`
- Org.nr `000000-0000` i sidfoten
- Tjänsteutbud och FAQ-svar (garanti, försäkring, nyckelhantering) – kontrollera att de stämmer

Kontaktformuläret öppnar besökarens e-postprogram med förfrågan ifylld. Koppla det till t.ex. Formspree eller Netlify Forms för att skicka direkt.
