
# 더하기 함수
def add(a, b):
    c=a+b
    print(c)

add(3, 2)
add(5, 7)


def add(a, b):
    c=a+b
    return c  #반환한 값

print(add(3, 2))

def add(a,b):
    c=a+b
    d=a-b
    return c, d #두개 이상 반환 가능

print(add(3, 2))


# 소수 추출 함수
def isPrime(x):
    for i in range(2, x):
        if x%i==0:
            return False  #소수가 아니면 도중에 False -> 종료
    return True
        
a=[12, 13, 7, 9, 19]
for y in a:
    if isPrime(y):
        print(y, end=' ')
