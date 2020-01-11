def solution(n, lost, reserve):
    answer = n
    coex = set(lost) & set(reserve)
    lost = list(set(lost)-set(coex))
    reserve = list(set(reserve)-set(coex))
    for i in range(0, len(reserve)):
        if reserve[i]-1 in lost:
            lost.remove(reserve[i]-1)
            continue
        if reserve[i]+1 in lost:
            lost.remove(reserve[i]+1)
            continue

    return answer-len(lost)


print(solution(5, [2, 4], [1, 3, 4]))
