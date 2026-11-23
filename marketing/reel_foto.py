# Foto-Reel im Firmenstil (echte Fotos, Ken-Burns-Zoom, Text-Einblendung, Logo-Schlusskarte, eigene Musik).
# Aufruf aus dem Repo-Hauptordner: python3 marketing/reel_foto.py <ausgabe.mp4>
# Szenen unten anpassen. Keine gezeichneten Figuren (Inhaber-Regel).
import sys, subprocess, math, os
from PIL import Image, ImageDraw, ImageFont, ImageFilter
W,H,FPS=1080,1920,30
F='/usr/share/fonts/opentype/inter/'
fb=lambda s:ImageFont.truetype(F+'Inter-ExtraBold.otf',s); fm=lambda s:ImageFont.truetype(F+'Inter-SemiBold.otf',s)
RED=(215,25,32)
LOGO=Image.open('public/img/signatur-logo-dunkel.png').convert('RGBA')
SCENES=[ # (foto, kicker, titel, dauer, zoom_richtung)
 ('public/img/heckenschnitt.jpg','HECKE & GARTEN','Wir bringen Ihren Garten in Form.',3.6,1),
 ('public/img/einfahrt-gartenpflege.jpg','HAUSMEISTERSERVICE','Fester Ansprechpartner. Feste Preise.',3.6,-1),
 ('public/img/gartentor-montage.jpg','ZAUN & TOR','Abbau, Entsorgung, Montage – alles aus einer Hand.',3.6,1),
]
END=3.4; XF=0.45
def wrap(d,t,f,mw):
    o=[];l=''
    for w in t.split():
        c=(l+' '+w).strip()
        if d.textlength(c,font=f)<=mw: l=c
        else: o.append(l); l=w
    o.append(l); return o
def ease(x): x=max(0,min(1,x)); return 1-(1-x)**3
def logo_img(w):
    s=w/LOGO.width; return LOGO.resize((w,int(LOGO.height*s)),Image.LANCZOS)
LG_SMALL=logo_img(330); LG_BIG=logo_img(760)
def shadow(lg):
    sh=Image.new('RGBA',lg.size,(0,0,0,0)); sh.putalpha(lg.split()[3].point(lambda a:int(a*0.55))); return sh.filter(ImageFilter.GaussianBlur(8))
SH_SMALL=shadow(LG_SMALL)
cache={}
def base(path):
    if path not in cache:
        im=Image.open(path).convert('RGB'); s=max(W*1.18/im.width,H*1.18/im.height)
        cache[path]=im.resize((int(im.width*s),int(im.height*s)),Image.LANCZOS)
    return cache[path]
def scene_frame(sc,t):
    path,kick,title,dur,dirn=sc; im=base(path); p=t/dur
    z=1+0.12*(p if dirn>0 else 1-p); cw=int(W*1.18/z); ch=int(H*1.18/z)
    cx=(im.width-cw)//2; cy=(im.height-ch)//2
    fr=im.crop((cx,cy,cx+cw,cy+ch)).resize((W,H),Image.LANCZOS).convert('RGBA')
    ov=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(ov)
    for y in range(H-900,H): d.line([(0,y),(W,y)],fill=(0,0,0,int(215*min(1,(y-(H-900))/600))))
    for y in range(0,300): d.line([(0,y),(W,y)],fill=(0,0,0,int(140*(1-y/300))))
    fr=Image.alpha_composite(fr,ov); d=ImageDraw.Draw(fr)
    x0=(W-LG_SMALL.width)//2; fr.alpha_composite(SH_SMALL,(x0+3,75)); fr.alpha_composite(LG_SMALL,(x0,70))
    a=ease((t-0.25)/0.5); off=int((1-a)*80)
    fk=fm(38); y=H-640
    tx=Image.new('RGBA',(W,H),(0,0,0,0)); td=ImageDraw.Draw(tx)
    td.rectangle([80,y+off,90,y+46+off],fill=RED+(255,)); td.text((110,y-2+off),kick,font=fk,fill=(255,255,255,255))
    ft=fb(84); yy=y+90+off
    for ln in wrap(td,title,ft,W-160): td.text((80,yy),ln,font=ft,fill=(255,255,255,255)); yy+=100
    al=tx.split()[3].point(lambda v:int(v*a)); tx.putalpha(al); fr.alpha_composite(tx)
    d.rectangle([0,H-16,W,H],fill=RED)
    return fr.convert('RGB')
def end_frame(t):
    fr=Image.new('RGB',(W,H),(14,14,15)); d=ImageDraw.Draw(fr)
    a=ease(t/0.6); lg=LG_BIG.copy(); lg.putalpha(lg.split()[3].point(lambda v:int(v*a)))
    fr.paste(lg,((W-lg.width)//2,560-int((1-a)*40)),lg)
    b=ease((t-0.5)/0.6)
    if b>0:
        c=int(255*b); f1=fb(92); s='0176 23751407'; w=d.textlength(s,font=f1); d.text(((W-w)/2,1020),s,font=f1,fill=(c,c,c))
        f2=fm(42); s2='Anrufen oder per WhatsApp'; w2=d.textlength(s2,font=f2); d.text(((W-w2)/2,1140),s2,font=f2,fill=(int(200*b),)*3)
        f3=fm(38); s3='Jülich · Düren · Aachen · Köln'; w3=d.textlength(s3,font=f3); d.text(((W-w3)/2,1260),s3,font=f3,fill=(int(170*b),)*3)
        d.rectangle([W//2-60,1350,W//2+60,1358],fill=RED)
    d.rectangle([0,H-16,W,H],fill=RED)
    return fr
total=sum(s[3] for s in SCENES)+END
starts=[];t=0
for s in SCENES: starts.append(t); t+=s[3]
out=sys.argv[1]; tmpv=out+'.v.mp4'; tmpa=out+'.wav'
p=subprocess.Popen(['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','rgb24','-s',f'{W}x{H}','-r',str(FPS),'-i','-','-c:v','libx264','-pix_fmt','yuv420p','-crf','20','-preset','medium',tmpv],stdin=subprocess.PIPE)
n=int(total*FPS)
for i in range(n):
    tt=i/FPS; k=None
    for j,st in enumerate(starts):
        if st<=tt<st+SCENES[j][3]: k=j
    if k is None: fr=end_frame(tt-sum(s[3] for s in SCENES))
    else:
        lt=tt-starts[k]; fr=scene_frame(SCENES[k],lt)
        rem=SCENES[k][3]-lt
        if rem<XF:
            nxt=scene_frame(SCENES[k+1],0) if k+1<len(SCENES) else end_frame(0)
            fr=Image.blend(fr,nxt,1-rem/XF)
    p.stdin.write(fr.tobytes())
p.stdin.close(); p.wait()
# Musik: ton_lib erzeugt Grundmusik beim Import (argv: datei, dauer)
code=f"""import sys;sys.argv=['x','{tmpa}','{total}'];sys.path.insert(0,'marketing')
from ton_lib import *
for s in {[round(x,2) for x in starts[1:]]+[round(sum(s[3] for s in SCENES),2)]}: whoosh(s-0.25,0.5,0.05)
ding({round(sum(s[3] for s in SCENES),2)}+0.6,1046.5,0.12)
finish(sys.argv[1])"""
subprocess.run([sys.executable,'-c',code],check=True)
subprocess.run(['ffmpeg','-v','error','-y','-i',tmpv,'-i',tmpa,'-c:v','copy','-c:a','aac','-b:a','160k','-shortest','-movflags','+faststart',out],check=True)
os.remove(tmpv); os.remove(tmpa); print('ok',out,round(total,1),'s')
