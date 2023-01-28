n = int(input())
arr = list(map(int,input().split()))

l,r = 0,n-1
lm, rm = 0,n-1
answer = abs(arr[l] + arr[r])
while l<r:
    if abs(arr[l]) > abs(arr[r]):
        l+=1
    else:
        r-=1
    if l<r and  answer > abs(arr[l] + arr[r]):
        lm = l
        rm = r
        answer = abs(arr[l] + arr[r])
print(arr[lm],arr[rm])