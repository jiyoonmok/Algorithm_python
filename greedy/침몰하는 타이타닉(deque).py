# -*- coding: utf-8 -*-#
import sys
from collections import deque 
#sys.stdin = open("input.txt", 'r')

n,limit=map(int,input().split())
p=list(map(int,input().split()))
p.sort()
p=deque(p)
cnt=0

while p: #비어있으면 거짓->멈춤
    if len(p)==1: #한명만 남았을때는
        cnt+=1
        break 
    if p[0]+p[-1]>limit:  #가장 가벼운 + 가장 무거운 > limit
        p.pop() #가장 무거운 사람만 탐
        cnt+=1 #구명보트 하나 +
    else:
        p.popleft() #같이 탄것이므로 가장 가벼운사람 pop
        p.pop() #가장 무거운사람 pop
        cnt+=1

print(cnt)