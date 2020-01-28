# 리스트로 주어진 연결리스트에서 BFS
def listBFS():

    llist = []
    visited = []

    def BFS(k):
        if(visited[k] == 1):
            return k
        else:
            visited[k] = 1

        for i in llist[k]:
            if(visited[k] == 1):
                continue
            q.append(i)

        BFS(q.pop(0))
