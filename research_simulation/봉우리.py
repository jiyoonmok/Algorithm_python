# -*- coding: utf-8 -*-
import sys
#sys.stdin = open("input.txt", 'r')
n=int(input())
a=[list(map(int, input().split())) for _ in range(n)]
cnt=0

## �׵θ��� 0 �߰��ϱ�
for i in range(n):
    a[i].insert(0,0)
    a[i].append(0)
a.insert(0,[0]*(n+2))
a.append([0]*(n+2))

## ���츮 ���� ����
for p in range(1,n+1):
    for q in range(1,n+1):
        if a[p][q]>a[p-1][q] and a[p][q]>a[p][q-1] and a[p][q]>a[p][q+1] and a[p][q]>a[p+1][q]:
            cnt+=1

print(cnt)