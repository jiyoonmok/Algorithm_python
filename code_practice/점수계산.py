# -*- coding: utf-8 -*-
import sys
#sys.stdin=open("input.txt", "r")

N=int(input())
a=list(map(int, input().split()))

chat_list = [0]*N

for i in range(N):
    if a[i]==0:
        chat_list[i]=0
    elif i==0 and a[i]==1:
        chat_list[i]=1
    elif a[i]==1 and a[i-1]==1:
        chat_list[i]=chat_list[i-1]+1
    elif a[i]==1 and a[i-1]==0:
        chat_list[i]=1

print(sum(chat_list))