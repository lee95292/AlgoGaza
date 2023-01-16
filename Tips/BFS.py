# 리스트로 주어진 연결리스트에서 BFS
# 0
# 1
# 23
# 45 6
# 7 8 9


"""def listBFS(llist):

    visited = [0 for x in llist]
    q = []

    def BFS(k):
        if(visited[k] == 1):
            return -1
        else:
            visited[k] = 1
            print("visit"+str(k))

        for i in llist[k]:
            if(visited[i] == 1):
                continue
            q.append(i)

        if(len(q) == 0):
            return

        BFS(q.pop(0))

    BFS(0)


listBFS([[1], [0, 2, 3], [1, 4, 5], [1, 6],
         [2, 7], [2, 8], [6, 9], [4], [5], [6]])"""


# 0702 구현
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

from collections import deque
def BFS(st,g):
    que = deque([st])
    visit = [0] * (v+1)
    visit[st] = 1
    res = []
    while que:
        n = que.popleft()
        res.append(n)
        for node in graph[n]:
            if visit[node] == 0 :
                visit[node] = 1
                que.append(node)

    return res

print(BFS(5,graph))


