"""
1931 회의실 배정
종료시간 기준 정렬, 종료시간이 빠른 순으로 추가하기.  
시작시간도 오른차순으로 정렬해야 함.

2
2 2
0 2

이런식으로 정렬되어있으면 2-2 가 먼저 추가되어, 시작시간이 0인 회의는 고려 제외됨.
"""
import sys
input = sys.stdin.readline

n = int(input())

arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))

arr = sorted(arr, key= lambda x:(x[1],x[0]))
en = 0
cnt=0
for ar in arr:
    if ar[0] >= en:
        en = ar[1]
        cnt= cnt+1
print(cnt)