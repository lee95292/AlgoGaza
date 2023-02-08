"""
백준 class5, 음악 프로그램
Topological Sort
"""
import sys
input = sys.stdin.readline
from collections import deque
N,M = map(int,input().split())
orders = [[] for _ in range(N)]
inDegree = [0] * N
for _ in range(M):
    order = list(map(lambda x: int(x)-1,input().split())) 
    for i in range(1,order[0]+2):
        if i > 1:
            inDegree[order[i]] +=1
        if i +1 < order[0]+2:
            orders[order[i]].append(order[i+1])
que = deque()
answer = []
for i in range(N):
    if inDegree[i] == 0:
        que.append(i)
    
while que:
    cur = que.popleft()
    answer.append(cur+1)

    for node in orders[cur]:
        inDegree[node]-=1
        if inDegree[node] == 0:
            que.append(node)

if len(answer) == N:
    print(*answer, end=' ')
else:
    print(0)