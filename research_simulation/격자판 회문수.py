# -*- coding: utf-8 -*-
import sys
#sys.stdin = open("input.txt", 'r')
a=[list(map(int, input().split())) for _ in range(7)]
cnt=0
# zip(*iterable): 동일한 개수로 이루어진 자료형을 묶어줌
# 이를통해 전치 행렬 b 만들기 가능
b=[list(x) for x in zip(*a)]

for i in range(7):
    for j in range(3):
        if a[i][j:j+5] == a[i][j:j+5][::-1] or b[i][j:j+5] == b[i][j:j+5][::-1]:
          cnt+=1

print(cnt)
