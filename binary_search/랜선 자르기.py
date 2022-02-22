# -*- coding: utf-8 -*-
import sys
#sys.stdin = open("input.txt", 'r')
k,n=map(int,input().split())
a=[]

for i in range(k):
    a.append(int(input()))

lt=0
rt=max(a)

while lt<=rt:
    mid=(lt+rt)//2
    x=0
    for i in range(k):
        x+=a[i]//mid
    if x<n:
        rt=mid-1
    else:
        res=mid
        lt=mid+1

print(res)