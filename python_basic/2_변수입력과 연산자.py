a = input("숫자를 입력하세요 : ")
print(a)


# 띄어쓰기로 분리
a, b = input("숫자를 입력하세요 : ").split()
print(a, b)
print(a+b) # 문자열로 추출됨
print(type(a))
c = a + b
print(type(c))

# 숫자형으로 바꾸려면
a, b = input("숫자를 입력하세요 : ").split()
a = int(a)
b = int(b)
print(a+b)
print(type(a+b))

# 더 간단한 방법
a, b = map(int, input("숫자를 입력하세요 : ").split())
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b) << 몫 연산
print(a%b) << 나머지 연산
print(a**b) << 거듭제곱


# 실수형 + 정수형 = 실수형
a = 4.3
b = 5
c = a+b
print(type(c))
