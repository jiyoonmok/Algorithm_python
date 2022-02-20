# -*- coding: utf-8 -*-
import sys
#sys.stdin = open("input.txt", 'r')
def check(a):
    for i in range(9):
        ch1=[0]*10  # 행을 체크하는 리스트
        ch2=[0]*10  # 열을 체크하는 리스트
        for j in range(9):
            ch1[a[i][j]]=1 #행 탐색
            ch2[a[j][i]]=1 #열 탐색
        if sum(ch1)!=9 or sum(ch2)!=9:
            return False #합이 9가 아니면 false

    for i in range(3):
        for j in range(3): # 9개의 정사각형 탐색
            ch3=[0]*10 # 정사각형 체크하는 리스트
            for k in range(3):
                for s in range(3): # 9개의 숫자 탐색
                    ch3[a[i*3+k][j*3+s]]=1 
            if sum(ch3)!=9:
                return False #return하면 함수 종료됨
    return True

a = [list(map(int,input().split())) for _ in range(9)]

if check(a): #True이면
    print("YES")
else: #False이면
    print("NO")

