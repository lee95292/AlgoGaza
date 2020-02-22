n = input()
n = int(n)
arr = list(map(int, input().split()))
f = input()
f = int(f)
term = len(arr)//2

pivot = term
ans = "X"
while term > 0:
    # print(term,pivot)
    term = term//2
    if(arr[pivot] > f):
        pivot = pivot//2
    elif(arr[pivot] < f):
        pivot = pivot+term
    else:
        ans = pivot+1

print(ans)
