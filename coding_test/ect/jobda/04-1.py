import heapq

MAX_VALUE = 10000001


def solution(n, m, k, u, v, l):
    adj = [MAX_VALUE] * (n+1)
    graph = [[] for _ in range(n+1)]

    def makeGraph():
        for i in range(m):
            a, b, w = v[i], u[i], l[i]
            graph[a].append([b, w])
            graph[b].append([a, w])

    def dijkstra():
        que = [[0, 0]]
        adj[0] = 0
        while que:
            cw, cur = heapq.heappop(que)

            for [to, w] in graph[cur]:
                if cw + w < adj[to]:
                    adj[to] = cw + w
                    heapq.heappush(que, [adj[to], to])
                    que.append([adj[to], to])

    makeGraph()
    dijkstra()
    print(graph)
    print(adj)
    answer = 0
    return 14

solution(2,3,3,[0,0,1],[1,2,2],[3,2,6])

