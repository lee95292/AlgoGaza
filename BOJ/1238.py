"""
1238번 파티 
모든 인덱스에서 X, X에서 모든 인덱스까지의 최소거리를 구해야하므로
플로이드 와샬 알고리즘이 가장 먼저 떠오르지만, node가 1000개이므로, 플로이드 와샬은 시간초과 (n**3)

우선순위큐를 사용한 다익스트라를 이용해야만 시간내에 통과 가능
"""
import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

n,m,x = list(map(int,input().split()))
x-=1
graph = [[] for i in range(n)]

dists = [[INF]*n for i in range(n)]
for i in range(m):
    a,b,f = list(map(int,input().split())) 
    a,b = a-1,b-1
    graph[a].append([b,f])
    dists[a][b] = f

def dijkstra(st):
    dist = [INF]*n
    visit = [False]*n
    q = []
    heapq.heappush(q,[0,st])
    dist[st] = 0
    while q:
        f,y = heapq.heappop(q)
        visit[y] = True
        for i in graph[y]:
            cost = i[1] + dist[y]
            if not visit[i[0]] and cost < dist[i[0]]:
                dist[i[0]] = cost
                heapq.heappush(q,[cost,i[0]])
    return dist


fromx = dijkstra(x)

maxv=0
for i in range(n):
    ito = dijkstra(i)
    maxv = max(maxv, ito[x] + fromx[i])
print(maxv) 



""""
플로이드 와샬 풀이. O(n**3) 으로 시간초과
for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j: continue
            dists[i][j] = min(dists[i][j],dists[i][k] + dists[k][j])

maxv = 0
for i in range(n):
    if i == x : continue
    maxv = max(maxv, dists[i][x] + dists[x][i])
print(maxv)
""""