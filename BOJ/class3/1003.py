n = int(input())

fnum = []

for i in range(n):
    fnum.append(int(input()))

fpair = [[1,0],[0,1]]

for i in range(2,max(fnum)+1):
    fpair.append([fpair[i-1][0]+fpair[i-2][0],fpair[i-1][1]+fpair[i-2][1]])

for i in fnum:
    print(fpair[i][0],fpair[i][1])