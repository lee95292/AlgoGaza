"""
카카오 인턴십 코테 #4
경주로 건설. 어려웠음
* visit[y][x][d]는 x,y점까지 d 방향으로 왔을 때 최소 건설비용을 DP로 저장한다. 
* 맵을 BFS로 탐색하며 최소건설비용을 찾는다.
* 큐에 [x,y,d]를 삽입해 x,y에 어떤 방향으로부터 건설했는지 체크하고, 다음 건설할 도로와 방향이 다른 경우/같은 경우를 따로 처리한다. 
"""
from collections import deque
debug = True


board = [
    [0,0,0,0],
    [0,0,0,1],
    [1,0,0,0],
    [1,0,1,0]
]
board = [[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]
n = len(board)
maxV = 500*30
visit = [[[maxV]*4 for _ in range(n)] for _ in range(n)]
que = deque()
dx = [1,0,0,-1]
dy = [0,1,-1,0]
visit[0][0]=[0,0,0,0]
que.append([0,0,-1])

while que:
    x,y,d = que.popleft()
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0<=nx<n and 0<=ny<n and  board[ny][nx] == 0 :
            cost=0
            origin = visit[ny][nx][i]
            if d == i or d == -1:
                visit[ny][nx][i] = min(visit[y][x][i] + 100, visit[ny][nx][i])
            elif d != i:
                minV = maxV
                for k in range(4):
                    if k != i:
                        minV = min(visit[y][x][k] + 600,minV)
                    visit[ny][nx][i] = min(minV, visit[ny][nx][i])
            
            if origin > visit[ny][nx][i]:
                que.append([nx,ny,i])
    if debug == True:
        print(x,y,d)
        for vv in visit:
            for v_ in vv:
                """
                print('{:6}'.format(min(v_)),end=' ')
                """
                for b in v_:
                    print("{:6}".format(b),end= ' ')
                print('/',end= '  ')
            print()
        print(que)            
print(min(visit[n-1][n-1]))