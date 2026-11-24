# Video-Reel aus echter Handyaufnahme des Inhabers: Hochformat 1080x1920, Logo oben, Text-Einblendungen,
# Schlusskarte mit Logo + Telefon, eigene Musik (ton_lib). Originalton wird entfernt, Metadaten auch.
# Aufruf aus dem Repo-Hauptordner:
#   python3 marketing/reel_video.py <eingabe.mov> <ausgabe.mp4> <start_s> <laenge_s> <texte.json>
# texte.json: [[start_s, "KICKER", "Titel"], ...] (Zeiten relativ zum Clip). Keine Preise (Inhaber-Regel).
import sys, subprocess, os, json
from PIL import Image, ImageDraw, ImageFont, ImageFilter
W,H,FPS=1080,1920,30
F='/usr/share/fonts/opentype/inter/'
fb=lambda s:ImageFont.truetype(F+'Inter-ExtraBold.otf',s); fm=lambda s:ImageFont.truetype(F+'Inter-SemiBold.otf',s)
RED=(215,25,32); END=3.4; XF=0.45
src,out,ss,ln,tj=sys.argv[1],sys.argv[2],float(sys.argv[3]),float(sys.argv[4]),sys.argv[5]
CAPS=json.load(open(tj,encoding='utf-8'))
LOGO=Image.open('public/img/signatur-logo-dunkel.png').convert('RGBA')
def logo_img(w): return LOGO.resize((w,int(LOGO.height*w/LOGO.width)),Image.LANCZOS)
LG_SMALL=logo_img(330); LG_BIG=logo_img(760)
SH=Image.new('RGBA',LG_SMALL.size,(0,0,0,0)); SH.putalpha(LG_SMALL.split()[3].point(lambda a:int(a*0.55))); SH=SH.filter(ImageFilter.GaussianBlur(8))
def ease(x): x=max(0,min(1,x)); return 1-(1-x)**3
def wrap(d,t,f,mw):
    o=[];l=''
    for w in t.split():
        c=(l+' '+w).strip()
        if d.textlength(c,font=f)<=mw: l=c
        else: o.append(l); l=w
    o.append(l); return o
GRAD=Image.new('RGBA',(W,H),(0,0,0,0)); g=ImageDraw.Draw(GRAD)
for y in range(H-900,H): g.line([(0,y),(W,y)],fill=(0,0,0,int(215*min(1,(y-(H-900))/600))))
for y in range(0,300): g.line([(0,y),(W,y)],fill=(0,0,0,int(140*(1-y/300))))
def overlay(fr,t):
    fr=Image.alpha_composite(fr.convert('RGBA'),GRAD)
    x0=(W-LG_SMALL.width)//2; fr.alpha_composite(SH,(x0+3,75)); fr.alpha_composite(LG_SMALL,(x0,70))
    cur=None
    for i,(st,k,ti) in enumerate(CAPS):
        nx=CAPS[i+1][0] if i+1<len(CAPS) else ln
        if st<=t<nx: cur=(st,nx,k,ti)
    if cur:
        st,nx,k,ti=cur; a=min(ease((t-st-0.2)/0.5),ease((nx-t)/0.35)); off=int((1-ease((t-st-0.2)/0.5))*80)
        tx=Image.new('RGBA',(W,H),(0,0,0,0)); td=ImageDraw.Draw(tx); y=H-640
        td.rectangle([80,y+off,90,y+46+off],fill=RED+(255,)); td.text((110,y-2+off),k,font=fm(38),fill=(255,255,255,255))
        yy=y+90+off
        for l in wrap(td,ti,fb(84),W-160): td.text((80,yy),l,font=fb(84),fill=(255,255,255,255)); yy+=100
        tx.putalpha(tx.split()[3].point(lambda v:int(v*a))); fr.alpha_composite(tx)
    d=ImageDraw.Draw(fr); d.rectangle([0,H-16,W,H],fill=RED)
    return fr.convert('RGB')
def end_frame(t):
    fr=Image.new('RGB',(W,H),(14,14,15)); d=ImageDraw.Draw(fr)
    a=ease(t/0.6); lg=LG_BIG.copy(); lg.putalpha(lg.split()[3].point(lambda v:int(v*a)))
    fr.paste(lg,((W-lg.width)//2,560-int((1-a)*40)),lg)
    b=ease((t-0.5)/0.6)
    if b>0:
        for s,f,y,c in [('0176 23751407',fb(92),1020,255),('Anrufen oder per WhatsApp',fm(42),1140,200),('Jülich · Düren · Aachen · Köln',fm(38),1260,170)]:
            w=d.textlength(s,font=f); d.text(((W-w)/2,y),s,font=f,fill=(int(c*b),)*3)
        d.rectangle([W//2-60,1350,W//2+60,1358],fill=RED)
    d.rectangle([0,H-16,W,H],fill=RED)
    return fr
tmpv=out+'.v.mp4'; tmpa=out+'.wav'
rd=subprocess.Popen(['ffmpeg','-v','error','-ss',str(ss),'-t',str(ln),'-i',src,'-vf',f'scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},fps={FPS}','-f','rawvideo','-pix_fmt','rgb24','-'],stdout=subprocess.PIPE)
wr=subprocess.Popen(['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','rgb24','-s',f'{W}x{H}','-r',str(FPS),'-i','-','-c:v','libx264','-pix_fmt','yuv420p','-crf','20','-preset','medium',tmpv],stdin=subprocess.PIPE)
n=int(ln*FPS); last=None
for i in range(n):
    raw=rd.stdout.read(W*H*3)
    if len(raw)<W*H*3: break
    fr=Image.frombytes('RGB',(W,H),raw); t=i/FPS
    o=overlay(fr,t); rem=ln-t
    if rem<XF: o=Image.blend(o,end_frame(0),1-rem/XF)
    wr.stdin.write(o.tobytes()); last=i
for i in range(int(END*FPS)): wr.stdin.write(end_frame(i/FPS).tobytes())
wr.stdin.close(); wr.wait(); rd.stdout.close(); rd.wait()
total=(last+1)/FPS+END
code=f"""import sys;sys.argv=['x','{tmpa}','{total}'];sys.path.insert(0,'marketing')
from ton_lib import *
for s in {[c[0] for c in CAPS[1:]]+[round(ln,2)]}: whoosh(s-0.25,0.5,0.05)
ding({round(ln,2)}+0.6,1046.5,0.12)
finish(sys.argv[1])"""
subprocess.run([sys.executable,'-c',code],check=True)
subprocess.run(['ffmpeg','-v','error','-y','-i',tmpv,'-i',tmpa,'-map_metadata','-1','-c:v','copy','-c:a','aac','-b:a','160k','-shortest','-movflags','+faststart',out],check=True)
os.remove(tmpv); os.remove(tmpa); print('ok',out,round(total,1),'s')
