def solution(N):
    answer = 0
    a = []
    a.append(1)
    a.append(1)
    for i in range(2, N+1):
        a.append(a[i-1]+a[i-2])
    return 2*(a[N]+a[N-1])
