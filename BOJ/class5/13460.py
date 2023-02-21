"""
BOJ class5 구슬탈출 시뮬레이션,,?

1. 구슬 겹치지 않도록
2. 이전에 횡단이동했으면 이후엔 종단이동

5 5
#####
#..B#
#.#.#
#RO.#
#####
"""
### PRE-DEFINITION ###
N,M = map(int,input().split())
grid = [[0]*M for _ in range(N)]
rx,ry,bx,by= 0,0,0,0
directions = [ (1,0),(-1,0),(0,1),(0,-1)]
answer = 11

for i in range(N):
    line = input()
    for j in range(M):
        if line[j] == '#':
            grid[i][j] = -1
        elif line[j] == "O":
            grid[i][j] = 1
        elif line[j] == "B":
            bx,by = j,i
        elif line[j] == "R":
            rx,ry = j,i
def rolling(x,y,dx,dy,ball=[-1,-1]):
    r = 1
    while grid[y+r*dy][x+r*dx] != -1 \
        and not (ball[0] == x+r*dx and ball[1] == y+r*dy):
        if grid[y+r*dy][x+r*dx] == 1:
            return [-1,-1]
        r+=1
    r-=1
    return [x+r*dx,y+r*dy]

def traverse(turn,rx,ry,bx,by,prev):
    global answer
    if turn >= answer:
        # print('answer',answer)
        return
    # print(turn,'    '*turn, f'turn: {turn}, [rx,ry]:[{rx},{ry}], [bx,by]:[{bx},{by}], prev:{prev}')
    for dir in range(prev*2 , prev*2 + 2):
        dx,dy = directions[dir]
        nrx, nry, nbx, nby, r = rx,ry,bx,by, 1
        redOrder = nrx*dx + nry * dy
        blueOrder = nbx * dx + nby * dy

        if redOrder >= blueOrder:
            nrx, nry = rolling(nrx,nry,dx,dy)
            nbx, nby = rolling(nbx,nby,dx,dy,[nrx,nry])
        else:
            nbx,nby = rolling(nbx,nby, dx,dy)
            nrx,nry = rolling(nrx,nry, dx,dy,[nbx,nby])
        # print(turn,'    '*turn,f'[dx,dy]: [{dx},{dy}] / [nrx,nry]: [{nrx},{nry}], [nbx,nby]: [{nbx},{nby}]')
        if nrx == -1 and nbx != -1 : # 빨간공만 구멍에 들어감
            answer = min(answer,turn+1)
        elif nrx !=-1 and nbx !=-1 : # 두 공 모두 구멍에 들어가지 않음
            traverse(turn+1, nrx, nry, nbx, nby, (prev+1)%2)
        # 나머지: 파란공만 들어가거나 두 공 모두 들어감

traverse(0,rx,ry,bx,by,0)
traverse(0,rx,ry,bx,by,1)

if answer == 11:
    print(-1)
else:
    print(answer)