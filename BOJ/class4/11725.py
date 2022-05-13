from collections import deque

n = int(input())
visit = [0] * (n+1)
parent = [0] * (n+1)
graph = [[] for _ in range(n+1)]

for i in range(n-1):
    a,b = list(map(int,input().split()))
    graph[b].append(a)
    graph[a].append(b)

que = deque([])
que.append(1)
visit[1] = 1
while que:
    x = que.popleft()
    
    for el in graph[x]:
        if visit[el] == 1:
            continue
        parent[el] = x
        visit[el] = 1
        que.append(el)
for p in parent[2:]:
    print(p)