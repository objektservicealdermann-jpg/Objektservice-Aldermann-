import sys
sys.path.insert(0,'.')
from cartoon_lib import *
import math, random
OUT=sys.argv[1]
SC=[('intro',3.2),('bau',4.4),('handy',2.8),('jan',2.6),('gaeste',4.6),('ende',3.8)]
def draw(cr,name,t,T,d):
    if name=='ende':
        cr.set_source_rgb(0.08,0.08,0.09); cr.paint()
        a=ease(t*2); sc=min(700/logo_d.get_width(),280/logo_d.get_height()); lw=logo_d.get_width()*sc
        cr.save(); cr.translate((W-lw)/2,560); cr.scale(sc,sc); cr.set_source_surface(logo_d,0,0); cr.paint_with_alpha(a); cr.restore()
        b=ease((t-0.4)*2)
        text(cr,'Möbelmontage.',W/2,1000,74,WHITE,alpha=b)
        text(cr,'Auf Wunsch auch ganz diskret.',W/2,1090,52,(1,0.8,0.8),alpha=b)
        c=ease((t-1.0)*2)
        text(cr,'0176 23751407',W/2,1280,92,WHITE,alpha=c)
        text(cr,'objektservicealdermann.com',W/2,1360,44,(0.8,0.8,0.82),bold=False,alpha=c)
        fade(cr,t,d+1); return
    room(cr)
    if name=='intro':
        title(cr,'„Schatz, das mach ich selbst!“',t)
        rr(cr,560,1180,300,240,10); stroke_fill(cr,(0.80,0.64,0.42),7); text(cr,'SCHRANK',710,1310,40,(0.5,0.35,0.2))
        char(cr,380,1760,'mann',T,'proud',arm_l=0.2,arm_r=2.6+0.2*math.sin(T*6),hold='drill',s=1.0)
        char(cr,880,1760,'frau',T,'worried',arm_l=0.3,arm_r=0.3,s=0.95)
    elif name=='bau':
        title(cr,'2 Stunden später …',t)
        tilt=min(0.22,max(0,(t-1.6)*0.12))
        wardrobe(cr,520,tilt=tilt,upside=True)
        char(cr,330,1760,'mann',T,'worried',arm_l=0.6,arm_r=0.4,hold='screws',s=1.0)
        sweat(cr,400,1240,T)
        speech(cr,80,620,560,170,'Passt schon …',62,ease((t-0.6)*3))
        if t>2.2: speech(cr,80,840,640,170,'Und die 3 Schrauben\nsind übrig, oder?',48,ease((t-2.2)*3))
    elif name=='handy':
        title(cr,'Währenddessen …',t)
        char(cr,540,1780,'frau',T,'wink',arm_l=0.3,arm_r=2.2,hold='phone',s=1.1)
        a=ease((t-0.3)*3)
        cr.save(); cr.push_group()
        rr(cr,160,560,760,300,40); stroke_fill(cr,(0.88,0.97,0.88),6)
        text(cr,'An: Objektservice Aldermann',540,640,40,(0.2,0.45,0.25))
        text(cr,'„Bitte morgen kommen.',540,730,54,OL); text(cr,'Und nichts meinem Mann sagen.“',540,800,44,OL)
        cr.pop_group_to_source(); cr.paint_with_alpha(a); cr.restore()
    elif name=='jan':
        title(cr,'Am nächsten Morgen …',t)
        wardrobe(cr,520,fixed=True)
        jx=200+ease(t/0.8)*120
        char(cr,jx,1760,'jan',T,'wink' if t>1.2 else 'happy',arm_l=0.3,arm_r=2.4 if t>1.2 else 0.3,s=1.0)
        if t>1.2:
            cr.set_source_rgb(1,0.85,0.2)
            for k in range(3): 
                s=back((t-1.2-k*0.1)*3)*22
                if s>0:
                    cx,cy=640+k*90,780+k*40; cr.move_to(cx,cy-s)
                    for i in range(1,10): an=-math.pi/2+i*math.pi/5; rad=s if i%2==0 else s*0.45; cr.line_to(cx+rad*math.cos(an),cy+rad*math.sin(an))
                    cr.close_path(); cr.fill()
    elif name=='gaeste':
        title(cr,'Am Wochenende …',t)
        wardrobe(cr,620,fixed=True)
        char(cr,170,1760,'gast1',T,'shock' if t>1.6 else 'happy',s=0.85)
        char(cr,370,1760,'gast2',T,'shock' if t>1.6 else 'happy',s=0.85)
        char(cr,560,1760,'mann',T,'proud',arm_l=0.3,arm_r=2.0,s=1.0)
        char(cr,900,1760,'frau',T,'wink' if t>2.6 else 'happy',arm_l=0.3,arm_r=0.3,s=0.95)
        speech(cr,90,600,900,170,'Hab ich alles selbst gebaut!',54,ease((t-0.5)*3),tail='right')
        if t>2.6:
            a=ease((t-2.6)*3)
            speech(cr,620,880,380,150,'Klar, Schatz.',52,a,tail='right')
    fade(cr,t,d)
render(OUT,SC,draw)
print('ok')
