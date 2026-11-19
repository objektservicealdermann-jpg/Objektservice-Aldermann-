import sys, math, random
sys.path.insert(0,'.')
from reel_lib import *
OUT=sys.argv[1]
BOX=(0.80,0.64,0.42); BOX_D=(0.62,0.47,0.28); FRONT=(0.97,0.97,0.96); TOP=(0.25,0.25,0.27)
def room(cr):
    cr.set_source_rgb(0.93,0.95,0.97); cr.paint()
    cr.set_source_rgb(0.72,0.72,0.74); cr.rectangle(0,1420,W,H-1420); cr.fill()
    cr.set_source_rgb(0.62,0.62,0.64)
    for x in range(-200,W+200,140): cr.move_to(x,1420); cr.line_to(x-120,H); cr.set_line_width(3); cr.stroke()
def box(cr,x,y,w,h,lab=True):
    cr.set_source_rgb(*BOX); cr.rectangle(x,y,w,h); cr.fill()
    cr.set_source_rgb(*BOX_D); cr.set_line_width(4); cr.rectangle(x,y,w,h); cr.stroke()
    cr.set_source_rgb(0.9,0.85,0.6); cr.rectangle(x+w/2-12,y,24,h); cr.fill()
    if lab and w>110: text(cr,'↑ OBEN',x+w/2,y+h/2+12,max(18,w/8),BOX_D)
def boxes(cr,n,T,wob=0):
    random.seed(4); i=0
    for row in range(9):
        for col in range(5):
            if i>=n: return
            w=random.choice([150,170,190]); h=random.choice([110,130]); x=120+col*170+random.uniform(-10,10)+math.sin(T*6+row)*wob*row*3; y=1420-(row+1)*125
            box(cr,x,y,w,h); i+=1
def kitchen(cr,p=1,x0=-420,steam=0,T=0):
    # Unterschränke
    n=12; w=230
    for i in range(n):
        if i/n>p: break
        x=x0+i*w
        cr.set_source_rgb(*FRONT); rr(cr,x+4,1100,w-8,320,8); cr.fill()
        cr.set_source_rgb(0.75,0.75,0.78); cr.set_line_width(3); rr(cr,x+4,1100,w-8,320,8); cr.stroke()
        cr.set_source_rgb(*INK); rr(cr,x+w/2-40,1130,80,10,5); cr.fill()
        # Oberschränke
        cr.set_source_rgb(*FRONT); rr(cr,x+4,560,w-8,330,8); cr.fill()
        cr.set_source_rgb(0.75,0.75,0.78); rr(cr,x+4,560,w-8,330,8); cr.stroke()
        cr.set_source_rgb(*INK); rr(cr,x+w/2-40,860,80,10,5); cr.fill()
    if p>=1:
        cr.set_source_rgb(*TOP); cr.rectangle(x0-10,1070,n*w+20,34); cr.fill()
        # Herd
        hx=x0+5*w; cr.set_source_rgb(0.15,0.15,0.17); rr(cr,hx+20,1160,w-40,200,10); cr.fill(); cr.set_source_rgb(0.95,0.55,0.15); rr(cr,hx+40,1180,w-80,150,8); cr.fill()
        for k in range(2): cr.set_source_rgb(0.3,0.3,0.32); cr.arc(hx+70+k*90,1062,26,0,2*math.pi); cr.fill()
        # Topf mit Dampf
        cr.set_source_rgb(*RED); rr(cr,hx+40,990,110,70,10); cr.fill()
        if steam:
            cr.set_source_rgba(1,1,1,0.8); cr.set_line_width(10)
            for k in range(3):
                bx=hx+60+k*35; cr.move_to(bx,980)
                for j in range(6): cr.line_to(bx+12*math.sin(T*5+j+k),980-j*30)
                cr.stroke()
        # Spüle
        sx=x0+3*w; cr.set_source_rgb(0.8,0.82,0.85); rr(cr,sx+30,1072,w-60,20,6); cr.fill()
        cr.set_source_rgb(0.6,0.62,0.65); cr.set_line_width(12); cr.move_to(sx+w/2,1072); cr.line_to(sx+w/2,990); cr.line_to(sx+w/2+50,990); cr.stroke()
        # Kühlschrank
        fx=x0+n*w; cr.set_source_rgb(0.85,0.87,0.90); rr(cr,fx+10,560,260,860,14); cr.fill(); cr.set_source_rgb(*INK); rr(cr,fx+40,700,12,160,6); cr.fill(); rr(cr,fx+40,1000,12,200,6); cr.fill()
def paper(cr,x,y,u,T):
    cr.save(); cr.translate(x,y); cr.rotate(math.sin(T*3)*0.08)
    for k in range(int(1+u*5)):
        cr.set_source_rgb(1,1,1); cr.rectangle(-60+k*70,-200+k*12,90,130); cr.fill()
        cr.set_source_rgb(*INK); cr.set_line_width(3); cr.rectangle(-60+k*70,-200+k*12,90,130); cr.stroke()
        for l in range(4): cr.move_to(-50+k*70,-180+k*12+l*25); cr.line_to(20+k*70,-180+k*12+l*25)
        cr.stroke()
    cr.restore()
def screws(cr,T):
    random.seed(int(T*10)); cr.set_source_rgb(0.55,0.56,0.6)
    for i in range(8):
        x=random.uniform(150,900); y=random.uniform(900,1400); cr.save(); cr.translate(x,y); cr.rotate(random.uniform(0,6)); rr(cr,-4,-18,8,36,3); cr.fill(); cr.restore()
def badge(cr,txt,x,y,a):
    cr.set_source_rgba(*RED,a); rr(cr,x-280,y-55,560,90,45); cr.fill(); text(cr,txt,x,y+8,46,WHITE,alpha=a)
SC=[('intro',3.4),('chaos',4.4),('jan',5.0),('wow',5.6),('ende',4.6)]
def draw(cr,name,t,T,d):
    if name=='ende':
        ende(cr,t,d,('Küchen- und Möbelmontage','Reparatur · Hausmeisterservice')); return
    room(cr)
    if name=='intro':
        n=int(min(40,ease(t/1.6)*40)); boxes(cr,n,T,wob=1 if t>1.6 else 0)
        person(cr,880,1720,'kunde',T,arm=1.0,s=0.85)
        caption(cr,0,'Die neue Küche ist da!','… in ein paar Kartons',t)
        if t>1.8: bubble(cr,330,700,700,180,'Das sind ja\n87 Kartons?!',56,ease((t-1.8)*3),tail='right')
    elif name=='chaos':
        boxes(cr,40,T,wob=1); screws(cr,T)
        person(cr,880,1720,'kunde',T,arm=0.6+0.5*math.sin(T*8),s=0.85); paper(cr,760,1500,min(1,t/2),T)
        caption(cr,0,'Aufbauanleitung','Seite 1 von 214 …',t)
        if t>2.2: bubble(cr,120,640,640,170,'Wo kommt\ndas hin?!',58,ease((t-2.2)*3))
    elif name=='jan':
        u=ease((t-1.2)/3.2)
        kitchen(cr,u)
        boxes(cr,int(40*(1-u)),T)
        jx=-150+ease(t/1.0)*560; person(cr,jx,1760,'jan',T,arm=0.4+0.6*abs(math.sin(T*14)) if t>1 else 0.2,s=0.9)
        person(cr,960,1760,'kunde',T,arm=0.2,s=0.8)
        caption(cr,0,'Schreiner-Modus: AN','Wir bauen das für Sie auf',t)
        if 1.2<t<4.6:
            cr.set_source_rgb(0.98,0.8,0.1); random.seed(int(T*12))
            for i in range(7): star(cr,random.uniform(80,1000),random.uniform(560,1400),random.uniform(12,28))
            cr.set_source_rgb(*RED); rr(cr,W/2-120,450,240,110,55); cr.fill(); cr.set_source_rgb(1,1,1)
            for dx in (-45,15):
                cr.move_to(W/2+dx,475); cr.line_to(W/2+dx+50,505); cr.line_to(W/2+dx,535); cr.close_path(); cr.fill()
    elif name=='wow':
        z=1.25-0.45*ease(t/1.8)
        cr.save(); cr.translate(W/2,1100); cr.scale(z,z); cr.translate(-W/2,-1100)
        kitchen(cr,1,x0=-760,steam=1,T=T)
        person(cr,260,1760,'jan',T,arm=1.0 if t>1.8 else 0.2,thumb=t>1.8,s=0.9)
        person(cr,560,1760,'kunde',T,arm=1.0 if t>2.2 else 0.3,thumb=t>2.2,s=0.9)
        cr.restore()
        caption(cr,0,'Gigantisch, oder?','Passgenau montiert vom Schreiner',t)
        if 1.8<t<3.0: text(cr,'WOW!',W/2,560,130,RED,alpha=ease((t-1.8)*4))
        if t>3.0: checklist(cr,t-3.0,['Küchenmontage','Möbelaufbau','Passgenau vom Schreiner'],520)
    fade(cr,t,d)
render(OUT,SC,draw)
print('ok')
