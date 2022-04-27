import sys
sys.setrecursionlimit(10**6)
k,room_number= 10,[1,3,4,1,3,1]
k, room_number = 10**11, [1]*200000

dset ={}
depth = {}
maxv = {}

answer = []

def find(x):
    if getDictValue(dset,x) == x:
        return x
    return find(dset[x])

def getDictValue(dict, a, setZero=False):
    if dict.get(a) == None:
        if setZero: dict[a] = 0
        else: dict[a] = a
    return dict[a]

def union(a,b):
    ar,br = find(a),find(b)
    if ar == br : 
        return br
    if getDictValue(depth,ar,True) > getDictValue(depth,br,True):
        ar,br= br,ar
    elif getDictValue(depth,ar,True) == getDictValue(depth,br,True):
        depth[br] += 1
    maxv[br] = max(getDictValue(maxv,ar),getDictValue(maxv,br))
    dset[ar] = br

    return br


for num in room_number:
    
    num -=1
    
    root = find(num)
    M = getDictValue(maxv,root)
    answer.append(M+1)
    union(M,M+1)

    # print(depth)
    # print(maxv[1])
print(answer)
