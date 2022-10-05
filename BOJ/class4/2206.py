# 백준 벽 부수고 이동하기
# BFS, DP
from collections import deque
import sys
input = sys.stdin.readline
maxv = 1000001
n,m = list(map(int, input().split()))
dp = [[ [maxv,maxv] for i in range(m)] for j in range(n)]

arr = []
que = deque()
directions = [(1,0), (-1,0), (0,1), (0,-1)]

for i in range(n):
    arr.append(list(map(int,input().removesuffix('\n'))))

#(x,y,j) j - # of jumped wall

que.append([0,0,0])
dp[0][0][0] =1
while que:
    x,y,j = que.popleft()
    # print(x,y,j)
    
    #End
    if x == m-1 and y == n-1:
        break
    for xi,yi in directions:
        xp, yp = x + xi, y+ yi
        # OOR
        if xp >= m or yp >= n or xp < 0 or yp < 0:
            continue
        
        
        # 벽 막힘, j=0
        if arr[yp][xp] == 1 and j == 0 and  dp[y][x][0] + 1 < dp[yp][xp][1]:
            dp[yp][xp][1] = dp[y][x][0] + 1
            que.append((xp,yp,1))
                
        
        # 벽 막히지 않음
        elif arr[yp][xp] == 0 and  dp[y][x][j] + 1 < dp[yp][xp][j]:
            dp[yp][xp][j] = dp[y][x][j] + 1 
            que.append((xp,yp,j))



if min(dp[n-1][m-1]) < maxv:
    print(min(dp[n-1][m-1]))
else:
    print(-1)



# for i in range(n):
#     for j in range(m):
#         if dp[i][j][0] == maxv:
#             dp[i][j][0] = -1
#         if dp[i][j][1] == maxv:
#             dp[i][j][1] = -1


# for i in range(n):
#     print(dp[i])


'''
6 4
0100
1110
1000
0000
0111
0000

6 4
0100
1110
0000
0000
0111
0000

4 4
0110
1110
1110
1110


5 5
00000
01111
01000
01011
01010

2 2
00
00

'''