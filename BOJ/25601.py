import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
N = int(input())

objects = {}
ps = 0
graph = [[] for _ in range(N+1)]
for i in range(N-1):
    a,b = input().split()
    if not objects.get(a): 
        objects[a] = ps
        ps+=1
    if not objects.get(b):
        objects[b]=ps
        ps+=1
    graph[objects[b]].append(objects[a])
a,b = map(objects.get, input().split())

def dfs(x,fnd):
    if len(graph[x])==0:
        return False
    if fnd in graph[x]:
        return True
    for node in graph[x]:
        if dfs(node,fnd): return True
    return False
# print(graph)
# print(objects)
if dfs(a,b) or dfs(b,a):
    print(1)
else:
    print(0)

