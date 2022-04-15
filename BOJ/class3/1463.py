n = int(input())

arr = [10**6] * (n+1)
arr[n] = 0

for i in range(n,0, -1):
    if i % 3 == 0:
        arr[i//3] = min (arr[i] + 1, arr[i//3])
    if i % 2 == 0:
        arr[i//2] = min (arr[i] + 1, arr[i//2])
    if i > 1 :
        arr[i-1]= min(arr[i] +1 , arr[i-1])  

#print(arr)
print(arr[1])