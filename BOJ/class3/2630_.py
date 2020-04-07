n = int(input())
ww=[0]
arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))
def recurs(a,b,n):
    if(n==1):
        return 1
    flag=True
    for i in range(b,b+n):
        if(arr[b][a:(a+n)] != [1]*n and arr[b][a:(a+n)] != [0]*n):
            flag=False
            break
    
    if(flag):
        if(arr[a][b] ==1):
            ww[0]=ww[0]+1
        return 1
    else:
        n=n//2
        res=recurs(a,b,n) + recurs(a+n,b,n) + recurs(a,b+n,n) + recurs(a+n,b+n,n)
        return res


print(recurs(0,0,n)-ww[0]-1)
print( ww[0]+1)