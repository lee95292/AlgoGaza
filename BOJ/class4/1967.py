"""
1967 트리의 지름.
가장 큰 트리의 지름을 찾는 문제. DFS를 통해 순회하면서 트리 자식들의 길이 합을 구해 지름을 구할 수 있다.
DFS문제.
"""
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())

tree ={}

for i in range(n-1):
    p,c,w = list(map(int,input().split()))
    
    if tree.get(p):
        tree[p].append([c,w]) # idx, weight, radius
    else:
        tree[p] = [[c,w]]

#print(tree)
maxRadius = [0]
def traverse(p):
    if tree.get(p) == None:
        return 0

    childs = tree[p]

    st = 0
    nd = 0
    for child in childs:
        c,w = child
        rd = traverse(c)+ w
        if rd >= st:
            nd = st
            st = rd
        elif rd > nd:
            nd = rd

    #print(p, st,nd)
    maxRadius[0] = max(st+nd, maxRadius[0])
    return st

traverse(1)
print(maxRadius[0])


"""

12
1 2 3
1 3 2
2 4 5
3 5 11
3 6 9
4 7 1
4 8 7
5 9 15
5 10 4
6 11 6
6 12 10

6
1 2 1
1 3 1
2 4 1
2 5 1
3 6 1

5
1 2 1
1 3 10
2 4 1
4 5 10

5
1 2 1
2 3 1
3 4 1
4 5 1

5
1 2 3
1 3 4
1 4 5
1 5 6
"""