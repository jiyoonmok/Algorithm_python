# -*- coding: utf-8 -*-
import sys
#sys.stdin = open("input.txt", 'r')
n,m=map(int,input().split())
a=list(map(int,input().split()))

lt=max(a)
rt=sum(a)

while lt<=rt:
    mid=(lt+rt)//2
    cnt=1
    x=0
    for i in range(n):
        x+=a[i]
        if x>mid:
            cnt+=1
            x=a[i]
            continue
    if cnt<=m:
        res=mid
        rt=mid-1
    else:
        lt=mid+1

print(res)