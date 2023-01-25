n = int(input())
dp = [100]*(n+1)
dp[n]=0
for i in range(n,0,-1):
    dp[i-1] = min(dp[i]+1, dp[i-1])
    if i%2==0:
        dp[i//2] = min(dp[i]+1, dp[i//2])
    if i%3==0:
        dp[i//3] = min(dp[i]+1, dp[i//3])

answer = [1]
for i in range(dp[1]-1, -1,-1):
    if answer[-1] * 3 <=n and dp[answer[-1] * 3] == i:
        answer.append(answer[-1] * 3)
    elif answer[-1] * 2 <= n  and  dp[answer[-1] * 2] == i:
        answer.append(answer[-1] * 2)
    elif answer[-1] +1 <= n and dp[answer[-1] + 1] == i:
        answer.append(answer[-1] + 1)

print(dp[1])
for a in answer[::-1]:
    print(a, end =' ')