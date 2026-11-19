import sys, math, random
sys.path.insert(0,'.')
from cartoon_lib import *
OUT=sys.argv[1]
def scene(cr,T,clear_right=True):
    g=cairo.LinearGradient(0,0,0,1300); g.add_color_stop_rgb(0,0.62,0.78,0.95); g.add_color_stop_rgb(1,0.88,0.93,0.99); cr.set_source(g); cr.paint()
    cr.set_source_rgb(0.98,0.99,1); cr.rectangle(0,1300,W,H-1300); cr.fill()
    for hx,col in ((270,(0.95,0.85,0.70)),(810,(0.92,0.93,0.96))):
        rr(cr,hx-210,800,420,500,10); stroke_fill(cr,col,8)
        cr.move_to(hx-250,820); cr.line_to(hx,600); cr.line_to(hx+250,820); cr.close_path(); stroke_fill(cr,RED if hx>500 else (0.45,0.35,0.30),8)
        cr.move_to(hx-250,820); cr.line_to(hx,600); cr.line_to(hx+250,820); cr.line_to(hx+225,800); cr.line_to(hx,625); cr.line_to(hx-225,800); cr.close_path(); cr.set_source_rgb(1,1,1); cr.fill()
        rr(cr,hx-50,1130,100,170,10); stroke_fill(cr,(0.50,0.33,0.20),6)
        for wx in (hx-160,hx+70):
            rr(cr,wx,900,90,90,8); stroke_fill(cr,(0.70,0.88,1.0),6)
    # Wege
    cr.move_to(240,1300); cr.line_to(300,1300); cr.line_to(420,H); cr.line_to(120,H); cr.close_path(); cr.set_source_rgb(0.85,0.93,1.0); cr.fill()
    cr.set_source_rgba(0.6,0.85,1,0.7)
    for k in range(5): rr(cr,170+k*40,1500+k*70,120,18,9); cr.fill()
    cr.move_to(780,1300); cr.line_to(840,1300); cr.line_to(960,H); cr.line_to(660,H); cr.close_path(); cr.set_source_rgb(0.60,0.62,0.66); cr.fill()
    random.seed(9); cr.set_source_rgb(0.42,0.35,0.28)
    for i in range(90):
        yy=random.uniform(1300,H); f=(yy-1300)/(H-1300); cr.arc(random.uniform(780-120*f,840+120*f),yy,4,0,2*math.pi); cr.fill()
    # Schnee fällt
    random.seed(5)
    for i in range(55):
        x=random.uniform(0,W)+math.sin(T+i)*20; y=(random.uniform(0,H)+T*90)%H
        cr.set_source_rgba(1,1,1,0.9); cr.arc(x,y,random.uniform(4,9),0,2*math.pi); cr.fill()
def penguin(cr,x,y,ang,T):
    cr.save(); cr.translate(x,y); cr.rotate(ang); cr.new_path()
    cr.save(); cr.scale(1,1.3); cr.arc(0,-90,70,0,2*math.pi); cr.restore(); stroke_fill(cr,OL,6)
    cr.new_path(); cr.save(); cr.scale(1,1.3); cr.arc(0,-80,48,0,2*math.pi); cr.restore(); cr.set_source_rgb(1,1,1); cr.fill()
    for ex in (-18,18): cr.new_path(); cr.arc(ex,-150,10,0,2*math.pi); cr.set_source_rgb(1,1,1); cr.fill(); cr.new_path(); cr.arc(ex,-150,5,0,2*math.pi); cr.set_source_rgb(*OL); cr.fill()
    cr.move_to(-14,-132); cr.line_to(0,-115); cr.line_to(14,-132); cr.close_path(); stroke_fill(cr,(1,0.6,0.1),3)
    for fx in (-30,30): cr.new_path(); cr.save(); cr.translate(fx,0); cr.scale(1.6,0.6); cr.arc(0,0,14,0,2*math.pi); cr.restore(); stroke_fill(cr,(1,0.6,0.1),3)
    cr.restore()
def slip(cr,who,t,x0,hold=None,label=None):
    # läuft rein, rutscht aus, schlittert aus dem Bild
    if t<0.7: char(cr,x0+t*120,1800,who,t*3,'happy',arm_r=0.3,hold=hold,s=0.75,walk=1)
    else:
        u=t-0.7; ang=-min(1.5,u*6); x=x0+84+u*420; y=1800-math.sin(min(1,u*3)*math.pi)*120
        char(cr,x,y,who,t*3,'shock',arm_l=2.5,arm_r=2.5,hold=hold,s=0.75,lean=ang)
SC=[('intro',3.0),('post',2.6),('pizza',2.6),('pingu',2.8),('klingel',4.4),('ende',3.8)]
def draw(cr,name,t,T,d):
    if name=='ende':
        cr.set_source_rgb(0.08,0.08,0.09); cr.paint()
        a=ease(t*2); sc=min(700/logo_d.get_width(),280/logo_d.get_height()); lw=logo_d.get_width()*sc
        cr.save(); cr.translate((W-lw)/2,560); cr.scale(sc,sc); cr.set_source_surface(logo_d,0,0); cr.paint_with_alpha(a); cr.restore()
        b=ease((t-0.4)*2)
        text(cr,'Winterdienst.',W/2,1000,74,WHITE,alpha=b)
        text(cr,'Damit bei Ihnen keiner ausrutscht.',W/2,1090,48,(1,0.8,0.8),alpha=b)
        c=ease((t-1.0)*2)
        text(cr,'0176 23751407',W/2,1280,92,WHITE,alpha=c)
        text(cr,'objektservicealdermann.com',W/2,1360,44,(0.8,0.8,0.82),bold=False,alpha=c)
        fade(cr,t,d+1); return
    scene(cr,T)
    if name=='intro':
        title(cr,'Zwei Nachbarn. Ein Winter.',t)
        char(cr,810,1760,'frau',T,'happy',arm_r=2.4,s=0.8)
        char(cr,270,1760,'nachbar',T,'happy',arm_r=0.3,s=0.8)
        if t>1.2: speech(cr,60,1080,420,130,'Schippen? Nö.',46,ease((t-1.2)*3))
    elif name=='post':
        title(cr,'Der Postbote …',t); slip(cr,'post',t,120,hold='letter')
        if t>0.9: text(cr,'HUIII!',300,560,90,RED,alpha=ease((t-0.9)*4))
    elif name=='pizza':
        title(cr,'Der Pizzabote …',t); slip(cr,'pizza',t,120,hold='pizzabox')
        if t>0.9:
            text(cr,'NEIN!',300,560,90,RED,alpha=ease((t-0.9)*4))
            cr.save(); cr.translate(250+t*200,1100-t*120); cr.rotate(t*8); cr.arc(0,0,60,0,2*math.pi); stroke_fill(cr,(0.98,0.80,0.40),5); cr.set_source_rgb(0.85,0.25,0.2)
            for k in range(5): cr.arc(30*math.cos(k*1.3),30*math.sin(k*1.3),9,0,2*math.pi); cr.fill()
            cr.restore()
    elif name=='pingu':
        title(cr,'Sogar der Pinguin …',t)
        x=100+t*330; penguin(cr,x,1800,-0.4-t*0.4 if t>0.8 else 0,T)
        if t>0.9: text(cr,'… rutscht.',330,560,80,RED,alpha=ease((t-0.9)*4))
    elif name=='klingel':
        title(cr,'Am nächsten Morgen …',t)
        char(cr,700,1760,'nachbar',T,'worried',arm_r=2.3 if t<1.4 else 0.3,s=0.8)
        char(cr,900,1760,'frau',T,'wink',s=0.8)
        speech(cr,60,1040,720,180,'Hätten Sie mal die Nummer\nvon Ihrem Winterdienst?',44,ease((t-0.5)*3),tail='right')
        if t>2.5: speech(cr,520,780,500,140,'Na klar!',56,ease((t-2.5)*3),tail='right')
    fade(cr,t,d)
render(OUT,SC,draw)
print('ok')
