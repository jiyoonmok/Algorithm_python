# -*- coding: utf-8 -*-
import sys
#sys.stdin = open("input.txt", 'r')

n=int(input())
a=[list(map(int,input().split())) for _ in range(n)]

#ȸ�� ����ð��� ���� ������ ����. ���ٸ� ���۽ð��� ���� ����
a.sort(key=lambda x:(x[1],x[0]))

# ����ð� �ʱ�ȭ
end=0
# ������ ȸ�� �� �ʱ�ȭ
cnt=0

for i in range(n):
    if a[i][0]>=end:
        end=a[i][1]
        cnt+=1
        
print(cnt)