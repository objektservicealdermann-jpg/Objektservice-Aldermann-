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
- **Steuer:** umsatzsteuerpflichtig. USt-IdNr. (zugleich W-IdNr.): **DE465887336** (seit 19.10.2026) – steht im Impressum und gehört auf jede Rechnung. Steuernummer und persönliche Steuer-ID nie veröffentlichen.

## Wichtige Regeln
- Bestandskunden (z. B. Hotels) **nicht** als Referenz auf der Website oder in Werbung nennen.
- Keine E-Mails ohne ausdrückliche Freigabe versenden. Vor jeder E-Mail IMMER fragen: „Als Entwurf ablegen oder direkt senden?“ (Wunsch des Inhabers, 19.11.2026). Ohne Antwort: nur als Entwurf ablegen.
- JEDE E-Mail (Entwurf oder Versand) bekommt IMMER die freigegebene HTML-Signatur aus `buero/email-signatur.html` mit beiden Logos als Inline-Anhang (siehe Abschnitt „E-Mail-Signatur“). Ohne Signatur keine E-Mail.
- Anrede in E-Mails, Briefen und Angeboten an Firmen IMMER: „Sehr geehrtes Team der [Firmenname],“ bzw. „Sehr geehrtes Team von [Firmenname],“ – keine Einzelpersonen, kein „Damen und Herren“ (Wunsch des Inhabers, 19.11.2026).
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

## Aktueller Fokus (Entscheidung des Inhabers, 19.11.2026)
- Erst den eigenen Betrieb vernünftig aufbauen – mit Mitarbeitern (mehr Pflegeobjekte, Team, feste Touren). Plattform und weitere Geschäftsideen danach (`buero/geschaeftsideen.md`).

## Zukunftsideen des Inhabers (nicht jetzt umsetzen)
- Arbeitsname der Plattform: **Fairfix** (gefällt dem Inhaber; Marke/Domain noch prüfen). Details: `buero/plattform-konzept.md`.
- Eigene Vermittlungsplattform für Aufträge (ähnlich MyHammer), aber besser und regional. Idee vom 19.11.2026, „weite Zukunft“. Bei Gelegenheit gemeinsam ein Konzept entwickeln (Zielgruppe, Startregion, Geschäftsmodell, Recht).

## E-Mail-Signatur
- Vorlage: `buero/email-signatur.html` – nebeneinander: Name/Inhaber/Objektservice links, roter Strich genau so hoch wie das Logo (66 px), Logo rechts OHNE Hintergrund, Kontaktdaten darunter.
- Zwei Logos: `LOGO_LIGHT` = `public/img/signatur-logo-hell.png` (dunkle Schrift, feine weiße Kontur – Standard, auch für Gmail), `LOGO_DARK` = `public/img/signatur-logo-dunkel.png` (weiße Schrift, wird per Dark-Mode-CSS in Apple Mail/Outlook eingeblendet). In Gmail-Entwürfen: `cid:att0` (hell) und `cid:att1` (dunkel) als Inline-Anhänge.
- Alle E-Mail-Entwürfe (HTML) mit dieser Signatur, Schrift Arial 14px. In E-Mails darf der volle Name stehen.
- Eigene E-Mail-Adresse (z. B. info@objektservicealdermann.com) über das bereits bezahlte Google Workspace einrichten; Gmail-Adresse weiterleiten; ggf. Tarif Business Starter. Erinnerung am 26.11.2026 geplant. Danach Website, Signatur, Impressum, Google-Profil, Instagram umstellen.
- Übersichtsseite des Büro-Teams: https://claude.ai/artifact/W38Nw8br4WR5kmitDEt6uW (Vorlage buero/buero-team-vorlage.html; bei neuen/geänderten Helfern aktualisieren).

## Rechnungen
- Generator: `buero/rechnungen/rechnung-erstellen.py <daten.json> <ausgabe.html> buero/rechnungen/logo.png`, danach mit Chromium als A4-PDF drucken (printBackground, Ränder 0). Layout = Vorlage des Inhabers (roter Kopf, Meta-Leiste, VON/AN/Zu bezahlen, Ausführungsort, Positionen, Summen, Bankverbindung).
- Preise sind kundenabhängig. Üblicher Stundensatz des Inhabers: 40–60 € netto. Stammkunde Hotel (Rechnungen R-01xx): bisher 32–33 €/Std., ab Rahmenvertrag (Angebot AGB-0101 vom 19.11.2026) 36,00 €/Std., Anfahrt Zone 2 = 25,00 €. Nächste Angebotsnummer: AGB-0105 (AGB-0102/0103 = finale Angebote HG, AGB-0104 = Objekt Ludwigsallee 148 Aachen, alle 19.11.2026). Neues Angebotsdesign (weiß, roter Balken, Leistungskarten, Preisbox) seit AGB-0104 – Inhaber wollte anderes Design. Hotel-Vorgaben: max. 600 € netto pro Rechnung (wegen Freigabe/Rückstellung); Ansprechpartner vor Ort ist der Haustechniker (koordiniert nur, entscheidet nicht über Verträge). Bei neuen Kunden IMMER vorher den Preis beim Inhaber erfragen, nie selbst festlegen. Anfahrtszonen und Materialaufschlag noch offen. 19 % USt, Zahlungsziel 7 Tage, Überweisung. Letzte Nummer: R-0140 (17.11.2026, neu ausgestellt 19.11.2026) → nächste R-0141 (R-0139 vorher beim Inhaber prüfen). Neues Rechnungsdesign (weiß, roter Balken, dunkle Betragsbox) seit R-0140 – Wunsch des Inhabers.
- Kunden- und Bankdaten NICHT in dieses öffentliche Repository schreiben; aus der letzten gesendeten Rechnung (Gmail) übernehmen, bis das Repo privat ist.
- Auf jede Rechnung: „USt-IdNr.: DE465887336“ (Pflichtangabe nach § 14 UStG, erfüllt durch die USt-IdNr.).
- Rechnung als Gmail-Entwurf mit Signatur an die Kreditoren-Adresse des Kunden vorbereiten, nie selbst senden.
- Angebote: Jedes Objekt/Haus bekommt ein EIGENES Angebot (auch wenn Häuser nebeneinander liegen) – Häuser laufen separat. Heckenschnitt IMMER pro laufendem Meter abrechnen, nie pro Stunde. Angebote mit fester Monatspauschale und Häufigkeiten je Leistung (Beispiel-Layout: Rechnungsstil mit rotem Kopf).
