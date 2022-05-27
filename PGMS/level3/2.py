def solution(gems):
    sections = []
    count = {}
    inset = set()
    gemsSet = set(gems)
    inset.add(gems[0])

    for gem in gemsSet:
        count[gem] = 0
    st, ed = 0,0
    count[gems[0]]+=1
    if len(inset) == len(gemsSet):
        sections.append([st+1,ed+1])

    while st <= ed :
        if ed +1 < len(gems):
            ed+=1
            count[gems[ed]]+=1
        if count[gems[ed]] == 1:
            inset.add(gems[ed])

        while count[gems[st]] > 1:
            count[gems[st]]-=1
            st+=1
        #print(st,ed,inset,count)
        if len(inset) == len(gemsSet):
            sections.append([st+1,ed+1])
        
        if count[gems[st]] == 1 and ed ==len(gems)-1:
            break

        
    sections = sorted(sections, key = lambda x: (x[1]- x[0], x[0]))
    #print(sections)
    return sections[0]


g1 = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
g2 = ["AA", "AB", "AC", "AA", "AC"]	
g3 =[ "L","A","A","A","R", "XYZ","XYZ","XYZ"]	
g4=["A"]
g5 = ["1","2","2","2","3","2","3","3","1","1"]
g6=["A","A","A"]

print(solution(g5))