import random as r

# 빈 리스트 만들기
a=[]
print(a)
b=list()
print(b)

# 리스트 초기화
a=[1, 2, 3, 4, 5]
print(a)
print(a[0])

b=list(range(1, 11))
print(b)

# 리스트 병합
c=a+b
print(c)

print(a)
# 값 추가
a.append(6)
print(a)

# 특정 인덱스에 값 삽입
a.insert(3, 7) # 3번 인덱스에 7을 삽입
print(a)

# 맨 마지막 값 지우기
a.pop()
print(a)

# 3번째 인덱스 값 지우기
a.pop(3)
print(a)

# 값에 따라 지우기 -> 숫자4 지우기
a.remove(4)
print(a)

# 값에 따른 인덱스 번호 추출 
print(a.index(5))

# sum, max, min
a=list(range(1, 11))
print(a)
print(sum(a))
print(max(a))
print(min(a))
print(min(7,5)) #7과 5 중의 최솟값

# list값 자리 섞기
r.shuffle(a)
print(a)

# 오름차순으로 정렬
a.sort()
print(a)
# 내림차순으로 정렬
a.sort(reverse=True)
print(a)

# 리스트에 있는 값 다 없애기
a.clear()
print(a)
