# Nexus Service AB – webbplats

Statisk webbplats i fem sidor: `index.html`, `tjanster.html`, `fastighet.html` (fastighetsägare & BRF), `om.html`, `kontakt.html`.

- **Sidorna genereras från `build.py`.** Ändra text, tjänster, årshjul eller kontaktuppgifter där och kör `python3 build.py`.
- `assets/style.css` – designsystem: Schibsted Grotesk, svart/off-white, logotypens orange som enda accent, raka hörn och hårfina linjer.
- `assets/app.js` – megameny, mobilmeny, tjänsteindex med bildförhandsvisning, innehållsförteckning och offertformulär.
- `img/logo.svg` – N-symbolen ritad om som vektor.

## Innehåll
All text bygger på företagets egen beskrivning och flygbladet (tjänster, slogan, fyra värdeord, kontaktuppgifter).
Inga påhittade siffror, kundcitat eller certifieringar. **Kontrollera innan publicering:**
- Telefonnumret `076-123 45 67` (ser ut som ett exempelnummer på flygbladet).
- Upplägget "Skötselavtal / Säsongsavtal / Underhållsprojekt" och årshjulet på `fastighet.html` är förslag.
- Formuleringar om ROT/RUT ("kan gälla") och "svarar normalt inom en arbetsdag".
- Lägg gärna till organisationsnummer, F-skatt och ansvarsförsäkring i sidfoten när uppgifterna finns.

## Offertformuläret
Formuläret öppnar besökarens e-postprogram med en ifylld förfrågan till info@nexusserviceab.se.
Länkar kan förifylla det: `kontakt.html?kund=brf&tjanst=maleri#offert`. Koppla till Formspree/Netlify Forms för att skicka direkt.

## Bilder
Riktiga fotografier från Unsplash (Unsplash-licensen, fri kommersiell användning), nedskalade till max 1600–2000 px.
Byt helst ut dem mot egna bilder från Nexus uppdrag när sådana finns – det stärker trovärdigheten mest av allt.
