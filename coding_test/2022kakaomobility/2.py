def solution(id_list, k):
    couponDict = {}
    answer = 0
    for dailyPurchaceList in id_list:
        purchaces = list(set(dailyPurchaceList.split(" ")))
        for p in purchaces:
            if couponDict.get(p) == None:
                couponDict[p] = 1
            else:
                couponDict[p] +=1
    for coupKey in couponDict.keys(): 
        if couponDict[coupKey] > k : 
            answer+=k
        else:
            answer += couponDict[coupKey]
    return answer

print(solution(
["A B C D", "A D", "A B D", "B D"], 2))