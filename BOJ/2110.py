"""
BOJ 2110 공유기 설치

이분탐색
경계값 10^6으로 잘못봐서 75%에서 틀림.
경계값 체크 잘하기.... + 반례 만들때 경계값 꼭 넣자
"""

import sys
input = sys.stdin.readline

N,C = map(int,input().split())

locates = []
for i in range(N):
    locates.append(int(input()))
locates.sort()

answer = 0
left, right = 1, 1000000000

def isClose(value):
    toSet= C-1
    dist = 0
    for i,x in enumerate(locates):
        if i == 0: continue
        dist += x-locates[i-1]
        if dist>=value:
            dist = 0
            toSet-=1

        if toSet == 0:
            # print(value,' close True')
            return True
    # print(value,' close False')
    return False

while left <= right:
    mid = (left + right)//2
    # print(left,mid,right)
    if isClose(mid): 
        answer = mid
        left = mid+1
    else: right = mid-1

print(answer)


"""
3 2
1
2
100

5 3
0
15 
22
1000 
1000000
"""