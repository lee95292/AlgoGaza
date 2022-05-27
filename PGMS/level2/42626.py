import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    flag = False
    while scoville[0] < K:
        if len(scoville) < 2:
            flag = True
            break
        l1,l2  = heapq.heappop(scoville), heapq.heappop(scoville)
        heapq.heappush(scoville, l1 + l2*2)
        heapq.heapify(scoville)
        answer +=1

    if flag:
        answer = -1
    return answer


print(solution([1, 2, 3, 9, 10, 12],7))