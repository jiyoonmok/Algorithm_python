# -*- coding: utf-8 -*-
import sys
#sys.stdin=open("input.txt", "r")

N=int(input())
price_list=[]
for n in range(N):
    a,b,c=list(map(int, input().split()))
    if a==b==c:
        price = 10000+a*1000
    elif a==b | a==c:
        price = 1000+a*100
    elif b==c:
        price = 1000+b*100
    else:
        m = max(a,b,c)
        price = m*100
    price_list.append(price)

print(max(price_list))