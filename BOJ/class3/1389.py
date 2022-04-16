##1389 플로이드 와샬 문제.
import sys
input = sys.stdin.readline

class Solution:
    def __init__(self):
        self.n, self.m = list(map(int,input().split()))
        self.vertex = []
        self.graph = [[100] * self.n for _ in range(self.n)]
        for i in range(self.m):
            x,y = list(map(int,input().split()))
            self.vertex.append([x,y])
            self.graph[x-1][y-1] = 1
            self.graph[y-1][x-1] = 1
    def solve(self):
        dp = [[0]*self.n for _ in range(self.n)]
        for i in range(self.n):
            for j in range(self.n):
                dp[i][j] = self.graph[i][j]
        
        for k in range(self.n):
            for i in range(self.n):
                for j in range(self.n):
                    if dp[i][k] + dp[k][j] < dp[i][j]:
                        dp[i][j]=dp[i][k] + dp[k][j]  
        
        minv = 100
        minidx = 0
        for idx,d in enumerate(dp):
            if sum(d) < minv:
                minv = sum(d)
                minidx = idx
        print(minidx +1)

solution = Solution()
solution.solve()