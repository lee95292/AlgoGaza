import sys
sys.stdin = open("input.txt","r")

import math

T = int(input())
max = 10001
arr = [1] * max
arr[0], arr[1] = 0,0
for i in range(1, int(math.sqrt(max)) +1):
    if arr[i] == 0:
        continue
    for j in range(i * i, max):
        if j%i == 0:
            arr[j] = 0


for k in range(T):
    n = int(input())
    print('n',n)
    a,b = 0,0
    for i,val in enumerate(arr[0:int(n/2)+1]):
        if i > 1 and arr[n-i] ==1 and arr[i]==1:
            a,b = i, n-i
    print(a,b)
