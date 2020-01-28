def solution(n, vertex):
    dist = [20001 for x in range(0, n+1)]
    dist[0] = 0
    dist[1] = 0

    ilist = [[] for x in range(0, n+1)]
    visit = [0 for x in range(0, n+1)]

    for v in vertex:
        ilist[v[0]].append(v[1])
        ilist[v[1]].append(v[0])

    for i in range(1, len(ilist)):
        bfs(i)

        for vtx in ilist[k]:
    return dist.count(max(dist))


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
