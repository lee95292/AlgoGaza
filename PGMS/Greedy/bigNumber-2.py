def solution(number, k):
    initialList = [int(x) for x in number]
    initialListLen = len(initialList)
    sortedList = initialList.copy()
    sortedList.sort()
    setList = set(sortedList)
    for i in range(9, -1, -1):
        if(i not in setList):
            continue

        count = sortedList.count(
            i)-countLatest(initialList, initialListLen, initialListLen-k, i)


def countLatest(numList, en, r, k):

    return answer

# k=0, k=initial len
