import sys
input = sys.stdin.readline

n = int(input())

arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))

arr = sorted(arr, key= lambda x:(x[1],x[0]))
en = 0
cnt=0
print(arr)
for ar in arr:
    if ar[0] >= en:
        en = ar[1]
        cnt= cnt+1
print(cnt)