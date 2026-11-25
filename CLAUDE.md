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
- **Steuer:** Umsatzsteuer-Status wird gerade mit dem Inhaber geklärt (Details NICHT ins öffentliche Repo, siehe Chat). Vor Änderungen an Rechnungen/Impressum den Inhaber fragen. USt-IdNr. (zugleich W-IdNr.): **DE465887336** (seit 19.10.2026) – steht im Impressum und gehört auf jede Rechnung. Steuernummer und persönliche Steuer-ID nie veröffentlichen.

## Wichtige Regeln
- Bestandskunden (z. B. Hotels) **nicht** als Referenz auf der Website oder in Werbung nennen.
- Keine E-Mails ohne ausdrückliche Freigabe versenden. Vor jeder E-Mail IMMER fragen: „Als Entwurf ablegen oder direkt senden?“ (Wunsch des Inhabers, 19.11.2026). Ohne Antwort: nur als Entwurf ablegen.
- JEDE E-Mail (Entwurf oder Versand) bekommt IMMER die freigegebene HTML-Signatur aus `buero/email-signatur.html` mit beiden Logos als Inline-Anhang (siehe Abschnitt „E-Mail-Signatur“). Ohne Signatur keine E-Mail.
- Anrede an Firmen (E-Mails, Briefe, Angebote), vor allem beim ersten Kontakt und wenn mehrere Leute mitlesen: „Sehr geehrtes Team der [Firmenname],“ bzw. „Sehr geehrtes Team von [Firmenname],“ – damit sich alle angesprochen fühlen und sich niemand übergangen fühlt; kein „Damen und Herren“. Persönliche Anrede nur, wenn wir eine Person gezielt anschreiben bzw. schon im persönlichen Kontakt sind (Wunsch des Inhabers, 19.11.2026).
- Keine unaufgeforderten Werbe-E-Mails an Firmen (UWG § 7); Akquise per Brief, Telefon, LinkedIn oder persönlich.
- Fotos vor dem Einbau verkleinern und Metadaten (GPS) entfernen.
- KEINE Preise auf der Website (Inhaber 23.11.2026) – Preise nur in Angeboten, Auftragsblättern und ggf. Kleinanzeigen. Auch nicht in strukturierten Daten/FAQ.
- SEO/Website: Claude darf Website-Änderungen selbstständig umsetzen und live stellen, muss den Inhaber aber jedes Mal kurz informieren, was geändert wurde (Inhaber 23.11.2026). Tabu ohne Rückfrage: Impressum, Datenschutz, rechtliche Texte; nie Bestandskunden nennen, keine erfundenen Zahlen/Bewertungen. Backup = Git-Historie.

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
- Website-Texte in der **Wir-Form** (seit 25.11.2026, Wunsch des Inhabers), nicht „ich“. Jan-Luca wird in der dritten Person genannt („Jan-Luca Aldermann ist gelernter Schreiner“). Fragen aus Kundensicht in FAQs („Kann ich …?“) und echte Bewertungen bleiben unverändert.
- Startseite: Logo-Animation oben im Hero (video/logo-intro.mp4, einmal pro Besuch, überspringbar).
- Kopf- und Fußbereich sind in jeder HTML-Datei enthalten – Änderungen dort auf allen Seiten nachziehen.
- Keine externen Schriften, Skripte oder Cookies (Datenschutz). Einzige Ausnahme seit 23.11.2026 (Inhaber-OK): Besucherstatistik PostHog cookieless (EU, Projekt 364742, Bibliothek selbst gehostet in `js/vendor/posthog.js`, Einbindung `js/stats.js`, zählt Seitenaufrufe + Klicks Anrufen/WhatsApp/E-Mail, steht in `datenschutz/` Abschnitt 4). Keine Session-Aufnahmen/Heatmaps/Autocapture einschalten. Neue Dienste immer in `datenschutz/` ergänzen.
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
- **Gilt für ALLE Helfer/Agenten und alle Texte, die Menschen lesen** (Instagram, Google, LinkedIn, Kleinanzeigen, Website, E-Mails, Briefe, Angebotsanschreiben): vorher den Skill `natuerlich-schreiben` anwenden (`.claude/skills/natuerlich-schreiben/`, Muster-Liste in `references/ki-muster.md`). Texte sollen menschlich klingen, nicht nach KI – z. B. keine langen Gedankenstriche, kein „nicht nur … sondern auch“, keine Dreierreihen, keine KI-Floskeln (Inhaber 25.11.2026).
- Persönlich und natürlich, in der Wir-Form („wir“ = Objektservice Aldermann) – nicht nach Werbeagentur oder KI klingen.
- Keine Emoji-Aufzählungen, höchstens mal ein einzelnes Emoji. Keine Floskeln.
- Kunden siezen („Sie“). Unterschrift immer: „Ihr Team von Objektservice Aldermann“ + 0176 23751407. Nie den Namen des Inhabers als Unterschrift.
- Wenige Hashtags (max. ca. 8), ortsbezogen.
- Reels: KEINE gezeichneten Strichmännchen-Videos mehr ohne vorherige Absprache (kamen nicht an, 19.11.2026); nie „Schreiner-Modus“ o. Ä. Vor neuen Reels Stil/Beispiel vom Inhaber holen, echte Aufnahmen bevorzugen.
- KEINE Preise auf Instagram (Beiträge, Stories, Reels) und auf der Website – Preise nur in Angeboten und Auftragsblättern (Wunsch des Inhabers, 19.11./23.11.2026).
- Stories mit Link: Windsor/API kann keine Link-Sticker setzen. Story-Bild dem Inhaber schicken, er postet in der Instagram-App mit Link-Sticker auf https://www.objektservicealdermann.com/...

## Ziel (Inhaber, 20.11.2026)
- **10.000 € netto Umsatz pro Monat.** Weg: ca. 6.000–7.000 € feste Monatspauschalen (10–12 Objekte à ~500–900 €) + Einzelaufträge; dafür ab ca. 4.000 € festen Pauschalen ersten Mitarbeiter (Minijob/Teilzeit) einplanen. Fortschritt im Wochenstart melden.

## Aktueller Fokus (Entscheidung des Inhabers, 19.11.2026)
- Erst den eigenen Betrieb vernünftig aufbauen – mit Mitarbeitern (mehr Pflegeobjekte, Team, feste Touren). Plattform und weitere Geschäftsideen danach (`buero/geschaeftsideen.md`).

## Zukunftsideen des Inhabers (nicht jetzt umsetzen)
- Arbeitsname der Plattform: **Fairfix** (gefällt dem Inhaber; Marke/Domain noch prüfen). Details: `buero/plattform-konzept.md`.
- Eigene Vermittlungsplattform für Aufträge (ähnlich MyHammer), aber besser und regional. Idee vom 19.11.2026, „weite Zukunft“. Bei Gelegenheit gemeinsam ein Konzept entwickeln (Zielgruppe, Startregion, Geschäftsmodell, Recht).

## E-Mail-Signatur
- Vorlage: `buero/email-signatur.html` – nebeneinander: Name/Inhaber/Objektservice links, roter Strich genau so hoch wie das Logo (66 px), Logo rechts OHNE Hintergrund, Kontaktdaten darunter.
- Zwei Logos: `LOGO_LIGHT` = `public/img/signatur-logo-hell.png` (dunkle Schrift, feine weiße Kontur – Standard, auch für Gmail), `LOGO_DARK` = `public/img/signatur-logo-dunkel.png` (weiße Schrift, wird per Dark-Mode-CSS in Apple Mail/Outlook eingeblendet). In Gmail-Entwürfen NUR das helle Logo als `cid:att0` (ohne Dark-Mode-CSS, ohne zweites Logo) – die Gmail-App zeigt beim Bearbeiten sonst beide Logos untereinander an (19.11.2026).
- Alle E-Mail-Entwürfe (HTML) mit dieser Signatur, Schrift Arial 14px. In E-Mails darf der volle Name stehen.
- Eigene E-Mail-Adresse (z. B. info@objektservicealdermann.com) über das bereits bezahlte Google Workspace einrichten; Gmail-Adresse weiterleiten; ggf. Tarif Business Starter. Erinnerung am 26.11.2026 geplant. Danach Website, Signatur, Impressum, Google-Profil, Instagram umstellen.
- Übersichtsseite des Büro-Teams: https://claude.ai/artifact/W38Nw8br4WR5kmitDEt6uW (Vorlage buero/buero-team-vorlage.html; bei neuen/geänderten Helfern aktualisieren).

## Tonnen-Erinnerungen (Wunsch des Inhabers, 20.11.2026)
- Sobald ein Objekt mit Tonnendienst beauftragt ist: Abfuhrplan holen (Stadt Aachen: abfallkalender.regioit.de/kalender-aachen, ICS-Download über downloadfile.jsp mit ort/strasse/hnr/fraktion-IDs) und für JEDEN Abfuhrtermin zwei Erinnerungen an den Inhaber planen (send_later): am Vortag nachmittags „Tonnen rausstellen“ und am Abfuhrtag „Tonnen zurückstellen“, inkl. Feiertagsverschiebungen. Jahreswechsel: neuen Kalender abrufen.
- Objekt Aachen (Angebot AGB-0105): Start erst ca. Mitte 2027 – dann aktuellen Abfuhrkalender holen und Erinnerungen anlegen.
- Objekte Jülich (AGB-0102/0103, beauftragt): Abfuhrbezirk 3 (Kalender Juli–Dez. 2026 von der Hausverwaltung per Mail). Erinnerungen für Dez. 2026 angelegt (14 Stück, 16:47 raus / 12:13 rein). Kalender 2027 Ende Dezember bei der Hausverwaltung anfordern und Erinnerungen ergänzen.

## Kommandozentrale
- Tagesübersicht für den Inhaber (Termine, Aufgaben, offene Angebote, Objekte, Weg zum 10.000-€-Ziel, Zahlen): https://claude.ai/artifact/5LHP11zr5rpgecwm4TUURj – Daten per ArtifactData (data/cc/termine, aufgaben, angebote, objekte, kennzahlen). Täglich 7:41 Uhr automatisch aktualisiert; bei neuen Angeboten/Zusagen/Terminen sofort nachtragen.

## Objektbuch
- Digitales Objektbuch (Einsätze, Mängel, Reparaturen, Tonnen, Winterdienst, Notizen je Objekt): https://claude.ai/artifact/5v9gYnBV7pY4h31w4JtikS – Daten per ArtifactData (Sammlungen `objekte`, `eintraege`). Grundlage für Monatsberichte an Kunden. Sprachnachrichten/Fotos des Inhabers dort eintragen.

## Rechnungsprogramm (Büro Aldermann)
- Private Seite https://claude.ai/artifact/NTKwHTu1YZKCLAVbra7dy3 – Übersicht (offen/überfällig, Umsatz, feste Pauschalen), Rechnungen, Angebote, Kunden; PDFs werden in der Seite angezeigt (pdf.js) und können aufs Handy gesichert werden. Daten per ArtifactData: `data/buero/rechnungen` (nr, kunde, datum, faellig, netto, brutto, status offen/bezahlt, bezahlt_am, file, text, notiz) und `data/buero/angebote` (nr, kunde, datum, netto, art, status offen/angenommen/abgelehnt/abgelaufen/ersetzt, file, text). PDFs sind Dateien der Seite (`files/NN-….pdf`, Quelle Scratchpad `ablage/`).
- Jede neue Rechnung/jedes neue Angebot SOFORT eintragen und das PDF als Seiten-Datei mitveröffentlichen; Zahlungseingänge/Zusagen nachtragen. Kunden-PDFs nie ins Repo.
- Frühe Rechnungen (Mai–Aug 2026) hatten keine eindeutigen Nummern (2026001/2026002) – in der Liste nach Datum benannt.

## Akquise
- Anrufliste Hausverwaltungen (Status/Notizen, db-Sammlung `anrufe`, Doc-ID = nr aus buero/hausverwaltungen.json): https://claude.ai/artifact/74sqdSFm1qDx98Tv7owhfv
- Texte (Bewertungsbitte mit Direktlink, Kleinanzeigen, Telefon-Leitfaden): `marketing/akquise-texte.md`. Google-Bewertungslink: https://search.google.com/local/writereview?placeid=ChIJa7bdtl4Bpy4Rbkde75itTR8

## Google Ads (seit 23.11.2026)
- Konto 351-164-8311 (Windsor connector google_ads). Kampagne „Aldermann – Jülich & Umgebung (Suche)“ id 24532303428: 5 €/Tag (vom Inhaber freigegeben, jederzeit kündbar), Klicks maximieren, max. 2 € pro Klick, 20 km um Jülich, Mo–Sa 7–19 Uhr, Deutsch. Anzeigengruppen Winterdienst (204797858280), Hausmeisterservice (201674650505) und Kleine Aufträge (205429430594, Montage/Reparatur/Laub/Entrümpelung, seit 24.11.2026), Anruf-Erweiterung, keine Preise. Automatische Kampagne „Performance Max-1“ (24474339346) am 24.11.2026 pausiert. Budget nie ohne ausdrückliches OK erhöhen; ab Mitte Februar Heckenschnitt/Gartenpflege vorschlagen.

## Rechnungen
- Generator: `buero/rechnungen/rechnung-erstellen.py <daten.json> <ausgabe.html> buero/rechnungen/logo.png`, danach mit Chromium als A4-PDF drucken (printBackground, Ränder 0). Layout = Vorlage des Inhabers (roter Kopf, Meta-Leiste, VON/AN/Zu bezahlen, Ausführungsort, Positionen, Summen, Bankverbindung).
- Preise sind kundenabhängig. Üblicher Stundensatz des Inhabers: 40–60 € netto. Stammkunde Hotel (Rechnungen R-01xx): bisher 32–33 €/Std., ab Rahmenvertrag (Angebot AGB-0101 vom 19.11.2026) 36,00 €/Std., Anfahrt Zone 2 = 25,00 €. Nächste Angebotsnummer: AGB-0108 (AGB-0107 = Winterdienst Gesamtobjekt 4 Häuser Jülich für eine Hausverwaltung, 24.11.2026: Saisonpauschale 240 € + 80 € nur Streuen + 139 € Räumen+Streuen pro Einsatz netto, inkl. Streugut/Anfahrt, mehrmals täglich einzeln berechnet; Vorgaben Stadt Jülich im Angebot; AGB-0106 = Jägerzaun-Erneuerung Im Vogelsang 2, neue Version 25.11.2026: 4.184 € netto (Material 1.850 €, 2,5 Arbeitstage, mit Fotos „Aktueller Stand vom Zaun“), vom Inhaber per WhatsApp verschickt; Material-Angebot mobau Hückelhoven ca. 909 € netto (vor Bestellung Element-Qualität und Torbreite klären); AGB-0102/0103 = HG, beauftragt 20.11.2026, von HG angepasst (Inhaber 25.11.2026): Haus mit Hecke (0102) Heckenschnitt nur bei Bedarf, Haus ohne Hecke (0103) Rasenschnitt nur auf Beauftragung; solange Baustelle/kein Bezug nur Kontrollgänge, Abrechnung nach tatsächlicher Leistung (Inhaber sagt monatlich, was gemacht wurde; Rasen ggf. nur halb berechnen); Haus mit Hecke (0102) fertig und Bezug ab 01.12.2026 (Pauschale ohne Hecke voraussichtlich 351,87 €), Haus ohne Hecke (0103) erst zum 01.02.2027 fertig – Kontrollgänge sind nicht vereinbart, bis dahin dort nichts zu tun/abzurechnen; Haus mit Hecke: alle 14 Tage Tonnen raus/rein und am selben Termin Treppenhaus putzen (eine Anfahrt); Winterdienst-Bereitschaft 65 €/Monat je Haus ab Dez. + 30 € je Einsatz laut Angebot; AGB-0104 ersetzt durch AGB-0105 = Objekt Ludwigsallee 139 Aachen, 674,58 € netto/Monat – Übernahme erst ca. Mitte 2027, weil der alte Vertrag so lange läuft (Info Frau Besch 25.11.2026); Frau Besch hat zusätzlich 5–6 größere Objekte in Düsseldorf in Aussicht gestellt, Besichtigung mit GaLaBau-Partner). Neues Angebotsdesign (weiß, roter Balken, Leistungskarten, Preisbox) seit AGB-0104 – Inhaber wollte anderes Design. Hotel-Vorgaben: max. 600 € netto pro Rechnung (wegen Freigabe/Rückstellung); Ansprechpartner vor Ort ist der Haustechniker (koordiniert nur, entscheidet nicht über Verträge). Bei neuen Kunden IMMER vorher den Preis beim Inhaber erfragen, nie selbst festlegen. Anfahrtszonen und Materialaufschlag noch offen. 19 % USt, Zahlungsziel 7 Tage, Überweisung. Letzte Nummer: R-0140 (17.11.2026, neu ausgestellt 19.11.2026) → nächste R-0141 (R-0139 vorher beim Inhaber prüfen). Neues Rechnungsdesign (weiß, roter Balken, dunkle Betragsbox) seit R-0140 – Wunsch des Inhabers.
- Kunden- und Bankdaten NICHT in dieses öffentliche Repository schreiben; aus der letzten gesendeten Rechnung (Gmail) übernehmen, bis das Repo privat ist.
- Steuern: Inhaber hat KEINEN Steuerberater (23.11.2026) und möchte, dass Claude Buchhaltung und Steuer-Vorbereitung übernimmt (Einnahmen/Ausgaben, Umsatzsteuer-Voranmeldung, Jahreserklärung vorbereiten). Abgabe über ELSTER macht der Inhaber selbst mit seinem Zugang; Claude gibt nur Zahlen und Klick-Anleitung. Unsichere Steuerfragen klar als „prüfen“ kennzeichnen.
- Auf jede Rechnung: „USt-IdNr.: DE465887336“ (Pflichtangabe nach § 14 UStG, erfüllt durch die USt-IdNr.).
- Rechnung als Gmail-Entwurf mit Signatur an die Kreditoren-Adresse des Kunden vorbereiten, nie selbst senden.
- Angebote: Jedes Objekt/Haus bekommt ein EIGENES Angebot (auch wenn Häuser nebeneinander liegen) – Häuser laufen separat. Heckenschnitt IMMER pro laufendem Meter abrechnen, nie pro Stunde (Spanne 6,50–15,00 € netto/lfd. m je nach Höhe, Breite, Zustand – Angabe des Inhabers 20.11.2026). Einzelaufträge mit viel Material (z. B. Zaunbau): Materialaufschlag 25 %, Anzahlung 35 % bei Auftragserteilung, Rest nach Fertigstellung – im Angebot NICHT dazuschreiben, wofür die Anzahlung ist (Inhaber 20.11.2026). Angebote mit fester Monatspauschale und Häufigkeiten je Leistung (Beispiel-Layout: Rechnungsstil mit rotem Kopf).
