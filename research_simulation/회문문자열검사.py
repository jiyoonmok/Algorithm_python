# -*- coding: utf-8 -*-
import sys
#sys.stdin=open("input.txt", "r")
N =int(input())

for n in range(N):
    ch = str(input())
    ch = ch.lower()
    ch_re = ch[::-1]

    if ch==ch_re:
        print("#%d YES" %(n+1))
    else:
        print("#%d NO" %(n+1))