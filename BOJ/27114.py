MAX_VALUE = 10000000
l,r,t,k = map(int,input().split())
dp = [[MAX_VALUE]*(k+1) for _ in range(4)]
dp[0][0] = 0
turn = [r,t,l]
for j in range(k):
    for i in range(4):
        for idx,ts in enumerate(turn):
            if j+ts < k+1:
                dp[(i+idx+1)%4][j+ts] = min(dp[i][j]+1,dp[(i+idx+1)%4][j+ts])
if dp[0][k] == MAX_VALUE: print(-1)
else: print(dp[0][k])