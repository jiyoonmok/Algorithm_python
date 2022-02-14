# 0~9 1차원 리스트 생성
a=[0]*10
print(a)

# 3*3 2차원 리스트 생성
a=[[0]*3 for _ in range(3)]
print(a)
a[0][1]=1 #0행1열
print(a)
a[1][1]=2 #1행1열
print(a)

for x in a:
    print(x) #행을 각각 출력

for x in a:
    for y in x:
        print(y, end=' ')
    print()

