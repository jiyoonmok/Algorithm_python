a=[23, 12, 36, 53, 19]
print(a[:3]) #0~2번째 추출
print(a[1:4]) #1~3번째 추출
print(len(a)) #리스트의 길이

for i in range(len(a)):
    print(a[i], end=' ')
print()

for x in a:
    if x%2==1:
        print(x, end=' ')
print()

# 인덱스와 값을 동시에 추출 (튜플 형식으로)
for x in enumerate(a):
    print(x)

## 튜플 만들기
b = (1, 2, 3, 4, 5)
print(b[0])

# 튜플 값은 변경할 수 없다.
# b[0]=4 불가능


## 인덱스와 값 동시에 추출 (튜플 값을 직접 꺼내기)
for x in enumerate(a):
    print(x[0], x[1]) 
print()

for index, value in enumerate(a):
    print(index, value)
print()

# 리스트 값들이 모두 60이하이면 참
if all(60>x for x in a):
    print("Yes")
else:
    print("No")

# 하나만 참이어도 참    
if any(15>x for x in a):
    print("Yes")
else:
    print("No")
    
