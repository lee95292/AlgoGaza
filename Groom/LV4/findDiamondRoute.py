n = input()
n = int(n)

route = []

for i in range(1, n):
    route.append(list(map(int, input().split())))

for i in range(n, 0, -1):
    route.append(list(map(int, input().split())))


for i in range(1, n):
    lroute = len(route[i])-1
    route[i][0] = route[i-1][0]+route[i][0]
    route[i][lroute] = route[i-1][lroute-1]+route[i][lroute]
    for j in range(1, lroute):
        route[i][j] = max(route[i][j]+route[i-1][j-1],
                          route[i][j]+route[i-1][j])

for i in range(n, 2*n-1):
    lroute = len(route[i])
    for j in range(lroute):
        route[i][j] = max(route[i][j]+route[i-1][j],
                          route[i][j]+route[i-1][j+1])

# print(route)

print(route[2*n-2][0])
