# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import sys
sys.stdin=open("input.txt", "r")
n=int(input())
ch=[0]*(n+1)
cnt=0
for i in range(2, n+1):
    if ch[i]==0:
        cnt+=1  # 값이 0인것만 카운팅
        for j in range(i, n+1, i):
            ch[j]=1   # 소수가 아닌 것은 1 넣기
print(cnt)