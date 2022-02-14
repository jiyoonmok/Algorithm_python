
# -*- coding: utf-8 -*-
import sys
#sys.stdin=open("input.txt", "rt")

# 6 3 이런식으로 입력할거기 때문에 map함수 사용, 띄어쓰기 있으니까 split()사용
n, k = map(int, input().split())
cnt=0 # 약수 갯수
for i in range(1, n+1):
    if n%i==0:
        cnt+=1
    if cnt==k:
        print(i)
        break
else: # for가 정상적으로 끝났을 때 (약수가 없을 때)
    print(-1)