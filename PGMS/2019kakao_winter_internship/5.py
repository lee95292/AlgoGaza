import math
stones = [7,6,5,6,7,8,3,3,3,7,7,8,9,3,3,3,4,5,6]
stones = [1,2,3,4,5,6,7,8,9]
stones = [2,2,2,2,9,8,7,6,5,4,3,3,4,3,3,4]
stones = [10,1,1,3,1,1,7,8,9]
stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]	
k=3


flag = True

minVal=1
maxVal=2000000000
mid = math.floor((minVal +maxVal)/2)

# O(n)
while minVal <= maxVal:
    mid = (minVal + maxVal)//2
    cnt=0
    temp = stones.copy()
    for st in temp:
        if st <= mid:
            cnt = cnt+1
        else:
            cnt = 0
        if cnt>=k:
            break
    if cnt >= k:
        maxVal = mid-1
    else:
        minVal = mid+1

print(minVal)


