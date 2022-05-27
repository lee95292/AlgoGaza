"""
9465 스티커
2*N 형태의 스티커들에서 이웃한 스티커 선택하지 않고 가장 높은 가치의 스티커들을 선택하는 문제
DP, 예외케이스 1: (위 / X / 아래) 선택했을 때가 (위/아래/위)보다 가치가 더 높은 경우 고려
"""
T = int(input())

for i in range(T):
    arr = []
    n = int(input())
    arr.append(list(map(int,input().split())))
    arr.append(list(map(int,input().split())))
    for i in range(1,n):
        if i == 1:
            arr[0][i] += arr[1][i-1] 
            arr[1][i] += arr[0][i-1] 
        else:
            arr[0][i] += max(arr[1][i-1], arr[1][i-2])
            arr[1][i] += max(arr[0][i-1], arr[0][i-2])
    #print(arr)
    if n == 1:
        print(max(arr[0][0],arr[1][0]))
    else:
        print(max(arr[0][n-1], arr[1][n-1],arr[0][n-2], arr[1][n-2] ))