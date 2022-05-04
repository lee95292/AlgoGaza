""""
9251 LCS

DP, LCS 알고리즘..
"""
a = input()
b = input()
dp = [[0]*(len(a)+1) for _ in range((len(b)+1))]

maxv =0
for i in range(len(b)+1):
    for j in range(len(a)+1):
        if i==0 or j==0:
            dp[i][j]=0
        elif b[i-1] == a[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        maxv = max(maxv,dp[i][j])
print(maxv)

"""
ACAYKP
CAPCAK
"""