import sys
sys.setrecursionlimit(10**6+1)
input = sys.stdin.readline
N = int(input())
tree = [[] for _ in range(N+1)]
dp = [[0,0] for _ in range(1000001)] # 0: early adapter, 1: not
for i in range(N-1):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

visit = [False for _ in range(N+1)]
def dfs(x):
    dp[x][0] = 1
    visit[x]=True
    for node in tree[x]:
        if visit[node]:continue
        dfs(node)
        dp[x][0] += min(dp[node])
        dp[x][1] += dp[node][0]

dfs(1)
if N == 1:
    print(1)
    exit(0)
# print(dp[1:N+1])
print(min(dp[1]))

