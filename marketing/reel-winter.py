import sys, math, random
sys.path.insert(0,'.')
from reel_lib import *
OUT=sys.argv[1]
NIGHT=(0.12,0.16,0.30); DAWN=(0.95,0.62,0.55)
def sky(cr,k=0):
    g=cairo.LinearGradient(0,0,0,1380)
    g.add_color_stop_rgb(0,*[a+(b-a)*k for a,b in zip(NIGHT,(0.55,0.75,0.95))]); g.add_color_stop_rgb(1,*[a+(b-a)*k for a,b in zip(DAWN,(0.85,0.93,0.99))])
    cr.set_source(g); cr.paint()
    cr.set_source_rgb(0.97,0.98,1); cr.rectangle(0,1380,W,H-1380); cr.fill()
def snow(cr,T,n=70,alpha=0.9):
    random.seed(5)
    for i in range(n):
        x0=random.uniform(0,W); sp=random.uniform(60,140); r=random.uniform(4,10)
        y=(random.uniform(0,H)+T*sp)%H; x=x0+math.sin(T*1.5+i)*20
        cr.set_source_rgba(1,1,1,alpha); cr.arc(x,y,r,0,2*math.pi); cr.fill()
def path(cr,clear=0,grit=0):
    cr.set_source_rgb(0.62,0.64,0.68); cr.move_to(500,1400); cr.line_to(580,1400); cr.line_to(700,H); cr.line_to(380,H); cr.close_path(); cr.fill()
    # Schnee auf dem Weg (wird von unten nach oben geräumt)
    top=H-(H-1400)*clear
    if top>1400:
        f=(top-1400)/(H-1400); cr.set_source_rgb(0.98,0.99,1)
        cr.move_to(500,1400); cr.line_to(580,1400); cr.line_to(580+120*f,top); cr.line_to(500-120*f,top); cr.close_path(); cr.fill()
    if grit>0:
        random.seed(9); cr.set_source_rgb(0.45,0.38,0.30)
        for i in range(int(140*grit)):
            yy=random.uniform(1400,top) if top>1400 else random.uniform(1400,H); f=(yy-1400)/(H-1400); xx=random.uniform(500-120*f,580+120*f)
            cr.arc(xx,yy,4,0,2*math.pi); cr.fill()
def clock(cr,x,y,a=1):
    cr.set_source_rgba(1,1,1,a); cr.arc(x,y,70,0,2*math.pi); cr.fill()
    cr.set_source_rgba(*INK,a); cr.set_line_width(8); cr.arc(x,y,70,0,2*math.pi); cr.stroke()
    cr.set_line_width(9); cr.move_to(x,y); cr.line_to(x,y+45); cr.stroke(); cr.set_line_width(6); cr.move_to(x,y); cr.line_to(x-25,y+20); cr.stroke()
def snowman(cr,x,y,s,cap=False,wave=0):
    if s<=0: return
    cr.save(); cr.translate(x,y); cr.scale(s,s)
    cr.set_source_rgb(1,1,1)
    for cy,r in [(-70,80),(-190,60),(-285,45)]: cr.arc(0,cy,r,0,2*math.pi); cr.fill()
    cr.set_source_rgb(0.7,0.75,0.82); cr.set_line_width(4)
    for cy,r in [(-70,80),(-190,60),(-285,45)]: cr.arc(0,cy,r,0,2*math.pi); cr.stroke()
    cr.set_source_rgb(*INK)
    for ex in (-15,15): cr.arc(ex,-295,6,0,2*math.pi); cr.fill()
    for k in range(3): cr.arc(0,-210+k*25,6,0,2*math.pi); cr.fill()
    cr.set_source_rgb(0.95,0.5,0.1); cr.move_to(0,-283); cr.line_to(40,-276); cr.line_to(0,-270); cr.close_path(); cr.fill()
    cr.set_source_rgb(*INK); cr.set_line_width(5); cr.arc(0,-268,14,0.2*math.pi,0.8*math.pi); cr.stroke()
    cr.set_source_rgb(0.45,0.3,0.2); cr.set_line_width(8)
    cr.move_to(-55,-200); cr.line_to(-120,-240); cr.stroke()
    ang=-0.9+0.5*math.sin(wave*8) if wave else -0.6
    cr.move_to(55,-200); cr.line_to(55+80*math.cos(ang),-200+80*math.sin(ang)); cr.stroke()
    if cap:
        cr.set_source_rgb(*RED); cr.arc(0,-300,47,math.pi,2*math.pi); cr.fill(); rr(cr,0,-312,70,14,7); cr.fill()
    cr.restore()
def shovel(cr,x,y,ang):
    cr.save(); cr.translate(x,y); cr.rotate(ang)
    cr.set_source_rgb(0.45,0.3,0.2); cr.set_line_width(10); cr.move_to(0,0); cr.line_to(0,170); cr.stroke()
    cr.set_source_rgb(*RED); rr(cr,-45,165,90,60,10); cr.fill()
    cr.restore()
def stars_round(cr,x,y,T):
    cr.set_source_rgb(0.98,0.8,0.1)
    for i in range(4):
        a=T*5+i*math.pi/2; star(cr,x+70*math.cos(a),y+25*math.sin(a),18)
def speed(cr,x,y,n=6):
    cr.set_source_rgba(1,1,1,0.8); cr.set_line_width(6)
    for i in range(n): cr.move_to(x-80-i*10,y-200+i*40); cr.line_to(x-200-i*20,y-200+i*40); cr.stroke()
SC=[('intro',3.2),('slip',4.6),('held',4.6),('streuen',3.6),('happy',5.2),('ende',4.6)]
def draw(cr,name,t,T,d):
    if name=='ende':
        ende(cr,t,d,('Winterdienst 2026/27','Noch Plätze in unserer Tour frei')); return
    k={'intro':0,'slip':0.1,'held':0.3,'streuen':0.6,'happy':1}[name]
    sky(cr,k); house(cr,540,1400,0.85)
    # Schneehaube aufs Dach
    cr.set_source_rgb(1,1,1); cr.move_to(370,1188); cr.line_to(540,1043); cr.line_to(710,1188); cr.line_to(690,1195); cr.line_to(540,1070); cr.line_to(390,1195); cr.close_path(); cr.fill()
    if name=='intro':
        path(cr,0); snow(cr,T)
        a=ease(t*2); clock(cr,W/2,640,a)
        caption(cr,0,'Montag, 6:30 Uhr …','Über Nacht hat es geschneit',t)
    elif name=='slip':
        path(cr,0); snow(cr,T,50)
        caption(cr,0,'Hoppla!','Glatteis vor der Haustür',t)
        if t<1.4:
            person(cr,560+t*60,1720,'kunde',T,s=0.9)
        else:
            u=min(1,(t-1.4)/0.5); ang=-u*1.6; lift=math.sin(u*math.pi)*160
            cr.save(); cr.translate(650,1730-lift); cr.rotate(ang); person(cr,0,0,'kunde',T,arm=1.0,s=0.9); cr.restore()
            if t>1.9: stars_round(cr,520,1620,T)
            if t>1.6: bubble(cr,120,760,560,170,'Huiiii!',70,ease((t-1.6)*4))
    elif name=='held':
        path(cr,min(1,max(0,(t-1.4)/2.6))); snow(cr,T,40)
        cr.save(); cr.translate(820,1600); cr.rotate(-1.6); person(cr,0,0,'kunde',T,arm=0.2,s=0.8); cr.restore()
        vx=-500+ease(t/1.0)*520; van(cr,vx,1840)
        if t>1.0:
            jy=1900-ease((t-1.0)/2.8)*420; jx=470+math.sin(T*14)*10
            person(cr,jx,jy,'jan',T,arm=0.5+0.4*math.sin(T*14),s=0.9)
            shovel(cr,jx+70,jy-200,0.5+0.4*math.sin(T*14)); speed(cr,jx,jy)
            random.seed(int(T*30)); cr.set_source_rgb(1,1,1)
            for i in range(8): cr.arc(jx+random.uniform(-200,-60),jy-random.uniform(100,400),random.uniform(8,18),0,2*math.pi); cr.fill()
        caption(cr,0,'Keine Sorge!','Wir räumen schon',t)
    elif name=='streuen':
        path(cr,1,min(1,t/2.5))
        person(cr,620,1700,'jan',T,arm=0.3+0.5*abs(math.sin(T*6)),s=0.9)
        snowman(cr,200,1560,back(t*1.2)*0.9)
        caption(cr,0,'Räumen und streuen','Sicher bis zur Haustür',t)
    elif name=='happy':
        path(cr,1,1)
        snowman(cr,200,1560,0.9,cap=t>0.6,wave=T if t>0.6 else 0)
        person(cr,480+t*40,1720,'kunde',T,arm=1.0 if t>1 else 0.2,thumb=t>1,s=0.9)
        person(cr,830,1700,'jan',T,arm=1.0 if t>1 else 0.3,thumb=t>1,s=0.85)
        caption(cr,0,'Sicher unterwegs','Und der Schneemann ist auch zufrieden',t)
        if t>1.6: checklist(cr,t-1.6,['Früh am Morgen vor Ort','Räumen und Streuen','Von der Haustür bis zur Straße'],560)
    fade(cr,t,d)
render(OUT,SC,draw)
print('ok')
