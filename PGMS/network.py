import queue

def solution(n, computers):
    visited=[0 for i in range(0,n)]
    q=queue.Queue()
    answer = 0
    
    for i in range(0,n):
        if(visited[i]==1):
            continue
        else:
            q.put(i)
            answer+=1
            
        while q.qsize()>0:
            vidx=q.get()
            visited[vidx]=1
            for j in range(0,n):
                if(i==j):
                    continue
                elif(computers[vidx][j]==1 and visited[j]==0):
                    q.put(j)
    
    return answer


print(solution(3,[[1,1,1],[1,1,1],[1,1,1]]))