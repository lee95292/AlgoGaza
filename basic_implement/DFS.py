def listDFS(llist):
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
