n = int(input())
dp = [100]*(n+1)
dp[n]=0
for i in range(n,0,-1):
    dp[i-1] = min(dp[i]+1, dp[i-1])
    if i%2==0:
        dp[i//2] = min(dp[i]+1, dp[i//2])
    if i%3==0:
        dp[i//3] = min(dp[i]+1, dp[i//3])

print(dp[1])
print(dp)
while n>0:
    print(n)
    if dp[n-1] == dp[n] +1:
        n=n-1
    elif n%2==0 and dp[n]+1 == dp[n//2]:
        n=n//2
    elif n%3==0 and dp[n]+1 == dp[n//3]:
        n=n//3

    
