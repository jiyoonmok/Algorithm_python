# -*- coding: utf-8 -*-
import sys
#sys.stdin = open("input.txt", 'r')

def Count(len):
    cnt=1
    ep=a[0]
    for i in range(1,n):
        if a[i]-ep >=len:
            cnt+=1
            ep=a[i]
    return cnt

n,c=map(int,input().split())
a=[]
for _ in range(n):
    a.append(int(input()))
a.sort()

lt=1
rt=a[n-1]

while lt<=rt:
    mid=(lt+rt)//2
    if Count(mid)>=c:
        res=mid
        lt=mid+1
    else:
        rt=mid-1 

print(res)