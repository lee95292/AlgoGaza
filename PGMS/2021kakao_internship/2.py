places= [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

debug = False
dx = [1,-1,0,0]
dy = [0,0,1,-1]
answer = []

for room in places:
    roomarr = []
    players =[]
    for idx,row in enumerate(room):
        units = [x for x in row]
        roomarr.append(units)
        players.extend([[i,idx] for i,x in enumerate(units) if x == 'P'])
    
    if debug == True:
        print('======')
        for room in roomarr:
            print(room)
        print(players)
    
    flag = False

    for player in players:
        visit = [[0]*5 for _ in range(5)]
        que = [[player[0],player[1]]]
        visit[player[1]][player[0]] =1
        while que:
            x,y= que.pop()
            for i in range(4):
                xn,yn = x+dx[i], y+dy[i]
                mdist = abs(player[0]-xn) + abs(player[1]-yn)
                if 0<=xn<len(room) and 0<=yn<len(room) and roomarr[yn][xn] != 'X' and mdist <=2 and visit[yn][xn]==0:
                    if roomarr[yn][xn] =='P':
                        flag = True
                        break
                    que.append([xn,yn])
                    visit[yn][xn] = 1
            
            if flag:
                break
        if flag:
            break
    if flag:
        answer.append(0)
    else:
        answer.append(1)
print(answer)