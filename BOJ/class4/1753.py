"""
1753 최단경로
다익스트라 Dijkstra 문제!
heapq의 우선순위는 dist[n]을 넣어주어야 함
"""
import  sys
import heapq
input = sys.stdin.readline

v,e = list(map(int,input().split()))
st = int(input())

graph = [ [] for _ in range(v+1)]
INF = 2000001
dist = [INF]*(v+1)

for i in range(e):
    a,b,f = list(map(int,input().split()))
    graph[a].append([b,f])

que = []
heapq.heappush(que,[0,st])
dist[st] = 0

while que:
    weight,now = heapq.heappop(que)

    for node in graph[now]:
        n, node_weight = node
        cost = dist[now] + node_weight
        if cost < dist[n]:
            dist[n] = cost
            heapq.heappush(que, [cost,n])

for d in dist[1:]:
    if d == INF:
        print('INF')
    else:
        print(d)
"""
5 6
1
5 1 1
1 2 2
1 3 3
2 3 4
2 4 5
3 4 6
"""