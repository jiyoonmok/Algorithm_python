# -*- coding: utf-8 -*-
import sys
#sys.stdin = open("input.txt", 'r')
n=int(input())
a=[list(map(int, input().split())) for _ in range(n)]
m=int(input())

## ȸ����Ű��
for i in range(m):
    h, t, k=map(int,input().split())
    if t==0:
        for _ in range(k): 
            #�� ���� ��(0��)�� ������ ������ �������(pop) �ڷ� �ٽ� ����(append)
            a[h-1].append(a[h-1].pop(0))  
    else:
        for _ in range(k):
            #�� �� �ڸ��� ������ �� ������ �ֱ�(insert(0,��) 0��° �ڸ��� �ִ´ٴ� ��)
            #pop() -> �� �� �ڸ��� ���� ����
            a[h-1].insert(0, a[h-1].pop())

## �𷡽ð� ����� ��
s=0
e=n
hap=0
for i in range(n):
    for j in range(s,e):
        hap += a[i][j]
    if i<n//2:
        s+=1
        e-=1
    else:
        s-=1
        e+=1

print(hap)