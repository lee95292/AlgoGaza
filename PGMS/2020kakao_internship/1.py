numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
numbers=[7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2] #LRLLRRLLLRR
hand = "left"	
answer = ''
#LRLLLRLLRRL

loc = [[] for _ in range(10)]
loc[0] =[3,1]

idx = 1
for i in range(3):
    for j in range(3):
        loc[idx] = [i,j]
        idx+=1
leftloc = [3,0]
rightloc = [3,2]

for idx,l in enumerate(loc):
    print(idx, l)
for number in numbers:
    flag = "L"
    if number in [1,4,7]:
        flag = "L"
    elif number in [3,6,9]:
        flag ="R"
    else:
        leftdist = abs(leftloc[0] - loc[number][0]) + abs(leftloc[1] - loc[number][1])
        rightdist = abs(rightloc[0] - loc[number][0]) + abs(rightloc[1] - loc[number][1])

        if leftdist == rightdist:
            if hand == "right":
                flag = "R"
            else:
                flag = "L"
        elif leftdist < rightdist:
            flag = "L"
        else:
            flag = "R"
    
    if flag == "L":
        leftloc = loc[number]
    if flag == "R":
        rightloc = loc[number]
    print(number, flag, leftloc, rightloc)
    answer= answer + flag

print(answer)