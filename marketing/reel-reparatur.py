import sys, math, random
sys.path.insert(0,'.')
from reel_lib import *
OUT=sys.argv[1]
WOOD=(0.78,0.58,0.38); WOOD_D=(0.55,0.38,0.22)
def room(cr):
    cr.set_source_rgb(0.96,0.92,0.84); cr.paint()
    cr.set_source_rgb(0.80,0.66,0.48); cr.rectangle(0,1420,W,H-1420); cr.fill()
    cr.set_source_rgb(0.70,0.56,0.40)
    for x in range(0,W,180): cr.rectangle(x,1420,4,H-1420); cr.fill()
    cr.set_source_rgb(0.62,0.48,0.34); cr.rectangle(0,1410,W,14); cr.fill()
    # Bild an der Wand
    cr.set_source_rgb(*INK); rr(cr,120,820,220,170,8); cr.fill(); cr.set_source_rgb(0.55,0.78,0.92); rr(cr,135,835,190,140,4); cr.fill()
    cr.set_source_rgb(0.42,0.70,0.33); cr.move_to(135,975); cr.line_to(200,900); cr.line_to(260,950); cr.line_to(325,890); cr.line_to(325,975); cr.close_path(); cr.fill()
def cabinet(cr,door=0,fallen=0,crooked=0):
    x,y,w,h=600,860,340,560
    cr.set_source_rgb(*WOOD_D); rr(cr,x-10,y-10,w+20,h+20,10); cr.fill()
    cr.set_source_rgb(0.35,0.24,0.14); cr.rectangle(x,y,w,h); cr.fill()
    # linke Tür
    cr.set_source_rgb(*WOOD); rr(cr,x+6,y+6,w/2-9,h-12,6); cr.fill(); cr.set_source_rgb(*INK); cr.arc(x+w/2-30,y+h/2,9,0,2*math.pi); cr.fill()
    if fallen>0:
        cr.save(); cr.translate(x+w*0.75+fallen*160,1420-40*fallen); cr.rotate(fallen*1.45)
        cr.set_source_rgb(*WOOD); rr(cr,-w/4,-h/2,w/2-9,h-12,6); cr.fill(); cr.restore(); return
    c=math.cos(door*1.3)
    cr.save(); cr.translate(x+w-6,y+6); cr.rotate(crooked*0.08)
    dw=(w/2-9)*c
    cr.set_source_rgb(*(WOOD if c>0 else WOOD_D)); rr(cr,-abs(dw) if c>0 else 0,0,max(abs(dw),4),h-12,6); cr.fill()
    if c>0.2: cr.set_source_rgb(*INK); cr.arc(-dw+30,h/2,9,0,2*math.pi); cr.fill()
    cr.restore()
def toolbox(cr,x,y):
    cr.set_source_rgb(*RED); rr(cr,x-70,y-60,140,60,8); cr.fill()
    cr.set_source_rgb(*INK); cr.set_line_width(8); cr.move_to(x-30,y-60); cr.line_to(x-30,y-85); cr.line_to(x+30,y-85); cr.line_to(x+30,y-60); cr.stroke()
def sweat(cr,x,y,T):
    cr.set_source_rgb(0.45,0.70,0.95)
    for i in range(3):
        yy=y+((T*120+i*40)%90); cr.arc(x+i*25,yy,9,0,2*math.pi); cr.fill()
def badge(cr,txt,x,y,a):
    cr.save(); cr.set_source_rgba(*RED,a); rr(cr,x-260,y-55,520,90,45); cr.fill(); text(cr,txt,x,y+8,46,WHITE,alpha=a); cr.restore()
SC=[('intro',3.0),('kampf',4.8),('whatsapp',3.6),('schreiner',4.6),('happy',5.2),('ende',4.6)]
def draw(cr,name,t,T,d):
    if name=='ende':
        ende(cr,t,d,('Reparatur · Montage · Schreinerarbeiten','Hausmeisterservice · Gartenpflege')); return
    room(cr)
    if name=='intro':
        cabinet(cr,door=0.35,crooked=1)
        caption(cr,0,'Jeder kennt sie …','die Schranktür, die nie zugeht',t)
    elif name=='kampf':
        caption(cr,0,'Tag 1.247','Sie geht einfach nicht zu',t)
        if t<3.0:
            dv=abs(math.sin(t*5))*0.6; cabinet(cr,door=dv,crooked=1)
            person(cr,420,1700,'kunde',T,arm=0.3+0.6*abs(math.cos(t*5)),s=0.95)
            if t>1.2: sweat(cr,470,1250,T)
        else:
            u=min(1,(t-3.0)/0.5); cabinet(cr,fallen=u)
            person(cr,420,1700,'kunde',T,arm=1.2,s=0.95)
            bubble(cr,80,700,560,170,'Ach nö …!',66,ease((t-3.1)*4))
    elif name=='whatsapp':
        cabinet(cr,fallen=1)
        person(cr,420,1700,'kunde',T,arm=0.9,phone=True,s=0.95)
        caption(cr,0,'Kurz ein Foto schicken','per WhatsApp – fertig',t)
        if t>0.5: bubble(cr,90,680,640,170,'Können Sie helfen?',52,ease((t-0.5)*3))
        if t>1.8: bubble(cr,360,900,620,150,'Klar, bin morgen da!',48,ease((t-1.8)*3),tail='right')
    elif name=='schreiner':
        u=ease((t-1.6)/1.6)
        cabinet(cr,door=0.0) if t>3.2 else cabinet(cr,fallen=1-u)
        jx=-150+ease(t/1.0)*560; person(cr,jx,1700,'jan',T,arm=0.4+0.5*abs(math.sin(T*12)) if t>1 else 0.2,s=0.95); toolbox(cr,jx-130,1700)
        caption(cr,0,'Gelernter Schreiner','Das passt jetzt wieder',t)
        if t>0.9: badge(cr,'Schreiner-Modus: AN',W/2,640,ease((t-0.9)*3))
        if 1.6<t<3.4:
            cr.set_source_rgb(0.98,0.8,0.1)
            random.seed(int(T*12))
            for i in range(6): star(cr,600+random.uniform(0,340),900+random.uniform(0,480),random.uniform(12,26))
    elif name=='happy':
        cabinet(cr,door=max(0,0.5-t*0.6))
        person(cr,420,1700,'kunde',T,arm=1.0 if t>1.0 else 0.2,thumb=t>1.0,s=0.95)
        person(cr,190,1700,'jan',T,arm=1.0 if t>1.0 else 0.2,thumb=t>1.0,s=0.9); toolbox(cr,110,1700)
        caption(cr,0,'Klick. Endlich zu.','Sauber und passgenau',t)
        if 0.8<t<1.6: text(cr,'KLICK!',800,820,80,RED,alpha=ease((t-0.8)*4))
        if t>1.7: checklist(cr,t-1.7,['Türen und Schränke','Möbel- und Küchenmontage','Kleine Reparaturen'],560)
    fade(cr,t,d)
render(OUT,SC,draw)
print('ok')
