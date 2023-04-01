from collections import deque
N = int(input())
sectionMap = {} # i->(x,y)
sidx = 0
graph=[]
def canGo(x1,y1,x2,y2):
    if x2< x1 < y2 or x2 < y1 <y2: return True
    return False

def findRoute(a,b):
    destx,desty = sectionMap[b]
    visit = [False]*len(graph)
    que = deque([a])
    while que:
        cur = que.popleft()
        srx,sry = sectionMap[cur]
        if canGo(srx,sry,destx,desty): return True
        visit[cur] = True
        for node in graph[cur]:
            if visit[node]: continue
            que.append(node)
    return False

for i in range(N):
    o, x, y = map(int,input().split())
    x,y= x-1,y-1

    if o == 1:
        sectionMap[sidx]=(x,y)
        graph.append([])
        for s in range(sidx):
            if canGo(sectionMap[s][0],sectionMap[s][1],x,y):
                graph[s].append(sidx)
            if canGo(x,y,sectionMap[s][0],sectionMap[s][1]): 
                graph[sidx].append(s)
        sidx+=1
    if o == 2:
        if findRoute(x,y): print(1)
        else: print(0)
    # print(sectionMap)
    # print(graph)
