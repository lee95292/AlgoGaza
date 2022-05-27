n=int(input())
dp = [0]*(n+2)
def rec(n):
    if n== 1:
        return 0
    if n == 2:
        return 1
    m1 = dp[n-1]
    if m1 == 0:
        m1 = rec(n-1)
    m2 = dp[n-2]
    if m2 == 0:
        m2 =rec(n-2)
    dp[n] = m1+m2
    return m1+m2

print(rec(n+1))