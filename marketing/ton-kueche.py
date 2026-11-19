from ton_lib import *
S=[0,3.4,7.8,12.8,18.4]
for s in S[1:]: whoosh(s-0.25,0.5,0.06)
for i in range(12): thump(0.1+i*0.13,0.18)
boing(S[0]+2.0,0.2)
for i in range(6): note(1800+i*150,S[1]+0.2+i*0.6,0.06,0.04,'pluck')
slide(S[1]+2.3,600,250,0.5,0.12)
for i in range(22): scrape(S[2]+1.2+i*0.15,0.07,0.09)
for i in range(6): ding(S[2]+1.3+i*0.5,1318.5+i*80,0.06)
for i in range(5): ding(S[3]+1.8+i*0.1,1046.5*(1.122**i),0.10)
for i in range(3): note(880,S[3]+3.1+i*0.25,0.25,0.05,'pluck')
ding(S[4]+0.6,1046.5,0.14)
finish(sys.argv[1])
