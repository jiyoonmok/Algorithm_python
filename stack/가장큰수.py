# -*- coding: utf-8 -*-#
import sys
sys.stdin = open("input.txt", 'r')

num,m=map(int,input().split())
num=list(map(int,str(num))) #문자로 바꾼후 다시 숫자로
stack=[]

for x in num:
    while stack and m>0 and stack[-1]<x: 
        #m이 0보다 클동안 stack이 비어있지않고 마지막에 들어간 숫자가 x보다 작을때 pop
        stack.pop()
        m-=1 #제거할 수 있는 개수 줄이기
    stack.append(x) #x를 계속 stack에 넣기

if m!=0: #개수를 다 쓰지 못했다.
    stack=stack[:-m] #뒤에서부터 m개를 제거한다.

res=''.join(map(str,stack))
print(res)