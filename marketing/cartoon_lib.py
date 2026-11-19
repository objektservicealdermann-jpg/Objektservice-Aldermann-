import sys, math, random
sys.path.insert(0,'.')
from reel_lib import W,H,FPS,RED,INK,WHITE,ease,back,rr,text,render,logo_d,fade
import cairo
OL=(0.13,0.12,0.14); SKIN=(1.0,0.82,0.68); BLUSH=(1,0.6,0.6)
WALL=(0.98,0.90,0.78); FLOOR=(0.70,0.50,0.34); WOOD=(0.86,0.66,0.44); WOOD_D=(0.64,0.45,0.27)
def stroke_fill(cr,col,lw=7):
    cr.set_source_rgb(*col); cr.fill_preserve(); cr.set_source_rgb(*OL); cr.set_line_width(lw); cr.stroke()
def room(cr,guests=False):
    cr.set_source_rgb(*WALL); cr.paint()
    cr.set_source_rgb(0.95,0.84,0.70)
    for x in range(0,W,90): cr.rectangle(x,0,45,1420); cr.fill()
    cr.set_source_rgb(*FLOOR); cr.rectangle(0,1420,W,H-1420); cr.fill()
    cr.set_source_rgb(0.62,0.43,0.28)
    for y in range(1460,H,90): cr.rectangle(0,y,W,5); cr.fill()
    cr.set_source_rgb(*OL); cr.rectangle(0,1414,W,10); cr.fill()
    # Fenster + Pflanze
    rr(cr,90,620,260,300,14); stroke_fill(cr,(0.70,0.88,1.0)); cr.move_to(220,620); cr.line_to(220,920); cr.move_to(90,770); cr.line_to(350,770); cr.stroke()
    rr(cr,120,1290,90,130,10); stroke_fill(cr,(0.85,0.42,0.30))
    for a in (-0.6,-0.2,0.2,0.6):
        cr.save(); cr.translate(165,1290); cr.rotate(a); cr.scale(1,2.2); cr.arc(0,-40,30,0,2*math.pi); cr.restore(); stroke_fill(cr,(0.35,0.70,0.35),5)
def face(cr,mood,T):
    blink=1 if (T*1.1)%3.2>0.1 else 0.1
    for ex in (-28,28):
        cr.save(); cr.translate(ex,-10); cr.scale(1,blink); cr.arc(0,0,16,0,2*math.pi); cr.restore(); stroke_fill(cr,(1,1,1),4)
        cr.set_source_rgb(*OL); cr.arc(ex+3,-8,7*blink,0,2*math.pi); cr.fill()
    cr.set_source_rgba(*BLUSH,0.6); cr.arc(-50,22,13,0,2*math.pi); cr.fill(); cr.arc(50,22,13,0,2*math.pi); cr.fill()
    cr.set_source_rgb(*OL); cr.set_line_width(6); cr.set_line_cap(cairo.LINE_CAP_ROUND)
    if mood=='happy': cr.arc(0,22,26,0.15*math.pi,0.85*math.pi); cr.stroke()
    elif mood=='proud':
        cr.arc(0,18,30,0.1*math.pi,0.9*math.pi); cr.close_path(); stroke_fill(cr,(0.55,0.15,0.15),5)
    elif mood=='worried':
        cr.move_to(-22,40); cr.curve_to(-8,28,8,28,22,40); cr.stroke()
        cr.move_to(-45,-40); cr.line_to(-15,-32); cr.move_to(45,-40); cr.line_to(15,-32); cr.stroke()
    elif mood=='wink':
        cr.arc(0,22,26,0.15*math.pi,0.85*math.pi); cr.stroke()
    elif mood=='shock':
        cr.arc(0,35,14,0,2*math.pi); stroke_fill(cr,(0.45,0.1,0.1),5)
def char(cr,x,y,who,T,mood='happy',arm_l=0.3,arm_r=0.3,s=1,lean=0,hold=None,walk=0):
    cr.save(); cr.translate(x,y); cr.scale(s,s); cr.rotate(lean)
    cfg={'mann':((0.30,0.55,0.85),(0.25,0.27,0.35),(0.40,0.25,0.12),'short'),
         'frau':((0.92,0.42,0.55),(0.25,0.27,0.40),(0.55,0.30,0.15),'long'),
         'jan':((0.15,0.15,0.17),(0.35,0.36,0.40),None,'cap'),
         'gast1':((0.45,0.75,0.45),(0.3,0.3,0.35),(0.85,0.70,0.30),'long'),
         'gast2':((0.95,0.70,0.25),(0.3,0.3,0.35),(0.20,0.15,0.12),'short'),
         'post':((1.0,0.80,0.10),(0.15,0.20,0.40),(0.35,0.22,0.10),'short'),
         'pizza':((0.85,0.20,0.20),(0.2,0.2,0.22),(0.10,0.08,0.06),'short'),
         'nachbar':((0.55,0.45,0.75),(0.30,0.30,0.32),(0.75,0.75,0.78),'short')}[who]
    shirt,pants,hair,style=cfg
    bob=abs(math.sin(T*8))*8 if walk else math.sin(T*3)*3
    cr.translate(0,-bob)
    # Beine
    sw=math.sin(T*10)*0.35 if walk else 0
    for side,ph in ((-1,sw),(1,-sw)):
        cr.save(); cr.translate(side*24,-150); cr.rotate(ph)
        rr(cr,-18,0,36,140,16); stroke_fill(cr,pants,6)
        rr(cr,-26 if side<0 else -16,130,46,26,12); stroke_fill(cr,OL,2); cr.restore()
    # Arme (hinter Körper links)
    def arm(side,a):
        cr.save(); cr.translate(side*62,-320); cr.rotate(-side*(0.25+a))
        rr(cr,-16,0,32,130,16); stroke_fill(cr,shirt,6)
        cr.arc(0,135,20,0,2*math.pi); stroke_fill(cr,SKIN,5)
        if hold=='phone' and side>0: rr(cr,-18,95,36,62,8); stroke_fill(cr,OL,3); cr.set_source_rgb(0.4,0.8,0.5); rr(cr,-12,102,24,44,4); cr.fill()
        if hold=='screws' and side<0:
            cr.set_source_rgb(0.6,0.62,0.66)
            for k in range(3): rr(cr,-20+k*14,140,8,30,3); cr.fill()
        if hold=='letter' and side>0: rr(cr,-30,120,60,40,4); stroke_fill(cr,(1,1,1),4)
        if hold=='pizzabox' and side>0: rr(cr,-60,110,120,30,4); stroke_fill(cr,(0.85,0.70,0.45),4)
        if hold=='drill' and side>0:
            rr(cr,-30,110,80,40,10); stroke_fill(cr,RED,4); rr(cr,50,122,40,12,5); stroke_fill(cr,(0.7,0.7,0.72),3)
        cr.restore()
    arm(-1,arm_l)
    # Körper
    rr(cr,-68,-340,136,200,52); stroke_fill(cr,shirt,7)
    if who=='jan':
        cr.set_source_rgb(*RED); cr.rectangle(-62,-250,124,16); cr.fill()
    arm(1,arm_r)
    # Kopf
    cr.translate(0,-420)
    if style=='long' and hair:
        rr(cr,-80,-60,160,150,60); stroke_fill(cr,hair,6)
    cr.arc(0,0,78,0,2*math.pi); stroke_fill(cr,SKIN,7)
    if style=='cap':
        cr.arc(0,-8,80,math.pi*1.02,math.pi*1.98); cr.close_path(); stroke_fill(cr,RED,7); rr(cr,10,-26,105,24,12); stroke_fill(cr,RED,6)
    elif hair:
        cr.arc(0,-6,80,math.pi*1.05,math.pi*1.95); cr.close_path(); stroke_fill(cr,hair,6)
        if style=='long':
            cr.arc(-40,-40,30,0,2*math.pi); cr.set_source_rgb(*hair); cr.fill()
    face(cr,mood,T)
    cr.restore()
def wardrobe(cr,x,tilt=0,upside=False,fixed=False,a=1):
    cr.save(); cr.translate(x+150,1420); cr.rotate(tilt); cr.translate(-150,0)
    rr(cr,0,-640,300,640,10); stroke_fill(cr,WOOD,8)
    rr(cr,14,-626,132,560,8); stroke_fill(cr,(0.92,0.76,0.55),5)
    if upside:
        cr.save(); cr.translate(154,-626); rr(cr,0,0,132,520,8); stroke_fill(cr,(0.92,0.76,0.55),5); cr.restore()
        rr(cr,160,-110,24,10,4); stroke_fill(cr,OL,2)
    else:
        rr(cr,154,-626,132,560,8); stroke_fill(cr,(0.92,0.76,0.55),5)
        rr(cr,166,-360,10,60,4); stroke_fill(cr,OL,2)
    rr(cr,124,-360,10,60,4); stroke_fill(cr,OL,2)
    rr(cr,14,-56,272,46,6); stroke_fill(cr,WOOD_D,5)
    cr.restore()
def sweat(cr,x,y,T):
    for i in range(2):
        yy=y+((T*140+i*45)%80)
        cr.move_to(x+i*40,yy-18); cr.curve_to(x+i*40-12,yy,x+i*40-12,yy+14,x+i*40,yy+14); cr.curve_to(x+i*40+12,yy+14,x+i*40+12,yy,x+i*40,yy-18); stroke_fill(cr,(0.55,0.80,1.0),3)
def speech(cr,x,y,w,h,txt,size,a,tail='left',think=False):
    if a<=0: return
    cr.save(); cr.push_group()
    rr(cr,x,y,w,h,40); stroke_fill(cr,(1,1,1),6)
    tx=x+70 if tail=='left' else x+w-70
    cr.move_to(tx-22,y+h-3); cr.line_to(tx+(-10 if tail=='left' else 10),y+h+48); cr.line_to(tx+26,y+h-3); cr.set_source_rgb(1,1,1); cr.fill_preserve(); cr.set_source_rgb(*OL); cr.set_line_width(6); cr.stroke()
    cr.set_source_rgb(1,1,1); cr.rectangle(tx-19,y+h-10,42,12); cr.fill()
    lines=txt.split('\n')
    for i,l in enumerate(lines): text(cr,l,x+w/2,y+h/2+size*0.36+(i-(len(lines)-1)/2)*size*1.2,size,OL)
    cr.pop_group_to_source(); cr.paint_with_alpha(a); cr.restore()
def title(cr,txt,t,sub=None):
    a=ease(t*3)
    cr.save(); cr.translate(0,(1-a)*-40)
    cr.select_font_face("Inter",0,1); cr.set_font_size(62); e=cr.text_extents(txt); w=e.width+80
    rr(cr,(W-w)/2,150,w,110,55); cr.set_source_rgba(1,1,1,0.95*a); cr.fill_preserve(); cr.set_source_rgba(*OL,a); cr.set_line_width(6); cr.stroke()
    text(cr,txt,W/2,226,62,OL,alpha=a)
    cr.restore()
