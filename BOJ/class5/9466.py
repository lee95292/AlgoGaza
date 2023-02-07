"""
3
7
3 1 3 7 3 4 6
8
1 2 3 4 5 6 7 8
5
2 5 4 5 3
"""
"""
DFS를 사용한 풀이방법
1. 모든 학생 목록에 대해 DFS

2- 1 사이클을 찾는데 시간초과가 나는 방법 : finish객체를 초기화할때 n만큼의 시간이 소요되므로, n**2의 시간복잡도. 
    - DFS를 시작 시 finish를 초기화, DFS가 끝나지 않았는데  visited==0, finish==1인 경우, 사이클 시작노드임
2- 2 최적화한 방법 : 

dfs(origin, current):
    base: 
    if visited == 1
    elif finished == 1
        visited <- -1로 하는 Cycle 수행, answer 추가
    elif 혼자 짝인경우 고려하기

    finish[cur] = 1
    dfs()
    visit[cur] = 1
    ---
    visited ==0 

"""
"""
import sys
sys.setrecursionlimit(10**6+1)

T = int(input())
for tc in range(T):
    N = int(input())
    global answer
    answer =0
    students = list(map(lambda x: int(x)-1,input().split()))
    visit = [0 for _ in range(N)]
    finish = []
    def dfs(origin, current):
        global answer
        if visit[current] == 1:
            return
        if visit[current] == -1:
            turn = current
            while True:
                visit[turn] = 1
                answer +=1
                turn = students[turn]
                # print(':',turn)
                if turn == current: break
            return
        if origin == current:
            answer+=1
            visit[origin] = 1
            return
                
        visit[current] = -1
        dfs(origin, students[current])
        visit[current] = 1
        return

    for idx in range(len(students)):
        if visit[idx] == 0: visit[idx] = -1
        else: continue
        dfs(idx,students[idx])
        visit[idx] = 1
    print(N-answer)

"""

"""
Topological Sort를 활용한 방법
Topological Sort란, DAG( 방향성이 있고 사이클이 없는 그래프 )의 정렬을 위한 방법이고, 선수과목 파악 등을 위해 사용된다.
방법으로는,
1) in degree가 0인 노드부터 큐에 넣고
2) queue에서 노드를 빼 그래프에서 삭제시켜 인접노드의 진입차수를 줄이고, 1)의 과정처럼 in degree가 0이 되면 큐에 넣어준다. 
3) queue에서 빠져나오는 순서가 위상정렬 순서이다. 

위상정렬은 DAG에 대해 수행하지만, 사이클이 있는 경우, 사이클의 시작정점은 in degree가 0이 될 수 없기때문에, 탐색 후에도 방문하지 않은 상태로 남아있다. 
이를 이용해 사이클이 아닌 노드의 개수를 판별할 수 있다. ( inDegree == 0 인 경우)
"""
from collections import deque

T = int(input())
for tc in range(T):
    N = int(input())
    students = list(map(lambda x: int(x)-1, input().split()))

    inDegree = [0]*N
    queue = deque([])
    for i in range(N):
        inDegree[students[i]] += 1
    
    for i in range(N):
        if inDegree[i] == 0:
            queue.append(i)
    while queue:
        cur = queue.popleft()
        next = students[cur]
        inDegree[next] -= 1
        if inDegree[next] == 0:
            queue.append(next)
    print(inDegree.count(0))