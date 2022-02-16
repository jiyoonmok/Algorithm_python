# -*- coding: utf-8 -*-
import sys
#sys.stdin=open("input.txt","rt")

n, m= map(int, input().split())
cnt=[0]*(n+m+1)

for i in range(1,n+1):
    for j in range(1,m+1):
        cnt[i+j]+=1  ## 값과 같은 인덱스의 값에 1씩 빈도수 추가

for idx, x in enumerate(cnt): #idx는 주사위 눈의 합, x는 합의 빈도수
     if x==max(cnt):
         print(idx,end=' ')