# -*- coding: utf-8 -*-
import sys
#sys.stdin = open("input.txt", 'r')

n=int(input())
a=[list(map(int,input().split())) for _ in range(n)]

#회의 종료시간이 빠른 순서로 정렬. 같다면 시작시간이 빠른 순서
a.sort(key=lambda x:(x[1],x[0]))

# 종료시간 초기화
end=0
# 배정된 회의 수 초기화
cnt=0

for i in range(n):
    if a[i][0]>=end:
        end=a[i][1]
        cnt+=1
        
print(cnt)