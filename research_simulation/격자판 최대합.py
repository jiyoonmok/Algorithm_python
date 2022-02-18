# -*- coding: utf-8 -*-
import sys
sys.stdin=open("input.txt", "r")

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
maxi=[]
daegak1=0
daegak2=0

##°¡·Î
for i in range(n):
    row=0
    column=0
    for j in range(n):
        row += a[i][j]
        maxi.append(row)
        column += a[j][i]
        maxi.append(column)
    daegak1 += a[i][i]
    daegak2 += a[i][n-i-1]
maxi.append(daegak1)
maxi.append(daegak2) 

print(max(maxi))
