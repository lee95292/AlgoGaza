def solution(number, k):
    initList = [int(x) for x in number]
    initListLen = len(initList)
    if(k == initListLen):
        return "0"
    answer = maxNumber(initList, 0, initListLen, initListLen-k)
    return str(answer)


def maxNumber(li, st,  en, r):
    if(r == 1):
        return li[listMax(li, st, en)]
    startIndex = listMax(li, st, en - r+1)+1
    subMax = li[startIndex-1]
    return pow(10, r-1)*subMax+maxNumber(li, startIndex, en, r-1)


def listMax(li, st, en):
    max = -1
    index = -1
    for i in range(st, en):
        if(max < li[i]):
            max = li[i]
            index = i
    return index


print(solution('10010', 1))
# 0~ n-k 까지의 원소 중 최대값 판별 : index i
# i~ n-k-r 로 재귀 : r은 자리수
