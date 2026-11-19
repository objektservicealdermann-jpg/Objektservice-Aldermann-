from ton_lib import *
S=[0,3.0,7.8,11.4,16.0,21.2]
for s in S[1:]: whoosh(s-0.25,0.5,0.06)
for i in range(5): boing(S[1]+0.3+i*0.63,0.18)
thump(S[1]+3.3,0.6); slide(S[1]+3.0,700,200,0.4,0.12)
ding(S[2]+0.5); ding(S[2]+1.8,1567.98)
for i in range(12): scrape(S[3]+1.6+i*0.13,0.08,0.10)
for i in range(4): ding(S[3]+2.0+i*0.3,1318.5+i*120,0.07)
kick(S[4]+0.8,0.35); note(3000,S[4]+0.8,0.05,0.08,'pluck')
for i in range(5): ding(S[4]+1.0+i*0.1,1046.5*(1.122**i),0.09)
for i in range(3): note(880,S[4]+1.8+i*0.25,0.25,0.05,'pluck')
ding(S[5]+0.6,1046.5,0.14)
finish(sys.argv[1])
