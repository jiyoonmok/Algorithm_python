arr=[5,3,7,9,2,5,2,6]
arrMin=arr[0] #ù��° ������ �ʱ�ȭ

for i in range(1, len(arr)):
    if arr[i] < arrMin:
        arrMin=arr[i]