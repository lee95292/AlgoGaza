import sys
input = sys.stdin.readline
debug = False
R,C,M = map(int,input().split())
moves = [[0,-1],[0,1],[1,0],[-1,0]]
grid = []
sharkPtr = [None]

class Shark:
    def __init__(self,x,y,speed,direction,size):
        self.x, self.y = x,y
        self.speed, self.direction,self.size = speed,direction,size
        if direction >= 2 and self.speed >=  2*(C-1): self.speed = self.speed % (2*(C-1))
        if direction < 2 and self.speed >= 2 * (R-1):self.speed = self.speed % (2*(R-1))
    def move(self):
        dx,dy = moves[self.direction]
        spd = self.speed
        cx,cy = self.x + dx*self.speed, self.y + dy*self.speed
        while OOM_X(cx):
            if cx > C-1 : cx = 2*C-2-cx
            elif cx < 0: cx = abs(cx)
            self.changeDirection()
        while OOM_Y(cy):
            if cy > R-1 : cy = 2*R -2 -cy
            elif cy < 0: cy = abs(cy)
            self.changeDirection()
        self.x, self.y = cx,cy

    def changeDirection(self):
        if self.direction%2 == 0:
            self.direction = self.direction + 1
        else:
            self.direction = self.direction - 1
def printGrid():
    if not debug: return
    print('============','grid','============')
    for g in grid:
        print(list(map(lambda x: chr(x+64),g)),end=' ')
        print()

    for i in range(M):
        if sharkPtr[i] == None:continue
        print('shark', chr(i+64), 'direction',sharkPtr[i].direction)
def OOM_X(x):
    if 0 <= x < C: return False
    return True
def OOM_Y(y):
    if 0 <= y < R: return False
    return True

def initGrid():
    return[[0] * C for _ in range(R)]

def fishing(line):
    for i in range(R):
        ptr = grid[i][line]
        if ptr > 0:
            size = sharkPtr[ptr].size
            sharkPtr[ptr] = None
            grid[i][line] = 0
            return size
    return 0
def moveSharks():
    global grid
    # loop sharkptr(1, M+1), shark.move
    for i in range(1,M+1):
        if sharkPtr[i] == None: continue
        sharkPtr[i].move()

    # init grid, append sharks to grid, eat anthor sharks
    grid = initGrid()
    for i in range(1,M+1):
        if sharkPtr[i] == None: continue
        shk = sharkPtr[i]
        x,y = shk.x,shk.y
        if grid[y][x] == 0:
            grid[y][x] = i
            continue
        pshkPtr = grid[y][x]
        pshk = sharkPtr[pshkPtr]
        if pshk.size > shk.size:
            sharkPtr[i] = None
        else:
            sharkPtr[pshkPtr] = None
            grid[y][x] = i

grid = initGrid()
for i in range(M):
    y,x,speed, direction, size = map(int,input().split())
    y,x,direction = y-1,x-1,direction-1
    sharkPtr.append(Shark(x,y,speed,direction,size))
    grid[y][x] = i+1

answer = 0
for i in range(C):
    answer += fishing(i)
    moveSharks()
    printGrid()
print(answer)
