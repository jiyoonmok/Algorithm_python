# -*- coding: utf-8 -*-#
import sys
sys.stdin = open("input.txt", 'r')

n=int(input())
p=list(map(int,input().split()))
cnt=0
a=[] 
end=0

while p: 
    if len(p)==1:
        if end<p[0]:
            p.pop(0)
            cnt+=1
            a.append("L")
            break
        else:
            break

    if p[0]<p[-1]:
        if end<p[0]:
            end=p[0]
            p.pop(0)
            cnt+=1
            a.append("L")
        elif end>p[-1]:
            break
        else:
            end=p[-1]
            p.pop()
            cnt+=1
            a.append("R")
    elif p[0]>p[-1]:
        if end<p[-1]:
            end=p[-1]
            p.pop()
            cnt+=1
            a.append("R")
        elif end>p[0]:
            break
        else: 
            end=p[0]
            p.pop(0)
            cnt+=1
            a.append("L")

print(cnt)
for i in a:
    print(i,end='')