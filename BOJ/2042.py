# segment_tree

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n, m, k = list(map(int, input().split()))

arr = [0]
inst = []
for i in range(n):
    arr.append(int(input()))

for i in range(m+k):
    inst.append(list(map(int, input().split())))


segTree = [0 for _ in range(2*n)]


def init(start, end, node):
    if(start == end):
        segTree[node] = arr[start]
        return segTree[node]
    else:
        segTree[node] = init(start, (start+end)//2, node*2) + \
            init((start+end)//2+1, end, node*2+1)
        return segTree[node]


def update(start, end, node, index, diff):
    if(index < start or index > end):
        return
    segTree[node] = segTree[node]+diff
    if(start != end):
        update(start, (start+end)//2, node*2, index, diff)
        update((start+end)//2+1, end, node*2+1, index, diff)


def segSum(start, end, node, a, b):
    if(a > end or b < start):
        return 0
    if(a <= start and b >= end):
        return segTree[node]

    return segSum(start, (start+end)//2, node*2, a, b) +\
        segSum((start+end)//2+1, end, node*2+1, a, b)


init(1, len(arr)-1, 1)

for i in inst:
    if(i[0] == 1):
        update(1, len(arr)-1, 1, i[1], i[2]-arr[i[1]])
        arr[i[1]] = i[2]
    elif(i[0] == 2):
        print(segSum(1, len(arr)-1, 1, i[1], i[2]))

# print(segTree)
