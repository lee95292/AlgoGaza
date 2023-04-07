"""
1. blowWind : BFS, turn ** 2 4*10^6
2. mixTemp: n**2
3. wall: n**2

temperature = n*n
aircons = [[x1,y1,d1]]
officies = [[x1,y1] ... ]
walls = n*n
바람 방향 0 ~ 4 : 좌 상 우 하
"""
from collections import deque

N,M,K = map(int,input().split())
temperature = [[0]*N for _ in range(N)]
walls = [[0]*N for _ in range(N)]
officies = []   # [x,y]
aircons = [] # [x,y,d]
moves = [[-1,0], [0,-1], [1,0], [0,1]]
        # 좌     상     우   하
windMoves = [
    [ [0], [1,0], [3,0]],
    [ [1], [0,1], [2,1]],
    [ [2], [1,2], [3,2]],
    [ [3], [0,3], [2,3]]
]


for i in range(N):
    line = list(map(int,input().split()))
    for j in range(N):
        if line[j] == 1:
            officies.append([j,i])
        if line[j] > 1:
            aircons.append([j,i,line[j]-2])

for i in range(M):
    y,x,s = map(int,input().split())
    walls[y-1][x-1] += s+1

def GRID_OOM(x,y):
    if 0<= x < N and 0 <= y < N:
        return False
    return True

def isAllOfficeCool():
    for [x,y] in officies:
        if temperature[y][x] < K:
            return False
    return True
def blowLocs(x,y,d):
    # 벽 0: 위 , 1: 왼
    locs = []

    for windMove in windMoves[d]:
        lx, ly = x,y
        flag = True
        for direction in windMove: # directions: [0,3], directoin: 3,2 ...
            dx,dy= moves[direction]
            cx,cy = lx+dx, ly+dy
            if GRID_OOM(cx,cy):
                flag = False
                break
            if direction == 0 and walls[ly][lx] >= 2: flag = False
            if direction == 1 and walls[ly][lx] == 1 or walls[ly][lx] == 3: flag = False
            if direction == 2 and walls[cy][cx] >= 2: flag = False
            if direction == 3 and walls[cy][cx] == 1 or walls[cy][cx] == 3: flag = False
            lx,ly = cx,cy
            if not flag: break
        if flag:
            locs.append([lx,ly])
    return locs



def blowWind(turn,aci):
    ax,ay,d = aci
    ax,ay = ax+ moves[d][0], ay + moves[d][1]
    # bfs_data = [x,y,d,t]
    que = deque([[ax,ay,d,turn-1]])
    visit = {}
    while que:
        x,y,cd,t = que.popleft()
        if t == 0: continue
        visit[(x,y)] = 1
        temperature[y][x]+=1
        locs = blowLocs(x,y,cd)
        for [cx,cy] in locs:
            if visit.get((cx,cy)): continue
            visit[(cx, cy)] = 1
            # temperature[cy][cx] += 1
            que.append([cx,cy,cd,t-1])

def mixTemp():
    mixMap = [[0]*N for _ in range(N)]
    for i in range(N-1,-1,-1):
        for j in range(N-1,-1,-1):
            for d in range(2):
                dx,dy = moves[d]
                cx,cy = j+dx, i+dy
                if GRID_OOM(cx,cy): continue

                diff = max(temperature[i][j],temperature[cy][cx]) - min(temperature[i][j],temperature[cy][cx])
                if diff < 4: continue
                if d == 0 and walls[i][j] >=2: continue
                if d == 1 and walls[i][j] == 1 or walls[i][j] == 3 : continue
                if temperature[i][j] > temperature[cy][cx]:
                    mixMap[cy][cx] += diff//4
                    mixMap[i][j] -= diff//4
                else:
                    mixMap[cy][cx] -= diff//4
                    mixMap[i][j] += diff//4
                # if d == 2 and walls[cy][cx] == 1 or walls[cy][cx] == 3: continue
                # if d == 3 and walls[cy][cx] >=2 : continue
    for i in range(N):
        for j in range(N):
            temperature[i][j] += mixMap[i][j]
def warmWallside():
    for i in range(N):
        for j in range(N):
            if temperature[i][j] == 0: continue
            if (i in [0,N-1]) or (j in [0,N-1]):
                temperature[i][j]-=1



answer=0
while True:
    answer+=1
    turn = 1
    for i in range(5):
        turn+=1
        for aircon in aircons:
            blowWind(turn,aircon)
    mixTemp()
    warmWallside()
    if isAllOfficeCool():
        print(answer)
        break
    elif answer > 100:
        print(-1)
        break


"""
10 0 10
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 1
4 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0


9 29 8
0 0 1 0 0 0 0 0 1 
0 0 3 0 0 0 0 0 0 
0 4 0 0 0 1 5 0 0 
1 3 4 0 3 2 0 3 1 
0 0 0 4 0 4 5 0 0 
0 0 0 0 0 0 0 3 1 
0 0 0 2 0 0 3 4 0 
0 0 0 0 3 0 0 0 0 
1 0 0 1 0 0 0 0 0 
4 1 0
1 5 1
2 4 0
3 4 0
4 4 0
7 2 1
7 1 0
9 2 1
3 8 0
6 5 0
5 3 1
2 8 0
8 4 1
5 9 0
9 5 1
4 9 0
6 2 1
3 5 1
7 6 1
9 8 0
8 3 1
2 8 1
7 9 0
2 1 0
7 2 0
7 3 0
1 3 1
9 3 0
6 5 1

-> 26


6 0 100
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
4 0 1 0 2 0
0 0 0 0 0 0
0 0 0 0 0 0
"""