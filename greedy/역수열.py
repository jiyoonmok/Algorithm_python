# -*- coding: utf-8 -*-#
import sys
#sys.stdin = open("input.txt", 'r')

n=int(input())
a=list(map(int,input().split()))
l=[0]*n 
cnt=0

for i in range(n):
    cnt=0
    for j in range(n):
        if l[j]==0:
            cnt+=1
         
        if cnt==a[i]+1:
            l[j]=i+1
            break
            
for t in range(n):
    print(l[t],end=' ')