"""def listDFS(llist):
    visited = [0 for x in llist]

    def DFS(x):
        if(visited[x] == 1):
            return -1
        else:
            print("visit"+str(x))
            visited[x] = 1

        for node in llist[x]:
            DFS(node)
    DFS(0)


listDFS([[1], [0, 2, 3], [1, 4, 5], [1, 6],
         [2, 7], [2, 8], [6, 9], [4], [5], [6]])
"""

# 220702 구현
inp = """5 1
1 2
1 3
2 3
2 4
3 4"""
v,e = 5,6
graph = [[] for _ in range(v+1)]
for line in inp.split('\n'):
    st, ed = list(map(int,line.split()))
    graph[st].append(ed)
    graph[ed].append(st)

def DFS(st,g):
    stack = []
    stack.append(st)
    visit = [0] *(v+1)
    visit[st] =1
    res = []
    while stack:
        node = stack.pop()
        res.append(node)
        for s in graph[node][::-1]:
            if visit[s] == 0:
                stack.append(s)
                visit[s] = 1
    return res

print(DFS(1,graph))