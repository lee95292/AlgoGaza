def solution(budgets, M):
    budgets.sort()
    budgetSum=[]
    lb=len(budgets)

    for i in range(0,lb):
        if(i==0):
            budgetSum.append(budgets[i])
            continue
        budgetSum.append(budgetSum[i-1]+budgets[i])

    predicate=0
    maxIndex=0

    for i in range(lb-1,-1,-1):     #1
        predicate=budgetSum[i]+budgets[i]*(lb-1-i)
        if(predicate<=M):
            maxIndex=i
            break

    if(maxIndex>=lb-1):             # E
        return budgets[lb-1]
    for i in range(budgets[maxIndex],budgets[maxIndex+1]+1): #2
        if(budgetSum[maxIndex]+i*(lb-maxIndex-1)>M):
            if(budgets[0]>=i):
                return M//lb
            return i-1

    return budgets[lb-1]


print(solution([120,110,140,150],485)) # 484
print(solution([6,5,4,3,7],20)) # 19
print(solution([100,100,100,100,100],100)) # 20


# Sort
# 이전 인덱스까지의 총합으로 이루어진 budgitSum 구함 :1
# maxIndex구함 : maxIndex 이후 값들을 상한으로 두고 더해도 M값을 초과하지 않는 maxIndex
# budgit의 maxIndex부터 1씩 증가하면서 최대 예산값 구함. :2


