# Instagram-Bild im Firmenstil: make(foto, W, H, kicker, titel, text, fuss, ausgabe, ratio) – Logo groß oben mittig ohne Hintergrund. Aus dem Repo-Hauptordner aufrufen.
from PIL import Image, ImageDraw, ImageFont, ImageOps, ImageFilter
F='/usr/share/fonts/opentype/inter/'
def font(w,s): return ImageFont.truetype(F+{'b':'Inter-Bold.otf','x':'Inter-ExtraBold.otf','m':'Inter-Medium.otf'}[w],s)
RED=(215,25,32); BLK=(17,17,17)
logo=Image.open('public/img/logo-dunkel.png').convert('RGBA')
def wrap(d,t,f,maxw):
    out=[];line=''
    for w in t.split():
        c=(line+' '+w).strip()
        if d.textlength(c,font=f)<=maxw: line=c
        else: out.append(line); line=w
    out.append(line); return out
def make(img,W,H,kicker,head,sub,foot,out,ratio=0.58):
    im=ImageOps.fit(Image.open('public/img/'+img).convert('RGB'),(W,H))
    ov=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(ov)
    top=int(H*ratio)
    for y in range(top-260,H):
        a=min(235,max(0,int((y-(top-260))/260*235)))
        d.line([(0,y),(W,y)],fill=(17,17,17,a))
    im=Image.alpha_composite(im.convert('RGBA'),ov); d=ImageDraw.Draw(im)
    pad=70; y=top
    fk=font('b',34); d.rectangle([pad,y,pad+8,y+40],fill=RED); d.text((pad+24,y-2),kicker.upper(),font=fk,fill=(255,255,255)); y+=72
    fh=font('x',84 if W<1080 or H<1500 else 92)
    for l in wrap(d,head,fh,W-2*pad): d.text((pad,y),l,font=fh,fill=(255,255,255)); y+=fh.size+12
    y+=18; fs=font('m',40)
    for l in wrap(d,sub,fs,W-2*pad): d.text((pad,y),l,font=fs,fill=(225,225,225)); y+=54
    d.rectangle([0,H-14,W,H],fill=RED)
    tg=Image.new('RGBA',(W,H),(0,0,0,0)); td=ImageDraw.Draw(tg)
    for y in range(0,320): td.line([(0,y),(W,y)],fill=(0,0,0,int(150*(1-y/320))))
    im=Image.alpha_composite(im,tg); d=ImageDraw.Draw(im)
    lg=Image.open('public/img/signatur-logo-dunkel.png').convert('RGBA'); s=500/lg.width; lg=lg.resize((500,int(lg.height*s)),Image.LANCZOS)
    sh=Image.new('RGBA',lg.size,(0,0,0,0)); sh.putalpha(lg.split()[3].point(lambda a:int(a*0.6))); sh=sh.filter(ImageFilter.GaussianBlur(8))
    x=(W-lg.width)//2; y0=55
    im.alpha_composite(sh,(x+3,y0+5)); im.alpha_composite(lg,(x,y0))
    ff=font('b',34); d.text((pad,H-90),foot,font=ff,fill=(255,255,255))
    im.convert('RGB').save(out,quality=90)
