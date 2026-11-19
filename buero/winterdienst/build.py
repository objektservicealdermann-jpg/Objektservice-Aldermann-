import base64
LOGO='data:image/png;base64,'+base64.b64encode(open('logo.png','rb').read()).decode()
doc=f'''<!doctype html><meta charset="utf-8"><style>
@page{{size:A4;margin:0}}*{{box-sizing:border-box}}
body{{margin:0;font-family:Arial,Helvetica,sans-serif;color:#141414;font-size:9.6pt}}
.page{{width:210mm;height:297mm;display:flex;flex-direction:column;overflow:hidden}}
.head{{background:linear-gradient(135deg,#7a0a0e,#a5141a 55%,#6b080c);height:40mm;position:relative;flex:none}}
.logo{{position:absolute;left:14mm;top:5mm;width:62mm;height:30mm;background:#fff;display:flex;align-items:center;justify-content:center}}.logo img{{width:52mm}}
.htxt{{position:absolute;right:14mm;top:8mm;text-align:right;color:#fff}}.htxt .r{{font-size:20pt;margin-bottom:3mm}}.htxt div{{font-size:10pt;line-height:1.5}}
.meta{{background:#2f3b45;color:#fff;padding:2.5mm 14mm;font-size:9pt;display:flex;justify-content:space-between}}
.in{{padding:4mm 14mm 0}} h2{{font-size:12pt;margin:0 0 2mm;color:#8a0f14}} p{{margin:0 0 2mm;line-height:1.45}}
ul{{margin:0 0 2mm;padding-left:5mm;line-height:1.5}}
.prices{{display:grid;grid-template-columns:1fr 1fr;gap:4mm;margin:3mm 0}}
.pr{{border:1px solid #ddd;border-top:1.2mm solid #d71920;padding:3mm 4mm}}.pr b{{display:block;font-size:10.5pt}}.pr .big{{font-size:20pt;color:#8a0f14;margin:1.5mm 0 .5mm}}.pr small{{color:#555}}
.form{{margin:2mm 14mm 0;border:1.5px solid #2f3b45;padding:3mm 4mm}}
.form h2{{color:#2f3b45}}
.row{{display:flex;gap:5mm;margin-top:3.2mm}}.f{{flex:1;border-bottom:1px solid #888;padding-top:4mm;font-size:7.8pt;color:#555;position:relative}}.f span{{position:absolute;top:-1mm;left:0}}
.ck{{margin-top:3mm;line-height:1.8}}.ck i{{display:inline-block;width:3.5mm;height:3.5mm;border:1px solid #333;margin-right:2mm;vertical-align:-0.6mm}}
.small{{font-size:7.8pt;color:#555;line-height:1.4;margin-top:2.5mm}}
.foot{{margin-top:auto;padding:3mm 14mm 7mm;border-top:1px solid #e3e3e3;font-size:7.8pt;color:#555}}
</style><div class="page">
<div class="head"><div class="logo"><img src="{LOGO}"></div><div class="htxt"><div class="r">Winterdienst 2026/27</div><div>Tel. / WhatsApp 0176 23751407</div><div>objektservicealdermann@gmail.com</div><div>www.objektservicealdermann.com</div></div></div>
<div class="meta"><span>Jülich · Kreis Düren · Aachen · Köln · Düsseldorf · Kreis Heinsberg</span><span>Saison 01.12.2026 – 31.03.2027</span></div>
<div class="in">
<h2>Wir räumen und streuen – Sie bleiben im Warmen</h2>
<p>Als Eigentümer, Vermieter oder Gewerbetreibender sind Sie für sichere Wege vor Ihrem Haus verantwortlich. Diese Arbeit nehmen wir Ihnen ab, zuverlässig und zu einem festen Preis pro Einsatz.</p>
<ul><li>Räumen und Streuen des Gehwegs vor dem Grundstück und des Zugangs bis zur Eingangstür</li>
<li>Einsatz bei Schnee und Glätte zu den Zeiten, die die Satzung Ihrer Stadt vorschreibt, bei anhaltendem Schneefall auch mehrmals am Tag</li>
<li>Kein Grundpreis, keine Bereitschaftspauschale: Sie zahlen nur, wenn wir wirklich im Einsatz waren</li>
<li>Eine Rechnung zum Monatsende mit Datum jedes Einsatzes</li></ul>
<div class="prices"><div class="pr"><b>Wohnhaus</b><div class="big">30,00 €</div><small>pro Einsatz, netto zzgl. 19 % USt. (35,70 € brutto)<br>Gehweg und Zugang bis zur Haustür</small></div>
<div class="pr"><b>Gewerbe</b><div class="big">60,00 €</div><small>pro Einsatz, netto zzgl. 19 % USt.<br>Gehweg, Eingang und Kundenzugang</small></div></div>
<p style="font-size:8.6pt;color:#555">Größere Flächen wie Parkplätze, Zufahrten oder Höfe bieten wir nach kurzer Besichtigung gesondert an.</p>
</div>
<div class="form"><h2>Auftrag Winterdienst</h2>
<div class="row"><div class="f"><span>Name / Firma</span></div><div class="f"><span>Telefon</span></div></div>
<div class="row"><div class="f"><span>Rechnungsanschrift</span></div></div>
<div class="row"><div class="f"><span>Objekt (falls abweichend)</span></div><div class="f" style="flex:.6"><span>E-Mail</span></div></div>
<div class="ck"><i></i>Wohnhaus – 30,00 € netto pro Einsatz &nbsp;&nbsp;&nbsp; <i></i>Gewerbe – 60,00 € netto pro Einsatz</div>
<div class="row"><div class="f"><span>Besonderheiten (z. B. Treppe, Rampe, zweiter Eingang)</span></div></div>
<div class="small">Leistungszeitraum 01.12.2026 bis 31.03.2027, danach endet der Auftrag automatisch. Abrechnung monatlich nach tatsächlichen Einsätzen, zahlbar innerhalb von 7 Tagen per Überweisung. Für die Dauer des Auftrags übernimmt Objektservice Aldermann das Räumen und Streuen der oben genannten Flächen. Ihre Angaben verwenden wir nur für diesen Auftrag und die Rechnung (Datenschutzhinweise: www.objektservicealdermann.com/datenschutz).</div>
<div class="row" style="margin-top:6mm"><div class="f"><span>Ort, Datum</span></div><div class="f"><span>Unterschrift Auftraggeber</span></div><div class="f"><span>Unterschrift Objektservice Aldermann</span></div></div>
</div>
<div class="foot">Objektservice Aldermann · Inhaber Jan-Luca Aldermann · Bretzelbäckerstr. 3 · 52428 Jülich · 0176 23751407 · USt-IdNr. DE465887336</div>
</div>'''
open('winterdienst-auftrag.html','w',encoding='utf-8').write(doc)
