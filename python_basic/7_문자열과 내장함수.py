msg = "It is Time"
print(msg.upper()) #대문자로 변형
print(msg.lower()) #소문자로 변형
tmp=msg.upper()
print(tmp)
print(tmp.find('T')) #위치(인덱스) 반환
print(tmp.count('T')) #T가 몇개 있는가
print(msg[:2]) #0~1번째 글자 반환
print(msg[3:5]) #3~4번째 글자 반환
print(len(msg)) #총 길이 반환 (공백포함)

for i in range(len(msg)):
    print(msg[i], end=' ')
print()

for x in msg:
    print(x, end=' ')
print()

for x in msg:
    if x.isupper(): #x가 대문자이면
        print(x, end='')
print()


for x in msg:
    if x.islower(): #x가 소문자이면
        print(x, end='')
print()

for x in msg:
    if x.isalpha(): #x가 알파벳이면 (공백이 아닐때만)
        print(x, end='')
print()

tmp = 'AZ'
for x in tmp:
    print(ord(x)) #ascii number 출력 (A:65 ~ Z:90)

tmp = 'az'
for x in tmp:
    print(ord(x)) #ascii number 출력 (a:97 ~ z:122)

tmp = 65
print(chr(tmp)) #ascii number에 대응되는 문자
