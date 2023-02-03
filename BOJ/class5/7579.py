"""
백준 7579
5 60
30 10 20 35 40
3 0 3 5 4

5 12
5 4 3 2 1
100 43 3 2 1

5 10
5 4 3 2 1
0 43 3 2 1

5 0
1 2 3 0 5
1 100 100 100 10

100 100
2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 

3 100
100 10 10
0 1 3

3 3
3 2 1 
10 5 4

3 10000000
2000000 4000000 4000000
50 100 100
"""

N,M = map(int,input().split())
mem = [0] + list(map(int,input().split()))
cost = [0] +list(map(int,input().split()))
MAX_C = sum(cost)+1
dp = [[0] * MAX_C for _ in range(N+1)]
for i in range(N):
    dp[i][cost[i]] = mem[i]
answer = 10**9*3
for i in range(1,N+1):
    for c in range(0,MAX_C):
        if cost[i] <= c:
            dp[i][c] = max(dp[i-1][c], dp[i-1][c-cost[i]] +mem[i])
        else:
            dp[i][c] = dp[i-1][c]
        if dp[i][c] >= M:
            answer = min(answer, c)
print(answer)