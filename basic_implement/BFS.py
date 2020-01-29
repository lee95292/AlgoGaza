# 리스트로 주어진 연결리스트에서 BFS
# 0
# 1
# 23
# 45 6
# 7 8 9


def listBFS(llist):

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
         [2, 7], [2, 8], [6, 9], [4], [5], [6]])
