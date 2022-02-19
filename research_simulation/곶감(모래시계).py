# -*- coding: utf-8 -*-
import sys
#sys.stdin = open("input.txt", 'r')
n=int(input())
a=[list(map(int, input().split())) for _ in range(n)]
m=int(input())

## 회전시키기
for i in range(m):
    h, t, k=map(int,input().split())
    if t==0:
        for _ in range(k): 
            #맨 앞의 값(0열)을 꺼내고 앞으로 땡긴다음(pop) 뒤로 다시 넣음(append)
            a[h-1].append(a[h-1].pop(0))  
    else:
        for _ in range(k):
            #맨 뒤 자리를 꺼내서 맨 앞으로 넣기(insert(0,값) 0번째 자리에 넣는다는 뜻)
            #pop() -> 맨 뒤 자리의 값을 꺼냄
            a[h-1].insert(0, a[h-1].pop())

## 모래시계 모양의 합
s=0
e=n
hap=0
for i in range(n):
    for j in range(s,e):
        hap += a[i][j]
    if i<n//2:
        s+=1
        e-=1
    else:
        s-=1
        e+=1

print(hap)