import json, base64, html
import sys
D=json.load(open(sys.argv[1],encoding='utf-8'))
OUT=sys.argv[2]
LOGO='data:image/png;base64,'+base64.b64encode(open('logo.png','rb').read()).decode()
css='''@page{size:A4;margin:0}
*{box-sizing:border-box}
body{margin:0;font-family:Arial,Helvetica,sans-serif;color:#141414}
.page{width:210mm;height:297mm;position:relative;page-break-after:always;overflow:hidden}
.fold{position:absolute;left:4mm;width:5mm;border-top:0.3pt solid #999}
.logo{position:absolute;top:14mm;right:20mm;width:62mm}
.redline{position:absolute;top:40mm;right:20mm;width:62mm;height:1mm;background:#d71920}
.absender{position:absolute;top:45mm;left:20mm;width:85mm;font-size:7pt;color:#555;border-bottom:0.3pt solid #999;padding-bottom:1mm}
.anschrift{position:absolute;top:52mm;left:20mm;width:85mm;font-size:10.5pt;line-height:1.35}
.info{position:absolute;top:50mm;right:20mm;width:62mm;font-size:8.5pt;line-height:1.5;color:#333}
.info b{color:#141414}
.content{position:absolute;top:98mm;left:20mm;right:20mm;font-size:10.5pt;line-height:1.5}
.betreff{font-weight:bold;font-size:11pt;margin:0 0 7mm}
.content p{margin:0 0 3.6mm}
.content ul{margin:0 0 3.6mm;padding-left:6mm}
.content li{margin:0 0 1mm}
.sig{margin-top:6mm}
.sig .name{font-weight:bold;color:#d71920}
.footer{position:absolute;bottom:12mm;left:20mm;right:20mm;border-top:0.4pt solid #ccc;padding-top:2.5mm;font-size:7.5pt;color:#666;display:flex;justify-content:space-between}
h2{font-size:15pt;margin:0 0 2mm}
.lead{color:#555;margin:0 0 6mm}
.box{border-left:1mm solid #d71920;padding:2mm 0 2mm 5mm;margin:0 0 5mm}
.box h3{margin:0 0 1.5mm;font-size:11pt}
.box p{margin:0;font-size:10pt;color:#333}
'''
def esc(s): return html.escape(s)
def footer():
    return '<div class="footer"><span>Objektservice Aldermann · Inhaber Jan-Luca Aldermann · Bretzelbäckerstraße 3 · 52428 Jülich</span><span>0176 23751407 · objektservicealdermann@gmail.com · www.objektservicealdermann.com</span></div>'
def letter(d):
    n=esc(d['name']); st=esc(d['stadt']); inort=st if st.startswith('im ') else 'in '+st
    return f'''<div class="page">
<div class="fold" style="top:105mm"></div><div class="fold" style="top:210mm"></div>
<img class="logo" src="{LOGO}"><div class="redline"></div>
<div class="absender">Objektservice Aldermann · Bretzelbäckerstraße 3 · 52428 Jülich</div>
<div class="anschrift">{n}<br>{esc(d['str'])}<br>{esc(d['ort'])}</div>
<div class="info"><b>Jan-Luca Aldermann</b><br>Inhaber<br>Tel. 0176 23751407<br>objektservicealdermann@gmail.com<br>www.objektservicealdermann.com<br><br>Jülich, im November 2026</div>
<div class="content">
<div class="betreff">Zuverlässige Betreuung Ihrer Objekte {inort} und Umgebung</div>
<p>Sehr geehrtes Team von {n},</p>
<p>mein Name ist Jan-Luca Aldermann. Ich bin gelernter Schreiner und Inhaber von Objektservice Aldermann aus Jülich. Wir betreuen Wohnanlagen, Mehrfamilienhäuser und Gewerbeobjekte {inort} und Umgebung – von der regelmäßigen Objektbetreuung über Grünpflege und Winterdienst bis zu kleineren Reparaturen.</p>
<p>Als Verwaltung brauchen Sie vor allem eines: einen Dienstleister, auf den Sie sich verlassen können, ohne ständig nachfassen zu müssen. Genau so arbeiten wir:</p>
<ul>
<li>ein fester Ansprechpartner, direkt erreichbar per Telefon und WhatsApp</li>
<li>klares Leistungsverzeichnis und feste Monatspauschale – planbar für Ihre Eigentümer</li>
<li>Mängel werden gemeldet und kleine Reparaturen direkt vor Ort erledigt</li>
<li>für größere Garten- und Landschaftsbauarbeiten ein fester Partnerbetrieb</li>
</ul>
<p>Gern übernehmen wir zunächst auch ein einzelnes Objekt oder einen kurzfristigen Auftrag, damit Sie uns unverbindlich kennenlernen können. Für diesen Winter haben wir außerdem noch freie Kapazitäten im Winterdienst.</p>
<p>Ich würde mich freuen, Sie kurz kennenzulernen, und melde mich gern in den nächsten Tagen telefonisch bei Ihnen. Sie erreichen mich natürlich auch direkt unter 0176 23751407.</p>
<div class="sig">Mit freundlichen Grüßen<br><br><br><span class="name">Jan-Luca Aldermann</span><br>Objektservice Aldermann</div>
</div>
{footer()}
</div>'''
def leistungen():
    items=[('Hausmeisterservice & Objektbetreuung','Regelmäßige Kontrollgänge, Mängelmeldung, Mülltonnenservice, Treppenhaus- und Außenreinigung, Ordnung am Objekt.'),
           ('Grün- & Gartenpflege','Rasenmähen, Hecken- und Formschnitt, Beetpflege, Laub, Unkraut auf Wegen und Pflasterflächen, Grünschnitt-Entsorgung.'),
           ('Winterdienst','Schneeräumen und Streuen auf Gehwegen, Zugängen und Zufahrten – zur festen Saisonpauschale, Übernahme der Räumpflicht.'),
           ('Reparatur & Montage','Durch die Schreinerausbildung vieles direkt aus einer Hand: Türen, Beschläge, Holzarbeiten, Mülltonnenboxen, Tore, Sichtschutz, Möbel- und Küchenmontage.'),
           ('So arbeiten wir','Kostenlose Besichtigung, schriftliches Angebot mit festem Preis, ein fester Ansprechpartner. Einsatzgebiet: Jülich, Kreis Düren, Aachen, Köln, Düsseldorf, Kreis Heinsberg, Mönchengladbach.')]
    boxes=''.join(f'<div class="box"><h3>{a}</h3><p>{b}</p></div>' for a,b in items)
    return f'''<div class="page">
<img class="logo" src="{LOGO}"><div class="redline"></div>
<div class="content" style="top:52mm"><h2>Unsere Leistungen für Hausverwaltungen</h2><p class="lead">Alles rund um Ihre Objekte – zuverlässig, persönlich und regional.</p>{boxes}
<p style="margin-top:6mm"><b>Kontakt:</b> Jan-Luca Aldermann · Tel. 0176 23751407 · objektservicealdermann@gmail.com · www.objektservicealdermann.com</p></div>
{footer()}</div>'''
import os
os.makedirs(OUT,exist_ok=True)
allp=[]
for i,d in enumerate(D,1):
    page=letter(d)+leistungen()
    allp.append(page)
    open(f'{OUT}/{i:02d}.html','w',encoding='utf-8').write(f'<!doctype html><meta charset=utf-8><style>{css}</style>'+page)
open(f'{OUT}/alle.html','w',encoding='utf-8').write(f'<!doctype html><meta charset=utf-8><style>{css}</style>'+''.join(allp))
print(len(D))
