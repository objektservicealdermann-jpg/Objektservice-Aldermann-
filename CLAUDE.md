# Objektservice Aldermann – Firmenprofil für Claude

Dieses Repository enthält die Website www.objektservicealdermann.com (statisches HTML, gehostet auf Cloudflare).
Kommunikation mit dem Inhaber immer auf Deutsch, einfach und ohne Fachjargon. Er arbeitet viel vom Handy aus.

## Betrieb
- **Firma:** Objektservice Aldermann (Einzelunternehmen, seit Mitte 2026)
- **Inhaber:** Jan-Luca Aldermann, gelernter Schreiner
- **Adresse:** Bretzelbäckerstraße 3, 52428 Jülich
- **Telefon / WhatsApp:** 0176 23751407
- **E-Mail:** objektservicealdermann@gmail.com
- **Einsatzgebiet:** Jülich, Kreis Düren, Aachen, Köln, Düsseldorf, Kreis Heinsberg, Mönchengladbach
- **Leistungen:** Hausmeisterservice/Objektbetreuung, Garten- und Grünpflege (Rasen, Hecken-/Formschnitt), Kleinreparaturen, Möbel-/Küchenmontage, Schreiner- und Montagearbeiten
- **Partner:** fester Garten- und Landschaftsbaubetrieb für größere Arbeiten
- **Ziel:** mehr Pflegeobjekte mit fester Monatspauschale (planbares Einkommen), Zielgruppe v. a. Hausverwaltungen, WEGs, Vermieter, Gewerbe
- **Steuer:** umsatzsteuerpflichtig, keine USt-IdNr. Steuernummer/Steuer-ID nie veröffentlichen.

## Wichtige Regeln
- Bestandskunden (z. B. Hotels) **nicht** als Referenz auf der Website oder in Werbung nennen.
- Keine E-Mails ohne ausdrückliche Freigabe versenden – immer als Entwurf vorbereiten.
- Keine unaufgeforderten Werbe-E-Mails an Firmen (UWG § 7); Akquise per Brief, Telefon, LinkedIn oder persönlich.
- Fotos vor dem Einbau verkleinern und Metadaten (GPS) entfernen.

## Website-Aufbau
- `index.html` – Startseite (Hero mit Video `video/hero.mp4`, Poster `img/hero-poster.jpg`)
- `leistungen/{gartenpflege,hausmeisterservice,reparatur-montage}/` – Leistungsseiten
- `impressum/`, `datenschutz/`, `404.html`
- `css/style.css`, `js/main.js`, `img/`, `video/`, `sitemap.xml`, `robots.txt`, `_headers`
- Kopf- und Fußbereich sind in jeder HTML-Datei enthalten – Änderungen dort auf allen Seiten nachziehen.
- Keine externen Schriften, Skripte, Cookies oder Tracking (Datenschutz). Neue Dienste immer in `datenschutz/` ergänzen.
- Nach Änderungen `sitemap.xml` (lastmod) aktualisieren.
