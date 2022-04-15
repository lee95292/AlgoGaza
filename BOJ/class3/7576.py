"""
7576 토마토
MXN 상자에 있는 토마토가 익는데 걸리는 일수 (인접토마토를 익힘)
BFS로 인접토마토 넣어주기
일수 구하는 IDEA가 특이한데, origin의 값을 1씩 늘려가며 마지막 익은 토마토가 일수를 나타내게끔 한다.
크게 어렵지는 않지만 빠뜨릴 여지가 있는 문제
"""
import sys
from collections import deque

input = sys.stdin.readline

class Solution:
    def __init__(self):
        self.m,self.n = list(map(int,input().split()))
        self.box = []
        self.que = deque([])
        for i in range(self.n):
            line = list(map(int,input().split()))
            self.box.append(line)
            
            
            if 1 in line:
                self.que.extend([[idx,i] for idx,x in enumerate(line) if x == 1])
    def solve(self):
        day =-1

        while self.que:
            x,y = self.que.popleft()
            for p in [[1,0],[0,1],[-1,0],[0,-1]]:
                xp, yp = x+ p[0], y+p[1]
                #out of range or invalid
                if  0 <=  yp <self.n and  0 <= xp < self.m and self.box[yp][xp] == 0:
                    self.que.append([xp,yp])
                    self.box[yp][xp] = self.box[y][x] + 1
        for i in self.box:
            if 0 in i:
                day = 0
                break
            day = max(max(i),day)
        print(day-1)

solution = Solution()
solution.solve()
# print(time.time()-start)