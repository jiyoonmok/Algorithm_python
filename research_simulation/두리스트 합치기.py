# -*- coding: utf-8 -*-
import sys
#sys.stdin=open("input.txt", "r")

n = int(input())
list1 = list(map(int,input().split()))
m = int(input())
list2 = list(map(int,input().split()))

list3 = []
list3 = list1+list2

list3.sort()
for l in list3:
    print(l, end=" ")

