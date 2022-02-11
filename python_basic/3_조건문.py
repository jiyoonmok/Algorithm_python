x = 7
if x == 7:
    print("lucky")


# 중첩

x = 10
if x>0:
    if x<10:
        print("10보다 작은 자연수")

x = 7
if x>0 and x<10:
    print("10보다 작은 자연수")


x = 7
if 0<x<10:
    print("10보다 작은 자연수")


x = 10
if x>0:
    print("양수")
else:
    print("음수")


# 다중 if문

x = 93
if x>=90:
    print('A')
elif x>=80:
    print('B')
elif x>=70:
    print('C')
elif x>=60:
    print('D')
else:
    print('F')
    
