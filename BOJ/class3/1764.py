n,m = list(map(int,input().split()))

nlist=[]
for i in range(n+m):
    nlist.append(input())


aset = set(nlist[0:n])
bset = set(nlist[n:n+m])

ans = sorted(list(aset & bset))

print(len(ans))

for i in ans:
    print(i)