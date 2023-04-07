"""
1/ 달팽이 2번 반복시 중복 제거
2/ 함수 똑바로 구현 (가까운 점 계산 시 가운데 계산안넣은거)

"""
N,M,H,K = map(int,input().split())
trees = [[0]*N for _ in range(N)]
runners = [[[0]*4for _ in range(N)] for _ in range(N)]
moves = [[0,-1], [1,0], [0,1],[-1,0]] # 상 우 하 좌
x,y = 0,0
arr=[[0,0,2]]
for i in range(0,N-1,2):
    for j in range(N-1-i):
        y+=1
        arr.append([x,y,2])
    for j in range(N-1-i):
        x+=1
        arr.append([x,y,1])
    for j in range(N-1-i):
        y-=1
        arr.append([x,y,0])
    for j in range(N-2-i):
        x-=1
        arr.append([x,y,3])
    y+=1
    arr.append([x,y,2])
snailArr = list(map(lambda x:[x[0],x[1],(x[2]+2)%4] ,arr))
snailArr.reverse()

snailArr.extend(arr[1:])
for i in range(len(arr),len(snailArr)-1):
    snailArr[i][2] = snailArr[i+1][2]
snailArr[0][2] = 0
snailArr[-1][2] = 0
snailArr = snailArr[:-1]
def GRID_OOM(x,y):
    if 0 <= x < N and 0 <= y < N: return False
    return True
def nearPoints(x,y):
    li = []
    for dx in range(-3, 4):
        for dy in range(-(3 - abs(dx)), 4 - abs(dx)):
            if GRID_OOM(x+dx,y+dy): continue
            li.append([x+dx,y+dy])
    return li

for i in range(M):
    y,x,d= map(int,input().split())
    y,x = y-1,x-1
    if d == 1: runners[y][x][1]+=1 #우
    if d== 2: runners[y][x][2]+=1 # 하
for i in range(H):
    y,x = map(lambda x: int(x)-1, input().split())
    trees[y][x] = 1

def moveRunners(turn, runners):
    sx, sy, _ = snailArr[turn-1]
    newRunners = [[[0]*4for _ in range(N)] for _ in range(N)]
    np = nearPoints(sx, sy)

    for [j,i] in np:
        for d in range(4):
            val = runners[i][j][d]
            runners[i][j][d]=0
            dx,dy = moves[d]
            cx,cy = j+dx,i+dy
            if GRID_OOM(cx,cy):
                d = (d+2)%4
                dx,dy = moves[d]
                cx,cy = j+dx,i+dy
            if cx ==sx and cy ==sy:
                newRunners[i][j][d] += val
            else: newRunners[cy][cx][d] += val
    for i in range(max(0,sy-4), min(N,sy+5)):
        for j in range(max(0,sx-4), min(N,sx+5)):
            for d in range(4):
                runners[i][j][d] += newRunners[i][j][d]
def catchRunners(turn,runners):
    sx, sy, d = snailArr[turn]
    # print(sx,sy,d)
    dx,dy = moves[d]
    catch = 0
    for i in range(3):
        cx,cy = sx + dx*i, sy + dy*i
        if GRID_OOM(cx,cy):continue
        if trees[cy][cx]==1: continue
        catch += sum(runners[cy][cx])
        runners[cy][cx] = [0,0,0,0]
    return catch

answer = 0
for k in range(1,K+1):
    moveRunners(k%len(snailArr),runners)
    answer += k*catchRunners(k%len(snailArr),runners)
print(answer)


"""
5 3 1 2
2 4 1
1 4 2
4 2 1
2 4
"""