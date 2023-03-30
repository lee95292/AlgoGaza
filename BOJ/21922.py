# import sys
# from collections import deque
# input = sys.stdin.readline
# N,M = map(int,input().split())
# grid = [[0]*M for _ in range(N)]
# que = deque([])
# moves = [ [1,0], [0,1], [-1,0], [0,-1]]
# items = [
#     [],
#     [2,1,0,3],
#     [0,3,2,1],
#     [3,2,1,0],
#     [1,0,3,2]
# ]
# def GRID_OOM(x,y):
#     if 0 <= x < M and 0 <= y < N: return False
#     return True
# visit = [[0]*M for _ in range(N) ]
# for i in range(N):
#     line = list(map(int,input().split()))
#     for j in range(M):
#         if line[j] == 9:
#             que.extend([[j,i,x] for x in range(4)])
#             visit[i][j]=2**4-1
#         elif line[j] > 0:
#             grid[i][j] = line[j]-1


# while que:
#     x,y,d = que.popleft()
#     dx,dy = moves[d]
#     cx,cy = x + dx, y+ dy
#     if GRID_OOM(cx,cy): continue
#     if visit[cy][cx]&d == d: continue
#     visit[cy][cx] |= d
#     new_d = d
#     if grid[cy][cx]> 0:
#         new_d = items[grid[cy][cx]][d]
#     que.append([cx,cy,new_d])

# answer = 0
# for v in visit:
#     print(v)
# for i in range(N):
#     for j in range(M):
#         if visit[i][j] > 0:
#             answer+=1
# print(answer)

import sys
from collections import deque
input = sys.stdin.readline
N,M = map(int,input().split())
grid = [[0]*M for _ in range(N)]
que = deque([])
moves = [ [1,0], [0,1], [-1,0], [0,-1]]
items = [
    [],
    [2,1,0,3],
    [0,3,2,1],
    [3,2,1,0],
    [1,0,3,2]
]
def GRID_OOM(x,y):
    if 0 <= x < M and 0 <= y < N: return False
    return True
visit = [[0]*M for _ in range(N)]
for i in range(N):
    line = list(map(int,input().split()))
    for j in range(M):
        if line[j] == 9:
            for k in range(4):
                que.append([j,i,k])
            visit[i][j] = 2**4-1 
        elif line[j] > 0:
            grid[i][j] = line[j]



while que:
    x,y,d = que.popleft()
    dx,dy = moves[d]
    cx,cy = x + dx, y+ dy
    if GRID_OOM(cx,cy): continue
    if visit[cy][cx] & 2**(d+1) == 2**(d+1): continue
    visit[cy][cx] |= 2**(d+1)
    new_d = d
    if grid[cy][cx]> 0:
        new_d = items[grid[cy][cx]][d]
    
    que.append([cx,cy,new_d])

answer = 0

# for v in visit:
#     print(v)
for i in range(N):
    for j in range(M):
        if visit[i][j] > 0:
            answer+=1
print(answer)