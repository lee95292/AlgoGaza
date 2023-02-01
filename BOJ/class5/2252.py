"""
백준 클래스5 2252,줄세우기 위상정렬 Topological Sort
"""
from collections import deque
import sys
input=sys.stdin.readline
N, M = map(int,input().split())

graph = [[] for _ in range(N)]
indegree =[0 for _ in range(N)]
for i in range(M):
    x,y = list(map(int,input().split()))
    graph[x-1].append(y-1)
    indegree[y-1] += 1
que = deque([])
for i in range(N):
    if indegree[i] == 0:
        que.append(i)
answer = []
while que :
    elem = que.popleft()
    answer.append(elem+1)
    for node in graph[elem]:
        indegree[node]-=1
        if indegree[node] == 0 :
            que.append(node)
            indegree[node] = -1

print(*answer)