# -*- coding: utf-8 -*-#
import sys
from collections import deque 
#sys.stdin = open("input.txt", 'r')

n,limit=map(int,input().split())
p=list(map(int,input().split()))
p.sort()
p=deque(p)
cnt=0

while p: #��������� ����->����
    if len(p)==1: #�Ѹ� ����������
        cnt+=1
        break 
    if p[0]+p[-1]>limit:  #���� ������ + ���� ���ſ� > limit
        p.pop() #���� ���ſ� ����� Ž
        cnt+=1 #����Ʈ �ϳ� +
    else:
        p.popleft() #���� ź���̹Ƿ� ���� �������� pop
        p.pop() #���� ���ſ��� pop
        cnt+=1

print(cnt)