"""
2423 전구를 켜라
구현이 까다로운 BFS

/ \ 방향을 0,1로 매핑해 각 경우별로 3차원 BFS
BFS 큐에는 [x,y,len]  len은 x,y에서 진행할때의 type
grid[y][x][case] : 회로가 case에서 x,y로 도달할 때까지 회전한 횟수

Test Cases

3 5
\\/\\
\\///
/\/\\

3 5
\////
/////
////\

3 5
\////
\\\\\
\\\/\
"""
from collections import deque

### PRE-DEFINITION###
def mapDigit(st):
    if st == '\\':
        return 0
    else:
        return 1

def OOM(x,y,M,N):
    if 0 <= x < M and 0 <= y < N:
        return False
    return True

### INPUT ###
N,M = map(int,input().split())
MAXV = M*N+10
grid = []

for i in range(N):
    grid.append(list(map(mapDigit, list(input()))))


### DEFINITION ###
dp = [[[MAXV,MAXV] for _ in range(M)] for _ in range(N)]


move =[ 
    [ [1,1,0],[1,0,1],[0,1,1],[-1,0,1],[-1,-1,0],[0,-1,1] ],
    [ [1,0,0],[1,-1,1],[0,1,0],[-1,1,1],[-1,0,0],[0,-1,0] ]
]
que = deque([[0,0,0]])

dp[0][0][0]=0
if grid[0][0] == 1:
    dp[0][0][0] +=1

### ALGORITIHM ###
while que:
    x,y,l = que.popleft()# l: x,y의 type
    dir = grid[y][x]
    flag = False
    for step in move[l]:
        xn, yn, ndir = x+step[0], y+step[1], step[2]
        if OOM(xn,yn,M,N): continue
        #Not Change 
        if ndir == grid[yn][xn] and dp[yn][xn][ndir] > dp[y][x][l]:
            dp[yn][xn][ndir] = dp[y][x][l]
            que.appendleft([xn,yn,ndir])
        #Change
        if ndir != grid[yn][xn] and dp[yn][xn][ndir] > dp[y][x][l]+1:
            dp[yn][xn][ndir] = dp[y][x][l]+1
            que.append([xn,yn,ndir])


        if xn==M-1 and yn == N-1 and ndir == 0:
            flag = True
    if flag:
        break

if dp[N-1][M-1][0] == MAXV:
    print("NO SOLUTION")
else:
    print(dp[N-1][M-1][0])