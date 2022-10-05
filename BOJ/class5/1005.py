# ACM Craft
# 위상정렬, DP
import sys
import queue

input = sys.stdin.readline

tc= int(input())

for t in range(tc):
    n,k = list(map(int,input().split()))
    wgt = list(map(int,input().split()))
    
    graph=[[] for i in range(n)]
    degree = [0] * n
    maxv=-1
    dp = [maxv]*n
    for i in range(k):
        x,y = list(map(int,input().split()))
        graph[x-1].append(y-1)
        degree[y-1] += 1
    que = queue.Queue()
    w = int(input()) -1

    for i in range(n):
        if degree[i] == 0:
            que.put(i)
            dp[i] = wgt[i]
    while que.qsize() > 0:
        cur = que.get()
        for i in graph[cur]:
            degree[i]-=1
            if degree[i] == 0:
                que.put(i)
            dp[i] = max(dp[i], dp[cur] + wgt[i])

    print(dp[w])







'''
2
4 4
10 1 100 10
1 2
1 3
2 4
3 4
4
8 8
10 20 1 5 8 7 1 43
1 2
1 3
2 4
2 5
3 6
5 7
6 7
7 8
7





1
4 4
10 1 100 10
1 2
1 3
2 4
3 4
4
'''