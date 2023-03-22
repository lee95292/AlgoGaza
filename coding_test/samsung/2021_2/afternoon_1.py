"""
1, 복제: 방향 생각
2. 이동 : 시체, OOR, 팩맨방향 이동불가, 8개의 이동 우선순위
3. 팩맨이동: 4개 이동 우선순위,
4. 시체 2턴 후 소멸
5. 부화
고려사항: 2**t만큼 몬스터 불어날 수 있음, -> 시간초과 주의

O(2**t * t)
[1] 복제: movedMonsters에서 eggs로 복사 (egg = movedMonsters.deepCopy())
[2] monsters = movedMonsters.deepCopy(), moveMonsters()
[3] movePackMan(), deadMap[i][j] =2
[4] if deamMap[i][j] > 0 : --1
[5] egg -> movedMonster copy
eggs = [n*n에 [[d1], ]]
monsters = [n*n에 [[d1], ]]
movedMonsters = -> monsters에서 복제
deadMap = [n*n 에 죽은시점에 2표시, 1씩 내리기]
px,py: 팩맨좌표
"""
M,T = map(int,input().split())
py,px = list(map(int,input().split()))
px,py = px-1,py-1
packmanPos = [px,py]

def getInitialMonsterMap():
    return [ [[] for _ in range(4)] for _ in range(4)]

eggs = getInitialMonsterMap()
monsters = getInitialMonsterMap()
movedMonsters = getInitialMonsterMap()
deadMonsters = [ [0]*4 for _ in range(4) ]

monsterMoves = [[0,-1],[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1]]
packmanMoves = [[0,-1],[-1,0],[0,1],[1,0]]

for i in range(M):
    y,x,d = map(int,input().split())
    x,y,d = x-1,y-1,d-1
    monsters[y][x].append(d)
    movedMonsters[y][x].append(d)

# ALGORITHM
def GRID_OOR(x,y):
    if 0<=x<4 and 0<=y<4:
        return False
    return True

def mapCopy(gridSrc, gridDest):
    for i in range(4):
        for j in range(4):
            gridDest[i][j] = gridSrc[i][j].copy()

def mapExtend(gridSrc, gridDest):
    for i in range(4):
        for j in range(4):
            gridDest[i][j].extend(gridSrc[i][j].copy())

def moveMonster(x,y,d):
    global packmanPos, movedMonsters, deadMonsters
    Px,Py = packmanPos
    flag=True
    for i in range(d, d+8):
        direction = i%8
        dx,dy = monsterMoves[direction]
        cx, cy = x + dx, y + dy
        if GRID_OOR(cx,cy): continue
        if deadMonsters[cy][cx] > 0: continue
        if cx == Px and cy == Py: continue
        movedMonsters[cy][cx].append(direction)
        flag=False
        break
    if flag : movedMonsters[y][x].append(d)

def duplicateMonsters(): #1
    global movedMonsters, eggs
    eggs = getInitialMonsterMap()
    mapCopy(movedMonsters, eggs)

def moveMonsters(): #2
    global movedMonsters, monsters
    mapCopy(movedMonsters,monsters)
    movedMonsters = getInitialMonsterMap()
    for i in range(4):
        for j in range(4):
            for k in monsters[i][j]:
                moveMonster(j,i,k)

def permutation(N,I):
    if N == 1:
        return [[I]]
    ret = []
    for i in range(4):
        for p in permutation(N-1,i):
            temp =[I]
            temp.extend(p)
            ret.append(temp)
    return ret

packmanMoveOrders = permutation(3,0)
packmanMoveOrders.extend(permutation(3,1))
packmanMoveOrders.extend(permutation(3,2))
packmanMoveOrders.extend(permutation(3,3))

def movePackman():
    global packmanPos
    Px,Py = packmanPos
    maxOrder, maxValue = [0,0,0],0
    for orders in packmanMoveOrders[::-1]: # orders: 0,0,0 / 0,1,2
        deadSum = 0
        isOOR=False
        Pcx, Pcy = Px,Py
        moveSet =[]
        for move in orders:
            dx,dy = packmanMoves[move]
            Pcx,Pcy = Pcx+dx, Pcy+dy

            if GRID_OOR(Pcx,Pcy):
                isOOR=True
                break
            if [Pcx, Pcy] not in moveSet:
                deadSum += len(movedMonsters[Pcy][Pcx])
                moveSet.append([Pcx, Pcy])
        if isOOR: continue

        if deadSum >= maxValue:
            maxOrder = orders
            maxValue = deadSum

    for order in maxOrder:
        dx,dy = packmanMoves[order]
        Px,Py = Px+dx, Py+dy
        if len(movedMonsters[Py][Px]) > 0:
            deadMonsters[Py][Px] = 3
        movedMonsters[Py][Px] = []
    packmanPos = [Px,Py]

def cleanDeads():
    for i in range(4):
        for j in range(4):
            if deadMonsters[i][j] > 0 :
                deadMonsters[i][j] -= 1

def createMonsters():
    global eggs, movedMonsters
    mapExtend(eggs, movedMonsters)
    mapCopy(movedMonsters,monsters)

def getAlivedMonsterCnt():
    answer = 0
    for i in range(4):
        for j in range(4):
            answer += len(movedMonsters[i][j])
    return answer

for i in range(T):
    duplicateMonsters()
    moveMonsters()
    movePackman()
    cleanDeads()
    createMonsters()

print(getAlivedMonsterCnt())