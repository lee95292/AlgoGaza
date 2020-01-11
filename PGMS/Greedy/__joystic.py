def solution(name):
    answer = 0
    nlist = list(name)
    stick = []
    for i in range(0, len(nlist)):
        tmp = ord(nlist[i])-65 if ord(nlist[i])-65 < ord('Z') - \
            ord(nlist[i])+1 else ord('Z')-ord(nlist[i])+1
        stick.append(tmp)
        answer += tmp
    acount = 0
    tmpcount = 0
    left = 0
    right = 0
    for i in range(0, len(nlist)):
        if(stick[i] == 0):
            tmpcount += 1
        else:
            if tmpcount > acount:
                acount = tmpcount
                tmpcount = 0
                right = i
                left = i-acount

    lcount = left+len(nlist)-acount
    rcount = 2*len(nlist)-right-acount-2
    answer += lcount if lcount < rcount else rcount
    return answer


print(solution("JEROEN"))
