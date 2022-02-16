
# -*- coding: utf-8 -*-
import sys
sys.stdin=open("input.txt","rt")

T=int(input()) # 테스트 케이스의 개수
for t in range(T):
    n,s,e,k = map(int, input().split())
    a = list(map(int, input().split())) # 숫자들을 리스트화
    a = a[s-1:e]
    a.sort()
    print("#%d %d" %(t+1,a[k-1]))
