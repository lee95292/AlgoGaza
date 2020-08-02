n = int(input())

origin = []
minArr = []
maxArr = []
for i in range(n):
    origin.append(list(map(int,input().split())))

minArr.append(origin[0])
maxArr.append(origin[0])
for i in range(1,n):
    maxArr.append([max(maxArr[0][0:2]) +origin[i][0], max(maxArr[0][0:3])+origin[i][1], max(maxArr[0][1:3])+origin[i][2]])
    minArr.append([min(minArr[0][0:2])+origin[i][0], min(minArr[0][0:3])+origin[i][1], min(minArr[0][1:3])+origin[i][2]])
    maxArr.pop(0)
    minArr.pop(0)
    
    
    
print(max(maxArr[0]),min(minArr[0]))