# Vorschau: Logo-Intro auf der Startseite (wartet auf OK des Inhabers, 25.11.2026)
Nicht live. Zum Freischalten:
  git apply marketing/vorschau/website-intro.patch
  cp marketing/vorschau/logo-intro.mp4 public/video/
  cp marketing/vorschau/logo-intro-poster.jpg public/img/
Intro läuft einmal pro Besuch (sessionStorage), überspringbar, nicht für Bots/reduced-motion.
