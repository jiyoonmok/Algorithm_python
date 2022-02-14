
def plus_one(x):
    return x+1

print(plus_one(1))


## 변수명 = lambda 매개변수 : 함수
plus_two = lambda x : x+2

print(plus_two(1))

# map(함수명, 리스트) 
a = [1, 2, 3]
print(list(map(plus_one, a)))

# lambda 이용하기
print(list(map(labmda x: x+1, a)))
