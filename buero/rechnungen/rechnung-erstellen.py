import json, sys, base64, html
d=json.load(open(sys.argv[1],encoding='utf-8')); out=sys.argv[2]
LOGO='data:image/png;base64,'+base64.b64encode(open(sys.argv[3] if len(sys.argv)>3 else 'logo.png','rb').read()).decode()
e=html.escape
def eur(x): return f"{x:,.2f}".replace(',','X').replace('.',',').replace('X','.')
def menge(m): return (f"{m:g}").replace('.',',')
netto=sum(p['menge']*p['preis'] for p in d['positionen']); ust=round(netto*d['ust']/100,2); brutto=netto+ust
rows=''
for p in d['positionen']:
    txt=e(p.get('text','')).replace('\n','<br>')
    rows+=f'<tr><td class="desc"><div class="t">{e(p["titel"])}</div><div class="d">{txt}</div></td><td class="num">{menge(p["menge"])} {e(p["einheit"])}</td><td class="num">{eur(p["preis"])}</td><td class="num">{eur(p["menge"]*p["preis"])}</td></tr>'
st=f'<div><b>Steuernummer:</b> {e(d["steuernummer"])}</div>' if d.get('steuernummer') else ''
b=d['bank']
doc=f'''<!doctype html><meta charset="utf-8"><style>
@page{{size:A4;margin:0}} *{{box-sizing:border-box}}
body{{margin:0;font-family:Arial,Helvetica,sans-serif;color:#141414;font-size:10pt}}
.page{{width:210mm;height:297mm;position:relative;display:flex;flex-direction:column;overflow:hidden}}
.head{{background:linear-gradient(135deg,#7a0a0e,#a5141a 55%,#6b080c);height:44mm;position:relative;flex:none}}
.logo{{position:absolute;left:14mm;top:5mm;width:68mm;height:34mm;background:#fff;display:flex;align-items:center;justify-content:center}}
.logo img{{width:56mm}}
.htxt{{position:absolute;right:14mm;top:9mm;text-align:right;color:#fff}}
.htxt .r{{font-size:19pt;letter-spacing:1px;margin-bottom:4mm}}
.htxt div{{font-size:10pt;line-height:1.55}}
.meta{{background:#2f3b45;color:#fff;display:grid;grid-template-columns:1fr 1fr 1fr;column-gap:6mm;row-gap:0;padding:3mm 14mm;font-size:8.8pt}}
.meta div{{display:flex;justify-content:space-between;line-height:1.55}} .meta b{{font-weight:700}}
.addr{{display:grid;grid-template-columns:1fr 1fr 1fr;border-bottom:1px solid #e3e3e3}}
.addr>div{{padding:4mm 0 5mm 14mm;line-height:1.45;border-right:1px solid #e3e3e3}} .addr>div:last-child{{border-right:0}}
.addr b{{display:block;margin-bottom:1mm}}
.big{{font-size:22pt;color:#8a0f14;margin-top:2mm}}
.ort{{padding:3mm 14mm;font-style:italic;line-height:1.5;border-bottom:1px solid #e3e3e3}}
table{{width:100%;border-collapse:collapse;margin-top:2mm}}
th{{text-align:left;font-size:9pt;padding:4mm 0 3mm;border-bottom:1.5px solid #bbb}} th.num,td.num{{text-align:right}}
th:first-child,td:first-child{{padding-left:14mm}} th:last-child,td:last-child{{padding-right:14mm}}
td{{vertical-align:top;padding:3mm 0;border-bottom:1px solid #e3e3e3}}
td.desc{{width:52%;padding-right:8mm}} .t{{margin-bottom:2mm}} .d{{line-height:1.42}}
.sum{{padding:3mm 14mm 0;}} .sum div{{display:flex;justify-content:space-between;line-height:1.8}}
.sum .tot{{font-size:15pt;font-weight:700;margin-top:1mm}}
.bank{{margin-top:auto;padding:4mm 14mm 8mm}}
.bank h4{{color:#8a0f14;font-size:9pt;margin:0 0 2mm;border-bottom:1px solid #e3e3e3;padding-bottom:2mm}}
.bank div{{font-size:8.6pt;line-height:1.6}}
</style><div class="page">
<div class="head"><div class="logo"><img src="{LOGO}"></div>
<div class="htxt"><div class="r">Rechnung</div><div>Jan-Luca Aldermann</div><div>+49 176 23751407</div><div>objektservicealdermann@gmail.com</div></div></div>
<div class="meta">
<div><span><b>RECHNUNGSNUMMER:</b></span><span>{e(d["nummer"])}</span></div><div><span><b>KUNDENNUMMER:</b></span><span>{e(d["kundennr"])}</span></div><div><span><b>AUSGESTELLT:</b></span><span>{e(d["ausgestellt"])}</span></div>
<div><span><b>ZAHLUNGSZIEL:</b></span><span>{e(d["zahlungsziel"])}</span></div><div><span><b>LIEFERDATUM:</b></span><span>{e(d["lieferdatum"])}</span></div><div><span><b>ZAHLUNGSFORM:</b></span><span>{e(d["zahlungsform"])}</span></div></div>
<div class="addr"><div><b>VON</b>Objektservice Aldermann<br>Bretzelbäckerstr. 3<br>52428 Jülich<br>Deutschland{('<br><span style="font-size:8.6pt">Steuernummer: '+e(d["steuernummer"])+'</span>') if d.get("steuernummer") else ''}</div>
<div><b>AN</b>{'<br>'.join(e(x) for x in d["an"])}</div>
<div><b>Zu bezahlen:</b><div class="big">{eur(brutto)} €</div></div></div>
<div class="ort">Ausführungsort:<br>{'<br>'.join(e(x) for x in d["ausfuehrungsort"])}</div>
<table><tr><th>BESCHREIBUNG</th><th class="num">MENGE</th><th class="num">PREIS (€)</th><th class="num">BETRAG (€)</th></tr>{rows}</table>
<div class="sum"><div><span>Nettobetrag</span><span>{eur(netto)} €</span></div><div><span><i>USt. {eur(d["ust"])} % von {eur(netto)}</i></span><span>{eur(ust)} €</span></div><div class="tot"><span>Gesamtbetrag (EUR):</span><span>{eur(brutto)} €</span></div></div>
<div class="bank"><h4>BANKVERBINDUNG:</h4><div><b>Zahlungsempfänger:</b> {e(b["empfaenger"])} &nbsp; <b>Bank:</b> {e(b["bank"])}</div><div><b>IBAN:</b> {e(b["iban"])} &nbsp; <b>BIC/SWIFT:</b> {e(b["bic"])}</div></div>
</div>'''
open(out,'w',encoding='utf-8').write(doc)
print(f"netto {eur(netto)} ust {eur(ust)} brutto {eur(brutto)}")
