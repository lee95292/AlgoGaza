# 크루스칼 알고리즘
# disjoint set을 이용해 집합 중복여부 판단


def solution(n, costs):
    costs = sorted(costs, key=lambda x: x[2])
    disjoint_set = [x for x in range(0, n)]
    answer = 0

    def union(x, y):
        disjoint_set[find(y)] = find(x)

    def find(x):
        if(x == disjoint_set[x]):
            return x
        else:
            return find(disjoint_set[x])

    for cost in costs:
        if(find(cost[0]) != find(cost[1])):
            union(cost[0], cost[1])
            answer += cost[2]
    return answer


print(solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]))

#
