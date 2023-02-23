"""
BOJ 12100 2048
0223 15:21 시작
0223 17:50 끝

3
2 2 2
4 4 4
8 8 8

2 4 16 8
8 4 0 0
16 8 2 0
2 8 2 0

4
2 0 2 0
0 2 2 0
0 0 0 0
0 0 0 0

4
2 64 2 0
0 2 0 0
0 0 0 0
0 0 0 0

4
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
"""
### PRE-DEFINITION ###
N = int(input())
grid = []
directions = [(1,0),(0,1),(-1,0),(0,-1)]
ranges = [range(0,N), range(N-1,-1,-1)]

answer = 0
for i in range(N):
    grid.append(list(map(int,input().split())))
    answer = max(answer, max(grid[-1]))

def gridCopy(grid):
    r = []
    for g in grid:
        r.append(g.copy())
    return r
# [1,1,4,2,2,8]
def makeRow(numbers):
    global answer
    row = []
    i =0
    while i < len(numbers):
        if i+1 < len(numbers) and numbers[i+1] == numbers[i]:
            row.append(numbers[i]*2)
            answer = max(answer, numbers[i]*2)
            i+=1
        else:
            row.append(numbers[i])
        i+=1
    while len(row) < N:
        row.append(0)
    return row

def moveSum(grid, direction):
    # 가장 큰 블록
    # 방향 맞춰 더하기
    for t in range(N):
        numbers = []
        for i in ranges[direction//2]:
            if direction%2 == 0 and grid[t][i] > 0:
                numbers.append(grid[t][i])
            elif direction%2 == 1 and grid[i][t] > 0:
                numbers.append(grid[i][t])
        row = makeRow(numbers)
        # print(f't{t}- ',row)
        for i in ranges[direction//2]:
            if direction%2 == 0:
                grid[t][i] = row[i]
            elif direction%2 == 1:
                grid[i][t] = row[N-1-i]
def printGrid(grid):
    for g in grid:
        print(g, end=' ')
        print()
def getOrders(cur,dgrid):
    if cur >= 5 : # 5
        return

    for i in range(4):
        _grid = gridCopy(dgrid)
        moveSum(_grid, i)
        # print('   '*cur,'direction: ', directions[i])
        # printGrid(_grid)
        getOrders(cur+1, _grid)
# print('--start--')
getOrders(0,grid)

print(answer)