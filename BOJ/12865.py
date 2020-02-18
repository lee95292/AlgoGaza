# ---Testcase---
# n, k = 4, 7
# item = [[6, 13], [4, 8], [3, 6], [5, 12]]

# ---Testcase---
import sys
sys.setrecursionlimit(10**6)


n, k = list(map(int, input().split()))

item = []
for i in range(n):
    item.append(list(map(int, input().split())))

state = [0 for x in range(k+1)]

item.sort(key=lambda x: x[0], reverse=True)
# mass : 담을 수 있는 질량 , value : 현재 가치


def DFS(mass, value, rest):
    if(mass < item[n-1][0] or len(rest) == 0):
        return
    for it in rest:
        if(mass >= it[0]):
            if(state[mass-it[0]] < value+it[1]):
                state[mass-it[0]] = value+it[1]
                tmp = [x for x in rest]
                tmp.remove([it[0], it[1]])
                DFS(mass-it[0], value+it[1], tmp)


rr = [x for x in item]
DFS(k, 0, rr)

print(max(state), end='')
