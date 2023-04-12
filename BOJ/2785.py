N = int(input())
chains = list(map(int,input().split()))
chains.sort()
n = N
n,k = n-1, 0
answer=0
while n > 0:
    if n >= chains[k]+1:
        n-=chains[k]+1
        answer+=chains[k]
        k+=1
    else:
        answer+=n
        break

print(answer)