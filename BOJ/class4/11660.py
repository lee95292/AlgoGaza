import sys
input = sys.stdin.readline

n,m = list(map(int,input().split()))
pos = []
board = [[] for _ in range(n)]

for i in range(n):
    board[i].extend(list(map(int,input().split())))
for i in range(m):
    pos.append(list(map(int,input().split())))

for i in range(n):
    for j in range(n):
        if i > 0:
            board[i][j] += board[i-1][j]
        if j > 0:
            board[i][j] += board[i][j-1] 
        if i > 0 and j > 0 :
            board[i][j]-=board[i-1][j-1]


for p in pos:
    x1,y1,x2,y2 = p
    x1,y1,x2,y2=x1-1,y1-1,x2-1,y2-1
    ret = board[x2][y2] 
    if x1 > 0 :
        ret -= board[x1-1][y2]
    if y1 > 0 :
        ret -= board[x2][y1-1]
    if x1 >0 and y1 > 0:
        ret += board[x1-1][y1-1]  
    print(ret)


"""
4 3
1 2 3 4
2 3 4 5
3 4 5 6
4 5 6 7

2 2 3 4
3 4 3 4
1 1 4 4

2 4
1 2
3 4
1 1 1 1
1 2 1 2
2 1 2 1
2 2 2 2
"""