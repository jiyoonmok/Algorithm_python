# -*- coding: utf-8 -*- 
import sys
#sys.stdin=open("input.txt","rt")

n, k = map(int, input().split())
a = list(map(int, input().split()))
add = [] # �� ���� �� ��� ����Ʈ

for i in range(n):
    for j in range(i+1,n):
        for l in range(j+1,n):
            s = a[i]+a[j]+a[l]
            add.append(s)

add=list(set(add)) # �ߺ� ���� -> set���� �����ϸ� �ߺ��� ���ŵȴ�.
add.sort(reverse=True) # ��������
print(add[k-1])