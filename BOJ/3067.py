"""
BOJ 3067 Coins, DP
DP[I][J]: I원을 J개 동전을 사용해 만들 수 있는 경우의 수

1
2
1 3
10
"""
import sys
input = sys.stdin.readline

T = int(input())
answer = []
for t in range(T):
    N = int(input())
    money = list(map(int,input().split()))
    X = int(input())
    maxv = max(money)
    dp = [0]*(X+1)
    dp[0] = 1

    for i in range(N):
        for j in range(money[i], X+1):
            dp[j] += dp[j-money[i]]
    print(dp[X])