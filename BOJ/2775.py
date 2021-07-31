import sys
sys.stdin = open("input.txt", "r")

arr = [[i for i in range(1,15)] for i in range(15)]
for i, sub in enumerate(arr[1:]):
    for j,sub2 in enumerate(arr[i+1]):
        arr[i+1][j] = sum(arr[i][0:j+1])

T  = int(input())
for i in range(T):
    k = int(input())
    n = int(input())
    print(arr[k][n-1])        