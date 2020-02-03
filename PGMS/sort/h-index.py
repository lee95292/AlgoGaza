def solution(citations):
    citations.sort()
    citations.reverse()
    answer = 1
    lc = len(citations)
    for i in range(0, lc):
        h = citations[i]
        # print(h, i+1)
        if(h < i+1):
            answer = i
            break
        answer = i+1
    return answer


print(solution([1, 0, 3, 5, 6]))
print(solution([100, 1, 1, 1, 1, 0]))
print(solution([1, 1, 1, 0]))
