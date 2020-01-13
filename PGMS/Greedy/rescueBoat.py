def solution(people, limit):
    answer = 0

    people.sort()
    people.reverse()
    stack=[]

    for i in range(0,len(people)):
        if(len(stack)==0):
            stackSum=people[i]
        else:
            stackSum=stack[len(stack)-1]
        flag=False
        for j in range(i,len(people)):
            stackSum+=people[j]
            if(stackSum<=limit):
                i=j
                flag=True
            else:
                stackSum-=people[j]
                break

        if(not flag):
            stack.append(people[i])
        else:
            stack.pop(len(stack)-1)
            k=0
            for i in range(len(stack)-1,-1,-1):
                if(stack[i]>stackSum):
                    k=i
                    break
            stack.insert(k,stackSum)
    return len(stack)

print(solution([70,40],100))