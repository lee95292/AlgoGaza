"""
BOJ 11559 뿌요뿌요, 그래프 탐색(DFS)
"""
from collections import deque
game_map = []
for i in range(12):
    game_map.append(list(input()))
def OOM(x,y):
    if 0<=x<6 and 0<=y<12:
        return False
    return True
dx,dy = [1,0,-1,0],[0,1,0,-1]
visit = []
res = [0]
def dfs(x,y,r):
    if game_map[y][x] == '.':
        return 0
    visit[y][x] = 1
    for i in range(4):
        nextX,nextY = x+dx[i], y+dy[i]
        if OOM(nextX,nextY) : continue
        if visit[nextY][nextX]==1 : continue
        if r != game_map[nextY][nextX]: continue
        res[0]+=1
        dfs(nextX,nextY,r)
        
    return 
def clean():
    for i in range(6):
        li = []
        for j in range(11,-1,-1):
            if game_map[j][i] != '.':
                li.append(game_map[j][i])
                game_map[j][i] = '.'
        for j in range(len(li)):
            game_map[11-j][i] = li[j]
answer = 0
def printMap(message):
    print(message)
    for m in game_map:
        print(*m, end='  ')
        print()
def bomb():
    for i in range(12):
        for j in range(6):
            if visit[i][j]==1:
                game_map[i][j]='.'
while True:
    derv= 0
    for i in range(6):
        for j in range(11,-1,-1):
            if game_map[j][i] !='.':
                while True:
                    visit = [[False]*6 for _ in range(12)]
                    res[0] = 1
                    dfs(i,j,game_map[j][i])
                    if res[0] >=4:
                        derv+=1
                        bomb()
                        # printMap(f'After Bomb{res[0]}, xy: {i},{j}')
                    else:
                        break
    
    clean()
    if derv==0:
        break
    else:
        answer+=1
                

print(answer)



"""
......
......
......
......
......
......
......
......
.Y....
.YG...
RRYG..
RRYGG.

......
......
......
......
..R...
GBR...
RRY...
GRY...
YYR...
GYR...
RRPP..
GRPP..


......
......
......
......
......
GB....
......
G.....
......
G.....
......
G.....

......
......
......
......
......
......
......
.AA...
ACA...
CCC...
GGGG..
YYYY..
"""