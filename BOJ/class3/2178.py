"""
BFS문제이지만, 시간제한이 빡세서 애먹은 문제.
BFS할 때, 방문표시를 "큐에 넣는 순간" 해야된다. 
"큐에서 빼는 순간" 방문표시를 하면, 큐에 들어있는동안 미방문 정점으로 체크됨
"""
import sys
from collections import deque

sys.setrecursionlimit(10**5)
h,w = list(map(int,input().split()))
input = sys.stdin.readline
maze = []
for i in range(h):
    linestr=input().replace('\n','')
    maze.append([int(s) for s in linestr])

mazeDP = [[10000]*w for _ in range(h)]
mazeDP[0][0]=1
    
dx=[1,0,-1,0]
dy=[0,1,0,-1]

que = deque()
que.append([0,0])
maze[0][0]=0
while que:
    x,y = que.popleft()
    for i in range(4):
        xp, yp = x + dx[i], y+dy[i]
        if 0<=xp<w and 0<=yp<h and maze[yp][xp] == 1:
            mazeDP[yp][xp] = min(mazeDP[y][x] + 1, mazeDP[yp][xp])
            que.append([xp,yp])
            maze[yp][xp] = 0 #Queue에 넣을 때 방문표시 할것!!!! 큐에 있는동안 방문표시가 안되어서, 다른 노드들이 방문할 수 있음
print(mazeDP[h-1][w-1])