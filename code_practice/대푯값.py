# -*- coding: utf-8 -*-
import sys
#sys.stdin=open("input.txt","rt")

n = int(input())
a = list(map(int, input().split()))
## round는 round_half_even 방식이다
# round_half_even : .5일때 짝수인 쪽으로 선택 (4.5->4)
avg = int((sum(a)/n)+0.5) # 0.5를 더한 후 소수점을 날림
min = 2147000000


for idx, x in enumerate(a): # idx에는 인덱스, x에는 값을 추출
    tmp=abs(x-avg)
    if tmp<min:
       min=tmp
       score=x #실제점수
       res=idx+1 #학생번호
    elif tmp==min: #점수차가 같을 때
        if x>score: # 점수가 같을 경우에는 바꾸지 x -> 학생번호가 가장 적은것으로 저장함
            score=x 
            res=idx+1
       
print(avg, res)
