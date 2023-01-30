n, s= list(map(int, input().split()))
arr = list(map(int, input().split()))

accarr = [0]*n
accarr[0] = arr[0]
for i in range(1, n):
    accarr[i] = arr[i] + accarr[i-1]

l,r = 0,1
answer = n
while r < n:
    while l+1 < r and accarr[r] - accarr[l+1] >= s:
        l+=1

    if accarr[r] - accarr[l] >= s:
        answer = min(answer, r-l)
    r+=1

if accarr[-1] < s:
    print(0)
elif arr[0] >= s:
    print(1)
else:
    print(answer)

"""
10 15
5 1 3 5 10 7 4 9 2 15
"""