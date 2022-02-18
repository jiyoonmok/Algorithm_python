# -*- coding: utf-8 -*-
import sys
#sys.stdin=open("input.txt", "r")
card=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
N=10

for n in range(N):
    a,b=map(int,input().split())
    if a==1:
        card[0:b] = card[b-1::-1]
    else:
        card[a-1:b] = card[b-1:a-2:-1]

for i in card:
    print(i, end=" ")