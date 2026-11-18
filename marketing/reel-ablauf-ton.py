import numpy as np, wave, sys
SR=44100; DUR=26.4; N=int(SR*DUR)
out=np.zeros(N)
def env(n,a=0.01,r=0.3):
    t=np.arange(n)/SR; e=np.minimum(1,t/a)*np.exp(-t/r); return e
def note(f,start,dur,vol,kind='pad'):
    n=int(dur*SR); t=np.arange(n)/SR; s0=int(start*SR)
    if s0>=N: return
    if kind=='pad':
        w=(np.sin(2*np.pi*f*t)+0.3*np.sin(2*np.pi*2*f*t)+0.15*np.sin(2*np.pi*3*f*t))
        e=np.minimum(1,t/0.05)*np.minimum(1,(dur-t)/0.1)
    elif kind=='pluck':
        w=np.sin(2*np.pi*f*t)+0.5*np.sin(2*np.pi*2*f*t); e=env(n,0.005,0.18)
    elif kind=='bass':
        w=np.sin(2*np.pi*f*t)+0.2*np.sin(2*np.pi*2*f*t); e=env(n,0.01,0.35)
    seg=w*e*vol; end=min(N,s0+n); out[s0:end]+=seg[:end-s0]
def kick(st,vol=0.5):
    n=int(0.25*SR); t=np.arange(n)/SR; f=110*np.exp(-t*18)+45
    seg=np.sin(2*np.pi*np.cumsum(f)/SR)*np.exp(-t*12)*vol; s0=int(st*SR); e=min(N,s0+n); out[s0:e]+=seg[:e-s0]
def hat(st,vol=0.08):
    n=int(0.05*SR); seg=np.random.randn(n)*np.exp(-np.arange(n)/SR*90)*vol; s0=int(st*SR); e=min(N,s0+n); out[s0:e]+=seg[:e-s0]
np.random.seed(1)
BPM=112; beat=60/BPM
# Akkorde C - G - Am - F
prog=[(261.63,329.63,392.0),(196.0,246.94,293.66),(220.0,261.63,329.63),(174.61,220.0,261.63)]
basses=[65.41,49.0,55.0,43.65]
melody=[523.25,587.33,659.25,587.33, 493.88,587.33,659.25,783.99, 659.25,587.33,523.25,659.25, 698.46,659.25,587.33,523.25]
t=0.0; bar=0
end_music=DUR-0.8
while t<end_music:
    ch=prog[bar%4]
    for f in ch: note(f,t,4*beat,0.045,'pad')
    for k in range(4):
        bt=t+k*beat
        if bt>=end_music: break
        note(basses[bar%4]*2,bt,beat*0.9,0.16,'bass')
        if bar>0: kick(bt,0.35 if k%2==0 else 0.22)
        hat(bt+beat/2)
        if bar>=1:
            m=melody[(bar*4+k)%16]
            note(m,bt,beat*0.8,0.06,'pluck')
    t+=4*beat; bar+=1
# Schlussakkord
for f in (261.63,329.63,392.0,523.25): note(f,end_music,0.8,0.05,'pad')
# Effekte
def ding(st,f=1318.5,vol=0.18):
    note(f,st,0.6,vol,'pluck'); note(f*1.5,st+0.07,0.6,vol*0.7,'pluck')
def whoosh(st,dur=0.5,vol=0.12):
    n=int(dur*SR); x=np.random.randn(n); t=np.arange(n)/SR
    # einfacher Tiefpass via kumulierter Mittelwert
    k=40; x=np.convolve(x,np.ones(k)/k,mode='same')
    e=np.sin(np.pi*t/dur)**2; s0=int(st*SR); e2=min(N,s0+n); out[s0:e2]+=(x*e*vol*6)[:e2-s0]
def thump(st,vol=0.5):
    kick(st,vol); whoosh(st-0.02,0.12,0.15)
def engine(st,dur,vol=0.06):
    n=int(dur*SR); t=np.arange(n)/SR
    f=55+20*np.minimum(1,t/1.2)
    w=np.sign(np.sin(2*np.pi*np.cumsum(f)/SR))*0.6+np.sin(2*np.pi*2*np.cumsum(f)/SR)*0.4
    k=30; w=np.convolve(w,np.ones(k)/k,mode='same')
    e=np.minimum(1,t/0.3)*np.minimum(1,(dur-t)/0.5); s0=int(st*SR); e2=min(N,s0+n); out[s0:e2]+=(w*e*vol)[:e2-s0]
S=[0,3.4,7.6,12.2,16.2,21.8]
for s in S[1:]: whoosh(s-0.25,0.5,0.06)
ding(S[1]+0.6)            # Nachricht
ding(S[1]+2.0,1567.98)    # Antwort
engine(S[2],1.8)          # Transporter
thump(S[3]+1.6,0.55)      # Festpreis-Stempel
for i in range(4): note(2093+i*200,S[4]+0.9+i*0.3,0.08,0.03,'pluck')  # Schnitt
for i in range(5): ding(S[4]+2.4+i*0.1,1046.5*(1.122**i),0.10)  # Sterne
for i in range(4): note(880,S[4]+3.0+i*0.25,0.25,0.05,'pluck')  # Checkliste
ding(S[5]+0.6,1046.5,0.14)
# Ausblenden + normalisieren
fade=int(0.8*SR); out[-fade:]*=np.linspace(1,0,fade)
out=out/np.max(np.abs(out))*0.85
st=np.stack([out,out],1)
with wave.open(sys.argv[1],'wb') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((st*32767).astype(np.int16).tobytes())
print('ok')
