n,m = list(map(int,input().split()))

arr = list(map(int,input().split()))
arr.sort()

answer = []


def bt(get, idx,k):
    if k == m:
        answer.append(get)
        return
    if idx >= n :
        return

    for i,v in enumerate(arr[idx:]):
        bt([*get,v],i+idx,k+1)

bt([],0,0)
print(answer)
answer.sort()
tmp = []
for a in answer:
    if a == tmp:
        continue
    print(*a,end=' ')
    print()
    tmp = a