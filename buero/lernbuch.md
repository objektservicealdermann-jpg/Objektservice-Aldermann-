# Lernbuch des Büros

Hier schreibt jeder Helfer nach seinem Einsatz kurz rein, was er gelernt oder bemerkt hat.
Vor jedem Einsatz lesen. Keine Kundendaten (Namen, Adressen, Telefonnummern) – dieses Repository ist öffentlich.
Grundregeln stehen in CLAUDE.md und werden nur vom Inhaber geändert.

Format: `JJJJ-MM-TT · Helfer · Erkenntnis`

---

2026-11-19 · Einrichtung · Inhaber möchte Social-Media-Texte persönlich, Wir-Form, ohne Emoji-Listen, Unterschrift „Ihr Team von Objektservice Aldermann“.
2026-11-19 · Einrichtung · Inhaber will Instagram-Inhalte vor dem Posten sehen; gezeichnete Erklär-Videos mit Ton kommen gut an.
2026-11-19 · Einrichtung · Google-Profil hatte vor dem Start fast keine Aufrufe (2 in 30 Tagen) – Ausgangswert zum Vergleich.
2026-11-19 · Inhaber · Video-Idee mit Potenzial: „Wer findet den Fehler?“ – Fotos/Videos von typischen Fehlern an Objekten (falsch montiert, schlecht geschnitten, Gefahrenstellen). Ablauf: Bild zeigen + Countdown, dann Auflösung mit rotem Kreis, kurzer Erklärung und Tipp. Ohne erkennbare Adressen, Gesichter oder Firmennamen; nur mit Erlaubnis des Eigentümers. Bis echte Fotos da sind: gezeichnete Varianten.
2026-11-19 · Inhaber · Kein Werbebudget gewünscht. Hausverwaltungen immer persönlich anschreiben: „Sehr geehrtes Team von <Name der Hausverwaltung>“.
2026-11-19 · Postfach · Erster Lauf: Inhaber fragt auch selbst bei größeren Hausmeister-/Facility-Firmen nach Subunternehmer-Zusammenarbeit an – Antworten und Abwesenheitsnotizen nachhalten und an Rückmeldung erinnern. Viel Rauschen durch Job-Mails (HeyJobs, LinkedIn-Jobs).
2026-11-19 · Inhaber · Vor Akquise-Briefen immer prüfen, ob die Firma schon Kunde/Kontakt ist (Angebote/Rechnungen in Gmail bzw. Billdu). Inhaber erstellt Angebote/Rechnungen bisher mit Billdu (Nummernkreis Angebote AGB-0xxx).
2026-11-19 · Scout · Stellenanzeigen von Hausverwaltungen für Hausmeister (mit Garten/Winterdienst) sind gute Akquise-Signale: dort besteht Bedarf – externen Service anbieten.

- 19.11.2026: Rahmenvertrag-Vorschlag für Stammkunden aus den echten Rechnungsstunden ableiten (Durchschnitt pro Monat), zwei Pakete anbieten, Absage-Regel (7 Tage verschiebbar, kurzfristig = erbracht) gegen Arbeitsausfall.
- 19.11.2026: Gmail-App (iPhone) ignoriert display:none beim Bearbeiten von Entwürfen → beide Signatur-Logos sichtbar. Lösung: in Gmail-Entwürfen nur ein Logo (hell, mit weißer Kontur).
- 19.11.2026: Gezeichnete Strichmännchen-Reels (Winterdienst, Schranktür, Küche) kamen beim Inhaber und seiner Freundin NICHT an: "nicht ansprechend, nicht lustig genug". Formulierung "Schreiner-Modus" geht gar nicht. Künftig: erst Beispiel-Reel/Stil vom Inhaber holen, bevorzugt echte Handyaufnahmen mit Texten/Musik schneiden statt Zeichnungen.
- 20.11.2026: Erste feste Pflegeobjekte beauftragt (2 Mehrfamilienhäuser, Jülich, Start 12/2026 und 02/2027). Was geholfen hat: je Haus ein eigenes Angebot, Intervalle gemeinsam am Telefon klären, saisonale Arbeiten auf 12 Monate verteilen, Option „monatlich oder auf einen Schlag“ anbieten.
- 20.11.2026: Vergleichsangebot exakt nach Leistungsverzeichnis des Kunden (jede Position einzeln, „inklusive“/„nach Aufwand“ markiert) + Recherche zum Objekt (Größe, Abfuhrplan) → Kunde will wechseln, wir liegen knapp unter dem bisherigen Dienstleister. Preis über Zeitansätze/Häufigkeiten angepasst, Stundensatz gehalten.
- 20.11.2026 · Wochenpflege: Website komplett erreichbar (alle Seiten 200). Google-Profil 13.–19.11.: 7 Aufrufe, 11 Website-Klicks, 0 Anrufe – Google-Daten kommen mit ein paar Tagen Verzögerung. Wochen-Routine schlägt noch gezeichnete Reels vor: laut Inhaber-Regel (19.11.) ausgelassen, stattdessen nur Bild-Beitrag + 2 Stories ohne Preise.
- 20.11.2026: Zaun-Angebot nach Video/Fotos vom Inhaber erstellt. Erst Stückliste klären (Elemente, Doppelpfosten, Tor), dann Materialpreise beim Baumarkt prüfen (OBI-Seite abrufbar, Bauhaus/Hornbach blocken). Rustikale T&J-Elemente nehmen, nicht die dünnen Billig-Elemente. Pfosten bei niedrigem Jägerzaun einschlagen statt einbetonieren.
- 23.11.2026: Neuer Helfer „Kleinanzeigen-Betreuung“ (Mo–Sa 12:41/18:41): liest Kleinanzeigen-Benachrichtigungen in Gmail und schreibt Antworten zum Kopieren – kein Zugang zum Konto selbst. Instagram-Bilder jetzt mit großem Logo oben mittig ohne Hintergrund (marketing/insta_bild.py), gefiel dem Inhaber besser.
- 23.11.2026: Scroll-Geschichte mit vielen Effekten (wanderndes Logo, Sticky-Kapitel, Clip-Path, Parallax) auf der Startseite ging live und wurde vom Inhaber sofort zurückgenommen: „Seite hängt total“. Lehre: Schwere Scroll-Effekte nie direkt live stellen, erst auf echtem Handy testen lassen (Vorschau-Link), Performance vor Effekte. Bild und Text müssen immer zusammenpassen.

## 23.11.2026 – Besucherstatistik PostHog
- PostHog nur cookieless (cookieless_mode always, Projekt-Einstellung „stateful“), Bibliothek selbst hosten (keine externen Skripte), erst nach dem Seitenladen starten (Seite bleibt schnell).
- Datenschutz-Änderungen nur mit OK des Inhabers (hier erteilt). Für Tests im Headless-Browser filtert PostHog Bots heraus – das ist kein Fehler auf der Website.
- Neue Werkzeuge: Firecrawl (Webseiten auslesen, z. B. eBay/Amazon-Gebühren), PostHog (Statistik).

## 24.11.2026 – Mehrere Häuser, ein Angebot?
- Bei Anfragen für mehrere zusammenhängende Häuser vorab fragen, ob ein Gesamtangebot oder je Haus ein eigenes Angebot gewünscht ist. Wunsch des Kunden geht vor die Standardregel „je Haus ein Angebot“.
- Briefe an Hausverwaltungen bringen Antworten per E-Mail – schnell (am selben Abend) antworten wirkt sehr gut.

## 24.11.2026 – Google-Beitrag + Profilzahlen
- Beitrag „Reparatur & Montage vom Schreiner“ veröffentlicht (Foto Türrahmen, Knopf Mehr erfahren).
- Profil letzte 7 Tage: 12× gesehen, 2 Website-Klicks, 0 Anrufe (Vorwoche 16.–22.11.: 16× gesehen, 9 Website-Klicks). Google meldet mit 2–3 Tagen Verzug, daher noch nicht vergleichbar. Erkenntnis: Profil ist noch klein – Bewertungen und Verzeichniseinträge sind der wichtigste Hebel.
- 24.11.2026 · Video-Creator: Für echte Handyvideos gibt es jetzt marketing/reel_video.py (Clip zuschneiden auf 1080x1920, Logo oben, Texte aus JSON, Schlusskarte, eigene Musik, Originalton und Metadaten raus). Danach mit crf 25 nachkomprimieren, sonst wird die Datei ~36 MB groß.
