from ton_lib import *
S=[0,3.2,7.8,12.4,16.0,21.2]
for s in S[1:]: whoosh(s-0.25,0.5,0.06)
slide(S[1]+1.4,300,900,0.45,0.14); boing(S[1]+1.9,0.3); thump(S[1]+1.9,0.4)
engine(S[2],1.2)
for i in range(10): scrape(S[2]+1.4+i*0.26,0.2,0.10)
for i in range(8): note(2400+i*90,S[3]+0.2+i*0.25,0.05,0.025,'pluck')
boing(S[3]+0.4,0.15)
for i in range(5): ding(S[4]+1.0+i*0.1,1046.5*(1.122**i),0.09)
for i in range(3): note(880,S[4]+1.7+i*0.25,0.25,0.05,'pluck')
ding(S[5]+0.6,1046.5,0.14)
finish(sys.argv[1])
