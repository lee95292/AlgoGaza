"""
23563 벽타기 : 0-1 BFS
이동좌표와 현재좌표가 모두 벽에 붙어있으면 이동시간 없음 -> que에 appendleft로 추가하면 시간절약 가능
"""
import sys
from collections import deque

input  = sys.stdin.readline

H,W = map(int,input().split())

grid = [[500*500+1] * W for _  in range(H)]
wallinfo = [[0] * W for _  in range(H)]
dx,dy = [1,0,-1,0],[0,1,0,-1]
def OOM(x,y):
    if 0<=x<W and 0<y<H:
        return False
    return True
ed = [0,0]
que = deque([])
for i  in range(H):
    line = input()
    for j in range(W):
        if line[j] == '#':
            for d in range(4):
                if not OOM(j+dx[d],i+dy[d]):
                    wallinfo[i+dy[d]][j+dx[d]] = -1
            grid[i][j] = -1
        elif line[j] == 'S':
            que.append([j,i])
            grid[i][j] = 0
        elif line[j] =='E':
            ed = [j,i]
while que:
    x,y = que.popleft()

    for i in range(4):
        nextX,nextY = x + dx[i] , y + dy[i]
        if OOM(x,y) or grid[y][x] == -1: continue
        
        if grid[y][x] < grid[nextY][nextX] and wallinfo[y][x] == -1 and wallinfo[nextY][nextX] == -1:
            grid[nextY][nextX] = grid[y][x]
            que.appendleft([nextX,nextY])
        elif grid[y][x] + 1 <  grid[nextY][nextX]:
            grid[nextY][nextX] = grid[y][x] + 1
            que.append([nextX,nextY])


print(grid[ed[1]][ed[0]])