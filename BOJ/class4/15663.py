n,m = list(map(int,input().split()))

arr = list(map(int,input().split()))
arr.sort()

answer = []


def bt(get, origin,k):
    if k == m:
        answer.append(get)
        return
    if len(origin) == 0 :
        return

    for i,v in enumerate(origin):
        bt([*get,v],[*origin[:i], *origin[i+1:]],k+1)

bt([],arr,0)
answer.sort()
tmp = []
for a in answer:
    if a == tmp:
        continue
    print(*a,end=' ')
    print()
    tmp = a