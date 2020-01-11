def solution(weight):
    weight.sort()
    if(weight[0] != 1):
        return 1

    answer = weight[0]
    for i in range(1, len(weight)):
        if(weight[i] > answer+1):
            return answer+1
        answer += weight[i]
    return answer+1


print(solution([3, 1, 6, 2, 7, 30, 1]))
