import heapq
import sys
input = sys.stdin.readline
INF= 100000  * 10001
n = int(input())
graph = [[] for _ in range(n+1)]
for i in range(n):
    arr = list(map(int,input().split()))
    for t in range((len(arr)-1)//2):
        graph[arr[0]].append([arr[2*t+1], arr[2*t+2]])

def dijkstra(k):
    dist = [INF] * (n+1)
    visit = [False] *(n+1)
    que = [(0,k)]
    dist[k] = 0
    visit[k] = True

    while que:
        _,now = heapq.heappop(que)

        for node in graph[now]:
            v,w = node
            if visit[v] == True:
                continue
            heapq.heappush(que,(w,v))
            visit[v] = True
            dist[v] = min(dist[now]+w, dist[v])

    return dist


i1, d1 = -1,-1
for idx,dist in enumerate(dijkstra(1)[1:]):
    if d1 < dist:
        i1 = idx
        d1 = dist

print(max(dijkstra(i1+1)[1:]))
"""
4
1 2 5 3 9 -1
2 1 5 -1
3 1 9 4 8 -1
4 3 8 -1

답 : 22

6
1 2 3 -1
2 1 3 5 3 3 5 -1
3 2 5 4 7 -1
4 3 7 -1
5 2 3 6 5 -1
6 5 5 -1

답 : 20

4
1 2 7 3 2 -1
2 1 7 -1
3 1 2 4 3 -1
4 3 3 -1

답 : 12

5
1 2 7 3 2 5 10 -1
2 1 7 -1
3 1 2 4 3 -1
4 3 3 -1
5 1 10 -1

답 : 17"""