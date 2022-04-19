"""
15654번 n과 m(5) 백트래킹 문제...
"""
n,m = list(map(int,input().split()))

arr = list(map(int,input().split()))

arr = sorted(arr)


ansIdxs = []
def selectIndex(get,left,k):
    if k == 0:
        ansIdxs.append(get)
        return get
    for idx,val in enumerate(left):
        new_left = [*left[0:idx],*left[idx+1:len(left)]]
        new_get = [*get,val]
        selectIndex(new_get,new_left,k-1)
selectIndex([], arr, m)

for val in ansIdxs:
    print(*val, end=' ')
    print()