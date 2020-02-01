def solution(money):
    dp0 = [0 for x in money]
    dp1 = [0 for x in money]

    def step(dp, x):
        if(x < 0):
            return 0
        dp[x] = max(



    dp[x]=dp[x-2], dp[x-3]
    answer=0
    return answer
