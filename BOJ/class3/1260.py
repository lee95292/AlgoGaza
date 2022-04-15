"""
1260 DFS와 BFS
개념만 잘 적용히먄 되는 문제. 
Class를 이용해 깔끔하게 풀어보았따
"""
import sys
from collections import deque

input = sys.stdin.readline

class Solution:
    def __init__(self):
        self.n, self.m, self.v = list(map(int,input().split()))
        self.vertex = [[] for _ in range(self.n+1)]
        for i in range(self.m):
            s,e = list(map(int,input().split()))
            self.vertex[s].append(e)
            self.vertex[e].append(s)
        
    def DFS(self):
        que = deque()
        visit = [0] * (self.n+1)
        que.append(self.v)
        ans = []
        while que :
            d = que.pop()
            if visit[d] == 1:
                continue
            visit[d] = 1
            que.extend(sorted(self.vertex[d], reverse=True))
            ans.append(d)
        return ans

    def BFS(self):
        que = deque()
        visit = [0] * (self.n+1)
        que.append(self.v)
        ans = []
        while que :
            d = que.popleft()
            if visit[d] == 1:
                continue
            visit[d] = 1
            que.extend(sorted(self.vertex[d]))
            ans.append(d)
        return ans


solution = Solution()
print(*solution.DFS(),'\n',end ='')
print(*solution.BFS(),end ='')