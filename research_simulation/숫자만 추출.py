# -*- coding: utf-8 -*-
import sys
#sys.stdin=open("input.txt", "r")
ch=input()

res=0
for x in ch:
    if x.isdecimal(): #숫자일 때
        res=res*10+int(x) #정수로 변경
print(res)

cnt=0
for i in range(1,res+1):
    if res%i==0:
        cnt+=1
print(cnt)