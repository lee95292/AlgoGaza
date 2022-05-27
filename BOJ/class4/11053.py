n = int(input())
per = list(map(int,input().split()))

v = [1]*n

for i in range(n-1,-1,-1):
    for j in range(i,n):
        if per[i] < per[j]:
            v[i] = max(v[i], v[j] +1)
            #print(i,j,v[i])

print(max(v))
