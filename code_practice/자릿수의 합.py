# -*- coding: utf-8 -*-

def digit_sum(N,k):
    p=[]
    for n in range(N):
        l = [int(i) for i in str(k[n])]
        p.append(sum(l))
    idx = p.index(max(p))
    return k[idx]

import sys
#sys.stdin=open("input.txt","rt")
N = int(input())
k = list(map(int, input().split()))

print(digit_sum(N,k))
    