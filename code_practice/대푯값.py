# -*- coding: utf-8 -*-
import sys
#sys.stdin=open("input.txt","rt")

n = int(input())
a = list(map(int, input().split()))
## round�� round_half_even ����̴�
# round_half_even : .5�϶� ¦���� ������ ���� (4.5->4)
avg = int((sum(a)/n)+0.5) # 0.5�� ���� �� �Ҽ����� ����
min = 2147000000


for idx, x in enumerate(a): # idx���� �ε���, x���� ���� ����
    tmp=abs(x-avg)
    if tmp<min:
       min=tmp
       score=x #��������
       res=idx+1 #�л���ȣ
    elif tmp==min: #�������� ���� ��
        if x>score: # ������ ���� ��쿡�� �ٲ��� x -> �л���ȣ�� ���� ���������� ������
            score=x 
            res=idx+1
       
print(avg, res)
