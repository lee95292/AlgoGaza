"""
2606 바이러스
N개의 컴퓨터에 대한 네트워크 연결 정보 제공,
간단한 그래프 탐색 문제
"""
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
nv = int(input())

arr = [[] for _ in range(n+1)] 
for _ in range(nv):
    v= list(map(int,input().split()))
    arr[v[0]].append(v[1])
    arr[v[1]].append(v[0])
    
que = deque()

que.extend(arr[1])
visit = [0] * (n+1)
cnt = 0
while len(que)> 0:
    idx = que.popleft()
    if visit[idx] == 1 :
        continue
    visit[idx] = 1
    cnt +=1
    que.extend(arr[idx])

if cnt > 0:
    print(cnt-1)
else:
    print(cnt)
