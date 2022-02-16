# -*- coding: utf-8 -*-
import sys
#sys.stdin=open("input.txt","rt")
N = int(input())
list=[]

for n in range(2,N+1):
    for i in range(2,n):
        if n%i == 0:
            break
    else:
         list.append(n)

print(len(list))