
# -*- coding: utf-8 -*-
import sys
#sys.stdin=open("input.txt", "rt")

# 6 3 �̷������� �Է��Ұű� ������ map�Լ� ���, ���� �����ϱ� split()���
n, k = map(int, input().split())
cnt=0 # ��� ����
for i in range(1, n+1):
    if n%i==0:
        cnt+=1
    if cnt==k:
        print(i)
        break
else: # for�� ���������� ������ �� (����� ���� ��)
    print(-1)