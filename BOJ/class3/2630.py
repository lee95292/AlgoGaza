"""
2630 색종이 자르기
특별할것 없는 분할정복/재귀 문제
"""

import sys
input = sys.stdin.readline

class Solution:
    def __init__(self):
        self.n = int(input())
        self.cnt = [0,0]
        self.paper = []
        for i in range(self.n):
            self.paper.append(list(map(int,input().split())))
    def solve(self,x,y, n):
        if n == 1:
            self.cnt[self.paper[y][x]] += 1
            return
        flag = True
        cta = self.paper[y][x]
        for p in self.paper[y:y+n]:
            if cta^1 in p[x:x+n]:
                flag = False
                break
        if flag:
            self.cnt[cta] += 1
            return
        else:
            self.solve(x, y, n//2)
            self.solve(x+n//2, y, n//2)
            self.solve(x, y+n//2, n//2)
            self.solve(x+n//2, y+n//2, n//2)
    def printAnswer(self):
        self.solve(0, 0,self.n)
        print(self.cnt[0])
        print(self.cnt[1])
solution = Solution()
solution.printAnswer()
