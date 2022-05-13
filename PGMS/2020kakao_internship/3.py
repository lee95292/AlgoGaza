


def solution(gems):
    count={}
    for g in set(gems):
        count[g] = 0

    s = 0
    v = set()
    ra = []
    for e in range(len(gems)):
        v.add(gems[e])
        count[gems[e]] += 1
        while count[gems[s]] > 1 and s < e:
            count[gems[s]]-=1
            s+=1
        if len(v) == len(count):
            ra.append([s+1,e+1])
    min = 1000001
    answer =[]
    for r in ra:
        if r[1] - r[0] < min:
            min = r[1]-r[0]
            answer = r
    return answer


#gems=["AA", "AB", "AC", "AA", "AC"]
gems=["XYZ", "XYZ", "XYZ"]
gems=["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]

gems = ["1","2","2","2","3","2","3","3","1","1"]
print(gems)
print(solution(gems))