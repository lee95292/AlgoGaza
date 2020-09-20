tc = int(input())

for i in range(tc):
    x, y, n = list(map(int, input().split()))
    pointArr = [[0 for i in range(y)] for j in range(x)]
    points = []
    graph = {}
    for i in range(n):
        points.append(list(map(int, input().split())))
        graph[(points[0],points[1])] = []
        pointArr[x][y] = 1

    def getAdj(p):
    for p in points:
        p.append(getAdj(p))
