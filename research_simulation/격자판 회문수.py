# -*- coding: utf-8 -*-
import sys
#sys.stdin = open("input.txt", 'r')
a=[list(map(int, input().split())) for _ in range(7)]
cnt=0
# zip(*iterable): ������ ������ �̷���� �ڷ����� ������
# �̸����� ��ġ ��� b ����� ����
b=[list(x) for x in zip(*a)]

for i in range(7):
    for j in range(3):
        if a[i][j:j+5] == a[i][j:j+5][::-1] or b[i][j:j+5] == b[i][j:j+5][::-1]:
          cnt+=1

print(cnt)
