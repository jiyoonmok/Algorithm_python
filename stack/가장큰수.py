# -*- coding: utf-8 -*-#
import sys
sys.stdin = open("input.txt", 'r')

num,m=map(int,input().split())
num=list(map(int,str(num))) #���ڷ� �ٲ��� �ٽ� ���ڷ�
stack=[]

for x in num:
    while stack and m>0 and stack[-1]<x: 
        #m�� 0���� Ŭ���� stack�� ��������ʰ� �������� �� ���ڰ� x���� ������ pop
        stack.pop()
        m-=1 #������ �� �ִ� ���� ���̱�
    stack.append(x) #x�� ��� stack�� �ֱ�

if m!=0: #������ �� ���� ���ߴ�.
    stack=stack[:-m] #�ڿ������� m���� �����Ѵ�.

res=''.join(map(str,stack))
print(res)