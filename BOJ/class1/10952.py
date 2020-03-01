arr = []
while(True):
    tmp = list(map(int, input().split()))
    if(tmp == [0, 0]):
        break
    arr.append(tmp)

for i in arr:
    print(i[0]+i[1])
