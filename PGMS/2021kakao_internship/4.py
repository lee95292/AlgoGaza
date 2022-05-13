from collections import deque

def solution(n, start, end, roads, traps):
    start,end= start-1, end-1
    maxv =10000000
    normroad = [[maxv for _ in range(n)] for _ in range(n)]
    traproad = [[maxv for _ in range(n)] for _ in range(n)]
    normvertex = [[] for _ in range(n)]
    trapvertex = [[] for _ in range(n)]

        

    for road in roads:
        x,y,f = road
        x,y = x-1,y-1
        #normroad[x][y], traproad[y][x] = f,f
        normvertex[x].append(y)
        trapvertex[y].append(x)

    
    def dfs(node,traps_,cnt,prev):
        if node == end:
            return cnt+1
        traps_ = traps_.copy()
        vertexes = normvertex
        trap = False
        if node+1 in traps_:
            trap = True
            traps_.remove(node+1)
            vertexes = trapvertex
        
        print(prev+1,node+1, cnt,trap)
        for vertex in vertexes[node]:
            dfs(vertex,traps_,cnt+1,node)
    
    dfs(start,traps,0,start) 
    
    return 0


print(solution(4,1,4,[[1, 2, 1], [3, 2, 1], [2, 4, 1]],[2,3]))