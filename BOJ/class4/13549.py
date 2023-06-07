"""
REDO
13549 순간이동. 
단순 BFS가 아니라, 이동에 우선순위가 있어, 우선순위 큐를 이용하던가 deque에서 appendleft를 사용해 풀어야하는 문제.
경계값 조건도 까다롭고, BFS로 풀리지 않아 많이 헤맸음.
다시 공부해볼것. : 우선순위 큐로 풀어보자.
"""
from collections import deque

a,b= list(map(int,input().split()))

max = 100001
dp = [max] * max
visit = [0] * max
dp[a] = 0

que = deque()
que.append(a)
while que:
    v = que.popleft()
    if v*2 < max and visit[v*2] == 0:
        dp[v*2] = min(dp[v], dp[v*2])
        que.appendleft(v*2)
        visit[v*2] = 1
    for i in [v-1,v+1]:
        if 0<= i <max and visit[i] == 0:
            dp[i] = min(dp[v]+1, dp[i])
            que.append(i)
            visit[i] = 1

    if b in [v-1, v+1, v*2]:
        print(dp[b])
        break

"""
3 5 => 1
4 6 => 1
"""