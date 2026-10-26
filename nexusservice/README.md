# Nexus Service AB – webbplats

Statisk webbplats i fem sidor: `index.html`, `tjanster.html`, `fastighet.html` (fastighetsägare & BRF), `om.html`, `kontakt.html`.

- **Sidorna genereras från `build.py`.** Ändra text, tjänster, årshjul eller kontaktuppgifter där och kör `python3 build.py`.
- `assets/style.css` – Source Sans 3, vit bakgrund, logotypens orange i rubriker och knappar.
- `assets/app.js` – meny, tjänstemeny och offertformulär.
- `img/logo.svg` – N-symbolen ritad om som vektor.

## Designprinciper (mot "AI-slop")
Förebilden är hur svenska bygg- och fastighetsbolag faktiskt ser ut (Peab, Coor, Skanska), inte designtrender:
- Inga etiketter ovanför varje rubrik, ingen numrering 01–10, inga koordinater eller jätteordmärken.
- Inga scrollanimationer, inga mörka helskärmshjältar, ingen ultratight jättetypografi.
- Rubriker säger vad sidan handlar om ("Bygg, renovering och fastighetsservice i Stockholm"), ingångar är frågor kunden har ("Ska du renovera?").
- Texten är hela meningar, främst företagets egen beskrivning. Inga påhittade siffror, citat eller certifieringar.
- Tjänster i dragspelslista och årsplan som vanlig tabell, alltså innehåll före dekoration.

## Kontrollera innan publicering
- Telefonnumret `076-123 45 67` (ser ut som ett exempelnummer på flygbladet).
- Årsplanen och avtalsformerna på `fastighet.html` är förslag.
- Formuleringar om ROT/RUT ("kan gälla").
- Lägg gärna till organisationsnummer och F-skatt i sidfoten.

## Bilder – viktigast att byta
Bilderna är fotografier från Unsplash (fri kommersiell användning). De är generiska och det är fortfarande det
som mest avslöjar en mall. **Byt dem mot egna foton** på personal i Nexus-kläder, bilen och verkliga uppdrag i Stockholm.
Takarbeten och underhåll visas utan bild tills egna foton finns (sätt `img` i `SERVICES` i `build.py`).

## Offertformuläret
Öppnar besökarens e-postprogram med förfrågan ifylld till info@nexusserviceab.se. Länkar kan förifylla det:
`kontakt.html?kund=brf&tjanst=maleri`. Koppla till Formspree eller Netlify Forms för att skicka direkt.
