
# 0~9까지 숫자
a = range(10)
print(list(a))

# 1부터 10까지 숫자
a = range(1,11)
print(list(a))

# hello를 10번(0~9) 출력
for i in range(10):
    print("i")
    print("hello")

# 감소하는 반복문
# 10부터 1까지 2씩 감소
for i in range(10, 0, -2):
    print(i)


## while문
i=1
while i<=10:
    print(i)
    i = i+1

i = 10
while i>=1:
    print(i)
    i = i-1
    
# break: 반복문 멈춤
i=1
while True:
    print(i)
    if i==10:
        break
    i+=1

# continue : 다음 반복문으로 넘어감감
# 짝수일 때만 출력
for i in range(1,11):
    if i%2==0:
        continue
    print(i)

# for ~ else
# break 당해서 끝까지 돌지 못하면 else 실행 X
for i in range(1,11):
    print(i)
    if i==5:
        break
else:
    print(11)
