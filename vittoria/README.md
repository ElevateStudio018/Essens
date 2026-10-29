# Vittoria Städ AB – webbplats

Statisk, responsiv one-page-sajt för ett städföretag. Typsnitt: Inter Tight (rubriker) och Inter (brödtext). Färger: mörk navy, varm off-white och ljusblå accent.

- `index.html` – alla sektioner: hero med video, löptext med tjänster, om oss, tjänster, arbetssätt, team, kunder, FAQ, kontakt och sidfot
- `assets/css/style.css` – stil och brytpunkter (1100 / 960 / 640 px)
- `assets/js/main.js` – mobilmeny, scroll-animationer, karusell för omdömen och kontaktformulär
- `assets/video/` – herovideo (1080p för dator, 720p för mobil) ihopklippt av sju klipp från Pexels (fri licens, fotograf Tima Miroshnichenko): 6195141, 6195524, 6196266, 6196269, 6195523, 6196262, 6197062
- `assets/img/` – bilder från Unsplash och Pexels (fri licens). `team-personal.webp` (Pexels 6195125) och `arbetssatt.webp` (Pexels 6197108) är från samma serie som videon. Byt gärna mot egna foton på personalen.

## Byt ut innan publicering (platshållare)

Det gick inte att hitta någon befintlig sajt för Vittoria Städ AB, så följande är platshållare:

- Telefon `070-000 00 00`, e-post `info@vittoriastad.se`, ort och öppettider (i `index.html` kontaktsektionen och sidfoten)
- `CONTACT_EMAIL` i `assets/js/main.js`
- Org.nr `000000-0000` i sidfoten
- Kundcitaten i sektionen "Vad våra kunder säger" – ersätt med riktiga omdömen
- Tjänsteutbud och FAQ-svar (RUT, garanti, försäkring) – kontrollera att de stämmer

Kontaktformuläret öppnar besökarens e-postprogram med förfrågan ifylld. Koppla det till t.ex. Formspree eller Netlify Forms för att skicka direkt.
