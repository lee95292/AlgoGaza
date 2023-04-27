##문제 : 배추농장의 배추들에게 상하좌우로 전파되는 농약류 지렁이의 최소개수를 구하는 문제
## 해결방법: 완전탐색
## REMIND
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

tc = int(input())

for t in range(tc):
    m,n,k = list(map(int, input().split()))
    gr = [ [0] *  m  for x in range(n)]
    visit = [ [0] *  m  for x in range(n)]
    
    cnt = 0

    bc = []
    for i in range(k):
        x,y = list(map(int,input().split()))
        bc.append([x,y])
        gr[y][x] = 1

    def placeWorm(b):
        x,y= b
        dx=[1,0,-1,0]
        dy=[0,1,0,-1]
        for i in range(4):
            xp = x + dx[i]
            yp = y + dy[i]

            if xp < 0 or yp < 0 or xp >= m or yp >= n or gr[yp][xp] == 0 or visit[yp][xp]==1:
                continue
            visit[yp][xp] = 1
            #print(x, y)
            placeWorm([xp,yp])

    for b in bc:
        x,y= b
        if visit[y][x] == 1:
            continue
        visit[y][x]=1
        placeWorm(b)
        cnt= cnt +1
    
    print(cnt)
            