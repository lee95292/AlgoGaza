def solution(weight):
    weight.sort()
    answer = 1
    for i in range(1, len(weight)):
        if(weight[i] > answer+1):
            return answer+1
        answer += weight[i]
    return answer+1


print(solution([3, 1, 6, 2, 7, 30, 1]))

# 저울추들을 무게별로 정렬 (O nlogn)
# A(n+1)번째 저울추를 A(1)~A(n) 까지의 저울추로 측정할 수 없으면 fail (O n)
