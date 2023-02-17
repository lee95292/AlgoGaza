"""
BOJ 13023 골드5 ABCDE 
방문초기화 + DFS
1. 사이클이 있는 그래프이므로 탐색을 완료한 가지에 대해서는 방문을 초기화.
2. 깊이가 4 이상이면 프로그램 종료 후 정답 출력하므로, 최악 시간복잡도 O(4*N)
5 4
0 1
1 2
2 3
3 4


7 8
0 1
1 4
4 5
0 2
2 3
3 4
0 6
6 4
"""
import sys
input = sys.stdin.readline
N,M = map(int,input().split())
graph = [[] for _ in range(N)]
for i in range(M):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

visit = [0 for _ in range(N)]
def dfs(i, depth):
    if visit[i] == 1:
        return
    
    if depth == 4:
        print(1)
        sys.exit()
    visit[i] = 1
    for node in graph[i]:
        dfs(node,depth+1)
    visit[i] -=1
for v in range(N):
    dfs(v,0)
print(0)