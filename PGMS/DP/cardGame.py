def solution(left, right):
    L = len(left)
    R = len(right)
    dp = [[] for x in range(0, len(left))]
    for i in range(0, len(left)):
        dp[i].extend([-1 for x in range(0, len(right))])

    def recurs(a, b):
        if(a == L or b == R):
            return 0

        # visited
        if(dp[a][b] != -1):
            return dp[a][b]

        dp[a][b] = max(recurs(a+1, b), recurs(a+1, b+1))

        if(left[a] > right[b]):
            dp[a][b] = max(dp[a][b], recurs(a, b+1)+right[b])

        return dp[a][b]

    return recurs(0, 0)


solution([3, 2, 5], [2, 4, 1])
