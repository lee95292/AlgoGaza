"""
2 4
CAAB
ADCB
"""
import sys
input = sys.stdin.readline

r,c = map(int,input().split())
dx, dy = [1,-1,0,0],[0,0,1,-1]
board = []
visit = [False]*26
for i in range(r):
    board.append(list(map(lambda x: ord(x)-65, list(input()))))

answer = [0]
def dfs(x,y,k):
    if answer[0] > 25:
        return
    if visit[board[y][x]] == True:
        return
    visit[board[y][x]] = True
    answer[0] = max(answer[0],k)
    for i in range(4):
        xp,yp = x+dx[i], y+dy[i]
        if 0<=xp<c and 0<=yp<r and not visit[board[yp][xp]]: 
            dfs(xp,yp,k+1)
    visit[board[y][x]] = False
dfs(0,0,1) 
print(answer[0])