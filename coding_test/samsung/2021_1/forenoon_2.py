"""
1. 폭탄제거
크기 > 빨간돌 개수 > 낮은 행, 높은 열부터 시작 (높은행,낮은열 돌 우선)


data structure
rockCounts={} - 돌 개수 세기

빨간돌 : 1
돌: -1
"""
from collections import deque

N,M = map(int,input().split())
grid = [[0]*N for _ in range(N)]
rockCnt = {x:0 for x in range(2,M+2)}
moves = [[-1,0],[0,1],[1,0],[0,-1]] # 좌, 하, 우, 상

for i in range(N):
    line = list(map(int, input().split()))
    for j in range(N):
        if line[j] >= 0:
            grid[i][j] = line[j]+1
            if grid[i][j] >= 2: rockCnt[grid[i][j]]+=1
        else: grid[i][j] = line[j]

def printGrid(msg):
    print('------------------------')
    print(msg)
    print('------------------------')

    for g in grid:
        print(g, end='')
        print()

def GRID_OOM(x,y):
    if 0 <= x < N and 0 <= y < N : return False
    return True
def isAllClean():
    for i in range(2,M+2):
        if rockCnt[i] > 0: return False
    return True

def bomb():
    visit = [[False]*N for _ in range(N)]
    # [total,red,x,y]
    total, red, x, y, color = 0,N*N-2,N-1,0,0
    for i in range(N):
        for j in range(N-1,-1,-1):
            if grid[i][j] <= 1: continue
            if visit[i][j] == True: continue

            [t, r, sx, sy] = bfs(visit,j,i)
            # if t-r != rockCnt[grid[i][j]]: continue
            if t < 2 or total > t \
                or (total == t and red < r) \
                or (total == t and red == r and sy < y) \
                or (total == t and red == r and sy == y and sx < x): continue
            total, red, x, y,color = t, r, sx, sy, grid[i][j]
    # bomb
    if color == 0: return 0
    visit = [[False] * N for _ in range(N)]
    que = deque([[x,y]])
    visit[y][x] = True
    while que:
        x,y = que.popleft()
        for [dx,dy] in moves:
            cx,cy = x+dx, y+dy
            if GRID_OOM(cx,cy): continue
            if visit[cy][cx]: continue
            if grid[cy][cx] != color and grid[cy][cx] != 1: continue
            visit[cy][cx] = True
            que.append([cx,cy])
        grid[y][x] = 0
    rockCnt[color] -= total-red
    return total**2

def bfs(visit,tx,ty):
    if visit[ty][tx] == True: return [0,0,0,0]
    if grid[ty][tx] <= 1: return [0,0,0,0]
    redRocks = []

    total = 1
    visit[ty][tx] = True
    color = grid[ty][tx]
    que = deque([[tx,ty]])
    while que:
        x,y = que.popleft()
        for [dx,dy] in moves:
            cx,cy= x+dx, y+dy
            if GRID_OOM(cx,cy): continue # OOM
            if visit[cy][cx] : continue
            if grid[cy][cx] != color and grid[cy][cx] != 1: continue # 색깔 다른경우
            if grid[cy][cx] == 1: # 시작부분 찾기
                redRocks.append([cx,cy])
            if cy > ty: tx,ty =cx,cy
            if ty == cy and tx > cx: tx,ty = cx,cy
            visit[cy][cx] = True
            total+=1
            que.append([cx,cy])
    for [x,y] in redRocks:
        visit[y][x] = False
    return [total, len(redRocks), tx,ty]


def gravity():
    for j in range(N):
        stacks = [deque([])]
        for i in range(N-1,-1,-1):
            if grid[i][j] > 0:
                stacks[-1].append(grid[i][j])
            if grid[i][j] == -1: stacks.append(deque([]))
        stp = 0
        for i in range(N-1,-1,-1):
            if grid[i][j] == -1: stp+=1
            elif len(stacks[stp]) > 0: grid[i][j] = stacks[stp].popleft()
            else: grid[i][j] = 0
def rotate():
    tmp = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            tmp[N-1-j][i]=grid[i][j]
    for i in range(N):
        for j in range(N):
            grid[i][j] = tmp[i][j]

score = 0

while True:
    add = bomb()
    score += add
    gravity()
    rotate()
    gravity()
    if add == 0:
        print(score)
        break

# printGrid('before bomb')
# bomb()
# printGrid('after bomb')
# gravity()
# printGrid('after gravity')
# rotate()
# printGrid('after rotate')
# gravity()
# printGrid('after gravity')
#
# print('====================')
# printGrid('before bomb')
# bomb()
# printGrid('after bomb')
# gravity()
# printGrid('after gravity')
# rotate()
# printGrid('after rotate')
# gravity()
# printGrid('after gravity')


"""
4 2
1 1 -1 -1
1 1 -1 -1
2 2 2 -1
0 0 -1 -1
"""