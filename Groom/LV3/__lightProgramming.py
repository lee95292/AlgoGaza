n, m = list(map(int, input().split()))
lamp = []

for i in range(0, n):
    lamp.append(list(map(int, input().split())))

p = int(input())
pInfo = []
for i in range(0, p):
    pInfo.append(list(map(int, input().split())))

for i in range(0, p):
    if(pInfo[i][0] == 0):
        lamp[pInfo[i][1]-1] = [x ^ 1 for x in lamp[pInfo[i][1]-1]]
    elif(pInfo[i][0] == 1):
        for j in range(0, len(lamp)):
            lamp[j][pInfo[i][1]-1] = lamp[j][pInfo[i][1]-1] ^ 1


for i in range(0, len(lamp)):
    for t in range(0, len(lamp[i])):
        if(t == len(lamp[i])-1):
            print(lamp[i][t])
            continue
        print(lamp[i][t], end=' ')
