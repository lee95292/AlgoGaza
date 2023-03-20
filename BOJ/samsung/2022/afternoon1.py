"""
start: 19:50
"""
import heapq

MAX_TIME = 15*15
BLOCKED_AREA = -100

N,M = map(int,input().split())
grid = []
stores = []
bases= []
storeBaseMap = []

for i in range(N):
    grid.append(list(map(int,input().split())))
    for j in range(N):
        if grid[i][j] == 1:
            bases.append([j,i])
            grid[i][j] = -1
B = len(bases)
for i in range(M):
    y,x = map(int,input().split())
    stores.append([x-1,y-1])
    grid[y-1][x-1] = -(i+1)


def mapBaseStore():
    visit = [False]*B
    for i,store in enumerate(stores):
        sx, sy = store
        profit = [100,100,100,100] # 거리, 행, 열,idx
        for j, [bx,by] in enumerate(bases):
            if visit[j]: continue
            
            distance = abs(bx-sx) + abs(by-sy)
            if distance < profit[0] \
                or (distance == profit[0] and  by < profit[1]) \
                or (distance == profit[0] and  by == profit[1] and bx < profit[2]):
                profit = [distance, by, bx,j]
        visit[profit[3]] = True
        storeBaseMap.append([profit[2],profit[1]])

def GRID_OOR(x,y):
    if 0 <= x < N and 0 <= y < N:
        return False
    return True

def getDist(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

mapBaseStore()
print(storeBaseMap)
moves = [[0,1],[-1,0],[1,0],[0,-1]]
que = [] # [time,storeNumber,x,y,start]
time = 0
for i in range(M):
    que.append([i+1,i,storeBaseMap[i][0],storeBaseMap[i][1],True])

answer = [MAX_TIME]*M
heapq.heapify(que)
visit =[[] for _ in range(M)]
for i in range(M):
    visit[i] = [[False]*N for _ in range(N)] 
while que:
    time,snum,x,y,start = heapq.heappop(que)
    if start:
        grid[y][x] = BLOCKED_AREA-time
    
    for [dx,dy] in moves:
        cx, cy = x+dx,y+dy
        if GRID_OOR(cx,cy):
            continue
        if answer[snum] != MAX_TIME:
            continue
        if visit[snum][cy][cx]:
            continue
        # if BLOCKED_AREA - time != grid[cy][cx] and grid[cy][cx] < BLOCKED_AREA:
        #     continue
        if grid[cy][cx] == -(snum+1):# 현재위치가 종착역인경우
            grid[cy][cx] = BLOCKED_AREA - time
            answer[snum] = min(answer[snum], time+1)
            continue
        visit[snum][cy][cx] = True
        heapq.heappush(que,[time+1,snum,cx,cy,False])
for g in grid:
    for k in g:
        print('%5s'%k,end=' ')

    print()
print(max(answer))
print(answer)

"""
5 3
0 1 0 0 0
0 0 0 0 0
1 0 0 0 0
0 1 0 0 0
0 0 0 0 0
3 4
3 2
2 2

4 2
0 0 0 0
0 0 1 0
0 0 0 0
1 0 0 0
4 3
4 4

4 2
1 0 0 0
0 0 1 0
0 0 0 0
0 0 0 0
1 3
1 4

x x x 0 0 1 1 x x 0 x
x 1 x x 1 1 1 x 0 1 1
0 0 x x 1 0 x x 1 0 1
x x 0 x 0 0 0 1 x 1 1
0 x x x 1 0 1 1 x 0 1
x 1 0 1 0 1 0 1 0 x x
0 0 x x 0 0 1 1 1 x x
1 1 1 1 0 0 0 1 0 x x
1 1 1 x x 1 1 1 1 x 1
1 1 0 0 0 x 1 1 0 x 1
1 x x 1 1 x 0 1 x x 1

11 21
0 0 1 0 0 1 1 1 0 0 1
1 1 1 1 1 1 1 0 0 1 1
0 0 0 0 1 0 1 0 1 0 1
1 0 0 0 0 0 0 1 1 1 1
0 1 0 1 1 0 1 1 0 0 1
0 1 0 1 0 1 0 1 0 0 1
0 0 0 1 0 0 1 1 1 1 0
1 1 1 1 0 0 0 1 0 1 0
1 1 1 1 0 1 1 1 1 1 1
1 1 0 0 0 1 1 1 0 0 1
1 1 0 1 1 0 0 1 1 0 1
10 10
5 9
11 10
7 3
4 4
11 6
1 2
5 3
3 8
2 8
3 3
9 5
1 1
3 4
7 11
8 11
1 9
6 10
11 3
3 2
6 1
"""

