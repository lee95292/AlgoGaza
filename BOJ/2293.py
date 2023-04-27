n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))

dp = [0] * (k+1)
dp[0] = 1


    
for coin in coins:
    for i in range(coin, k+1):
        pc = dp[i - coin]
        dp[i] += pc
print(dp[k+1])