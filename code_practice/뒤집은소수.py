# -*- coding: utf-8 -*-
import sys
#sys.stdin=open("input.txt", "r")

N=int(input())
num=list(map(int, input().split()))

def reverse(x):
    res=0
    while x>0:
        t=x%10
        res=res*10+t #앞이 0일때까지는 res=0이므로 자릿수가 안올라감
        x=x//10
    return res

def isPrime(x):
    if x==1:
        return False
    for i in range(2,x):
        if x%i == 0:
            return False
    return True


for i in range(N):
    if isPrime(reverse(num[i])):
        print(reverse(num[i]),end=' ')
    
        