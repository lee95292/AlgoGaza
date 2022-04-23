n = int(input())
v = int(input())

maxV= 100000 * 100
dp = [[maxV]*n for _ in range(n)]

for i in range(v):
    x,y,w = list(map(int,input().split()))
    dp[x-1][y-1] = min(w, dp[x-1][y-1])

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i ==j :
                continue
            dp[i][j] = min(dp[i][j], dp[i][k] +dp[k][j])
for i in range(n):
    for j in range(n):
        if dp[i][j] == maxV:
            dp[i][j] = 0
    print(*dp[i], end=' ')
    print()
"""
5
14
1 2 2
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
3 5 10
3 1 8
1 4 2
5 1 7
3 4 2
5 2 4
"""
