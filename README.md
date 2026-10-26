# Essens Arkitektur – ny webbplats

Statisk, modern omarbetning av essensarkitektur.se. All text och alla bilder kommer från originalsajten.

- `index.html`, `projekt.html`, `tjanster.html`, `info.html`, `kontakt.html` + `projekt/*.html` (12 projekt)
- Typsnitt: Poppins (Google Fonts). Stil: `assets/css/style.css`. JS: `assets/js/main.js`
- Sidorna genereras från `build.py` – ändra text/projekt där och kör `python3 build.py`.
- Kontaktformuläret öppnar besökarens e-postklient med förfrågan ifylld till kontakt@essensarkitektur.se. Koppla till t.ex. Formspree/Netlify Forms för att skicka direkt.

Öppna `index.html` i webbläsaren, eller publicera mappen på valfri statisk hosting (Netlify, Vercel, GitHub Pages).
