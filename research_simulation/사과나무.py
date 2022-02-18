# -*- coding: utf-8 -*-
import sys
#sys.stdin=open("input.txt", "r")

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
hap=0
k=n//2

for i in range(k+1):
    for j in range(k-i,k+i+1):
        hap+=a[i][j]

for i in range(k+1,n):
    for j in range(i-k,k+n-i):
        hap+=a[i][j]

print(hap)