inp = """5 1 1
1 2 2
1 3 3
2 3 4
2 4 5
3 4 6"""
import heapq
v,e = 5,6
st = 1
graph = [ [] for _ in range(v+1)]
for line in inp.split('\n'):
    s,e,f = list(map(int, line.split()))
    graph[s].append([e,f])

def dijkstra(g, st):
    que = []
    heapq.heappush(que, [0,st])
    INF = 2000000001
    dist =[INF]*(v+1)
    dist[st] = 0

    while que:
        weight, vtx = heapq.heappop(que)
        for ed, node_weight in g[vtx]:
            cost = dist[vtx] +node_weight
            if cost < dist[ed]:
                dist[ed] = cost
                heapq.heappush(que,[cost, ed])
    return dist
            
    
print(dijkstra(graph,st))