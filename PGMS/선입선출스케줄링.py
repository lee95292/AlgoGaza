"""
https://school.programmers.co.kr/learn/courses/30/lessons/12920#
Heap Queue로 풀었는데, 시간초과!
파라메트릭 서치 사용, 통과

# 우선순위 큐  # 이분탐색 # 이진탐색 #파라매트릭 서치
"""

def solution(n, cores):

# Priority Queue, NlogN 실패
#     que = [[0,i] for i,x in enumerate(cores)] # [처리끝나는 시간, 인덱스]

#     while True:
#         # print(que)
#         endTime, idx = heapq.heappop(que)
#         led,lidx = que[0]
#         k = max(1,(led-endTime) // cores[idx])
#         n-= k
#         heapq.heappush(que,[endTime+k * cores[idx] ,idx])
#         if n <= 0 : return idx+1
    if n <= len(cores):
        return 0
    n-=len(cores)
    def isOverN(t):
        compJobs=0
        for c in cores:
            compJobs+=t//c
            if compJobs >= n:
                return True
        return False
    left,right = 0, 10**9
    while left <= right:
        mid = (left+right)//2
        if isOverN(mid):
            right=mid-1
        else:
            left=mid+1

    sc= cores.copy()
    k=0
    for i,x in enumerate(sc):
        k = (left-1)//x
        sc[i] += k*x
        n-=k
    for i in range(len(cores)):
        if sc[i]<=left: n-=1
        if n == 0: return i+1
    return sc[0]+1