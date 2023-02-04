"""
5 5
2
4 2 1
2 4 0
"""
from collections import deque
import heapq
import sys
input = sys.stdin.readline
N,M = map(int,input().split())
K = int(input())
trafflicList = []
for i in range(K):
    trafflicList.append(list(map(int,input().split())))
MAX_VALUE = M*N+10
grid = [[MAX_VALUE]*N for _ in range(M)]
def modBound(x,y):
    if 0<=x<N and 0<=y<M:
        grid[y][x] = -1

for traffic in trafflicList:
    x,y,d = traffic[0]-1,traffic[1]-1,traffic[2]
    grid[y][x] = -1
    
    for i in range(0,d+1):
        a,b = d-i,i
        for op in [[1,1],[1,-1],[-1,1],[-1,-1]]:
            modBound(x+a*op[0],y+b*op[1])
        
que = deque([[0,0,0]])
dx = [1,0,-1,0]
dy = [0,1,0,-1]
while que:
    x,y,r = que.popleft()
    for i in range(4):
        nextX,nextY = x + dx[i], y + dy[i]
        if 0<= nextX < N and 0<= nextY < M and r+1 < grid[nextY][nextX] :
            grid[nextY][nextX] = r+1
            que.append([nextX,nextY,r+1])
    if x==N-1 and y ==M-1:
        break
# for g in grid:
#     print(*g,end ='   ')
#     print()
if grid[M-1][N-1] == MAX_VALUE:
    print("NO")
else:
    print("YES")
    print(grid[M-1][N-1])