from collections import deque
N,M,C = map(int,input().split())

smap = [[0]*N for _ in range(N)]
emap = [[[]*N for _ in range(N)] for _ in range(N)]
grid = []
start = []
end = []
moves = [[0,-1],[-1,0],[1,0],[0,1]]
for i in range(N):
    grid.append(list(map(int,input().split())))
cary,carx = map(lambda x: int(x)-1,input().split())

for i in range(M):
    y1,x1,y2,x2 = map(lambda x:int(x)-1,input().split())
    smap[y1][x1] = i+1
    emap[y2][x2].append(i+1)
def GRID_OOM(x,y):
    if 0 <= x < N and 0 <= y < N: return False
    return True
# BFS, (x,y,type) -> sx,sy,dist
# type -1 : find start, dist
# type > 0 : find end, dist
TYPE_FINDSTART = - 100000
visit = [[-1]*N for _ in range(N)]
def findRoute(cx,cy,type,visitIdx):
    if type == -1: return [-1,-1,-1]
    que = deque([[cx,cy,0]])

    visit[cy][cx] = True
    startCand = []
    while que:
        x,y,d = que.popleft()
        if smap[y][x] > 0 and type==TYPE_FINDSTART and (len(startCand) == 0 or startCand[-1][2] == d):
            startCand.append([x,y,d])
        if type == TYPE_FINDSTART and len(startCand) > 0 and startCand[-1][2] < d:
            break
        if  type in emap[y][x] and type > 0:
            return [x,y,d]
        for [dx,dy] in moves:
            curx,cury = x+dx, y+dy
            if GRID_OOM(curx,cury): continue
            if grid[cury][curx] == 1: continue
            if visit[cury][curx] == visitIdx: continue
            visit[cury][curx] = visitIdx
            que.append([curx,cury,d+1])
    if type == TYPE_FINDSTART and len(startCand)> 0:
        startCand.sort(key=lambda x: (x[2],x[1],x[0]))
        return startCand[0]
    return [-1,-1,-1]
for i in range(M):
    carx,cary,d = findRoute(carx,cary,TYPE_FINDSTART,2*i)
    # print('turn start,cost:', d,'turn loc', carx, cary)
    C-=d
    type = smap[cary][carx]
    smap[cary][carx] = 0
    carx,cary,d = findRoute(carx,cary,type,2*i+1)
    # print('turn end, cost:', d, 'turn loc', carx, cary)
    C-=d
    if C < 0 or d == -1:
        print(-1)
        exit(0)
    C+= 2*d
    # print(C)
print(C)