# -*- coding: utf-8 -*-
import sys
sys.stdin = open("input.txt", 'r')

n=int(input())
body=[]
for i in range(n):
    a,b=map(int,input().split())
    body.append((a,b))

#키를 기준으로 내림차순 정렬
body.sort(reverse=True)
largest=0
cnt=0

# 몸무게를 비교 (키는 앞에 사람보다 작거나 같은거 확정이니까 몸무게라도 커야함)
for x,y in body:
    if y>largest:
        largest=y
        cnt+=1
print(cnt)