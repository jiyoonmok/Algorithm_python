# -*- coding: utf-8 -*-
import sys
#sys.stdin = open("input.txt", 'r')
def check(a):
    for i in range(9):
        ch1=[0]*10  # ���� üũ�ϴ� ����Ʈ
        ch2=[0]*10  # ���� üũ�ϴ� ����Ʈ
        for j in range(9):
            ch1[a[i][j]]=1 #�� Ž��
            ch2[a[j][i]]=1 #�� Ž��
        if sum(ch1)!=9 or sum(ch2)!=9:
            return False #���� 9�� �ƴϸ� false

    for i in range(3):
        for j in range(3): # 9���� ���簢�� Ž��
            ch3=[0]*10 # ���簢�� üũ�ϴ� ����Ʈ
            for k in range(3):
                for s in range(3): # 9���� ���� Ž��
                    ch3[a[i*3+k][j*3+s]]=1 
            if sum(ch3)!=9:
                return False #return�ϸ� �Լ� �����
    return True

a = [list(map(int,input().split())) for _ in range(9)]

if check(a): #True�̸�
    print("YES")
else: #False�̸�
    print("NO")

