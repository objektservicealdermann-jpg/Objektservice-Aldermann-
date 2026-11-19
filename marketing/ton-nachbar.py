from ton_lib import *
S=[0,3.0,5.6,8.2,11.0,15.4]
for s in S[1:]: whoosh(s-0.25,0.5,0.06)
for s in S[1:4]:
    slide(s+0.7,300,1000,0.4,0.14); boing(s+0.9,0.25); thump(s+1.0,0.35)
ding(S[4]+0.5,1046.5,0.08); note(330,S[4]+0.3,0.5,0.06,'pluck')
ding(S[4]+2.5,1318.5,0.12)
ding(S[5]+0.4,1046.5,0.14)
finish(sys.argv[1])
