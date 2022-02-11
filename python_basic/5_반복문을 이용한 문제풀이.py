
# 1) 1부터 N까지 홀수 출력하기
n = int(input())
for i in range(1, n+1):
    if i%2==1:
        print(i)

# 2) 1부터 N까지 합 구하기
n = int(input())
sum = 0
for i in range(1, n+1):
    sum=sum+i
print(sum)

# 3) N의 약수 출력하기
n = int(input())
for i in range(1, n+1):
    if n%i==0:
        print(i, end=' ')
