# -*- coding: utf-8 -*-
import sys
#sys.stdin=open("input.txt","rt")

n, m= map(int, input().split())
cnt=[0]*(n+m+1)

for i in range(1,n+1):
    for j in range(1,m+1):
        cnt[i+j]+=1  ## ���� ���� �ε����� ���� 1�� �󵵼� �߰�

for idx, x in enumerate(cnt): #idx�� �ֻ��� ���� ��, x�� ���� �󵵼�
     if x==max(cnt):
         print(idx,end=' ')