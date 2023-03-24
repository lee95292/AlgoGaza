N,M = map(int,input().split())
# directions = [[1,0],[0,1],[-1,0],[0,-1]]
directions = [[0,-1],[0,1],[-1,0],[1,0]]
answer = 0
maze = [list(map(int,input().split())) for _ in range(N)]
attacks = [list(map(int,input().split())) for _ in range(M)]

sx,sy = 0,0
snailOrder = []
for r in range((N-1)//2):
    for i in range(N-r*2-1):
        snailOrder.append([sx,sy])
        sx+=1
    for i in range(N-r*2-1):
        snailOrder.append([sx, sy])
        sy+=1
    for i in range(N-r*2-1):
        snailOrder.append([sx, sy])
        sx-=1
    for i in range(N-r*2-1):
        snailOrder.append([sx, sy])
        sy-=1
    sx,sy = sx+1, sy+1

# grid = [[0]*N for _ in range(N)]
# for i,[x,y] in enumerate(snailOrder):
#     grid[y][x] = i+1
# for g in grid:
#     print(g)
snailOrder.reverse()


def MAZE_OOM(x,y):
    if 0 <= x < N and 0 <= y < N:
        return False
    return True

def printMaze(message):
    return
    print(message)
    for m in maze:
        print(m)
def fillSnail():
    fillOrder = 0
    for i in range(len(snailOrder)):
        fx,fy = snailOrder[fillOrder]
        tx,ty = snailOrder[i]
        if maze[ty][tx] == 0:
            continue
        maze[fy][fx] = maze[ty][tx]
        fillOrder+=1
    for i in range(fillOrder, len(snailOrder)):
        tx, ty = snailOrder[i]
        maze[ty][tx] = 0
    printMaze('fillSnail')

def attackMonster(t):
    global answer
    direction, power = attacks[t]
    dx,dy = directions[direction-1]
    for i in range(power):
        cx,cy = N // 2 + (i + 1) * dx, N // 2 + (i + 1) * dy
        if MAZE_OOM(cx,cy): continue
        if maze[cy][cx] != 0:
            # answer += maze[cy][cx]
            maze[cy][cx] = 0

    printMaze(f'attack monster power:{power}, dx{dx}, dy{dy}')

def deleteDuplicateMonster():
    global answer
    while True:
        isDel = False
        #IMPLEMENT
        prev = maze[snailOrder[0][1]][snailOrder[0][0]]
        delCnt = 0
        for midx in range(1,len(snailOrder)):
            cx,cy = snailOrder[midx]

            if prev == maze[cy][cx]:
                delCnt+=1
                continue

            if delCnt >= 3:
                isDel = True
                answer += (delCnt + 1) * prev
                for i in range(midx-delCnt-1,midx):
                    delx,dely = snailOrder[i]
                    maze[dely][delx] = 0
            prev = maze[cy][cx]
            delCnt = 0
            if maze[cy][cx] == 0:
                break
        if isDel:
            fillSnail()
        else:
            break

    pass
def pairMonsters():
    global maze
    pairs = [[0,maze[snailOrder[0][1]][snailOrder[0][0]]]]
    for i in range(len(snailOrder)):
        cx,cy = snailOrder[i]
        if maze[cy][cx] == 0: break
        elif pairs[-1][1] == maze[cy][cx]:
            pairs[-1][0]+=1
        else:
            pairs.append([1,maze[cy][cx]])
    tmp = []
    for p in pairs:
        tmp.extend(p)

    # maze = [[0]*N for _ in range(N)]
    for i in range(min(len(tmp), len(snailOrder))):
        cx, cy = snailOrder[i]
        maze[cy][cx] =  tmp[i]
    # for i in range(len(pairs)):
    #     if 2*i >= N-1: break
    #     cx1,cy1 = snailOrder[2*i]
    #     cx2, cy2 = snailOrder[2 * i + 1]
    #     maze[cy1][cx1] = pairs[i][0]
    #     maze[cy2][cx2] = pairs[i][1]


for i in range(M):
    attackMonster(i)
    fillSnail()
    deleteDuplicateMonster()
    pairMonsters()
    printMaze('')

print(answer)

"""
11 1
0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 
0 0 3 3 3 3 1 3 0 0 0 
0 0 1 3 3 2 2 3 0 0 0 
0 0 2 3 2 0 1 1 0 0 0 
0 0 1 1 1 1 3 3 0 0 0 
0 0 1 3 2 2 1 1 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 
2 3

7 1
0 0 0 0 0 0 0
3 2 1 3 0 3 0
2 1 2 1 0 1 0
2 1 1 0 0 1 1
3 3 0 0 0 1 2
3 3 3 0 3 3 2
2 3 2 0 3 2 3
2 2
"""