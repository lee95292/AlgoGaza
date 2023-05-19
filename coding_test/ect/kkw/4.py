"""
문제: 소나기 피하기
최대 1000 * 1000 배열
"""
from collections import deque

n  = int(input())
grid = []
INIT_VALUE = 2001
answer = [[INIT_VALUE]*n for _ in range(n)]
moves = [[1,0],[0,1],[-1,0],[0,-1]]

def GRID_OOR(x,y):
    if 0<= x < n and 0<= y < n: return False
    return True

que = deque()
for i in range(n):
    line = list(map(int,list(input())))
    grid.append(line)
    for j,v in enumerate(line):
        if v == 1:
            for d in range(4):
                que.append([0,d,j,i]) # Queue에 넣는 값: [빌딩으로부터의 거리, 방향, x, y]
                answer[i][j] = 0

while que : 
    dist, direction, x,y = que.popleft()
    dx,dy = moves[direction]
    cx, cy = x + dx, y + dy
    if GRID_OOR(cx,cy): continue
    if answer[cy][cx] == 0 : continue

    que.append([dist+1, direction, cx,cy])
    answer[cy][cx] = min(answer[cy][cx], dist+1)

for line in answer:
    print(*list(map(lambda x: -1 if x == INIT_VALUE else x, line)))
