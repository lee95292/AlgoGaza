n = int(input())

arr = list(map(int, input().split()))
ansArr = arr.copy()

lenArr = len(arr)
for i in range(lenArr):
    for j in range(i-1, -1, -1):
        if(arr[i] >= arr[j]):
            ansArr[i] = max(arr[i]+ansArr[j], ansArr[i])

print(ansArr)
print(max(ansArr))
