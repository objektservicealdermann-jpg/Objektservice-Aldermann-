import cairo, math, subprocess, sys, random
W,H,FPS=1080,1920,30
OUT=sys.argv[1]
RED=(215/255,25/255,32/255); INK=(0.08,0.08,0.09); WHITE=(1,1,1)
SKY=(0.89,0.94,0.98); GRASS=(0.42,0.70,0.33); GRASS_D=(0.30,0.55,0.25)
SKIN=(0.98,0.80,0.66); HEDGE=(0.22,0.52,0.24); HEDGE_L=(0.30,0.62,0.30)
logo=cairo.ImageSurface.create_from_png('logo.png')
logo_d=cairo.ImageSurface.create_from_png('logo_dark.png')
def ease(t): t=max(0,min(1,t)); return t*t*(3-2*t)
def back(t):
    t=max(0,min(1,t)); c=1.7; return 1+(c+1)*(t-1)**3+c*(t-1)**2
def rr(cr,x,y,w,h,r):
    cr.new_sub_path(); cr.arc(x+w-r,y+r,r,-math.pi/2,0); cr.arc(x+w-r,y+h-r,r,0,math.pi/2)
    cr.arc(x+r,y+h-r,r,math.pi/2,math.pi); cr.arc(x+r,y+r,r,math.pi,3*math.pi/2); cr.close_path()
def text(cr,s,x,y,size,col=INK,bold=True,center=True,alpha=1):
    cr.select_font_face("Inter",cairo.FONT_SLANT_NORMAL,cairo.FONT_WEIGHT_BOLD if bold else cairo.FONT_WEIGHT_NORMAL)
    cr.set_font_size(size); e=cr.text_extents(s)
    cr.move_to(x-(e.width/2+e.x_bearing) if center else x,y); cr.set_source_rgba(*col,alpha); cr.show_text(s)
def bg(cr):
    cr.set_source_rgb(*SKY); cr.paint()
    # Wolken
    for cx,cy,s in [(220,520,1),(820,430,0.8)]:
        cr.set_source_rgb(1,1,1)
        for dx,dy,r in [(0,0,50),(55,-20,60),(115,0,45)]:
            cr.arc(cx+dx*s,cy+dy*s,r*s,0,2*math.pi); cr.fill()
    cr.set_source_rgb(*GRASS); cr.rectangle(0,1380,W,H-1380); cr.fill()
    cr.set_source_rgb(*GRASS_D); cr.rectangle(0,1380,W,10); cr.fill()
def house(cr,x,y,s=1):
    cr.save(); cr.translate(x,y); cr.scale(s,s)
    cr.set_source_rgb(0.96,0.93,0.88); cr.rectangle(-170,-260,340,260); cr.fill()
    cr.set_source_rgb(*RED); cr.move_to(-200,-250); cr.line_to(0,-420); cr.line_to(200,-250); cr.close_path(); cr.fill()
    cr.set_source_rgb(*INK); cr.set_line_width(10); cr.move_to(-200,-250); cr.line_to(0,-420); cr.line_to(200,-250); cr.stroke()
    cr.set_source_rgb(0.45,0.30,0.20); rr(cr,-35,-130,70,130,8); cr.fill()
    for wx in (-120,60):
        cr.set_source_rgb(0.65,0.82,0.95); cr.rectangle(wx,-200,60,60); cr.fill()
        cr.set_source_rgb(*INK); cr.set_line_width(5); cr.rectangle(wx,-200,60,60); cr.stroke()
        cr.move_to(wx+30,-200); cr.line_to(wx+30,-140); cr.move_to(wx,-170); cr.line_to(wx+60,-170); cr.stroke()
    cr.restore()
def hedge(cr,x,y,w,messy):
    # messy 1 = wild, 0 = ordentlich
    cr.set_source_rgb(*HEDGE)
    h=150
    if messy<=0.01:
        rr(cr,x,y-h,w,h,24); cr.fill()
        cr.set_source_rgb(*HEDGE_L); rr(cr,x+10,y-h+10,w-20,30,14); cr.fill()
    else:
        random.seed(3)
        rr(cr,x,y-h,w,h,24); cr.fill()
        for i in range(16):
            bx=x+random.uniform(0,w); by=y-h+random.uniform(-10,40); r=random.uniform(30,60)*messy
            cr.arc(bx,by-r*0.6,r,0,2*math.pi); cr.fill()
        cr.set_source_rgb(*HEDGE_L)
        for i in range(10):
            bx=x+random.uniform(0,w); by=y-h+random.uniform(-40,20); r=random.uniform(12,24)*messy
            cr.arc(bx,by-r,r,0,2*math.pi); cr.fill()
def person(cr,x,y,kind,t=0,arm=0,thumb=False,phone=False,clip=False,s=1):
    cr.save(); cr.translate(x,y); cr.scale(s,s)
    bob=math.sin(t*6)*4
    cr.translate(0,bob)
    shirt=INK if kind=='jan' else (0.25,0.47,0.80)
    pants=(0.35,0.36,0.40) if kind=='jan' else (0.20,0.22,0.30)
    # Beine
    cr.set_source_rgb(*pants); cr.set_line_width(30); cr.set_line_cap(cairo.LINE_CAP_ROUND)
    cr.move_to(-22,-120); cr.line_to(-26,0); cr.move_to(22,-120); cr.line_to(26,0); cr.stroke()
    cr.set_source_rgb(*INK); rr(cr,-48,-8,46,20,9); cr.fill(); rr(cr,2,-8,46,20,9); cr.fill()
    # Körper
    cr.set_source_rgb(*shirt); rr(cr,-58,-290,116,190,40); cr.fill()
    if kind=='jan':
        cr.set_source_rgb(*RED); cr.rectangle(-58,-200,116,14); cr.fill()
    # Arme
    cr.set_line_width(26); cr.set_source_rgb(*shirt)
    cr.move_to(-50,-260); cr.line_to(-80,-170); cr.stroke()
    a=-0.9-arm*1.2
    ex=50+math.cos(a)*95; ey=-260+math.sin(a)*-(-95)
    ex=50+95*math.sin(0.5+arm*1.6); ey=-260+95*math.cos(0.5+arm*1.6)
    cr.move_to(50,-260); cr.line_to(ex,ey); cr.stroke()
    cr.set_source_rgb(*SKIN); cr.arc(-80,-170,15,0,2*math.pi); cr.fill(); cr.arc(ex,ey,15,0,2*math.pi); cr.fill()
    if thumb:
        cr.set_source_rgb(*SKIN); rr(cr,ex-6,ey-38,13,30,6); cr.fill()
    if phone:
        cr.set_source_rgb(*INK); rr(cr,ex-16,ey-58,32,56,6); cr.fill()
        cr.set_source_rgb(0.35,0.75,0.45); rr(cr,ex-11,ey-52,22,40,4); cr.fill()
    if clip:
        cr.set_source_rgb(0.55,0.38,0.22); rr(cr,-118,-225,62,80,6); cr.fill()
        cr.set_source_rgb(1,1,1); rr(cr,-111,-214,48,62,3); cr.fill()
        cr.set_source_rgb(*INK); cr.set_line_width(4)
        for k in range(4): cr.move_to(-105,-202+k*13); cr.line_to(-70,-202+k*13)
        cr.stroke()
    # Kopf
    cr.set_source_rgb(*SKIN); cr.arc(0,-345,58,0,2*math.pi); cr.fill()
    if kind=='jan':
        cr.set_source_rgb(*RED); cr.arc(0,-360,60,math.pi,2*math.pi); cr.fill()
        rr(cr,0,-372,88,18,9); cr.fill()
    else:
        cr.set_source_rgb(0.45,0.27,0.15); cr.arc(0,-360,62,math.pi*0.95,2.05*math.pi); cr.fill()
        rr(cr,-64,-370,26,90,12); cr.fill(); rr(cr,38,-370,26,90,12); cr.fill()
    cr.set_source_rgb(*INK)
    blink=1 if (t*1.3)%3>0.08 else 0.15
    for ex2 in (-20,20):
        cr.save(); cr.translate(ex2,-345); cr.scale(1,blink); cr.arc(0,0,7,0,2*math.pi); cr.fill(); cr.restore()
    cr.set_line_width(5); cr.arc(0,-330,22,0.2*math.pi,0.8*math.pi); cr.stroke()
    cr.restore()
def van(cr,x,y):
    cr.save(); cr.translate(x,y)
    cr.set_source_rgb(1,1,1); rr(cr,-260,-230,420,190,26); cr.fill()
    cr.move_to(160,-200); cr.line_to(250,-140); cr.line_to(250,-40); cr.line_to(160,-40); cr.close_path(); cr.fill()
    cr.set_source_rgb(*INK); cr.set_line_width(8); rr(cr,-260,-230,420,190,26); cr.stroke()
    cr.move_to(160,-200); cr.line_to(250,-140); cr.line_to(250,-40); cr.line_to(160,-40); cr.stroke()
    cr.set_source_rgb(0.65,0.82,0.95); cr.move_to(175,-185); cr.line_to(235,-145); cr.line_to(175,-145); cr.close_path(); cr.fill()
    cr.set_source_rgb(*RED); cr.rectangle(-256,-110,412,16); cr.fill()
    cr.save(); sc=300/logo.get_width(); cr.translate(-210,-215); cr.scale(sc,sc); cr.set_source_surface(logo,0,0); cr.paint(); cr.restore()
    for wx in (-160,150):
        cr.set_source_rgb(*INK); cr.arc(wx,-40,44,0,2*math.pi); cr.fill()
        cr.set_source_rgb(0.75,0.75,0.78); cr.arc(wx,-40,18,0,2*math.pi); cr.fill()
    cr.restore()
def bubble(cr,x,y,w,h,txt,size=44,alpha=1,tail='left'):
    cr.save(); cr.push_group()
    cr.set_source_rgb(1,1,1); rr(cr,x,y,w,h,28); cr.fill()
    tx=x+60 if tail=='left' else x+w-60
    cr.move_to(tx-20,y+h-2); cr.line_to(tx-5,y+h+40); cr.line_to(tx+25,y+h-2); cr.close_path(); cr.fill()
    cr.set_source_rgb(*INK); cr.set_line_width(5); rr(cr,x,y,w,h,28); cr.stroke()
    lines=txt.split('\n')
    for i,l in enumerate(lines): text(cr,l,x+w/2,y+h/2+size*0.35+(i-(len(lines)-1)/2)*size*1.25,size)
    cr.pop_group_to_source(); cr.paint_with_alpha(alpha); cr.restore()
def caption(cr,step,title,sub,t):
    a=ease(t*3)
    cr.save(); cr.translate(0,(1-a)*-60)
    cr.set_source_rgba(*INK,a); rr(cr,70,170,W-140,230,30); cr.fill()
    if step:
        cr.set_source_rgba(*RED,a); cr.arc(170,285,55,0,2*math.pi); cr.fill()
        text(cr,str(step),170,307,64,WHITE,alpha=a)
        text(cr,title,260,280,64,WHITE,center=False,alpha=a); text(cr,sub,262,352,40,(0.85,0.85,0.85),bold=False,center=False,alpha=a)
    else:
        text(cr,title,W/2,280,70,WHITE,alpha=a); text(cr,sub,W/2,350,40,(0.85,0.85,0.85),bold=False,alpha=a)
    cr.restore()
def logo_top(cr,alpha=1):
    cr.save(); sc=520/logo.get_width(); w=520; h=logo.get_height()*sc
    cr.set_source_rgba(1,1,1,alpha); rr(cr,(W-w)/2-30,40,w+60,h+30,22); cr.fill()
    cr.translate((W-w)/2,55); cr.scale(sc,sc); cr.set_source_surface(logo,0,0); cr.paint_with_alpha(alpha); cr.restore()
def star(cr,cx,cy,r):
    cr.move_to(cx,cy-r)
    for i in range(1,10):
        a=-math.pi/2+i*math.pi/5; rad=r if i%2==0 else r*0.45
        cr.line_to(cx+rad*math.cos(a),cy+rad*math.sin(a))
    cr.close_path(); cr.fill()
def fade(cr,t,d):
    a=0
    if t<0.25: a=1-t/0.25
    elif t>d-0.25: a=(t-(d-0.25))/0.25
    if a>0: cr.set_source_rgba(1,1,1,a); cr.paint()

SC=[('intro',3.4),('anfrage',4.2),('besuch',4.6),('angebot',4.0),('fertig',5.0),('ende',4.5)]
p=subprocess.Popen(['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','bgra','-s',f'{W}x{H}','-r',str(FPS),'-i','-',
  '-f','lavfi','-i','anullsrc=r=44100:cl=stereo','-shortest','-c:v','libx264','-crf','22','-preset','slow','-pix_fmt','yuv420p','-c:a','aac','-b:a','64k','-movflags','+faststart',OUT],stdin=subprocess.PIPE)
surf=cairo.ImageSurface(cairo.FORMAT_ARGB32,W,H)
G=0
for name,d in SC:
    n=int(d*FPS)
    for f in range(n):
        t=f/FPS; T=G+t; cr=cairo.Context(surf); cr.set_antialias(cairo.ANTIALIAS_BEST)
        if name=='ende':
            cr.set_source_rgb(0,0,0); cr.paint()
            a=ease(t*2)
            sc=860/logo_d.get_width(); cr.save(); cr.translate((W-860)/2,560+(1-a)*40); cr.scale(sc,sc); cr.set_source_surface(logo_d,0,0); cr.paint_with_alpha(a); cr.restore()
            text(cr,'Hausmeisterservice · Gartenpflege',W/2,880,44,(0.85,0.85,0.85),bold=False,alpha=a)
            text(cr,'Winterdienst · Reparaturen',W/2,940,44,(0.85,0.85,0.85),bold=False,alpha=a)
            cr.set_source_rgba(*RED,a); cr.rectangle(W/2-70,990,140,8); cr.fill()
            b=ease((t-0.5)*2)
            text(cr,'0176 23751407',W/2,1130,100,WHITE,alpha=b)
            text(cr,'objektservicealdermann.com',W/2,1220,46,(0.85,0.85,0.85),bold=False,alpha=b)
            c=ease((t-1.0)*2)
            text(cr,'Jülich · Düren · Aachen',W/2,1380,42,(0.65,0.65,0.68),bold=False,alpha=c)
            text(cr,'Köln · Düsseldorf · Umgebung',W/2,1440,42,(0.65,0.65,0.68),bold=False,alpha=c)
            cr.set_source_rgba(*RED,c); rr(cr,W/2-300,1560,600,110,55); cr.fill()
            text(cr,'Jetzt anfragen!',W/2,1632,54,WHITE,alpha=c)
            fade(cr,t,d+1)
        else:
            bg(cr)
            if name=='intro':
                hx=W/2; s=back(t*1.5)
                house(cr,hx,1400,0.2+0.8*s)
                hedge(cr,80,1420,260,1); hedge(cr,W-340,1420,260,1)
                logo_top(cr,ease(t*2))
                a=ease((t-0.5)*2)
                cr.set_source_rgba(*INK,a); rr(cr,90,330,W-180,250,34); cr.fill()
                text(cr,'So einfach läuft’s',W/2,440,80,WHITE,alpha=a)
                text(cr,'In 4 Schritten zum gepflegten Objekt',W/2,520,40,(0.85,0.85,0.85),bold=False,alpha=a)
            elif name=='anfrage':
                house(cr,760,1400,0.85); hedge(cr,40,1420,380,1)
                person(cr,330,1560,'kunde',T,arm=0.9,phone=True)
                caption(cr,1,'Anfrage','Anruf oder WhatsApp genügt',t)
                if t>0.6: bubble(cr,130,700,620,190,'Hallo! Können Sie\nmeine Hecke schneiden?',44,ease((t-0.6)*3))
                if t>2.0: bubble(cr,380,950,620,150,'Klar! Ich komme vorbei 👍'.replace(' 👍',''),46,ease((t-2.0)*3),tail='right')
            elif name=='besuch':
                house(cr,760,1400,0.85); hedge(cr,40,1420,380,1)
                vx=-500+ease(t/1.6)*720
                van(cr,vx,1700)
                jx=420+ease((t-1.8)/1.0)*120
                if t>1.6: person(cr,jx,1640,'jan',T,arm=0.3+0.3*math.sin(T*3),clip=True,s=0.95)
                person(cr,900,1640,'kunde',T,arm=0.2,s=0.95)
                caption(cr,2,'Besichtigung','Kostenlos und unverbindlich vor Ort',t)
            elif name=='angebot':
                house(cr,760,1400,0.85); hedge(cr,40,1420,380,1)
                person(cr,900,1640,'kunde',T,arm=0.2,s=0.95)
                caption(cr,3,'Festes Angebot','Schriftlich – mit Festpreis',t)
                a=back((t-0.2)*1.4); y=1500-a*560
                cr.save(); cr.translate(W/2-40,y); cr.rotate((1-a)*0.5)
                cr.set_source_rgb(1,1,1); rr(cr,-230,-300,460,600,20); cr.fill()
                cr.set_source_rgb(*INK); cr.set_line_width(6); rr(cr,-230,-300,460,600,20); cr.stroke()
                text(cr,'ANGEBOT',0,-200,58)
                cr.set_source_rgb(0.75,0.75,0.78)
                for k in range(5): rr(cr,-170,-140+k*55,340-(k%2)*90,18,9); cr.fill()
                cr.set_source_rgb(*RED); cr.set_line_width(5)
                if t>1.6:
                    st=ease((t-1.6)*4); cr.save(); cr.translate(60,190); cr.rotate(-0.2); cr.scale(0.6+0.4*st,0.6+0.4*st)
                    cr.set_source_rgba(*RED,st); rr(cr,-150,-55,300,110,16); cr.set_line_width(10); cr.stroke()
                    text(cr,'FESTPREIS',0,22,54,RED,alpha=st); cr.restore()
                cr.restore()
            elif name=='fertig':
                house(cr,760,1400,0.85)
                m=1-ease((t-0.8)/1.4)
                hedge(cr,40,1420,380,m)
                # Schnitt-Animation
                if 0.8<t<2.2:
                    random.seed(int(T*20))
                    cr.set_source_rgb(*HEDGE_L)
                    for i in range(10):
                        lx=60+random.uniform(0,340); ly=1200+random.uniform(0,200)+ (t-0.8)*120
                        cr.arc(lx,ly,random.uniform(5,12),0,2*math.pi); cr.fill()
                person(cr,500,1640,'jan',T,arm=0.4+0.5*math.sin(T*10) if t<2.2 else 0.2,s=0.95)
                person(cr,900,1640,'kunde',T,arm=1.0 if t>2.4 else 0.2,thumb=t>2.4,s=0.95)
                caption(cr,4,'Sauber erledigt','Zuverlässig – und wieder schön',t)
                if t>2.6:
                    cr.set_source_rgb(0.98,0.75,0.10)
                    for i in range(5):
                        a=back((t-2.6-i*0.12)*3)
                        if a>0: star(cr,W/2-240+i*120,700,55*a)
                    if t>3.4: bubble(cr,170,820,740,150,'Top Arbeit – gerne wieder!',48,ease((t-3.4)*3),tail='right')
                # Glanz
                if t>2.2:
                    cr.set_source_rgba(1,1,1,0.9*abs(math.sin(T*4)))
                    for sx,sy in [(120,1230),(300,1250),(220,1300)]:
                        star(cr,sx,sy,18)
            fade(cr,t,d)
        p.stdin.write(bytes(surf.get_data()))
    G+=d
p.stdin.close(); p.wait(); print('fertig')
