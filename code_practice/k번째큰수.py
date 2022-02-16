# -*- coding: utf-8 -*- 
import sys
#sys.stdin=open("input.txt","rt")

n, k = map(int, input().split())
a = list(map(int, input().split()))
add = [] # 세 수의 합 모든 리스트

for i in range(n):
    for j in range(i+1,n):
        for l in range(j+1,n):
            s = a[i]+a[j]+a[l]
            add.append(s)

add=list(set(add)) # 중복 제거 -> set으로 변경하면 중복이 제거된다.
add.sort(reverse=True) # 내림차순
print(add[k-1])