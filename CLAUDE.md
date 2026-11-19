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
Alle öffentlichen Dateien liegen im Ordner `public/` (nur dieser Ordner geht online).
- `index.html` – Startseite (Hero mit Video `video/hero.mp4`, Poster `img/hero-poster.jpg`)
- `leistungen/{gartenpflege,hausmeisterservice,reparatur-montage}/` – Leistungsseiten
- `leistungen/winterdienst/` – Winterdienst (Grafik `img/winterdienst-grafik.jpg`, kein echtes Foto – beim ersten Schnee echtes Foto vom Inhaber einbauen)
- `hausmeisterservice-{dueren,aachen,koeln,duesseldorf}/` – Städteseiten (eigene Texte, nicht kopieren)
- Startseite: saisonales Band `.season-band` unter dem Hero (Winter: Winterdienst; ab März: Gartenpflege-Abo; ab Oktober: Laub/Heckenschnitt)
- Google-Bewertung „5,0“ ist fest eingetragen (Startseite) – bei Änderungen der Bewertung anpassen
- `impressum/`, `datenschutz/`, `404.html`
- `css/style.css`, `js/main.js`, `img/`, `video/`, `sitemap.xml`, `robots.txt`, `_headers`
- Kopf- und Fußbereich sind in jeder HTML-Datei enthalten – Änderungen dort auf allen Seiten nachziehen.
- Keine externen Schriften, Skripte, Cookies oder Tracking (Datenschutz). Neue Dienste immer in `datenschutz/` ergänzen.
- Nach Änderungen `sitemap.xml` (lastmod) aktualisieren.

## Veröffentlichung & Technik
- **Cloudflare-Konto:** Login mit objektservicealdermann@gmail.com („Mit Google anmelden“). Worker **aldermann-website** (statische Dateien, `wrangler.jsonc`, Ordner `public/`), per Workers Builds mit GitHub verbunden – was auf **main** landet, geht automatisch online.
- **Adresse:** objektservicealdermann.com und www → Worker-Routen auf `aldermann-website` (DNS: AAAA `100::`, proxied). Zone in Cloudflare mit Nameservern george/stevie.ns.cloudflare.com (seit 19.11.2026).
- **E-Mail:** Google Workspace (MX smtp.google.com, SPF, DKIM in Cloudflare-DNS) – diese Einträge nie löschen.
- **Domain-Registrar:** Squarespace, gekauft über Google Workspace. Login bei Squarespace nur mit dem Workspace-Konto objektservicealdermann@objektservicealdermann.com („Mit Google fortfahren“).
- Alte Worker im Konto (objektservice-aldermann, delicate-cake-0577, broken-violet-25fe, purple-poetry-2f11) sind nicht mit der Adresse verbunden.
- Cloudflare-API: Token „Claude Website“ ist als Netzwerk-Geheimnis in der Claude-Umgebung hinterlegt (nie im Klartext speichern).

## Lernbuch
- `buero/lernbuch.md`: vor jedem Einsatz lesen, danach kurz eintragen, was gelernt wurde (ohne Kundendaten). Korrekturen des Inhabers als feste Regel hier in CLAUDE.md festhalten.

## Laufende Betreuung (Auftrag des Inhabers vom 19.11.2026)
Claude ist dauerhaft für Website, Google-Profil und Social Media zuständig: alles am Laufen halten, regelmäßig Abwechslung (Saison-Band, Fotos, Texte), wöchentlich Google-Beitrag (`marketing/google-beitraege.md`), Instagram-Inhalte (Beiträge + Stories) erstellen. KI-generierte Bilder nie als eigene Arbeitsfotos ausgeben – nur als erkennbare Grafiken.

## Schreibstil für Social Media & Google-Beiträge (Wunsch des Inhabers)
- Persönlich und natürlich, in der Wir-Form („wir“ = Objektservice Aldermann) – nicht nach Werbeagentur oder KI klingen.
- Keine Emoji-Aufzählungen, höchstens mal ein einzelnes Emoji. Keine Floskeln.
- Kunden siezen („Sie“). Unterschrift immer: „Ihr Team von Objektservice Aldermann“ + 0176 23751407. Nie den Namen des Inhabers als Unterschrift.
- Wenige Hashtags (max. ca. 8), ortsbezogen.

## Zukunftsideen des Inhabers (nicht jetzt umsetzen)
- Eigene Vermittlungsplattform für Aufträge (ähnlich MyHammer), aber besser und regional. Idee vom 19.11.2026, „weite Zukunft“. Bei Gelegenheit gemeinsam ein Konzept entwickeln (Zielgruppe, Startregion, Geschäftsmodell, Recht).

## E-Mail-Signatur
- Vorlage: `buero/email-signatur.html` (zentriert unter dem schwarzen Logo, roter Strich genau logobreit; `LOGO` durch `cid:att0` ersetzen und `public/img/signatur-logo.png` als Inline-Anhang mitgeben, oder später die URL https://www.objektservicealdermann.com/img/signatur-logo.png).
- Alle E-Mail-Entwürfe (HTML) mit dieser Signatur, Schrift Arial 14px. In E-Mails darf der volle Name stehen.
