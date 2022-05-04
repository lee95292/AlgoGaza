"""
2805 나무 자르기
이분탐색문제! (이진탐색, Binary Search)

이분탐색은 경계조건 신경써야하는부분이 많다.
1. 중간값을 반복 맨 밑에서 구해줘야되는부분
2. left, right값 갱신
3. 
"""
import sys
input = sys.stdin.readline
n,m = list(map(int,input().split()))
trees = list(map(int,input().split()))

left = 0 
right = 2000000000
mid = (left+right)//2
while left <= right:
    
    cutlen = 0
    for tree in trees:
        cutlen+= max(0,tree-mid)
    if m > cutlen:# 적정보다 적게 자름
        right = mid-1
    elif m < cutlen:#많이자름
        left = mid+1
    else:
        break
    mid = (left + right) // 2


print(mid)

"""
5 2000000000 
900000000 900000000 900000000 900000000 900000000

2 1
100 100
99

2 10
10 10
5

2 1
1 1
0
"""
        


