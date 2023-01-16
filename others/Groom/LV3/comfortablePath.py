n = input()
n = int(n)

route = []
for i in range(n):
    route.append(list(map(int, input().split())))

for i in range(1, n):
    route[0][i] = route[0][i-1]+route[0][i]
    route[i][0] = route[i-1][0]+route[i][0]

for i in range(1, n):
    for j in range(1, n):
        route[i][j] = max(route[i-1][j], route[i][j-1])+route[i][j]

# print(route)
print(route[n-1][n-1])
