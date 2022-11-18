"""
문제.
0 < times <= 100,000
0 < n <= 1,000,000,000
n명의 심사대상, 심사관 i는 time[i]만큼 심사시간 소요
최소 심사시간 return

Solution 1. priority que 방법: 시간초과 
que에는 다음 사람이 심사를 받았을 때, 걸리는 총 시간이 있음
que에서 숫자가 가장 작은 심사관을 꺼내 시간 추가 후 heapify

= n * log(len)


Solution 2. 이분탐색 방법 :

left: 0, right: n * max(times)로 구성, 
mid만큼의 시간동안 처리할 수 있는 사람 수 구함: sum (mid // times)

사람 수가 너무 많거나 적으면, low,high 조정
"""
import heapq

def solution_pq(n, times):
    que = []
    
    for idx,time in enumerate(times):
        que.append([time, idx])

    heapq.heapify(que)
    for i in range(n):
        que[0][0] += times[que[0][1]]
        heapq.heapify(que)
    
    answer = 0
    for val in que:
        time, idx = val
        answer = max(answer, time-times[idx])    
    return answer


def solution(n, times):
    answer = n * max(times)
    low, high = 0, n * max(times)

    while low <= high:
        mid = (low+high) // 2
        # maxNum: mid시간동안 처리할 수 있는 사람 수의 합
        maxNum = sum([mid//time for time in times])

        if maxNum >= n:
            answer = min(answer, mid)
            high = mid-1
        elif maxNum < n:
            low = mid+1


    return answer
# print(solution(6, [7,10]))
# print(solution(6, [10,1]))
print(solution(6, [2,5]))
# 6	[10, 1]	6
# 6	[2, 5]	10