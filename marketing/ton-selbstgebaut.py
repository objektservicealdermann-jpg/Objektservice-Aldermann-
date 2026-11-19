from ton_lib import *
S=[0,3.2,7.6,10.4,13.0,17.6]
for s in S[1:]: whoosh(s-0.25,0.5,0.06)
for i in range(4): scrape(0.8+i*0.18,0.12,0.12)
slide(S[1]+1.6,500,180,1.6,0.10); boing(S[1]+0.6,0.15); note(392,S[1]+2.4,0.4,0.08,'pluck'); note(370,S[1]+2.8,0.6,0.08,'pluck')
ding(S[2]+0.3); ding(S[2]+0.8,1567.98)
for i in range(3): ding(S[3]+1.2+i*0.1,1318.5*(1.122**i),0.09)
note(523,S[4]+0.5,0.3,0.06,'pluck'); note(659,S[4]+0.8,0.3,0.06,'pluck'); note(784,S[4]+1.1,0.5,0.06,'pluck')
boing(S[4]+2.6,0.18)
ding(S[5]+0.4,1046.5,0.14)
finish(sys.argv[1])
