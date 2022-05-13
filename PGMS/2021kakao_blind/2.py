from itertools import combinations

def solution(orders, course):
    answer=[]
    for num in course:
        combineCount = {}
        for order in orders:
            for i in combinations(order,num):
                c=''
                i = sorted(list(i))
                for j in i:
                    c +=j 
                if combineCount.get(c):
                   combineCount[c] += 1
                else:
                    combineCount[c] = 1
        
        maxCnt = 1
        result =[]
        for key in combineCount:
            if combineCount[key] < 2:
                continue
            if maxCnt < combineCount[key]:
                result = []
                maxCnt = combineCount[key]
                result.append(key)
            elif maxCnt == combineCount[key]:
                result.append(key)

        answer.extend(result)
    answer.sort()
    return answer


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4]))