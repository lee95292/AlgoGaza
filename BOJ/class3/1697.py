# BFS
from collections import deque

a, b = map(int, input().split())

q = deque()

q.append(a)
ans = 0
dp = [0]*100001

while(q):
    i = q.popleft()

    if(i == b):
        ans = dp[i]
        break
    for j in (i-1, i+1, 2*i):
        if((0 <= j < 100001) and dp[j] == 0):
            dp[j] = dp[i]+1
            q.append(j)

print(dp[b])
