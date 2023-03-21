N,M,K = map(int,input().split())
grid = []

for i in range(N):
    grid.append(list(map(int, input().split())))

def GRID_OOR(x,y):
    if 0 <= x < N and 0 <= y < N:
        return False
    return True

teamsRoute = [[] for _ in range(M)]
teamPeopleNum = [0]*M
headTailPoints = [[-1,-1,-1] for _ in range(M)] #[head,tail, direction(+,-1)]
moves = [[1,0],[0,-1],[-1,0],[0,1]]
ballDirection = [[1,0],[0,1],[-1,0],[0,-1]]
gridVisit = [[False]*N for _ in range(N)]

def findTeamsRoute(x,y,cnt):
    if gridVisit[y][x]:
        return False

    gridVisit[y][x] = True
    teamsRoute[cnt].append([x,y])
    for [dx,dy] in moves:
        cx,cy = x+dx, y+dy
        if GRID_OOR(cx,cy): continue
        if grid[cy][cx] == 0: continue
        if gridVisit[cy][cx]: continue
        findTeamsRoute(cx,cy,cnt)

teamCnt = 0
for i in range(N):
    for j in range(N):
        if grid[i][j] == 0: continue
        if gridVisit[i][j]: continue
        findTeamsRoute(j,i,teamCnt)
        teamCnt+=1

for k, routes in enumerate(teamsRoute):
    for t,[x,y] in enumerate(routes):
        if grid[y][x] == 1:
            headTailPoints[k][0] = t
            teamPeopleNum[k]+=1
        elif grid[y][x] == 3:
            headTailPoints[k][1] = t
            teamPeopleNum[k]+=1
        elif grid[y][x] == 2:
            teamPeopleNum[k]+=1

        r = grid[y][x] # 초기값
        grid[y][x] = [t,k,r] # 루트에서 N번째, K번째 팀, 초깃값

    headNextNum = (headTailPoints[k][0] + 1) % len(teamsRoute[k])
    nx,ny = teamsRoute[k][headNextNum]
    if grid[ny][nx][2] == 4:
        headTailPoints[k][2] = 1

inc = [[x for x in range(N)], [x for x in range(N-1,-1,-1)], [0]*N]
def getScoreAndTeam(xinc, yinc, n):
    score,team_ = -1,-1
    for i in range(N):
        ballLocation = grid[inc[yinc][i]][inc[xinc][i]]
        if xinc == 2:
            ballLocation = grid[inc[yinc][i]][n]
        elif yinc == 2 :
            ballLocation = grid[n][inc[xinc][i]]

        if ballLocation == 0 : continue
        team = ballLocation[1]
        pos = headTailPoints[team][2]
        head,tail = headTailPoints[team][0],headTailPoints[team][1]
        for j in range(1,teamPeopleNum[team]+1):
            if head+pos*-j == ballLocation[0]:
                print(f'head {head}, tail {tail}, j {j}, team {team}, i {i}')
                return [j,team]
        # if pos > 0 and head <= ballLocation[0] or ballLocation[0] <= tail:
        #     print(f'head {head}, tail {tail}, ballLocation[0]{ballLocation[0]}')
        #     return [(ballLocation[0]-head)%teamPeopleNum[team],team]
        # elif pos < 0 and tail <= ballLocation[0] or ballLocation[0] <= head:
        #     return [(head-ballLocation[0])%teamPeopleNum[team],team]

    return [score,team_]

answer = 0
for k in range(K):
    # 라운드별 Head, Tail 업데이트
    for m in range(M):
        headTailPoints[m][0] = (headTailPoints[m][0]+headTailPoints[m][2]) % len(teamsRoute[m])
        headTailPoints[m][1] = (headTailPoints[m][1]+headTailPoints[m][2]) % len(teamsRoute[m])

    # 라운드별 공 던지기
    dth = (k//N)%N
    nth = k%N
    score,team = 0,0
    if dth == 0:
        score,team =getScoreAndTeam(0,2,nth)
    elif dth == 1:
        score,team =getScoreAndTeam(1,2,nth)
    elif dth == 2:
        score,team =getScoreAndTeam(2,1,nth)
    elif dth == 3:
        score,team =getScoreAndTeam(2,0,nth)
    print(score, team,dth)
    for g in grid:
        print(f'%9s',g)

    if team != -1:
        answer+=score**2
        headTailPoints[team][2] *= -1
        headTailPoints[team][0], headTailPoints[team][1] = headTailPoints[team][1], headTailPoints[team][0]
print(answer)