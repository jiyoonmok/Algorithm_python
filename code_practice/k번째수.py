
# -*- coding: utf-8 -*-
import sys
sys.stdin=open("input.txt","rt")

T=int(input()) # �׽�Ʈ ���̽��� ����
for t in range(T):
    n,s,e,k = map(int, input().split())
    a = list(map(int, input().split())) # ���ڵ��� ����Ʈȭ
    a = a[s-1:e]
    a.sort()
    print("#%d %d" %(t+1,a[k-1]))
