def solution(n, costs):
    costs = sorted(costs, key=lambda x: x[2])
    answer = 0
    linkedList = [[] for x in range(0, n)]
    for i in range(0, n):
        linkedList[costs[i][0]].append([costs[i][1], costs[i][2]])
        linkedList[costs[i][1]].append([costs[i][0], costs[i][2]])

    graph = [].append(linkedList[0])
    graphSize = len(graph)
    while graphSize < n:
        graph
        graphSize = len(graph)
    return answer


print(solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]))

#
