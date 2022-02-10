a=1
A=2
A1=3

print(a, A, A1)

# 동시에 3개의 변수 만들기
a, b, c = 3, 2, 1
print(a, b, c)

# 값 교환
a, b = 10, 20
print(a, b)
a, b = b, a
print(a, b)

# 변수 타입
a = 12345
print(type(a)) # 정수형

a = 12.123456789
print(type(a)) # 실수형

# 출력 방식
print("number")
a, b, c = 1, 2, 3
print(a, b, c)
print("number : ", a, b, c)
print(a, b, c, sep=',') # 변수 사이에 ,넣어서 출력
print(a, b, c, sep=' ')
print(a, b, c, sep='\n')
print(a, end=' ') # 줄바꿈 없이 출력
print(b, end=' ')
print(c)
