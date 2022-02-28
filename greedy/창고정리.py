# -*- coding: utf-8 -*-
import sys
#sys.stdin = open("input.txt", 'r')

n=int(input())
a=list(map(int,input().split()))
m=int(input())

for _ in range(m):
    a[a.index(max(a))]-=1
    a[a.index(min(a))]+=1

print(a[a.index(max(a))]-a[a.index(min(a))])